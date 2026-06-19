#!/usr/bin/env python3
"""
Phase 5A: 从唐朝275人的summary中智能解析生平事件
提取：官职任命、科举信息、成就事件、关键年份节点
"""
import json, os, glob, re

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'data', 'events')
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open('/tmp/tang_phase5a_candidates.json') as f:
    candidates = json.load(f)

all_events = []

def add(id, title, titleEn, startYear, endYear=None, importance=3,
        summary='', summaryEn='', tags=None, tagsEn=None,
        personIds=None, regionId='tang-dynasty', sourceIds=None, isApprox=False,
        placeName=None, placeNameEn=None, coords=None):
    e = {
        'id': id, 'title': title, 'titleEn': titleEn,
        'startYear': startYear,
        'importance': importance,
        'summary': summary, 'summaryEn': summaryEn,
        'description': summary,
        'descriptionEn': summaryEn,
        'tags': tags or [], 'tagsEn': tagsEn or [],
        'personIds': personIds or [], 'regionId': regionId,
        'sourceIds': sourceIds or [], 'relatedEventIds': [],
        'datePrecision': 'year', 'isApproximate': isApprox,
        'dataStatus': 'published', 'confidenceScore': 0.8,
        'externalReferences': [],
    }
    if endYear is not None: e['endYear'] = endYear
    if placeName is not None: e['placeName'] = placeName
    if placeNameEn is not None: e['placeNameEn'] = placeNameEn
    if coords is not None: e['coordinates'] = coords
    all_events.append(e)

def extract_years(text):
    """Extract all 4-digit year mentions from text, prioritizing those followed by 年"""
    years = re.findall(r'(\d{3,4})年', text)
    return [int(y) for y in years if 500 <= int(y) <= 950]

def extract_offices(text):
    """Extract office/appointment mentions with years"""
    results = []
    # Pattern: YYYY年...为/任/拜/授...职
    matches = re.finditer(r'(\d{3,4})年[^，。；]*?(?:为|任|拜|授|官至|担任|曾任)[^，。；]{4,30}?(?:尚书|侍郎|刺史|宰相|节度使|太守|县令|中書|門下|僕射|御史|參軍|司馬|長史|將軍|都督|郎中|員外|學士|舍人|給事中|諫議大夫|侍御史|中丞|卿|少卿|祭酒)', text)
    for m in matches:
        year = int(m.group(1))
        if 500 <= year <= 950:
            desc = m.group(0)
            results.append((year, desc))
    return results

def extract_exam(text):
    """Extract imperial exam information"""
    patterns = [
        (r'(\d{3,4})年[^，。；]*?进士', '进士及第'),
        (r'(\d{3,4})年[^，。；]*?明经', '明经及第'),
        (r'(\d{3,4})年[^，。；]*?举人', '中举人'),
        (r'(\d{3,4})年[^，。；]*?及第', '科举及第'),
    ]
    for pat, label in patterns:
        m = re.search(pat, text)
        if m:
            year = int(m.group(1))
            if 500 <= year <= 950:
                return (year, label, m.group(0))
    return None

def process_person(p):
    """Generate events for one person"""
    pid = p['id']
    name = p['name']
    name_en = p.get('nameEn', name)
    birth = p.get('birthYear')
    death = p.get('deathYear')
    summary = p.get('summary', '')
    sources = p.get('sourceIds', [])
    tags = p.get('tags', [])
    occs = p.get('occupations', [])
    
    events = []
    event_idx = 0
    
    # 1. Birth event (if we have birth year)
    if birth:
        event_idx += 1
        birth_summary = f'{name}于{abs(birth)}年出生。' if birth < 0 else f'{name}于{birth}年出生。'
        add(f'evt-deep5a-{pid}-birth', f'{name}出生', f'Birth of {name_en}',
            birth, importance=2,
            summary=birth_summary,
            summaryEn=f'{name_en} was born in {birth}.',
            tags=['出生'] + tags[:3], tagsEn=['Birth'] + p.get('tagsEn', [])[:3],
            personIds=[pid], sourceIds=sources)

    # 2. Exam event
    exam = extract_exam(summary)
    if exam:
        event_idx += 1
        year, label, desc = exam
        add(f'evt-deep5a-{pid}-exam', f'{name}{label}', f'{name_en}: {label}',
            year, importance=3,
            summary=desc, summaryEn=f'{name_en} passed the imperial examination in {year}.',
            tags=['科举', '唐朝'] + [t for t in tags if t not in ['科举','唐朝']][:3],
            tagsEn=['Civil Exam', 'Tang Dynasty'] + p.get('tagsEn', [])[:3],
            personIds=[pid], sourceIds=sources)

    # 3. Office appointments
    offices = extract_offices(summary)
    shown_offices = set()
    for year, desc in offices:
        # Deduplicate similar offices
        office_key = desc[:20]
        if office_key in shown_offices: continue
        shown_offices.add(office_key)
        
        event_idx += 1
        add(f'evt-deep5a-{pid}-office{event_idx}', f'{name}任官', f'{name_en} Appointed',
            year, importance=3,
            summary=desc[:150], summaryEn=f'{name_en} received an official appointment in {year}.',
            tags=['仕途', '唐朝'] + tags[:3],
            tagsEn=['Career', 'Tang Dynasty'] + p.get('tagsEn', [])[:3],
            personIds=[pid], sourceIds=sources)

    # 4. Death event (if we have death year)
    if death and abs(death - (birth or 0)) > 5:  # Only if lived more than 5 years
        event_idx += 1
        death_summary = f'{name}于{abs(death)}年去世' if death < 0 else f'{name}于{death}年去世。'
        add(f'evt-deep5a-{pid}-death', f'{name}去世', f'Death of {name_en}',
            death, importance=3,
            summary=death_summary,
            summaryEn=f'{name_en} died in {death}.',
            tags=['逝世'] + tags[:3], tagsEn=['Death'] + p.get('tagsEn', [])[:3],
            personIds=[pid], sourceIds=sources)

    return events

# Process all candidates
total_processed = 0
total_events = 0
empty = 0

for p in candidates:
    events = process_person(p)
    total_processed += 1
    if events:
        total_events += 1
    else:
        empty += 1
    
    if total_processed % 50 == 0:
        print(f"Processed {total_processed}/{len(candidates)}...")

print(f"\nProcessed: {total_processed}")
print(f"With events: {total_events}")
print(f"Without events (skipped): {empty}")
print(f"Total events generated: {len(all_events)}")

# Save as JSON batches (200 per file)
batch_size = 200
for batch_idx in range(0, len(all_events), batch_size):
    batch = all_events[batch_idx:batch_idx + batch_size]
    batch_num = batch_idx // batch_size + 1
    output_file = os.path.join(OUTPUT_DIR, f'_deepEvents_tang_phase5a_{batch_num}.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(batch, f, ensure_ascii=False, indent=2)

total_batches = (len(all_events) + batch_size - 1) // batch_size
print(f"Written {total_batches} batch files")

# Show some sample events
print(f"\nSample generated events:")
for e in all_events[:5]:
    print(f"  {e['id']}: {e['title']} ({e['startYear']}) - persons: {e['personIds']}")
