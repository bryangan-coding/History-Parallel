#!/usr/bin/env python3
"""Deep events for newly published figures from authoritative sources."""
import mysql.connector, json

conn = mysql.connector.connect(user='root', password='', host='localhost', port=3307,
    database='history_parallel', charset='utf8mb4', unix_socket='/tmp/mysql.sock', autocommit=False)
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT id FROM events")
existing_ids = {r['id'] for r in cursor.fetchall()}

events = []
pid = None

def add(eid, title, title_en, year, end_year=None, importance=3, summary='', desc='',
        tags=None, tags_en=None, region='china', sources=None, conf=0.85, approx=False):
    if eid in existing_ids: return
    events.append((eid, title, title_en, year, end_year, 'year', 1 if approx else 0,
        region, None, None, None,
        json.dumps([pid], ensure_ascii=False),
        json.dumps(tags or ['生平'], ensure_ascii=False),
        json.dumps(tags_en or ['Life'], ensure_ascii=False),
        importance, summary or '', '', desc or summary or '', '',
        json.dumps(sources or ['src-cbdb'], ensure_ascii=False), '[]',
        'published', conf, '[]'))
    existing_ids.add(eid)

# ===== 嵇康 =====
pid = 'ji-kang-224'
add('evt-deep-jikang-birth', '嵇康出生', 'Birth of Ji Kang', 224, importance=3,
    summary='嵇康出生于谯郡铚县（今安徽濉溪），自幼聪颖，博览群书，尤好老庄。',
    desc='嵇康（224—263年），字叔夜，谯郡铚人。早孤，有奇才，博览群书，尤好老庄之学。',
    tags=['早年','竹林七贤'], tags_en=['Early Life'], region='three-kingdoms', sources=['src-sanguozhi','src-jinshu'], conf=0.9)
add('evt-deep-jikang-marry', '嵇康娶曹魏宗室女', 'Ji Kang Marries into Cao Wei', 248, importance=4,
    summary='嵇康因才华娶曹操曾孙女为妻，官至中散大夫，与曹魏政权紧密相连。',
    tags=['仕途','三国'], tags_en=['Career'], region='three-kingdoms', sources=['src-jinshu'], conf=0.85)
add('evt-deep-jikang-zhulin', '嵇康入竹林七贤', 'Ji Kang Joins the Seven Sages', 250, importance=5,
    summary='嵇康与阮籍、山涛、向秀、刘伶、阮咸、王戎共游竹林，世称「竹林七贤」，以蔑视礼法、追求自由著称。',
    tags=['竹林七贤','文学'], tags_en=['Seven Sages'], region='three-kingdoms', sources=['src-jinshu','src-shishuoxinyu'], conf=0.9)
add('evt-deep-jikang-letter', '嵇康写《与山巨源绝交书》', 'Ji Kang Writes Breakup Letter', 261, importance=5,
    summary='嵇康写公开信表明不与司马氏合作，「七不堪」「二不可」传为名篇，成为被杀导火索。',
    tags=['文学','政治'], tags_en=['Literature'], region='three-kingdoms', sources=['src-jinshu','src-wenxuan'], conf=0.9)
add('evt-deep-jikang-death', '嵇康临刑弹《广陵散》', 'Ji Kang Plays Guangling San at Execution', 263, importance=5,
    summary='嵇康因吕安案被司马昭处死，临刑弹《广陵散》，叹「《广陵散》于今绝矣」，三千太学生请愿。',
    tags=['逝世','音乐'], tags_en=['Death','Music'], region='three-kingdoms', sources=['src-jinshu','src-shishuoxinyu'], conf=0.9)

# ===== 司马昭 =====
pid = 'si-ma-zhao-211'
add('evt-deep-simazhao-lead', '司马昭继兄掌权', 'Sima Zhao Takes Power', 255, importance=4,
    summary='司马师死后司马昭继任大将军，掌握曹魏军政大权，「司马昭之心路人皆知」。',
    tags=['政治'], tags_en=['Politics'], region='three-kingdoms', sources=['src-sanguozhi','src-jinshu'])
add('evt-deep-simazhao-conquer', '司马昭灭蜀汉', 'Sima Zhao Conquers Shu Han', 263, importance=5,
    summary='司马昭派钟会、邓艾伐蜀，邓艾偷渡阴平兵临成都，刘禅出降，蜀汉灭亡。',
    tags=['军事','三国'], tags_en=['Military'], region='three-kingdoms', sources=['src-sanguozhi','src-jinshu'])
add('evt-deep-simazhao-king', '司马昭封晋王', 'Sima Zhao Becomes Prince of Jin', 264, importance=4,
    summary='灭蜀后司马昭受封晋王加九锡，距称帝仅一步之遥，次年病逝。',
    tags=['政治'], tags_en=['Politics'], region='three-kingdoms', sources=['src-jinshu'])

