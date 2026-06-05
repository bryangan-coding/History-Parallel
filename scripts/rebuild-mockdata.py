#!/usr/bin/env python3
"""Rebuild mockData.ts: replace inline people data with JSON file imports."""
import sys

TS_FILE = 'src/data/mockData.ts'
BACKUP_FILE = 'src/data/mockData.ts.json-split-backup'

# Read the file
print(f"Reading {TS_FILE}...")
with open(TS_FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f"  {len(lines):,} lines")

# Create backup
with open(BACKUP_FILE, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print(f"  Backup saved to {BACKUP_FILE}")

# Find key boundaries
imports_end = 0
regions_end = 0
people_comment_start = 0
people_start = 0
people_end = 0
events_start = 0

for i, line in enumerate(lines):
    if line.startswith('import type') and imports_end == 0:
        imports_end = i + 1
    if line.strip().startswith('export const regions:') and regions_end == 0:
        continue
    if i > 0 and lines[i-1].strip() == '];' and 'regions' in lines[i-2] if i >= 2 else '' and regions_end == 0:
        # Find the actual regions end
        pass

# Simpler approach: use the known line numbers
# Line 4: end of imports
# Line 711: end of sources array (];)
# Line 713-714: PEOPLE comment
# Line 617444: end of people combined (];)
# Line 617445: blank line
# Line 617446: events start

# Extract sections
# Section 1: imports (lines 0-3)
# Section 2: regions + sources (lines 4-711)
# Section 3: PEOPLE section replacement (was lines 712-617444)
# Section 4: events + rest (lines 617445-)

header = ''.join(lines[:4])  # import line
regions_sources = ''.join(lines[4:712])  # regions + sources
events_rest = ''.join(lines[617445:])  # events + helper functions

# Build the new PEOPLE section
people_section = '''
// ==================== PEOPLE ====================
// Data stored in JSON files to avoid TypeScript compilation overhead.
// See src/data/people/ for the individual partition files.

import _peoplePart1Data from './people/_peoplePart1.json';
import _peoplePart2Data from './people/_peoplePart2.json';
import _peoplePart3Data from './people/_peoplePart3.json';
import _peoplePart4Data from './people/_peoplePart4.json';
import _newDynastiesPeopleData from './people/_newDynastiesPeople.json';

export const _peoplePart1: Person[] = _peoplePart1Data as Person[];
export const _peoplePart2: Person[] = _peoplePart2Data as Person[];
export const _peoplePart3: Person[] = _peoplePart3Data as Person[];
export const _peoplePart4: Person[] = _peoplePart4Data as Person[];
export const _newDynastiesPeople: Person[] = _newDynastiesPeopleData as Person[];

export const people: Person[] = [
  ..._peoplePart1,
  ..._peoplePart2,
  ..._peoplePart3,
  ..._peoplePart4,
  ..._newDynastiesPeople,
];

'''

# Combine
new_content = header + regions_sources + people_section + events_rest

# Write
with open(TS_FILE, 'w', encoding='utf-8') as f:
    f.write(new_content)

new_lines = new_content.count('\n')
print(f"\nNew file: {new_lines:,} lines (was {len(lines):,})")
print(f"Size reduction: {len(''.join(lines)) - len(new_content):,} bytes ({(1 - len(new_content)/len(''.join(lines)))*100:.1f}%)")
print(f"\n✅ mockData.ts rebuilt with JSON imports")
