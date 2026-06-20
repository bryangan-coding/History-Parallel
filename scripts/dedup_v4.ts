/**
 * 最终去重脚本 v4
 * 
 * 改进：
 * 1. 同年事件（精确年份匹配）才比较，避免跨年事件被误合并
 * 2. 关键词重叠 + 相同年份 = 同一事件
 * 3. 特别处理 evt-lifespan-* 和 struct 模板
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

interface EventRow {
  id: string;
  title: string;
  start_year: number | null;
  summary: string | null;
  description: string | null;
  importance: number;
  confidence_score: number;
  source_ids: string;
  tags: string;
}

function extractCoreKeywords(title: string, summary: string): string[] {
  const text = ((title || '') + ' ' + (summary || '')).toLowerCase();
  const keywords: string[] = [];
  
  const patterns = [
    '乌台诗案', '乌台', '诗案',
    '进士及第', '进士', '及第', '科举', '殿试',
    '贬谪', '被贬', '流放', '贬', '谪',
    '黄州', '惠州', '儋州', '岭南', '海南', '夜郎',
    '赤壁赋', '赤壁', '赤鼻',
    '翰林', '供奉',
    '庆历新政', '变法', '熙宁', '王安石', '新法',
    '安史之乱', '安禄山',
    '岳阳楼记', '岳阳楼',
    '资治通鉴', '通鉴',
    '苏堤', '杭州', '西湖', '疏浚',
    '出蜀', '远游', '仗剑',
    '草堂', '成都',
    '上万言书', '万言书',
    '金石', '赵明诚',
    '出生', '诞生', '出世',
    '逝世', '去世', '病逝', '卒',
    '生平', '一生',
    '任官', '任职', '为官',
    '致仕', '归乡', '退休',
    '政绩', '政声',
    '仕途', '官场',
  ];
  
  for (const p of patterns) {
    if (text.includes(p)) keywords.push(p);
  }
  
  return keywords;
}

function eventQualityScore(e: EventRow): number {
  let score = 0;
  
  const id = e.id;
  if (id.startsWith('evt-deep-')) score += 1000;
  else if (id.includes('-major')) score += 600;
  else if (id.startsWith('evt-tsymq-')) score += 500;
  else if (id.includes('-event-')) score += 400;
  else if (id.startsWith('evt-rich-')) score += 250;
  else if (id.startsWith('evt-rich2-')) score += 200;
  else if (id.startsWith('evt-lifespan-')) score -= 500;
  else if (id.startsWith('evt-struct')) score -= 200;
  else if (id.startsWith('evt-mass-')) score += 0;
  
  const descLen = (e.description || '').length;
  const summaryLen = (e.summary || '').length;
  score += Math.min(descLen, 600);
  score += Math.min(summaryLen, 300);
  
  try {
    const sources = JSON.parse(e.source_ids || '[]');
    score += sources.length * 200;
  } catch {}
  
  score += e.importance * 80;
  score += e.confidence_score * 150;
  
  const title = e.title || '';
  if ((title === '生平' || (title.endsWith('生平') && title.length <= 8))) score -= 300;
  if (/^[\u4e00-\u9fa5()（）·]+[·\-\—]\s*[\-\—\d]/.test(title)) score -= 100;
  if (title.includes('出生') && (e.summary || '').length < 50) score -= 50;
  if (title.includes('逝世') && (e.summary || '').length < 50) score -= 50;
  
  try {
    const tags = JSON.parse(e.tags || '[]');
    score += tags.length * 30;
  } catch {}
  
  return score;
}

async function main() {
  const conn = await pool.getConnection();
  
  try {
    console.log('查询所有有事件的人物...');
    const [personRows] = await conn.query<mysql.RowDataPacket[]>(
      `SELECT DISTINCT p.id, p.name, p.name_en
       FROM people p
       INNER JOIN event_persons ep ON p.id = ep.person_id
       WHERE p.data_status = 'published'
       ORDER BY p.name`
    );
    const people = personRows as any[];
    console.log(`找到 ${people.length} 个人物\n`);

    const toDelete: string[] = [];
    const duplicateGroups: any[] = [];

    for (const person of people) {
      const [eventRows] = await conn.query<mysql.RowDataPacket[]>(
        `SELECT e.id, e.title, e.start_year, e.summary, e.description, 
                e.importance, e.confidence_score, e.source_ids, e.tags
         FROM events e
         INNER JOIN event_persons ep ON e.id = ep.event_id
         WHERE ep.person_id = ? AND e.data_status = 'published'
         ORDER BY e.start_year, e.id`,
        [person.id]
      );
      const events: EventRow[] = eventRows as any[];
      
      if (events.length < 2) continue;

      // Group by EXACT year
      const yearGroups = new Map<number, EventRow[]>();
      for (const e of events) {
        const y = e.start_year ?? 0;
        if (!yearGroups.has(y)) yearGroups.set(y, []);
        yearGroups.get(y)!.push(e);
      }

      for (const [year, yearEvents] of yearGroups) {
        if (yearEvents.length < 2) continue;

        const eventKeywords = yearEvents.map(e => extractCoreKeywords(e.title || '', e.summary || ''));
        const assigned = new Set<number>();
        const clusters: EventRow[][] = [];

        for (let i = 0; i < yearEvents.length; i++) {
          if (assigned.has(i)) continue;
          
          const cluster: EventRow[] = [yearEvents[i]];
          assigned.add(i);
          
          for (let j = i + 1; j < yearEvents.length; j++) {
            if (assigned.has(j)) continue;
            
            const ki = eventKeywords[i];
            const kj = eventKeywords[j];
            const overlap = ki.filter(k => kj.includes(k)).length;
            
            const bothLifespan = yearEvents[i].id.startsWith('evt-lifespan-') && yearEvents[j].id.startsWith('evt-lifespan-');
            const bothStruct = (yearEvents[i].id.includes('struct') || yearEvents[i].id.includes('rich')) &&
                              (yearEvents[j].id.includes('struct') || yearEvents[j].id.includes('rich'));
            
            // For non-template events: require keyword overlap AND not completely different topics
            // For template events (lifespan/struct): always merge if same person same year
            if (bothLifespan || bothStruct) {
              cluster.push(yearEvents[j]);
              assigned.add(j);
            } else if (overlap > 0) {
              // Additional check: if one is "birth" and another is a specific event,
              // only merge if they share "birth" keyword
              const isBirth1 = ki.includes('出生') || ki.includes('诞生');
              const isBirth2 = kj.includes('出生') || kj.includes('诞生');
              const isDeath1 = ki.includes('逝世') || ki.includes('去世') || ki.includes('卒');
              const isDeath2 = kj.includes('逝世') || kj.includes('去世') || kj.includes('卒');
              
              // If one is birth/death template and other is a real event, DON'T merge
              if ((isBirth1 && !isBirth2) || (!isBirth1 && isBirth2)) continue;
              if ((isDeath1 && !isDeath2) || (!isDeath1 && isDeath2)) continue;
              
              cluster.push(yearEvents[j]);
              assigned.add(j);
            }
          }
          
          if (cluster.length > 1) {
            clusters.push(cluster);
          }
        }

        for (const cluster of clusters) {
          cluster.sort((a, b) => eventQualityScore(b) - eventQualityScore(a));
          
          const best = cluster[0];
          const dupes = cluster.slice(1);
          
          duplicateGroups.push({
            personName: `${person.name}${person.name_en ? ` (${person.name_en})` : ''}`,
            year,
            keep: { id: best.id, title: best.title, score: eventQualityScore(best) },
            delete: dupes.map(d => ({ id: d.id, title: d.title, score: eventQualityScore(d) })),
          });
          
          for (const d of dupes) toDelete.push(d.id);
        }
      }
    }

    console.log(`发现 ${duplicateGroups.length} 组重复事件`);
    console.log(`需删除 ${toDelete.length} 条\n`);

    // Check famous figures
    const famous = ['苏轼', '王安石', '李白', '杜甫', '白居易', '司马迁', '诸葛亮', '曹操', '岳飞', '文天祥', '辛弃疾', '欧阳修', '司马光', '韩愈', '柳宗元', '范仲淹', '陆游', '李清照'];
    
    console.log('========== 重要人物去重检查 ==========');
    for (const name of famous) {
      const personGroups = duplicateGroups.filter(g => g.personName.includes(name));
      if (personGroups.length > 0) {
        console.log(`\n--- ${name} (${personGroups.length}组) ---`);
        for (const g of personGroups) {
          console.log(`  ${g.year}年:`);
          console.log(`    ✓ KEEP [${g.keep.id}] s=${g.keep.score} "${g.keep.title}"`);
          for (const d of g.delete) {
            console.log(`    ✗ DEL  [${d.id}] s=${d.score} "${d.title}"`);
          }
        }
      }
    }

    // Pattern breakdown
    const patternCount: Record<string, number> = {};
    for (const id of toDelete) {
      let pattern = 'other';
      if (id.startsWith('evt-lifespan-')) pattern = 'evt-lifespan-* (生平模板)';
      else if (id.includes('newpub')) pattern = 'evt-newpub-*';
      else if (id.includes('-major')) pattern = '*-major';
      else if (id.includes('-birth')) pattern = '*-birth';
      else if (id.includes('-death')) pattern = '*-death';
      else if (id.startsWith('evt-rich') || id.includes('rich')) pattern = 'evt-rich*-*';
      else if (id.startsWith('evt-struct')) pattern = 'evt-struct*-*';
      else if (id.startsWith('evt-deep')) pattern = 'evt-deep-*';
      else if (id.startsWith('evt-tsymq-')) pattern = 'evt-tsymq-*';
      else if (id.startsWith('evt-mass-')) pattern = 'evt-mass-*';
      else if (id.startsWith('evt-')) pattern = 'evt-*';
      patternCount[pattern] = (patternCount[pattern] || 0) + 1;
    }
    
    console.log('\n========== 按事件类型分类 ==========');
    for (const [pattern, count] of Object.entries(patternCount).sort((a, b) => b[1] - a[1])) {
      console.log(`  ${pattern}: ${count} 条`);
    }

    // Save report
    const fs = await import('fs');
    fs.writeFileSync('scripts/dedup_v4_report.json', JSON.stringify({
      totalGroups: duplicateGroups.length,
      totalToDelete: toDelete.length,
      patternBreakdown: patternCount,
      deleteIds: toDelete,
      groups: duplicateGroups,
    }, null, 2));
    console.log(`\n完整报告已保存到 scripts/dedup_v4_report.json`);

    // Generate SQL
    const sqlLines: string[] = [
      '-- ============================================',
      '-- 事件去重 SQL v4 (精确年份匹配)',
      `-- 共删除 ${toDelete.length} 条重复事件`,
      `-- 生成时间: ${new Date().toISOString()}`,
      '-- ============================================',
      '',
      'START TRANSACTION;',
      '',
    ];
    
    for (let i = 0; i < toDelete.length; i += 100) {
      const batch = toDelete.slice(i, i + 100);
      const ids = batch.map(id => `'${id.replace(/'/g, "\\'")}'`).join(',');
      sqlLines.push(`-- Batch ${Math.floor(i / 100) + 1} (${batch.length} events)`);
      sqlLines.push(`DELETE FROM event_persons WHERE event_id IN (${ids});`);
      sqlLines.push(`DELETE FROM events WHERE id IN (${ids});`);
      sqlLines.push('');
    }
    
    sqlLines.push('COMMIT;');
    sqlLines.push('');
    sqlLines.push('-- Verify:');
    sqlLines.push("-- SELECT COUNT(*) as remaining FROM events WHERE data_status = 'published';");
    
    fs.writeFileSync('scripts/dedup_v4.sql', sqlLines.join('\n'));
    console.log(`SQL 已保存到 scripts/dedup_v4.sql`);

  } finally {
    conn.release();
    await pool.end();
  }
}

main().catch(console.error);
