/**
 * 从 TuGraph 三国数据集导入人物和战役
 * 
 * 数据来源：https://github.com/TuGraph-family/tugraph-db-demo
 * 许可证：Apache License 2.0
 * 路径：three_kingdoms/raw_data/
 */

import mysql from 'mysql2/promise';

const pool = mysql.createPool({
  host: process.env.MYSQL_HOST || 'localhost',
  port: parseInt(process.env.MYSQL_PORT || '3307', 10),
  user: process.env.MYSQL_USER || 'root',
  password: process.env.MYSQL_PASSWORD ?? undefined,
  database: process.env.MYSQL_DATABASE || 'history_parallel',
  charset: 'utf8mb4',
  socketPath: process.env.MYSQL_SOCKET || '/tmp/mysql.sock',
  waitForConnections: true,
  connectionLimit: 5,
});

interface PersonRow {
  name: string;
  camp: string;
  hometown: string;
  family: string;
  father_position?: string;
  position?: string;
}

interface BattleRow {
  name: string;
  start: string;
  end: string;
}

function generateId(name: string): string {
  return `tk-tugraph-${name}`;
}

function generateEventId(prefix: string): string {
  return `tk-tg-${prefix}-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 6)}`;
}

async function downloadCSV(url: string): Promise<string> {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.text();
}

function parseCSV(csv: string): Record<string, string>[] {
  const lines = csv.trim().split('\n');
  if (lines.length < 2) return [];
  const headers = lines[0].split(',').map(h => h.trim());
  const result: Record<string, string>[] = [];
  for (let i = 1; i < lines.length; i++) {
    const values = lines[i].split(',').map(v => v.trim());
    const row: Record<string, string> = {};
    headers.forEach((h, idx) => { row[h] = values[idx] || ''; });
    result.push(row);
  }
  return result;
}

