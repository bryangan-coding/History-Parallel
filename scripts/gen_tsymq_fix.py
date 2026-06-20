#!/usr/bin/env python3
"""Fix: insert remaining events for 朱元璋, 朱棣, 王守仁"""
import mysql.connector, json

conn = mysql.connector.connect(
    host='localhost', port=3307, user='root', password='',
    database='history_parallel', charset='utf8mb4',
    unix_socket='/tmp/mysql.sock', autocommit=False
)
cur = conn.cursor()

EVENTS = [
    ("朱元璋", "朱元璋参加红巾军起义", 1352, None,
     "至正十二年（1352年），二十五岁的朱元璋因家乡濠州大旱和瘟疫走投无路，投奔郭子兴领导的红巾军。他作战勇敢，足智多谋，很快被郭子兴招为女婿。次年朱元璋回乡募兵，徐达、汤和等人应募相从，奠定了他日后建立大明的核心班底。",
     4, ["src-ss"], ["红巾军", "起义", "郭子兴"]),
    ("朱元璋", "朱元璋攻克集庆建立根据地", 1356, None,
     "至正十六年（1356年），朱元璋率军攻克集庆（今南京），改名应天府。他采纳朱升'高筑墙、广积粮、缓称王'的策略，在江南韬光养晦积蓄力量。此后数年，朱元璋先后消灭陈友谅、张士诚、方国珍等割据势力，逐步统一江南。",
     4, ["src-ss"], ["集庆", "应天府", "高筑墙"]),
    ("朱元璋", "朱元璋称帝建立明朝", 1368, None,
     "洪武元年（1368年）正月初四，朱元璋在应天府（南京）即皇帝位，国号大明，年号洪武。同年八月，徐达、常遇春率明军攻入大都，元顺帝北逃，元朝在中原的统治正式结束。朱元璋以贫苦农民出身终成一代开国皇帝。",
     5, ["src-ss"], ["洪武", "大明", "开国"]),
    ("朱棣", "靖难之役：朱棣夺位", 1399, 1402,
     "建文元年（1399年），燕王朱棣以'清君侧'为名在北平（今北京）起兵靖难。经过四年内战，建文四年（1402年）朱棣军队攻入南京应天府。宫中起火，建文帝朱允炆下落不明。朱棣即皇帝位，改元永乐，是为明成祖。",
     5, ["src-ss"], ["靖难之役", "永乐", "夺位"]),
    ("朱棣", "永乐帝迁都北京建紫禁城", 1406, 1420,
     "永乐四年（1406年），明成祖下诏以北京为都城，开始大规模营建北京城。十余万工匠、百万民夫历时十五年，建成了宏伟壮丽的紫禁城。永乐十九年（1421年）正式迁都北京。此后五百余年，紫禁城一直是明清两代的皇宫，直至今日成为故宫博物院。",
     5, ["src-ss"], ["迁都", "紫禁城", "北京"]),
    ("王守仁", "龙场悟道：王阳明创立心学", 1508, None,
     "正德三年（1508年），王阳明因触怒刘瑾被贬至贵州龙场驿。在蛮荒之地，他日夜端居澄坐，某夜忽然顿悟：'圣人之道，吾性自足，向之求理于事物者误也。'由此创立心学体系。龙场悟道成为中国文化思想史上一次决定性的转折。",
     5, ["src-ss"], ["龙场悟道", "心学", "知行合一"]),
    ("王守仁", "王阳明平定宁王之乱", 1519, None,
     "正德十四年（1519年），宁王朱宸濠在南昌举兵叛乱。王阳明仅用三十五天平定这场震惊朝野的叛乱——他一面虚张声势迷惑叛军，一面直捣南昌端其老巢，在鄱阳湖一战擒获朱宸濠。此战展现了王阳明卓越的军事才能。",
     5, ["src-ss"], ["平叛", "宁王", "军事"]),
]

cur.execute("SELECT COALESCE(MAX(CAST(SUBSTRING_INDEX(id,'-',-1) AS UNSIGNED)), 56) + 1 FROM events WHERE id LIKE 'evt-tsymq-%'")
seq = int(cur.fetchone()[0])

inserted = 0
for name, title, start_year, end_year, summary, importance, source_ids, tags in EVENTS:
    cur.execute("SELECT id FROM people WHERE name = %s AND data_status = 'published'", (name,))
    rows = cur.fetchall()
    if not rows:
        print(f"SKIP: {name}")
        continue
    pid = rows[0][0]
    cur.execute("SELECT COUNT(*) FROM events e INNER JOIN event_persons ep ON e.id=ep.event_id WHERE ep.person_id=%s AND e.title=%s", (pid, title))
    if cur.fetchone()[0] > 0:
        print(f"EXISTS: {name} - {title}")
        continue
    eid = f"evt-tsymq-{seq:04d}"
    seq += 1
    cur.execute("INSERT INTO events (id, title, start_year, end_year, summary, importance, source_ids, tags, data_status, confidence_score) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'published',0.95)",
        (eid, title, start_year, end_year, summary, importance, json.dumps(source_ids), json.dumps(tags)))
    cur.execute("INSERT INTO event_persons (event_id, person_id) VALUES (%s,%s)", (eid, pid))
    inserted += 1

conn.commit()
cur.execute("SELECT COUNT(*) FROM events WHERE data_status='published'")
total = cur.fetchone()[0]
print(f"Inserted {inserted}, total events: {total}")
cur.close()
conn.close()
