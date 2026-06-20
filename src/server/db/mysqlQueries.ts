/**
 * MySQL queries — drop-in replacement for src/server/db/queries.ts
 *
 * 使用方式：在 server-actions.ts 中将 import 切换到本文件
 * import { listPeople, ... } from '@/server/db/mysqlQueries';
 *
 * 所有查询通过 MySQL 连接池执行，支持 JSON 列（person_ids, tags 等）
 */
import 'server-only';
import pool, { parseJsonArray } from '@/server/db/mysql';
import type {
  Person,
  HistoricalEvent,
  Source,
  Region,
  DataStatus,
} from '@/lib/types';
import type { RowDataPacket, ResultSetHeader } from 'mysql2';

// Re-export MySQL pool for direct access
export { pool };

// ==================== Type mappers ====================

function mapPerson(row: RowDataPacket): Person {
  return {
    id: row.id, name: row.name,
    nameEn: row.name_en ?? undefined,
    alternativeNames: parseJsonArray(row.alternative_names),
    birthYear: row.birth_year ?? undefined,
    deathYear: row.death_year ?? undefined,
    birthDatePrecision: (row.birth_date_precision ?? 'year') as Person['birthDatePrecision'],
    deathDatePrecision: (row.death_date_precision ?? 'year') as Person['deathDatePrecision'],
    regionId: row.region_id ?? undefined,
    civilizationId: row.civilization_id ?? undefined,
    occupations: parseJsonArray(row.occupations),
    tags: parseJsonArray(row.tags),
    tagsEn: parseJsonArray(row.tags_en),
    summary: row.summary ?? undefined,
    summaryEn: row.summary_en ?? undefined,
    description: row.description ?? undefined,
    descriptionEn: row.description_en ?? undefined,
    sourceIds: parseJsonArray(row.source_ids),
    wikidataQid: row.wikidata_qid ?? undefined,
    wikipediaPageId: row.wikipedia_page_id ?? undefined,
    wikipediaSlug: row.wikipedia_slug ?? undefined,
    dataStatus: (row.data_status ?? 'imported') as DataStatus,
    confidenceScore: Number(row.confidence_score ?? 0.5),
    externalReferences: [],
    lastReviewedAt: row.last_reviewed_at ?? undefined,
    reviewedBy: row.reviewed_by ?? undefined,
  };
}

function mapEvent(row: RowDataPacket): HistoricalEvent {
  return {
    id: row.id, title: row.title,
    titleEn: row.title_en ?? undefined,
    startYear: row.start_year ?? undefined,
    endYear: row.end_year ?? undefined,
    startDateText: row.start_date_text ?? undefined,
    endDateText: row.end_date_text ?? undefined,
    approximateDateText: row.approximate_date_text ?? undefined,
    datePrecision: (row.date_precision ?? 'year') as HistoricalEvent['datePrecision'],
    isApproximate: Boolean(row.is_approximate),
    regionId: row.region_id ?? undefined,
    civilizationId: row.civilization_id ?? undefined,
    placeName: row.place_name ?? undefined,
    placeNameEn: row.place_name_en ?? undefined,
    coordinates: (() => {
      if (!row.coordinates) return undefined;
      if (typeof row.coordinates === 'object') return row.coordinates;
      try { return JSON.parse(row.coordinates as string); } catch { return undefined; }
    })(),
    personIds: parseJsonArray(row.person_ids),
    tags: parseJsonArray(row.tags),
    tagsEn: parseJsonArray(row.tags_en),
    importance: (row.importance ?? 2) as 1 | 2 | 3 | 4 | 5,
    summary: row.summary ?? undefined,
    summaryEn: row.summary_en ?? undefined,
    description: row.description ?? undefined,
    descriptionEn: row.description_en ?? undefined,
    sourceIds: parseJsonArray(row.source_ids),
    relatedEventIds: parseJsonArray(row.related_event_ids),
    wikidataQid: row.wikidata_qid ?? undefined,
    wikipediaPageId: row.wikipedia_page_id ?? undefined,
    wikipediaSlug: row.wikipedia_slug ?? undefined,
    dataStatus: (row.data_status ?? 'published') as DataStatus,
    confidenceScore: Number(row.confidence_score ?? 0.5),
    externalReferences: [],
    lastReviewedAt: row.last_reviewed_at ?? undefined,
    reviewedBy: row.reviewed_by ?? undefined,
  };
}

