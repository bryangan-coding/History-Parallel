#!/usr/bin/env python3
"""
从人物数据生成生平概要事件。
策略：
1. 深度补全：为有丰富生平描述（>100 chars 非模板）的人物生成详细事件
2. 基础补全：为其余所有人至少生成一条「生平概要」事件

时间处理逻辑：
- 如果有确切生卒年，事件覆盖其一生
- 如果只有生年或只有卒年，以已知年份为中心±30年
- 如果生卒年都不确定，从summary中推断大致活跃时期
- 所有事件标记 isApproximate 并在 summary 中说明时间模糊性
"""
import json
import os
import glob
import re
import sys

# Template patterns to detect generic descriptions
TEMPLATE_PATTERNS = [
    '关于其生平与事迹的记载，散见于相关史籍文献之中',
    '反映了当时的历史风貌与社会环境',
    '其生平事迹见于相关史料记载',
]

def is_template_desc(desc):
    if not desc:
        return True
    for pat in TEMPLATE_PATTERNS:
        if pat in desc:
            return True
    return False

def esc(s):
    """Escape string for TypeScript single-quoted string literals"""
    if not s:
        return ''
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n").replace("\r", "")

def infer_years(p):
    """Infer active years for a person, returning (startYear, endYear, isApproximate, note)"""
    birth = p.get('birthYear')
    death = p.get('deathYear')
    
    if birth is not None and death is not None:
        if birth == death:
            return (birth, birth, True, '生卒年相同，可能只有一年记录')
        return (birth, death, False, '')
    
    if birth is not None and death is None:
        # Assume lived ~60 years
        return (birth, birth + 60, True, '卒年不详，假定约享年60岁')
    
    if birth is None and death is not None:
        # Assume lived ~60 years
        return (death - 60, death, True, '生年不详，假定约享年60岁')
    
    # Both unknown - try to extract from summary
    summary = p.get('summary', '')
    years = re.findall(r'(\d{3,4})年', summary)
    if len(years) >= 1:
        y = int(years[0])
        return (y - 30, y + 30, True, '生卒年均不详，根据史料中提及的年份推断大致活跃时期')
    
    return (None, None, True, '生卒年及活跃时期均不详')

def format_years_for_title(birth, death, approx):
    """Format years for event title"""
    if birth is None and death is None:
        return '生卒年不详'
    if birth is None:
        return f'？—{death}年'
    if death is None:
        return f'{birth}年—？'
    if birth == death:
        return f'{birth}年'
    return f'{birth}—{death}年'

def make_event(person, event_id, start_year, end_year, title, title_en, summary, summary_en, 
               tags, tags_en, importance=3, desc='', desc_en='', place=None, place_en=None, 
               coords=None, is_approx=False, date_prec='year', note='', srcs=None):
    """Create an event object"""
    evt = {
        'id': event_id,
        'title': title,
        'titleEn': title_en,
        'startYear': start_year,
        'endYear': end_year,
        'regionId': person.get('regionId', 'china'),
        'personIds': [person['id']],
        'tags': tags,
        'tagsEn': tags_en,
        'importance': importance,
        'summary': summary,
        'summaryEn': summary_en,
        'description': desc if desc else summary,
        'descriptionEn': desc_en if desc_en else summary_en,
        'sourceIds': srcs if srcs else person.get('sourceIds', []),
        'relatedEventIds': [],
        'datePrecision': date_prec,
        'isApproximate': is_approx,
        'dataStatus': 'published',
        'confidenceScore': person.get('confidenceScore', 0.65),
        'externalReferences': [],
    }
    if place:
        evt['placeName'] = place
    if place_en:
        evt['placeNameEn'] = place_en
    if coords:
        evt['coordinates'] = coords
    if note:
        evt['timeNote'] = note  # Custom field for time ambiguity note
    return evt

