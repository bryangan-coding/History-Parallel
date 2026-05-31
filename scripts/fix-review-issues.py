#!/usr/bin/env python3
"""Fix issues found by code review: duplicate event IDs and wrong person ID references"""
import re

with open('src/data/mockData.ts', 'r') as f:
    content = f.read()

# ===== 1. Remove duplicate event entries =====
# These event IDs exist in BOTH the original 39 and the new 61
duplicates = ['evt-qin-unification', 'evt-norman-conquest', 'evt-marco-polo']

for eid in duplicates:
    # Find all occurrences of this event ID as a full entry
    # We need to find the second occurrence (the one in the new section) and remove it
    pattern = re.compile(
        r"(\n\n  // --- .+? ---\n  \{\n    id: '" + re.escape(eid) + r"',.+?\n  \},)",
        re.DOTALL
    )
    matches = list(pattern.finditer(content))
    if len(matches) >= 2:
        # Remove the second occurrence
        content = content[:matches[1].start()] + content[matches[1].end():]
        print(f"Removed duplicate: {eid}")

# ===== 2. Fix person ID references =====
person_id_map = {
    'abraham-lincoln': 'lincoln',
    'charles-darwin': 'darwin',
    'galileo-galilei': 'galileo',
    'george-washington': 'washington',
    'isaac-newton': 'newton',
    'johannes-gutenberg': 'gutenberg',
    'kublai-khan': 'khubilai-khan',
    'li-shimin': 'emperor-taizong',
    'nicolaus-copernicus': 'copernicus',  # doesn't exist, just remove
}

# For person IDs that don't exist in the people array, replace with empty or remove
nonexistent_ids = [
    'cao-cao', 'charles-martel', 'christopher-columbus', 'cleopatra',
    'hulegu', 'kalidasa', 'li-si', 'li-yuan', 'lin-zexu', 'liu-bang',
    'martin-luther', 'mehmed-ii', 'nicolaus-copernicus', 'oliver-cromwell',
    'raphael', 'zhang-qian'
]

# Apply the map (fix known-name mismatches)
for wrong, correct in person_id_map.items():
    if correct:  # If mapping exists
        content = content.replace(f"'{wrong}'", f"'{correct}'")
        print(f"Fixed: {wrong} → {correct}")
    else:
        # Remove reference entirely - replace ', wrong,' with just comma
        content = content.replace(f"'{wrong}'", "")
        content = content.replace("[, ", "[")  # Clean up empty arrays
        content = content.replace("[ ]", "[]")
        print(f"Removed: {wrong} (not in people array)")

# For IDs that don't exist in people, just empty them
for nid in nonexistent_ids:
    # Replace the ID in personIds arrays
    content = content.replace(f"'{nid}'", "")
    print(f"Removed: {nid}")

# Clean up: remove empty array entries that result in double commas or [ , ]
content = content.replace("[, ", "[")
content = content.replace(", ,", ",")
content = content.replace(",,", ",")
# Fix cases where removal left [, ' → [' 
content = re.sub(r'\[, ', '[', content)
content = re.sub(r', \]', ']', content)

with open('src/data/mockData.ts', 'w') as f:
    f.write(content)

print("\nDone! Run tsc --noEmit to verify.")
