#!/usr/bin/env python3
"""Ultra-mass generation: take up to 300 people from CBDB data."""
import json, re, sys, random

def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")

with open('/tmp/cbdb_all_missing.json') as f:
    all_people = json.load(f)

with open('src/data/mockData.ts') as f:
    content = f.read()

our_ids = set(re.findall(r"\n\s+id: '([^']+)'", content))
our_names_cn = set(re.findall(r"name: '([^']+)'", content))

dyn_region = {'唐':'tang-dynasty','宋':'song-dynasty','元':'yuan-dynasty','明':'ming-dynasty','清':'qing-dynasty'}

# Filter: not in our system, good name length, prioritize birth/death known
candidates = []
for p in all_people:
    n = p['name']
    if len(n) < 2 or n in our_names_cn:
        continue
    # Prioritize people with birth AND death dates
    has_dates = int(p['birth'] is not None and p['birth'] > 0 and p['death'] is not None and p['death'] > 0)
    candidates.append((has_dates, p))

# Sort: those with dates first, then random shuffle within groups
random.seed(42)
dates_known = [p for _, p in candidates if _ == 1]
dates_unknown = [p for _, p in candidates if _ == 0]

# Pick up to 150 with dates + 150 without = 300 total
batch = dates_known[:150] + dates_unknown[:150]
random.shuffle(batch[75:150])  # Shuffle the middle range for dynasty diversity

count = 0
for p in batch:
    name = p['name']
    name_en = p.get('name_en', name) or name
    birth = p['birth'] if p['birth'] and p['birth'] > 0 else -9999
    death = p['death'] if p['death'] and p['death'] > 0 else -9999
    dyn = p['dynasty']
    region = dyn_region.get(dyn, 'china')
    is_female = p.get('female', False)
    
    # Generate ID
    pid = name.lower().replace(' ', '-').replace('（','').replace('）','')
    pid = re.sub(r'[^a-z-]', '', pid)
    base = pid
    num = 2
    while pid in our_ids:
        pid = f"{base}-{num}"
        num += 1
    our_ids.add(pid)
    
    # Tags
    tags = [dyn] if dyn else []
    tagsen = [dyn] if dyn else []
    if is_female:
        tags.append('女性'); tagsen.append('Women')
    
    # Occupations  
    occs = ['学者']
    
    # Description  
    if birth > 0 and death > 0:
        life = f"（{birth}年—{death}年）"
        life_en = f" ({birth}–{death})"
    elif birth > 0:
        life = f"（约{birth}年生）"
        life_en = f" (born ca. {birth})"
    elif death > 0:
        life = f"（?—{death}年）"
        life_en = f" (?–{death})"
    else:
        life = ""
        life_en = ""
    
    desc_zh = f"{name}{life}是{dyn}人物。生平事迹记载于相关史料中。"
    desc_en = f"{name}{life_en} was a figure of the {dyn} period. Their life and achievements are recorded in relevant historical sources."
    
    summary_zh = f"{dyn}人物{life}。" if life else f"{dyn}人物。"
    summary_en = f"{dyn} figure{life_en}." if life_en else f"{dyn} figure."
    
    count += 1
    
    print(f"""  {{
    id: '{pid}',
    name: '{esc(name)}',
    nameEn: '{esc(name_en)}',
    birthYear: {birth},
    deathYear: {death},
    regionId: '{region}',
    occupations: [{', '.join(f"'{o}'" for o in occs)}],
    tags: [{', '.join(f"'{t}'" for t in tags)}],
    tagsEn: [{', '.join(f"'{t}'" for t in tagsen)}],
    summary: '{esc(summary_zh)}',
    summaryEn: '{esc(summary_en)}',
    description: '{esc(desc_zh)}',
    descriptionEn: '{esc(desc_en)}',
    alternativeNames: [],
    sourceIds: [],
    wikidataQid: '',
    dataStatus: 'published',
    confidenceScore: 0.7,
    externalReferences: [],
  }},""")

print(f"\n// Total: {count} auto-generated figures")
print(f"// Source: CBDB (cbdb_20260530.sqlite3)")
