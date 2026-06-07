#!/usr/bin/env python3
"""
Import Republic of China (民國) figures from grand-timeline dataset.
Filter: active 1912–1949 (died 1912+ OR born after 1870 with late death).

Source: https://github.com/LingDong-/grand-timeline (Wikipedia, CC0)
Output: src/data/people/_republicOfChinaPeople.json
"""

import json, re, sys, glob
from pypinyin import lazy_pinyin, Style
from opencc import OpenCC

cc = OpenCC('t2s')

def to_pinyin_id(name, birth):
    py = lazy_pinyin(name, style=Style.TONE3)
    py_clean = [re.sub(r'\d', '', p) for p in py]
    slug = '-'.join(py_clean).lower()
    slug = re.sub(r'[^a-z-]', '', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    if birth and birth > 0:
        return f"{slug}-{birth}"
    return slug

def parse_year(val):
    if val in ('?', '不详', '', None):
        return None
    nums = re.findall(r'\d+', str(val))
    if not nums:
        return None
    year = int(nums[0])
    if '前' in str(val):
        return -abs(year)
    return year

with open('/tmp/people-ancient-china.json') as f:
    src_data = json.load(f)

# Load existing names/IDs
existing_names = set()
existing_names_simp = set()
existing_ids = set()
for fp in glob.glob('src/data/people/*.json'):
    with open(fp) as f:
        for p in json.load(f):
            existing_names.add(p['name'])
            existing_names_simp.add(cc.convert(p['name']))
            existing_ids.add(p['id'])

print(f"// Source: {len(src_data):,} entries, Existing: {len(existing_names):,} names", file=sys.stderr)

CONTEXT_ZH = '中华民国（1912—1949年）是中国历史上承前启后的转型时期，经历了北洋政府、国民政府、抗日战争及国共内战等重大历史阶段，涌现出大批政治家、军事家、文学家、科学家和艺术家。'
CONTEXT_EN = 'The Republic of China (1912–1949) was a transitional period in Chinese history, encompassing the Beiyang Government, the Nationalist Government, the War of Resistance against Japan, and the Chinese Civil War, producing numerous statesmen, military leaders, writers, scientists, and artists.'

entries = []
stats = {'民国': 0, '晚清': 0}
skipped_dup = 0
skipped_era = 0
skipped_short = 0

for name, src in src_data.items():
    born_raw = src.get('born', '?')
    died_raw = src.get('died', '?')
    
    born = parse_year(born_raw)
    died = parse_year(died_raw)
    
    # Filter: active during Republic of China period (1912-1949)
    # Include if:
    #   - died between 1912-1960 (民国+ early PRC transition)
    #   - OR born 1870+ and died 1912+
    # Exclude: died before 1912 (pure 清代), born after 1950 (too recent)
    if died:
        if died < 1912:
            skipped_era += 1
            continue
        if died > 1960:
            # May be too recent. Check if born before 1920 (active in 民国)
            if born and born > 1930:
                skipped_era += 1
                continue
        # Active in 民国 if died 1912+
        period = '民国'
    elif born:
        if born < 1870 or born > 1949:
            skipped_era += 1
            continue
        period = '民国'
    else:
        skipped_era += 1
        continue
    
    if len(name) < 2:
        skipped_short += 1
        continue
    
    # Dedup
    name_simp = cc.convert(name)
    if name in existing_names or name_simp in existing_names_simp:
        skipped_dup += 1
        continue
    
    stats[period] = stats.get(period, 0) + 1
    
    # Pinyin ID
    pid = to_pinyin_id(name, born or died or 0)
    base_pid = pid
    suffix = 1
    while pid in existing_ids:
        suffix += 1
        pid = f"{base_pid}-{suffix}"
    existing_ids.add(pid)
    
    name_en = ' '.join(lazy_pinyin(name)).title()
    
    # Year info
    if born and died:
        year_info = f"{born}—{died}年"
        lived_info = f"生于{born}年，卒于{died}年"
        conf = 0.8
    elif died:
        year_info = f"?—{died}年"
        lived_info = f"卒于{died}年"
        conf = 0.7
    elif born:
        year_info = f"{born}年—?"
        lived_info = f"生于{born}年"
        conf = 0.7
    else:
        year_info = "年代不详"
        lived_info = ""
        conf = 0.6
    
    summary_src = src.get('summary', '').strip()
    if len(summary_src) > 250:
        summary_src = summary_src[:247] + '...'
    
    if lived_info:
        summary_zh = f"民国时期人物，{lived_info}。{summary_src}"
    else:
        summary_zh = f"民国时期人物。{summary_src}"
    
    summary_en = f"Figure of the Republic of China period. {summary_src[:100]}"
    
    desc_zh = f'{name}（{year_info}），民国人物。{CONTEXT_ZH}{summary_src}'
    desc_en = f'{name} ({year_info}), a figure of the Republican era. {CONTEXT_EN}'
    
    # Auto-detect occupations from summary
    occs = ['历史人物']
    if any(kw in summary_src for kw in ['政治', '官员', '总统', '总理', '部长', '省长', '县长', '议员', '外交']):
        occs.insert(0, '政治人物')
    if any(kw in summary_src for kw in ['军事', '将军', '司令', '军长', '师长', '旅长', '团长', '八路军', '新四军', '红军', '抗日']):
        occs.append('军事人物')
    if any(kw in summary_src for kw in ['文学', '作家', '诗人', '小说', '散文', '翻译']):
        occs.append('文学家')
    if any(kw in summary_src for kw in ['科学', '物理', '化学', '生物', '数学', '工程', '医学', '教授', '院士']):
        occs.append('科学家')
    if any(kw in summary_src for kw in ['教育', '校长', '教师', '创办', '大学', '学校']):
        occs.append('教育家')
    if any(kw in summary_src for kw in ['艺术', '画家', '书法', '音乐', '电影', '戏剧', '表演', '导演']):
        occs.append('艺术家')
    if any(kw in summary_src for kw in ['商业', '实业', '企业家', '公司', '银行', '商会']):
        occs.append('实业家')
    
    tags = ['民国']
    tags_en = ['Republic of China']
    for o in occs[1:]:
        if o == '政治人物': tags.append('政治人物'); tags_en.append('Political Figure')
        elif o == '军事人物': tags.append('军事人物'); tags_en.append('Military Figure')
        elif o == '文学家': tags.append('文学家'); tags_en.append('Writer')
        elif o == '科学家': tags.append('科学家'); tags_en.append('Scientist')
        elif o == '教育家': tags.append('教育家'); tags_en.append('Educator')
        elif o == '艺术家': tags.append('艺术家'); tags_en.append('Artist')
        elif o == '实业家': tags.append('实业家'); tags_en.append('Entrepreneur')
    
    entry = {
        "id": pid, "name": name, "nameEn": name_en,
        "regionId": "republic-of-china",
        "occupations": occs,
        "tags": tags, "tagsEn": tags_en,
        "summary": summary_zh[:500],
        "summaryEn": summary_en[:500],
        "description": desc_zh[:1000],
        "descriptionEn": desc_en[:1000],
        "alternativeNames": [],
        "sourceIds": ["src-grand-timeline"],
        "wikidataQid": "",
        "dataStatus": "published",
        "confidenceScore": conf,
        "externalReferences": [],
    }
    if born:
        entry["birthYear"] = born
    if died:
        entry["deathYear"] = died
    
    entries.append(entry)

out_path = 'src/data/people/_republicOfChinaPeople.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"\n✅ Written {len(entries):,} entries to {out_path}", file=sys.stderr)
print(f"   Skipped duplicates: {skipped_dup}", file=sys.stderr)
print(f"   Skipped wrong era: {skipped_era}", file=sys.stderr)
print(f"   Skipped too short: {skipped_short}", file=sys.stderr)
print(f"\n=== 分布 ===", file=sys.stderr)
for k, v in sorted(stats.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v:,} 人", file=sys.stderr)
