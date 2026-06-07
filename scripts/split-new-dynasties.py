#!/usr/bin/env python3
"""Split _newDynastiesPeople into smaller parts and update mockData.ts"""
import re

MOCKDATA = 'src/data/mockData.ts'
CHUNK_SIZE = 1000  # entries per part

with open(MOCKDATA, 'r') as f:
    content = f.read()

# Extract the _newDynastiesPeople array
start = content.find('export const _newDynastiesPeople: Person[] = [')
end = content.find('\n];', start) + 3  # include ];

if start == -1:
    print("ERROR: _newDynastiesPeople not found")
    exit(1)

# Get the array content (between [ and ])
array_start = content.index('[', start) + 1
array_end = content.rindex(']', start, end)

# Split into individual entries
# Each entry starts with "  {" and ends with "  },"
entries_text = content[array_start:array_end].strip()

# Find individual entries by matching { ... },
entries = []
depth = 0
current = []
lines = entries_text.split('\n')
for line in lines:
    current.append(line)
    # Count braces
    for ch in line:
        if ch == '{': depth += 1
        elif ch == '}': depth -= 1
    if depth == 0 and current:
        entries.append('\n'.join(current))
        current = []
        depth = 0

print(f"Found {len(entries)} entries")

# Count how many entries per source to verify
src_counts = {}
for e in entries:
    m = re.search(r"sourceIds:\s*\[([^\]]+)\]", e)
    if m:
        src = m.group(1).strip()
        src_counts[src] = src_counts.get(src, 0) + 1
print(f"Source counts: {src_counts}")

# Split into chunks
chunks = []
for i in range(0, len(entries), CHUNK_SIZE):
    chunk = entries[i:i+CHUNK_SIZE]
    chunks.append(chunk)

print(f"Split into {len(chunks)} chunks")

# Generate replacement
parts = []
part_names = []
for idx, chunk in enumerate(chunks):
    part_name = f'_newDynastiesPart{idx+1}'
    part_names.append(part_name)
    parts.append(f"export const {part_name}: Person[] = [\n{',\n'.join(chunk)},\n];")

new_data_block = '\n\n'.join(parts)

# Replace the old _newDynastiesPeople with new parts
# Remove old block
before = content[:start]
after = content[end:]

# Also fix the people export: remove _newDynastiesPeople and add the new parts
people_export_old = 'export const people: Person[] = [..._peoplePart1, ..._peoplePart2, ..._peoplePart3,\n  ..._peoplePart4,\n  ..._newDynastiesPeople,\n];'

new_parts_spread = ',\n  '.join(['...' + pn for pn in part_names])
people_export_new = f'export const people: Person[] = [..._peoplePart1, ..._peoplePart2, ..._peoplePart3,\n  ..._peoplePart4,\n  {new_parts_spread},\n];'

after = after.replace(people_export_old, people_export_new)

new_content = before + new_data_block + '\n\n' + after

with open(MOCKDATA, 'w') as f:
    f.write(new_content)

print(f"Done! Split into {len(chunks)} parts: {part_names}")