async function importPerson(
  data: Record<string, string>,
  category: '主公' | '武将' | '文臣',
  conn: mysql.PoolConnection
): Promise<boolean> {
  const name = data.name;
  if (!name) return false;
  
  const personId = generateId(name);

  // Check if exists
  const [existing] = await conn.query<mysql.RowDataPacket[]>(
    'SELECT id FROM people WHERE id = ?', [personId]
  );
  if (existing.length > 0) {
    return false; // already exists
  }

  const camp = data.camp || '';
  const hometown = data.hometown || '';
  const family = data.family || '';
  const fatherPos = data.father_position || '';
  const position = data.position || '';

  // Build tags and summary
  const tags = ['三国', camp, category].filter(Boolean);
  if (family) tags.push(family);
  
  const summaryParts: string[] = [];
  if (camp) summaryParts.push(`${camp}势力`);
  if (hometown) summaryParts.push(`籍贯${hometown}`);
  if (position) summaryParts.push(position);
  if (family) summaryParts.push(`出自${family}`);
  if (fatherPos) summaryParts.push(`父为${fatherPos}`);
  
  const summary = `${name}，${summaryParts.join('，')}。`;

  // Estimate birth/death years based on historical context
  // Most Three Kingdoms figures lived 160-280 AD
  let birthYear: number | undefined;
  let deathYear: number | undefined;

  // Known birth/death years for famous figures
  const knownYears: Record<string, [number, number]> = {
    '曹操': [155, 220], '曹丕': [187, 226], '曹叡': [204, 239],
    '刘备': [161, 223], '刘禅': [207, 271],
    '孙坚': [155, 191], '孙策': [175, 200], '孙权': [182, 252],
    '袁绍': [154, 202], '袁术': [155, 199],
    '司马懿': [179, 251], '司马师': [208, 255], '司马昭': [211, 265],
    '董卓': [138, 192], '吕布': [156, 198],
    '公孙瓒': [157, 199], '刘焉': [132, 194], '刘璋': [162, 219],
    '刘表': [142, 208], '刘协': [181, 234], '马腾': [156, 212],
    '刘繇': [156, 197],
    // 武将
    '关羽': [160, 220], '张飞': [167, 221], '赵云': [168, 229],
    '马超': [176, 222], '黄忠': [148, 220], '魏延': [174, 234],
    '姜维': [202, 264], '张郃': [167, 231], '徐晃': [169, 227],
    '张辽': [169, 222], '乐进': [159, 218], '于禁': [159, 221],
    '张绣': [155, 207], '夏侯惇': [157, 220], '夏侯渊': [162, 219],
    '曹仁': [168, 223], '曹洪': [169, 232], '许褚': [170, 222],
    '典韦': [160, 197],
    '周瑜': [175, 210], '鲁肃': [172, 217], '吕蒙': [178, 220],
    '陆逊': [183, 245], '陆抗': [226, 274], '程普': [154, 210],
    '黄盖': [145, 215], '甘宁': [175, 222], '太史慈': [166, 206],
    '徐盛': [177, 228], '丁奉': [186, 271],
    // 文臣
    '诸葛亮': [181, 234], '荀彧': [163, 212], '荀攸': [157, 214],
    '贾诩': [147, 223], '郭嘉': [170, 207], '程昱': [141, 220],
    '陈群': [165, 237], '钟繇': [151, 230], '钟会': [225, 264],
    '庞统': [179, 214], '法正': [176, 220], '蒋琬': [188, 246],
    '费祎': [195, 253], '董允': [190, 246],
    '张昭': [156, 236], '顾雍': [168, 243], '诸葛瑾': [174, 241],
    '步骘': [177, 247],
  };

  if (knownYears[name]) {
    [birthYear, deathYear] = knownYears[name];
  }

  // Insert person
  try {
    await conn.query(
      `INSERT INTO people (id, name, alternative_names, birth_year, death_year,
       birth_date_precision, death_date_precision, region_id, occupations, tags,
       summary, description, data_status, confidence_score, source_ids)
       VALUES (?, ?, '[]', ?, ?, 'year', 'year', 'han-dynasty', ?, ?, ?, ?, 'published', 0.75, ?)`,
      [
        personId,
        name,
        birthYear ?? null,
        deathYear ?? null,
        JSON.stringify([category]),
        JSON.stringify(tags),
        summary,
        summary,
        JSON.stringify(['src-tugraph-three-kingdoms']),
      ]
    );

    // Create events
    const events: { title: string; year: number; summary: string; imp: 1|2|3|4|5 }[] = [];

    if (birthYear) {
      events.push({
        title: `${name}出生`,
        year: birthYear,
        summary: `${name}出生于${hometown || '不详之地'}${family ? `，出自${family}` : ''}`,
        imp: 2,
      });
    }

    // Career event
    const careerYear = birthYear ? birthYear + 30 : undefined;
    if (careerYear && deathYear && careerYear < deathYear) {
      events.push({
        title: `${name}的${category}生涯`,
        year: careerYear,
        summary: `${name}，${camp}势力${category}${position ? `，${position}` : ''}${hometown ? `，籍贯${hometown}` : ''}`,
        imp: 3,
      });
    }

    if (deathYear) {
      events.push({
        title: `${name}逝世`,
        year: deathYear,
        summary: `${name}逝世${position ? `，终其一生为${position}` : ''}`,
        imp: 3,
      });
    }

    // Insert events
    for (const evt of events) {
      const eventId = generateEventId(name.substring(0, 3));
      await conn.query(
        `INSERT INTO events (id, title, start_year, end_year, summary, importance,
         data_status, confidence_score, source_ids, tags)
         VALUES (?, ?, ?, NULL, ?, ?, 'published', 0.7, ?, ?)`,
        [
          eventId, evt.title, evt.year, evt.summary, evt.imp,
          JSON.stringify(['src-tugraph-three-kingdoms']),
          JSON.stringify(['三国', camp].filter(Boolean)),
        ]
      );
      await conn.query(
        'INSERT INTO event_persons (event_id, person_id) VALUES (?, ?)',
        [eventId, personId]
      );
    }

    return true;
  } catch (e: any) {
    console.error(`  ✗ ${name}: ${e.message?.substring(0, 80)}`);
    return false;
  }
}

