/**
 * 事件去重脚本
 * 
 * 策略：
 * 1. 找出同一人物、同一年份附近的相似事件
 * 2. 保留最详细/准确的一条
 * 3. 标记重复项（先不删除，只输出报告）
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
  title_en: string | null;
  start_year: number | null;
  end_year: number | null;
  summary: string | null;
  summary_en: string | null;
  description: string | null;
  description_en: string | null;
  person_ids: string;
  tags: string;
  importance: number;
  confidence_score: number;
  source_ids: string;
  data_status: string;
}

interface PersonRow {
  id: string;
  name: string;
  name_en: string | null;
  birth_year: number | null;
  death_year: number | null;
}

// Normalize Chinese text
function normalizeChinese(text: string): string {
  return text
    .replace(/\s+/g, '')
    .replace(/[，,。．、；;：:！!？?""''「」『』【】（）()《》<>\[\]{}""'']/g, '')
    .trim()
    .toLowerCase();
}

// Jaccard similarity on bigrams
function textSimilarity(a: string, b: string): number {
  const na = normalizeChinese(a);
  const nb = normalizeChinese(b);
  if (!na || !nb) return 0;
  if (na === nb) return 1.0;
  
  const bigramsA = new Set<string>();
  const bigramsB = new Set<string>();
  
  for (let i = 0; i < na.length - 1; i++) bigramsA.add(na.substring(i, i + 2));
  for (let i = 0; i < nb.length - 1; i++) bigramsB.add(nb.substring(i, i + 2));
  
  if (bigramsA.size === 0 && bigramsB.size === 0) return 0;
  
  let intersection = 0;
  for (const bg of bigramsA) {
    if (bigramsB.has(bg)) intersection++;
  }
  
  const union = bigramsA.size + bigramsB.size - intersection;
  return union > 0 ? intersection / union : 0;
}

// Score how good an event record is
function eventQualityScore(e: EventRow): number {
  let score = 0;
  
  if (e.description && e.description.length > 0) {
    score += Math.min(e.description.length, 500);
  }
  if (e.summary && e.summary.length > 0) {
    score += Math.min(e.summary.length, 200);
  }
  try {
    const sources = JSON.parse(e.source_ids || '[]');
    score += sources.length * 100;
  } catch {}
  score += e.importance * 50;
  score += e.confidence_score * 100;
  if (e.title_en && e.title_en.length > 0) score += 50;
  try {
    const tags = JSON.parse(e.tags || '[]');
    score += tags.length * 20;
  } catch {}
  
  return score;
}

async function main() {
  const conn = await pool.getConnection();
  
  try {
    // Find all people with events
    console.log('查询所有有事件的人物...');
    const [personRows] = await conn.query<mysql.RowDataPacket[]>(
      `SELECT DISTINCT p.id, p.name, p.name_en, p.birth_year, p.death_year
       FROM people p
       INNER JOIN event_persons ep ON p.id = ep.person_id
       WHERE p.data_status = 'published'
       ORDER BY p.name`
    );
    const people: PersonRow[] = personRows as any[];
    console.log(`找到 ${people.length} 个人物\n`);

    const duplicateGroups: { personName: string; events: EventRow[] }[] = [];
    const toDelete: string[] = [];

    for (const person of people) {
      const [eventRows] = await conn.query<mysql.RowDataPacket[]>(
        `SELECT e.* FROM events e
         INNER JOIN event_persons ep ON e.id = ep.event_id
         WHERE ep.person_id = ? AND e.data_status = 'published'
         ORDER BY e.start_year, e.id`,
        [person.id]
      );
      const events: EventRow[] = eventRows as any[];
      
      if (events.length < 2) continue;

      const processed = new Set<string>();
      
      for (let i = 0; i < events.length; i++) {
        if (processed.has(events[i].id)) continue;
        
        const group: EventRow[] = [events[i]];
        processed.add(events[i].id);
        
        for (let j = i + 1; j < events.length; j++) {
          if (processed.has(events[j].id)) continue;
          
          const ei = events[i];
          const ej = events[j];
          
          const yearDiff = Math.abs((ei.start_year ?? 0) - (ej.start_year ?? 0));
          if (yearDiff > 3) continue;
          
          const titleSim = textSimilarity(
            (ei.title || '') + (ei.summary || ''),
            (ej.title || '') + (ej.summary || '')
          );
          
          if (titleSim >= 0.35) {
            group.push(ej);
            processed.add(ej.id);
          }
        }
        
        if (group.length > 1) {
          group.sort((a, b) => eventQualityScore(b) - eventQualityScore(a));
          
          const best = group[0];
          const dupes = group.slice(1);
          
          duplicateGroups.push({
            personName: `${person.name}${person.name_en ? ` (${person.name_en})` : ''}`,
            events: group,
          });
          
          for (const d of dupes) toDelete.push(d.id);
        }
      }
    }

    console.log(`\n========== 去重分析报告 ==========`);
    console.log(`共 ${duplicateGroups.length} 组重复事件`);
    console.log(`需处理 ${toDelete.length} 条重复记录\n`);

    for (const group of duplicateGroups) {
      console.log(`\n--- ${group.personName} (${group.events.length}条) ---`);
      for (const e of group.events) {
        const isKeep = e === group.events[0];
        const marker = isKeep ? '✓ KEEP' : '✗ DEL';
        console.log(`  ${marker} [${e.id}] ${e.start_year}年 | imp=${e.importance} | score=${eventQualityScore(e)}`);
        console.log(`      标题: ${e.title}`);
        if (e.summary) console.log(`      摘要: ${e.summary.substring(0, 150)}`);
        if (e.description) console.log(`      详情: ${e.description.substring(0, 150)}`);
        if (e.title_en) console.log(`      英文: ${e.title_en}`);
      }
    }

    // Save report
    const fs = await import('fs');
    const report = {
      totalGroups: duplicateGroups.length,
      totalDuplicates: toDelete.length,
      groups: duplicateGroups.map(g => ({
        personName: g.personName,
        keep: g.events[0].id,
        keepTitle: g.events[0].title,
        delete: g.events.slice(1).map(e => ({ id: e.id, title: e.title })),
      })),
      deleteIds: toDelete,
    };
    
    fs.writeFileSync('scripts/dedup_report.json', JSON.stringify(report, null, 2));
    console.log(`\n报告已保存到 scripts/dedup_report.json`);

  } finally {
    conn.release();
    await pool.end();
  }
}

main().catch(console.error);