def generate_lifespan_event(person, existing_event_ids):
    """Generate a basic lifespan event for a person"""
    pid = person['id']
    name = person['name']
    name_en = person.get('nameEn', name)
    tags = person.get('tags', [])
    tags_en = person.get('tagsEn', [])
    summary = person.get('summary', '')
    region = person.get('regionId', 'china')
    
    # Check if person already has events (via personIds in existing events)
    # We'll skip if already has events - handled by caller
    
    birth = person.get('birthYear')
    death = person.get('deathYear')
    start_year, end_year, is_approx, note = infer_years(person)
    
    if start_year is None:
        return None  # Can't determine any years
    
    # Generate event ID
    event_id = f"evt-lifespan-{pid}"
    if event_id in existing_event_ids:
        return None
    
    year_str = format_years_for_title(birth, death, is_approx)
    
    # Build event data
    title = f'{name}生平'
    title_en = f'Life of {name_en}'
    
    # Build summary with time note
    evt_summary = summary[:200] if summary else f'{name}，{year_str}。'
    if note:
        evt_summary += f'（时间说明：{note}）'
    
    evt_summary_en = person.get('summaryEn', '')[:200] if person.get('summaryEn') else f'{name_en}, {year_str}.'
    
    # Tags
    evt_tags = ['生平'] + [t for t in tags if t not in ['生平']]
    evt_tags_en = ['Biography'] + [t for t in tags_en if t not in ['Biography']]
    
    # Importance: rulers/major figures get higher score
    importance = 2
    important_tags = ['皇帝', '君主', '名臣', '文学家', '军事人物', '改革家', '科学家', '哲学家', 'Emperor', 'Monarch', 'Writer', 'Military']
    for t in tags + tags_en:
        if t in important_tags:
            importance = 3
            break
    
    evt = {
        'id': event_id,
        'title': title,
        'titleEn': title_en,
        'startYear': start_year,
        'endYear': end_year if end_year != start_year else None,
        'regionId': region,
        'personIds': [pid],
        'tags': evt_tags[:8],
        'tagsEn': evt_tags_en[:8],
        'importance': importance,
        'summary': evt_summary,
        'summaryEn': evt_summary_en,
        'description': person.get('description', evt_summary),
        'descriptionEn': person.get('descriptionEn', evt_summary_en) if person.get('descriptionEn') else evt_summary_en,
        'sourceIds': person.get('sourceIds', []),
        'relatedEventIds': [],
        'datePrecision': 'year',
        'isApproximate': is_approx,
        'dataStatus': 'published',
        'confidenceScore': person.get('confidenceScore', 0.65),
        'externalReferences': [],
    }
    if note:
        evt['_timeNote'] = note
    
    return evt


def generate_rich_events(person, existing_event_ids):
    """Generate multiple detailed events for a person with rich description"""
    pid = person['id']
    name = person['name']
    desc = person.get('description', '')
    birth = person.get('birthYear')
    death = person.get('deathYear')
    region = person.get('regionId', 'china')
    tags = person.get('tags', [])
    tags_en = person.get('tagsEn', [])
    sources = person.get('sourceIds', [])
    confidence = person.get('confidenceScore', 0.85)
    
    events = []
    
    # Strategy: For people with rich descriptions, the description often contains 
    # multiple life events. We parse key milestones from the description.
    # Since we can't reliably parse all events from text, we generate a high-quality
    # lifespan event that incorporates the rich description.
    
    # Generate lifespan event with rich description
    start_year, end_year, is_approx, note = infer_years(person)
    if start_year is None:
        return events
    
    event_id = f"evt-lifespan-{pid}"
    if event_id in existing_event_ids:
        return events
    
    year_str = format_years_for_title(birth, death, is_approx)
    summary_text = person.get('summary', '')
    
    # For rich description people, use the description as the event description
    evt_summary = summary_text[:300]
    evt_desc = desc[:1500] if desc else summary_text
    
    name_en = person.get('nameEn', name)
    
    importance = 4  # Rich description implies more important figure
    
    evt = {
        'id': event_id,
        'title': f'{name}生平',
        'titleEn': f'Life of {name_en}',
        'startYear': start_year,
        'endYear': end_year if end_year != start_year else None,
        'regionId': region,
        'personIds': [pid],
        'tags': ['生平'] + [t for t in tags if t not in ['生平']][:7],
        'tagsEn': ['Biography'] + [t for t in tags_en if t not in ['Biography']][:7],
        'importance': importance,
        'summary': evt_summary,
        'summaryEn': person.get('summaryEn', '')[:300] if person.get('summaryEn') else evt_summary,
        'description': evt_desc,
        'descriptionEn': person.get('descriptionEn', '')[:1500] if person.get('descriptionEn') else evt_desc,
        'sourceIds': sources,
        'relatedEventIds': [],
        'datePrecision': 'year',
        'isApproximate': is_approx,
        'dataStatus': 'published',
        'confidenceScore': confidence,
        'externalReferences': [],
    }
    if note:
        evt['_timeNote'] = note
    
    events.append(evt)
    return events


