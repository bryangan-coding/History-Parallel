#!/usr/bin/env python3
"""
Phase 5B: 为唐朝5254位有完整生卒年的人物生成结构化3事件生平
- 出生、中年仕途/成就、逝世
- 利用 occupation + tags 信息丰富事件内容
"""
import json, os, glob, re

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'data', 'events')
os.makedirs(OUTPUT_DIR, exist_ok=True)

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'data', 'people')

# Load all Tang people with both birth and death years
all_people = []
for f in sorted(glob.glob(f'{data_dir}/*.json')):
    if 'biographical' in f: continue
    with open(f) as fh: data = json.load(fh)
    for p in data:
        if p.get('regionId') != 'tang-dynasty': continue
        if p.get('dataStatus') != 'published': continue
        birth = p.get('birthYear')
        death = p.get('deathYear')
        if birth is None or death is None: continue
        if abs(death - birth) < 5: continue  # Too short lifespan
        all_people.append(p)

# Collect existing event IDs to avoid conflicts
existing_ids = set()
for f in sorted(glob.glob(f'{OUTPUT_DIR}/_lifespanEvents*.json') + 
                glob.glob(f'{OUTPUT_DIR}/_detailedEvents_*.json') + 
                glob.glob(f'{OUTPUT_DIR}/_deepEvents_phase*.json') +
                glob.glob(f'{OUTPUT_DIR}/_deepEvents_tang_phase5a_*.json')):
    with open(f) as fh: data = json.load(fh)
    existing_ids.update(e['id'] for e in data)
# Also from mockData
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'data', 'mockData.ts')) as f:
    content = f.read()
events_start = content.find('export const events')
for m in re.finditer(r"id:\s*'([^']+)'", content[events_start:content.find('// ===', events_start)]):
    existing_ids.add(m.group(1))

# Only skip people who already have deep events from earlier phases
# (Exclude _deepEvents_tang_phase5b_* as we're regenerating those)
deep_event_people = set()
for f in sorted(glob.glob(f'{OUTPUT_DIR}/_detailedEvents_*.json') + 
                glob.glob(f'{OUTPUT_DIR}/_deepEvents_phase*.json') +
                glob.glob(f'{OUTPUT_DIR}/_deepEvents_tang_phase5a_*.json')):
    with open(f) as fh: data = json.load(fh)
    for e in data:
        deep_event_people.update(e.get('personIds', []))

print(f"Tang people with both years: {len(all_people)}")
print(f"Existing event IDs: {len(existing_ids)}")

# Occupation-based event descriptions
OCCUPATION_EVENTS = {
    '政治家': ('仕途任职', 'Official Career', '担任朝廷要职，参与国家治理。', 'Held important government positions.'),
    '官员': ('仕途任职', 'Official Career', '在唐朝各级政府中担任官职。', 'Served in Tang government posts.'),
    '文学家': ('文学创作', 'Literary Career', '从事文学创作，在唐代文坛产生影响。', 'Engaged in literary creation during the Tang dynasty.'),
    '诗人': ('诗歌创作', 'Poetic Career', '创作诗歌，为唐代诗歌繁荣做出贡献。', 'Composed poetry during the golden age of Tang verse.'),
    '学者': ('学术活动', 'Scholarly Work', '从事学术研究和著述。', 'Engaged in scholarly research and writing.'),
    '画家': ('绘画创作', 'Painting Career', '从事绘画创作，参与唐代艺术发展。', 'Created paintings during Tang\'s artistic flourishing.'),
    '书法家': ('书法创作', 'Calligraphy Career', '研习书法，唐代书法艺术达到高峰。', 'Practiced calligraphy during Tang\'s golden age of the art.'),
    '僧侣': ('佛门修行', 'Buddhist Practice', '出家为僧，修行佛法。唐代佛教兴盛，寺院林立。', 'Practiced Buddhism during Tang\'s flourishing Buddhist period.'),
    '军事家': ('军事生涯', 'Military Career', '参与唐朝军事活动，历经边疆征战。', 'Participated in Tang military campaigns.'),
    '将领': ('军事生涯', 'Military Career', '担任军职，参与唐朝的边疆防务和征战。', 'Served as a military officer in the Tang dynasty.'),
    '历史人物': ('生平活动', 'Life and Activities', '在唐朝时期生活并参与社会活动。', 'Lived and was active during the Tang dynasty.'),
    '统治者': ('执政治国', 'Governance', '执掌政权，管理国家事务。', 'Governed and managed state affairs.'),
    '君主': ('君临天下', 'Reign', '统治帝国，处理朝政。', 'Ruled the empire and managed court affairs.'),
}

all_events = []
generated = 0

