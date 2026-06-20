/**
 * 精准去重脚本
 * 
 * 策略：
 * 1. 找出同一人物、同一年份（±3年）的重复事件
 * 2. 保留信息最完整、与权威来源最一致的版本
 * 3. 删除模板生成的简略版本
 * 
 * 优先级：
 *   - evt-deep-* (深度生成，最详细) > evt-sushi-* / evt-*-major > evt-wutai > evt-lifespan-*
 *   - 有完整 description > 只有 summary
 *   - importance 高 > 低
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
  end_year: number | null;
  summary: string | null;
  description: string | null;
  importance: number;
  confidence_score: number;
  source_ids: string;
  tags: string;
}

function normalizeChinese(text: string): string {
  return text
    .replace(/\s+/g, '')
    .replace(/[，,。．、；;：:！!？?""''「」『』【】（）()《》<>\[\]{}""'']/g, '')
    .trim()
    .toLowerCase();
}

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
  for (const bg of bigramsA) { if (bigramsB.has(bg)) intersection++; }
  const union = bigramsA.size + bigramsB.size - intersection;
  return union > 0 ? intersection / union : 0;
}

function eventQualityScore(e: EventRow): number {
  let score = 0;
  
  // ID-based priority
  const id = e.id;
  if (id.startsWith('evt-deep-')) score += 500;
  else if (id.includes('-major') || id.includes('-event-')) score += 300;
  else if (id.startsWith('evt-lifespan-')) score -= 200;
  
  // Content quality
  if (e.description && e.description.length > 0) score += Math.min(e.description.length, 500);
  if (e.summary && e.summary.length > 0) score += Math.min(e.summary.length, 200);
  
  try {
    const sources = JSON.parse(e.source_ids || '[]');
    score += sources.length * 100;
  } catch {}
  
  score += e.importance * 50;
  score += e.confidence_score * 100;
  
  // Deduct for template patterns
  const title = e.title || '';
  if (title.includes('生平') && title.length < 10) score -= 100;
  if (/^[\u4e00-\u9fa5]+·[—\-\d]/.test(title)) score -= 50; // "XXX·-YYYY年)" pattern
  
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
    const people = personRows as any[];
    console.log(`找到 ${people.length} 个人物\n`);

    const toDelete: string[] = [];
    const duplicateGroups: any[] = [];
    let totalGroups = 0;

    for (const person of people) {
      const [eventRows] = await conn.query<mysql.RowDataPacket[]>(
        `SELECT e.id, e.title, e.start_year, e.end_year, e.summary, e.description, 
                e.importance, e.confidence_score, e.source_ids, e.tags
         FROM events e
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
          
          // Compare title + summary
          const combinedA = (ei.title || '') + ' ' + (ei.summary || '');
          const combinedB = (ej.title || '') + ' ' + (ej.summary || '');
          const titleSim = textSimilarity(combinedA, combinedB);
          
          // Also check if titles share key characters (for short titles)
          const titleOnlySim = textSimilarity(ei.title || '', ej.title || '');
          const maxSim = Math.max(titleSim, titleOnlySim);
          
          if (maxSim >= 0.35) {
            group.push(ej);
            processed.add(ej.id);
          }
        }
        
        if (group.length > 1) {
          group.sort((a, b) => eventQualityScore(b) - eventQualityScore(a));
          
          const best = group[0];
          const dupes = group.slice(1);
          
          // Verify they're actually about the same topic
          // Skip if the best is a "lifespan" entry but there are more specific events
          
          duplicateGroups.push({
            personName: `${person.name}${person.name_en ? ` (${person.name_en})` : ''}`,
            year: group[0].start_year,
            keep: { id: best.id, title: best.title, score: eventQualityScore(best) },
            delete: dupes.map(d => ({ id: d.id, title: d.title, score: eventQualityScore(d) })),
          });
          
          for (const d of dupes) toDelete.push(d.id);
          totalGroups++;
        }
      }
    }

    console.log(`发现 ${totalGroups} 组重复事件，共 ${toDelete.length} 条需删除\n`);

    // Print summary grouped by event ID pattern
    const patternCount: Record<string, number> = {};
    for (const id of toDelete) {
      let pattern = 'other';
      if (id.startsWith('evt-lifespan-')) pattern = 'evt-lifespan-* (生平模板)';
      else if (id.startsWith('evt-newpub-') && id.includes('-event-')) pattern = 'evt-newpub-*-event-*';
      else if (id.includes('-major')) pattern = '*-major';
      else if (id.includes('-birth')) pattern = '*-birth';
      else if (id.includes('-death')) pattern = '*-death';
      else if (id.startsWith('evt-rich2-')) pattern = 'evt-rich2-*';
      else if (id.startsWith('evt-deep-')) pattern = 'evt-deep-*';
      else if (id.startsWith('evt-')) pattern = 'evt-* (specific events)';
      patternCount[pattern] = (patternCount[pattern] || 0) + 1;
    }
    
    console.log('按事件类型分类:');
    for (const [pattern, count] of Object.entries(patternCount).sort((a, b) => b[1] - a[1])) {
      console.log(`  ${pattern}: ${count} 条`);
    }

    // Print some examples
    console.log(`\n========== 示例（前30组）==========`);
    for (const group of duplicateGroups.slice(0, 30)) {
      console.log(`\n${group.personName} (${group.year}年)`);
      console.log(`  ✓ KEEP [${group.keep.id}] score=${group.keep.score} "${group.keep.title}"`);
      for (const d of group.delete) {
        console.log(`  ✗ DEL  [${d.id}] score=${d.score} "${d.title}"`);
      }
    }

    // Save report
    const fs = await import('fs');
    fs.writeFileSync('scripts/dedup_report_v2.json', JSON.stringify({
      totalGroups,
      totalToDelete: toDelete.length,
      patternBreakdown: patternCount,
      deleteIds: toDelete,
      groups: duplicateGroups,
    }, null, 2));
    console.log(`\n完整报告已保存到 scripts/dedup_report_v2.json`);
    
    // Output SQL for manual review
    console.log(`\n========== 删除SQL（预览前50条）==========`);
    for (const id of toDelete.slice(0, 50)) {
      console.log(`DELETE FROM event_persons WHERE event_id = '${id}';`);
      console.log(`DELETE FROM events WHERE id = '${id}';`);
    }
    if (toDelete.length > 50) {
      console.log(`-- ... 还有 ${toDelete.length - 50} 条`);
    }

  } finally {
    conn.release();
    await pool.end();
  }
}

main().catch(console.error);
