#!/usr/bin/env python3
"""
丰富 CBDB Tier 1 人物（生卒年齐全）的摘要：添加籍贯信息
"""
import sqlite3, json, glob, sys, os, re
from opencc import OpenCC
from collections import defaultdict

DB_PATH = '/tmp/cbdb_20260530.sqlite3'
PEOPLE_DIR = '/Users/bryangan/Documents/Projects/历史平行线/src/data/people'
BATCH_SIZE = 500

cc = OpenCC('s2t')

def clean_address_note(notes):
    """清理 BIOG_ADDR_DATA 的 c_notes，提取纯地址信息"""
    if not notes:
        return None
    # 移除括号内的参考来源（如 宋人傳記資料索引(電子版)）
    cleaned = re.sub(r'[（(][^)）]*[)）]', '', notes)
    cleaned = re.sub(r'[《][^》]*[》]', '', cleaned)
    # 移除明显的元数据标记
    cleaned = cleaned.replace('\x7f', '').strip()
    
    if not cleaned or len(cleaned) < 2:
        return None
    
    # 常见格式：XX人 / XX-XX-XX / XX府XX縣
    # 只取有用的地址部分
    if '人' in cleaned:
        # "婺源人" → "婺源人"
        match = re.search(r'([\u4e00-\u9fff]{2,6}人)', cleaned)
        if match:
            return match.group(1)
    
    # 尝试提取地点名称
    match = re.match(r'([\u4e00-\u9fff]{2,8}(?:府|縣|州))', cleaned)
    if match:
        return match.group(1)
    
    # 带连字符的格式：南京-蘇州府-吳縣
    parts = cleaned.split('-')
    addr_parts = [p for p in parts if p.strip() and not p.strip().isdigit()]
    if addr_parts:
        return '-'.join(addr_parts[:2])
    
    return None

def batch_query_addresses(conn, name_tuples):
    """批量查询地址信息"""
    cursor = conn.cursor()
    
    # Build traditional names
    trad_lookup = {}
    for name, birth, death in name_tuples:
        trad = cc.convert(name)
        trad_lookup[trad] = (name, birth, death)
        trad_lookup[name] = (name, birth, death)  # also try simplified
    
    all_names = list(set(trad_lookup.keys()))
    
    # Map cbdb name → list of (pid, birth, death)
    name_to_pids = defaultdict(list)
    
    for i in range(0, len(all_names), BATCH_SIZE):
        batch = all_names[i:i+BATCH_SIZE]
        placeholders = ','.join(['?']*len(batch))
        
        cursor.execute(f"""
            SELECT c_name_chn, c_personid, c_birthyear, c_deathyear
            FROM BIOG_MAIN
            WHERE c_name_chn IN ({placeholders})
        """, batch)
        
        for c_name, pid, by, dy in cursor.fetchall():
            name_to_pids[c_name].append((pid, by, dy))
    
    # Resolve to unique pid per simplified name
    results = {}  # simp_name → (pid, address_str)
    
    for trad_name, (simp_name, birth, death) in trad_lookup.items():
        candidates = name_to_pids.get(trad_name, [])
        if not candidates:
            continue
        
        pid = None
        if len(candidates) == 1:
            pid = candidates[0][0]
        else:
            for cp, cby, cdy in candidates:
                score = 0
                if birth and cby and cby > 0 and abs(birth - cby) <= 2:
                    score += 2
                if death and cdy and cdy > 0 and abs(death - cdy) <= 2:
                    score += 2
                if score >= 2:
                    pid = cp
                    break
            if not pid:
                pid = candidates[0][0]
        
        if pid and simp_name not in results:
            # Get address data
            cursor.execute("""
                SELECT c_notes FROM BIOG_ADDR_DATA
                WHERE c_personid = ? AND c_notes IS NOT NULL AND c_notes != ''
                ORDER BY c_sequence
                LIMIT 3
            """, (pid,))
            notes_list = cursor.fetchall()
            
            for (notes,) in notes_list:
                addr = clean_address_note(notes)
                if addr:
                    results[simp_name] = addr
                    break  # Take first valid address
    
    return results

def enrich_summary_with_address(summary, address):
    """在摘要中插入籍贯信息"""
    if not address or not summary:
        return summary
    
    # Clean address: remove dots, brackets
    address = address.replace('·', '').replace('．', '').strip()
    
    # Check if address already ends with 人
    if address.endswith('人'):
        insert = address + "。"
    else:
        insert = address + "人。"
    
    # Find the dynasty prefix
    dynasty_match = re.match(r'^([\u4e00-\u9fff]+时期)', summary)
    if dynasty_match:
        prefix = dynasty_match.group(1)
        rest = summary[len(prefix):]
        
        # Check if rest starts with 进士/举人/官吏 etc.
        if rest.startswith('进士') or rest.startswith('举人') or rest.startswith('官吏') or rest.startswith('人物') or rest.startswith('examination'):
            return prefix + insert + rest
        elif rest.startswith('。'):
            return prefix + insert + rest[1:]
    
    return summary


# ========== 主程序 ==========

print("Loading existing CBDB Tier 1 data...", file=sys.stderr)

# Collect Tier 1 CBDB entries
tier1_entries = []  # (file, idx, name, birthYear, deathYear, regionId)
files_data = {}

for fp in sorted(glob.glob(f'{PEOPLE_DIR}/*.json')):
    with open(fp, encoding='utf-8') as f:
        data = json.load(f)
    files_data[fp] = data
    
    for i, p in enumerate(data):
        if 'src-cbdb' in p.get('sourceIds', []):
            by = p.get('birthYear')
            dy = p.get('deathYear')
            if by and dy:  # Tier 1 only
                tier1_entries.append({
                    'file': fp, 'idx': i,
                    'name': p['name'],
                    'birthYear': by, 'deathYear': dy,
                    'regionId': p.get('regionId'),
                })

print(f"Tier 1 entries to enrich: {len(tier1_entries):,}", file=sys.stderr)

conn = sqlite3.connect(DB_PATH)
enriched_count = 0
added_count = 0

total_batches = (len(tier1_entries) + BATCH_SIZE - 1) // BATCH_SIZE

for batch_idx in range(0, len(tier1_entries), BATCH_SIZE):
    batch = tier1_entries[batch_idx:batch_idx + BATCH_SIZE]
    batch_num = batch_idx // BATCH_SIZE + 1
    
    name_tuples = [(e['name'], e['birthYear'], e['deathYear']) for e in batch]
    addresses = batch_query_addresses(conn, name_tuples)
    
    for entry in batch:
        name = entry['name']
        if name in addresses:
            addr = addresses[name]
            old_summary = files_data[entry['file']][entry['idx']].get('summary', '')
            new_summary = enrich_summary_with_address(old_summary, addr)
            
            if new_summary and new_summary != old_summary:
                files_data[entry['file']][entry['idx']]['summary'] = new_summary
                enriched_count += 1
            added_count += 1
    
    if batch_num % 20 == 0 or batch_num == total_batches:
        pct = min(100, batch_num * 100 // total_batches)
        print(f"  Progress: {batch_num}/{total_batches} ({pct}%) — {enriched_count:,} enriched", file=sys.stderr)

conn.close()

# Write back
print(f"\nWriting updated files...", file=sys.stderr)
for fp, data in files_data.items():
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ Enriched {enriched_count:,} Tier 1 entries with address info", file=sys.stderr)
print(f"   Total Tier 1 with addresses: {added_count:,}", file=sys.stderr)