def emit_ts_event(evt):
    """Emit a single event as TypeScript object literal"""
    lines = []
    lines.append('  {')
    lines.append(f"    id: '{esc(evt['id'])}',")
    lines.append(f"    title: '{esc(evt['title'])}',")
    if evt.get('titleEn'):
        lines.append(f"    titleEn: '{esc(evt['titleEn'])}',")
    
    start_y = evt.get('startYear')
    lines.append(f"    startYear: {start_y if start_y is not None else 'undefined'},")
    
    end_y = evt.get('endYear')
    if end_y is not None:
        lines.append(f"    endYear: {end_y},")
    
    lines.append(f"    regionId: '{evt['regionId']}',")
    
    if evt.get('placeName'):
        lines.append(f"    placeName: '{esc(evt['placeName'])}',")
    if evt.get('placeNameEn'):
        lines.append(f"    placeNameEn: '{esc(evt['placeNameEn'])}',")
    if evt.get('coordinates'):
        c = evt['coordinates']
        lines.append(f"    coordinates: {{ lat: {c['lat']}, lng: {c['lng']} }},")
    
    pids = evt.get('personIds', [])
    pids_str = ', '.join("'" + p + "'" for p in pids)
    lines.append(f"    personIds: [{pids_str}],")
    
    tags = evt.get('tags', [])
    tags_str = ', '.join("'" + t + "'" for t in tags)
    lines.append(f"    tags: [{tags_str}],")
    
    tags_en = evt.get('tagsEn', [])
    if tags_en:
        tags_en_str = ', '.join("'" + t + "'" for t in tags_en)
        lines.append(f"    tagsEn: [{tags_en_str}],")
    
    lines.append(f"    datePrecision: '{evt.get('datePrecision', 'year')}',")
    lines.append(f"    isApproximate: {'true' if evt.get('isApproximate') else 'false'},")
    lines.append(f"    importance: {evt.get('importance', 2)},")
    lines.append(f"    summary: '{esc(evt.get('summary', ''))}',")
    if evt.get('summaryEn'):
        lines.append(f"    summaryEn: '{esc(evt['summaryEn'])}',")
    lines.append(f"    description: '{esc(evt.get('description', ''))}',")
    if evt.get('descriptionEn'):
        lines.append(f"    descriptionEn: '{esc(evt['descriptionEn'])}',")
    
    srcs = evt.get('sourceIds', [])
    srcs_str = ', '.join("'" + s + "'" for s in srcs)
    lines.append(f"    sourceIds: [{srcs_str}],")
    lines.append(f"    relatedEventIds: [],")
    lines.append(f"    dataStatus: 'published' as const,")
    lines.append(f"    confidenceScore: {evt.get('confidenceScore', 0.65)},")
    lines.append(f"    externalReferences: [],")
    lines.append('  },')
    return '\n'.join(lines)


