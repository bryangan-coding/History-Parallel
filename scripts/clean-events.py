#!/usr/bin/env python3
"""Remove duplicates from generated events and fix person ID references"""
import re

# Read generated events
with open('/tmp/new-events.ts', 'r') as f:
    text = f.read()

# Remove duplicate event blocks
for eid in ['evt-qin-unification', 'evt-norman-conquest', 'evt-marco-polo']:
    pattern = r'\n\n  // --- .+? ---\n  \{\n    id: .' + re.escape(eid) + r"'.+?\n  \},"
    text = re.sub(pattern, '', text, count=1, flags=re.DOTALL)
    print(f'Removed duplicate: {eid}')

# Fix person ID references (known name mismatches)
mappings = {
    "'abraham-lincoln'": "'lincoln'",
    "'charles-darwin'": "'darwin'",
    "'galileo-galilei'": "'galileo'",
    "'george-washington'": "'washington'",
    "'isaac-newton'": "'newton'",
    "'johannes-gutenberg'": "'gutenberg'",
    "'kublai-khan'": "'khubilai-khan'",
    "'li-shimin'": "'emperor-taizong'",
}
for wrong, correct in mappings.items():
    count = text.count(wrong)
    if count > 0:
        text = text.replace(wrong, correct)
        print(f'Fixed: {wrong} -> {correct} ({count}x)')

# Remove references to IDs not in people array
nids = [
    "'cao-cao'", "'charles-martel'", "'christopher-columbus'", "'cleopatra'",
    "'hulegu'", "'kalidasa'", "'li-si'", "'li-yuan'", "'lin-zexu'",
    "'liu-bang'", "'martin-luther'", "'mehmed-ii'", "'nicolaus-copernicus'",
    "'oliver-cromwell'", "'raphael'", "'zhang-qian'"
]
for nid in nids:
    count = text.count(nid)
    if count > 0:
        text = text.replace(nid, '')
        print(f'Removed: {nid} ({count}x)')

# Clean up array syntax
text = text.replace('[, ', '[')
text = text.replace(', ,', ',')
text = text.replace(' ,]', ']')
text = text.replace('[,]', '[]')
text = re.sub(r'\[\s*,', '[', text)
text = re.sub(r',\s*\]', ']', text)

with open('/tmp/new-events-clean.ts', 'w') as f:
    f.write(text)

count = text.count("id: 'evt-")
print(f'Clean events: {count} (expected: 58)')
