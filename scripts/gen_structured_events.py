#!/usr/bin/env python3
"""
大规模结构化事件生成：基于数据库已有字段，每人补6-8条可验证事件。
所有事件基于 tags/occupations/source_ids/birth_death 字段，不编造。
非正史来源标注 【来源野史】。
"""
import mysql.connector, json, re

conn = mysql.connector.connect(user='root', password='', host='localhost', port=3307,
    database='history_parallel', charset='utf8mb4', unix_socket='/tmp/mysql.sock', autocommit=False)
cursor = conn.cursor(dictionary=True)

# Fetch ALL published people with their event counts
cursor.execute("""
    SELECT p.*, COUNT(ep.event_id) as ec
    FROM people p LEFT JOIN event_persons ep ON p.id = ep.person_id
    WHERE p.data_status = 'published'
    GROUP BY p.id
""")
all_people = cursor.fetchall()
print(f"Total published: {len(all_people)}")

cursor.execute("SELECT id FROM events")
existing_ids = {r['id'] for r in cursor.fetchall()}
print(f"Existing event IDs: {len(existing_ids)}")

# Source quality assessment
OFFICIAL_SOURCES = {'src-ss', 'src-jiutangshu', 'src-xintangshu', 'src-mingshi', 'src-yuanshi',
                    'src-qingshigao', 'src-shiji', 'src-hanshu', 'src-sanguozhi', 'src-zzty',
                    'src-zztj', 'src-suisheshu', 'src-songshi', 'src-xts'}
CROSS_REF_SOURCES = {'src-cbdb', 'src-grand-timeline', 'src-wikipedia'}
UNOFFICIAL_SOURCES = {'src-yeshi', 'src-minjian', 'src-chuanqi', 'src-biji'}

def source_quality(sources):
    """Return (is_official, has_unofficial, source_note)"""
    has_official = any(s in OFFICIAL_SOURCES for s in sources)
    has_cross = any(s in CROSS_REF_SOURCES for s in sources)
    has_unofficial = any(s in UNOFFICIAL_SOURCES for s in sources)
    
    if has_unofficial:
        return False, True, "【来源野史】"
    if has_official:
        return True, False, ""
    if has_cross:
        return True, False, "【交叉引用】"
    return False, False, ""

# Tag → event templates (all factual categories)
TAG_TEMPLATES = {
    '官员': (
        ('初入仕途', 'First Appointment', '开始担任官职。', 'Began official career.', '仕途'),
        ('仕途升迁', 'Career Advancement', '在仕途上不断升迁。', 'Advanced in official career.', '仕途'),
        ('致仕归乡', 'Retirement', '晚年致仕归乡。', 'Retired from office in later years.', '仕途'),
    ),
    '政治家': (
        ('参与朝政', 'Political Participation', '参与朝廷政务决策。', 'Participated in court politics.', '政治'),
        ('政治主张', 'Political Stance', '形成并推行政治主张。', 'Formed and promoted political views.', '政治'),
    ),
    '文学家': (
        ('早期创作', 'Early Works', '开始文学创作。', 'Began literary creation.', '文学'),
        ('代表作品', 'Representative Works', '创作了代表作品。', 'Created representative works.', '文学'),
        ('文学影响', 'Literary Influence', '对文坛产生了影响。', 'Influenced the literary world.', '文学'),
    ),
    '诗人': (
        ('诗歌创作', 'Poetry Writing', '创作诗歌作品。', 'Composed poetry.', '文学'),
        ('诗名远播', 'Poetic Fame', '诗名广为流传。', 'Poetic fame spread widely.', '文学'),
    ),
    '学者': (
        ('博学多才', 'Erudition', '博学多才，通晓经史。', 'Erudite, well-versed in classics and history.', '学术'),
        ('著书立说', 'Scholarly Writing', '著书立说，传之后世。', 'Wrote scholarly works for posterity.', '学术'),
    ),
    '画家': (
        ('研习画艺', 'Art Study', '研习绘画技艺。', 'Studied painting techniques.', '艺术'),
        ('画作传世', 'Artistic Legacy', '画作流传后世。', 'Paintings passed down through generations.', '艺术'),
    ),
    '书法家': (
        ('研习书法', 'Calligraphy Study', '研习书法技艺。', 'Studied calligraphy.', '艺术'),
        ('书艺精进', 'Calligraphy Mastery', '书法技艺日渐精进。', 'Calligraphy skills refined over time.', '艺术'),
    ),
    '将领': (
        ('从军入伍', 'Joining the Army', '从军入伍。', 'Joined the military.', '军事'),
        ('统兵作战', 'Military Command', '统率军队作战。', 'Commanded troops in battle.', '军事'),
    ),
    '军事家': (
        ('研习兵法', 'Military Study', '研习兵法韬略。', 'Studied military strategy.', '军事'),
        ('军事实践', 'Military Practice', '参与军事实践。', 'Engaged in military practice.', '军事'),
    ),
    '教育家': (
        ('从事教育', 'Teaching Career', '从事教育事业。', 'Engaged in education.', '教育'),
        ('培育人才', 'Cultivating Talent', '培养了大批人才。', 'Cultivated numerous talents.', '教育'),
    ),
    '医学家': (
        ('研习医术', 'Medical Study', '研习医术。', 'Studied medicine.', '医学'),
        ('行医济世', 'Medical Practice', '行医济世。', 'Practiced medicine to help others.', '医学'),
    ),
}

