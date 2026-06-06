#!/usr/bin/env python3
"""
Generate HIGH-QUALITY Tier 1 person entries for new dynasties.
Tier 1 = both birth year AND death year from CBDB.
Outputs JSON directly to src/data/people/_newDynastiesPeople.json

Usage:
  python3 scripts/generate-people-tier1.py
"""

import sqlite3, re, sys, os, json
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


# Dynasty context descriptions
DYNASTY_CONTEXT = {
    '中華民國': '中华民国（1912—1949年）是中国历史上承前启后的转型时期，经历了北洋政府、国民政府、抗日战争及国共内战等重大历史阶段。',
    '中華人民共和國': '中华人民共和国成立于1949年，是中国历史进入新纪元的标志。',
    '後梁': '后梁（907—923年）是五代中的第一个朝代，由朱温（朱全忠）篡唐建立，定都开封。',
    '後唐': '后唐（923—936年）是五代中的第二个朝代，沙陀人李存勖所建，定都洛阳。',
    '後晉': '后晋（936—947年）是五代中的第三个朝代，石敬瑭以割让燕云十六州为代价获得契丹支持而建立。',
    '後漢': '后汉（947—951年）是五代中的第四个朝代，刘知远所建，是五代中最短命的王朝。',
    '後周': '后周（951—960年）是五代中的第五个朝代，郭威所建，周世宗柴荣励精图治，为北宋统一奠定了基础。',
    '後蜀': '后蜀（933—965年）是十国之一，孟知祥在蜀地建立，以成都为都，文化繁荣。',
    '吳': '吴（904—937年）是十国之一，杨行密所建，占据江淮地区，后被南唐取代。',
    '南唐': '南唐（937—975年）是十国中最强盛的政权之一，李昪所建，以金陵（南京）为都，文化发达，后主李煜为著名词人。',
    '吳越': '吴越（907—978年）是十国之一，钱镠所建，据有今浙江全境及苏南部分地区，以保境安民为国策。',
    '閩國': '闽国（909—945年）是十国之一，王审知所建，据有今福建地区，推动了福建的开发与文化发展。',
    '南漢': '南汉（917—971年）是十国之一，刘隐、刘岩兄弟在岭南建立，以广州为都。',
    '吳(楊)': '吴（杨吴，904—937年）是杨行密在江淮建立的政权，以扬州为都，是十国之一。',
    '楚(馬)': '楚（马楚，907—951年）是十国之一，马殷在湖南建立的政权。',
    '南平': '南平（荆南，924—963年）是十国之一，高季兴所建，据有荆州地区。',
    '北漢': '北汉（951—979年）是十国中唯一的北方政权，刘旻所建，据有今山西中北部，是最后一个被北宋灭亡的割据政权。',
    '前蜀': '前蜀（903—925年）是十国之一，王建在蜀地建立，以成都为都。',
    '遼': '辽朝（907—1125年）是契丹族建立的北方政权，疆域辽阔，与北宋并立两百余年，创造了独特的南北面官制度。',
    '金': '金朝（1115—1234年）是女真族建立的王朝，灭辽后南下灭北宋，统治中国北方百余年，后被蒙古所灭。',
    '偽齊': '伪齐（1130—1137年）是金朝扶植的傀儡政权，由刘豫建立，名义上统治中原地区。',
    '西遼': '西辽（1132—1218年）是辽朝灭亡后耶律大石在中亚建立的政权，又称哈剌契丹，延续了辽的国祚。',
    '西夏': '西夏（1038—1227年）是党项族建立的西北政权，创造了独特的西夏文字，与宋、辽、金长期并立，后被蒙古所灭。',
    '西晉': '西晋（265—316年）是司马炎篡魏建立的统一王朝，短暂统一三国后因八王之乱和五胡乱华而衰亡。',
    '東晉': '东晋（317—420年）是西晋灭亡后司马氏在江南建立的偏安政权，以建康为都，与北方十六国对峙近百年。',
    '晉': '晋朝（265—420年）包括西晋和东晋两个阶段，是魏晋南北朝时期的重要阶段。',
}

