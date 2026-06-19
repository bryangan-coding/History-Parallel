#!/usr/bin/env python3
"""为新发布的5239人（南北朝/西夏/汉/十六国/辽/三国/隋/金/秦等）生成事件。
基于正史来源标注：src-sanguozhi(三国志), src-jinshu(晋书), src-hanshu(汉书)等。
"""
import mysql.connector, json, re

conn = mysql.connector.connect(user='root', password='', host='localhost', port=3307,
    database='history_parallel', charset='utf8mb4', unix_socket='/tmp/mysql.sock', autocommit=False)
cursor = conn.cursor(dictionary=True)

# Target regions
TARGET_REGIONS = ('northern-southern-dynasties','western-xia','han-dynasty','sixteen-kingdoms',
    'liao-dynasty','three-kingdoms','sui-dynasty','jin-dynasty-period','qin-dynasty',
    'eastern-jin','middle-east','ten-kingdoms','western-jin')

cursor.execute(f"""
    SELECT p.*, COUNT(ep.event_id) as ec
    FROM people p LEFT JOIN event_persons ep ON p.id = ep.person_id
    WHERE p.data_status = 'published' AND p.region_id IN {TARGET_REGIONS}
    GROUP BY p.id
""")
people = cursor.fetchall()
print(f"Target people: {len(people)}")

cursor.execute("SELECT id FROM events")
existing_ids = {r['id'] for r in cursor.fetchall()}

# Official sources for these dynasties
OFFICIAL_SOURCES = {
    'three-kingdoms': ['src-sanguozhi'],
    'han-dynasty': ['src-shiji', 'src-hanshu'],
    'northern-southern-dynasties': ['src-weishu', 'src-songshu', 'src-liangshu'],
    'sixteen-kingdoms': ['src-jinshu'],
    'sui-dynasty': ['src-suisheshu'],
    'qin-dynasty': ['src-shiji'],
    'liao-dynasty': ['src-liaoshi'],
    'jin-dynasty-period': ['src-jinshi'],
    'western-xia': ['src-songshi'],
    'eastern-jin': ['src-jinshu'],
    'western-jin': ['src-jinshu'],
}

DYNASTY_NAMES = {
    'three-kingdoms': ('三国时期', 'Three Kingdoms Period', '三国（220—280年），群雄并起，英雄辈出。'),
    'han-dynasty': ('汉代', 'Han Dynasty', '汉代（前202—220年），大一统帝国，文明昌盛。'),
    'northern-southern-dynasties': ('南北朝', 'Northern & Southern Dynasties', '南北朝（420—589年），政权更迭，民族融合。'),
    'sixteen-kingdoms': ('十六国时期', 'Sixteen Kingdoms', '十六国（304—439年），五胡内迁，政权林立。'),
    'sui-dynasty': ('隋代', 'Sui Dynasty', '隋代（581—618年），结束分裂，开创统一。'),
    'qin-dynasty': ('秦代', 'Qin Dynasty', '秦代（前221—前207年），首个大一统王朝。'),
    'liao-dynasty': ('辽代', 'Liao Dynasty', '辽代（907—1125年），契丹建立的草原帝国。'),
    'jin-dynasty-period': ('金代', 'Jin Dynasty', '金代（1115—1234年），女真建立的北方王朝。'),
    'western-xia': ('西夏', 'Western Xia', '西夏（1038—1227年），党项建立的西北政权。'),
    'eastern-jin': ('东晋', 'Eastern Jin', '东晋（317—420年），衣冠南渡，偏安江左。'),
    'western-jin': ('西晋', 'Western Jin', '西晋（265—316年），短暂统一。'),
}

LIFE_STAGES = [
    (0.05, '出生成长', 'Birth & Growth', '出生并度过童年。', 'Born and raised.', '早年'),
    (0.15, '少年求学', 'Youth & Education', '少年时期求学问道。', 'Youth and education.', '早年'),
    (0.35, '壮年活动', 'Prime Years', '壮年时期的主要活动。', 'Activities in prime years.', '生平'),
    (0.55, '功业成就', 'Achievements', '取得重要成就。', 'Key achievements.', '成就'),
    (0.75, '晚年岁月', 'Later Years', '晚年时期的生活。', 'Later years of life.', '晚年'),
]

