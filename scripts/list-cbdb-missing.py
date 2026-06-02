#!/usr/bin/env python3
"""Mass generation: top CBDB missing people to TypeScript entries.
Cross-references CBDB extraction with our existing data."""
import json, re, subprocess

# Load existing names
with open('src/data/mockData.ts') as f:
    content = f.read()
our_names = set()
for m in re.finditer(r"name: '([^']+)'", content):
    our_names.add(m.group(1))

# Load CBDB extraction
with open('/tmp/cbdb_extract.json') as f:
    data = json.load(f)

missing = data['missing_high_score']

# Get unique, not-in-our-system, top by score
seen = set()
candidates = []
for p in missing:
    n = p['name']
    if n not in seen and n not in our_names:
        seen.add(n)
        candidates.append(p)

# Take top 50
candidates.sort(key=lambda x: x['score'], reverse=True)
top = candidates[:50]

# Map dynasty to region
dyn_to_region = {'唐':'tang-dynasty','宋':'song-dynasty','元':'yuan-dynasty','明':'ming-dynasty','清':'qing-dynasty'}

# Manual descriptions for top candidates (for quality)
descriptions = {}

# We'll generate entries in batches to keep file manageable
# For this run, generate top 30 with descriptions
count = 0
for p in top:
    name = p['name']
    birth = p['birth'] or 0
    death = p['death'] or 0
    dyn = p['dynasty']
    region = dyn_to_region.get(dyn, 'china')
    pid = re.sub(r'[^a-z-]', '', name.lower().replace(' ','-'))[:40]
    
    # Tags based on score profile
    tags = []
    tagsen = []
    if p['offices'] > 10:
        tags.append('政治家'); tagsen.append('Statesman')
    if p['assoc'] > 100:
        tags.append('文学家'); tagsen.append('Writer')
    if p['assoc'] > 200:
        tags.append('学者'); tagsen.append('Scholar')
    tags.append(dyn); tagsen.append(dyn_to_region.get(dyn, dyn))
    
    print(f"{count+1:2d}. {name} ({birth}-{death}) {dyn} score={p['score']}")
    count += 1

print(f"\nTotal candidates: {len(top)}")
print(f"Top 5 missing: {[(p['name'], p['score']) for p in top[:5]]}")
