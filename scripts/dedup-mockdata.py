#!/usr/bin/env python3
"""
Deduplicate entries in mockData.ts by id.
Keeps the first occurrence of each id.
Preserves file structure exactly.
"""
import sys
import re

def deduplicate_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    # Find array boundaries by line number
    array_starts = {}
    array_ends = {}

    for i, line in enumerate(lines):
        if line.strip().startswith('export const regions:'):
            array_starts['regions'] = i
        elif line.strip().startswith('export const sources:'):
            array_starts['sources'] = i
        elif line.strip().startswith('export const people:'):
            array_starts['people'] = i
        elif line.strip().startswith('export const events:'):
            array_starts['events'] = i
        elif line.strip() == '];':
            # Assign to the most recent array start
            if array_starts and 'events' in array_starts and 'events' not in array_ends:
                array_ends['events'] = i
            elif array_starts and 'people' in array_starts and 'people' not in array_ends:
                array_ends['people'] = i
            elif array_starts and 'sources' in array_starts and 'sources' not in array_ends:
                array_ends['sources'] = i
            elif array_starts and 'regions' in array_starts and 'regions' not in array_ends:
                array_ends['regions'] = i

    print(f"Arrays found: {list(array_starts.keys())}")
    for name in array_starts:
        print(f"  {name}: lines {array_starts[name]+1} - {array_ends[name]+1}")

    # Process each array
    result_lines = []
    last_processed_line = 0

    for name in ['regions', 'sources', 'people', 'events']:
        if name not in array_starts:
            continue

        start_line = array_starts[name]
        end_line = array_ends[name]

        # Copy lines before this array (from last processed to array start)
        result_lines.extend(lines[last_processed_line:start_line + 1])

        # Process array body (between opening [ and closing ];)
        # The opening [ is on the same line as export const
        # Find entries in the body
        body_start = start_line + 1
        body_end = end_line

        seen_ids = set()
        in_entry = False
        entry_lines = []
        current_id = None
        skip_entry = False

        for i in range(body_start, body_end):
            line = lines[i]

            if not in_entry:
                if '{' in line:
                    in_entry = True
                    entry_lines = [line]
                    current_id = None
                    skip_entry = False

                    m = re.search(r"id:\s*'([^']+)'", line)
                    if m:
                        current_id = m.group(1)
                        if current_id in seen_ids:
                            skip_entry = True

                    # Check if single-line entry
                    if line.count('{') == line.count('}'):
                        if not skip_entry:
                            if current_id:
                                seen_ids.add(current_id)
                            result_lines.extend(entry_lines)
                        in_entry = False
                        entry_lines = []
                # else: skip blank lines between entries
            else:
                entry_lines.append(line)

                if current_id is None:
                    m = re.search(r"id:\s*'([^']+)'", line)
                    if m:
                        current_id = m.group(1)
                        if current_id in seen_ids:
                            skip_entry = True

                # Check if entry ends
                # An entry ends when we have matching braces
                # Count braces in accumulated entry
                entry_text = ''.join(entry_lines)
                if entry_text.count('{') == entry_text.count('}'):
                    if not skip_entry:
                        if current_id and current_id not in seen_ids:
                            seen_ids.add(current_id)
                            result_lines.extend(entry_lines)
                        elif current_id is None:
                            result_lines.extend(entry_lines)
                    in_entry = False
                    entry_lines = []
                    current_id = None
                    skip_entry = False

        # Add the closing ]; line
        result_lines.append(lines[end_line])

        last_processed_line = end_line + 1
        print(f"  {name}: kept {len(seen_ids)} unique entries")

    # Copy remaining lines after last array
    result_lines.extend(lines[last_processed_line:])

    with open(filepath, 'w') as f:
        f.writelines(result_lines)

    print("Deduplication complete.")

if __name__ == '__main__':
    filepath = sys.argv[1] if len(sys.argv) > 1 else 'src/data/mockData.ts'
    deduplicate_file(filepath)
