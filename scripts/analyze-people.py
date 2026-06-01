#!/usr/bin/env python3
"""Analyze current people distribution by region and era"""
import re, json

with open('src/data/mockData.ts', 'r') as f:
    content = f.read()

# Extract people array
match = re.search(r"export const people: Person\[\] = \[(.*?)\n\];", content, re.DOTALL)
if not match:
    print("Could not find people array")
    exit(1)

people_text = match.group(1)
# Parse each person entry
people = []
for m in re.finditer(r"\{[^}]*id: '([^']+)'[^}]*name: '([^']+)'[^}]*regionId: '([^']+)'[^}]*birthYear: (-?\d+)[^}]*deathYear: (-?\d+)[^}]*\}", people_text, re.DOTALL):
    people.append({
        'id': m.group(1),
        'name': m.group(2),
        'regionId': m.group(3),
        'birthYear': int(m.group(4)),
        'deathYear': int(m.group(5)),
    })

# Count by region
from collections import Counter
region_counts = Counter(p['regionId'] for p in people)
era_counts = Counter()

for p in people:
    by = p['birthYear']
    if by <= -500:
        era = 'Ancient (BCE >500)'
    elif by <= 0:
        era = 'Ancient (500-1 BCE)'
    elif by <= 500:
        era = 'Early CE (1-500)'
    elif by <= 1000:
        era = 'Medieval (501-1000)'
    elif by <= 1300:
        era = 'Medieval (1001-1300)'
    elif by <= 1500:
        era = 'Renaissance (1301-1500)'
    elif by <= 1700:
        era = 'Early Modern (1501-1700)'
    elif by <= 1800:
        era = '18th Century (1701-1800)'
    elif by <= 1900:
        era = '19th Century (1801-1900)'
    else:
        era = '20th Century (1901+)'
    era_counts[era] += 1

print(f"=== Total people: {len(people)} ===\n")
print("=== By Region ===")
for region, count in region_counts.most_common():
    print(f"  {region}: {count}")

print("\n=== By Era ===")
for era, count in sorted(era_counts.items()):
    print(f"  {era}: {count}")

# Count people per century for finer analysis
century_counts = Counter()
for p in people:
    century = (p['birthYear'] // 100) * 100
    if century < 0:
        century = -((-century + 99) // 100) * 100  # BCE centuries
    century_counts[str(century)] += 1

print("\n=== By Century ===")
for century in sorted(century_counts.keys(), key=lambda x: int(x)):
    label = f"{abs(int(century))} BCE" if int(century) < 0 else f"{century} CE"
    print(f"  {label}: {century_counts[century]}")