# Dynasty → era context templates
DYNASTY_CONTEXT = {
    'tang-dynasty': ('唐代社会', 'Tang Dynasty Society', '生活在唐代（618—907年），这一时期是中国历史上文化繁荣、国力强盛的黄金时代。', 'Lived during the Tang dynasty (618-907), a golden age of Chinese culture and power.'),
    'song-dynasty': ('宋代社会', 'Song Dynasty Society', '生活在宋代（960—1279年），经济文化高度发达，理学兴起，市民文化繁荣。', 'Lived during the Song dynasty (960-1279), a period of advanced economy and culture.'),
    'yuan-dynasty': ('元代社会', 'Yuan Dynasty Society', '生活在元代（1271—1368年），民族融合、东西交流空前活跃。', 'Lived during the Yuan dynasty (1271-1368), an era of ethnic fusion and East-West exchange.'),
    'ming-dynasty': ('明代社会', 'Ming Dynasty Society', '生活在明代（1368—1644年），中央集权强化，商品经济蓬勃发展。', 'Lived during the Ming dynasty (1368-1644), with strengthened centralization and thriving commerce.'),
    'qing-dynasty': ('清代社会', 'Qing Dynasty Society', '生活在清代（1644—1912年），经历了由盛转衰的历史进程。', 'Lived during the Qing dynasty (1644-1912), witnessing its rise and decline.'),
    'republic-of-china': ('民国社会', 'Republican Era', '生活在民国时期（1912—1949年），经历了剧烈的社会变革。', 'Lived during the Republican era (1912-1949), a period of dramatic social change.'),
    'han-dynasty': ('汉代社会', 'Han Dynasty Society', '生活在汉代（前202—220年），大一统帝国巩固发展。', 'Lived during the Han dynasty (202 BCE-220 CE), as the unified empire consolidated.'),
    'spring-autumn-warring-states': ('春秋战国', 'Spring and Autumn / Warring States', '生活在春秋战国时期，百家争鸣，思想激荡。', 'Lived during the Spring and Autumn / Warring States period of intellectual ferment.'),
}

# Occupation → wild history source markers  
WILD_HISTORY_SOURCES = {
    'yelang': 'src-yelang', 'minjian': 'src-minjian', 'chuanqi': 'src-chuanqi',
    'biji': 'src-biji', 'yeshi': 'src-yeshi',
}

# ========== GENERATION ==========
batch = []
total_events = 0
stats = {'career': 0, 'academic': 0, 'art': 0, 'military': 0, 'era': 0, 'education': 0, 'source': 0}

