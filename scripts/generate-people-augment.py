#!/usr/bin/env python3
"""
Phase 2: Augment existing dynasties with additional Tier 1 entries.
Focus: 唐, 元, 明, 清 (Song already saturated at 10.5K)

Tier 1 = both birth year AND death year from CBDB.
Outputs JSON to src/data/people/_augmentDynastiesPeople.json
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


DYNASTY_CONTEXT = {
    '唐': '唐朝（618—907年）是中国历史上最强盛的王朝之一，定都长安。贞观之治、开元盛世创造了空前的繁荣，诗歌、书法、绘画等文化艺术达到巅峰，对东亚文明影响深远。',
    '元': '元朝（1271—1368年）是蒙古族建立的统一王朝，定都大都（今北京），疆域辽阔，横跨欧亚，促进了东西方文化交流。行省制度的创立对后世影响深远。',
    '明': '明朝（1368—1644年）是朱元璋推翻元朝建立的汉族王朝，定都应天（南京）后迁都北京。永乐盛世、郑和下西洋彰显国威，后期宦官专权、党争激烈，终被农民起义推翻。',
    '清': '清朝（1644—1912年）是中国最后一个封建王朝，由满族建立，定都北京。康乾盛世时疆域辽阔、人口剧增，是中国传统社会的巅峰时期，晚期面临内忧外患而走向衰亡。',
}

DYNASTY_CONTEXT_EN = {
    '唐': "The Tang dynasty (618–907) was one of China's greatest imperial ages, with its capital at Chang'an. The Zhenguan and Kaiyuan eras saw unprecedented prosperity, and poetry, calligraphy, and painting reached their zenith, profoundly influencing East Asian civilization.",
    '元': 'The Yuan dynasty (1271–1368) was the Mongol-established unified empire with its capital at Dadu (Beijing). Its vast territory spanned Eurasia, facilitating East-West cultural exchange, and its provincial administration system had lasting influence.',
    '明': 'The Ming dynasty (1368–1644) was founded by Zhu Yuanzhang, with its capital first at Nanjing then Beijing. The Yongle era and Zheng He\'s voyages projected Chinese power overseas, while later periods saw eunuch dominance and factional strife.',
    '清': 'The Qing dynasty (1644–1912) was China\'s last imperial dynasty, founded by the Manchus with its capital at Beijing. The Kangxi-Qianlong era saw vast territorial expansion and population growth, representing the peak of traditional Chinese society before facing internal and external crises.',
}

DYN_REGION = {
    '唐': 'tang-dynasty', '元': 'yuan-dynasty',
    '明': 'ming-dynasty', '清': 'qing-dynasty',
}

DYN_DISPLAY = {
    '唐': '唐', '元': '元', '明': '明', '清': '清',
}

DB_PATH = '/tmp/cbdb_20260530.sqlite3'

# Load existing names/IDs
existing_names = set()
existing_names_simp = set()
existing_ids = set()
json_dir = 'src/data/people'
for fp in glob.glob(f'{json_dir}/*.json'):
    with open(fp) as f:
        for p in json.load(f):
            existing_names.add(p['name'])
            existing_names_simp.add(cc.convert(p['name']))
            existing_ids.add(p['id'])
print(f"// Loaded {len(existing_names):,} existing names, {len(existing_ids):,} existing IDs", file=sys.stderr)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT c_merged_from_personid FROM MERGED_PERSON_DATA")
merged_ids = set(row[0] for row in cursor.fetchall())

dyn_names = list(DYN_REGION.keys())
dyn_placeholders = ','.join([f"'{d}'" for d in dyn_names])

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

print(f"// {len(candidates):,} Phase 2 Tier 1 candidates from CBDB", file=sys.stderr)

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
        name_display_en = ' '.join(lazy_pinyin(name_chn)).title()
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

out_path = 'src/data/people/_augmentDynastiesPeople.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"\n✅ Phase 2: Written {len(entries):,} entries to {out_path}", file=sys.stderr)
print(f"\n=== Phase 2 朝代分布 ===", file=sys.stderr)
for dyn, cnt in sorted(stats.items(), key=lambda x: -x[1]):
    print(f"  {dyn}: {cnt:,} 人", file=sys.stderr)