async function importBattles(conn: mysql.PoolConnection): Promise<number> {
  const csv = await downloadCSV(
    'https://raw.githubusercontent.com/TuGraph-family/tugraph-db-demo/main/three_kingdoms/raw_data/战役.csv'
  );
  const rows = parseCSV(csv);
  let count = 0;

  for (const row of rows) {
    const name = row.name;
    if (!name) continue;
    
    const startYear = parseInt(row.start);
    const endYear = parseInt(row.end);
    if (isNaN(startYear)) continue;

    const eventId = `tk-tg-battle-${name}`;
    
    // Check if exists
    const [existing] = await conn.query<mysql.RowDataPacket[]>(
      'SELECT id FROM events WHERE id = ?', [eventId]
    );
    if (existing.length > 0) continue;

    const summary = startYear === endYear
      ? `公元${startYear}年，${name}爆发`
      : `公元${startYear}年至${endYear}年，${name}`;

    try {
      await conn.query(
        `INSERT INTO events (id, title, start_year, end_year, summary, importance,
         data_status, confidence_score, source_ids, tags)
         VALUES (?, ?, ?, ?, ?, 5, 'published', 0.8, ?, ?)`,
        [
          eventId, name, startYear, endYear !== startYear ? endYear : null,
          summary,
          JSON.stringify(['src-tugraph-three-kingdoms']),
          JSON.stringify(['三国', '战役']),
        ]
      );
      count++;
    } catch (e: any) {
      console.error(`  ✗ 战役 ${name}: ${e.message?.substring(0, 60)}`);
    }
  }

  return count;
}

async function main() {
  const conn = await pool.getConnection();

  try {
    const BASE = 'https://raw.githubusercontent.com/TuGraph-family/tugraph-db-demo/main/three_kingdoms/raw_data';

    // Import 主公
    console.log('=== 导入主公 ===');
    const lordCSV = await downloadCSV(`${BASE}/主公.csv`);
    const lords = parseCSV(lordCSV);
    let lordCount = 0;
    for (const row of lords) {
      if (await importPerson(row, '主公', conn)) lordCount++;
    }
    console.log(`  成功: ${lordCount}/${lords.length}\n`);

    // Import 武将
    console.log('=== 导入武将 ===');
    const generalCSV = await downloadCSV(`${BASE}/武将.csv`);
    const generals = parseCSV(generalCSV);
    let generalCount = 0;
    for (const row of generals) {
      if (await importPerson(row, '武将', conn)) generalCount++;
    }
    console.log(`  成功: ${generalCount}/${generals.length}\n`);

    // Import 文臣
    console.log('=== 导入文臣 ===');
    const advisorCSV = await downloadCSV(`${BASE}/文臣.csv`);
    const advisors = parseCSV(advisorCSV);
    let advisorCount = 0;
    for (const row of advisors) {
      if (await importPerson(row, '文臣', conn)) advisorCount++;
    }
    console.log(`  成功: ${advisorCount}/${advisors.length}\n`);

    // Import 战役
    console.log('=== 导入战役 ===');
    const battleCount = await importBattles(conn);
    console.log(`  成功: ${battleCount}\n`);

    const total = lordCount + generalCount + advisorCount;
    console.log(`========== 导入完成 ==========`);
    console.log(`人物: ${total} (主公${lordCount} + 武将${generalCount} + 文臣${advisorCount})`);
    console.log(`战役: ${battleCount}`);

    // Add source record
    const [existingSrc] = await conn.query<mysql.RowDataPacket[]>(
      "SELECT id FROM sources WHERE id = 'src-tugraph-three-kingdoms'"
    );
    if (existingSrc.length === 0) {
      await conn.query(
        `INSERT INTO sources (id, title, url, note, license)
         VALUES ('src-tugraph-three-kingdoms',
         'TuGraph Three Kingdoms Dataset',
         'https://github.com/TuGraph-family/tugraph-db-demo',
         '三国人物与战役结构化数据，用于图数据库演示',
         'Apache License 2.0')`
      );
      console.log('✓ 已添加数据来源记录');
    }

  } finally {
    conn.release();
    await pool.end();
  }
}

main().catch(console.error);
