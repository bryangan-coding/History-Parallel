#!/usr/bin/env python3
"""
Extract key historical figures from CBDB SQLite database.
Focus: people with Chinese names, known dates, and significant data.
Output: JSON summary for analysis + identify which figures we're missing.
"""
import sqlite3, json, sys

DB = '/tmp/cbdb_20260530.sqlite3'
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

# ===== STEP 1: Extract all people with Chinese names and known dates =====
print("=== Step 1: Extract people with Chinese names ===")
query = """
SELECT b.c_personid, b.c_name_chn, b.c_name, 
       b.c_birthyear, b.c_deathyear, b.c_female,
       d.c_dynasty_chn as dynasty_chn, d.c_dynasty as dynasty_en,
       b.c_index_year, b.c_notes, b.c_by_nh_year, b.c_dy_nh_year,
       b.c_death_age, b.c_surname_chn, b.c_mingzi_chn
FROM BIOG_MAIN b
JOIN DYNASTIES d ON b.c_dy = d.c_dy
WHERE b.c_name_chn IS NOT NULL AND b.c_name_chn != ''
  AND b.c_dy IN (6, 15, 18, 19, 20)  -- Tang, Song, Yuan, Ming, Qing
  AND (b.c_birthyear > 0 OR b.c_deathyear > 0)
ORDER BY b.c_personid
"""
people = [dict(r) for r in conn.execute(query)]
print(f"  Extracted: {len(people)} people with known dates in Tang-Song-Yuan-Ming-Qing")

# ===== STEP 2: Get office posting counts =====
print("=== Step 2: Get office data ===")
office_counts = {}
for r in conn.execute("""
    SELECT c_personid, COUNT(*) as cnt 
    FROM POSTED_TO_OFFICE_DATA 
    WHERE c_personid IS NOT NULL
    GROUP BY c_personid
"""):
    office_counts[r['c_personid']] = r['cnt']
print(f"  People with office postings: {len(office_counts)}")

# ===== STEP 3: Get association counts =====
print("=== Step 3: Get association data ===")
assoc_counts = {}
for r in conn.execute("""
    SELECT c_personid, COUNT(*) as cnt 
    FROM ASSOC_DATA 
    WHERE c_personid IS NOT NULL
    GROUP BY c_personid
"""):
    assoc_counts[r['c_personid']] = r['cnt']
print(f"  People with associations: {len(assoc_counts)}")

# ===== STEP 4: Get kinship counts =====
kin_counts = {}
for r in conn.execute("""
    SELECT c_personid, COUNT(*) as cnt 
    FROM KIN_DATA 
    WHERE c_personid IS NOT NULL
    GROUP BY c_personid
"""):
    kin_counts[r['c_personid']] = r['cnt']

# ===== STEP 5: Get biography address =====
addr_counts = {}
for r in conn.execute("""
    SELECT c_personid, COUNT(*) as cnt 
    FROM BIOG_ADDR_DATA 
    WHERE c_personid IS NOT NULL
    GROUP BY c_personid
"""):
    addr_counts[r['c_personid']] = r['cnt']

# ===== STEP 6: Compute significance score =====
print("=== Step 6: Compute significance scores ===")
for p in people:
    pid = p['c_personid']
    p['office_count'] = office_counts.get(pid, 0)
    p['assoc_count'] = assoc_counts.get(pid, 0)
    p['kin_count'] = kin_counts.get(pid, 0)
    p['addr_count'] = addr_counts.get(pid, 0)
    # Score = office + assoc + kinship counts. More data = more significant.
    p['score'] = p['office_count'] * 2 + p['assoc_count'] + p['kin_count']

# Sort by score descending
people.sort(key=lambda x: x['score'], reverse=True)

# ===== STEP 7: Print top people by dynasty =====
print("\n=== Top People by Dynasty ===")
for dynasty in ['唐', '宋', '元', '明', '清']:
    dp = [p for p in people if p['dynasty_chn'] == dynasty]
    print(f"\n{dynasty} ({len(dp)} people with dates):")
    for p in dp[:15]:
        name = p['c_name_chn'] or p['c_name'] or '?'
        birth = p['c_birthyear'] or '?'
        death = p['c_deathyear'] or '?'
        print(f"  {name} ({birth}-{death}) score={p['score']} offices={p['office_count']} assoc={p['assoc_count']}")

# ===== STEP 8: Compare with our existing people =====
print("\n=== Step 8: Cross-reference with our data ===")
# Extract our person names from mockData.ts
import re
with open('src/data/mockData.ts') as f:
    content = f.read()
our_names = set()
for m in re.finditer(r"name: '([^']+)'", content):
    our_names.add(m.group(1))
print(f"  Our project has {len(our_names)} unique names")

# Find high-scoring CBDB people NOT in our system
missing = []
for p in people:
    name = (p['c_name_chn'] or p['c_name'] or '').strip()
    if name and name not in our_names and p['score'] >= 3:
        missing.append(p)
missing.sort(key=lambda x: x['score'], reverse=True)

print(f"\n  High-scoring people NOT in our system: {len(missing)}")
print("\n=== Top missing people (by significance score) ===")
for p in missing[:50]:
    name = p['c_name_chn'] or p['c_name']
    birth = p['c_birthyear'] or '?'
    death = p['c_deathyear'] or '?'
    dyn = p['dynasty_chn']
    print(f"  {name} ({dyn}, {birth}-{death}) score={p['score']}")

# Save full extraction for later use
output = {
    'total_in_db': len(people),
    'dynasty_counts': {},
    'missing_high_score': [{
        'name': (p['c_name_chn'] or p['c_name'] or '').strip(),
        'name_en': (p['c_name'] or '').strip(),
        'birth': p['c_birthyear'],
        'death': p['c_deathyear'],
        'dynasty': p['dynasty_chn'],
        'score': p['score'],
        'offices': p['office_count'],
        'assoc': p['assoc_count'],
        'female': p['c_female'] > 0
    } for p in missing[:5000]]
}
for p in people:
    dyn = p['dynasty_chn']
    output['dynasty_counts'][dyn] = output['dynasty_counts'].get(dyn, 0) + 1

with open('/tmp/cbdb_extract.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
print(f"\nFull extraction saved to /tmp/cbdb_extract.json")
print(f"  High-scoring missing: {len(missing)} people (score >= 3)")
print(f"  Total in extract: {len(people)}")
print("Done!")
conn.close()
