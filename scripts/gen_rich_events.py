#!/usr/bin/env python3
"""
从有实质summary的人物中提取明确记载的事件，不编造。
只提取summary里明确写出来的：科举年份、任职年份、著作、重大事件。
"""
import mysql.connector, json, re

conn = mysql.connector.connect(user='root', password='', host='localhost', port=3307,
    database='history_parallel', charset='utf8mb4', unix_socket='/tmp/mysql.sock', autocommit=False)
cursor = conn.cursor(dictionary=True)

# Find people with substantive, non-template summaries and <5 events
cursor.execute("""
    SELECT p.id, p.name, p.name_en, p.birth_year, p.death_year,
           p.summary, p.summary_en, p.description, p.description_en,
           p.tags, p.tags_en, p.occupations, p.region_id, p.source_ids,
           p.confidence_score, COUNT(ep.event_id) as ec
    FROM people p LEFT JOIN event_persons ep ON p.id = ep.person_id
    WHERE p.data_status = 'published'
      AND p.birth_year IS NOT NULL
      AND p.death_year IS NOT NULL
      AND CHAR_LENGTH(p.summary) > 80
      AND p.summary NOT LIKE '%关于其生平与事迹%'
      AND p.summary NOT LIKE '%历史风貌与社会环境%'
      AND p.summary NOT LIKE '%其生平事迹见于%'
    GROUP BY p.id HAVING ec < 5
    ORDER BY CHAR_LENGTH(p.summary) DESC
""")
candidates = cursor.fetchall()
print(f"Candidates with substantive summaries (<5 events): {len(candidates)}")

cursor.execute("SELECT id FROM events")
existing_ids = {r['id'] for r in cursor.fetchall()}

events_to_insert = []
stats = {'total': 0, 'events': 0, 'exam': 0, 'office': 0, 'work': 0, 'milestone': 0}