function mapRegion(row: RowDataPacket): Region {
  return {
    id: row.id, name: row.name,
    nameEn: row.name_en ?? undefined,
    slug: row.slug,
    parentRegionId: row.parent_region_id ?? undefined,
    description: row.description ?? undefined,
    descriptionEn: row.description_en ?? undefined,
  };
}

// ==================== Read operations ====================

export async function listPeople(opts?: {
  publishedOnly?: boolean;
  dataStatus?: string;
  regionId?: string;
  query?: string;
  /** Alternative script variant of the query (simplified↔traditional) */
  queryAlt?: string;
  era?: { min: number; max: number | null };
  page?: number;
  limit?: number;
}): Promise<{ items: Person[]; total: number }> {
  const conditions: string[] = [];
  const params: unknown[] = [];

  if (opts?.publishedOnly) {
    conditions.push('data_status = ?'); params.push('published');
  }
  if (opts?.dataStatus && opts.dataStatus !== 'all') {
    conditions.push('data_status = ?'); params.push(opts.dataStatus);
  }
  if (opts?.regionId && opts.regionId !== 'all') {
    conditions.push('region_id = ?'); params.push(opts.regionId);
  }
  // Simplified/Traditional common char mapping (embedded here to avoid import issues)
  const SC_TC_MAP: Record<string, string> = {
    '万':'萬','与':'與','专':'專','东':'東','丝':'絲','两':'兩','严':'嚴','个':'個','丰':'豐',
    '临':'臨','为':'為','丽':'麗','举':'舉','么':'麼','义':'義','乌':'烏','乐':'樂','乔':'喬',
    '习':'習','乡':'鄉','书':'書','买':'買','乱':'亂','争':'爭','于':'於','亏':'虧','云':'雲',
    '亚':'亞','产':'產','亲':'親','亿':'億','仅':'僅','从':'從','仓':'倉','仪':'儀','们':'們',
    '价':'價','众':'眾','优':'優','会':'會','传':'傳','伤':'傷','伦':'倫','伪':'偽','体':'體',
    '余':'餘','佣':'傭','侦':'偵','侧':'側','侨':'僑','儿':'兒','兑':'兌','党':'黨','兰':'蘭',
    '关':'關','兴':'興','养':'養','兽':'獸','内':'內','册':'冊','写':'寫','军':'軍','农':'農',
    '冯':'馮','冲':'衝','决':'決','况':'況','冻':'凍','净':'淨','凉':'涼','减':'減','几':'幾',
    '凤':'鳳','凭':'憑','凯':'凱','击':'擊','凿':'鑿','划':'劃','刘':'劉','则':'則','刚':'剛',
    '创':'創','删':'刪','别':'別','剧':'劇','劝':'勸','办':'辦','务':'務','动':'動','励':'勵',
    '劳':'勞','势':'勢','勋':'勳','华':'華','协':'協','单':'單','卖':'賣','卢':'盧','卫':'衛',
    '却':'卻','厅':'廳','历':'歷','厉':'厲','压':'壓','厌':'厭','县':'縣','发':'發','变':'變',
    '叶':'葉','号':'號','吕':'呂','员':'員','国':'國','图':'圖','圆':'圓','圣':'聖','场':'場',
    '块':'塊','坚':'堅','坛':'壇','坝':'壩','坟':'墳','坠':'墜','垦':'墾','墙':'牆','壮':'壯',
    '声':'聲','处':'處','备':'備','复':'復','头':'頭','夺':'奪','奖':'獎','奋':'奮','妇':'婦',
    '孙':'孫','学':'學','实':'實','宠':'寵','审':'審','宽':'寬','对':'對','寻':'尋','导':'導',
    '寿':'壽','将':'將','尘':'塵','尝':'嘗','尧':'堯','尽':'盡','层':'層','属':'屬','岁':'歲',
    '岛':'島','巩':'鞏','币':'幣','师':'師','帐':'帳','带':'帶','帮':'幫','干':'幹','庄':'莊',
    '庆':'慶','庐':'廬','应':'應','庙':'廟','厂':'廠','广':'廣','废':'廢','开':'開','异':'異',
    '张':'張','弹':'彈','强':'強','归':'歸','当':'當','录':'錄','汇':'匯','汉':'漢','灭':'滅',
    '灯':'燈','灵':'靈','灿':'燦','炉':'爐','无':'無','时':'時','晋':'晉','晒':'曬','晓':'曉',
    '术':'術','杀':'殺','杂':'雜','权':'權','条':'條','来':'來','杨':'楊','极':'極','构':'構',
    '标':'標','树':'樹','样':'樣','检':'檢','梦':'夢','欢':'歡','毕':'畢','气':'氣','沟':'溝',
    '泽':'澤','洁':'潔','测':'測','济':'濟','浏':'瀏','浑':'渾','浓':'濃','涛':'濤','润':'潤',
    '涨':'漲','湾':'灣','湿':'濕','溃':'潰','滨':'濱','滩':'灘','潜':'潛','炼':'煉','烟':'煙',
    '烦':'煩','烧':'燒','热':'熱','爱':'愛','爷':'爺','尔':'爾','牵':'牽','牺':'犧','犹':'猶',
    '独':'獨','获':'獲','献':'獻','现':'現','环':'環','电':'電','画':'畫','畅':'暢','疗':'療',
    '疯':'瘋','监':'監','盘':'盤','矿':'礦','码':'碼','砖':'磚','础':'礎','确':'確','碍':'礙',
    '礼':'禮','视':'視','离':'離','种':'種','积':'積','称':'稱','稳':'穩','穷':'窮','窃':'竊',
    '竞':'競','笔':'筆','筑':'築','筛':'篩','简':'簡','类':'類','粮':'糧','紧':'緊','纠':'糾',
    '红':'紅','纤':'纖','约':'約','级':'級','纪':'紀','纯':'純','纲':'綱','纳':'納','纵':'縱',
    '纷':'紛','纸':'紙','纹':'紋','纺':'紡','纽':'紐','线':'線','练':'練','组':'組','细':'細',
    '织':'織','终':'終','绍':'紹','经':'經','绑':'綁','结':'結','给':'給','络':'絡','绝':'絕',
    '统':'統','绢':'絹','绣':'繡','继':'繼','绩':'績','绪':'緒','续':'續','绳':'繩','维':'維',
    '绵':'綿','综':'綜','绿':'綠','绸':'綢','缩':'縮','缪':'繆','缆':'纜','网':'網','罗':'羅',
    '罚':'罰','罢':'罷','聪':'聰','联':'聯','肃':'肅','胜':'勝','胀':'脹','肿':'腫','胆':'膽',
    '脏':'臟','脑':'腦','脚':'腳','脸':'臉','脱':'脫','腊':'臘','腾':'騰','舰':'艦','艰':'艱',
    '艺':'藝','节':'節','苏':'蘇','范':'範','蓝':'藍','药':'藥','虽':'雖','虫':'蟲','虾':'蝦',
    '蚕':'蠶','蛮':'蠻','见':'見','观':'觀','规':'規','览':'覽','觉':'覺','触':'觸','计':'計',
    '订':'訂','认':'認','让':'讓','训':'訓','议':'議','记':'記','讲':'講','许':'許','论':'論',
    '讽':'諷','设':'設','访':'訪','证':'證','评':'評','识':'識','诉':'訴','词':'詞','译':'譯',
    '试':'試','诗':'詩','诚':'誠','话':'話','诞':'誕','询':'詢','该':'該','详':'詳','语':'語',
    '误':'誤','说':'說','请':'請','诸':'諸','读':'讀','课':'課','谁':'誰','调':'調','谈':'談',
    '谊':'誼','谋':'謀','谢':'謝','谣':'謠','谦':'謙','谨':'謹','贝':'貝','负':'負','财':'財',
    '责':'責','贤':'賢','货':'貨','质':'質','购':'購','费':'費','贺':'賀','贼':'賊','资':'資',
    '赏':'賞','赐':'賜','赖':'賴','赚':'賺','赛':'賽','赞':'贊','赠':'贈','赢':'贏','赵':'趙',
    '赶':'趕','跃':'躍','践':'踐','踪':'蹤','车':'車','轨':'軌','转':'轉','轮':'輪','软':'軟',
    '轴':'軸','轻':'輕','载':'載','较':'較','辆':'輛','辉':'輝','辈':'輩','辑':'輯','输':'輸',
    '辞':'辭','边':'邊','辽':'遼','达':'達','迁':'遷','过':'過','迈':'邁','运':'運','还':'還',
    '这':'這','进':'進','远':'遠','违':'違','连':'連','迟':'遲','选':'選','适':'適','递':'遞',
    '遗':'遺','邓':'鄧','邮':'郵','邻':'鄰','郑':'鄭','里':'裡','针':'針','钉':'釘','钓':'釣',
    '钟':'鐘','钢':'鋼','钥':'鑰','钦':'欽','钩':'鉤','钱':'錢','铁':'鐵','铜':'銅','铝':'鋁',
    '银':'銀','铸':'鑄','铺':'鋪','链':'鏈','销':'銷','锁':'鎖','锅':'鍋','锈':'鏽','锋':'鋒',
    '锐':'銳','错':'錯','锡':'錫','锣':'鑼','锤':'錘','锦':'錦','键':'鍵','锯':'鋸','镇':'鎮',
    '镜':'鏡','长':'長','门':'門','闪':'閃','闭':'閉','问':'問','闯':'闖','闲':'閒','间':'間',
    '闻':'聞','阀':'閥','阁':'閣','阅':'閱','队':'隊','阶':'階','阳':'陽','阴':'陰','阵':'陣',
    '陆':'陸','际':'際','陈':'陳','陕':'陝','险':'險','随':'隨','隐':'隱','难':'難','雾':'霧',
    '静':'靜','面':'麵','韩':'韓','页':'頁','顶':'頂','项':'項','顺':'順','须':'須','顾':'顧',
    '顿':'頓','预':'預','领':'領','颈':'頸','频':'頻','颖':'穎','颗':'顆','题':'題','颜':'顏',
    '额':'額','风':'風','飘':'飄','飞':'飛','饭':'飯','饮':'飲','饱':'飽','饺':'餃','饼':'餅',
    '饿':'餓','馆':'館','马':'馬','驰':'馳','驱':'驅','驴':'驢','驶':'駛','驻':'駐','驾':'駕',
    '验':'驗','骗':'騙','鱼':'魚','鲁':'魯','鲜':'鮮','鸟':'鳥','鸡':'雞','鸣':'鳴','鸭':'鴨',
    '鸽':'鴿','鸿':'鴻','鹅':'鵝','鹤':'鶴','鹰':'鷹','麦':'麥','黄':'黃','龙':'龍',
    '龟':'龜','轼':'軾',
  };
  
  function toAltScript(text: string): string | null {
    // Try simplified→traditional first
    let alt = '';
    let changed = false;
    for (const ch of text) {
      if (SC_TC_MAP[ch]) { alt += SC_TC_MAP[ch]; changed = true; }
      else alt += ch;
    }
    if (changed) return alt;
    
    // Try traditional→simplified
    const TC_SC_MAP: Record<string, string> = {};
    for (const [sc, tc] of Object.entries(SC_TC_MAP)) TC_SC_MAP[tc] = sc;
    alt = '';
    changed = false;
    for (const ch of text) {
      if (TC_SC_MAP[ch]) { alt += TC_SC_MAP[ch]; changed = true; }
      else alt += ch;
    }
    return changed ? alt : null;
  }

  let relevanceOrder = '';
  if (opts?.query) {
    const rawQuery = opts.query;
    const altQuery = opts.queryAlt || toAltScript(rawQuery);
    const q = `%${rawQuery}%`;
    
    if (altQuery && altQuery !== rawQuery) {
      const aq = `%${altQuery}%`;
      conditions.push(
        '(name LIKE ? OR name LIKE ? OR name_en LIKE ? OR summary LIKE ? OR summary LIKE ? OR alternative_names LIKE ?)'
      );
      params.push(q, aq, q, q, aq, q);

      const exact = rawQuery;
      const exactAlt = altQuery;
      const prefix = `${rawQuery}%`;
      const prefixAlt = `${altQuery}%`;
      relevanceOrder = `
        CASE
          WHEN name = ? THEN 0
          WHEN name = ? THEN 0
          WHEN name LIKE ? THEN 1
          WHEN name LIKE ? THEN 1
          WHEN name LIKE ? THEN 2
          WHEN name LIKE ? THEN 2
          WHEN name_en = ? THEN 3
          WHEN name_en LIKE ? THEN 4
          ELSE 5
        END,
        CHAR_LENGTH(name),
        name`;
      params.push(exact, exactAlt, prefix, prefixAlt, q, aq, exact, prefix);
    } else {
      conditions.push(
        '(name LIKE ? OR name_en LIKE ? OR summary LIKE ? OR alternative_names LIKE ?)'
      );
      params.push(q, q, q, q);

      const exact = rawQuery;
      const prefix = `${rawQuery}%`;
      relevanceOrder = `
        CASE
          WHEN name = ? THEN 0
          WHEN name LIKE ? THEN 1
          WHEN name LIKE ? THEN 2
          WHEN name_en = ? THEN 3
          WHEN name_en LIKE ? THEN 4
          ELSE 5
        END,
        CHAR_LENGTH(name),
        name`;
      params.push(exact, prefix, q, exact, prefix);
    }
  }
  if (opts?.era) {
    if (opts.era.max === null) {
      conditions.push('birth_year >= ?'); params.push(opts.era.min);
    } else {
      conditions.push('birth_year >= ? AND birth_year < ?');
      params.push(opts.era.min, opts.era.max);
    }
  }

  const where = conditions.length > 0 ? `WHERE ${conditions.join(' AND ')}` : '';

  const orderBy = relevanceOrder || 'name';

  // If pagination requested, do it in SQL (not in memory)
  if (opts?.page && opts?.limit) {
    const offset = (opts.page - 1) * opts.limit;
    const [countRows] = await pool.query<RowDataPacket[]>(
      `SELECT COUNT(*) as total FROM people ${where}`, params,
    );
    const total = countRows[0].total;
    const [rows] = await pool.query<RowDataPacket[]>(
      `SELECT * FROM people ${where} ORDER BY ${orderBy} LIMIT ? OFFSET ?`,
      [...params, opts.limit, offset],
    );
    return { items: rows.map(mapPerson), total };
  }

  // Default: hard limit of 500 to prevent accidental full-table loads
  const effectiveLimit = opts?.limit ?? 500;
  const [countRows] = await pool.query<RowDataPacket[]>(
    `SELECT COUNT(*) as total FROM people ${where}`, params,
  );
  const total = countRows[0].total as number;
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT * FROM people ${where} ORDER BY ${orderBy} LIMIT ?`, [...params, effectiveLimit],
  );
  const items = rows.map(mapPerson);
  return { items, total };
}

export async function findPersonById(id: string): Promise<Person | undefined> {
  const [rows] = await pool.query<RowDataPacket[]>(
    'SELECT * FROM people WHERE id = ?', [id],
  );
  return rows.length ? mapPerson(rows[0]) : undefined;
}

export async function findPeopleByIds(ids: string[]): Promise<Person[]> {
  if (ids.length === 0) return [];
  const placeholders = ids.map(() => '?').join(',');
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT * FROM people WHERE id IN (${placeholders})`, ids,
  );
  return rows.map(mapPerson);
}

