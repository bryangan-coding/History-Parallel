#!/usr/bin/env python3
"""
P3: Fill missing descriptions by copying substantive summaries
Entries with summaries > 30 chars get description = summary
"""
import json, glob, sys

PEOPLE_DIR = '/Users/bryangan/Documents/Projects/历史平行线/src/data/people'
MIN_LENGTH = 30  # Only copy if summary is substantive

files_data = {}
total_processed = 0
copied = 0
skipped_short = 0

for fp in sorted(glob.glob(f'{PEOPLE_DIR}/*.json')):
    with open(fp, encoding='utf-8') as f:
        data = json.load(f)
    files_data[fp] = data
    
    for p in data:
        summary = (p.get('summary') or '').strip()
        desc = (p.get('description') or '').strip()
        
        if desc:  # Already has description
            continue
        if not summary:
            continue
        
        total_processed += 1
        
        if len(summary) >= MIN_LENGTH:
            p['description'] = summary
            copied += 1
        else:
            skipped_short += 1

# Write back
print(f"Entries without description: {total_processed:,}", file=sys.stderr)
print(f"  Copied summary→description: {copied:,} (summary ≥ {MIN_LENGTH} chars)", file=sys.stderr)
print(f"  Skipped (summary too short): {skipped_short:,}", file=sys.stderr)

for fp, data in files_data.items():
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Done", file=sys.stderr)
