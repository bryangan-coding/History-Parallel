#!/usr/bin/env python3
"""
从 CBDB POSTED_TO_OFFICE_DATA.c_notes 提取可靠的历史事件描述
来源包括：宋史、墓志铭、续长编等一手史料
仅从可验证的史料中提取，不编造任何信息
"""
import sqlite3, json, glob, sys, os, re
from opencc import OpenCC

DB_PATH = '/tmp/cbdb_20260530.sqlite3'
PEOPLE_DIR = '/Users/bryangan/Documents/Projects/历史平行线/src/data/people'
BATCH_SIZE = 500

cc = OpenCC('s2t')

def clean_office_note(note):
    """清洗 POSTED_TO_OFFICE_DATA 的 c_notes，提取有用历史描述"""
    if not note:
        return None
    
    # Remove Hartwell metadata
    note = re.sub(r'Hartwell\s+defined\s+the\s+office\s+as\s+\w+[^。）]*(?:。|）)', '', note)
    note = re.sub(r'LZL\s*MasterFileLine\w*', '', note)
    note = re.sub(r'LZL\s*Master\s*File\s*Line\s*ID\w*', '', note)
    
    # Remove purely English text
    note = re.sub(r'\([^)]*[a-zA-Z]{3,}[^)]*\)', '', note)
    
    # Clean whitespace
    note = re.sub(r'\s+', '', note)
    note = re.sub(r'\x7f', '', note)
    note = note.strip()
    
    # Must contain Chinese and be meaningful
    if len(note) < 15 or not re.search(r'[\u4e00-\u9fff]{5,}', note):
        return None
    
    # Must cite a specific source or describe a specific event
    # Sources: 墓誌, 宋史, 續長編, 要錄, 實錄, 碑, 記, 狀, etc.
    has_source = bool(re.search(r'[據按依見考]|墓誌|碑|史卷|長編|要錄|實錄|記曰|狀云', note))
    has_event = bool(re.search(r'遷|除|改|授|知|判|兼|拜|擢|貶|罷|卒|薨', note))
    
    if not (has_source or has_event):
        return None
    
    # Truncate at ~80 chars
    if len(note) > 80:
        # Find a good break point (。or ；)
        break_at = note.rfind('。', 0, 80)
        if break_at < 30:
            break_at = note.rfind('；', 0, 80)
        if break_at >= 30:
            note = note[:break_at+1]
        else:
            note = note[:80]
    
    return note

def extract_events(conn, pid):
    """提取人物的可信历史事件（最多2个）"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c_notes FROM POSTED_TO_OFFICE_DATA
        WHERE c_personid = ? AND c_notes IS NOT NULL AND c_notes != ''
        AND length(c_notes) > 20
        ORDER BY c_firstyear DESC
        LIMIT 8
    """, (pid,))
    
    events = []
    for (note,) in cursor.fetchall():
        cleaned = clean_office_note(note)
        if cleaned and cleaned not in events:
            events.append(cleaned)
        if len(events) >= 2:
            break
    
    return events

def enrich_summary_with_events(summary, events):
    """在摘要后添加可信历史事件"""
    if not events:
        return summary
    
    # Only add if summary is currently short (<100 chars) — don't touch already-enriched ones
    if len(summary) >= 100:
        return summary
    
    # Take first event only, keep it concise
    event_text = events[0]
    
    # Determine how to add: append after existing content
    if summary.endswith('。'):
        return summary[:-1] + "。" + event_text + "。"
    else:
        return summary + "。" + event_text + "。"


# ========== 主程序 ==========

print("Loading Tier 1 CBDB data...", file=sys.stderr)

# Collect Tier 1 CBDB entries WITHOUT GT enrichment
tier1_entries = []
files_data = {}

for fp in sorted(glob.glob(f'{PEOPLE_DIR}/*.json')):
    with open(fp, encoding='utf-8') as f:
        data = json.load(f)
    files_data[fp] = data
    
    for i, p in enumerate(data):
        srcs = p.get('sourceIds', [])
        if 'src-cbdb' in srcs:
            by = p.get('birthYear')
            dy = p.get('deathYear')
            if by and dy:  # Tier 1
                # Only process entries NOT already enriched with GT
                if 'src-grand-timeline' not in srcs and len(p.get('summary', '')) < 100:
                    tier1_entries.append({
                        'file': fp, 'idx': i,
                        'name': p['name'],
                        'birthYear': by, 'deathYear': dy,
                    })

print(f"Tier 1 entries to check for events: {len(tier1_entries):,}", file=sys.stderr)

conn = sqlite3.connect(DB_PATH)
enriched = 0
events_found = 0

total_batches = (len(tier1_entries) + BATCH_SIZE - 1) // BATCH_SIZE

for batch_idx in range(0, len(tier1_entries), BATCH_SIZE):
    batch = tier1_entries[batch_idx:batch_idx + BATCH_SIZE]
    batch_num = batch_idx // BATCH_SIZE + 1
    
    # Batch query person IDs
    cursor = conn.cursor()
    trad_names = [cc.convert(e['name']) for e in batch]
    simp_names = [e['name'] for e in batch]
    all_names = list(set(trad_names + simp_names))
    
    # Map name -> pid
    name_to_pids = {}
    for i in range(0, len(all_names), BATCH_SIZE):
        sub = all_names[i:i+BATCH_SIZE]
        placeholders = ','.join(['?']*len(sub))
        cursor.execute(f"""
            SELECT c_name_chn, c_personid FROM BIOG_MAIN
            WHERE c_name_chn IN ({placeholders})
        """, sub)
        for name, pid in cursor.fetchall():
            if name not in name_to_pids:
                name_to_pids[name] = pid
    
    for entry in batch:
        name = entry['name']
        trad = cc.convert(name)
        pid = name_to_pids.get(name) or name_to_pids.get(trad)
        
        if not pid:
            continue
        
        events = extract_events(conn, pid)
        if events:
            events_found += 1
            old_summary = files_data[entry['file']][entry['idx']].get('summary', '')
            new_summary = enrich_summary_with_events(old_summary, events)
            
            if new_summary and new_summary != old_summary:
                files_data[entry['file']][entry['idx']]['summary'] = new_summary
                enriched += 1
    
    if batch_num % 20 == 0 or batch_num == total_batches:
        pct = min(100, batch_num * 100 // total_batches)
        print(f"  Progress: {batch_num}/{total_batches} ({pct}%) — {events_found:,} with events, {enriched:,} enriched", file=sys.stderr)

conn.close()

# Write back
print(f"\nWriting updated files...", file=sys.stderr)
for fp, data in files_data.items():
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ {events_found:,} entries have verifiable events, {enriched:,} summaries enriched", file=sys.stderr)
