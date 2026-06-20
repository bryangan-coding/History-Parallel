#!/usr/bin/env python3
"""
生成知名历史人物的真正大事件数据。
每个事件必须是特定历史时间点发生的特定事情，不是模板填充。
"""
import mysql.connector
import json
import re

conn = mysql.connector.connect(
    host='localhost', port=3307, user='root', password='',
    database='history_parallel', charset='utf8mb4',
    unix_socket='/tmp/mysql.sock'
)
cur = conn.cursor()

# ==================== 知名人物大事件库 ====================
# 格式: (person_name, event_title, start_year, end_year, summary, importance, source_ids, tags)
EVENTS_DATA = [
    # ===== 苏轼 (1037-1101) =====
    ("苏轼", "苏轼进士及第轰动京师",
     1057, None,
     "嘉祐二年（1057年），21岁的苏轼与19岁的弟弟苏辙同榜进士及第，轰动京师。主考官欧阳修读到苏轼文章时误以为是弟子曾巩所作，为避嫌将之列为第二。宋仁宗殿试后喜道：'朕今日为子孙得两宰相矣！'",
     5, ["src-ss"], ["进士", "科举", "欧阳修", "嘉祐"]),
     
    ("苏轼", "乌台诗案：苏轼入狱百日",
     1079, 1079,
     "元丰二年（1079年），御史李定、舒亶等人弹劾苏轼以诗文'讥切时政'，苏轼被捕入御史台狱（因院中遍植柏树，常有乌鸦栖息，故称'乌台'）。在狱中受审百余日，几乎丧命。太皇太后曹氏为其求情，王安石亦上书'安有圣世而杀才士乎？'最终贬为黄州团练副使。此案牵连司马光、黄庭坚等二十余人，是北宋最大的一场文字狱。",
     5, ["src-ss"], ["文字狱", "乌台诗案", "党争", "新法"]),
     
    ("苏轼", "苏轼贬谪黄州自号东坡居士",
     1080, 1080,
     "元丰三年（1080年），苏轼出狱后被贬为黄州团练副使，本州安置，不得签书公事。他在黄州城东的东坡上开荒种地，筑室而居，自号'东坡居士'。这四年是苏轼文学创作的高峰期，在逆境中完成了精神境界的蜕变。",
     4, ["src-ss"], ["贬谪", "黄州", "东坡居士"]),
     
    ("苏轼", "苏轼游赤壁作《赤壁赋》",
     1082, 1082,
     "元丰五年（1082年）七月十六日，苏轼与友人泛舟于黄州城外的赤鼻矶，醉后写下了千古名篇《前赤壁赋》。文中'寄蜉蝣于天地，渺沧海之一粟'的旷达胸襟，将宇宙人生的哲理与诗意的审美融为一体。同年十月重游，又作《后赤壁赋》，并留下'大江东去，浪淘尽，千古风流人物'的《念奴娇·赤壁怀古》。",
     5, ["src-ss"], ["赤壁赋", "文学", "黄州", "经典"]),
     
    ("苏轼", "苏轼知杭州筑苏堤",
     1089, 1091,
     "元祐四年（1089年），苏轼以龙图阁学士出知杭州。他发现西湖淤塞严重，遂发动二十万民工大规模疏浚西湖，将挖出的淤泥葑草堆筑成一条纵贯南北的长堤，并在堤上遍植桃柳芙蓉。后人称此堤为'苏堤'，'苏堤春晓'成为西湖十景之首。苏轼还修建了三座石塔作为标志，即后来的'三潭印月'。",
     4, ["src-ss"], ["杭州", "水利", "西湖", "苏堤"]),
     
    ("苏轼", "苏轼贬谪惠州再谪儋州",
     1094, 1097,
     "绍圣元年（1094年），哲宗亲政后新党重新上台，五十九岁的苏轼被贬至岭南惠州。他在惠州写下'日啖荔枝三百颗，不辞长作岭南人'。然而政敌并不罢休，三年后再将他贬到更偏远的海南儋州（今海南岛）。在儋州，时已六十二岁的苏轼开办学堂，传播中原文化，培养出海南历史上第一位举人姜唐佐。",
     4, ["src-ss"], ["贬谪", "惠州", "儋州", "岭南"]),

    # ===== 曹操 (155-220) =====
    ("曹操", "曹操举孝廉入仕",
     174, None,
     "熹平三年（174年），二十岁的曹操被举为孝廉，入京都洛阳为郎，不久被任命为洛阳北部尉。他到任后造五色棒悬于衙门，有犯禁者不避豪强皆棒杀之。权臣蹇硕的叔父违禁夜行，曹操毫不留情将其处死，一时京师敛迹。",
     4, ["src-shiji"], ["孝廉", "洛阳", "举荐"]),
     
    ("曹操", "曹操起兵讨伐董卓",
     190, None,
     "初平元年（190年），董卓废少帝立献帝，焚烧洛阳迁都长安。曹操散尽家财，招募义兵，首发檄文号召天下诸侯共讨董卓。虽然关东联军最终因各怀异心而解散，但曹操在此役中展现出超人的决断力与号召力，从此走上了争霸天下的道路。",
     5, ["src-shiji"], ["董卓", "讨董", "起兵", "关东联军"]),
     
    ("曹操", "曹操迎汉献帝都许",
     196, None,
     "建安元年（196年），曹操采纳谋士荀彧的建议，率军至洛阳迎接颠沛流离的汉献帝刘协，迁都于许县（今许昌）。从此'挟天子以令诸侯'，以朝廷名义号令天下，在政治上占据了绝对优势。曹操被任命为司空，行车骑将军事，总揽朝政。",
     5, ["src-shiji"], ["汉献帝", "许都", "挟天子"]),
     
    ("曹操", "官渡之战：曹操以少胜多",
     200, 200,
     "建安五年（200年），袁绍率精兵十万南下进攻曹操。曹操以不足两万的兵力在官渡（今河南中牟）与袁绍对峙。曹操采纳许攸之计，亲率五千精兵夜袭乌巢，焚烧袁军粮草辎重，袁军大乱溃败。此战曹操歼敌七万余人，奠定了统一北方的基础，是中国历史上最著名的以少胜多的战役之一。",
     5, ["src-shiji"], ["官渡之战", "袁绍", "以少胜多", "北方统一"]),
     
    ("曹操", "赤壁之战：曹操兵败北还",
     208, 208,
     "建安十三年（208年），曹操率大军二十余万南下，欲一举平定江南。孙权与刘备结盟，周瑜以火攻之策大破曹军于赤壁（今湖北赤壁市）。曹操被迫退守北方，从此奠定三国鼎立的格局。",
     5, ["src-shiji"], ["赤壁之战", "孙权", "刘备", "三国鼎立"]),

    # ===== 诸葛亮 (181-234) =====
    ("诸葛亮", "三顾茅庐：诸葛亮隆中对策",
     207, None,
     "建安十二年（207年），刘备经徐庶推荐，三次亲赴隆中（今湖北襄阳）拜访二十七岁的诸葛亮。第三次终于得见，诸葛亮在茅庐中为刘备分析了天下大势，提出'先取荆州为家，再取益州成鼎足之势，然后待天下有变，命一上将将荆州之兵以向宛洛，将军身率益州之众以出秦川'的战略蓝图，史称《隆中对》。",
     5, ["src-shiji"], ["三顾茅庐", "隆中对", "刘备"]),
     
    ("诸葛亮", "赤壁之战：诸葛亮出使东吴促成孙刘联盟",
     208, None,
     "建安十三年（208年），曹操大军南下，刘备危急。诸葛亮奉命出使东吴，在柴桑（今江西九江）舌战群儒，以'曹操虽托名汉相，实汉贼也'说服孙权下定决心与刘备结盟，共同抗曹。孙刘联盟的成立直接导致了赤壁之战的胜利。",
     4, ["src-shiji"], ["赤壁之战", "孙刘联盟", "舌战群儒"]),
     
    ("诸葛亮", "诸葛亮受托孤之重任辅佐刘禅",
     223, None,
     "章武三年（223年），刘备在夷陵之战大败后病危于白帝城，临终前托孤于诸葛亮，说道：'君才十倍曹丕，必能安国，终定大事。若嗣子可辅，辅之；如其不才，君可自取。'诸葛亮涕泣答道：'臣敢竭股肱之力，效忠贞之节，继之以死！'此后诸葛亮开府治事，事无巨细皆由己出，全权执掌蜀汉军政大权。",
     4, ["src-shiji"], ["托孤", "白帝城", "刘备", "刘禅"]),
     
    ("诸葛亮", "诸葛亮率军南征七擒孟获",
     225, 225,
     "建兴三年（225年），诸葛亮率军南征，平定南中（今云南、贵州、四川南部）的叛乱。他采用参军马谡'攻心为上'的策略，对南中首领孟获七擒七纵，最终使其心悦诚服归降。此役不仅稳定了蜀汉后方，还为北伐曹魏积累了南方资源。",
     4, ["src-shiji"], ["南征", "孟获", "攻心"]),
     
    ("诸葛亮", "诸葛亮上《出师表》北伐曹魏",
     227, 227,
     "建兴五年（227年），诸葛亮上《出师表》于后主刘禅，以'鞠躬尽瘁，死而后已'的决心率军北驻汉中准备北伐。文中'亲贤臣，远小人，此先汉所以兴隆也；亲小人，远贤臣，此后汉所以倾颓也'成为千古名言。此后五年，诸葛亮先后五次出兵北伐。",
     5, ["src-shiji"], ["出师表", "北伐", "鞠躬尽瘁"]),

    # ===== 李白 (701-762) =====
    ("李白", "李白辞亲远游仗剑出蜀",
     725, None,
     "开元十三年（725年），二十五岁的李白'仗剑去国，辞亲远游'，离开四川沿长江而下。他途经江陵、洞庭、庐山、金陵、扬州等地，一路结交名士、饮酒赋诗。在江陵遇到道教大师司马承祯，被赞'有仙风道骨，可与神游八极之表'，李白备受鼓舞写下《大鹏赋》自比大鹏。",
     4, ["src-jts"], ["出蜀", "远游", "司马承祯"]),
     
    ("李白", "李白奉诏入长安供奉翰林",
     742, 743,
     "天宝元年（742年），四十二岁的李白因玉真公主和贺知章的推荐，受唐玄宗李隆基召见入长安。玄宗降辇步迎，以七宝床赐食，亲手调羹。李白供奉翰林院，为玄宗起草诏书、陪侍宴游，传说曾令高力士脱靴、杨贵妃磨墨。然而两年后发现翰林供奉不过是文学侍从，与其政治理想相去甚远，最终被赐金放还。",
     5, ["src-jts"], ["长安", "唐玄宗", "翰林供奉", "力士脱靴"]),
     
    ("李白", "李白与杜甫洛阳相遇",
     744, 744,
     "天宝三载（744年），李白被赐金放还离开长安后，在洛阳与三十三岁的杜甫相遇。两人一见如故，同游梁宋（今河南开封、商丘一带），在汴州遇到高适，三人登吹台、游梁园，饮酒赋诗。闻一多称这次相遇是'青天里太阳和月亮走碰了头'，是文学史上最伟大的友谊之一。",
     4, ["src-jts"], ["杜甫", "洛阳", "相遇"]),
     
    ("李白", "李白流放夜郎遇赦",
     757, 759,
     "至德二载（757年），李白因参与永王李璘的幕府而获罪，被判长流夜郎（今贵州桐梓一带）。他从浔阳出发，沿长江西行，次年行至白帝城时朝廷因关中大旱宣布大赦。李白狂喜之下写下千古名篇《早发白帝城》：'朝辞白帝彩云间，千里江陵一日还。两岸猿声啼不住，轻舟已过万重山。'",
     4, ["src-jts"], ["流放", "夜郎", "白帝城", "大赦"]),

    # ===== 杜甫 (712-770) =====
    ("杜甫", "杜甫漫游吴越与齐鲁",
     735, 740,
     "开元二十三年（735年），二十四岁的杜甫首次远游江南吴越，徜徉于苏州、杭州、绍兴等地。五年后再游齐赵（今山东、河北一带），在泰山写下'会当凌绝顶，一览众山小'的《望岳》。这段漫游生涯开阔了杜甫的胸襟与视野，为后来的诗歌创作奠定了基础。",
     3, ["src-jts"], ["漫游", "吴越", "泰山"]),
     
    ("杜甫", "安史之乱中杜甫身陷长安",
     756, 756,
     "至德元载（756年），安史叛军攻陷长安，杜甫在投奔唐肃宗的途中被叛军俘虏押回长安。他亲眼目睹国破家亡的惨状，写下'国破山河在，城春草木深。感时花溅泪，恨别鸟惊心'的《春望》，其诗被誉为'诗史'，记录了战争给人民带来的深重苦难。",
     5, ["src-jts"], ["安史之乱", "长安", "春望", "诗史"]),
     
    ("杜甫", "杜甫避乱成都营建草堂",
     759, 760,
     "乾元二年（759年），杜甫弃官西行，携家入蜀，在好友严武等人的帮助下于成都浣花溪畔建草堂而居。这段相对安定的四年中，他写下《茅屋为秋风所破歌》《春夜喜雨》《蜀相》《登楼》等名篇。其中'安得广厦千万间，大庇天下寒士俱欢颜'展现了他悲天悯人的情怀。",
     4, ["src-jts"], ["成都", "草堂", "蜀中"]),
     
    ("杜甫", "杜甫漂泊荆湘客死舟中",
     768, 770,
     "大历三年（768年），杜甫离开四川顺江而下，辗转漂泊于湖北、湖南一带。大历五年（770年）冬，贫病交加的杜甫在由潭州往岳阳的一条小船上去世，终年五十九岁。他的绝笔诗《风疾舟中伏枕书怀》仍以'战血流依旧，军声动至今'忧国忧民，至死不忘天下苍生。",
     4, ["src-jts"], ["漂泊", "湘江", "逝世"]),
]

