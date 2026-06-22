/**
 * 从 fthux/Characters_of_the_Three_Kingdoms 导入三国人物数据
 * 
 * 数据来源：https://github.com/fthux/Characters_of_the_Three_Kingdoms
 * 许可证：MIT License - Copyright (c) 2018-present, fthux
 * 
 * 该数据源整理了维基百科、百度百科的三国人物结构化数据
 */

import mysql from 'mysql2/promise';
import { v4 as uuidv4 } from 'uuid';

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

interface CharacterData {
  name: string;
  courtesyName?: string | null;
  pseudonym?: (string | null)[] | null;
  aliase?: { name: string; desc: string | null }[] | null;
  gender?: number;
  faction?: string;
  birthdate?: string | null;
  birthplace?: string;
  birthplacePresentDay?: string;
  deathdate?: string | null;
  deathplace?: string;
  deathplacePresentDay?: string;
  position?: string[];
  peerage?: string[];
  posthumousName?: string[];
  templeName?: string[];
  monarch?: string[];
  historicalBriefIIntroduction?: string;
  novelisticBriefIIntroduction?: string;
  family?: {
    father?: { character?: { name: string }[]; desc?: string | null };
    mother?: { character?: { name: string }[]; desc?: string | null };
    brothers?: { character?: { name: string }[]; desc?: string | null };
    sisters?: { character?: { name: string }[]; desc?: string | null };
    spouse?: { character?: { name: string }[]; desc?: string | null };
    sons?: { character?: { name: string }[]; desc?: string | null };
    daughters?: { character?: { name: string }[]; desc?: string | null };
  };
  historicalEvaluations?: string[];
}

function parseYear(dateStr: string | null | undefined): number | undefined {
  if (!dateStr) return undefined;
  const match = dateStr.match(/(-?\d+)\s*年/);
  if (match) return parseInt(match[1], 10);
  const numMatch = dateStr.match(/^(-?\d+)/);
  if (numMatch) return parseInt(numMatch[1], 10);
  return undefined;
}

function generatePersonId(name: string): string {
  // Generate a stable ID from the Chinese name
  return `tk-${name}`;
}

function generateEventId(personId: string, type: string): string {
  return `tk-${personId}-${type}-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 6)}`;
}

async function importCharacter(data: CharacterData, conn: mysql.PoolConnection): Promise<boolean> {
  const personId = generatePersonId(data.name);
  const birthYear = parseYear(data.birthdate);
  const deathYear = parseYear(data.deathdate);

  // Check if person already exists
  const [existing] = await conn.query<mysql.RowDataPacket[]>(
    'SELECT id FROM people WHERE id = ?', [personId]
  );
  if (existing.length > 0) {
    console.log(`  ⏭ ${data.name} 已存在，跳过`);
    return false;
  }

  // Build alternative names
  const altNames: string[] = [];
  if (data.courtesyName) altNames.push(data.courtesyName);
  if (data.pseudonym) {
    for (const p of data.pseudonym) {
      if (p) altNames.push(p);
    }
  }
  if (data.aliase) {
    for (const a of data.aliase) {
      if (a.name && a.name !== data.name) altNames.push(a.name);
    }
  }

  // Build summary
  const summary = data.historicalBriefIIntroduction || data.novelisticBriefIIntroduction || '';

  // Build occupations/tags
  const occupations: string[] = [];
  const tags: string[] = ['三国'];
  if (data.position) {
    occupations.push(...data.position);
    tags.push(...data.position);
  }
  if (data.faction) tags.push(data.faction);

  // Insert person
  try {
    await conn.query(
      `INSERT INTO people (id, name, alternative_names, birth_year, death_year, 
       birth_date_precision, death_date_precision, region_id, occupations, tags,
       summary, description, data_status, confidence_score, source_ids)
       VALUES (?, ?, ?, ?, ?, 'year', 'year', 'han-dynasty', ?, ?, ?, ?, 'published', 0.7, ?)`,
      [
        personId,
        data.name,
        JSON.stringify(altNames),
        birthYear ?? null,
        deathYear ?? null,
        JSON.stringify(occupations),
        JSON.stringify(tags),
        summary.substring(0, 500),
        summary,
        JSON.stringify(['src-three-kingdoms']),
      ]
    );

    // Create events from the character data
    const events: { title: string; startYear: number; endYear?: number; summary: string; importance: 1|2|3|4|5 }[] = [];

    // Birth event
    if (birthYear) {
      events.push({
        title: `${data.name}出生`,
        startYear: birthYear,
        summary: data.birthplacePresentDay
          ? `${data.name}出生于${data.birthplace || ''}（今${data.birthplacePresentDay}）`
          : `${data.name}出生于${data.birthplace || '不详之地'}`,
        importance: 2,
      });
    }

    // Main career event
    if (data.historicalBriefIIntroduction) {
      const intro = data.historicalBriefIIntroduction;
      // Extract key events from the biography
      const sentences = intro.split(/[。；;]/).filter((s: string) => s.trim().length > 10);
      if (sentences.length > 0) {
        const firstSentence = sentences[0];
        const year = birthYear ? birthYear + 30 : undefined; // approximate career start
        if (year) {
          events.push({
            title: `${data.name}的主要事迹`,
            startYear: year,
            summary: firstSentence.trim(),
            importance: 3,
          });
        }
      }
    }

    // Death event
    if (deathYear) {
      events.push({
        title: `${data.name}逝世`,
        startYear: deathYear,
        summary: data.deathplacePresentDay
          ? `${data.name}逝世于${data.deathplace || ''}（今${data.deathplacePresentDay}）`
          : `${data.name}逝世于${data.deathplace || '不详之地'}`,
        importance: 3,
      });
    }

    // Insert events
    for (const evt of events) {
      const eventId = generateEventId(personId, evt.title.substring(0, 4));
      await conn.query(
        `INSERT INTO events (id, title, start_year, end_year, summary, importance, 
         data_status, confidence_score, source_ids, tags)
         VALUES (?, ?, ?, ?, ?, ?, 'published', 0.7, ?, ?)`,
        [
          eventId,
          evt.title,
          evt.startYear,
          evt.endYear ?? null,
          evt.summary,
          evt.importance,
          JSON.stringify(['src-three-kingdoms']),
          JSON.stringify(['三国']),
        ]
      );

      // Link event to person
      await conn.query(
        'INSERT INTO event_persons (event_id, person_id) VALUES (?, ?)',
        [eventId, personId]
      );
    }

    console.log(`  ✓ ${data.name} (${birthYear || '?'}–${deathYear || '?'}) ${events.length} 事件`);
    return true;
  } catch (e: any) {
    console.error(`  ✗ ${data.name} 导入失败:`, e.message?.substring(0, 100));
    return false;
  }
}

