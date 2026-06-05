#!/usr/bin/env python3
"""Split _peoplePart2 into _peoplePart2 and _peoplePart3 when TS2590 occurs."""
import sys

def split_people_part(filepath, part_name, split_at):
    """Split a _peoplePartN array into two parts at split_at entries."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Find the part declaration
    decl = f'export const {part_name}: Person[] = ['
    start = content.index(decl)
    body_start = content.index('[', start) + 1
    
    # Navigate to find array end by counting braces at the top level
    # Strategy: count id: ' occurrences to find the split point
    pos = body_start
    entry_count = 0
    split_pos = None
    
    while pos < len(content):
        line = content[pos:pos+100]  # look ahead
        
        # Check for 'id: ' at start of an entry
        if content[pos:pos+8].strip() == 'id:':
            entry_count += 1
            if entry_count == split_at + 1:
                split_pos = pos - 4  # go back to newline before { 
                # walk back to find the newline before this entry
                while split_pos > body_start and content[split_pos] != '\n':
                    split_pos -= 1
                break
        
        pos += 1
    
    if split_pos is None:
        print(f"Error: Could not find split point (entry {split_at + 1})")
        sys.exit(1)
    
    # Now find the actual array end
    pos = body_start
    depth = 1
    while depth > 0 and pos < len(content):
        if content[pos] == '{':
            depth += 1
        elif content[pos] == '}':
            depth -= 1
        pos += 1
    
    while pos < len(content) and content[pos] != ']':
        pos += 1
    array_end = pos  # position of ]
    
    # Generate new part name
    new_name = part_name.replace('Part', 'Part')
    base_num = int(part_name.replace('_peoplePart', ''))
    new_name_3 = f'_peoplePart{base_num + 1}'
    
    # Ensure no duplicate
    if new_name_3 in content:
        # Rename existing parts
        # Find all existing parts
        import re
        all_parts = re.findall(r'_peoplePart(\d+)', content)
        max_num = max(int(p) for p in all_parts)
        new_name_3 = f'_peoplePart{max_num + 1}'
    
    # Build new content
    first_half = content[body_start:split_pos].rstrip()
    second_half = content[split_pos:array_end].strip()
    
    # Construct new content
    new_dec1 = f'export const {part_name}: Person[] = [\n{first_half}\n];'
    new_dec2 = f'export const {new_name_3}: Person[] = [\n{second_half}\n];'
    
    # Replace the old part
    old_part = content[start:array_end+1]
    new_parts = new_dec1 + '\n\n' + new_dec2
    
    new_content = content.replace(old_part, new_parts, 1)
    
    # Now update the `people` export to include the new part
    people_decl = 'export const people: Person[] = ['
    people_start = new_content.index(people_decl)
    people_end = new_content.index('];', people_start) + 2
    
    people_section = new_content[people_start:people_end]
    # Add the new part before ]; 
    if f'...{new_name_3}' not in people_section:
        people_section = people_section.replace('];', f'  ...{new_name_3},\n];')
        new_content = new_content[:people_start] + people_section + new_content[people_end:]
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    print(f"Split {part_name} at entry {split_at}")
    print(f"  → {part_name}: entries 0-{split_at-1}")
    print(f"  → {new_name_3}: entries {split_at}-end")
    
    # Count entries in new parts
    final_p1 = new_content.count(f'export const {part_name}')
    final_p2 = new_content.count(f'export const {new_name_3}')
    print(f"  Declarations: {part_name}={final_p1}, {new_name_3}={final_p2}")

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        split_at = int(sys.argv[2]) if len(sys.argv) > 2 else None
    else:
        print("Usage: split-people-part.py <mockData.ts> <split_at_entries>")
        sys.exit(1)
    
    # Find which part is too large
    import re
    with open(sys.argv[1]) as f:
        content = f.read()
    
    # Find all _peoplePart declarations and their entry counts
    parts = {}
    for m in re.finditer(r'export const (_peoplePart\d+): Person\[\] = \[', content):
        name = m.group(1)
        start = m.start()
        # Find next export or events
        next_decl = re.search(r'export const ', content[start+10:])
        end = start + 10 + next_decl.start() if next_decl else len(content)
        section = content[start:end]
        count = len(re.findall(r'^\s{4}id:\s*\'', section, re.MULTILINE))
        parts[name] = (count, start, end)
    
    print("Current parts:")
    total = 0
    for name, (count, _, _) in sorted(parts.items()):
        print(f"  {name}: {count} entries")
        total += count
    print(f"  Total: {total}")
    
    # Find the largest part
    largest = max(parts, key=lambda k: parts[k][0])
    size = parts[largest][0]
    print(f"\nSplitting {largest} ({size} entries) at {split_at}...")
    
    split_people_part(sys.argv[1], largest, split_at)