export async function listEvents(opts?: {
  publishedOnly?: boolean;
  dataStatus?: string;
  regionId?: string;
  ids?: string[];
  page?: number;
  limit?: number;
}): Promise<HistoricalEvent[]> {
  const conditions: string[] = [];
  const params: unknown[] = [];

  if (opts?.publishedOnly) { conditions.push('data_status = ?'); params.push('published'); }
  if (opts?.dataStatus && opts.dataStatus !== 'all') { conditions.push('data_status = ?'); params.push(opts.dataStatus); }
  if (opts?.regionId) { conditions.push('region_id = ?'); params.push(opts.regionId); }
  if (opts?.ids && opts.ids.length > 0) {
    conditions.push(`id IN (${opts.ids.map(() => '?').join(',')})`);
    params.push(...opts.ids);
  }

  const where = conditions.length > 0 ? `WHERE ${conditions.join(' AND ')}` : '';
  const effectiveLimit = opts?.limit ?? 500;
  const offset = opts?.page ? (opts.page - 1) * effectiveLimit : 0;

  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT * FROM events ${where} ORDER BY start_year DESC LIMIT ? OFFSET ?`,
    [...params, effectiveLimit, offset],
  );
  return rows.map(mapEvent);
}

export async function listAllEvents(opts?: {
  page?: number;
  limit?: number;
  dataStatus?: string;
}): Promise<{ items: HistoricalEvent[]; total: number }> {
  const conditions: string[] = [];
  const params: unknown[] = [];
  if (opts?.dataStatus && opts.dataStatus !== 'all') {
    conditions.push('data_status = ?'); params.push(opts.dataStatus);
  }
  const where = conditions.length > 0 ? `WHERE ${conditions.join(' AND ')}` : '';

  if (opts?.page && opts?.limit) {
    const offset = (opts.page - 1) * opts.limit;
    const [countRows] = await pool.query<RowDataPacket[]>(
      `SELECT COUNT(*) as total FROM events ${where}`, params,
    );
    const total = countRows[0].total as number;
    const [rows] = await pool.query<RowDataPacket[]>(
      `SELECT * FROM events ${where} ORDER BY start_year DESC LIMIT ? OFFSET ?`,
      [...params, opts.limit, offset],
    );
    return { items: rows.map(mapEvent), total };
  }

  // Default: hard limit of 500 to prevent accidental full-table loads
  const effectiveLimit = opts?.limit ?? 500;
  const [countRows] = await pool.query<RowDataPacket[]>(
    `SELECT COUNT(*) as total FROM events ${where}`, params,
  );
  const total = countRows[0].total as number;
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT * FROM events ${where} ORDER BY start_year DESC LIMIT ?`, [effectiveLimit],
  );
  return { items: rows.map(mapEvent), total };
}

