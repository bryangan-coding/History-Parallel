const mysql = require('mysql2/promise');
(async () => {
  const pool = await mysql.createPool({
    host: 'localhost', port: 3307, user: 'root', password: undefined,
    database: 'history_parallel', charset: 'utf8mb4',
    socketPath: '/tmp/mysql.sock'
  });

  console.log('=== 有importance>=4事件的人物 TOP 30 ===');
  const [important] = await pool.query(`
    SELECT p.name, p.birth_year, p.death_year, COUNT(DISTINCT e.id) as evt_cnt,
           MAX(e.importance) as max_imp
    FROM people p
    INNER JOIN event_persons ep ON p.id = ep.person_id
    INNER JOIN events e ON ep.event_id = e.id AND e.data_status = 'published'
    WHERE p.data_status = 'published'
    GROUP BY p.id, p.name, p.birth_year, p.death_year
    HAVING max_imp >= 4
    ORDER BY evt_cnt DESC
    LIMIT 30
  `);
  important.forEach(r => console.log(r.name + ' (' + r.birth_year + '-' + r.death_year + '): ' + r.evt_cnt + ' events, max_imp=' + r.max_imp));

  console.log('\n=== 高评分但事件数很少的人物 TOP 20 ===');
  const [highScore] = await pool.query(`
    SELECT p.name, p.birth_year, p.death_year, p.confidence_score, p.occupations,
           COUNT(ep.event_id) as evt_cnt
    FROM people p
    LEFT JOIN event_persons ep ON p.id = ep.person_id
    LEFT JOIN events e ON ep.event_id = e.id AND e.data_status = 'published'
    WHERE p.data_status = 'published' AND p.confidence_score >= 0.9
    GROUP BY p.id, p.name, p.birth_year, p.death_year, p.confidence_score, p.occupations
    HAVING evt_cnt <= 3
    ORDER BY p.confidence_score DESC
    LIMIT 20
  `);
  highScore.forEach(r => console.log(r.name + ' (' + r.birth_year + '-' + r.death_year + '), score=' + r.confidence_score + ', occ=' + r.occupations + ', events=' + r.evt_cnt));

  console.log('\n=== 分布统计 ===');
  const [stats] = await pool.query(`
    SELECT 
      COUNT(*) as total_people,
      SUM(CASE WHEN evt_cnt >= 4 THEN 1 ELSE 0 END) as has_4plus,
      SUM(CASE WHEN evt_cnt >= 4 AND imp3_cnt >= 2 THEN 1 ELSE 0 END) as has_quality,
      SUM(CASE WHEN evt_cnt >= 6 AND imp3_cnt >= 3 THEN 1 ELSE 0 END) as good_coverage
    FROM (
      SELECT p.id,
        COUNT(ep.event_id) as evt_cnt,
        SUM(CASE WHEN e.importance >= 3 THEN 1 ELSE 0 END) as imp3_cnt
      FROM people p
      LEFT JOIN event_persons ep ON p.id = ep.person_id
      LEFT JOIN events e ON ep.event_id = e.id AND e.data_status = 'published'
      WHERE p.data_status = 'published'
        AND p.birth_year IS NOT NULL
        AND p.death_year IS NOT NULL
      GROUP BY p.id
    ) sub
  `);
  const s = stats[0];
  console.log('有生卒年人物: ' + s.total_people);
  console.log('有4+事件: ' + s.has_4plus + ' (' + (s.has_4plus/s.total_people*100).toFixed(1) + '%)');
  console.log('4+事件且2+条importance>=3: ' + s.has_quality);
  console.log('6+事件且3+条importance>=3: ' + s.good_coverage);

  // Tags distribution
  console.log('\n=== 事件tags分布 TOP 20 ===');
  const [tags] = await pool.query(`
    SELECT tag, COUNT(*) as cnt FROM (
      SELECT JSON_UNQUOTE(JSON_EXTRACT(tags, CONCAT('$[', idx, ']'))) as tag
      FROM events
      JOIN (
        SELECT 0 AS idx UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4
        UNION SELECT 5 UNION SELECT 6 UNION SELECT 7
      ) AS numbers
      WHERE data_status = 'published' AND tags IS NOT NULL
    ) sub
    WHERE tag IS NOT NULL AND tag != ''
    GROUP BY tag
    ORDER BY cnt DESC
    LIMIT 20
  `);
  tags.forEach(r => console.log(r.tag + ': ' + r.cnt));

  await pool.end();
})();