for p in all_people:
    pid = p['id']
    
    # Skip if already has deep events  
    if pid in deep_event_people:
        continue
    
    name = p['name']
    name_en = p.get('nameEn', name)
    birth = p['birthYear']
    death = p['deathYear']
    mid = (birth + death) // 2
    tags = p.get('tags', [])
    tags_en = p.get('tagsEn', [])
    occs = p.get('occupations', [])
    sources = p.get('sourceIds', [])
    
    # Find matching occupation event description
    event_label = '生平活动'
    event_label_en = 'Life Activities'
    event_desc = f'在唐朝（618—907年）时期生活与活动。'
    event_desc_en = 'Lived during the Tang dynasty (618-907).'
    
    for occ in occs:
        if occ in OCCUPATION_EVENTS:
            event_label, event_label_en, event_desc, event_desc_en = OCCUPATION_EVENTS[occ]
            break
    
    # Also check tags for better categorization
    if '文学家' in tags and event_label == '生平活动':
        event_label = '文学创作'
        event_label_en = 'Literary Career'
        event_desc = '从事文学创作，在唐代文坛产生影响。'
        event_desc_en = 'Engaged in literary creation during the Tang dynasty.'
    
    gen_events = []
    
    def make_evt(eid, title, titleEn, year, importance, summary, summaryEn, description, descriptionEn, tags, tagsEn, is_approx=False, conf=0.75):
        e = {
            'id': eid, 'title': title, 'titleEn': titleEn,
            'startYear': year, 'importance': importance,
            'summary': summary, 'summaryEn': summaryEn,
            'description': description, 'descriptionEn': descriptionEn,
            'tags': tags, 'tagsEn': tagsEn,
            'personIds': [pid], 'regionId': 'tang-dynasty',
            'sourceIds': sources, 'relatedEventIds': [],
            'datePrecision': 'year', 'isApproximate': is_approx,
            'dataStatus': 'published', 'confidenceScore': conf, 'externalReferences': [],
        }
        return e
    
    # Birth
    eid_birth = f'evt-5b-{pid}-birth'
    if eid_birth not in existing_ids:
        gen_events.append(make_evt(eid_birth, f'{name}出生', f'Birth of {name_en}', birth, 2,
            f'{name}于{abs(birth)}年出生在唐代。' if birth < 0 else f'{name}于{birth}年出生。',
            f'{name_en} was born in {birth} during the Tang dynasty.',
            f'{name}出生于唐代（618—907年），这是中国历史上文化繁荣、国力强盛的时期。',
            f'{name_en} was born during the Tang dynasty (618-907).',
            ['出生'] + tags[:4], ['Birth'] + tags_en[:4]))
    
    # Mid-life career
    eid_mid = f'evt-5b-{pid}-mid'
    if eid_mid not in existing_ids:
        gen_events.append(make_evt(eid_mid, f'{name}的{event_label}', f'{name_en}: {event_label_en}', mid, 2,
            event_desc, event_desc_en,
            f'{name}（{birth}—{death}年），{event_desc}',
            f'{name_en} ({birth}—{death}), {event_desc_en}',
            ['生平'] + tags[:4], ['Life'] + tags_en[:4], is_approx=True, conf=0.7))
    
    # Death
    eid_death = f'evt-5b-{pid}-death'
    if eid_death not in existing_ids:
        death_summary = f'{name}于{abs(death)}年逝世，享年约{abs(death-birth)}岁。' if death < 0 else f'{name}于{death}年逝世，享年约{death-birth}岁。'
        gen_events.append(make_evt(eid_death, f'{name}逝世', f'Death of {name_en}', death, 2,
            death_summary,
            f'{name_en} died in {death}, aged approximately {abs(death-birth)}.',
            f'{name}（{birth}—{death}）在唐代生活了约{abs(death-birth)}年，其生平见于相关史料记载。',
            f'{name_en} ({birth}—{death}) lived approximately {abs(death-birth)} years during the Tang dynasty.',
            ['逝世'] + tags[:4], ['Death'] + tags_en[:4]))
    
    for e in gen_events:
        existing_ids.add(e['id'])
    all_events.extend(gen_events)
    generated += 1
    
    if generated % 500 == 0:
        print(f"Generated {generated}/{len(all_people)}...")

print(f"\nTotal people processed: {generated}")
print(f"Total events generated: {len(all_events)}")

# Write in batches of 500
batch_size = 500
for batch_idx in range(0, len(all_events), batch_size):
    batch = all_events[batch_idx:batch_idx + batch_size]
    batch_num = batch_idx // batch_size + 1
    output_file = os.path.join(OUTPUT_DIR, f'_deepEvents_tang_phase5b_v2_{batch_num}.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(batch, f, ensure_ascii=False, indent=2)

total_batches = (len(all_events) + batch_size - 1) // batch_size
print(f"Written {total_batches} batch files")