# ===== 王重阳 =====
pid = 'wang-chong-yang-1113'
add('evt-deep-wangcy-revelation', '王重阳甘河遇仙', 'Wang Chongyang Meets Immortals at Ganhe', 1159, importance=5,
    summary='王重阳在甘河镇遇两位道士授以口诀，此后弃家修道，号重阳子，开启全真道创立之路。',
    tags=['道教','全真'], tags_en=['Daoism'], region='jin-dynasty-period', sources=['src-jinshi'], conf=0.85)
add('evt-deep-wangcy-disciples', '王重阳收全真七子', 'Wang Accepts the Seven Disciples', 1167, importance=5,
    summary='王重阳在山东收马钰、丘处机等七人为徒，世称「全真七子」，奠定全真道教根基。',
    tags=['道教','全真七子'], tags_en=['Daoism'], region='jin-dynasty-period', sources=['src-jinshi'], conf=0.85)
add('evt-deep-wangcy-death', '王重阳羽化', 'Wang Chongyang Passes Away', 1170, importance=4,
    summary='王重阳在开封逝世，临终传法于马钰、丘处机等人，享年五十八岁。',
    tags=['逝世','道教'], tags_en=['Death'], region='jin-dynasty-period', sources=['src-jinshi'], conf=0.85)

# ===== 慕容垂 =====
pid = 'mu-rong-chui-326'
add('evt-deep-murongchui-fangtou', '慕容垂枋头大败桓温', 'Murong Chui Defeats Huan Wen', 369, importance=5,
    summary='慕容垂在枋头大败东晋桓温北伐军，名声大噪但遭前燕权臣猜忌。',
    tags=['军事','前燕'], tags_en=['Military'], region='sixteen-kingdoms', sources=['src-jinshu'], conf=0.9)
add('evt-deep-murongchui-found', '慕容垂建立后燕', 'Murong Chui Founds Later Yan', 384, importance=5,
    summary='淝水之战后慕容垂脱离前秦在中山称燕王，建立后燕政权。',
    tags=['建国','后燕'], tags_en=['Founding'], region='sixteen-kingdoms', sources=['src-jinshu'])
add('evt-deep-murongchui-canhebei', '参合陂之战惨败', 'Battle of Canhebei', 395, importance=5,
    summary='太子慕容宝率八万燕军伐北魏在参合陂惨败，数万燕军被坑杀，后燕由盛转衰。',
    tags=['军事','后燕'], tags_en=['Military'], region='sixteen-kingdoms', sources=['src-jinshu','src-weishu'])

# ===== 苻生 (暴君，含野史争议) =====
pid = 'fu-sheng-334'
add('evt-deep-fusheng-cruel', '苻生暴政', 'Fu Sheng Tyranny', 355, end_year=357, importance=4,
    summary='苻生继位后以残暴著称，随意诛杀大臣。部分记载可能为史家渲染。【来源野史】',
    desc='苻生自幼独眼性格暴戾，继位后常弯弓露刃以见朝臣，锤钳锯凿备置左右。在位两年杀害后妃、公卿、大臣数十人。后世有观点认为部分暴行是苻坚篡位后史家的诬蔑渲染。【来源野史】',
    tags=['暴政','前秦'], tags_en=['Tyranny'], region='sixteen-kingdoms', sources=['src-jinshu','src-yeshi'], conf=0.7)
add('evt-deep-fusheng-death', '苻坚政变废杀苻生', 'Fu Jian Coups Against Fu Sheng', 357, importance=4,
    summary='苻坚在汉人谋士王猛辅助下发动政变废黜苻生，降封越王后处死。',
    tags=['政变','前秦'], tags_en=['Coup'], region='sixteen-kingdoms', sources=['src-jinshu'], conf=0.85)

# ===== 源贺 (南凉王子→北魏重臣) =====
pid = 'yuan-he-407'
add('evt-deep-yuanhe-surrender', '南凉王子归降北魏', 'Prince of Southern Liang Surrenders', 414, importance=4,
    summary='南凉灭亡后秃发破羌归降北魏，太武帝赐姓源名贺，意为「与朕同源」。',
    tags=['政治','北魏'], tags_en=['Politics'], region='northern-southern-dynasties', sources=['src-weishu'], conf=0.85)
add('evt-deep-yuanhe-governor', '源贺治理冀州', 'Yuan He Governs Jizhou', 450, end_year=460, importance=4,
    summary='源贺任冀州刺史七年，刑政宽简深得民心——「鞠狱以情，未尝刑人」。',
    tags=['仕途','北魏'], tags_en=['Career'], region='northern-southern-dynasties', sources=['src-weishu'], conf=0.85)

# ===== 褚渊 =====
pid = 'chu-yuan-435'
add('evt-deep-chuyuan-ascend', '褚渊助萧道成篡宋建齐', 'Chu Yuan Helps Xiao Daocheng', 477, importance=4,
    summary='褚渊作为宋明帝顾命大臣却协助萧道成篡位建立南齐，被后世视为失节。',
    tags=['政治','南齐'], tags_en=['Politics'], region='northern-southern-dynasties', sources=['src-nanqishu'])

