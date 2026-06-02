#!/usr/bin/env python3
"""Merge new rulers, regions, and sources into mockData.ts."""
import re, subprocess, sys

TARGET = 'src/data/mockData.ts'
BASE = '/Users/bryangan/.workbuddy/binaries/python/versions/3.13.12/bin/python3'

# Count before
with open(TARGET) as f:
    content = f.read()
people_before = len(re.findall(r"\n\s+id: '[a-z]", content))
print(f"BEFORE: {people_before} people (approx)")

# Step 1: Insert new regions before regions array closing
print("Step 1: Inserting new regions...")
result = subprocess.run([BASE, 'scripts/generate-rulers-regions.py'],
                       capture_output=True, text=True, cwd='/Users/bryangan/Documents/Projects/历史平行线')
new_regions = result.stdout

with open(TARGET) as f:
    lines = f.readlines()

# Find the closing ]; of regions array
regions_close = None
in_regions = False
brace_count = 0
for i, line in enumerate(lines):
    if "export const regions: Region[] = [" in line:
        in_regions = True
        continue
    if in_regions and (line.strip() == '];' or line.strip().endswith('as Person[];')):
        regions_close = i
        break

if regions_close:
    new_lines = lines[:regions_close] + ['\n'] + [new_regions] + ['\n'] + lines[regions_close:]
    with open(TARGET, 'w') as f:
        f.writelines(new_lines)
    print(f"  Inserted new regions at line {regions_close + 1}")
else:
    print("ERROR: Could not find regions array close")
    sys.exit(1)

# Step 2: Insert new sources before sources array closing
print("Step 2: Inserting new sources...")
result = subprocess.run([BASE, 'scripts/generate-rulers-sources.py'],
                       capture_output=True, text=True, cwd='/Users/bryangan/Documents/Projects/历史平行线')
new_sources = result.stdout

with open(TARGET) as f:
    lines = f.readlines()

sources_close = None
in_sources = False
for i, line in enumerate(lines):
    if "export const sources: Source[] = [" in line:
        in_sources = True
        continue
    if in_sources and (line.strip() == '];' or line.strip().endswith('as Person[];')):
        sources_close = i
        break

if sources_close:
    new_lines = lines[:sources_close] + ['\n'] + [new_sources] + ['\n'] + lines[sources_close:]
    with open(TARGET, 'w') as f:
        f.writelines(new_lines)
    print(f"  Inserted new sources at line {sources_close + 1}")
else:
    print("ERROR: Could not find sources array close")
    sys.exit(1)

# Step 3: Insert Chinese emperors before people array closing
print("Step 3: Inserting Chinese emperors...")
result = subprocess.run([BASE, 'scripts/generate-rulers-china.py'],
                       capture_output=True, text=True, cwd='/Users/bryangan/Documents/Projects/历史平行线')
china_people = result.stdout
# Remove "// Total:" line
if '\n// Total:' in china_people:
    china_people = china_people[:china_people.rfind('\n// Total:')]
china_count = china_people.count("    id: '")
print(f"  {china_count} Chinese emperors")

with open(TARGET) as f:
    lines = f.readlines()

people_close = None
in_people = False
for i, line in enumerate(lines):
    if "export const people: Person[] = [" in line:
        in_people = True
        continue
    if in_people and (line.strip() == '];' or line.strip().endswith('as Person[];')):
        people_close = i
        break

if people_close:
    new_lines = lines[:people_close] + ['\n'] + [china_people] + ['\n'] + lines[people_close:]
    with open(TARGET, 'w') as f:
        f.writelines(new_lines)
    print(f"  Inserted Chinese emperors at line {people_close + 1}")
else:
    print("ERROR: Could not find people array close")
    sys.exit(1)

# Step 4: Insert global rulers before people array closing  
print("Step 4: Inserting global rulers...")
result = subprocess.run([BASE, 'scripts/generate-rulers-global.py'],
                       capture_output=True, text=True, cwd='/Users/bryangan/Documents/Projects/历史平行线')
global_people = result.stdout
if '\n// Total:' in global_people:
    global_people = global_people[:global_people.rfind('\n// Total:')]
global_count = global_people.count("    id: '")
print(f"  {global_count} global rulers")

with open(TARGET) as f:
    lines = f.readlines()

people_close = None
in_people = False
for i, line in enumerate(lines):
    if "export const people: Person[] = [" in line:
        in_people = True
        continue
    if in_people and (line.strip() == '];' or line.strip().endswith('as Person[];')):
        people_close = i
        break

if people_close:
    new_lines = lines[:people_close] + ['\n'] + [global_people] + ['\n'] + lines[people_close:]
    with open(TARGET, 'w') as f:
        f.writelines(new_lines)
    print(f"  Inserted global rulers at line {people_close + 1}")
else:
    print("ERROR: Could not find people array close")
    sys.exit(1)

# Step 5: Final count
with open(TARGET) as f:
    content = f.read()
people_after = len(re.findall(r"\n\s+id: '[a-z]", content))
total = china_count + global_count
print(f"\nFINAL: {people_after} total entries (approximately)")
print(f"Added: {total} new rulers ({china_count} Chinese + {global_count} global)")
print("Done! Run 'tsc --noEmit' to verify.")