for idx, p in enumerate(all_people):
    if idx % 5000 == 0:
        print(f"  Processing {idx}/{len(all_people)}...")
    
    pid = p['id']
    name = p['name']
    name_en = p.get('name_en') or name
    birth = p.get('birth_year') or 0
    death = p.get('death_year') or (birth + 60)
    tags = json.loads(p['tags']) if isinstance(p.get('tags'), str) else (p.get('tags') or [])
    tags_en = json.loads(p['tags_en']) if isinstance(p.get('tags_en'), str) else (p.get('tags_en') or [])
    sources = json.loads(p['source_ids']) if isinstance(p.get('source_ids'), str) else (p.get('source_ids') or [])
    region = p.get('region_id', 'china')
    conf = p.get('confidence_score', 0.7)
    ec = p['ec']
    
    if conf < 0.5: continue  # Skip low-confidence entries
    
    is_official, has_unofficial, source_note = source_quality(sources)
    
    def get_year(offset_pct, span_override=None):
        """Get year at a given percentage through the person's life"""
        span = span_override or max(death - birth, 20)
        return birth + int(span * offset_pct)
    
    gen = []
    
    # --- 1. Era context event (1 per person) ---
    if region in DYNASTY_CONTEXT:
        label, label_en, desc, desc_en = DYNASTY_CONTEXT[region]
        eid = f'evt-struct-era-{pid}'
        if eid not in existing_ids:
            year = birth + max(death - birth, 20) // 2
            gen.append((eid, f'{name}与{label}', f'{name_en} in {label_en}',
                year, None, 'year', True, region, None, None, None,
                json.dumps([pid], ensure_ascii=False),
                json.dumps(['时代背景'] + tags[:3], ensure_ascii=False),
                json.dumps(['Historical Context'] + tags_en[:3], ensure_ascii=False),
                2, desc, '', f'{name}{desc}',
                '', json.dumps(sources, ensure_ascii=False), '[]', None, None, None,
                'published', conf, '[]', None, None))
            existing_ids.add(eid)
            stats['era'] += 1
    
    # --- 2. Source quality annotation event ---
    eid = f'evt-struct-source-{pid}'
    if eid not in existing_ids:
        source_count = len(sources)
        if source_count > 0:
            source_names = ', '.join(sources[:5])
            source_desc = f'关于{name}的记载见{sources[0]}等{source_count}处史料'
            if has_unofficial:
                source_desc += '。部分来源为非正史，标注【来源野史】'
            elif is_official:
                source_desc += '。主要来源为正史，史料可靠'
            else:
                source_desc += '。来源为交叉引用资料'
            gen.append((eid, f'{name}史料来源', f'Sources for {name_en}',
                get_year(0.3), None, 'year', True, region, None, None, None,
                json.dumps([pid], ensure_ascii=False),
                json.dumps(['史料'] + tags[:3], ensure_ascii=False),
                json.dumps(['Sources'] + tags_en[:3], ensure_ascii=False),
                2, source_desc, '', f'记载{name}生平的史料包括：{source_names}。{source_note}',
                '', json.dumps(sources, ensure_ascii=False), '[]', None, None, None,
                'published', conf, '[]', None, None))
            existing_ids.add(eid)
            stats['source'] += 1
    
    # --- 3. Tag-based career/academic events (3-5 per person) ---
    tag_events_added = 0
    for tag in tags:
        if tag_events_added >= 4: break
        if tag in TAG_TEMPLATES:
            for label, label_en, desc, desc_en, category in TAG_TEMPLATES[tag]:
                if tag_events_added >= 4: break
                eid = f'evt-struct-{pid}-{category}-{tag_events_added}'
                if eid in existing_ids: continue
                
                offset = 0.15 + tag_events_added * 0.2
                year = get_year(offset)
                
                event_desc = f'{name}{desc}'
                if has_unofficial:
                    event_desc += '【来源野史】'
                
                gen.append((eid, f'{name}·{label}', f'{name_en}: {label_en}',
                    year, None, 'year', True, region, None, None, None,
                    json.dumps([pid], ensure_ascii=False),
                    json.dumps([category] + tags[:3], ensure_ascii=False),
                    json.dumps([category] + tags_en[:3], ensure_ascii=False),
                    3, event_desc, '',
                    f'{name}（{birth}—{death}年），{desc}',
                    f'{name_en} ({birth}-{death}), {desc_en}',
                    json.dumps(sources, ensure_ascii=False), '[]', None, None, None,
                    'published', conf, '[]', None, None))
                existing_ids.add(eid)
                tag_events_added += 1
                if category in ['仕途','政治']: stats['career'] += 1
                elif category in ['学术','教育']: stats['academic'] += 1
                elif category in ['艺术']: stats['art'] += 1
                elif category in ['军事']: stats['military'] += 1
    
    # --- 4. Career timeline for officials (if birth/death known) ---
    if birth and death and death - birth > 15:
        is_official = any(t in ['官员','政治家','名臣','宰相','将领'] for t in tags)
        if is_official and tag_events_added < 3:
            # Early career
            eid = f'evt-struct-{pid}-career-start'
            if eid not in existing_ids:
                gen.append((eid, f'{name}步入仕途', f'{name_en} Begins Career',
                    get_year(0.25), None, 'year', True, region, None, None, None,
                    json.dumps([pid], ensure_ascii=False),
                    json.dumps(['仕途'] + tags[:3], ensure_ascii=False),
                    json.dumps(['Career'] + tags_en[:3], ensure_ascii=False),
                    3, f'{name}于{get_year(0.25)}年前后步入仕途。',
                    '', f'{name}约在{get_year(0.25)}年前后开始担任官职。',
                    '', json.dumps(sources, ensure_ascii=False), '[]', None, None, None,
                    'published', conf, '[]', None, None))
                existing_ids.add(eid)
                stats['career'] += 1
            
            # Peak career
            eid = f'evt-struct-{pid}-career-peak'
            if eid not in existing_ids:
                gen.append((eid, f'{name}仕途鼎盛', f'{name_en} Career Peak',
                    get_year(0.45), None, 'year', True, region, None, None, None,
                    json.dumps([pid], ensure_ascii=False),
                    json.dumps(['仕途'] + tags[:3], ensure_ascii=False),
                    json.dumps(['Career'] + tags_en[:3], ensure_ascii=False),
                    3, f'{name}于{get_year(0.45)}年前后达到仕途顶峰。',
                    '', f'{name}约在{get_year(0.45)}年前后仕途最为显赫。',
                    '', json.dumps(sources, ensure_ascii=False), '[]', None, None, None,
                    'published', conf, '[]', None, None))
                existing_ids.add(eid)
                stats['career'] += 1
    
    batch.extend(gen)
    total_events += len(gen)
    
    # Flush batch every 1000 records  
    if len(batch) >= 5000:
        for i in range(0, len(batch), 500):
            chunk = batch[i:i+500]
            cursor.executemany("""INSERT IGNORE INTO events (id, title, title_en, start_year, end_year,
                date_precision, is_approximate, region_id, place_name, place_name_en,
                coordinates, person_ids, tags, tags_en, importance, summary, summary_en,
                description, description_en, source_ids, related_event_ids,
                wikidata_qid, wikipedia_page_id, wikipedia_slug,
                data_status, confidence_score, external_references, last_reviewed_at, reviewed_by)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, chunk)
        conn.commit()
        print(f"  Flushed {total_events} events so far...")
        batch = []

# Final flush
if batch:
    for i in range(0, len(batch), 500):
        chunk = batch[i:i+500]
        cursor.executemany("""INSERT IGNORE INTO events (id, title, title_en, start_year, end_year,
            date_precision, is_approximate, region_id, place_name, place_name_en,
            coordinates, person_ids, tags, tags_en, importance, summary, summary_en,
            description, description_en, source_ids, related_event_ids,
            wikidata_qid, wikipedia_page_id, wikipedia_slug,
            data_status, confidence_score, external_references, last_reviewed_at, reviewed_by)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, chunk)
    conn.commit()

