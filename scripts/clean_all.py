#!/usr/bin/env python3
"""全面清洗数据库模板垃圾"""
import mysql.connector, json, re, time

conn = mysql.connector.connect(
    host='localhost', port=3307, user='root', password='',
    database='history_parallel', charset='utf8mb4',
    unix_socket='/tmp/mysql.sock', autocommit=False
)
cur = conn.cursor()

print("Starting comprehensive cleanup...")

# ===== Phase 1: Delete all template garbage =====
deletions = [
    ("成年立世", "title LIKE '%成年立世%'"),
    ("史料来源", "title LIKE '%史料来源%'"),
    ("与XX社会", "title LIKE '%与%社会%'"),
    ("生活在XX时期", "summary REGEXP '生活在[A-Za-z\\\\u4e00-\\\\u9fff]+时期'"),
    ("早期创作", "title LIKE '%早期创作%'"),
    ("成长岁月", "title LIKE '%成长岁月%'"),
    ("垂暮之年", "title LIKE '%垂暮之年%'"),
    ("文风成熟", "title LIKE '%文风成熟%'"),
    ("文坛影响", "title LIKE '%文坛影响%'"),
    ("文学成就", "title LIKE '%文学成就%'"),
    ("文学风格", "title LIKE '%文学风格%'"),
    ("诗歌创作", "title LIKE '%诗歌创作%'"),
    ("诗歌成熟", "title LIKE '%诗歌成熟%'"),
    ("历史印记", "title LIKE '%历史印记%'"),
]

# Build a single composite DELETE for efficiency
conditions = []
for label, where in deletions:
    cur.execute(f"SELECT COUNT(*) as cnt FROM events WHERE data_status='published' AND ({where})")
    cnt = cur.fetchone()[0]
    if cnt > 0:
        print(f"  {label}: {cnt} 条")
        conditions.append(f"({where})")

if conditions:
    combined = " OR ".join(conditions)
    cur.execute(f"DELETE FROM events WHERE data_status='published' AND ({combined})")
    print(f"Phase 1: Deleted {cur.rowcount} template garbage events")
    conn.commit()
else:
    print("Phase 1: Nothing to delete")

# ===== Phase 2: Delete duplicate events (same person, same title) =====
cur.execute("""
    DELETE e1 FROM events e1
    INNER JOIN event_persons ep1 ON e1.id = ep1.event_id
    INNER JOIN (
        SELECT e2.title, ep2.person_id, MIN(e2.id) as keep_id
        FROM events e2
        INNER JOIN event_persons ep2 ON e2.id = ep2.event_id
        WHERE e2.data_status = 'published'
        GROUP BY e2.title, ep2.person_id
        HAVING COUNT(*) > 1
    ) dup ON e1.title = dup.title AND e1.id != dup.keep_id
    WHERE ep1.person_id = dup.person_id
""")
print(f"Phase 2: Deleted {cur.rowcount} duplicate events (same person same title)")
conn.commit()

# ===== Phase 3: Delete events with "XXXX于XXXX年出生。" template =====
# These are redundant with the already-existing detailed birth events
cur.execute("""
    DELETE e1 FROM events e1
    INNER JOIN (
        SELECT e1.id as del_id
        FROM events e1
        INNER JOIN event_persons ep1 ON e1.id = ep1.event_id
        WHERE e1.data_status = 'published'
        AND e1.title LIKE '%出生'
        AND e1.summary LIKE '%于%年出生%'
        AND LENGTH(e1.summary) < 30
    ) sub ON e1.id = sub.del_id
""")
print(f"Phase 3: Deleted {cur.rowcount} redundant birth events")

# ===== Stats after cleanup =====
cur.execute("SELECT COUNT(*) FROM events WHERE data_status='published'")
remaining = cur.fetchone()[0]
print(f"\nEvents remaining: {remaining}")
cur.execute("SELECT COUNT(*) FROM event_persons")
print(f"event_persons remaining: {cur.fetchone()[0]}")
cur.execute("SELECT COUNT(*) FROM people WHERE data_status='published'")
people = cur.fetchone()[0]
print(f"People: {people}")
print(f"Events per person: {remaining/people:.1f}")