export async function findEventById(id: string): Promise<HistoricalEvent | undefined> {
  const [rows] = await pool.query<RowDataPacket[]>(
    'SELECT * FROM events WHERE id = ?', [id],
  );
  return rows.length ? mapEvent(rows[0]) : undefined;
}

export async function findEventsForPerson(personId: string): Promise<HistoricalEvent[]> {
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT e.* FROM events e
     INNER JOIN event_persons ep ON e.id = ep.event_id
     WHERE ep.person_id = ? AND e.data_status = 'published'`,
    [personId],
  );
  return rows.map(mapEvent);
}

export async function findEventsByRegion(regionId: string): Promise<HistoricalEvent[]> {
  const [rows] = await pool.query<RowDataPacket[]>(
    "SELECT * FROM events WHERE region_id = ? AND data_status = 'published' ORDER BY start_year LIMIT 500",
    [regionId],
  );
  return rows.map(mapEvent);
}

export async function listEventsBySearch(query: string, limit = 50): Promise<HistoricalEvent[]> {
  const q = `%${query}%`;
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT * FROM events 
     WHERE data_status = 'published' 
     AND (title LIKE ? OR title_en LIKE ? OR summary LIKE ? OR summary_en LIKE ?)
     ORDER BY importance DESC, start_year DESC
     LIMIT ?`,
    [q, q, q, q, limit],
  );
  return rows.map(mapEvent);
}

