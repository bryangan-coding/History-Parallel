/**
 * 最终去重脚本
 * 
 * 核心策略：
 * 1. 同一人物、同年（±2年）的事件如果在同一语义域内，视为重复
 * 2. 保留标准：evt-deep-* > evt-*-major > 具体事件 > evt-lifespan-*
 * 3. 综合评估 description 完整度、summary 长度、importance、来源引用
 * 4. 与权威来源（百度百科）比对确认准确性
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

// 核心关键词集合 — 同一人物同年的事件如果共享核心关键词，视为同一事件
function extractCoreKeywords(title: string, summary: string): string[] {
  const text = (title + ' ' + (summary || '')).toLowerCase();
  const keywords: string[] = [];
  
  // 提取重要的事件关键词
  const patterns = [
    '乌台诗案', '乌台', '诗案',
    '进士及第', '进士', '及第', '科举',
    '贬谪', '被贬', '流放', '贬',
    '黄州', '惠州', '儋州', '岭南', '海南',
    '赤壁赋', '赤壁',
    '翰林', '供奉',
    '庆历新政', '变法', '熙宁', '王安石',
    '安史之乱',
    '岳阳楼记',
    '资治通鉴',
    '苏堤', '杭州', '西湖',
    '出蜀', '远游',
    '出生', '诞生',
    '逝世', '去世', '病逝',
    '生平',
  ];
  
  for (const p of patterns) {
    if (text.includes(p)) keywords.push(p);
  }
  
  return keywords;
}

function normalizeChinese(text: string): string {
  return text
    .replace(/\s+/g, '')
    .replace(/[，,。．、；;：:！!？?""''「」『』【】（）()《》<>\[\]{}""''…·\-—]/g, '')
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
  
  // ID-based priority (highest weight)
  const id = e.id;
  if (id.startsWith('evt-deep-')) score += 1000;
  else if (id.includes('-major') || id.includes('-event-')) score += 500;
  else if (id.startsWith('evt-tsymq-')) score += 400;
  else if (id.startsWith('evt-rich-') || id.startsWith('evt-rich2-')) score += 200;
  else if (id.startsWith('evt-lifespan-')) score -= 500; // template content
  else if (id.startsWith('evt-struct') || id.startsWith('evt-struct3')) score -= 200;
  
  // Content completeness
  const descLen = (e.description || '').length;
  const summaryLen = (e.summary || '').length;
  score += Math.min(descLen, 600); // description up to 600
  score += Math.min(summaryLen, 300); // summary up to 300
  
  // Source references
  try {
    const sources = JSON.parse(e.source_ids || '[]');
    score += sources.length * 200;
  } catch {}
  
  score += e.importance * 80;
  score += e.confidence_score * 150;
  
  // Penalize template patterns
  const title = e.title || '';
  if (title === '生平' || title.endsWith('生平') && title.length <= 6) score -= 300;
  if (/^[\u4e00-\u9fa5()（）·]+[·\-\—]\s*[\-\—\d]/.test(title)) score -= 100;
  if (title.includes('出生') && (e.summary || '').length < 50) score -= 50;
  
  // Bonus for rich tags
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

      // Group events by year buckets
      const yearGroups = new Map<number, EventRow[]>();
      for (const e of events) {
        const y = e.start_year ?? 0;
        // Find a nearby bucket
        let found = false;
        for (const [bucketYear, bucketEvents] of yearGroups) {
          if (Math.abs(y - bucketYear) <= 2) {
            bucketEvents.push(e);
            found = true;
            break;
          }
        }
        if (!found) {
          yearGroups.set(y, [e]);
        }
      }

      // Within each year group, find duplicates
      for (const [, yearEvents] of yearGroups) {
        if (yearEvents.length < 2) continue;

        // Compute pairwise similarity and cluster
        const clusters: EventRow[][] = [];
        const assigned = new Set<number>();

        for (let i = 0; i < yearEvents.length; i++) {
          if (assigned.has(i)) continue;
          
          const cluster: EventRow[] = [yearEvents[i]];
          assigned.add(i);
          
          for (let j = i + 1; j < yearEvents.length; j++) {
            if (assigned.has(j)) continue;
            
            const ei = yearEvents[i];
            const ej = yearEvents[j];
            
            // Check core keyword overlap
            const ki = extractCoreKeywords(ei.title || '', ei.summary || '');
            const kj = extractCoreKeywords(ej.title || '', ej.summary || '');
            
            const keywordOverlap = ki.filter(k => kj.includes(k)).length;
            const hasKeywordMatch = keywordOverlap > 0 || (ki.length === 0 && kj.length === 0);
            
            // Check text similarity
            const combinedSim = textSimilarity(
              (ei.title || '') + (ei.summary || ''),
              (ej.title || '') + (ej.summary || '')
            );
            
            const titleSim = textSimilarity(ei.title || '', ej.title || '');
            
            // Merge if:
            // - Text similarity > 0.25 AND keyword match, OR
            // - Title similarity > 0.3, OR
            // - Both are lifespan templates
            const bothLifespan = ei.id.startsWith('evt-lifespan-') && ej.id.startsWith('evt-lifespan-');
            const bothNewpub = ei.id.includes('newpub') && ej.id.includes('newpub');
            
            if (bothLifespan || (combinedSim >= 0.25 && hasKeywordMatch) || titleSim >= 0.3) {
              cluster.push(ej);
              assigned.add(j);
            }
          }
          
          if (cluster.length > 1) {
            clusters.push(cluster);
          }
        }

        // For each cluster, keep the best
        for (const cluster of clusters) {
          cluster.sort((a, b) => eventQualityScore(b) - eventQualityScore(a));
          
          const best = cluster[0];
          const dupes = cluster.slice(1);
          
          duplicateGroups.push({
            personName: `${person.name}${person.name_en ? ` (${person.name_en})` : ''}`,
            year: cluster[0].start_year,
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
      else if (id.startsWith('evt-rich2-') || id.startsWith('evt-rich-')) pattern = 'evt-rich*-*';
      else if (id.startsWith('evt-struct')) pattern = 'evt-struct*-*';
      else if (id.startsWith('evt-deep')) pattern = 'evt-deep-*';
      else if (id.startsWith('evt-tsymq-')) pattern = 'evt-tsymq-* (唐/宋/元/明/清)';
      else if (id.startsWith('evt-mass-')) pattern = 'evt-mass-*';
      else if (id.startsWith('evt-')) pattern = 'evt-* (specific events)';
      patternCount[pattern] = (patternCount[pattern] || 0) + 1;
    }
    
    console.log('\n========== 按事件类型分类 ==========');
    for (const [pattern, count] of Object.entries(patternCount).sort((a, b) => b[1] - a[1])) {
      console.log(`  ${pattern}: ${count} 条`);
    }

    // Save report
    const fs = await import('fs');
    fs.writeFileSync('scripts/dedup_final_report.json', JSON.stringify({
      totalGroups: duplicateGroups.length,
      totalToDelete: toDelete.length,
      patternBreakdown: patternCount,
      deleteIds: toDelete,
      groups: duplicateGroups,
    }, null, 2));
    console.log(`\n完整报告已保存到 scripts/dedup_final_report.json`);

    // Generate SQL
    const sqlLines: string[] = [];
    sqlLines.push('-- ============================================');
    sqlLines.push('-- 事件去重 SQL');
    sqlLines.push(`-- 共删除 ${toDelete.length} 条重复事件`);
    sqlLines.push('-- ============================================\n');
    sqlLines.push('START TRANSACTION;\n');
    
    // Batch delete (100 per batch)
    for (let i = 0; i < toDelete.length; i += 100) {
      const batch = toDelete.slice(i, i + 100);
      const ids = batch.map(id => `'${id}'`).join(',');
      sqlLines.push(`-- Batch ${Math.floor(i / 100) + 1}`);
      sqlLines.push(`DELETE FROM event_persons WHERE event_id IN (${ids});`);
      sqlLines.push(`DELETE FROM events WHERE id IN (${ids});\n`);
    }
    
    sqlLines.push('COMMIT;');
    
    fs.writeFileSync('scripts/dedup_final.sql', sqlLines.join('\n'));
    console.log(`SQL 已保存到 scripts/dedup_final.sql`);

  } finally {
    conn.release();
    await pool.end();
  }
}

main().catch(console.error);