# ===== Phase 4: Generate simple lifespan events for people missing birth/death =====
print("\nGenerating missing birth/death events...")
# People without any birth event
cur.execute("""
    SELECT p.id, p.name, p.birth_year, p.death_year
    FROM people p
    WHERE p.data_status = 'published'
    AND p.birth_year IS NOT NULL
    AND NOT EXISTS (
        SELECT 1 FROM event_persons ep
        INNER JOIN events e ON ep.event_id = e.id
        WHERE ep.person_id = p.id AND e.title LIKE '%出生%' AND e.data_status = 'published'
    )
    LIMIT 50000
""")
missing_birth = cur.fetchall()
birth_inserted = 0
for pid, name, by, dy in missing_birth:
    event_id = f"evt-birth-{pid}"
    try:
        cur.execute("INSERT INTO events (id, title, start_year, summary, importance, tags, data_status) VALUES (%s,%s,%s,%s,%s,%s,'published')",
            (event_id, f"{name}出生", by, f"{name}出生于公元{by}年。", 2, json.dumps(["出生"])))
        cur.execute("INSERT INTO event_persons (event_id, person_id) VALUES (%s,%s)", (event_id, pid))
        birth_inserted += 1
    except: pass
conn.commit()
print(f"  Generated {birth_inserted} missing birth events")

# People without any death event
cur.execute("""
    SELECT p.id, p.name, p.birth_year, p.death_year
    FROM people p
    WHERE p.data_status = 'published'
    AND p.death_year IS NOT NULL
    AND NOT EXISTS (
        SELECT 1 FROM event_persons ep
        INNER JOIN events e ON ep.event_id = e.id
        WHERE ep.person_id = p.id AND (e.title LIKE '%逝世%' OR e.title LIKE '%去世%') AND e.data_status = 'published'
    )
    LIMIT 50000
""")
missing_death = cur.fetchall()
death_inserted = 0
for pid, name, by, dy in missing_death:
    event_id = f"evt-death-{pid}"
    age = dy - by if by else None
    summary = f"{name}于公元{dy}年逝世" + (f"，享年{age}岁。" if age else "。")
    try:
        cur.execute("INSERT INTO events (id, title, start_year, summary, importance, tags, data_status) VALUES (%s,%s,%s,%s,%s,%s,'published')",
            (event_id, f"{name}逝世", dy, summary, 2, json.dumps(["逝世"])))
        cur.execute("INSERT INTO event_persons (event_id, person_id) VALUES (%s,%s)", (event_id, pid))
        death_inserted += 1
    except: pass
conn.commit()
print(f"  Generated {death_inserted} missing death events")

# ===== Final stats =====
cur.execute("SELECT COUNT(*) FROM events WHERE data_status='published'")
final_events = cur.fetchone()[0]

cur.execute("""
    SELECT 
        SUM(CASE WHEN sub.cnt <= 2 THEN 1 ELSE 0 END) as basic,
        SUM(CASE WHEN sub.cnt BETWEEN 3 AND 5 THEN 1 ELSE 0 END) as medium,
        SUM(CASE WHEN sub.cnt BETWEEN 6 AND 10 THEN 1 ELSE 0 END) as good,
        SUM(CASE WHEN sub.cnt > 10 THEN 1 ELSE 0 END) as rich
    FROM (
        SELECT p.id, COUNT(ep.event_id) as cnt
        FROM people p
        LEFT JOIN event_persons ep ON p.id = ep.person_id
        INNER JOIN events e ON ep.event_id = e.id AND e.data_status = 'published'
        WHERE p.data_status = 'published'
        GROUP BY p.id
    ) sub
""")
dist = cur.fetchone()
print(f"\n=== Cleanup Complete ===")
print(f"Total events: {final_events}")
print(f"Events/person: {final_events/people:.1f}")
print(f"≤2 events/person (basic): {dist[0]}")
print(f"3-5 events/person (medium): {dist[1]}")
print(f"6-10 events/person (good): {dist[2]}")
print(f">10 events/person (rich): {dist[3]}")

cur.close()
conn.close()
print("\nDone!")
