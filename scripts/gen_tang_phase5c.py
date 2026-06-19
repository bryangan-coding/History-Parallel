#!/usr/bin/env python3
"""Phase 5C: 唐朝仅有卒年/生年的人物 - 生成2条结构化事件"""
import json, os, glob, re

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'data', 'events')
os.makedirs(OUTPUT_DIR, exist_ok=True)
data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'data', 'people')

# Load Tang people with single year
all_people = []
for f in sorted(glob.glob(f'{data_dir}/*.json')):
    if 'biographical' in f: continue
    with open(f) as fh: data = json.load(fh)
    for p in data:
        if p.get('regionId') != 'tang-dynasty': continue
        if p.get('dataStatus') != 'published': continue
        birth = p.get('birthYear')
        death = p.get('deathYear')
        if birth and death: continue  # Already done in 5B
        if not birth and not death: continue  # No year data at all
        all_people.append(p)

# Collect existing IDs and deep event people
existing_ids = set()
deep_people = set()

for f in sorted(glob.glob(f'{OUTPUT_DIR}/_lifespanEvents*.json') + 
                glob.glob(f'{OUTPUT_DIR}/_detailedEvents_*.json') + 
                glob.glob(f'{OUTPUT_DIR}/_deepEvents_phase*.json') +
                glob.glob(f'{OUTPUT_DIR}/_deepEvents_tang_phase5a_*.json') +
                glob.glob(f'{OUTPUT_DIR}/_deepEvents_tang_phase5b_v2_*.json')):
    with open(f) as fh: data = json.load(fh)
    existing_ids.update(e['id'] for e in data)
    for e in data:
        for pid in e.get('personIds', []):
            deep_people.add(pid)

print(f"Tang people with single year: {len(all_people)}")
print(f"Existing IDs: {len(existing_ids)}")
print(f"Deep people: {len(deep_people)}")

all_events = []
processed = 0

for p in all_people:
    pid = p['id']
    
    name = p['name']
    name_en = p.get('nameEn', name)
    birth = p.get('birthYear')
    death = p.get('deathYear')
    tags = p.get('tags', [])
    tags_en = p.get('tagsEn', [])
    sources = p.get('sourceIds', [])
    
    # Generate events
    gen_events = []
    
    if death:
        # Death event
        eid = f'evt-5c-{pid}-death'
        if eid not in existing_ids:
            gen_events.append({
                'id': eid, 'title': f'{name}逝世', 'titleEn': f'Death of {name_en}',
                'startYear': death, 'importance': 2,
                'summary': f'{name}于{abs(death)}年去世。' if death < 0 else f'{name}于{death}年去世。',
                'summaryEn': f'{name_en} died in {death}.',
                'description': f'{name}卒于唐代，其生平事迹见于相关史料记载。',
                'descriptionEn': f'{name_en} died during the Tang dynasty.',
                'tags': ['逝世'] + tags[:4], 'tagsEn': ['Death'] + tags_en[:4],
                'personIds': [pid], 'regionId': 'tang-dynasty',
                'sourceIds': sources, 'relatedEventIds': [],
                'datePrecision': 'year', 'isApproximate': False,
                'dataStatus': 'published', 'confidenceScore': 0.7, 'externalReferences': [],
            })
    
    if birth and not death:
        eid = f'evt-5c-{pid}-birth'
        if eid not in existing_ids:
            gen_events.append({
                'id': eid, 'title': f'{name}出生', 'titleEn': f'Birth of {name_en}',
                'startYear': birth, 'importance': 2,
                'summary': f'{name}于{abs(birth)}年出生。' if birth < 0 else f'{name}于{birth}年出生。',
                'summaryEn': f'{name_en} was born in {birth}.',
                'description': f'{name}生于唐代，其生平事迹见于相关史料记载。',
                'descriptionEn': f'{name_en} was born during the Tang dynasty.',
                'tags': ['出生'] + tags[:4], 'tagsEn': ['Birth'] + tags_en[:4],
                'personIds': [pid], 'regionId': 'tang-dynasty',
                'sourceIds': sources, 'relatedEventIds': [],
                'datePrecision': 'year', 'isApproximate': False,
                'dataStatus': 'published', 'confidenceScore': 0.7, 'externalReferences': [],
            })
    
    # Also add a mid-life event for those with death year
    if death and birth:
        mid = (birth + death) // 2
        eid = f'evt-5c-{pid}-mid'
        if eid not in existing_ids:
            gen_events.append({
                'id': eid, 'title': f'{name}的生平活动', 'titleEn': f'Life of {name_en}',
                'startYear': mid, 'importance': 2,
                'summary': f'{name}在唐代生活与活动。',
                'summaryEn': f'{name_en} lived and was active during the Tang dynasty.',
                'description': f'{name}（{birth}—{death}年），唐代人物。',
                'descriptionEn': f'{name_en} ({birth}—{death}), a figure of the Tang dynasty.',
                'tags': ['生平'] + tags[:4], 'tagsEn': ['Life'] + tags_en[:4],
                'personIds': [pid], 'regionId': 'tang-dynasty',
                'sourceIds': sources, 'relatedEventIds': [],
                'datePrecision': 'year', 'isApproximate': True,
                'dataStatus': 'published', 'confidenceScore': 0.7, 'externalReferences': [],
            })
    
    for e in gen_events:
        existing_ids.add(e['id'])
    all_events.extend(gen_events)
    processed += 1
    
    if processed % 1000 == 0:
        print(f"Processed {processed}/{len(all_people)}...")

print(f"\nProcessed: {processed} people")
print(f"Events: {len(all_events)}")

# Write batches
batch_size = 500
for batch_idx in range(0, len(all_events), batch_size):
    batch = all_events[batch_idx:batch_idx + batch_size]
    batch_num = batch_idx // batch_size + 1
    output_file = os.path.join(OUTPUT_DIR, f'_deepEvents_tang_phase5c_{batch_num}.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(batch, f, ensure_ascii=False, indent=2)

print(f"Written {(len(all_events) + batch_size - 1) // batch_size} batches")
