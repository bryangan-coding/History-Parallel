/**
 * 大规模模板事件清理
 * 
 * 目标：删除 evt-lifespan-*、evt-struct*-*、evt-rich*-* 中的重复模板
 * 
 * 安全策略：
 * - 仅当同一人物在同年有其他非模板事件时才删除模板
 * - 如果模板是该人物在该年份的唯一事件，保留它
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

async function main() {
  const conn = await pool.getConnection();
  
  try {
    // Find lifespan events where the same person has another non-lifespan event in the same year
    console.log('查找可删除的模板事件...');
    
    const [rows] = await conn.query<mysql.RowDataPacket[]>(`
      SELECT DISTINCT e.id, e.title, e.start_year, p.name
      FROM events e
      INNER JOIN event_persons ep ON e.id = ep.event_id
      INNER JOIN people p ON ep.person_id = p.id
      WHERE e.data_status = 'published'
      AND (
        e.id LIKE 'evt-lifespan-%'
        OR e.id LIKE 'evt-struct%'
        OR e.id LIKE 'evt-rich%'
        OR e.id LIKE 'evt-rich2%'
        OR e.id LIKE 'evt-struct3%'
      )
      AND EXISTS (
        SELECT 1 FROM events e2
        INNER JOIN event_persons ep2 ON e2.id = ep2.event_id
        WHERE ep2.person_id = ep.person_id
        AND e2.start_year = e.start_year
        AND e2.id != e.id
        AND e2.id NOT LIKE 'evt-lifespan-%'
        AND e2.id NOT LIKE 'evt-struct%'
        AND e2.id NOT LIKE 'evt-rich%'
        AND e2.id NOT LIKE 'evt-rich2%'
        AND e2.id NOT LIKE 'evt-struct3%'
        AND e2.data_status = 'published'
      )
      ORDER BY p.name, e.start_year
    `);
    
    const toDelete = rows as any[];
    console.log(`找到 ${toDelete.length} 条可删除的模板事件\n`);

    // Show some examples
    const sample = toDelete.slice(0, 30);
    console.log('示例（前30条）:');
    for (const r of sample) {
      console.log(`  [${r.id}] ${r.name} ${r.start_year}年 - "${r.title}"`);
    }

    // Group by ID pattern
    const patternCount: Record<string, number> = {};
    for (const r of toDelete) {
      let pattern = 'other';
      if (r.id.startsWith('evt-lifespan-')) pattern = 'evt-lifespan-*';
      else if (r.id.startsWith('evt-struct3-')) pattern = 'evt-struct3-*';
      else if (r.id.startsWith('evt-struct-')) pattern = 'evt-struct-*';
      else if (r.id.startsWith('evt-rich2-')) pattern = 'evt-rich2-*';
      else if (r.id.startsWith('evt-rich-')) pattern = 'evt-rich-*';
      patternCount[pattern] = (patternCount[pattern] || 0) + 1;
    }
    
    console.log('\n按类型分布:');
    for (const [p, c] of Object.entries(patternCount).sort((a, b) => b[1] - a[1])) {
      console.log(`  ${p}: ${c} 条`);
    }

    // Save
    const fs = await import('fs');
    fs.writeFileSync('scripts/template_cleanup_report.json', JSON.stringify({
      totalToDelete: toDelete.length,
      patternBreakdown: patternCount,
      deleteIds: toDelete.map((r: any) => r.id),
    }, null, 2));

    // Generate SQL
    const deleteIds = toDelete.map((r: any) => r.id);
    const sqlLines: string[] = [
      '-- ============================================',
      '-- 模板事件清理',
      `-- 共删除 ${deleteIds.length} 条`,
      '-- 仅删除那些同一人物同年有更好事件的模板',
      '-- ============================================',
      '',
      'START TRANSACTION;',
      '',
    ];
    
    for (let i = 0; i < deleteIds.length; i += 100) {
      const batch = deleteIds.slice(i, i + 100);
      const ids = batch.map((id: string) => `'${id.replace(/'/g, "\\'")}'`).join(',');
      sqlLines.push(`-- Batch ${Math.floor(i / 100) + 1}`);
      sqlLines.push(`DELETE FROM event_persons WHERE event_id IN (${ids});`);
      sqlLines.push(`DELETE FROM events WHERE id IN (${ids});`);
      sqlLines.push('');
    }
    
    sqlLines.push('COMMIT;');
    
    fs.writeFileSync('scripts/template_cleanup.sql', sqlLines.join('\n'));
    console.log(`\nSQL 已保存到 scripts/template_cleanup.sql`);

  } finally {
    conn.release();
    await pool.end();
  }
}

main().catch(console.error);