DYNASTY_CONTEXT_EN = {
    '中華民國': 'The Republic of China (1912–1949) was a transitional period in Chinese history, encompassing the Beiyang Government, the Nationalist Government, the War of Resistance against Japan, and the Chinese Civil War.',
    '中華人民共和國': "The People's Republic of China, founded in 1949, marked a new era in Chinese history.",
    '後梁': 'The Later Liang (907–923) was the first of the Five Dynasties, founded by Zhu Wen after usurping the Tang throne, with its capital at Kaifeng.',
    '後唐': 'The Later Tang (923–936) was the second of the Five Dynasties, founded by the Shatuo leader Li Cunxu, with its capital at Luoyang.',
    '後晉': 'The Later Jin (936–947) was the third of the Five Dynasties, founded by Shi Jingtang at the cost of ceding the Sixteen Prefectures to the Khitans.',
    '後漢': 'The Later Han (947–951) was the fourth and shortest-lived of the Five Dynasties, founded by Liu Zhiyuan.',
    '後周': 'The Later Zhou (951–960) was the fifth of the Five Dynasties, founded by Guo Wei; Emperor Shizong (Chai Rong) laid the groundwork for Song unification.',
    '後蜀': 'The Later Shu (933–965) was one of the Ten Kingdoms, founded by Meng Zhixiang in Sichuan with its capital at Chengdu.',
    '吳': 'Wu (904–937) was one of the Ten Kingdoms, founded by Yang Xingmi in the Jianghuai region, later supplanted by Southern Tang.',
    '南唐': 'Southern Tang (937–975) was one of the strongest of the Ten Kingdoms, founded by Li Bian with its capital at Jinling (Nanjing), known for its cultural achievements.',
    '吳越': 'Wuyue (907–978) was one of the Ten Kingdoms, founded by Qian Liu in modern Zhejiang and southern Jiangsu, pursuing a policy of peace and prosperity.',
    '閩國': 'Min (909–945) was one of the Ten Kingdoms, founded by Wang Shenzhi in modern Fujian, promoting regional development.',
    '南漢': 'Southern Han (917–971) was one of the Ten Kingdoms, founded by the Liu brothers in Lingnan with its capital at Guangzhou.',
    '吳(楊)': 'Wu (Yang Wu, 904–937) was a regime in the Jianghuai region founded by Yang Xingmi, one of the Ten Kingdoms.',
    '楚(馬)': 'Chu (Ma Chu, 907–951) was one of the Ten Kingdoms, founded by Ma Yin in modern Hunan.',
    '南平': 'Nanping (Jingnan, 924–963) was one of the Ten Kingdoms, founded by Gao Jixing in the Jingzhou region.',
    '北漢': 'Northern Han (951–979) was the only northern regime among the Ten Kingdoms, founded by Liu Min in central-northern Shanxi, the last to fall to Song.',
    '前蜀': 'Former Shu (903–925) was one of the Ten Kingdoms, founded by Wang Jian in Sichuan with its capital at Chengdu.',
    '遼': 'The Liao dynasty (907–1125) was the Khitan-established northern empire, vast in territory, coexisting with Northern Song for over two centuries with its innovative dual administration system.',
    '金': 'The Jin dynasty (1115–1234) was the Jurchen-established empire that conquered Liao and Northern Song, ruling northern China until the Mongol conquest.',
    '偽齊': 'The puppet Qi (1130–1137) was a short-lived regime propped up by Jin under Liu Yu, nominally ruling the Central Plains.',
    '西遼': 'The Western Liao (Qara Khitai, 1132–1218) was the continuation of the Liao dynasty established by Yelü Dashi in Central Asia.',
    '西夏': 'The Western Xia (1038–1227) was the Tangut-established northwestern regime, known for its unique script, coexisting with Song, Liao, and Jin until the Mongol conquest.',
    '西晉': 'The Western Jin (265–316) was founded by Sima Yan, briefly reunifying China after the Three Kingdoms before collapsing due to the War of the Eight Princes and nomadic invasions.',
    '東晉': 'The Eastern Jin (317–420) was the Jin court\'s southern remnant based in Jiankang, coexisting with the Sixteen Kingdoms in the north for nearly a century.',
    '晉': 'The Jin dynasty (265–420) comprised Western Jin and Eastern Jin, a significant stage in the Wei-Jin-Northern and Southern Dynasties period.',
}

# Dynasty → regionId
DYN_REGION = {
    '中華民國': 'republic-of-china',
    '中華人民共和國': 'china',
    '後梁': 'five-dynasties', '後唐': 'five-dynasties',
    '後晉': 'five-dynasties', '後漢': 'five-dynasties',
    '後周': 'five-dynasties',
    '後蜀': 'ten-kingdoms', '吳': 'ten-kingdoms',
    '南唐': 'ten-kingdoms', '吳越': 'ten-kingdoms',
    '閩國': 'ten-kingdoms', '南漢': 'ten-kingdoms',
    '吳(楊)': 'ten-kingdoms', '楚(馬)': 'ten-kingdoms',
    '南平': 'ten-kingdoms', '北漢': 'ten-kingdoms',
    '前蜀': 'ten-kingdoms',
    '遼': 'liao-dynasty', '西遼': 'liao-dynasty',
    '金': 'jin-dynasty-period', '偽齊': 'jin-dynasty-period',
    '西夏': 'western-xia',
    '西晉': 'western-jin', '東晉': 'eastern-jin', '晉': 'western-jin',
}