# ==================== 先删除这些知名人物的旧模板块事件 ====================
# 删除模板垃圾：早期创作、成年立世、成长岁月、垂暮之年、文风成熟、文坛影响、文学成就、诗歌创作、史料来源、诗歌成熟、与XX社会
names = ["苏轼", "曹操", "诸葛亮", "李白", "杜甫"]

for name in names:
    # Find person id
    cur.execute("SELECT id FROM people WHERE name = %s AND data_status = 'published'", (name,))
    rows = cur.fetchall()
    if not rows:
        print(f"NOT FOUND: {name}")
        continue
    pid = rows[0][0]
    
    # Delete junk events for this person (模板事件)
    cur.execute("""
        DELETE e FROM events e
        INNER JOIN event_persons ep ON e.id = ep.event_id
        WHERE ep.person_id = %s
        AND (
            e.title LIKE '%早期创作%'
            OR e.title LIKE '%成年立世%'
            OR e.title LIKE '%成长岁月%'
            OR e.title LIKE '%垂暮之年%'
            OR e.title LIKE '%文风成熟%'
            OR e.title LIKE '%文坛影响%'
            OR e.title LIKE '%文学成就%'
            OR e.title LIKE '%诗歌创作%'
            OR e.title LIKE '%史料来源%'
            OR e.title LIKE '%诗歌成熟%'
            OR e.title LIKE '%与%社会%'
        )
    """, (pid,))
    deleted = cur.rowcount
    if deleted > 0:
        print(f"{name}: deleted {deleted} junk events")
    
    # Also delete duplicate events (same title)
    cur.execute("""
        DELETE e1 FROM events e1
        INNER JOIN event_persons ep1 ON e1.id = ep1.event_id
        INNER JOIN (
            SELECT e2.title, MIN(e2.id) as keep_id
            FROM events e2
            INNER JOIN event_persons ep2 ON e2.id = ep2.event_id
            WHERE ep2.person_id = %s
            GROUP BY e2.title
            HAVING COUNT(*) > 1
        ) dup ON e1.title = dup.title AND e1.id != dup.keep_id
        WHERE ep1.person_id = %s
    """, (pid, pid))
    if cur.rowcount > 0:
        print(f"  also removed {cur.rowcount} duplicate events")

