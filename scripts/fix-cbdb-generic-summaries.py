#!/usr/bin/env python3
"""
修复 CBDB 泛化模板 summary（"X时期历史人物"）→ CBDB名称匹配→提取官职/科举/籍贯→生成摘要
处理约 2,988 条无生卒年的 CBDB 条目，只通过名称匹配
"""
import sqlite3, json, glob, sys, os, re
from opencc import OpenCC
from collections import defaultdict

DB_PATH = '/tmp/cbdb_20260530.sqlite3'
PEOPLE_DIR = '/Users/bryangan/Documents/Projects/历史平行线/src/data/people'
BATCH_SIZE = 500

cc = OpenCC('s2t')  # 简体→繁体

# regionId → 朝代简称
REGION_NAMES = {
    'qin-dynasty': '秦', 'han-dynasty': '汉', 'three-kingdoms': '三国',
    'western-jin': '西晋', 'eastern-jin': '东晋',
    'sixteen-kingdoms': '十六国', 'northern-southern-dynasties': '南北朝',
    'sui-dynasty': '隋', 'tang-dynasty': '唐',
    'five-dynasties': '五代', 'ten-kingdoms': '十国',
    'song-dynasty': '宋', 'liao-dynasty': '辽',
    'western-xia': '西夏', 'jin-dynasty-period': '金',
    'yuan-dynasty': '元', 'ming-dynasty': '明', 'qing-dynasty': '清',
    'republic-of-china': '民国', 'zhou-dynasty': '周',
}

def clean_address_note(notes):
    """清理 BIOG_ADDR_DATA 的 c_notes，提取纯地址信息"""
    if not notes:
        return None
    cleaned = re.sub(r'[（(][^)）]*[)）]', '', notes)
    cleaned = re.sub(r'[《][^》]*[》]', '', cleaned)
    cleaned = cleaned.replace('\x7f', '').strip()
    
    if not cleaned or len(cleaned) < 2:
        return None
    
    if '人' in cleaned:
        match = re.search(r'([\u4e00-\u9fff]{2,6}人)', cleaned)
        if match:
            return match.group(1)
    
    match = re.match(r'([\u4e00-\u9fff]{2,8}(?:府|縣|州))', cleaned)
    if match:
        return match.group(1)
    
    parts = cleaned.split('-')
    addr_parts = [p for p in parts if p.strip() and not p.strip().isdigit()]
    if addr_parts:
        return '-'.join(addr_parts[:2])
    
    return None

def get_dynasty_name(region_id):
    if region_id in REGION_NAMES:
        return REGION_NAMES[region_id]
    return None

def batch_query_cbdb(conn, name_tuples):
    """批量查询 CBDB，返回 {simp_name: [(pid, birth, death, index_year), ...]}"""
    cursor = conn.cursor()
    results = defaultdict(list)
    
    trad_names = [cc.convert(n) for n, _ in name_tuples]
    simp_names = [n for n, _ in name_tuples]
    all_names = list(set(trad_names + simp_names))
    
    for i in range(0, len(all_names), BATCH_SIZE):
        batch = all_names[i:i+BATCH_SIZE]
        placeholders = ','.join(['?'] * len(batch))
        
        cursor.execute(f"""
            SELECT c_name_chn, c_personid, c_birthyear, c_deathyear, c_index_year
            FROM BIOG_MAIN
            WHERE c_name_chn IN ({placeholders})
        """, batch)
        
        rows = cursor.fetchall()
        
        # Map names to matches
        name_to_rows = defaultdict(list)
        for c_name, pid, by, dy, iy in rows:
            name_to_rows[c_name].append((pid, by, dy, iy))
        
        # Match back to simplified names
        for simp_name, _ in name_tuples:
            trad_name = cc.convert(simp_name)
            matches = name_to_rows.get(trad_name, [])
            if not matches:
                matches = name_to_rows.get(simp_name, [])
            if matches:
                results[simp_name] = matches
    
    return dict(results)

def query_office_info(conn, pid):
    """查询官职信息（最多 3 个）"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT o.c_office_chn, pto.c_firstyear
        FROM POSTED_TO_OFFICE_DATA pto
        LEFT JOIN OFFICE_CODES o ON pto.c_office_id = o.c_office_id
        WHERE pto.c_personid = ?
        AND pto.c_office_id != 0
        AND o.c_office_chn IS NOT NULL
        AND o.c_office_chn != '未詳'
        ORDER BY pto.c_firstyear DESC
        LIMIT 3
    """, (pid,))
    return cursor.fetchall()

def query_entry_info(conn, pid):
    """查询科举/仕途入门信息"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ec.c_entry_desc_chn, ed.c_year
        FROM ENTRY_DATA ed
        JOIN ENTRY_CODES ec ON ed.c_entry_code = ec.c_entry_code
        WHERE ed.c_personid = ?
        AND ed.c_entry_code != 0
        ORDER BY ed.c_year DESC
        LIMIT 1
    """, (pid,))
    return cursor.fetchall()

def query_address(conn, pid):
    """查询籍贯"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c_notes FROM BIOG_ADDR_DATA
        WHERE c_personid = ? AND c_notes IS NOT NULL AND c_notes != ''
        ORDER BY c_sequence LIMIT 3
    """, (pid,))
    for (notes,) in cursor.fetchall():
        addr = clean_address_note(notes)
        if addr:
            return addr
    return None

