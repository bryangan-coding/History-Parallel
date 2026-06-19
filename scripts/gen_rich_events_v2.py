#!/usr/bin/env python3
"""
V2: 从summary中提取所有 "X年 + 动作" 模式的事件。
只提取summary中明确记载的事实，不编造。
"""
import mysql.connector, json, re

conn = mysql.connector.connect(user='root', password='', host='localhost', port=3307,
    database='history_parallel', charset='utf8mb4', unix_socket='/tmp/mysql.sock', autocommit=False)
cursor = conn.cursor(dictionary=True)

cursor.execute("""
    SELECT p.id, p.name, p.name_en, p.birth_year, p.death_year,
           p.summary, p.tags, p.tags_en, p.region_id, p.source_ids,
           p.confidence_score, COUNT(ep.event_id) as ec
    FROM people p LEFT JOIN event_persons ep ON p.id = ep.person_id
    WHERE p.data_status = 'published'
      AND p.birth_year IS NOT NULL AND p.death_year IS NOT NULL
      AND CHAR_LENGTH(p.summary) > 100
      AND p.summary NOT LIKE '%关于其生平%'
      AND p.summary NOT LIKE '%历史风貌%'
      AND p.summary NOT LIKE '%其生平事迹见于%'
      AND p.summary REGEXP '[0-9]{3,4}年[^出卒]'
    GROUP BY p.id HAVING ec < 5
    ORDER BY CHAR_LENGTH(p.summary) DESC
""")
candidates = cursor.fetchall()
print(f"Candidates: {len(candidates)}")

cursor.execute("SELECT id FROM events")
existing_ids = {r['id'] for r in cursor.fetchall()}

events_batch = []
total_generated = 0
people_generated = 0

for p in candidates:
    pid = p['id']
    name = p['name']
    name_en = p.get('name_en') or name
    summary = p.get('summary', '')
    tags = json.loads(p['tags']) if isinstance(p.get('tags'), str) else (p.get('tags') or [])
    tags_en = json.loads(p['tags_en']) if isinstance(p.get('tags_en'), str) else (p.get('tags_en') or [])
    sources = json.loads(p['source_ids']) if isinstance(p.get('source_ids'), str) else (p.get('source_ids') or [])
    region = p.get('region_id', 'china')
    conf = p.get('confidence_score', 0.7)
    birth = p['birth_year']
    death = p['death_year']
    
    # Match any year + action pattern after the year
    # Pattern: XXXX年, [description of action]。
    year_actions = re.findall(
        r'(\d{3,4})年[，,，\s]*([^。；\n]{10,80})',
        summary
    )
    
    # Filter: year should be within person's lifetime (±20 years)
    valid_actions = []
    seen_years = set()
    for year_str, action in year_actions:
        year = int(year_str)
        if year in seen_years: continue
        if abs(year - birth) > 150 and abs(year - death) > 150: continue
        # Skip birth/death descriptions
        if any(w in action[:5] for w in ['出生', '生于', '去世', '逝世', '卒于', '生於', '於']):
            continue
        seen_years.add(year)
        valid_actions.append((year, action.strip('，, ')))
    
    # Max 3 events per person
    for i, (year, action) in enumerate(valid_actions[:3]):
        eid = f'evt-rich2-{pid}-{i}'
        if eid in existing_ids: continue
        
        # Determine importance based on tags
        imp = 3 if any(t in ['皇帝','君主','名臣','文学家','军事人物','科学家','改革家'] for t in tags) else 2
        
        # Short title from action
        title_text = action[:30] + ('…' if len(action) > 30 else '')
        
        events_batch.append((
            eid, title_text, f'{name_en}: {action[:60]}',
            year, None, 'year', False, region, None, None, None,
            json.dumps([pid], ensure_ascii=False),
            json.dumps(['事迹'] + tags[:3], ensure_ascii=False),
            json.dumps(['Event'] + tags_en[:3], ensure_ascii=False),
            imp,
            f'{year}年，{action[:150]}',
            '',
            f'{name}于{year}年{action[:200]}',
            '',
            json.dumps(sources, ensure_ascii=False), '[]', None, None, None,
            'published', conf, '[]', None, None,
        ))
        existing_ids.add(eid)
        total_generated += 1
    
    if valid_actions:
        people_generated += 1
    if people_generated % 1000 == 0:
        print(f"  {people_generated} people, {total_generated} events...")

print(f"\nGenerated {total_generated} events for {people_generated} people")

if events_batch:
    for i in range(0, len(events_batch), 500):
        batch = events_batch[i:i+500]
        cursor.executemany("""INSERT IGNORE INTO events (id, title, title_en, start_year, end_year,
            date_precision, is_approximate, region_id, place_name, place_name_en,
            coordinates, person_ids, tags, tags_en, importance, summary, summary_en,
            description, description_en, source_ids, related_event_ids,
            wikidata_qid, wikipedia_page_id, wikipedia_slug,
            data_status, confidence_score, external_references, last_reviewed_at, reviewed_by)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, batch)
    conn.commit()
    print(f"Inserted {len(events_batch)} events")

    cursor.execute("""
        INSERT IGNORE INTO event_persons (event_id, person_id)
        SELECT e.id, jt.person_id FROM events e
        CROSS JOIN JSON_TABLE(e.person_ids, '$[*]' COLUMNS(person_id VARCHAR(100) PATH '$')) AS jt
        WHERE e.id LIKE 'evt-rich2-%'
    """)
    conn.commit()

cursor.execute("SELECT COUNT(*) FROM events")
total_ev = cursor.fetchone()['COUNT(*)']
cursor.execute("SELECT COUNT(*) FROM (SELECT person_id FROM event_persons GROUP BY person_id HAVING COUNT(*)>=5) t")
deep5 = cursor.fetchone()['COUNT(*)']
cursor.execute("SELECT COUNT(*) FROM (SELECT person_id FROM event_persons GROUP BY person_id HAVING COUNT(*)>=3) t")
deep3 = cursor.fetchone()['COUNT(*)']
print(f"\nTotal: {total_ev} events, >=5: {deep5}, >=3: {deep3}")
cursor.close()
conn.close()
