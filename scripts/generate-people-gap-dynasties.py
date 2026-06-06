#!/usr/bin/env python3
"""
Phase 1: Generate Tier 1 entries for GAP dynasties (not covered by Phase 0).
Fills: 周, 汉(东汉/西汉), 三国, 南北朝, 隋(增补), 十六国(增补)

Tier 1 = both birth year AND death year from CBDB.
Outputs JSON directly to src/data/people/_gapDynastiesPeople.json
"""

import sqlite3, re, sys, os, json, glob
from pypinyin import lazy_pinyin, Style
from opencc import OpenCC

cc = OpenCC('t2s')

def to_pinyin_id(name, birth):
    py = lazy_pinyin(name, style=Style.TONE3)
    py_clean = []
    for p in py:
        p = re.sub(r'\d', '', p)
        py_clean.append(p)
    slug = '-'.join(py_clean).lower()
    slug = re.sub(r'[^a-z-]', '', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    if birth and birth > 0:
        return f"{slug}-{birth}"
    return slug


# ==================== Dynasty Context Descriptions ====================

DYNASTY_CONTEXT = {
    # 周朝
    '周': '周朝（前1046—前256年）是中国历史上存续时间最长的王朝，约八百年。西周定都镐京（今西安），创分封制与礼乐制度；东周王室衰微，进入诸侯争霸的春秋战国时代，诸子百家思想繁荣。',

    # 汉朝
    '東漢': '东汉（25—220年）是刘秀推翻王莽新朝后重建的汉政权，定都洛阳。东汉前期光武中兴、明章之治，国力强盛；后期外戚与宦官交替专权，终致黄巾起义与群雄割据。',
    '西漢': '西汉（前202—公元9年）是刘邦建立的汉政权，定都长安。文景之治、汉武盛世奠定了中国两千年帝制的基本格局，张骞通西域开辟了丝绸之路。',
    '秦漢': '秦汉时期（前221—公元220年）是中国历史上第一个大一统帝国时代，秦朝确立中央集权制度，汉朝继承并发展了这套制度，奠定了中华文明的基本格局。',

    # 三国
    '三國': '三国时期（220—280年）是东汉灭亡后魏、蜀、吴三国鼎立的历史阶段，是中国历史上最著名的乱世之一，人才辈出，故事流传千古。',
    '三國魏': '曹魏（220—265年）是三国之一，曹丕篡汉建立，定都洛阳，占据北方广大地区，实力最为雄厚，后被司马氏篡夺。',
    '三國吳': '孙吴（222—280年）是三国之一，孙权在江东建立的政权，以建业（今南京）为都，拥有强大的水军，开发了江南地区。',
    '三國蜀': '蜀汉（221—263年）是三国之一，刘备以汉室宗亲自居建立的政权，定都成都，诸葛亮辅政时期一度强盛，后为曹魏所灭。',

    # 南北朝
    '南北朝': '南北朝时期（420—589年）是东晋灭亡后中国南北分裂的时代，南朝经历了宋、齐、梁、陈四个汉族政权，北朝经历了北魏、东魏、西魏、北齐、北周等政权，是民族大融合的重要阶段。',
    '宋(劉)': '刘宋（420—479年）是南朝的第一个朝代，刘裕建立，定都建康（今南京），是南朝疆域最广、国力最强盛的一朝。',
    '南齊': '南齐（479—502年）是南朝的第二个朝代，萧道成所建，定都建康，享国短暂但文学艺术有所发展。',
    '南梁': '南梁（502—557年）是南朝的第三个朝代，萧衍（梁武帝）所建，定都建康，梁武帝崇佛，文化发达，后期发生侯景之乱而衰落。',
    '陳': '陈朝（557—589年）是南朝最后一个朝代，陈霸先所建，定都建康，是南朝疆域最小的政权，后被隋朝所灭。',
    '北魏': '北魏（386—534年）是北朝的第一个朝代，鲜卑拓跋氏建立，统一北方，孝文帝推行汉化改革，迁都洛阳，对民族融合贡献巨大。',
    '北周': '北周（557—581年）是北朝的政权之一，宇文氏建立，灭北齐统一北方，为隋朝统一全国奠定了基础。',
    '東魏': '东魏（534—550年）是北魏分裂后的东部政权，定都邺城，由高欢实际控制，后被北齐取代。',
    '西魏': '西魏（535—556年）是北魏分裂后的西部政权，定都长安，由宇文泰实际控制，后被北周取代。',
    '東梁': '东梁（555—587年）是南北朝时期存在于江陵地区的西梁政权，又称后梁，是北朝的附庸。',
    '西梁': '西梁（555—587年）是南北朝后期存在于江陵地区的政权，又称后梁，名义上延续梁朝，实际受西魏/北周/隋控制。',

    # 十六国
    '前秦': '前秦（350—394年）是十六国之一，氐族苻洪建立，苻坚时期在王猛辅佐下统一北方，推行汉化政策，淝水之战后崩溃。',
    '前燕': '前燕（337—370年）是十六国之一，鲜卑慕容氏建立于辽东，后迁都邺城，一度雄踞华北，被前秦所灭。',
    '前涼': '前凉（317—376年）是十六国之一，汉人张轨在河西走廊建立的政权，崇尚儒学，保存了大量中原文化。',
    '後燕': '后燕（384—407年）是十六国之一，鲜卑慕容垂在淝水之战后重建的政权，定都中山（今河北定州）。',
    '後趙': '后赵（319—351年）是十六国之一，羯族石勒所建，一度统治北方大部分地区，石虎时期残暴统治导致内乱。',
    '後涼': '后凉（386—403年）是十六国之一，氐族吕光在凉州建立的政权，后被后秦所灭。',
    '西涼': '西凉（400—421年）是十六国之一，汉人李暠在敦煌建立的政权，崇尚儒学，后被北凉所灭。',
    '後秦': '后秦（384—417年）是十六国之一，羌族姚苌所建，据有关中地区，推崇佛教，被东晋刘裕所灭。',
    '南燕': '南燕（398—410年）是十六国之一，鲜卑慕容德建立于山东，被东晋所灭。',
    '北燕': '北燕（407—436年）是十六国之一，冯跋建立的汉族政权，据有辽西，后被北魏所灭。',
    '前趙': '前赵（304—329年）是十六国之一，匈奴刘渊所建，是十六国时期最早建立的政权之一。',
    '西秦': '西秦（385—431年）是十六国之一，鲜卑乞伏国仁所建于陇西，后被赫连夏所灭。',
    '北涼': '北凉（401—439年）是十六国之一，匈奴沮渠蒙逊所建，据有河西走廊，后被北魏所灭。',
    '西燕': '西燕（384—394年）是十六国之一，鲜卑慕容冲建立于关中，后被后燕所灭。',
    '代': '代国（310—376年）是十六国之一，鲜卑拓跋部在漠南建立的政权，是北魏的前身。',

    # 隋朝
    '隋': '隋朝（581—618年）是杨坚结束南北朝分裂建立的统一王朝，定都大兴城（今西安），创立三省六部制与科举制度，开凿大运河，为唐朝盛世奠定了基础。',
}

DYNASTY_CONTEXT_EN = {
    '周': 'The Zhou dynasty (1046–256 BCE) was the longest-lasting dynasty in Chinese history, spanning nearly eight centuries. The Western Zhou established feudalism and the ritual-music system; the Eastern Zhou saw the rise of contending states and the flourishing of the Hundred Schools of Thought.',

    '東漢': 'The Eastern Han (25–220 CE) was the restored Han dynasty founded by Liu Xiu, with its capital at Luoyang. It saw a period of revival followed by the rise of eunuch and consort clan power struggles, ultimately leading to the Yellow Turban Rebellion.',
    '西漢': 'The Western Han (202 BCE–9 CE) was founded by Liu Bang with its capital at Chang\'an. The reigns of Wen, Jing, and Wu established the fundamental patterns of Chinese imperial governance, and Zhang Qian\'s missions opened the Silk Road.',
    '秦漢': 'The Qin-Han period (221 BCE–220 CE) was China\'s first great imperial age. The Qin established centralized rule, and the Han inherited and developed this system, laying the foundations of Chinese civilization.',

    '三國': 'The Three Kingdoms period (220–280 CE) followed the fall of the Han, with Wei, Shu, and Wu vying for supremacy. It is one of the most celebrated eras in Chinese history, rich in tales of strategy and heroism.',
    '三國魏': 'Cao Wei (220–265) was the strongest of the Three Kingdoms, founded by Cao Pi in the north with its capital at Luoyang. It was later usurped by the Sima clan.',
    '三國吳': 'Sun Wu (222–280) was one of the Three Kingdoms, established by Sun Quan in the Jiangdong region with its capital at Jianye (Nanjing), known for its powerful navy.',
    '三國蜀': 'Shu Han (221–263) was founded by Liu Bei in Sichuan with its capital at Chengdu, claiming to continue the Han dynasty. Under Zhuge Liang\'s regency it achieved brief prominence before being conquered by Wei.',

    '南北朝': 'The Northern and Southern Dynasties period (420–589) was an era of division between northern and southern China, marked by frequent regime changes and significant ethnic integration.',
    '宋(劉)': 'The Liu Song dynasty (420–479) was the first of the Southern Dynasties, founded by Liu Yu with its capital at Jiankang, boasting the largest territory among the southern regimes.',
    '南齊': 'The Southern Qi (479–502) was the second Southern Dynasty, founded by Xiao Daocheng, brief but culturally active.',
    '南梁': 'The Southern Liang (502–557) was founded by Xiao Yan (Emperor Wu), a devout Buddhist whose long reign saw cultural flourishing before the catastrophic Hou Jing rebellion.',
    '陳': 'The Chen dynasty (557–589) was the last of the Southern Dynasties, founded by Chen Baxian, the smallest in territory, eventually conquered by the Sui.',
    '北魏': 'The Northern Wei (386–534) unified northern China under the Xianbei Tuoba clan. Emperor Xiaowen\'s sinicization reforms, including moving the capital to Luoyang, profoundly shaped Chinese history.',
    '北周': 'The Northern Zhou (557–581), founded by the Yuwen clan, conquered the Northern Qi and unified the north, paving the way for Sui reunification.',
    '東魏': 'The Eastern Wei (534–550) was the eastern successor state after the Northern Wei split, controlled by Gao Huan, later replaced by Northern Qi.',
    '西魏': 'The Western Wei (535–556) was the western successor state after the Northern Wei split, controlled by Yuwen Tai, later replaced by Northern Zhou.',
    '東梁': 'The Eastern Liang (555–587), also known as Western Liang or Later Liang, was a small buffer state in the Jiangling region.',
    '西梁': 'The Western Liang (555–587), also known as Later Liang, was a small succession state in the Jiangling region, nominally continuing the Liang dynasty.',

    '前秦': 'Former Qin (350–394) was one of the Sixteen Kingdoms, founded by the Di leader Fu Hong. Under Fu Jian and his minister Wang Meng, it briefly unified the north before collapsing after the Battle of Fei River.',
    '前燕': 'Former Yan (337–370) was one of the Sixteen Kingdoms, established by the Xianbei Murong clan in Liaodong, later moving its capital to Ye.',
    '前涼': 'Former Liang (317–376) was one of the Sixteen Kingdoms, a Han Chinese regime founded by Zhang Gui in the Hexi Corridor, preserving classical culture.',
    '後燕': 'Later Yan (384–407) was re-established by the Xianbei Murong Chui after the Battle of Fei River, with its capital at Zhongshan.',
    '後趙': 'Later Zhao (319–351) was founded by the Jie leader Shi Le, once dominating most of northern China before descending into internal strife.',
    '後涼': 'Later Liang (386–403) was a Di regime founded by Lü Guang in Liangzhou.',
    '西涼': 'Western Liang (400–421) was founded by the Han Chinese Li Gao at Dunhuang, known for its scholarly culture.',
    '後秦': 'Later Qin (384–417) was founded by the Qiang leader Yao Chang in the Guanzhong region, known for promoting Buddhism.',
    '南燕': 'Southern Yan (398–410) was founded by the Xianbei Murong De in Shandong.',
    '北燕': 'Northern Yan (407–436) was a Han Chinese regime founded by Feng Ba in western Liaoning.',
    '前趙': 'Former Zhao (304–329) was founded by the Xiongnu Liu Yuan, one of the earliest of the Sixteen Kingdoms.',
    '西秦': 'Western Qin (385–431) was founded by the Xianbei Qifu Guoren in Longxi.',
    '北涼': 'Northern Liang (401–439) was founded by the Xiongnu Juqu Mengxun in the Hexi Corridor.',
    '西燕': 'Western Yan (384–394) was founded by the Xianbei Murong Chong in the Guanzhong region.',
    '代': 'The Dai state (310–376) was established by the Xianbei Tuoba clan south of the Gobi, the predecessor of Northern Wei.',

    '隋': 'The Sui dynasty (581–618) was founded by Yang Jian, who reunified China after centuries of division. It established the Three Departments and Six Ministries system, the imperial examination, and the Grand Canal, laying the foundation for the Tang golden age.',
}

# CBDB dynasty → regionId
DYN_REGION = {
    '周': 'zhou-dynasty',
    '東漢': 'han-dynasty', '西漢': 'han-dynasty', '秦漢': 'han-dynasty',
    '三國': 'three-kingdoms', '三國魏': 'three-kingdoms',
    '三國吳': 'three-kingdoms', '三國蜀': 'three-kingdoms',
    '南北朝': 'northern-southern-dynasties',
    '宋(劉)': 'northern-southern-dynasties',
    '南齊': 'northern-southern-dynasties',
    '南梁': 'northern-southern-dynasties',
    '陳': 'northern-southern-dynasties',
    '北魏': 'northern-southern-dynasties',
    '北周': 'northern-southern-dynasties',
    '東魏': 'northern-southern-dynasties',
    '西魏': 'northern-southern-dynasties',
    '東梁': 'northern-southern-dynasties',
    '西梁': 'northern-southern-dynasties',
    '隋': 'sui-dynasty',
    '前秦': 'sixteen-kingdoms', '前燕': 'sixteen-kingdoms',
    '前涼': 'sixteen-kingdoms', '後燕': 'sixteen-kingdoms',
    '後趙': 'sixteen-kingdoms', '後涼': 'sixteen-kingdoms',
    '西涼': 'sixteen-kingdoms', '後秦': 'sixteen-kingdoms',
    '南燕': 'sixteen-kingdoms', '北燕': 'sixteen-kingdoms',
    '前趙': 'sixteen-kingdoms', '西秦': 'sixteen-kingdoms',
    '北涼': 'sixteen-kingdoms', '西燕': 'sixteen-kingdoms',
    '代': 'sixteen-kingdoms',
}

# Display name for tags
DYN_DISPLAY = {
    '周': '周', '東漢': '东汉', '西漢': '西汉', '秦漢': '秦汉',
    '三國': '三国', '三國魏': '曹魏', '三國吳': '孙吴', '三國蜀': '蜀汉',
    '南北朝': '南北朝', '宋(劉)': '刘宋', '南齊': '南齐', '南梁': '南梁',
    '陳': '陈', '北魏': '北魏', '北周': '北周',
    '東魏': '东魏', '西魏': '西魏', '東梁': '东梁', '西梁': '西梁',
    '隋': '隋',
    '前秦': '前秦', '前燕': '前燕', '前涼': '前凉', '後燕': '后燕',
    '後趙': '后赵', '後涼': '后凉', '西涼': '西凉', '後秦': '后秦',
    '南燕': '南燕', '北燕': '北燕', '前趙': '前赵', '西秦': '西秦',
    '北涼': '北凉', '西燕': '西燕', '代': '代国',
}

DB_PATH = '/tmp/cbdb_20260530.sqlite3'

# Load existing names/IDs from ALL people JSON files
existing_names = set()
existing_names_simp = set()
existing_ids = set()
json_dir = 'src/data/people'
for fp in glob.glob(f'{json_dir}/*.json'):
    with open(fp) as f:
        data = json.load(f)
        for p in data:
            existing_names.add(p['name'])
            existing_names_simp.add(cc.convert(p['name']))
            existing_ids.add(p['id'])
print(f"// Loaded {len(existing_names):,} existing names, {len(existing_ids):,} existing IDs from JSON files", file=sys.stderr)

# Connect to CBDB
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT DISTINCT c_merged_from_personid FROM MERGED_PERSON_DATA")
merged_ids = set(row[0] for row in cursor.fetchall())

dyn_names = list(DYN_REGION.keys())
dyn_placeholders = ','.join([f"'{d}'" for d in dyn_names])

# TIER 1 ONLY
cursor.execute(f"""
    SELECT b.c_personid, b.c_name_chn, b.c_name, b.c_birthyear, b.c_deathyear, 
           d.c_dynasty_chn, b.c_female
    FROM BIOG_MAIN b
    JOIN DYNASTIES d ON b.c_dy = d.c_dy
    WHERE b.c_name_chn != '未詳'
    AND b.c_birthyear > 0 
    AND b.c_deathyear > 0
    AND d.c_dynasty_chn IN ({dyn_placeholders})
    AND b.c_personid NOT IN (SELECT DISTINCT c_merged_from_personid FROM MERGED_PERSON_DATA)
    ORDER BY b.c_birthyear, b.c_personid
""")

candidates = cursor.fetchall()

cursor.execute("SELECT c_personid, COUNT(*) FROM POSTING_DATA GROUP BY c_personid")
posting_counts = dict(cursor.fetchall())

conn.close()

print(f"// {len(candidates):,} Phase 1 Tier 1 candidates from CBDB", file=sys.stderr)

seens = set()
entries = []
stats = {}

for row in candidates:
    personid, name_chn, name_en, birth, death, dynasty, female = row
    name_simp = cc.convert(name_chn)

    if (name_chn in existing_names or name_simp in existing_names_simp
        or name_chn in seens or name_simp in seens):
        continue
    if len(name_chn) < 2:
        continue

    seens.add(name_chn)

    region = DYN_REGION.get(dynasty, 'china')
    display_dyn = DYN_DISPLAY.get(dynasty, dynasty)
    stats[display_dyn] = stats.get(display_dyn, 0) + 1

    if not name_en or name_en == name_chn:
        py = lazy_pinyin(name_chn)
        name_display_en = ' '.join(py).title()
    else:
        name_display_en = name_en

    pid = to_pinyin_id(name_chn, birth)
    base_pid = pid
    suffix = 1
    while pid in existing_ids:
        suffix += 1
        pid = f"{base_pid}-{suffix}"
    existing_ids.add(pid)

    num_postings = posting_counts.get(personid, 0)

    tags = [display_dyn]
    tags_en = [display_dyn]
    occs = []

    if num_postings >= 10:
        tags.append('官员'); tags_en.append('Official'); occs.append('官员')
    elif num_postings >= 3:
        tags.append('官员'); tags_en.append('Official'); occs.append('官员')

    if not occs:
        occs.append('历史人物')

    year_info = f"{birth}—{death}年"
    year_info_en = f"{birth}–{death}"
    lived_info = f"生于{year_info}"
    lived_info_en = f"lived {year_info_en}"

    if num_postings >= 20:
        career_note = "，仕途显达"; career_note_en = ", held numerous official positions"
    elif num_postings >= 5:
        career_note = "，有仕宦经历"; career_note_en = ", held official positions"
    elif num_postings >= 1:
        career_note = "，曾任官职"; career_note_en = ", held an official post"
    else:
        career_note = ""; career_note_en = ""

    female_note = '女性' if female else ''
    female_note_en = ' (female)' if female else ''

    period_name = display_dyn
    context_zh = DYNASTY_CONTEXT.get(dynasty, f'{period_name}是中国历史上的重要时期。')
    context_en = DYNASTY_CONTEXT_EN.get(dynasty, f'The {period_name} period was an important era in Chinese history.')

    summary_zh = f"{period_name}时期{female_note}历史人物，{lived_info}{career_note}。其事迹见于相关史料记载。"
    summary_en = f"Historical figure of the {period_name} period{female_note_en}, {lived_info_en}{career_note_en}. Documented in historical sources."

    desc_zh = f'{name_chn}（{year_info}），{period_name}人物。{context_zh}关于其生平与事迹的记载，散见于相关史籍文献之中，反映了当时的历史风貌与社会环境。'
    desc_en = f'{name_chn} ({year_info_en}) was a figure of the {period_name} period. {context_en} Records of their life and deeds are preserved in historical texts and documents, reflecting the historical context and social environment of the era.'

    entry = {
        "id": pid, "name": name_chn, "nameEn": name_display_en,
        "birthYear": birth, "deathYear": death,
        "regionId": region, "occupations": occs,
        "tags": tags, "tagsEn": tags_en,
        "summary": summary_zh, "summaryEn": summary_en,
        "description": desc_zh, "descriptionEn": desc_en,
        "alternativeNames": [],
        "sourceIds": ["src-cbdb"],
        "wikidataQid": "",
        "dataStatus": "published",
        "confidenceScore": 0.8,
        "externalReferences": [],
    }
    entries.append(entry)

out_path = 'src/data/people/_gapDynastiesPeople.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"\n✅ Phase 1: Written {len(entries):,} entries to {out_path}", file=sys.stderr)
print(f"\n=== Phase 1 朝代分布 ===", file=sys.stderr)
for dyn, cnt in sorted(stats.items(), key=lambda x: -x[1]):
    print(f"  {dyn}: {cnt:,} 人", file=sys.stderr)