def pick_best_pid(matches):
    """从多个匹配中选择最佳 pid：优先有数据的"""
    if len(matches) == 1:
        return matches[0]
    
    # Score each match: +1 for birth, +1 for death, +1 for index_year
    best = None
    best_score = -1
    for pid, by, dy, iy in matches:
        score = 0
        if by and by > 0: score += 1
        if dy and dy > 0: score += 1
        if iy and iy > 0: score += 1
        if score > best_score:
            best_score = score
            best = (pid, by, dy, iy)
    
    return best if best else matches[0]

def generate_summary(dynasty_name, birth_year, death_year, address, offices, entries):
    """生成有意义的摘要"""
    parts = []
    
    prefix = f"{dynasty_name}时期" if dynasty_name else "历史"
    
    # 科举信息
    entry_str = None
    for desc, year in entries:
        if desc and year and year > 0:
            if '進士' in desc:
                entry_str = f"进士（{year}年）"
            elif '舉人' in desc:
                entry_str = f"举人（{year}年）"
            elif '太學' in desc:
                entry_str = f"太学生（{year}年）"
            elif '科舉' in desc:
                entry_str = f"{desc}（{year}年）"
            else:
                entry_str = f"{desc}（{year}年）"
            break
    
    if entry_str:
        parts.append(f"{prefix}{entry_str}")
    elif offices:
        parts.append(f"{prefix}官吏")
    elif death_year and death_year > 0:
        parts.append(f"{prefix}人物")
    else:
        parts.append(f"{prefix}人")
    
    # 籍贯
    if address:
        if address.endswith('人'):
            parts.append(address)
        else:
            parts.append(f"{address}人")
    
    # 官职（取 top 2）
    top_offices = []
    for office_name, year in offices:
        if office_name and '未詳' not in office_name:
            top_offices.append(office_name)
    if top_offices:
        offices_str = "、".join(top_offices[:2])
        parts.append(f"曾任{offices_str}等职")
    
    # 卒年
    if death_year and death_year > 0:
        parts.append(f"卒于{death_year}年")
    elif birth_year and birth_year > 0:
        parts.append(f"约生于{birth_year}年")
    elif not address and not top_offices:
        # No useful data from CBDB, add "生平不详"
        pass  # Don't add, the prefix is sufficient
    
    if not parts:
        return f"{prefix}历史人物"
    
    summary = "。".join(parts) + "。"
    if len(summary) > 120:
        summary = summary[:117] + "..."
    
    return summary

def generate_fallback_summary(dynasty_name, tags):
    """为未匹配条目生成 fallback 摘要"""
    tag_str = "、".join(tags[:3]) if tags else ""
    if tag_str:
        return f"{dynasty_name}时期{tag_str}相关人物，生平事迹不详。"
    return f"{dynasty_name}时期人物，生平事迹不详。"

# ========== 主程序 ==========

print("Loading generic template entries...", file=sys.stderr)

all_generic = []  # [(file, idx, id, name, regionId, tags)]
files_data = {}

for fp in sorted(glob.glob(f'{PEOPLE_DIR}/*.json')):
    with open(fp, encoding='utf-8') as f:
        data = json.load(f)
    files_data[fp] = data
    
    for i, p in enumerate(data):
        s = p.get('summary', '')
        if '时期历史人物' in s and len(s) <= 15:
            all_generic.append({
                'file': fp, 'idx': i,
                'id': p['id'], 'name': p['name'],
                'regionId': p.get('regionId'),
                'tags': p.get('tags', []),
            })

print(f"Generic template entries to fix: {len(all_generic):,}", file=sys.stderr)

conn = sqlite3.connect(DB_PATH)
updated_count = 0
matched_count = 0
fallback_count = 0
total_batches = (len(all_generic) + BATCH_SIZE - 1) // BATCH_SIZE

for batch_idx in range(0, len(all_generic), BATCH_SIZE):
    batch = all_generic[batch_idx:batch_idx + BATCH_SIZE]
    batch_num = batch_idx // BATCH_SIZE + 1
    
    # Prepare name tuples
    name_tuples = [(e['name'], e['regionId']) for e in batch]
    cbdb_matches = batch_query_cbdb(conn, name_tuples)
    
    for entry in batch:
        name = entry['name']
        dynasty = get_dynasty_name(entry['regionId'])
        
        if name in cbdb_matches:
            matches = cbdb_matches[name]
            pid, by, dy, iy = pick_best_pid(matches)
            
            # Extract enrichment data
            offices = query_office_info(conn, pid)
            entries = query_entry_info(conn, pid)
            address = query_address(conn, pid)
            
            # Update birth/death if available from CBDB
            if by and by > 0 and not files_data[entry['file']][entry['idx']].get('birthYear'):
                files_data[entry['file']][entry['idx']]['birthYear'] = by
            if dy and dy > 0 and not files_data[entry['file']][entry['idx']].get('deathYear'):
                files_data[entry['file']][entry['idx']]['deathYear'] = dy
            
            new_summary = generate_summary(dynasty, by, dy, address, offices, entries)
            matched_count += 1
        else:
            new_summary = generate_fallback_summary(dynasty, entry['tags'])
            fallback_count += 1
        
        files_data[entry['file']][entry['idx']]['summary'] = new_summary
        updated_count += 1
    
    if batch_num % 10 == 0 or batch_num == total_batches:
        pct = min(100, batch_num * 100 // total_batches)
        print(f"  Progress: {batch_num}/{total_batches} ({pct}%) — {matched_count:,} matched, {fallback_count:,} fallback", file=sys.stderr)

conn.close()

# Write back
print(f"\nWriting updated JSON files...", file=sys.stderr)
for fp, data in files_data.items():
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done: {updated_count:,} entries rewritten", file=sys.stderr)
print(f"   CBDB matched: {matched_count:,}", file=sys.stderr)
print(f"   Fallback: {fallback_count:,}", file=sys.stderr)