async function main() {
  const conn = await pool.getConnection();

  try {
    // List of all character files from the GitHub API
    const characterFiles = [
      '曹操', '刘备', '刘宠', '刘岱', '刘宏', '刘琦', '刘表', '刘陶', '刘陶2',
      '刘焉', '刘繇', '刘虞', '刘舆', '孙权', '张宝', '张苞', '张布', '张超',
      '张承1', '张承2', '张纯', '张达', '张当', '张道陵', '张飞', '张郃', '张横',
      '张衡', '张虎', '张华', '张既', '张济', '张俭', '张角', '张缉', '张津',
      '张举', '张峻', '张钧', '张闿', '张梁', '张辽', '张鲁', '张茂', '张弥',
      '张南1', '张南2', '张让', '张任', '张绍', '张世平', '张爽', '张松', '张肃',
      '张特', '张悌', '张统', '张卫', '张温1', '张温2', '张武', '张象', '张绣',
      '张休', '张勋', '张燕', '张杨', '张嶷', '张裔', '张翼', '张音', '张英',
      '张邈', '张纮', '张允', '张昭', '张著', '张遵', '张约', '诸葛亮',
    ];

    console.log(`准备导入 ${characterFiles.length} 个三国人物\n`);

    let imported = 0;
    let skipped = 0;
    let failed = 0;

    for (const name of characterFiles) {
      try {
        const url = `https://raw.githubusercontent.com/fthux/Characters_of_the_Three_Kingdoms/master/characters/${encodeURIComponent(name)}.json`;
        const response = await fetch(url);
        if (!response.ok) {
          console.log(`  ⚠ ${name}: HTTP ${response.status}`);
          failed++;
          continue;
        }
        const data: CharacterData = await response.json();
        const result = await importCharacter(data, conn);
        if (result) imported++;
        else skipped++;
      } catch (e: any) {
        console.error(`  ✗ ${name}: ${e.message?.substring(0, 80)}`);
        failed++;
      }
    }

    console.log(`\n========== 导入完成 ==========`);
    console.log(`成功导入: ${imported}`);
    console.log(`已存在跳过: ${skipped}`);
    console.log(`失败: ${failed}`);

    // Add source record
    const [existingSource] = await conn.query<mysql.RowDataPacket[]>(
      "SELECT id FROM sources WHERE id = 'src-three-kingdoms'"
    );
    if (existingSource.length === 0) {
      await conn.query(
        `INSERT INTO sources (id, title, url, note, license)
         VALUES ('src-three-kingdoms', 'Characters of the Three Kingdoms',
         'https://github.com/fthux/Characters_of_the_Three_Kingdoms',
         '三国人物结构化数据，整理自维基百科、百度百科',
         'MIT License - Copyright (c) 2018-present, fthux')`
      );
      console.log('✓ 已添加数据来源记录');
    }

  } finally {
    conn.release();
    await pool.end();
  }
}

main().catch(console.error);