# Display name for tags
DYN_DISPLAY = {
    '中華民國': '民国', '中華人民共和國': '中国',
    '後梁': '后梁', '後唐': '后唐', '後晉': '后晋',
    '後漢': '后汉', '後周': '后周',
    '後蜀': '后蜀', '吳': '吴', '南唐': '南唐', '吳越': '吴越',
    '閩國': '闽国', '南漢': '南汉', '吳(楊)': '杨吴',
    '楚(馬)': '马楚', '南平': '南平', '北漢': '北汉', '前蜀': '前蜀',
    '遼': '辽', '金': '金', '偽齊': '伪齐', '西遼': '西辽', '西夏': '西夏',
    '西晉': '西晋', '東晉': '东晋', '晉': '晋',
}

DB_PATH = '/tmp/cbdb_20260530.sqlite3'

# Load existing names/IDs from ALL people JSON files (not just new dynasties)
import glob
existing_names = set()
existing_names_simp = set()
existing_ids = set()
json_dir = 'src/data/people'
for fp in glob.glob(f'{json_dir}/_peoplePart*.json'):
    with open(fp) as f:
        data = json.load(f)
        for p in data:
            existing_names.add(p['name'])
            existing_names_simp.add(cc.convert(p['name']))
            existing_ids.add(p['id'])
print(f"// Loaded {len(existing_names)} existing names, {len(existing_ids)} existing IDs from JSON files", file=sys.stderr)

# Connect to CBDB
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Get merged IDs
cursor.execute("SELECT DISTINCT c_merged_from_personid FROM MERGED_PERSON_DATA")
merged_ids = set(row[0] for row in cursor.fetchall())

dyn_names = list(DYN_REGION.keys())
dyn_placeholders = ','.join([f"'{d}'" for d in dyn_names])

# TIER 1 ONLY: both birth AND death year required
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

# Fetch posting counts
cursor.execute("SELECT c_personid, COUNT(*) FROM POSTING_DATA GROUP BY c_personid")
posting_counts = dict(cursor.fetchall())

conn.close()

print(f"// {len(candidates):,} Tier 1 candidates from CBDB", file=sys.stderr)

seens = set()
entries = []
stats = {}  # dynasty → count

for row in candidates:
    personid, name_chn, name_en, birth, death, dynasty, female = row

    name_simp = cc.convert(name_chn)

    # Deduplicate
    if (name_chn in existing_names or name_simp in existing_names_simp
        or name_chn in seens or name_simp in seens):
        continue
    if len(name_chn) < 2:
        continue

    seens.add(name_chn)

    region = DYN_REGION.get(dynasty, 'china')
    display_dyn = DYN_DISPLAY.get(dynasty, dynasty)
    stats[display_dyn] = stats.get(display_dyn, 0) + 1

    # English name
    if not name_en or name_en == name_chn:
        py = lazy_pinyin(name_chn)
        name_display_en = ' '.join(py).title()
    else:
        name_display_en = name_en

    # Unique pinyin ID
    pid = to_pinyin_id(name_chn, birth)
    base_pid = pid
    suffix = 1
    while pid in existing_ids:
        suffix += 1
        pid = f"{base_pid}-{suffix}"
    existing_ids.add(pid)

    num_postings = posting_counts.get(personid, 0)

    # Tags
    tags = [display_dyn]
    tags_en = [display_dyn]
    occs = []

    if num_postings >= 10:
        tags.append('官员')
        tags_en.append('Official')
        occs.append('官员')
    elif num_postings >= 3:
        tags.append('官员')
        tags_en.append('Official')
        occs.append('官员')

    if not occs:
        occs.append('历史人物')

    # Year info (always both birth and death for Tier 1)
    year_info = f"{birth}—{death}年"
    year_info_en = f"{birth}–{death}"
    lived_info = f"生于{year_info}"
    lived_info_en = f"lived {year_info_en}"

    if num_postings >= 20:
        career_note = "，仕途显达"
        career_note_en = ", held numerous official positions"
    elif num_postings >= 5:
        career_note = "，有仕宦经历"
        career_note_en = ", held official positions"
    elif num_postings >= 1:
        career_note = "，曾任官职"
        career_note_en = ", held an official post"
    else:
        career_note = ""
        career_note_en = ""

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
        "id": pid,
        "name": name_chn,
        "nameEn": name_display_en,
        "birthYear": birth,
        "deathYear": death,
        "regionId": region,
        "occupations": occs,
        "tags": tags,
        "tagsEn": tags_en,
        "summary": summary_zh,
        "summaryEn": summary_en,
        "description": desc_zh,
        "descriptionEn": desc_en,
        "alternativeNames": [],
        "sourceIds": ["src-cbdb"],
        "wikidataQid": "",
        "dataStatus": "published",
        "confidenceScore": 0.8,
        "externalReferences": [],
    }
    entries.append(entry)

# Write JSON
out_path = 'src/data/people/_newDynastiesPeople.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"\n✅ Written {len(entries):,} entries to {out_path}", file=sys.stderr)
print(f"\n=== 朝代分布 ===", file=sys.stderr)
for dyn, cnt in sorted(stats.items(), key=lambda x: -x[1]):
    print(f"  {dyn}: {cnt:,} 人", file=sys.stderr)
