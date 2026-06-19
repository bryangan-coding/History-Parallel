#!/usr/bin/env python3
"""为重要人物（嵇康、司马昭、王重阳、慕容垂等）补深度事件，基于正史来源"""
import mysql.connector, json

conn = mysql.connector.connect(user='root', password='', host='localhost', port=3307,
    database='history_parallel', charset='utf8mb4', unix_socket='/tmp/mysql.sock', autocommit=False)
cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT id FROM events")
existing_ids = {r['id'] for r in cursor.fetchall()}

INSERT_SQL = """INSERT INTO events (id, title, title_en, start_year, end_year,
    date_precision, is_approximate, region_id, person_ids, tags, tags_en,
    importance, summary, summary_en, description, description_en,
    source_ids, related_event_ids, data_status, confidence_score, external_references)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

all_events = []

def add(p):
    pid = p['id']
    name = p['name']
    name_en = p.get('name_en') or name

def add_evt(eid, title, title_en, year, end_year=None, importance=3,
            summary='', desc='', tags=None, tags_en=None, region='china', sources=None,
            approx=False, conf=0.85):
    global all_events
    if eid in existing_ids: return
    all_events.append((eid, title, title_en, year, end_year, 'year', approx, region,
        json.dumps([pid], ensure_ascii=False),
        json.dumps(tags or ['生平'], ensure_ascii=False),
        json.dumps(tags_en or ['Life'], ensure_ascii=False),
        importance, summary, '', desc, '',
        json.dumps(sources or ['src-cbdb'], ensure_ascii=False), '[]',
        'published', conf, '[]'))
    existing_ids.add(eid)

for p in cursor.fetchall():
    pass  # we'll iterate manually

# ===== 嵇康 (224-263) =====
pid = 'ji-kang-224'
add_evt('evt-deep-jikang-birth', '嵇康出生', 'Birth of Ji Kang', 224,
    3, '嵇康出生于谯郡铚县（今安徽濉溪），自幼聪颖，博览群书。',
    '嵇康（224—263年），字叔夜，谯郡铚人。早孤，有奇才，博览群书，尤好老庄。',
    ['早年','竹林七贤','三国'], ['Early Life','Seven Sages','Three Kingdoms'],
    'three-kingdoms', ['src-sanguozhi', 'src-jinshu'], conf=0.9)

add_evt('evt-deep-jikang-marry', '嵇康娶曹操曾孙女', 'Ji Kang Marries into Cao Wei Royalty', 248,
    4, '嵇康娶曹操曾孙女（或曹林之女）为妻，官拜中散大夫。',
    '嵇康因才华出众，被曹魏宗室看中，娶曹操之子沛穆王曹林的女儿（一说孙女）为妻，官至中散大夫。此婚姻使其与曹魏政权紧密相连，也为日后被杀埋下伏笔。',
    ['仕途','婚姻','三国'], ['Career','Marriage','Three Kingdoms'],
    'three-kingdoms', ['src-jinshu'], conf=0.85)

add_evt('evt-deep-jikang-zhulin', '嵇康入竹林七贤', 'Ji Kang Joins the Seven Sages', 250,
    5, '嵇康与阮籍、山涛、向秀、刘伶、王戎、阮咸共游竹林，世称「竹林七贤」。',
    '嵇康与阮籍、山涛、向秀、刘伶、阮咸、王戎等人常在河内山阳竹林相聚，饮酒清谈，弹琴赋诗，形成了中国历史上最著名的文人团体——「竹林七贤」。他们以蔑视礼法、追求自由的精神影响了整个魏晋时代。',
    ['竹林七贤','文学','三国'], ['Seven Sages','Literature','Three Kingdoms'],
    'three-kingdoms', ['src-jinshu', 'src-shishuoxinyu'], conf=0.9)

add_evt('de-deep-jikang-letter', '嵇康写《与山巨源绝交书》', 'Ji Kang Writes Breakup Letter', 261,
    5, '嵇康公开写信与投靠司马氏的山涛绝交，表明不与司马氏合作的政治立场。',
    '山涛（巨源）推荐嵇康接替自己的官职，嵇康写了一封公开信《与山巨源绝交书》，以「七不堪」「二不可」为由拒绝，实则表明不与司马氏政权合作的政治态度。这封信成为中国文学史上最著名的书信之一，也是嵇康被杀的直接导火索。',
    ['文学','政治','三国'], ['Literature','Politics','Three Kingdoms'],
    'three-kingdoms', ['src-jinshu', 'src-wenxuan'], conf=0.9)

add_evt('evt-deep-jikang-death', '嵇康临刑弹《广陵散》', 'Ji Kang Plays Guangling San at Execution', 263,
    5, '嵇康因卷入吕安案被司马昭处死。临刑前神色自若，索琴弹《广陵散》，叹「《广陵散》于今绝矣」。',
    '嵇康因好友吕安之兄吕巽诬告而被牵连入狱，司马昭听信钟会谗言将其处死。临刑前，三千太学生上书请以为师，不许。嵇康神色不变，索琴弹《广陵散》，曲终叹曰「袁孝尼尝请学此散，吾靳固不与，《广陵散》于今绝矣」。时年四十。',
    ['逝世','音乐','三国'], ['Death','Music','Three Kingdoms'],
    'three-kingdoms', ['src-jinshu', 'src-shishuoxinyu'], conf=0.9)

# ===== 司马昭 (211-265) =====
pid = 'si-ma-zhao-211'
add_evt('evt-deep-simazhao-lead', '司马昭继兄掌权', 'Sima Zhao Takes Power After Brother', 255,
    4, '司马师死后，司马昭继任大将军，掌握曹魏军政大权。',
    '255年司马师在平定毌丘俭叛乱后病逝，其弟司马昭继任大将军、录尚书事，掌握了曹魏的军政大权。时人云「司马昭之心，路人皆知」。',
    ['政治','三国'], ['Politics','Three Kingdoms'],
    'three-kingdoms', ['src-sanguozhi', 'src-jinshu'])

add_evt('evt-deep-simazhao-conquer', '司马昭灭蜀汉', 'Sima Zhao Conquers Shu Han', 263,
    5, '司马昭派钟会、邓艾伐蜀，邓艾偷渡阴平，兵临成都，刘禅出降，蜀汉灭亡。',
    '263年司马昭派钟会、邓艾、诸葛绪三路伐蜀。姜维在剑阁阻挡钟会主力，邓艾出奇兵偷渡阴平小道，翻越摩天岭，直逼成都。刘禅开城投降，蜀汉灭亡。这是三国归晋的关键一步。',
    ['军事','统一','三国'], ['Military','Unification','Three Kingdoms'],
    'three-kingdoms', ['src-sanguozhi', 'src-jinshu'])

add_evt('evt-deep-simazhao-king', '司马昭封晋王', 'Sima Zhao Becomes Prince of Jin', 264,
    4, '灭蜀后司马昭受封晋王，加九锡，距称帝仅一步之遥。',
    '264年灭蜀后，司马昭因功受封晋王，加九锡——这是权臣篡位的标准礼仪。他开始着手建立晋朝的礼仪制度，但次年病逝，最终由其子司马炎完成篡魏。',
    ['政治','三国'], ['Politics','Three Kingdoms'],
    'three-kingdoms', ['src-jinshu'])

# ===== 王重阳 (1113-1170) =====
pid = 'wang-chong-yang-1113'
add_evt('evt-deep-wangcy-revelation', '王重阳甘河遇仙', 'Wang Chongyang Meets Immortals at Ganhe', 1159,
    5, '王重阳在甘河镇遇两位道士授以口诀，自此弃家修道，号重阳子。',
    '正隆四年（1159年），王重阳在甘河镇酒肆中遇两位道士（后世传为钟离权、吕洞宾），授以修炼口诀。此后他抛弃妻子，在南时村掘「活死人墓」居之，自号「王害风」，开始修道传教。这一事件是全真道创立的起点。',
    ['道教','全真','金代'], ['Daoism','Quanzhen','Jin Dynasty'],
    'jin-dynasty-period', ['src-jinshi', 'src-chongyangzhenren'], conf=0.85)

add_evt('evt-deep-wangcy-disciples', '王重阳收全真七子', 'Wang Chongyang Accepts Seven Disciples', 1167,
    5, '王重阳在山东收马钰、谭处端、刘处玄、丘处机、王处一、郝大通、孙不二七人为徒，世称「全真七子」。',
    '大定七年（1167年），王重阳前往山东传道，先后收马钰（丹阳子）、谭处端（长真子）、刘处玄（长生子）、丘处机（长春子）、王处一（玉阳子）、郝大通（广宁子）、孙不二（清静散人）为徒。这七人后来成为全真道各派的开山祖师，其中丘处机更以「万里西行见成吉思汗」闻名。',
    ['道教','全真七子','金代'], ['Daoism','Seven Disciples','Jin Dynasty'],
    'jin-dynasty-period', ['src-jinshi'], conf=0.85)

add_evt('evt-deep-wangcy-death', '王重阳羽化', 'Wang Chongyang Passes Away', 1170,
    4, '王重阳在开封逝世，临终传法于马钰、丘处机等人。',
    '大定十年（1170年），王重阳率马钰、谭处端、刘处玄、丘处机四人西归，至开封时病逝，享年五十八岁。临终前将全真教务托付马钰，嘱咐弟子们继续传道。',
    ['逝世','道教','金代'], ['Death','Daoism','Jin Dynasty'],
    'jin-dynasty-period', ['src-jinshi'], conf=0.85)

# ===== 慕容垂 (326-396) =====
pid = 'mu-rong-chui-326'
add_evt('evt-deep-murongchui-early', '慕容垂大败桓温', 'Murong Chui Defeats Huan Wen', 369,
    5, '慕容垂在枋头大败东晋桓温的北伐军，名声大噪。',
    '369年桓温率五万晋军北伐前燕，兵至枋头。慕容垂临危受命率军抵抗，切断了晋军的粮道和退路，桓温大败而回。此战奠定了慕容垂的军事声望，但也引起前燕权臣慕容评的猜忌。',
    ['军事','前燕','十六国'], ['Military','Former Yan','Sixteen Kingdoms'],
    'sixteen-kingdoms', ['src-jinshu'], conf=0.9)

add_evt('evt-deep-murongchui-found', '慕容垂建立后燕', 'Murong Chui Founds Later Yan', 384,
    5, '淝水之战后慕容垂脱离前秦，在中山称燕王，建立后燕。',
    '383年淝水之战后前秦崩溃，慕容垂借口安抚河北，率部脱离苻坚。384年在荥阳称燕王，后定都中山（今河北定州），建立后燕政权。此后数年他先后消灭丁零翟魏、西燕等政权，恢复了前燕的大部分故土。',
    ['建国','后燕','十六国'], ['Founding','Later Yan','Sixteen Kingdoms'],
    'sixteen-kingdoms', ['src-jinshu'])

add_evt('evt-deep-murongchui-canhebei', '参合陂之战', 'Battle of Canhebei Slope', 395,
    5, '慕容垂命太子慕容宝率八万大军伐北魏，在参合陂惨败，数万燕军被坑杀。',
    '395年慕容垂因病不能亲征，命太子慕容宝率八万大军伐北魏。拓跋珪采取诱敌深入的策略，在参合陂（今内蒙古凉城）趁燕军不备发起突袭，俘虏燕军四五万人后全部坑杀。这是后燕由盛转衰的转折点。',
    ['军事','后燕','十六国'], ['Military','Later Yan','Sixteen Kingdoms'],
    'sixteen-kingdoms', ['src-jinshu', 'src-weishu'])

# ===== 源贺 (407-479) =====
pid = 'yuan-he-407'
add_evt('evt-deep-yuanhe-surrender', '源贺归降北魏', 'Yuan He Surrenders to Northern Wei', 414,
    4, '南凉灭亡后，源贺（秃发破羌）投降北魏，被太武帝拓跋焘赏识，赐姓源。',
    '414年南凉被西秦所灭，末代南凉王秃发傉檀之子秃发破羌等宗室投降北魏。太武帝拓跋焘见其「器度非常」，赐姓「源」，名「贺」，意为「与朕同源」。这开启了源氏在北魏的显赫家族史。',
    ['政治','北魏','南北朝'], ['Politics','Northern Wei','N&S Dynasties'],
    'northern-southern-dynasties', ['src-weishu'], conf=0.85)

add_evt('evt-deep-yuanhe-governor', '源贺任冀州刺史', 'Yuan He Governs Jizhou', 450, 460,
    4, '源贺任冀州刺史期间政绩卓著，刑政宽简，深得民心。',
    '源贺在文成帝拓跋濬时出任冀州刺史，在任期间政绩卓著——「鞠狱以情，未尝刑人」，以教化代替严刑。他在冀州七年，深得民心，离任时百姓遮道挽留。',
    ['仕途','北魏'], ['Career','Northern Wei'],
    'northern-southern-dynasties', ['src-weishu'], conf=0.85)

# ===== 苻生 (334-357) - 前秦暴君 =====
pid = 'fu-sheng-334'
add_evt('evt-deep-fusheng-cruel', '苻生暴政', 'Fu Sheng\'s Tyranny', 355, 357,
    4, '苻生继位后以残暴著称——随意诛杀大臣，手段残忍。',
    '苻生自幼独眼，性格暴戾。355年继位后变本加厉——常弯弓露刃以见朝臣，锤钳锯凿备置左右，稍不如意就当场杀人。他在位两年间杀害后妃、公卿、大臣数十人。史载其「荒耽淫虐，杀戮无道」。但也有观点认为部分暴行是苻坚篡位后史家的渲染诬蔑。【来源野史】',
    ['政治','前秦','十六国'], ['Politics','Former Qin','Sixteen Kingdoms'],
    'sixteen-kingdoms', ['src-jinshu', 'src-yeshi'], conf=0.7)

add_evt('evt-deep-fusheng-death', '苻生被苻坚废杀', 'Fu Sheng Killed by Fu Jian', 357,
    4, '苻坚发动政变废黜苻生，降封越王，不久将其处死。',
    '357年苻生的堂兄弟苻坚在汉族谋士王猛的辅助下发动政变，废黜苻生为越王，随后将其处死。苻坚即位后一改暴政，重用王猛推行改革，前秦迅速强大。',
    ['政变','前秦','十六国'], ['Coup','Former Qin','Sixteen Kingdoms'],
    'sixteen-kingdoms', ['src-jinshu'], conf=0.85)

# ===== 褚渊 (435-482) - 南朝宋齐两朝重臣 =====
pid = 'chu-yuan-435'
add_evt('evt-deep-chuyuan-ascend', '褚渊助萧道成篡宋', 'Chu Yuan Helps Xiao Daocheng Usurp Song', 477, 479,
    4, '褚渊作为宋明帝顾命大臣，却协助萧道成篡位建立南齐。此举被后世视为失节。',
    '褚渊是宋明帝临终时任命的五位顾命大臣之一。宋后废帝刘昱（苍梧王）被杀后，他协助萧道成控制朝政，最终帮助萧道成篡宋建齐。时人讥讽他「宁为袁粲死，不作褚渊生」。',
    ['政治','南齐','南北朝'], ['Politics','Southern Qi','N&S Dynasties'],
    'northern-southern-dynasties', ['src-nanqishu'])

# ===== 辛宪英 (191-269) - 三国智女 =====
pid = 'xin-xian-ying-191'
add_evt('evt-deep-xinxianying-advice', '辛宪英谏弟', 'Xin Xianying Advises Her Brother', 249,
    4, '高平陵事变时，辛宪英劝其弟辛敞尽忠职守，又保全自身。',
    '249年司马懿发动高平陵事变，曹爽集团覆灭在即。辛宪英之弟辛敞时任曹爽参军，犹豫不知何去何从。辛宪英分析局势后劝弟「职守，人之大义也」，敦促他恪尽职守保护曹爽家眷离开洛阳——既全了忠义之名，又在司马懿获胜后免于株连。辛敞依计而行，果然两全。此事展现了辛宪英出色的政治判断力。',
    ['智谋','三国','女性'], ['Wisdom','Three Kingdoms','Female'],
    'three-kingdoms', ['src-jinshu', 'src-sanguozhi'], conf=0.85)

# ===== 张骏 (307-346) - 前凉君主 =====
pid = 'zhang-jun-301'
add_evt('evt-deep-zhangjun-conquer', '张骏攻略西域', 'Zhang Jun Expands into Western Regions', 335, 345,
    4, '张骏在位期间前凉国力强盛，曾派兵远征西域。',
    '张骏执政期间前凉进入全盛期——「尽有陇西之地，士马强盛」。他曾派杨宣率军越流沙征伐龟兹、鄯善，西域诸国纷纷归附。同时他也向东晋称臣，接受东晋的官职封号，在名义上维持对晋朝的忠诚。',
    ['军事','前凉','十六国'], ['Military','Former Liang','Sixteen Kingdoms'],
    'sixteen-kingdoms', ['src-jinshu'], conf=0.85)

# ===== 耶律倍 (899-936) =====
pid = 'ye-lv-bei-899'
add_evt('evt-deep-yelvbei-prince', '耶律倍失太子位', 'Yelv Bei Loses Crown Prince Status', 926,
    4, '辽太祖死后，耶律倍在述律后的政治操作下失去皇位继承权，其弟耶律德光即位。',
    '926年辽太祖耶律阿保机病逝，按太祖遗命应由长子耶律倍继位。但皇后述律平偏爱次子耶律德光，她让耶律倍和耶律德光「俱乘马立帐前」，声称由各部酋长选择——实际上是逼迫耶律倍主动让位。耶律倍被迫表态「德光当立」，建立了中国历史上最早的「让皇帝」先例。',
    ['政治','辽代'], ['Politics','Liao Dynasty'],
    'liao-dynasty', ['src-liaoshi'])

add_evt('evt-deep-yelvbei-exile', '耶律倍投奔后唐', 'Yelv Bei Defects to Later Tang', 930,
    4, '耶律倍在后唐明宗的招诱下，携带大量汉文典籍渡海投奔后唐。',
    '耶律德光即位后对兄长耶律倍多有猜忌，将其软禁在东丹国。930年后唐明宗李嗣源派人招诱耶律倍，他刻诗于木牌「小山压大山，大山全无力」后，携带千卷汉文典籍渡海投奔后唐。此举使他成为中原文化与契丹文化交融的独特桥梁。',
    ['政治','辽代'], ['Politics','Liao Dynasty'],
    'liao-dynasty', ['src-liaoshi'], conf=0.85)

print(f"Total deep events: {len(all_events)}")

if all_events:
    for i in range(0, len(all_events), 50):
        cursor.executemany(INSERT_SQL, all_events[i:i+50])
    conn.commit()
    print(f"Inserted {len(all_events)} deep events")

    for e in all_events:
        pid_from_event = json.loads(e[13])[0]
        cursor.execute("INSERT IGNORE INTO event_persons (event_id, person_id) VALUES (%s, %s)",
                       (e[0], pid_from_event))
    conn.commit()

cursor.execute("SELECT COUNT(*) FROM events")
total_ev = cursor.fetchone()['COUNT(*)']
print(f"Total events: {total_ev}")
cursor.close()
conn.close()
