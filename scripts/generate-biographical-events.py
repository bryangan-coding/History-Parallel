#!/usr/bin/env python3
"""
Generate biographical events for ALL people in mockData.ts.
Block-based parsing: split by }, then extract fields per block.
Each person gets: birth + death + major achievement = 3 events.
"""
import re, sys

def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'")

with open('src/data/mockData.ts', 'r') as f:
    content = f.read()

start = content.find('export const people: Person[] = [')
events_hdr = content.find('// ==================== EVENTS', start)
end = content.rfind('];', start, events_hdr)
text = content[start:end]

# Extract fields by position - find all id: then extract surrounding fields
ids = [(m.start(), m.group(1)) for m in re.finditer(r"id:\s*'([^']+)'", text)]
people = []

for i, (pos, pid) in enumerate(ids):
    # Determine window: from this id to just before next id (or end)
    end_pos = ids[i+1][0] if i+1 < len(ids) else len(text)
    window = text[pos:end_pos]
    
    p = {'id': pid}
    m = re.search(r"name:\s*'([^']*)'", window)
    p['name'] = m.group(1) if m else "Unknown"
    m = re.search(r"nameEn:\s*'([^']*)'", window)
    p['nameEn'] = m.group(1) if m else "Unknown"
    m = re.search(r"birthYear:\s*(-?\d+)", window)
    p['birthYear'] = int(m.group(1)) if m else 0
    m = re.search(r"deathYear:\s*(-?\d+|undefined)", window)
    dy_val = m.group(1) if m else '0'
    p['deathYear'] = int(dy_val) if dy_val != 'undefined' and dy_val else 0
    m = re.search(r"regionId:\s*'([^']+)'", window)
    p['regionId'] = m.group(1) if m else "europe"
    m = re.search(r"summary:\s*'([^']*)'", window)
    p['summary'] = m.group(1) if m else ""
    m = re.search(r"summaryEn:\s*'([^']*)'", window)
    p['summaryEn'] = m.group(1) if m else ""
    m = re.search(r"description:\s*'([^']*)'", window)
    p['description'] = m.group(1) if m else p.get('summary', '')
    
    # Skip non-person entries (regions, sources have specific id patterns)
    if pid.startswith('src-') or pid in ('asia','africa','americas','europe','china','japan','india',
        'middle-east','mongol-empire','england','byzantine','roman-empire','song-dynasty',
        'tang-dynasty','ming-dynasty','seljuk','renaissance-europe'):
        continue
    people.append(p)

print(f"Parsed {len(people)} people", file=sys.stderr)

def yr_text(y):
    return f"公元前{abs(y)}年" if y < 0 else f"公元{y}年"

def yr_text_en(y):
    return f"{abs(y)} BCE" if y < 0 else f"{y} CE"

events = []
for p in people:
    pid = p['id']; name = p['name']; name_en = p['nameEn']
    by = p['birthYear']; dy = p['deathYear']; rid = p['regionId']
    summ = p['summary']; summ_en = p['summaryEn']
    desc = p['description']
    
    # 1) BIRTH
    events.append({
        "id": f"evt-{pid}-birth", "titleEn": f"Birth of {name_en}",
        "title": f"{name}出生",
        "startYear": by, "endYear": by,
        "regionId": rid, "placeName": "",
        "tags": ["人物", "出生"], "tagsEn": ["Biography", "Birth"],
        "summary": f"{name}于{yr_text(by)}出生。",
        "summaryEn": f"{name_en} was born in {yr_text_en(by)}.",
        "description": f"{name}于{yr_text(by)}出生。{summ}",
        "descriptionEn": f"{name_en} was born in {yr_text_en(by)}. {summ_en}",
        "personIds": [pid], "importance": 2,
        "datePrecision": "year", "isApproximate": False,
        "relatedEventIds": [],
    })
    
    # 2) DEATH
    if dy and dy > by:
        age = dy - by
        events.append({
            "id": f"evt-{pid}-death", "titleEn": f"Death of {name_en}",
            "title": f"{name}逝世",
            "startYear": dy, "endYear": dy,
            "regionId": rid, "placeName": "",
            "tags": ["人物", "逝世"], "tagsEn": ["Biography", "Death"],
            "summary": f"{name}于{yr_text(dy)}逝世，享年{age}岁。",
            "summaryEn": f"{name_en} died in {yr_text_en(dy)}, aged {age}.",
            "description": f"{name}在{yr_text(dy)}逝世。{summ}",
            "descriptionEn": f"{name_en} passed away in {yr_text_en(dy)}. {summ_en}",
            "personIds": [pid], "importance": 4,
        })
    
    # 3) MAJOR ACHIEVEMENT
    if dy > by + 5:
        mid = by + max((dy - by) // 3, 10)
    else:
        mid = by + 5
    first_sent = desc.split("。")[0][:60] if desc else summ[:60]
    events.append({
        "id": f"evt-{pid}-major", "titleEn": f"Major achievement of {name_en}",
        "title": f"{name}的重大成就",
        "startYear": mid, "endYear": mid,
        "regionId": rid, "placeName": "",
        "tags": ["人物", "成就"], "tagsEn": ["Biography", "Achievement"],
        "summary": f"{name}在{yr_text(mid)}前后{first_sent}",
        "summaryEn": f"Around {yr_text_en(mid)}, {name_en} achieved a major milestone.",
        "description": f"{name}一生中的重要成就时期。{first_sent}",
        "descriptionEn": f"A pivotal period in {name_en}'s life. {summ_en}",
        "personIds": [pid], "importance": 3,
        "datePrecision": "year", "isApproximate": False,
        "relatedEventIds": [],
    })

print(f"Generated {len(events)} events for {len(people)} people", file=sys.stderr)

# OUTPUT
lines = []
for e in events:
    l = []
    l.append("  // --- %s ---" % e["titleEn"][:60])
    l.append("  {")
    l.append("    id: '%s'," % esc(e["id"]))
    l.append("    title: '%s'," % esc(e["title"]))
    l.append("    titleEn: '%s'," % esc(e["titleEn"]))
    l.append("    startYear: %s," % e["startYear"])
    l.append("    endYear: %s," % e["endYear"])
    l.append("    regionId: '%s'," % e["regionId"])
    l.append("    coordinates: undefined,")
    l.append("    placeName: '%s'," % (e["placeName"] or ""))
    pids = ", ".join("'%s'" % esc(p) for p in e["personIds"])
    l.append("    personIds: [%s]," % pids)
    tags = ", ".join("'%s'" % esc(t) for t in e["tags"])
    l.append("    tags: [%s]," % tags)
    tagsEn = ", ".join("'%s'" % esc(t) for t in e["tagsEn"])
    l.append("    tagsEn: [%s]," % tagsEn)
    l.append("    summary: '%s'," % esc(e["summary"]))
    l.append("    summaryEn: '%s'," % esc(e["summaryEn"]))
    l.append("    description: '%s'," % esc(e["description"]))
    l.append("    descriptionEn: '%s'," % esc(e["descriptionEn"]))
    l.append("    sourceIds: [],")
    l.append("    importance: %s," % e["importance"])
    l.append("    datePrecision: 'year' as const,")
    l.append("    isApproximate: false,")
    l.append("    relatedEventIds: [],")
    l.append("    dataStatus: 'published' as const,")
    l.append("    confidenceScore: 0.9,")
    l.append("    externalReferences: [],")
    l.append("  },")
    lines.append("\n".join(l))

print("\n\n".join(lines))
print("\n// Total: %d new biographical events" % len(events))