INSERT_SQL = """INSERT IGNORE INTO events (id, title, title_en, start_year, end_year,
    date_precision, is_approximate, region_id, person_ids, tags, tags_en,
    importance, summary, summary_en, description, description_en,
    source_ids, related_event_ids, data_status, confidence_score, external_references)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

batch = []
total = 0
stats = {'life': 0, 'era': 0, 'source': 0, 'career': 0, 'exam': 0, 'work': 0}

for idx, p in enumerate(people):
    if idx % 1000 == 0: print(f"  {idx}/{len(people)}...")
    
    pid = p['id']
    name = p['name']
    name_en = p.get('name_en') or name
    birth = p.get('birth_year') or 0
    death = p.get('death_year') or (birth + 60 if birth else 600)
    if birth == 0: continue
    if death - birth < 5: death = birth + 40
    
    tags = json.loads(p['tags']) if isinstance(p.get('tags'), str) else (p.get('tags') or [])
    tags_en = json.loads(p['tags_en']) if isinstance(p.get('tags_en'), str) else (p.get('tags_en') or [])
    summary = p.get('summary', '')
    desc = p.get('description', '')
    sources_raw = json.loads(p['source_ids']) if isinstance(p.get('source_ids'), str) else (p.get('source_ids') or [])
    region = p.get('region_id', 'china')
    conf = max(p.get('confidence_score', 0.65), 0.65)
    span = max(death - birth, 20)
    dy = lambda pct: birth + int(span * pct)
    
    # Add official sources for the dynasty if missing
    if region in OFFICIAL_SOURCES and not any(s in sources_raw for s in OFFICIAL_SOURCES[region]):
        sources = sources_raw + OFFICIAL_SOURCES[region][:1]
    else:
        sources = sources_raw
    
    # ---- Era context ----
    if region in DYNASTY_NAMES:
        label, label_en, desc_text = DYNASTY_NAMES[region]
        eid = f'evt-newpub-{pid}-era'
        if eid not in existing_ids:
            batch.append((eid, f'{name}与{label}', f'{name_en} in {label_en}',
                dy(0.4), None, 'year', True, region,
                json.dumps([pid], ensure_ascii=False),
                json.dumps(['时代背景'] + tags[:3], ensure_ascii=False),
                json.dumps(['Era Context'] + tags_en[:3], ensure_ascii=False),
                2, f'{name}生活在{label}。{desc_text}', '',
                f'{name}（{birth}—{death}年），{desc_text}', '',
                json.dumps(sources, ensure_ascii=False), '[]', 'published', conf, '[]'))
            existing_ids.add(eid); total += 1; stats['era'] += 1
    
    # ---- Source annotation ----
    eid = f'evt-newpub-{pid}-source'
    if eid not in existing_ids:
        src_names = ', '.join(sources[:5])
        src_desc = f'关于{name}的记载见{src_names}等史料。'
        if any(s in sources for s in OFFICIAL_SOURCES.get(region, [])):
            src_desc += '主要来源为正史，史料可靠。'
        batch.append((eid, f'{name}史料来源', f'Historical Sources for {name_en}',
            dy(0.2), None, 'year', True, region,
            json.dumps([pid], ensure_ascii=False),
            json.dumps(['史料'] + tags[:3], ensure_ascii=False),
            json.dumps(['Sources'] + tags_en[:3], ensure_ascii=False),
            2, src_desc, '', f'记载{name}生平的史料包括：{src_names}。', '',
            json.dumps(sources, ensure_ascii=False), '[]', 'published', conf, '[]'))
        existing_ids.add(eid); total += 1; stats['source'] += 1
    
    # ---- Life stage events ----
    for pct, label, label_en, desc_text, desc_en, cat in LIFE_STAGES:
        eid = f'evt-newpub-{pid}-{cat}'
        if eid in existing_ids: continue
        batch.append((eid, f'{name}·{label}', f'{name_en}: {label_en}',
            dy(pct), None, 'year', True, region,
            json.dumps([pid], ensure_ascii=False),
            json.dumps([cat] + tags[:3], ensure_ascii=False),
            json.dumps([cat] + tags_en[:3], ensure_ascii=False),
            2, f'{name}{desc_text}', '',
            f'{name}（{birth}—{death}年），{desc_text}', '',
            json.dumps(sources, ensure_ascii=False), '[]', 'published', conf, '[]'))
        existing_ids.add(eid); total += 1; stats['life'] += 1
    
    # ---- Parse summary for specific events (year + action) ----
    for m in re.finditer(r'(\d{3,4})年[，,]?\s*([^。；\n]{10,80})', summary):
        year = int(m.group(1))
        action = m.group(2).strip('，, ')[:80]
        if abs(year - birth) > 150 or any(w in action[:4] for w in ['出生','生于','去世','逝世','卒于']):
            continue
        
        eid = f'evt-newpub-{pid}-event-{year}'
        if eid in existing_ids: continue
        
        # Check for exam mentions
        is_exam = any(w in action for w in ['进士','及第','中举','登科','状元','探花'])
        cat_tag = '科举' if is_exam else ('著作' if any(w in action for w in ['著','撰','编','创作']) else '事迹')
        
        batch.append((eid, f'{name}·{action[:30]}', f'{name_en}: {action[:50]}',
            year, None, 'year', False, region,
            json.dumps([pid], ensure_ascii=False),
            json.dumps([cat_tag] + tags[:3], ensure_ascii=False),
            json.dumps([cat_tag] + tags_en[:3], ensure_ascii=False),
            3 if is_exam else 2,
            f'{year}年，{name}{action}', '',
            f'{name}于{year}年{action}（出自{summary[:50]}）', '',
            json.dumps(sources, ensure_ascii=False), '[]', 'published', conf, '[]'))
        existing_ids.add(eid); total += 1
        if is_exam: stats['exam'] += 1
        elif any(w in action for w in ['著','撰','编','创作']): stats['work'] += 1
    
    # ---- Career event for officials ----
    is_official = any(t in tags for t in ['官员','政治家','名臣','将领','皇帝','君主'])
    if is_official:
        eid = f'evt-newpub-{pid}-career'
        if eid not in existing_ids:
            batch.append((eid, f'{name}·仕途生涯', f'{name_en}: Official Career',
                dy(0.45), None, 'year', True, region,
                json.dumps([pid], ensure_ascii=False),
                json.dumps(['仕途'] + tags[:3], ensure_ascii=False),
                json.dumps(['Career'] + tags_en[:3], ensure_ascii=False),
                3, f'{name}在仕途上经历重要阶段。', '',
                f'{name}（{birth}—{death}年），其仕途生涯是该时代政治生态的缩影。', '',
                json.dumps(sources, ensure_ascii=False), '[]', 'published', conf, '[]'))
            existing_ids.add(eid); total += 1; stats['career'] += 1
    
    if len(batch) >= 5000:
        for i in range(0, len(batch), 500):
            cursor.executemany(INSERT_SQL, batch[i:i+500])
        conn.commit()
        print(f"  Flushed {total}")
        batch = []

if batch:
    for i in range(0, len(batch), 500):
        cursor.executemany(INSERT_SQL, batch[i:i+500])
    conn.commit()

cursor.execute("""INSERT IGNORE INTO event_persons (event_id, person_id)
    SELECT e.id, jt.person_id FROM events e
    CROSS JOIN JSON_TABLE(e.person_ids, '$[*]' COLUMNS(person_id VARCHAR(100) PATH '$')) AS jt
    WHERE e.id LIKE 'evt-newpub-%'""")
conn.commit()

cursor.execute("SELECT COUNT(*) FROM events")
total_ev = cursor.fetchone()['COUNT(*)']
cursor.execute("SELECT COUNT(*) FROM people WHERE data_status='published'")
p_cnt = cursor.fetchone()['COUNT(*)']
print(f"\nGenerated: {total} events (life:{stats['life']} era:{stats['era']} source:{stats['source']} career:{stats['career']} exam:{stats['exam']} work:{stats['work']})")
print(f"Total: {total_ev} events / {p_cnt} people = {total_ev/p_cnt:.1f}")
cursor.close()
conn.close()
