#!/usr/bin/env python3
"""
P2: 丰富短摘要（≤20字符）→ CBDB NIAN_HAO 年号转换 + 补充缺失籍贯
策略：
1. NIAN_HAO 年号转换：631年 → 贞观五年（631年）
2. CBDB 籍贯补充：对缺地址的条目查询 BIOG_ADDR_DATA
3. 格式优化："X时期"→"X代"，移除"人物。"等冗余
"""
import sqlite3, json, glob, sys, os, re
from opencc import OpenCC
from collections import defaultdict

DB_PATH = '/tmp/cbdb_20260530.sqlite3'
PEOPLE_DIR = '/Users/bryangan/Documents/Projects/历史平行线/src/data/people'
BATCH_SIZE = 1000

cc = OpenCC('s2t')

# regionId → CBDB dynasty names (用于 NIAN_HAO 查询)
REGION_TO_DYNASTY = {
    'qin-dynasty': ['秦'],
    'han-dynasty': ['西漢', '東漢', '漢'],
    'three-kingdoms': ['三國'],
    'western-jin': ['西晉'],
    'eastern-jin': ['東晉'],
    'northern-southern-dynasties': ['南北朝'],
    'sui-dynasty': ['隋'],
    'tang-dynasty': ['唐'],
    'song-dynasty': ['北宋', '南宋', '宋'],
    'liao-dynasty': ['遼'],
    'western-xia': ['西夏'],
    'jin-dynasty-period': ['金'],
    'yuan-dynasty': ['元'],
    'ming-dynasty': ['明'],
    'qing-dynasty': ['清'],
    'zhou-dynasty': ['周'],
}

# regionId → 朝代简称（用于摘要生成）
REGION_SHORT = {
    'qin-dynasty': '秦', 'han-dynasty': '汉', 'three-kingdoms': '三国',
    'western-jin': '西晋', 'eastern-jin': '东晋',
    'northern-southern-dynasties': '南北朝',
    'sui-dynasty': '隋', 'tang-dynasty': '唐',
    'song-dynasty': '宋', 'liao-dynasty': '辽',
    'western-xia': '西夏', 'jin-dynasty-period': '金',
    'yuan-dynasty': '元', 'ming-dynasty': '明', 'qing-dynasty': '清',
    'zhou-dynasty': '周', 'republic-of-china': '民国',
}

def build_era_lookup(conn):
    """构建 (year) → era_name 的快速查找"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c_dynasty_chn, c_nianhao_chn, c_firstyear, c_lastyear
        FROM NIAN_HAO
        WHERE c_nianhao_chn != '未詳' AND c_firstyear IS NOT NULL AND c_lastyear IS NOT NULL
    """)
    
    lookup = {}  # year → (dynasty, era_name, first_year)
    for dynasty, era, fy, ly in cursor.fetchall():
        if fy is None or ly is None:
            continue
        for y in range(fy, ly + 1):
            if y not in lookup:
                lookup[y] = (dynasty, era, fy)
    
    return lookup

def get_era(year, era_lookup, region_id=None):
    """获取年份对应的年号，返回 (era_name, era_year) 或 None
    如果提供了 region_id，会检查年号朝代是否匹配"""
    if year == 0 or year is None:
        return None
    if year in era_lookup:
        dynasty, era, first = era_lookup[year]
        # Check dynasty compatibility
        if region_id and region_id in REGION_TO_DYNASTY:
            allowed = REGION_TO_DYNASTY[region_id]
            if dynasty not in allowed:
                return None  # Era belongs to wrong dynasty, skip
        era_year = year - first + 1
        if era_year == 1:
            return (era, '元')
        return (era, str(era_year))
    return None

def clean_address_note(notes):
    """清理 BIOG_ADDR_DATA 的 c_notes"""
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

