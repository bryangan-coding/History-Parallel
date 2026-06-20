const mysql = require('mysql2/promise');
(async () => {
  const pool = await mysql.createPool({
    host: 'localhost', port: 3307, user: 'root', password: undefined,
    database: 'history_parallel', charset: 'utf8mb4',
    socketPath: '/tmp/mysql.sock'
  });

  // 按朝代查询 - 通过出生年份范围筛选
  const eras = [
    {name: '唐', min: 618, max: 907},
    {name: '宋', min: 960, max: 1279},
    {name: '元', min: 1271, max: 1368},
    {name: '明', min: 1368, max: 1644},
    {name: '清', min: 1644, max: 1912},
  ];

  for (const era of eras) {
    console.log(`\n=== ${era.name}朝名人 ===`);
    
    // 找出每个朝代事件最多的人物
    const [top] = await pool.query(`
      SELECT p.name, p.id, p.birth_year, p.death_year, p.occupations,
             COUNT(ep.event_id) as evt_cnt,
             GROUP_CONCAT(e.title ORDER BY e.start_year SEPARATOR ' | ') as titles
      FROM people p
      INNER JOIN event_persons ep ON p.id = ep.person_id
      INNER JOIN events e ON ep.event_id = e.id AND e.data_status = 'published'
      WHERE p.data_status = 'published'
        AND p.birth_year IS NOT NULL
        AND p.birth_year >= ?
        AND (p.birth_year < ? OR p.death_year < ?)
      GROUP BY p.id, p.name, p.birth_year, p.death_year, p.occupations
      HAVING evt_cnt >= 3
      ORDER BY evt_cnt DESC
      LIMIT 30
    `, [era.min, era.max, era.max + 50]);

    top.forEach(r => {
      const titles = r.titles ? r.titles.split(' | ').splice(0, 6).join(' | ') : '';
      console.log(`  ${r.name} (${r.birth_year}-${r.death_year}) [${r.evt_cnt} evts]: ${titles}`);
    });

    // Count how many people have too few events
    const [stats] = await pool.query(`
      SELECT 
        SUM(CASE WHEN evt_cnt <= 2 THEN 1 ELSE 0 END) as basic,
        SUM(CASE WHEN evt_cnt BETWEEN 3 AND 5 THEN 1 ELSE 0 END) as medium,
        SUM(CASE WHEN evt_cnt >= 6 THEN 1 ELSE 0 END) as good,
        COUNT(*) as total
      FROM (
        SELECT p.id, COUNT(ep.event_id) as evt_cnt
        FROM people p
        LEFT JOIN event_persons ep ON p.id = ep.person_id
        INNER JOIN events e ON ep.event_id = e.id AND e.data_status = 'published'
        WHERE p.data_status = 'published'
          AND p.birth_year IS NOT NULL
          AND p.birth_year >= ?
          AND (p.birth_year < ? OR p.death_year < ?)
        GROUP BY p.id
      ) sub
    `, [era.min, era.max, era.max + 50]);
    console.log(`  分布: ≤2事件=${stats[0].basic}, 3-5=${stats[0].medium}, 6+=${stats[0].good}, 总计=${stats[0].total}`);
  }

  await pool.end();
})();