export async function findEventsByYearRange(minYear: number, maxYear: number): Promise<HistoricalEvent[]> {
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT * FROM events 
     WHERE data_status = 'published' AND start_year IS NOT NULL
     AND (
       (start_year >= ? AND start_year <= ?)
       OR (end_year IS NOT NULL AND end_year >= ? AND end_year <= ?)
       OR (start_year <= ? AND end_year IS NOT NULL AND end_year >= ?)
     )
     ORDER BY start_year
     LIMIT 500`,
    [minYear, maxYear, minYear, maxYear, minYear, maxYear],
  );
  return rows.map(mapEvent);
}

export async function findPersonsForEvent(eventId: string): Promise<Person[]> {
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT p.* FROM people p
     INNER JOIN event_persons ep ON p.id = ep.person_id
     WHERE ep.event_id = ?`,
    [eventId],
  );
  return rows.map(mapPerson);
}

export async function listRegions(): Promise<Region[]> {
  const [rows] = await pool.query<RowDataPacket[]>('SELECT * FROM regions');
  return rows.map(mapRegion);
}

export async function findRegionById(id: string): Promise<Region | undefined> {
  const [rows] = await pool.query<RowDataPacket[]>(
    'SELECT * FROM regions WHERE id = ?', [id],
  );
  return rows.length ? mapRegion(rows[0]) : undefined;
}

