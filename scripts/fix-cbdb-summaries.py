#!/usr/bin/env python3
"""
修复 CBDB 模板化 summary → 从 CBDB 数据库提取真实官职/科举信息生成有意义的摘要
处理约 67,443 条数据，分批查询避免 OOM
"""
import sqlite3, json, glob, sys, os, re
from opencc import OpenCC
from collections import defaultdict

DB_PATH = '/tmp/cbdb_20260530.sqlite3'
PEOPLE_DIR = '/Users/bryangan/Documents/Projects/历史平行线/src/data/people'
BATCH_SIZE = 500   # 每批查询的姓名数

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
    'republic-of-china': '民国',
    'zhou-dynasty': '周',
}

def get_dynasty_name(region_id):
    """从 regionId 推导朝代名"""
    if region_id in REGION_NAMES:
        return REGION_NAMES[region_id]
    return None

def batch_query_cbdb(conn, name_tuples):
    """批量查询 CBDB，返回 (name_simp, pid, birth, death, offices, entries) 列表"""
    cursor = conn.cursor()
    results = []
    
    # Build IN clause with traditional names
    trad_names = [cc.convert(n) for n, _, _, _ in name_tuples]
    simp_names = [n for n, _, _, _ in name_tuples]
    
    # Query by traditional + simplified names
    all_names = list(set(trad_names + simp_names))
    
    # Split into sub-batches for IN clause
    for i in range(0, len(all_names), BATCH_SIZE):
        batch = all_names[i:i+BATCH_SIZE]
        placeholders = ','.join(['?'] * len(batch))
        
        cursor.execute(f"""
            SELECT c_name_chn, c_personid, c_birthyear, c_deathyear
            FROM BIOG_MAIN
            WHERE c_name_chn IN ({placeholders})
        """, batch)
        
        rows = cursor.fetchall()
        
        # Build name→pids map
        name_to_pids = defaultdict(list)
        for c_name, pid, by, dy in rows:
            name_to_pids[c_name].append((pid, by, dy))
        
        # Match back to original simplified names
        for simp_name, birth_year, death_year, _ in name_tuples:
            trad_name = cc.convert(simp_name)
            
            # Try traditional first
            candidates = name_to_pids.get(trad_name, [])
            if not candidates:
                candidates = name_to_pids.get(simp_name, [])
            
            pid = None
            if len(candidates) == 1:
                pid = candidates[0][0]
            elif len(candidates) > 1:
                # Multiple matches: use birth/death year to disambiguate
                for cp, cby, cdy in candidates:
                    score = 0
                    if birth_year and cby and cby > 0 and abs(birth_year - cby) <= 2:
                        score += 2
                    if death_year and cdy and cdy > 0 and abs(death_year - cdy) <= 2:
                        score += 2
                    if score >= 2:
                        pid = cp
                        break
                if not pid:
                    pid = candidates[0][0]  # fallback
            
            results.append((simp_name, pid))
    
    return results

def query_office_info(conn, pid):
    """查询一个人的官职信息（最多 3 个）"""
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
    """查询一个人的科举/仕途入门信息"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ec.c_entry_desc, ed.c_year
        FROM ENTRY_DATA ed
        JOIN ENTRY_CODES ec ON ed.c_entry_code = ec.c_entry_code
        WHERE ed.c_personid = ?
        AND ed.c_entry_code != 0
        ORDER BY ed.c_year DESC
        LIMIT 1
    """, (pid,))
    return cursor.fetchall()

def generate_summary(dynasty_name, birth_year, death_year, offices, entries):
    """根据提取的信息生成有意义的摘要"""
    parts = []
    
    # 朝代 + 身份
    if dynasty_name:
        prefix = f"{dynasty_name}时期"
    else:
        prefix = "历史"
    
    # 科举信息
    entry_str = None
    for desc, year in entries:
        if desc and year and year > 0:
            # Simplify entry description
            if 'jinshi' in desc.lower() or '進士' in desc:
                entry_str = f"进士（{year}年）"
            elif 'juren' in desc.lower() or '舉人' in desc:
                entry_str = f"举人（{year}年）"
            elif 'student' in desc.lower():
                entry_str = f"太学生（{year}年）"
            else:
                entry_str = f"{desc}（{year}年）"
            break
    
    if entry_str:
        parts.append(f"{prefix}{entry_str}")
    elif offices:
        parts.append(f"{prefix}官吏")
    else:
        if death_year and death_year > 0:
            parts.append(f"{prefix}人物")
    
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
    
    if not parts:
        return f"{prefix}历史人物"
    
    # Join with periods
    summary = "。".join(parts) + "。"
    
    # Ensure summary is not too long
    if len(summary) > 120:
        summary = summary[:117] + "..."
    
    return summary