def main():
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'src', 'data', 'people')
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'src', 'data', 'events')
    os.makedirs(output_dir, exist_ok=True)
    
    # Target dynasties
    target_regions = ['tang-dynasty', 'song-dynasty', 'yuan-dynasty', 'ming-dynasty', 'qing-dynasty']
    
    # Collect existing event IDs from mockData.ts
    existing_event_ids = set()
    mockdata_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'data', 'mockData.ts')
    with open(mockdata_path, 'r') as f:
        content = f.read()
    existing_event_ids = set(re.findall(r"id:\s*'([^']+)'", 
        content[content.find('export const events'):content.find('// ===', content.find('export const events'))]
    ))
    
    # Also collect existing person->event mappings
    # Track which people already have events
    people_with_events = set()
    events_section = content[content.find('export const events'):]
    events_section = events_section[:events_section.find('\n// ===')]
    for m in re.finditer(r"personIds:\s*\[(.*?)\]", events_section, re.DOTALL):
        pids = re.findall(r"'([^']+)'", m.group(1))
        people_with_events.update(pids)
    
    print(f"Existing event IDs: {len(existing_event_ids)}")
    print(f"People already with events: {len(people_with_events)}")
    
    # Load all people
    all_people = []
    for f in sorted(glob.glob(f'{data_dir}/*.json')):
        if 'biographical' in f:
            continue
        with open(f) as fh:
            data = json.load(fh)
        all_people.extend(data)
    
    # Filter for target dynasties, published only
    stats = {r: {'total': 0, 'rich': 0, 'basic': 0, 'skipped_has_event': 0, 'skipped_no_years': 0, 'events_generated': 0} for r in target_regions}
    
    all_new_events = []
    
    for person in all_people:
        region = person.get('regionId', '')
        if region not in target_regions:
            continue
        if person.get('dataStatus') != 'published':
            continue
        
        pid = person['id']
        stats[region]['total'] += 1
        
        # Skip if already has events
        if pid in people_with_events:
            stats[region]['skipped_has_event'] += 1
            continue
        
        desc = person.get('description', '')
        is_rich = len(desc) > 100 and not is_template_desc(desc)
        
        if is_rich:
            stats[region]['rich'] += 1
            new_events = generate_rich_events(person, existing_event_ids)
        else:
            stats[region]['basic'] += 1
            new_evt = generate_lifespan_event(person, existing_event_ids)
            new_events = [new_evt] if new_evt else []
        
        if not new_events:
            stats[region]['skipped_no_years'] += 1
            continue
        
        for evt in new_events:
            if evt['id'] not in existing_event_ids:
                all_new_events.append(evt)
                existing_event_ids.add(evt['id'])
                stats[region]['events_generated'] += 1
    
    print(f"\nTotal new events generated: {len(all_new_events)}")
    print()
    
    for r in target_regions:
        s = stats[r]
        print(f"{r}: total={s['total']}, rich={s['rich']}, basic={s['basic']}, "
              f"skipped_has_event={s['skipped_has_event']}, skipped_no_years={s['skipped_no_years']}, "
              f"events={s['events_generated']}")
    
    # Split into batches of ~1000 events to avoid huge files
    batch_size = 1500
    total_events = len(all_new_events)
    
    for batch_idx in range(0, total_events, batch_size):
        batch = all_new_events[batch_idx:batch_idx + batch_size]
        batch_num = batch_idx // batch_size + 1
        
        # Write TypeScript file
        ts_lines = [
            "import type { HistoricalEvent } from '@/lib/types';",
            '',
            f'export const _lifespanEventsBatch{batch_num}: HistoricalEvent[] = [',
        ]
        
        for evt in batch:
            ts_lines.append(emit_ts_event(evt))
        
        ts_lines.append('];')
        
        output_file = os.path.join(output_dir, f'_lifespanEventsBatch{batch_num}.ts')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(ts_lines))
        
        print(f"\nWritten {len(batch)} events to {output_file}")
    
    # Write stats as JSON for reporting
    stats_output = os.path.join(output_dir, '_lifespanStats.json')
    with open(stats_output, 'w', encoding='utf-8') as f:
        json.dump({r: {k: v for k, v in s.items()} for r, s in stats.items()}, f, ensure_ascii=False, indent=2)
    
    print(f"\nStats written to {stats_output}")
    print(f"Total events: {total_events}")
    print(f"Total batches: {(total_events + batch_size - 1) // batch_size}")

if __name__ == '__main__':
    main()