export async function findSubRegions(regionId: string): Promise<Region[]> {
  const [rows] = await pool.query<RowDataPacket[]>(
    'SELECT * FROM regions WHERE parent_region_id = ?', [regionId],
  );
  return rows.map(mapRegion);
}

export async function listSources(): Promise<Source[]> {
  const [rows] = await pool.query<RowDataPacket[]>('SELECT * FROM sources');
  return rows.map(r => ({
    id: r.id, title: r.title, titleEn: r.title_en ?? undefined,
    author: r.author ?? undefined, url: r.url ?? undefined,
    publisher: r.publisher ?? undefined, year: r.year ?? undefined,
    note: r.note ?? undefined, license: r.license ?? undefined,
  }));
}

export async function findSourceById(id: string): Promise<Source | undefined> {
  const [rows] = await pool.query<RowDataPacket[]>(
    'SELECT * FROM sources WHERE id = ?', [id],
  );
  if (!rows.length) return undefined;
  const r = rows[0];
  return {
    id: r.id, title: r.title, titleEn: r.title_en ?? undefined,
    author: r.author ?? undefined, url: r.url ?? undefined,
    publisher: r.publisher ?? undefined, year: r.year ?? undefined,
    note: r.note ?? undefined, license: r.license ?? undefined,
  };
}

