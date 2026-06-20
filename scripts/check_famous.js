const mysql = require('mysql2/promise');
(async () => {
  const pool = await mysql.createPool({
    host: 'localhost', port: 3307, user: 'root', password: undefined,
    database: 'history_parallel', charset: 'utf8mb4',
    socketPath: '/tmp/mysql.sock'
  });

  // 唐/宋/元/明/清 真正名人
  const famous = [
    // 唐
    '李白', '杜甫', '白居易', '王维', '韩愈', '柳宗元', '李商隐', '杜牧',
    '李世民(唐太宗)', '武则天', '魏征', '李靖', '郭子仪', '颜真卿', '吴道子',
    // 宋
    '苏轼', '王安石', '欧阳修', '司马光', '辛弃疾', '陆游',
    '李清照', '岳飞', '范仲淹', '文天祥', '朱熹', '沈括',
    // 元
    '关汉卿', '赵孟頫', '郭守敬', '马致远', '王实甫',
    // 明
    '朱元璋(明太祖)', '朱棣(明成祖)', '王守仁(王阳明)', '张居正', '戚继光',
    '郑和', '海瑞', '徐光启', '汤显祖', '唐寅', '徐渭', '郑板桥',
    // 清
    '康熙(清圣祖)', '乾隆(清高宗)', '林则徐', '曾国藩', '李鸿章',
    '左宗棠', '曹雪芹', '蒲松龄', '龚自珍', '纪昀(纪晓岚)',
  ];

  console.log('=== 五代名人当前事件 ===');
  for (const name of famous) {
    const [person] = await pool.query(
      'SELECT id, name, birth_year, death_year FROM people WHERE name = ? AND data_status = "published"', [name]
    );
    if (!person.length) {
      console.log(`NOT FOUND: ${name}`);
      continue;
    }
    const p = person[0];
    const [events] = await pool.query(`
      SELECT e.title, e.start_year, e.importance, e.summary
      FROM events e
      INNER JOIN event_persons ep ON e.id = ep.event_id
      WHERE ep.person_id = ? AND e.data_status = 'published'
      ORDER BY e.start_year
    `, [p.id]);
    
    const nonBirth = events.filter(e => !e.title.includes('出生') && !e.title.includes('逝世'));
    console.log(`\n${p.name} (${p.birth_year}-${p.death_year}): ${events.length} events total, ${nonBirth.length} non-birth`);
    events.forEach(e => console.log(`  ${e.start_year} | imp=${e.importance} | ${e.title} | ${(e.summary||'').substring(0,80)}`));
  }

  await pool.end();
})();