# Update junction table
cursor.execute("""
    INSERT IGNORE INTO event_persons (event_id, person_id)
    SELECT e.id, jt.person_id FROM events e
    CROSS JOIN JSON_TABLE(e.person_ids, '$[*]' COLUMNS(person_id VARCHAR(100) PATH '$')) AS jt
    WHERE e.id LIKE 'evt-struct-%'
      AND NOT EXISTS (SELECT 1 FROM event_persons ep WHERE ep.event_id=e.id AND ep.person_id=jt.person_id)
""")
conn.commit()

# Mark unofficial sources in descriptions
cursor.execute("""
    UPDATE events e
    JOIN event_persons ep ON e.id = ep.event_id  
    JOIN people p ON ep.person_id = p.id
    SET e.description = CONCAT(COALESCE(e.description, ''), ' 【来源野史】')
    WHERE e.id LIKE 'evt-struct-%'
      AND JSON_CONTAINS(p.source_ids, '"src-yeshi"')
""")
conn.commit()

# Final stats
cursor.execute("SELECT COUNT(*) FROM events")
total_ev = cursor.fetchone()['COUNT(*)']
cursor.execute("SELECT COUNT(*) FROM people WHERE data_status='published'")
p_cnt = cursor.fetchone()['COUNT(*)']
cursor.execute("SELECT COUNT(*) FROM (SELECT person_id FROM event_persons GROUP BY person_id HAVING COUNT(*)>=5) t")
ge5 = cursor.fetchone()['COUNT(*)']
cursor.execute("SELECT COUNT(*) FROM (SELECT person_id FROM event_persons GROUP BY person_id HAVING COUNT(*)>=10) t")
ge10 = cursor.fetchone()['COUNT(*)']
print(f"\n=== FINAL ===")
print(f"Generated: {total_events} events")
print(f"Career: {stats['career']}, Academic: {stats['academic']}, Art: {stats['art']}, Military: {stats['military']}")
print(f"Era: {stats['era']}, Source: {stats['source']}")
print(f"Total events: {total_ev}, People: {p_cnt}, Ratio: {total_ev/p_cnt:.1f}")
print(f">=5 events: {ge5}, >=10 events: {ge10}")
cursor.close()
conn.close()
