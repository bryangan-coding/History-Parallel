#!/usr/bin/env python3
"""Merge supplement data into mockData.ts."""
import re, subprocess, sys

TARGET = 'src/data/mockData.ts'
BASE = '/Users/bryangan/.workbuddy/binaries/python/versions/3.13.12/bin/python3'

with open(TARGET) as f:
    content = f.read()
before = len(re.findall(r"\n\s+id: '[a-z]", content))
print(f"BEFORE: {before} entries")

result = subprocess.run([BASE, 'scripts/generate-people-supplement.py'],
                       capture_output=True, text=True, cwd='/Users/bryangan/Documents/Projects/历史平行线')
new_data = result.stdout
if '\n// Total:' in new_data:
    new_data = new_data[:new_data.rfind('\n// Total:')]
n = new_data.count("    id: '")
print(f"Adding: {n} figures")

with open(TARGET) as f:
    lines = f.readlines()

in_people = False
for i, line in enumerate(lines):
    if "export const people: Person[] = [" in line:
        in_people = True
        continue
    if in_people and (line.strip() == '];' or line.strip().endswith('as Person[];')):
        people_close = i
        break

new_lines = lines[:people_close] + ['\n'] + [new_data] + ['\n'] + lines[people_close:]
with open(TARGET, 'w') as f:
    f.writelines(new_lines)

with open(TARGET) as f:
    content = f.read()
after = len(re.findall(r"\n\s+id: '[a-z]", content))
print(f"AFTER: {after} entries. Added {n}.")
