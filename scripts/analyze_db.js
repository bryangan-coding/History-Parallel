const mysql = require('mysql2/promise');
(async () => {
  const pool = await mysql.createPool({
    host: 'localhost', port: 3307, user: 'root', password: undefined,
    database: 'history_parallel', charset: 'utf8mb4',
    socketPath: '/tmp/mysql.sock'
  });

  // ===== 1. 人物-事件分布 =====
  const [pTotal] = await pool.query("SELECT COUNT(*) as cnt FROM people WHERE data_status='published'");
  console.log('=== 人物-事件分布 ===');
  console.log('Published people:', pTotal[0].cnt);

  const [ec] = await pool.query(`
    SELECT 
      SUM(CASE WHEN cnt = 0 THEN 1 ELSE 0 END) as zero,
      SUM(CASE WHEN cnt = 1 THEN 1 ELSE 0 END) as one,
      SUM(CASE WHEN cnt BETWEEN 2 AND 3 THEN 1 ELSE 0 END) as two_three,
      SUM(CASE WHEN cnt BETWEEN 4 AND 5 THEN 1 ELSE 0 END) as four_five,
      SUM(CASE WHEN cnt BETWEEN 6 AND 10 THEN 1 ELSE 0 END) as six_ten,
      SUM(CASE WHEN cnt > 10 THEN 1 ELSE 0 END) as over_ten,
      COUNT(*) as total
    FROM (
      SELECT p.id, COUNT(ep.event_id) as cnt
      FROM people p
      LEFT JOIN event_persons ep ON p.id = ep.person_id
      INNER JOIN events e ON ep.event_id = e.id AND e.data_status = 'published'
      WHERE p.data_status = 'published'
      GROUP BY p.id
    ) sub
  `);
  const ecr = ec[0];
  console.log('0 events:', ecr.zero);
  console.log('1 event:', ecr.one);
  console.log('2-3 events:', ecr.two_three);
  console.log('4-5 events:', ecr.four_five);
  console.log('6-10 events:', ecr.six_ten);
  console.log('>10 events:', ecr.over_ten);

  // ===== 2. 模板垃圾统计 =====
  console.log('');
  console.log('=== 模板垃圾残留统计 ===');
  const patterns = [
    ['早期创作', "title LIKE '%早期创作%'"],
    ['成年立世', "title LIKE '%成年立世%'"],
    ['成长岁月', "title LIKE '%成长岁月%'"],
    ['垂暮之年', "title LIKE '%垂暮之年%'"],
    ['文风成熟', "title LIKE '%文风成熟%'"],
    ['文坛影响', "title LIKE '%文坛影响%'"],
    ['文学成就', "title LIKE '%文学成就%'"],
    ['文学风格', "title LIKE '%文学风格%'"],
    ['诗歌创作', "title LIKE '%诗歌创作%'"],
    ['史料来源', "title LIKE '%史料来源%'"],
    ['诗歌成熟', "title LIKE '%诗歌成熟%'"],
    ['历史印记', "title LIKE '%历史印记%'"],
    ['历史遗产', "title LIKE '%历史遗产%'"],
    ['时代印记', "title LIKE '%时代印记%'"],
    ['生平活动', "title LIKE '%的生平活动%'"],
    ['仕途任职', "title LIKE '%的仕途任职%'"],
    ['军事活动', "title LIKE '%的军事活动%'"],
    ['政治活动', "title LIKE '%的政治活动%'"],
    ['文学创作', "title LIKE '%文学创作%'"],
    ['代表作品', "title LIKE '%代表作品%'"],
    ['——(评价)', "title LIKE '%——%' AND title NOT LIKE '%出生%' AND title NOT LIKE '%逝世%' AND title NOT LIKE '%去世%' AND title NOT LIKE '%登基%' AND title NOT LIKE '%即位%'"],
    ['与XX社会', "title LIKE '%与%社会%'"],
    ['"留下了"模板', "summary LIKE '%留下了属于这个时代的历史印记%' OR summary LIKE '%一生为后世留下了宝贵%'"],
    ['生活与活动', "summary LIKE '%生活并参与社会活动%' OR summary LIKE '%间生活与活动%'"],
    ['生活在XX时期', "summary REGEXP '生活在[A-Za-z\\\\u4e00-\\\\u9fff]+时期'"],
  ];

  for (const [label, where] of patterns) {
    const [r] = await pool.query('SELECT COUNT(*) as cnt FROM events WHERE data_status="published" AND (' + where + ')');
    if (r[0].cnt > 0) console.log(label + ': ' + r[0].cnt + ' 条');
  }

  // ===== 3. 独特事件数（所有模板垃圾去重） =====
  const allWheres = patterns.map(p => '(' + p[1] + ')').join(' OR ');
  const [uniq] = await pool.query('SELECT COUNT(DISTINCT id) as cnt FROM events WHERE data_status="published" AND (' + allWheres + ')');
  console.log('');
  console.log('去重后模板垃圾总数: ' + uniq[0].cnt);

  // ===== 4. 事件去重（同标题同人物） =====
  const [dups] = await pool.query(`
    SELECT COUNT(*) as cnt FROM (
      SELECT e.title, ep.person_id, COUNT(*) as cnt
      FROM events e
      INNER JOIN event_persons ep ON e.id = ep.event_id
      WHERE e.data_status = 'published'
      GROUP BY e.title, ep.person_id
      HAVING COUNT(*) > 1
    ) d
  `);
  console.log('');
  console.log('重复事件（同人同标题）: ' + dups[0].cnt + ' 组');

  // ===== 5. 质量评级分布 =====
  const [qual] = await pool.query(`
    SELECT 
      SUM(CASE WHEN summary IS NULL OR summary = '' OR LENGTH(summary) < 20 THEN 1 ELSE 0 END) as no_summary,
      SUM(CASE WHEN LENGTH(summary) >= 20 AND LENGTH(summary) < 50 THEN 1 ELSE 0 END) as short_summary,
      SUM(CASE WHEN LENGTH(summary) >= 50 AND LENGTH(summary) < 100 THEN 1 ELSE 0 END) as medium_summary,
      SUM(CASE WHEN LENGTH(summary) >= 100 THEN 1 ELSE 0 END) as long_summary,
      COUNT(*) as total
    FROM events WHERE data_status = 'published'
  `);
  const qr = qual[0];
  console.log('');
  console.log('=== 事件摘要长度分布 ===');
  console.log('无摘要/极短(<20字):', qr.no_summary);
  console.log('简短(20-50字):', qr.short_summary);
  console.log('中等(50-100字):', qr.medium_summary);
  console.log('详细(≥100字):', qr.long_summary);

  // ===== 6. 出生/逝世事件占比 =====
  const [birthDeath] = await pool.query(`
    SELECT COUNT(*) as cnt FROM events 
    WHERE data_status='published' AND (title LIKE '%出生%' OR title LIKE '%逝世%' OR title LIKE '%去世%')
  `);
  console.log('');
  console.log('出生/逝世事件: ' + birthDeath[0].cnt);

  const [total] = await pool.query("SELECT COUNT(*) as cnt FROM events WHERE data_status='published'");
  console.log('已发布事件总数: ' + total[0].cnt);

  // ===== 7. 人物重要性分布 =====
  const [impDist] = await pool.query(`
    SELECT importance, COUNT(*) as cnt FROM events
    WHERE data_status = 'published' AND start_year IS NOT NULL
    GROUP BY importance
    ORDER BY importance
  `);
  console.log('');
  console.log('=== 事件重要性分布 ===');
  impDist.forEach(r => console.log('  Importance ' + r.importance + ': ' + r.cnt));

  await pool.end();
})();
