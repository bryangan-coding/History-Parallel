#!/usr/bin/env python3
"""
P2 Post-Fix: 全量年号转换 + "时期"→"代"统一
针对所有 CBDB 条目（不限长度），使用 regionId 确定朝代，用 NIAN_HAO 转换年号
"""
import sqlite3, json, glob, sys, re
from collections import defaultdict

DB_PATH = '/tmp/cbdb_20260530.sqlite3'
PEOPLE_DIR = '/Users/bryangan/Documents/Projects/历史平行线/src/data/people'

# regionId → 朝代简称
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

# regionId → CBDB dynasty names for era matching
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

def build_era_lookup(conn):
    """构建 year → (dynasty, era_name, first_year) 的查找"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c_dynasty_chn, c_nianhao_chn, c_firstyear, c_lastyear
        FROM NIAN_HAO
        WHERE c_nianhao_chn != '未詳' AND c_firstyear IS NOT NULL AND c_lastyear IS NOT NULL
    """)
    lookup = {}
    for dynasty, era, fy, ly in cursor.fetchall():
        if fy is None or ly is None:
            continue
        for y in range(fy, ly + 1):
            if y not in lookup:  # First match wins (avoid overwrites)
                lookup[y] = (dynasty, era, fy)
    return lookup

def get_era_text(year, era_lookup, region_id):
    """获取年号文本，如 '貞觀5年（631年）'，无匹配则返回 '631年'"""
    if not year or year == 0:
        return None
    if year not in era_lookup:
        return f"{year}年"
    
    dynasty, era, first = era_lookup[year]
    
    # Check dynasty compatibility
    if region_id in REGION_TO_DYNASTY:
        if dynasty not in REGION_TO_DYNASTY[region_id]:
            return f"{year}年"  # Wrong dynasty, skip era
    
    era_year = year - first + 1
    if era_year == 1:
        return f"{era}元年（{year}年）"
    return f"{era}{era_year}年（{year}年）"

def fix_summary(summary, dynasty_name, death_year, era_lookup, region_id):
    """修复单条摘要"""
    if not summary:
        return summary
    
    s = summary
    
    # Step 0: Fix "历史X" → correct dynasty prefix
    if s.startswith('历史') and dynasty_name != '历史':
        s = dynasty_name + '代' + s[2:]  # '历史人' → '宋代人'
        s = s.replace('代人。代', '代')  # Clean up '代人。代人' → '代人'
    
    # Step 1: Replace "X时期" → "X代"
    for dyn_short in set(REGION_SHORT.values()):
        s = re.sub(
            re.escape(dyn_short) + r'时期(?=[^人])',
            dyn_short + '代',
            s
        )
    
    # Step 2: Replace "卒于YYYY年" with era format
    if death_year and death_year != 0:
        era_text = get_era_text(death_year, era_lookup, region_id)
        s = re.sub(
            r'卒于\s*' + re.escape(str(death_year)) + r'\s*年',
            f'卒于{era_text}',
            s
        )
    
    # Step 3: Clean up
    s = re.sub(r'generated from personid=\d+ by kinship code = \d+ or \d+人[。]?', '', s)
    s = re.sub(r'[。]{2,}', '。', s)
    s = re.sub(r'^[。]', '', s)
    s = re.sub(r'[。]人物[。](?=.+[。])', '。', s)
    s = re.sub(r'代人[。]代人?', '代人', s)  # Fix '代人。代人' → '代人'
    
    s = s.strip()
    if not s or s == '。':
        s = f"{dynasty_name}代人物。"
    
    return s

# ========== 主程序 ==========

print("Building era lookup...", file=sys.stderr)
conn = sqlite3.connect(DB_PATH)
era_lookup = build_era_lookup(conn)
conn.close()
print(f"  {len(era_lookup):,} year→era mappings", file=sys.stderr)

print("\nProcessing all CBDB entries...", file=sys.stderr)

files_data = {}
total_cbdb = 0
fixed_era = 0
fixed_prefix = 0
fixed_gen = 0

for fp in sorted(glob.glob(f'{PEOPLE_DIR}/*.json')):
    with open(fp, encoding='utf-8') as f:
        data = json.load(f)
    files_data[fp] = data
    
    for i, p in enumerate(data):
        if 'src-cbdb' not in p.get('sourceIds', []):
            continue
        total_cbdb += 1
        
        region_id = p.get('regionId', '')
        dynasty_name = REGION_SHORT.get(region_id, '历史')
        death_year = p.get('deathYear')
        old_summary = p.get('summary', '')
        
        new_summary = fix_summary(old_summary, dynasty_name, death_year, era_lookup, region_id)
        
        if new_summary != old_summary:
            files_data[fp][i]['summary'] = new_summary
            
            if '卒于' in old_summary and '卒于' in new_summary and old_summary != new_summary:
                fixed_era += 1
            if '时期' in old_summary and '时期' not in new_summary:
                fixed_prefix += 1
            if 'generated from' in old_summary:
                fixed_gen += 1

print(f"  Total CBDB: {total_cbdb:,}", file=sys.stderr)
print(f"  Era converted: {fixed_era:,}", file=sys.stderr)
print(f"  '时期'→'代': {fixed_prefix:,}", file=sys.stderr)
print(f"  'generated from' cleaned: {fixed_gen:,}", file=sys.stderr)

# Write back
print(f"\nWriting...", file=sys.stderr)
for fp, data in files_data.items():
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Done", file=sys.stderr)