def batch_query_addresses(conn, name_tuples):
    """批量查询籍贯"""
    cursor = conn.cursor()
    results = {}
    
    trad_names = [cc.convert(n) for n, _, _ in name_tuples]
    simp_names = [n for n, _, _ in name_tuples]
    all_names = list(set(trad_names + simp_names))
    
    name_to_pids = defaultdict(list)
    
    for i in range(0, len(all_names), BATCH_SIZE):
        batch = all_names[i:i+BATCH_SIZE]
        placeholders = ','.join(['?'] * len(batch))
        cursor.execute(f"""
            SELECT c_name_chn, c_personid
            FROM BIOG_MAIN
            WHERE c_name_chn IN ({placeholders})
        """, batch)
        for c_name, pid in cursor.fetchall():
            name_to_pids[c_name].append(pid)
    
    for simp_name, birth, death in name_tuples:
        trad_name = cc.convert(simp_name)
        pids = name_to_pids.get(trad_name, [])
        if not pids:
            pids = name_to_pids.get(simp_name, [])
        if not pids:
            continue
        pid = pids[0]
        
        cursor.execute("""
            SELECT c_notes FROM BIOG_ADDR_DATA
            WHERE c_personid = ? AND c_notes IS NOT NULL AND c_notes != ''
            ORDER BY c_sequence LIMIT 3
        """, (pid,))
        for (notes,) in cursor.fetchall():
            addr = clean_address_note(notes)
            if addr:
                results[simp_name] = addr
                break
    return results

def parse_summary(summary):
    """解析现有摘要的结构"""
    result = {
        'dynasty': None,
        'address': None,
        'office': None,
        'entry': None,
        'death_year': None,
    }
    if not summary:
        return result
    
    # Extract dynasty prefix: "X时期" or "X代"
    m = re.match(r'([\u4e00-\u9fff]+)(?:时期|代)', summary)
    if m:
        result['dynasty'] = m.group(1)
    
    # Extract address: "XX人。" but NOT "X时期人。" or "X代人。"
    # Strip dynasty prefix first
    addr_text = summary
    # Remove known dynasty prefixes with 时期/代
    addr_text = re.sub(r'^[\u4e00-\u9fff]+(?:时期|代)', '', addr_text)
    m = re.search(r'([\u4e00-\u9fff]{2,8}人)[。]', addr_text)
    if m:
        result['address'] = m.group(1)
    
    # Extract office
    m = re.search(r'曾任(.+?)等职', summary)
    if m:
        result['office'] = m.group(1)
    
    # Extract entry/degree
    m = re.search(r'(进士|举人|太学生)[（(]\s*(\d+)\s*年?[)）]', summary)
    if m:
        result['entry'] = (m.group(1), m.group(2))
    
    # Extract death year
    m = re.search(r'卒于\s*(-?\d+)\s*年', summary)
    if m:
        result['death_year'] = int(m.group(1))
    
    # Extract approximate birth year
    m = re.search(r'约生于\s*(-?\d+)\s*年', summary)
    if m:
        result['birth_year_approx'] = int(m.group(1))
    
    return result

def generate_enriched_summary(parsed, death_year, era_info, address):
    """生成丰富化摘要"""
    parts = []
    dynasty = parsed['dynasty'] or '历史'
    
    # 朝代标识
    dyn_prefix = f"{dynasty}代" if dynasty != '历史' else '历史'
    
    # 科举/官职
    entry = parsed.get('entry')
    office = parsed.get('office')
    addr = address or parsed.get('address')
    
    if entry:
        parts.append(f"{dyn_prefix}{entry[0]}（{entry[1]}年）")
    elif office:
        if len(office) <= 6:
            parts.append(f"{dyn_prefix}官吏")
        else:
            parts.append(f"{dyn_prefix}{office[:4]}等职")
    elif death_year and death_year > 0:
        parts.append(f"{dyn_prefix}人物")
    else:
        parts.append(f"{dyn_prefix}人")
    
    # 籍贯
    if addr:
        if not addr.endswith('人'):
            addr = addr + '人'
        parts.append(addr)
    
    # 官职详情
    if office and len(office) > 6:
        parts.append(f"曾任{office}等职")
    
    # 卒年（含年号）
    if death_year and death_year > 0:
        if era_info:
            era_name, era_year = era_info
            year_str = f"{era_name}{era_year}年（{death_year}年）"
        else:
            year_str = f"{death_year}年"
        parts.append(f"卒于{year_str}")
    
    # 生年（约）
    by_approx = parsed.get('birth_year_approx')
    if by_approx and by_approx > 0 and not death_year:
        parts.append(f"约生于{by_approx}年")
    
    if not parts:
        return f"{dyn_prefix}历史人物"
    
    summary = "。".join(parts) + "。"
    return summary

