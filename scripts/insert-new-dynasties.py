#!/usr/bin/env python3
"""Insert new dynasty people data into mockData.ts"""
import sys

MOCKDATA = 'src/data/mockData.ts'
NEW_DATA = '/tmp/cbdb_new_dynasties_clean.ts'

with open(MOCKDATA, 'r') as f:
    content = f.read()

with open(NEW_DATA, 'r') as f:
    new_data = f.read()

# Remove the export header line (first line is comment, second is comment, third is comment, fourth is export)
# We want just the array body, starting from the first "{" 
# Find the export line and keep everything from there
lines = new_data.split('\n')
start_idx = None
for i, line in enumerate(lines):
    if line.startswith('export const _newDynastiesPeople'):
        start_idx = i
        break

if start_idx is None:
    print("ERROR: Could not find export line in new data", file=sys.stderr)
    sys.exit(1)

# Strip leading comments, keep from export line
new_data_clean = '\n'.join(lines[start_idx:])

# Insert before the people export
insert_marker = '\n\nexport const people: Person[] = [..._peoplePart1, ..._peoplePart2, ..._peoplePart3,'
new_content = content.replace(
    insert_marker,
    f'\n{new_data_clean}\n{insert_marker}'
)

# Update the people export to include the new array
old_people_export = 'export const people: Person[] = [..._peoplePart1, ..._peoplePart2, ..._peoplePart3,\n  ..._peoplePart4,\n];'
new_people_export = 'export const people: Person[] = [..._peoplePart1, ..._peoplePart2, ..._peoplePart3,\n  ..._peoplePart4,\n  ..._newDynastiesPeople,\n];'

if old_people_export not in new_content:
    print("ERROR: Could not find people export to update", file=sys.stderr)
    # Try to find it
    if new_people_export in new_content:
        print("People export already updated", file=sys.stderr)
    else:
        print("Using regex fallback...", file=sys.stderr)
        import re
        new_content = re.sub(
            r'export const people: Person\[\] = \[(.*?)\];',
            lambda m: 'export const people: Person[] = [' + m.group(1) + ',  ..._newDynastiesPeople,\n];',
            new_content,
            flags=re.DOTALL
        )
else:
    new_content = new_content.replace(old_people_export, new_people_export)

with open(MOCKDATA, 'w') as f:
    f.write(new_content)

print(f"Done! Inserted new data into {MOCKDATA}", file=sys.stderr)
print(f"New data lines: {len(lines)}", file=sys.stderr)