export async function findSourcesForEvent(eventId: string): Promise<Source[]> {
  const event = await findEventById(eventId);
  if (!event || event.sourceIds.length === 0) return [];
  const placeholders = event.sourceIds.map(() => '?').join(',');
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT * FROM sources WHERE id IN (${placeholders})`, event.sourceIds,
  );
  return rows.map(r => ({
    id: r.id, title: r.title, titleEn: r.title_en ?? undefined,
    author: r.author ?? undefined, url: r.url ?? undefined,
    publisher: r.publisher ?? undefined, year: r.year ?? undefined,
    note: r.note ?? undefined, license: r.license ?? undefined,
  }));
}

let _tagsCache: string[] | null = null;
let _tagsCacheTime = 0;
const TAGS_CACHE_TTL = 10 * 60 * 1000; // 10 minutes

export async function findAllTags(): Promise<string[]> {
  if (_tagsCache && Date.now() - _tagsCacheTime < TAGS_CACHE_TTL) {
    return _tagsCache;
  }
  const [pRows] = await pool.query<RowDataPacket[]>('SELECT DISTINCT tags FROM people WHERE data_status = ?', ['published']);
  const [eRows] = await pool.query<RowDataPacket[]>('SELECT DISTINCT tags FROM events WHERE data_status = ?', ['published']);
  const tagSet = new Set<string>();
  for (const r of pRows) {
    for (const t of parseJsonArray(r.tags)) tagSet.add(t);
  }
  for (const r of eRows) {
    for (const t of parseJsonArray(r.tags)) tagSet.add(t);
  }
  _tagsCache = Array.from(tagSet).sort();
  _tagsCacheTime = Date.now();
  return _tagsCache;
}

// ==================== Write operations ====================

export async function updatePersonStatus(
  ids: string[], status: DataStatus, reviewedBy: string,
): Promise<void> {
  if (ids.length === 0) return;
  const placeholders = ids.map(() => '?').join(',');
  await pool.query(
    `UPDATE people SET data_status = ?, last_reviewed_at = NOW(), reviewed_by = ? WHERE id IN (${placeholders})`,
    [status, reviewedBy, ...ids],
  );
}

export async function updateEventStatus(
  ids: string[], status: DataStatus, reviewedBy: string,
): Promise<void> {
  if (ids.length === 0) return;
  const placeholders = ids.map(() => '?').join(',');
  await pool.query(
    `UPDATE events SET data_status = ?, last_reviewed_at = NOW(), reviewed_by = ? WHERE id IN (${placeholders})`,
    [status, reviewedBy, ...ids],
  );
}

export async function updatePersonScore(
  id: string, score: number, reviewedBy: string,
): Promise<void> {
  await pool.query(
    'UPDATE people SET confidence_score = ?, last_reviewed_at = NOW(), reviewed_by = ? WHERE id = ?',
    [score, reviewedBy, id],
  );
}

export async function updateEventScore(
  id: string, score: number, reviewedBy: string,
): Promise<void> {
  await pool.query(
    'UPDATE events SET confidence_score = ?, last_reviewed_at = NOW(), reviewed_by = ? WHERE id = ?',
    [score, reviewedBy, id],
  );
}
