#!/usr/bin/env python3
"""Mass generation from CBDB: auto-generate entries for top missing people.
Uses CBDB structured data + template-based descriptions for efficiency."""
import json, re, sys
from opencc import OpenCC
cc = OpenCC('t2s')  # traditional to simplified

def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")

# Load CBDB extraction
with open('/tmp/cbdb_extract.json') as f:
    data = json.load(f)

# Load existing names
with open('src/data/mockData.ts') as f:
    content = f.read()
# Get both name and nameEn fields to cross-check — people section only
# Extract just the people array to avoid matching region/event names
people_start = content.find('export const people')
events_start = content.find('export const events', people_start)
people_section = content[people_start:events_start]
our_ids = set(re.findall(r"\n\s+id: '([^']+)'", people_section))
our_names_cn = set(re.findall(r"name: '([^']+)'", people_section))

# Map dynasty to region
dyn_region = {'唐':'tang-dynasty','宋':'song-dynasty','元':'yuan-dynasty','明':'ming-dynasty','清':'qing-dynasty'}

# Filter: not in our system, unique names, prioritized by score
missing = data['missing_high_score']
seen = set()
candidates = []
for p in missing:
    n = p['name']
    # Skip if name too short (likely bad data)
    if len(n) < 2:
        continue
    n_simp = cc.convert(n)  # Convert to simplified for comparison
    if n not in seen and n not in our_names_cn and n_simp not in our_names_cn:
        seen.add(n)
        candidates.append(p)

candidates.sort(key=lambda x: x['score'], reverse=True)

# Take a batch with optional offset (for repeated runs)
import os
batch_size = int(os.environ.get('BATCH_SIZE', '200'))
batch_offset = int(os.environ.get('BATCH_OFFSET', '0'))
batch = candidates[batch_offset:batch_offset + batch_size]

print(f"// Auto-generated from CBDB extraction")
print(f"// {len(batch)} figures generated")
print()

# Find max existing cbdb ID to start counting from
max_cbdb = 0
for pid in our_ids:
    if pid.startswith('cbdb-'):
        try:
            num = int(pid.replace('cbdb-', '').split('-')[0])
            max_cbdb = max(max_cbdb, num)
        except:
            pass
count = max_cbdb  # Start from the highest existing cbdb ID
for p in batch:
    name = p['name']
    name_en = p.get('name_en', name)
    birth = p['birth'] or 'undefined'
    death = p['death'] or 'undefined'
    dyn = p['dynasty']
    region = dyn_region.get(dyn, 'china')
    score = p['score']
    offices = p['offices']
    assoc = p['assoc']
    is_female = p.get('female', False)
    
    # Generate ID
    pid = name.lower().replace(' ', '-').replace('（','').replace('）','')
    pid = re.sub(r'[^a-z-]', '', pid)
    # Fallback: if name-derived ID is empty (pure Chinese), use cbdb-NNN
    if not pid:
        pid = f'cbdb-{count+1}'
    # Ensure uniqueness by appending number if needed
    if pid in our_ids:
        pid = pid + '-2'
    our_ids.add(pid)
    
    # Tags
    tags = []
    tagsen = []
    if dyn in ['唐','宋','元','明','清']:
        tags.append(dyn); tagsen.append(dyn)
    if offices > 5:
        tags.append('政治家'); tagsen.append('Statesman')
    if assoc > 30:
        tags.append('文学家'); tagsen.append('Writer')
    if assoc > 80:
        tags.append('学者'); tagsen.append('Scholar')
    if is_female:
        tags.append('女性'); tagsen.append('Women')
    
    if not tags:
        tags = [dyn]; tagsen = [dyn]
    
    # Occupations
    occs = []
    if '政治家' in tags: occs.append('政治家')
    if '文学家' in tags: occs.append('文学家')
    if not occs: occs.append('学者')
    
    # Metrics-based summary
    if offices >= 20:
        career_zh = f"历任{offices}职"
        career_en = f"Served in {offices} official posts"
    elif offices >= 5:
        career_zh = f"曾任{offices}职"
        career_en = f"Held {offices} official positions"
    else:
        career_zh = "任职经历"
        career_en = "Official career"
    
    if assoc >= 200:
        network_zh = f"CBDB记录{assoc}条社交关联——社会网络的核心节点"
        network_en = f"CBDB records {assoc} social associations — a central network hub"
    elif assoc >= 50:
        network_zh = f"CBDB记录{assoc}条社交关联"
        network_en = f"CBDB records {assoc} social associations"
    else:
        network_zh = ""
        network_en = ""
    
    summary_zh = f"{dyn}人物。{career_zh}。{network_zh}".strip('。').strip() + '。'
    summary_en = f"{dyn} figure. {career_en}. {network_en}".strip('.').strip() + '.'
    
    # Brief description
    if dyn == '宋':
        period = "宋代"
        period_en = "Song dynasty"
    elif dyn == '唐':
        period = "唐代"
        period_en = "Tang dynasty"
    elif dyn == '元':
        period = "元代"
        period_en = "Yuan dynasty"
    elif dyn == '明':
        period = "明代"
        period_en = "Ming dynasty"
    elif dyn == '清':
        period = "清代"
        period_en = "Qing dynasty"
    else:
        period = f"{dyn}"
        period_en = f"{dyn} period"
    
    desc_zh = f"{name}是{period}重要人物。CBDB数据库记录了其{offices}次任职经历和{assoc}条社会关系——反映了他在当时政治和学术网络中的活跃参与。其生平详细记载于相关史料文献中。"
    desc_en = f"{name} was an important figure of the {period_en}. CBDB records {offices} office postings and {assoc} social associations — reflecting active engagement in the political and scholarly networks of the era. Detailed biographical information is preserved in relevant historical sources."
    
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
    confidenceScore: 0.75,
    externalReferences: [],
  }},""")

print(f"\n// Total: {count} auto-generated figures")
print(f"// Generated from CBDB extraction (cbdb_20260530.sqlite3)")