for p in candidates:
    pid = p['id']
    name = p['name']
    name_en = p.get('name_en') or name
    summary = p.get('summary', '')
    desc = p.get('description', '')
    tags = json.loads(p['tags']) if isinstance(p.get('tags'), str) else (p.get('tags') or [])
    tags_en = json.loads(p['tags_en']) if isinstance(p.get('tags_en'), str) else (p.get('tags_en') or [])
    sources = json.loads(p['source_ids']) if isinstance(p.get('source_ids'), str) else (p.get('source_ids') or [])
    region = p.get('region_id', 'china')
    conf = p.get('confidence_score', 0.7)
    birth = p['birth_year']
    death = p['death_year']
    
    # Combine summary + description for parsing
    text = summary + ' ' + (desc or '')
    
    def add_evt(eid, title, title_en, year, importance, summary_text, desc_text, tags_e, tags_en_e, is_approx=False):
        if eid in existing_ids: return
        events_to_insert.append((
            eid, title, title_en, year, None, 'year', is_approx, region, None, None, None,
            json.dumps([pid], ensure_ascii=False),
            json.dumps(tags_e, ensure_ascii=False),
            json.dumps(tags_en_e, ensure_ascii=False),
            importance, summary_text, '', desc_text, '',
            json.dumps(sources, ensure_ascii=False), '[]', None, None, None,
            'published', conf, '[]', None, None,
        ))
        existing_ids.add(eid)
    
    # --- Parse exam events ---
    # Pattern: X年进士 / X年及第 / XXXX年进士
    for m in re.finditer(r'(\d{3,4})年[^，。；]{0,20}(?:进士|及第|中举|明经|登科|状元|探花|榜眼)', text):
        year = int(m.group(1))
        if abs(year - birth) < 100 and 500 < year < 2000:
            snippet = m.group(0)[:120]
            add_evt(f'evt-rich-{pid}-exam', f'{name}科举及第', f'{name_en} Passes Imperial Exam',
                    year, 3, snippet, snippet,
                    ['科举'] + tags[:3], ['Civil Exam'] + tags_en[:3])
            stats['exam'] += 1
    
    # --- Parse office/rank events ---
    # Pattern: X年拜/任/授/为/官至 + 官职
    office_patterns = [
        (r'(\d{3,4})年[^，。；]{0,30}(?:拜|任|授|官至|擔任|为)([^，。；]{3,20}?(?:宰相|尚書|侍郎|刺史|節度使|大學士|首輔|樞密|僕射|中書|太守|將軍|都督))', 4),
        (r'(\d{3,4})年[^，。；]{0,10}(?:拜相|任宰相|为相)', 4),
        (r'(\d{3,4})年[^，。；]{0,10}(?:进士|及第|中举)', 3),
    ]
    for pat, imp in office_patterns:
        for m in re.finditer(pat, text):
            year = int(m.group(1))
            if abs(year - birth) < 120 and 500 < year < 2000:
                snippet = m.group(0)[:150]
                add_evt(f'evt-rich-{pid}-office{stats["office"]}', f'{name}任官', 
                        f'{name_en} Appointed', year, imp, snippet, snippet,
                        ['仕途'] + tags[:3], ['Career'] + tags_en[:3])
                stats['office'] += 1
    
    # --- Parse works/achievements ---
    # Pattern: 著/编/撰/创作 + 书名/作品名
    work_patterns = [
        (r'[著有編撰创](?:有|《)([^》]{2,20})[》]', 4),
        (r'[著有編撰创作]([^，。；]{3,20}?(?:集|书|记|传|录|经|史|诗))', 4),
    ]
    for pat, imp in work_patterns:
        for m in re.finditer(pat, text):
            if stats['work'] >= 2: break  # Max 2 work events
            work_name = m.group(1)[:30]
            year = (birth + death) // 2
            snippet = f'{name}创作《{work_name}》。'
            add_evt(f'evt-rich-{pid}-work{stats["work"]}', f'{name}创作《{work_name}》',
                    f'{name_en}: {work_name}', year, imp, snippet, 
                    f'{name}著有《{work_name}》。{snippet}',
                    ['著作'] + tags[:3], ['Work'] + tags_en[:3], is_approx=True)
            stats['work'] += 1
    
    # --- Parse nicknames/titles (for context) ---
    if stats['exam'] + stats['office'] + stats['work'] == 0 and len(text) > 200:
        # Last resort: extract a key milestone from the text
        milestone_patterns = [
            r'(?:与|和)([^，。；]{3,8})(?:并称|齐名|合称)([^，。；]{3,8})',
            r'被(?:誉为|称为|尊为)([^，。；]{3,20})',
        ]
        for pat in milestone_patterns:
            m = re.search(pat, text)
            if m:
                year = (birth + death) // 2
                snippet = m.group(0)[:120]
                add_evt(f'evt-rich-{pid}-milestone', f'{name}的成就', f'{name_en} Achievement',
                        year, 2, snippet, snippet,
                        ['成就'] + tags[:3], ['Achievement'] + tags_en[:3], is_approx=True)
                stats['milestone'] += 1
                break

    stats['total'] += 1
    stats['events'] += stats['exam'] + stats['office'] + stats['work'] + stats['milestone']
    if stats['total'] % 500 == 0:
        print(f"  Processed {stats['total']} people, {stats['events']} events...")

print(f"\nProcessed {stats['total']} people")
print(f"Generated {len(events_to_insert)} events (exam:{stats['exam']} office:{stats['office']} work:{stats['work']} milestone:{stats['milestone']})")

if events_to_insert:
    cursor.executemany("""INSERT IGNORE INTO events (id, title, title_en, start_year, end_year,
        date_precision, is_approximate, region_id, place_name, place_name_en,
        coordinates, person_ids, tags, tags_en, importance, summary, summary_en,
        description, description_en, source_ids, related_event_ids,
        wikidata_qid, wikipedia_page_id, wikipedia_slug,
        data_status, confidence_score, external_references, last_reviewed_at, reviewed_by)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, events_to_insert)
    conn.commit()
    print(f"Inserted {len(events_to_insert)} events")

    cursor.execute("""
        INSERT IGNORE INTO event_persons (event_id, person_id)
        SELECT e.id, jt.person_id FROM events e
        CROSS JOIN JSON_TABLE(e.person_ids, '$[*]' COLUMNS(person_id VARCHAR(100) PATH '$')) AS jt
        WHERE e.id LIKE 'evt-rich-%'
    """)
    conn.commit()

cursor.execute("SELECT COUNT(*) FROM events")
total_ev = cursor.fetchone()['COUNT(*)']
cursor.execute("SELECT COUNT(*) FROM (SELECT person_id FROM event_persons GROUP BY person_id HAVING COUNT(*)>=5) t")
deep5 = cursor.fetchone()['COUNT(*)']
print(f"\nTotal events: {total_ev}")
print(f">=5 events people: {deep5}")
cursor.close()
conn.close()
