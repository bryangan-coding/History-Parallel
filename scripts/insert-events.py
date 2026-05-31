#!/usr/bin/env python3
"""Insert generated events into mockData.ts"""
with open('src/data/mockData.ts', 'r') as f:
    content = f.read()

with open('/tmp/new-events.ts', 'r') as f:
    new_events = f.read()

# Find the end of the last event and the closing ]; before HELPERS
# The pattern is the last event's externalReferences line + closing

# Simpler approach: find the ending pattern
end_pattern = "\n];\n\n// ==================== HELPERS"
insertion = new_events + end_pattern

if end_pattern in content:
    content = content.replace(end_pattern, insertion)
    with open('src/data/mockData.ts', 'w') as f:
        f.write(content)
    print('SUCCESS: Events inserted')
    print(f'New file size: {len(content)} chars')
    
    # Verify event count
    event_count = content.count("id: 'evt-")
    print(f'Total events in file: {event_count}')
else:
    print('ERROR: Could not find end_pattern')
    # Debug: find where ]; is
    import re
    matches = list(re.finditer(r'\n\];\n', content))
    print(f'Found {len(matches)} ]; patterns')
    for m in matches[-3:]:
        start = max(0, m.start() - 50)
        end = min(len(content), m.end() + 50)
        print(f'  Around position {m.start()}: ...{content[start:end]}...')