conn.commit()

# ==================== 插入新事件 ====================
inserted = 0
seq = 0
for name, title, start_year, end_year, summary, importance, source_ids, tags in EVENTS_DATA:
    cur.execute("SELECT id FROM people WHERE name = %s AND data_status = 'published'", (name,))
    rows = cur.fetchall()
    if not rows:
        print(f"SKIP (no person): {name}")
        continue
    pid = rows[0][0]
    
    event_id = f"evt-deep-{re.sub(r'[^a-z0-9]', '-', name.lower())}-{seq}"
    seq += 1
    
    # Check for existing event with same title for this person
    cur.execute("""
        SELECT e.id FROM events e
        INNER JOIN event_persons ep ON e.id = ep.event_id
        WHERE ep.person_id = %s AND e.title = %s
    """, (pid, title))
    if cur.fetchone():
        print(f"EXISTS: {name} - {title}")
        continue
    
    # Insert event
    cur.execute("""
        INSERT INTO events (id, title, start_year, end_year, summary, importance, source_ids, tags, data_status, confidence_score)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'published', 0.9)
    """, (event_id, title, start_year, end_year, summary, importance, json.dumps(source_ids), json.dumps(tags)))
    
    # Link to person
    cur.execute("INSERT IGNORE INTO event_persons (event_id, person_id) VALUES (%s, %s)", (event_id, pid))
    inserted += 1

conn.commit()
print(f"\nInserted {inserted} new high-quality events")

# ==================== Show result for these figures ====================
for name in names:
    cur.execute("SELECT id FROM people WHERE name = %s AND data_status = 'published'", (name,))
    rows = cur.fetchall()
    if not rows: continue
    pid = rows[0][0]
    cur.execute("""
        SELECT COUNT(*) FROM events e
        INNER JOIN event_persons ep ON e.id = ep.event_id
        WHERE ep.person_id = %s AND e.data_status = 'published'
    """, (pid,))
    count = cur.fetchone()[0]
    print(f"{name}: {count} total events after cleanup")

cur.close()
conn.close()
print("\nDone!")
