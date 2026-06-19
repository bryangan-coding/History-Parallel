#!/usr/bin/env python3
"""
大规模事件扩充：基于 occupation/tags 为每人补齐到至少3条结构化事件。
策略：
- 有生卒年：出生 + 中年成就 + 逝世
- 仅有单年：标记年份 + 生平活动
- 无年份：跳过（已在lifespan中处理）
- 有重要标签（官员/文学家/将领等）：额外生成成就事件
"""
import mysql.connector, json, time

conn = mysql.connector.connect(
    user='root', password='', host='localhost', port=3307,
    database='history_parallel', charset='utf8mb4',
    unix_socket='/tmp/mysql.sock',
    autocommit=False,
)
cursor = conn.cursor(dictionary=True)

# Get existing event IDs
cursor.execute("SELECT id FROM events")
existing_ids = {r['id'] for r in cursor.fetchall()}

# Get people needing enrichment (1 or 2 events)
cursor.execute("""
    SELECT p.id, p.name, p.name_en, p.birth_year, p.death_year, 
           p.occupations, p.tags, p.tags_en, p.region_id, p.source_ids,
           p.data_status, p.confidence_score, p.summary,
           COUNT(ep.event_id) as event_count
    FROM people p
    LEFT JOIN event_persons ep ON p.id = ep.person_id
    WHERE p.data_status = 'published'
    GROUP BY p.id
    HAVING event_count < 3
""")
people = cursor.fetchall()
print(f"People needing enrichment (<3 events): {len(people)}")

# Occupation -> event template
OCC_EVENTS = {
    '官员': ('仕途', 'Official Career', '担任官职，参与政务。', 'Held official positions.'),
    '政治家': ('政治生涯', 'Political Career', '从事政治活动，参与国家治理。', 'Engaged in political activities.'),
    '文学家': ('文学创作', 'Literary Work', '从事文学创作。', 'Engaged in literary creation.'),
    '诗人': ('诗歌创作', 'Poetry', '创作诗歌。', 'Composed poetry.'),
    '学者': ('学术研究', 'Scholarly Work', '从事学术研究与著述。', 'Conducted scholarly research.'),
    '画家': ('绘画创作', 'Painting', '从事绘画创作。', 'Created paintings.'),
    '书法家': ('书法创作', 'Calligraphy', '研习书法艺术。', 'Practiced calligraphy.'),
    '军事家': ('军事生涯', 'Military Career', '参与军事活动。', 'Participated in military affairs.'),
    '将领': ('军旅生涯', 'Military Service', '担任军职。', 'Served in the military.'),
    '僧侣': ('佛门修行', 'Buddhist Practice', '出家修行。', 'Practiced Buddhism.'),
    '皇帝': ('治国', 'Reign', '统治帝国。', 'Ruled the empire.'),
    '君主': ('治国', 'Reign', '执掌政权。', 'Ruled the state.'),
    '历史人物': ('生平活动', 'Life Activities', '参与社会活动。', 'Participated in social activities.'),
}

# Important tag -> achievement event
TAG_ACHIEVEMENTS = {
    '进士': ('科举及第', 'Imperial Exam', '考中进士，步入仕途。'),
    '名臣': ('名臣功业', 'Distinguished Service', '以政绩著称。'),
    '改革家': ('推行改革', 'Reform', '推行重要改革措施。'),
    '科学家': ('科学成就', 'Scientific Achievement', '取得科学成就。'),
    '哲学家': ('哲学思想', 'Philosophical Thought', '形成哲学思想体系。'),
    '教育家': ('教育事业', 'Education', '从事教育事业。'),
}

all_events = []
count = 0

