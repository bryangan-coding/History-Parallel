#!/usr/bin/env python3
"""
Import Spring & Autumn / Warring States figures from grand-timeline dataset.
Also includes 西周 figures to augment zhou-dynasty.

Source: https://github.com/LingDong-/grand-timeline
Data: Wikipedia-based, CC0 licensed.
Output: src/data/people/_springAutumnPeople.json
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

# Load grand-timeline data
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

print(f"// Source: {len(src_data):,} grand-timeline entries", file=sys.stderr)
print(f"// Existing: {len(existing_names):,} names", file=sys.stderr)

# Dynasty context descriptions
CONTEXT_ZH = {
    'spring-autumn': '春秋时期（前770—前476年）是周王室衰微后诸侯争霸的时代。齐桓公、晋文公、楚庄王等先后称霸，百家争鸣的思想萌芽在此时期孕育，是中国文化史上极为璀璨的篇章。',
    'warring-states': '战国时期（前475—前221年）是诸侯兼并、列国争雄的时代。齐、楚、燕、韩、赵、魏、秦七雄并立，变法图强，诸子百家思想大放异彩，最终由秦国统一天下。',
    'western-zhou': '西周（前1046—前771年）是周朝的前期，定都镐京（今西安）。周公制礼作乐，建立宗法制与分封制，奠定了中国礼乐文明的基础。',
}

CONTEXT_EN = {
    'spring-autumn': 'The Spring and Autumn period (770–476 BCE) was an era of hegemonic struggle after the Zhou royal decline. Rulers like Duke Huan of Qi and Duke Wen of Jin vied for supremacy, and the intellectual seeds of the Hundred Schools of Thought were sown.',
    'warring-states': 'The Warring States period (475–221 BCE) saw intense warfare among seven major states—Qi, Chu, Yan, Han, Zhao, Wei, and Qin—alongside a remarkable flourishing of philosophy and statecraft that culminated in Qin unification.',
    'western-zhou': 'The Western Zhou (1046–771 BCE) was the first half of the Zhou dynasty, with its capital at Haojing near modern Xi\'an. The Duke of Zhou established the ritual-music system and the feudal order that defined Chinese civilization.',
}

REGION_MAP = {
    'spring-autumn': 'spring-autumn-warring-states',
    'warring-states': 'spring-autumn-warring-states',
    'western-zhou': 'zhou-dynasty',
}

TAG_MAP = {
    'spring-autumn': '春秋',
    'warring-states': '战国',
    'western-zhou': '西周',
}

def classify(year):
    """Classify a BCE year into era."""
    if year is None:
        return None
    if year < -770:
        return 'western-zhou'
    elif -770 <= year <= -476:
        return 'spring-autumn'
    elif -475 <= year <= -221:
        return 'warring-states'
    return None

def parse_year(val):
    """Parse a year string from grand-timeline format."""
    if val in ('?', '不详', '', None):
        return None
    nums = re.findall(r'-?\d+', str(val))
    if not nums:
        return None
    year = int(nums[0])
    if '前' in str(val):
        return -abs(year)
    if '-' in str(val) and year > 0:
        return -year
    return year

entries = []
stats = {}
skipped_dup = 0
skipped_era = 0
skipped_non_bce = 0

for name, src in src_data.items():
    born_raw = src.get('born', '?')
    died_raw = src.get('died', '?')
    
    born = parse_year(born_raw)
    died = parse_year(died_raw)
    
    # ONLY classify by actual negative (BCE) year values.
    # Skip summary keyword matching — it catches Japanese Sengoku ("战国") false positives.
    # Also skip figures with positive (CE) years entirely.
    era = classify(died) or classify(born)
    if era is None:
        skipped_era += 1
        continue
    
    # Dedup
    name_simp = cc.convert(name)
    if name in existing_names or name_simp in existing_names_simp:
        skipped_dup += 1
        continue
    
    region = REGION_MAP[era]
    tag_display = TAG_MAP[era]
    stats[tag_display] = stats.get(tag_display, 0) + 1
    
    # Pinyin ID - use BCE year as negative for distinction
    pid = to_pinyin_id(name, abs(born or died or 0))
    base_pid = pid
    suffix = 1
    while pid in existing_ids:
        suffix += 1
        pid = f"{base_pid}-{suffix}"
    existing_ids.add(pid)
    
    # English name
    py = lazy_pinyin(name)
    name_en = ' '.join(py).title()
    
    # Year info
    if born and died:
        # BCE display
        year_info = f"前{abs(born)}—前{abs(died)}年"
        lived_info = f"生于前{abs(born)}年，卒于前{abs(died)}年"
        conf = 0.8
    elif died:
        year_info = f"?—前{abs(died)}年"
        lived_info = f"约卒于前{abs(died)}年"
        conf = 0.7
    elif born:
        year_info = f"约前{abs(born)}年"
        lived_info = f"约生于前{abs(born)}年"
        conf = 0.7
    else:
        year_info = "年代不详"
        lived_info = ""
        conf = 0.6
    
    context_zh = CONTEXT_ZH[era]
    context_en = CONTEXT_EN[era]
    
    summary_src = src.get('summary', '').strip()
    if len(summary_src) > 200:
        summary_src = summary_src[:197] + '...'
    
    if lived_info:
        summary_zh = f"{tag_display}时期人物，{lived_info}。{summary_src}"
    else:
        summary_zh = f"{tag_display}时期人物。{summary_src}"
    
    summary_en = f"Figure of the {tag_display} period. {summary_src[:100]}" if summary_src else f"Historical figure of the {tag_display} period."
    
    desc_zh = f'{name}（{year_info}），{tag_display}人物。{context_zh}{summary_src}'
    desc_en = f'{name} ({year_info}), a figure of the {tag_display} period. {context_en}'
    
    entry = {
        "id": pid,
        "name": name,
        "nameEn": name_en,
        "regionId": region,
        "occupations": ["历史人物"],
        "tags": [tag_display],
        "tagsEn": [tag_display],
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

out_path = 'src/data/people/_springAutumnPeople.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"\n✅ Written {len(entries):,} entries to {out_path}", file=sys.stderr)
print(f"   Skipped duplicates: {skipped_dup}", file=sys.stderr)
print(f"   Skipped wrong era: {skipped_era}", file=sys.stderr)
print(f"\n=== 分布 ===", file=sys.stderr)
for tag, cnt in sorted(stats.items(), key=lambda x: -x[1]):
    print(f"  {tag}: {cnt:,} 人", file=sys.stderr)