# ========== 主程序 ==========

print("Building era lookup from NIAN_HAO...", file=sys.stderr)
conn = sqlite3.connect(DB_PATH)
era_lookup = build_era_lookup(conn)
print(f"  Loaded {len(era_lookup):,} year→era mappings", file=sys.stderr)

print("\nLoading short summary entries...", file=sys.stderr)

all_entries = []  # [(file, idx, entry)]
files_data = {}

for fp in sorted(glob.glob(f'{PEOPLE_DIR}/*.json')):
    with open(fp, encoding='utf-8') as f:
        data = json.load(f)
    files_data[fp] = data
    
    for i, p in enumerate(data):
        s = (p.get('summary') or '').strip()
        if 0 < len(s) <= 20:
            all_entries.append({
                'file': fp, 'idx': i,
                'id': p['id'], 'name': p['name'],
                'summary': s,
                'birthYear': p.get('birthYear'),
                'deathYear': p.get('deathYear'),
                'regionId': p.get('regionId'),
                'tags': p.get('tags', []),
            })

print(f"Short summaries to enrich: {len(all_entries):,}", file=sys.stderr)

# Step 1: Enrich era names + reformat
era_enriched = 0
addr_queried = 0
addr_found = 0

for entry in all_entries:
    dy = entry['deathYear']
    rid = entry.get('regionId')
    era_info = get_era(dy, era_lookup, rid) if dy and dy != 0 else None
    
    parsed = parse_summary(entry['summary'])
    new_summary = generate_enriched_summary(parsed, dy, era_info, None)
    
    if new_summary != entry['summary']:
        files_data[entry['file']][entry['idx']]['summary'] = new_summary
        era_enriched += 1
        entry['_enriched'] = True

print(f"  Era name enriched: {era_enriched:,}", file=sys.stderr)

# Step 2: Query CBDB for missing addresses
needs_addr = [e for e in all_entries if not parse_summary(e['summary']).get('address')]
print(f"  Entries without address: {len(needs_addr):,}", file=sys.stderr)

total_batches = (len(needs_addr) + BATCH_SIZE - 1) // BATCH_SIZE

for batch_idx in range(0, len(needs_addr), BATCH_SIZE):
    batch = needs_addr[batch_idx:batch_idx + BATCH_SIZE]
    batch_num = batch_idx // BATCH_SIZE + 1
    
    name_tuples = [(e['name'], e.get('birthYear'), e.get('deathYear')) for e in batch]
    addresses = batch_query_addresses(conn, name_tuples)
    addr_queried += len(batch)
    
    for entry in batch:
        if entry['name'] in addresses:
            addr = addresses[entry['name']]
            dy = entry['deathYear']
            rid = entry.get('regionId')
            era_info = get_era(dy, era_lookup, rid) if dy and dy != 0 else None
            parsed = parse_summary(entry['summary'])
            new_summary = generate_enriched_summary(parsed, dy, era_info, addr)
            files_data[entry['file']][entry['idx']]['summary'] = new_summary
            addr_found += 1
    
    if batch_num % 10 == 0 or batch_num == total_batches:
        pct = min(100, batch_num * 100 // total_batches)
        print(f"  Address query: {batch_num}/{total_batches} ({pct}%) — {addr_found:,} found", file=sys.stderr)

print(f"  Addresses found: {addr_found:,} / {addr_queried:,}", file=sys.stderr)

conn.close()

# Write back
print(f"\nWriting updated JSON files...", file=sys.stderr)
for fp, data in files_data.items():
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

total_enriched = era_enriched + addr_found
print(f"\n✅ Done: {total_enriched:,} summaries enriched", file=sys.stderr)
print(f"   Era name: {era_enriched:,}", file=sys.stderr)
print(f"   Address added: {addr_found:,}", file=sys.stderr)