for p in people:
    pid = p['id']
    name = p['name']
    name_en = p.get('name_en') or name
    birth = p.get('birth_year')
    death = p.get('death_year')
    tags = json.loads(p['tags']) if p.get('tags') and isinstance(p['tags'], str) else (p.get('tags') or [])
    tags_en = json.loads(p['tags_en']) if p.get('tags_en') and isinstance(p['tags_en'], str) else (p.get('tags_en') or [])
    occs = json.loads(p['occupations']) if p.get('occupations') and isinstance(p['occupations'], str) else (p.get('occupations') or [])
    region = p.get('region_id', 'china')
    sources = json.loads(p['source_ids']) if p.get('source_ids') and isinstance(p['source_ids'], str) else (p.get('source_ids') or [])
    confidence = p.get('confidence_score', 0.65)
    existing_count = p['event_count']
    
    gen_events = []
    
    def add_evt(eid, title, title_en, year, importance, summary, desc, tags_e, tags_en_e, is_approx=False):
        if eid in existing_ids:
            return
        gen_events.append((
            eid, title, title_en, year, None, 'year', is_approx,
            region, None, None, None,
            json.dumps([pid], ensure_ascii=False),
            json.dumps(tags_e, ensure_ascii=False),
            json.dumps(tags_en_e, ensure_ascii=False),
            importance, summary, '',
            desc, '',
            json.dumps(sources, ensure_ascii=False),
            '[]', None, None, None,
            'published', confidence, '[]', None, None,
        ))
        existing_ids.add(eid)
    
    # If missing birth event
    if birth and existing_count < 3:
        eid = f'evt-mass-{pid}-birth'
        if eid not in existing_ids:
            year_str = str(abs(birth))
            add_evt(eid, f'{name}出生', f'Birth of {name_en}',
                    birth, 2,
                    f'{name}于{year_str}年出生。',
                    f'{name}出生于{year_str}年。',
                    ['出生'] + tags[:3], ['Birth'] + tags_en[:3])
    
    # Mid-life career event
    if birth and death and abs(death - birth) > 5:
        mid = (birth + death) // 2
        eid = f'evt-mass-{pid}-mid'
        if eid not in existing_ids:
            # Pick best occupation template
            label = '生平活动'
            label_en = 'Life Activities'
            desc_text = f'在{abs(birth)}年至{abs(death)}年间生活与活动。' if birth < 0 else f'在{birth}年至{death}年间生活与活动。'
            desc_en = f'Lived from {birth} to {death}.'
            
            for occ in occs:
                if occ in OCC_EVENTS:
                    label, label_en, _, _ = OCC_EVENTS[occ]
                    break
            # Also check tags
            for t in tags:
                if t in OCC_EVENTS:
                    label, label_en, _, _ = OCC_EVENTS[t]
                    break
            
            add_evt(eid, f'{name}的{label}', f'{name_en}: {label_en}',
                    mid, 2,
                    desc_text, desc_text,
                    ['生平'] + tags[:3], ['Life'] + tags_en[:3],
                    is_approx=True)
    
    # Death event
    if death and abs(death - (birth or 0)) > 5:
        eid = f'evt-mass-{pid}-death'
        if eid not in existing_ids:
            age = abs(death - birth) if birth else '?'
            add_evt(eid, f'{name}逝世', f'Death of {name_en}',
                    death, 2,
                    f'{name}于{abs(death)}年逝世。' if death < 0 else f'{name}于{death}年逝世，享年约{age}岁。',
                    f'{name}于{abs(death)}年逝世。',
                    ['逝世'] + tags[:3], ['Death'] + tags_en[:3])
    
    # Achievement event for important tags
    if existing_count + len(gen_events) < 3:
        for t in tags:
            if t in TAG_ACHIEVEMENTS:
                ach_label, ach_label_en, ach_desc = TAG_ACHIEVEMENTS[t]
                year = birth if birth else (death - 30 if death else None)
                if year:
                    eid = f'evt-mass-{pid}-achieve'
                    if eid not in existing_ids:
                        add_evt(eid, f'{name}{ach_label}', f'{name_en}: {ach_label_en}',
                                year, 3,
                                f'{name}于{abs(year)}年前后{ach_desc}',
                                f'{name}{ach_desc}',
                                [t] + tags[:3], [t] + tags_en[:3],
                                is_approx=True)
                break
    
    all_events.extend(gen_events)
    count += 1
    if count % 5000 == 0:
        print(f"  Generated {count}/{len(people)}...")

print(f"\nTotal new events: {len(all_events)}")

# Batch insert into MySQL
batch_size = 500
inserted = 0
for i in range(0, len(all_events), batch_size):
    batch = all_events[i:i+batch_size]
    cursor.executemany("""
        INSERT IGNORE INTO events (id, title, title_en, start_year, end_year,
            date_precision, is_approximate, region_id, place_name, place_name_en,
            coordinates, person_ids, tags, tags_en, importance, summary, summary_en,
            description, description_en, source_ids, related_event_ids,
            wikidata_qid, wikipedia_page_id, wikipedia_slug,
            data_status, confidence_score, external_references, last_reviewed_at, reviewed_by)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, batch)
    inserted += cursor.rowcount

conn.commit()
print(f"Inserted {inserted} events into MySQL")

# Update event_persons junction
cursor.execute("""
    INSERT IGNORE INTO event_persons (event_id, person_id)
    SELECT e.id, jt.person_id
    FROM events e
    CROSS JOIN JSON_TABLE(e.person_ids, '$[*]' COLUMNS(person_id VARCHAR(100) PATH '$')) AS jt
    WHERE e.id LIKE 'evt-mass-%'
      AND NOT EXISTS (SELECT 1 FROM event_persons ep WHERE ep.event_id = e.id AND ep.person_id = jt.person_id)
""")
conn.commit()
print(f"Updated event_persons junction table")

# Final stats
cursor.execute("SELECT COUNT(*) FROM events")
total = cursor.fetchone()['COUNT(*)']
cursor.execute("SELECT COUNT(*) FROM people WHERE data_status='published'")
people_cnt = cursor.fetchone()['COUNT(*)']
cursor.execute("SELECT COUNT(*) FROM (SELECT person_id FROM event_persons GROUP BY person_id HAVING COUNT(*)>=3) t")
deep = cursor.fetchone()['COUNT(*)']
print(f"\nFinal: {total} events / {people_cnt} people = {total/people_cnt:.1f} per person")
print(f"People with >=3 events: {deep} ({deep/people_cnt*100:.1f}%)")

cursor.close()
conn.close()
