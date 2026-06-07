#!/usr/bin/env python3
"""
用 grand-timeline (Wikipedia) 的丰富摘要替换 CBDB Tier 1 条目摘要
遇到 Wikipedia 与 CBDB 信息矛盾时，以 Wikipedia 为准
"""
import json, glob, sys, os
from opencc import OpenCC

SRC_PATH = '/tmp/people-ancient-china.json'
PEOPLE_DIR = '/Users/bryangan/Documents/Projects/历史平行线/src/data/people'

cc = OpenCC('s2t')

def build_gt_lookup():
    """构建 grand-timeline name → summary 查找表"""
    with open(SRC_PATH, encoding='utf-8') as f:
        gtl = json.load(f)
    
    lookup = {}  # simp_name → {summary, born, died}
    for name, entry in gtl.items():
        summary = entry.get('summary', '').strip()
        if len(summary) < 20:
            continue  # Skip too-short entries
        
        # Store by original name
        if name not in lookup:
            lookup[name] = {'summary': summary, 'born': entry.get('born'), 'died': entry.get('died')}
        
        # Also store simplified version
        name_simp = cc.convert(name)
        if name_simp != name and name_simp not in lookup:
            lookup[name_simp] = {'summary': summary, 'born': entry.get('born'), 'died': entry.get('died')}
    
    return lookup

print("Building GT lookup...", file=sys.stderr)
gt_lookup = build_gt_lookup()
print(f"  Lookup size: {len(gt_lookup):,} entries", file=sys.stderr)

# Process all JSON files
enriched_count = 0
files_modified = 0

for fp in sorted(glob.glob(f'{PEOPLE_DIR}/*.json')):
    with open(fp, encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    for p in data:
        if 'src-cbdb' not in p.get('sourceIds', []):
            continue
        if not p.get('birthYear') or not p.get('deathYear'):
            continue  # Tier 1 only
        
        name = p['name']
        
        # Try direct match
        gt = gt_lookup.get(name)
        # Try traditional match
        if not gt:
            trad = cc.convert(name)
            gt = gt_lookup.get(trad)
        
        if gt:
            gt_summary = gt['summary']
            old_summary = p.get('summary', '')
            
            # Only replace if GT summary is significantly longer/more informative
            if len(gt_summary) > len(old_summary) * 1.5 or len(gt_summary) > 80:
                p['summary'] = gt_summary
                
                # Add GT source if not already present
                if 'src-grand-timeline' not in p.get('sourceIds', []):
                    p['sourceIds'] = list(p['sourceIds']) + ['src-grand-timeline']
                
                modified = True
                enriched_count += 1
    
    if modified:
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        files_modified += 1

print(f"\n✅ Enriched {enriched_count:,} CBDB Tier 1 entries with Wikipedia summaries", file=sys.stderr)
print(f"   Modified {files_modified} files", file=sys.stderr)
