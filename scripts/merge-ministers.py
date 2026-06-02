#!/usr/bin/env python3
"""Merge ministers/literati/scientists/strategists data into mockData.ts."""
import re, subprocess, sys

TARGET = 'src/data/mockData.ts'
BASE = '/Users/bryangan/.workbuddy/binaries/python/versions/3.13.12/bin/python3'

# Count before
with open(TARGET) as f:
    content = f.read()
people_before = len(re.findall(r"\n\s+id: '[a-z]", content))
print(f"BEFORE: {people_before} total entries")

# Generate new people
result = subprocess.run([BASE, 'scripts/generate-people-ministers.py'],
                       capture_output=True, text=True, cwd='/Users/bryangan/Documents/Projects/历史平行线')
new_people = result.stdout
if '\n// Total:' in new_people:
    new_people = new_people[:new_people.rfind('\n// Total:')]
new_count = new_people.count("    id: '")
print(f"Generating: {new_count} new figures")

# Read file
with open(TARGET) as f:
    lines = f.readlines()

# Find closing ]; of people array
people_close = None
in_people = False
for i, line in enumerate(lines):
    if "export const people: Person[] = [" in line:
        in_people = True
        continue
    if in_people and (line.strip() == '];' or line.strip().endswith('as Person[];')):
        people_close = i
        break

if not people_close:
    print("ERROR: Could not find people array close")
    sys.exit(1)

# Insert
new_lines = lines[:people_close] + ['\n'] + [new_people] + ['\n'] + lines[people_close:]
with open(TARGET, 'w') as f:
    f.writelines(new_lines)

# Verify
with open(TARGET) as f:
    content = f.read()
people_after = len(re.findall(r"\n\s+id: '[a-z]", content))
print(f"AFTER: {people_after} total entries")
print(f"Added: {new_count} new figures")
print("Done! Run 'tsc --noEmit' to verify.")
