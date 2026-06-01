#!/usr/bin/env python3
"""
Pipeline: Load existing people → append new people → generate events → verify
One-shot data expansion script.
"""
import re, sys, subprocess

def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'")

TARGET = 'src/data/mockData.ts'

# Step 0: Verify current state
with open(TARGET) as f:
    content = f.read()
people_count = len(re.findall(r"^\s+id: '[a-z]", content, re.MULTILINE))
event_count = len(re.findall(r"^\s+id: 'evt-", content, re.MULTILINE))
print(f"BEFORE: {people_count} people, {event_count} events")

# Step 1: Generate new people by running all batch scripts
batches = [
    'scripts/generate-people-batch5.py',
    'scripts/generate-people-batch6.py', 
    'scripts/generate-people-batch9.py',
]

all_new = []
for script in batches:
    try:
        result = subprocess.run(['/Users/bryangan/.workbuddy/binaries/python/versions/3.13.12/bin/python3', script],
                               capture_output=True, text=True, cwd='/Users/bryangan/Documents/Projects/历史平行线')
        all_new.append(result.stdout)
        # Parse count from stderr
        for line in result.stderr.split('\n'):
            if 'generated' in line.lower():
                print(f"  {script}: {line.strip()}")
    except Exception as e:
        print(f"  {script}: ERROR - {e}")

# Step 2: Insert new people into mockData.ts
combined = '\n'.join(all_new)
# Remove total lines
while '\n// Total:' in combined:
    pos = combined.rfind('\n// Total:')
    combined = combined[:pos]

new_people_count = combined.count("    id: '")

with open(TARGET) as f:
    lines = f.readlines()

# Find insertion point - before "// Total: 102 new people" or people array end
insert_pos = None
for i, line in enumerate(lines):
    if '// Total: 102 new people' in line or (line.strip() == '];' and i > 5000 and '// ==================== EVENTS' in ''.join(lines[i-3:i])):
        insert_pos = i
        break

if insert_pos:
    new_lines = lines[:insert_pos] + ['\n'] + [combined] + ['\n'] + lines[insert_pos:]
    with open(TARGET, 'w') as f:
        f.writelines(new_lines)
    print(f"Inserted {new_people_count} new people at line {insert_pos + 1}")
else:
    print("ERROR: Could not find insertion point")
    sys.exit(1)

# Step 3: Count now
with open(TARGET) as f:
    content = f.read()
people_count = len(re.findall(r"\n\s+id: '[a-z]", content))
print(f"AFTER PEOPLE: {people_count} people")

# Step 4: Run events generator
print("Generating events...")
result = subprocess.run(['/Users/bryangan/.workbuddy/binaries/python/versions/3.13.12/bin/python3', 
                        'scripts/generate-biographical-events.py'],
                       capture_output=True, text=True, cwd='/Users/bryangan/Documents/Projects/历史平行线')
events_content = result.stdout
for line in result.stderr.split('\n'):
    print(f"  {line.strip()}")

# Remove total line
if '\n// Total:' in events_content:
    events_content = events_content[:events_content.rfind('\n// Total:')]

new_event_count = events_content.count("    id: 'evt-")

# Step 5: Insert events before HELPERS
with open(TARGET) as f:
    content = f.read()
pos = content.rfind('];\n\n// ==================== HELPERS')
if pos > 0:
    content = content[:pos] + '\n' + events_content + '\n' + content[pos:]
    with open(TARGET, 'w') as f:
        f.write(content)
    print(f"Inserted {new_event_count} new events")
else:
    print("ERROR: Could not find HELPERS insertion point")

# Step 6: Final count
with open(TARGET) as f:
    content = f.read()
people_count = len(re.findall(r"\n\s+id: '[a-z]", content))
event_count = len(re.findall(r"\n\s+id: 'evt-", content))
print(f"\nFINAL: {people_count} people, {event_count} events")