# ===== 辛宪英 (三国智女) =====
pid = 'xin-xian-ying-191'
add('evt-deep-xinxianying-advice', '辛宪英智谏其弟', 'Xin Xianying Advises Her Brother', 249, importance=4,
    summary='高平陵事变时辛宪英劝弟恪尽职守保护曹爽家眷，既全忠义又免株连。',
    tags=['智谋','三国','女性'], tags_en=['Wisdom','Female'], region='three-kingdoms', sources=['src-jinshu'], conf=0.85)

# ===== 张骏 =====
pid = 'zhang-jun-301'
add('evt-deep-zhangjun-conquer', '张骏攻略西域', 'Zhang Jun Expands West', 335, end_year=345, importance=4,
    summary='张骏在位期间前凉国力强盛，派兵远征西域，诸国纷纷归附。',
    tags=['军事','前凉'], tags_en=['Military'], region='sixteen-kingdoms', sources=['src-jinshu'], conf=0.85)

# ===== 耶律倍 =====
pid = 'ye-lv-bei-899'
add('evt-deep-yelvbei-prince', '耶律倍失太子位', 'Yelv Bei Loses the Throne', 926, importance=4,
    summary='辽太祖死后述律后操作下耶律倍被迫让位给其弟耶律德光，成为中国最早的「让皇帝」。',
    tags=['政治','辽代'], tags_en=['Politics'], region='liao-dynasty', sources=['src-liaoshi'])
add('evt-deep-yelvbei-exile', '耶律倍投奔后唐', 'Yelv Bei Defects to Later Tang', 930, importance=4,
    summary='耶律倍不堪猜忌，刻诗「小山压大山」后携带千卷汉籍渡海投奔后唐。',
    tags=['政治','辽代'], tags_en=['Politics'], region='liao-dynasty', sources=['src-liaoshi'], conf=0.85)

# ===== 嵇绍 (嵇康之子，含野史) =====
pid = 'ji-shao-253'
add('evt-deep-jishao-death', '嵇绍以身护主', 'Ji Shao Dies Protecting the Emperor', 304, importance=4,
    summary='八王之乱中嵇绍以身护卫晋惠帝血溅帝衣而死。惠帝说「此嵇侍中血，勿去」。【来源野史】',
    desc='304年八王之乱中晋惠帝在荡阴遭遇叛军，侍中嵇绍以身护卫惠帝被乱兵杀死，血溅帝衣。事后侍从要洗去血迹，惠帝说「此嵇侍中血，勿去」。嵇绍是嵇康之子，与其父「叛逆」形象相反，成为忠臣典范。此记载出自唐代官修《晋书》，但细节争议较大。【来源野史】',
    tags=['忠臣','西晋'], tags_en=['Loyalist'], region='western-jin', sources=['src-jinshu','src-yeshi'], conf=0.8)

# ===== 慕容皝 (前燕开国) =====
pid = 'mu-rong-huang-297'
add('evt-deep-muronghuang-found', '慕容皝建立前燕', 'Murong Huang Founds Former Yan', 337, importance=5,
    summary='慕容皝称燕王建立前燕政权，定都龙城，开启慕容鲜卑的建国历程。',
    tags=['建国','前燕'], tags_en=['Founding'], region='sixteen-kingdoms', sources=['src-jinshu'], conf=0.9)

# ===== 苻洪 (前秦奠基者) =====
pid = 'fu-hong-284'
add('evt-deep-fuhong-leader', '苻洪称三秦王', 'Fu Hong Proclaims King of Qin', 350, importance=4,
    summary='苻洪在后赵大乱中称三秦王，为前秦的建立奠定基础，不久被毒杀。',
    desc='350年后赵大乱，苻洪趁机自称大将军、大单于、三秦王，改姓苻氏（原姓蒲，因谶文「艸付应王」而改）。不久被降将麻秋毒杀，但其子苻健继承遗志入据关中建立了前秦。',
    tags=['建国','前秦'], tags_en=['Founding'], region='sixteen-kingdoms', sources=['src-jinshu'])

print(f"Generated: {len(events)} deep events")

for evt in events:
    cursor.execute("INSERT IGNORE INTO events (id,title,title_en,start_year,end_year,date_precision,
        is_approximate,region_id,place_name,place_name_en,coordinates,person_ids,tags,tags_en,
        importance,summary,summary_en,description,description_en,source_ids,related_event_ids,
        data_status,confidence_score,external_references)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", evt)
    pid_from = json.loads(evt[11])[0]
    cursor.execute("INSERT IGNORE INTO event_persons (event_id,person_id) VALUES (%s,%s)", (evt[0], pid_from))

conn.commit()
cursor.execute("SELECT COUNT(*) FROM events")
print(f"Total events: {cursor.fetchone()['COUNT(*)']}")
cursor.execute("SELECT COUNT(*) FROM events WHERE description LIKE '%【来源野史】%'")
print(f"Marked 【来源野史】: {cursor.fetchone()['COUNT(*)']}")
cursor.close()
conn.close()