def process_batch(conn, name_tuples):
    """处理一批姓名，返回 (name_simp, new_summary) 列表"""
    matched = batch_query_cbdb(conn, name_tuples)
    
    summaries = {}
    for simp_name, pid in matched:
        if pid is None:
            continue
        
        # Query office and entry info
        offices = query_office_info(conn, pid)
        entries = query_entry_info(conn, pid)
        
        # Find original data for birth/death/dynasty
        orig = None
        for n, by, dy, rid in name_tuples:
            if n == simp_name:
                orig = (by, dy, rid)
                break
        
        if orig:
            dynasty = get_dynasty_name(orig[2])
            new_summary = generate_summary(dynasty, orig[0], orig[1], offices, entries)
            summaries[simp_name] = new_summary
    
    return summaries

# ========== 主程序 ==========

print("Loading CBDB src data from all JSON files...", file=sys.stderr)

# 收集所有 src-cbdb 条目的信息
all_cbdb_entries = []  # [(file, idx_in_file, name, birthYear, deathYear, regionId)]
files_data = {}  # file → loaded data

for fp in sorted(glob.glob(f'{PEOPLE_DIR}/*.json')):
    with open(fp, encoding='utf-8') as f:
        data = json.load(f)
    files_data[fp] = data
    
    for i, p in enumerate(data):
        if 'src-cbdb' in p.get('sourceIds', []):
            all_cbdb_entries.append({
                'file': fp,
                'idx': i,
                'name': p['name'],
                'birthYear': p.get('birthYear'),
                'deathYear': p.get('deathYear'),
                'regionId': p.get('regionId'),
            })

print(f"Total src-cbdb entries to process: {len(all_cbdb_entries):,}", file=sys.stderr)

conn = sqlite3.connect(DB_PATH)
updated_count = 0
skipped_count = 0

# 分批处理
total_batches = (len(all_cbdb_entries) + BATCH_SIZE - 1) // BATCH_SIZE

for batch_idx in range(0, len(all_cbdb_entries), BATCH_SIZE):
    batch = all_cbdb_entries[batch_idx:batch_idx + BATCH_SIZE]
    batch_num = batch_idx // BATCH_SIZE + 1
    
    # Prepare name tuples for batch query
    name_tuples = [(e['name'], e['birthYear'], e['deathYear'], e['regionId']) for e in batch]
    
    # Get new summaries
    summaries = process_batch(conn, name_tuples)
    
    # Update entries in memory
    for entry in batch:
        name = entry['name']
        if name in summaries:
            new_summary = summaries[name]
            old_summary = files_data[entry['file']][entry['idx']].get('summary', '')
            
            # Only update if summary is generic
            if '其事迹见于相关史料记载' in old_summary or len(old_summary) < 30:
                files_data[entry['file']][entry['idx']]['summary'] = new_summary
                updated_count += 1
            else:
                skipped_count += 1
    
    if batch_num % 20 == 0 or batch_num == total_batches:
        pct = min(100, batch_num * 100 // total_batches)
        print(f"  Progress: {batch_num}/{total_batches} batches ({pct}%) — {updated_count:,} updated, {skipped_count:,} skipped", file=sys.stderr)

conn.close()

# 写回 JSON 文件
print(f"\nWriting updated JSON files...", file=sys.stderr)
for fp, data in files_data.items():
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  {os.path.basename(fp)} ({len(data)} entries)", file=sys.stderr)

print(f"\n✅ Done: {updated_count:,} summaries updated, {skipped_count:,} unchanged", file=sys.stderr)
