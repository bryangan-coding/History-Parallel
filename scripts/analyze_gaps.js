const mysql = require('mysql2/promise');
(async () => {
  const pool = await mysql.createPool({
    host: 'localhost', port: 3307, user: 'root', password: undefined,
    database: 'history_parallel', charset: 'utf8mb4',
    socketPath: '/tmp/mysql.sock'
  });

  // Find people with high confidence_score but very few non-birth events
  console.log('=== 高评分人物：≤2条非出生逝世事件 ===');
  const [highScore] = await pool.query(`
    SELECT p.name, p.birth_year, p.death_year, p.confidence_score, p.occupations,
           COUNT(ep.event_id) as total_evts,
           SUM(CASE WHEN e.title NOT LIKE '%出生%' AND e.title NOT LIKE '%逝世%' AND e.title NOT LIKE '%去世%' AND e.title NOT LIKE '%生平%' THEN 1 ELSE 0 END) as non_birth
    FROM people p
    LEFT JOIN event_persons ep ON p.id = ep.person_id
    LEFT JOIN events e ON ep.event_id = e.id AND e.data_status = 'published'
    WHERE p.data_status = 'published'
      AND p.confidence_score >= 0.85
      AND p.birth_year IS NOT NULL
      AND p.death_year IS NOT NULL
    GROUP BY p.id, p.name, p.birth_year, p.death_year, p.confidence_score, p.occupations
    HAVING non_birth <= 2
    ORDER BY p.confidence_score DESC, non_birth ASC
    LIMIT 50
  `);
  highScore.forEach(r => console.log(`${r.name} (${r.birth_year}-${r.death_year}) score=${r.confidence_score} total=${r.total_evts} nonBirth=${r.non_birth} occ=${r.occupations}`));

  // People with importance >= 5 events already (very important figures) but < 5 non-birth events
  console.log('\n=== 重要性5级人物但非出生事件<5条 ===');
  const [imp5] = await pool.query(`
    SELECT p.name, p.birth_year, p.death_year,
           COUNT(ep.event_id) as total_evts,
           SUM(CASE WHEN e.title NOT LIKE '%出生%' AND e.title NOT LIKE '%逝世%' AND e.title NOT LIKE '%去世%' AND e.title NOT LIKE '%生平%' THEN 1 ELSE 0 END) as non_birth
    FROM people p
    INNER JOIN event_persons ep ON p.id = ep.person_id
    INNER JOIN events e ON ep.event_id = e.id AND e.data_status = 'published'
    WHERE p.data_status = 'published'
    GROUP BY p.id, p.name, p.birth_year, p.death_year
    HAVING MAX(e.importance) >= 5 AND non_birth < 5
    ORDER BY non_birth ASC
    LIMIT 30
  `);
  imp5.forEach(r => console.log(`${r.name} (${r.birth_year}-${r.death_year}) total=${r.total_evts} nonBirth=${r.non_birth}`));

  // 按朝代：事件不足的名人（按重要性排序）
  console.log('\n=== 宋元明清名人 ≤3条非出生事件 ===');
  const [byEra] = await pool.query(`
    SELECT p.name, p.birth_year, p.death_year, p.confidence_score,
           COUNT(ep.event_id) as total,
           SUM(CASE WHEN e.title NOT LIKE '%出生%' AND e.title NOT LIKE '%逝世%' AND e.title NOT LIKE '%去世%' AND e.title NOT LIKE '%生平%' THEN 1 ELSE 0 END) as non_birth
    FROM people p
    LEFT JOIN event_persons ep ON p.id = ep.person_id
    LEFT JOIN events e ON ep.event_id = e.id AND e.data_status = 'published'
    WHERE p.data_status = 'published'
      AND p.birth_year >= 960 AND p.death_year <= 1912
      AND p.confidence_score >= 0.8
    GROUP BY p.id, p.name, p.birth_year, p.death_year, p.confidence_score
    HAVING non_birth <= 3
    ORDER BY p.confidence_score DESC, non_birth ASC
    LIMIT 40
  `);
  byEra.forEach(r => console.log(`${r.name} (${r.birth_year}-${r.death_year}) score=${r.confidence_score} total=${r.total} nonBirth=${r.non_birth}`));

  await pool.end();
})();
