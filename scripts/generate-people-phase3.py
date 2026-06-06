#!/usr/bin/env python3
"""
Phase 3: Rescue missing dynasties (秦/西汉/西夏) + Expand 唐/元/明 to Song level.

Phase 3a — Rescue (even without Tier 1, all available data):
  秦 (贏秦/秦漢), 西汉 (西漢/漢前), 西夏

Phase 3b — Expand to ~10,500 (Song standard):
  唐 (LIMIT 6000), 元 (LIMIT 10000), 明 (LIMIT 10000)

Tiers handled:
  Tier 2: birth OR death only (confidence 0.65)
  Tier 3: index_year only (confidence 0.65)
  No date: dynasty period only (confidence 0.5, no birth/death field)

Output: src/data/people/_rescueAndExpandPeople.json
"""

import sqlite3, re, sys, os, json, glob
from pypinyin import lazy_pinyin, Style
from opencc import OpenCC

cc = OpenCC('t2s')

def to_pinyin_id(name, birth):
    py = lazy_pinyin(name, style=Style.TONE3)
    py_clean = [re.sub(r'\d', '', p) for p in py]
    slug = '-'.join(py_clean).lower()
    slug = re.sub(r'[^a-z-]', '', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    if birth and birth > 0:
        return f"{slug}-{birth}"
    return slug


# ==================== Dynasty Context ====================

DYNASTY_CONTEXT = {
    # Phase 3a: Rescue dynasties
    '贏秦': '秦朝（前221—前207年）是中国历史上第一个大一统帝国，秦王嬴政灭六国后称始皇帝，推行郡县制、统一文字度量衡、修筑长城。虽享国短暂，但奠定了中国两千余年帝制的基本格局。',
    '秦漢': '秦汉时期（前221—公元220年）是中国历史上第一个大一统帝国时代，秦朝确立中央集权制度，汉朝继承并发展了这套制度。',
    '西漢': '西汉（前202—公元9年）是刘邦建立的强大帝国，定都长安。文景之治、汉武盛世奠定了中国两千年帝制的基本格局，张骞通西域开辟了丝绸之路。',
    '漢前': '汉朝前期（前202—公元9年），即西汉时期，是刘邦建立的强大帝国，开创了中国历史上第一个长期稳定的大一统王朝。',
    '西夏': '西夏（1038—1227年）是党项族建立的西北政权，创造了独特的西夏文字，与宋、辽、金长期并立近两百年，后被蒙古所灭。',

    # Phase 3b: Expand dynasties
    '唐': '唐朝（618—907年）是中国历史上最强盛的王朝之一，定都长安。贞观之治、开元盛世创造了空前的繁荣，诗歌、书法、绘画等文化艺术达到巅峰，对东亚文明影响深远。',
    '元': '元朝（1271—1368年）是蒙古族建立的统一王朝，定都大都（今北京），疆域辽阔，横跨欧亚，促进了东西方文化交流。行省制度的创立对后世影响深远。',
    '明': '明朝（1368—1644年）是朱元璋推翻元朝建立的汉族王朝，定都应天（南京）后迁都北京。永乐盛世、郑和下西洋彰显国威，后期宦官专权、党争激烈，终被农民起义推翻。',
}

DYNASTY_CONTEXT_EN = {
    '贏秦': 'The Qin dynasty (221–207 BCE) was China\'s first unified empire. Qin Shi Huang conquered the six warring states, established the commandery-county system, standardized writing and measurements, and built the Great Wall. Though short-lived, it laid the foundations for two millennia of imperial rule.',
    '秦漢': 'The Qin-Han period (221 BCE–220 CE) was China\'s first great imperial age. The Qin established centralized rule, and the Han inherited and developed this system.',
    '西漢': 'The Western Han (202 BCE–9 CE) was founded by Liu Bang with its capital at Chang\'an. The reigns of Wen, Jing, and Wu established the fundamental patterns of Chinese imperial governance, and Zhang Qian\'s missions opened the Silk Road.',
    '漢前': 'The Early Han period (202 BCE–9 CE), i.e. Western Han, was a powerful empire founded by Liu Bang, China\'s first enduring unified dynasty.',
    '西夏': 'The Western Xia (1038–1227) was the Tangut-established northwestern regime, known for its unique script, coexisting with Song, Liao, and Jin for nearly two centuries until the Mongol conquest.',
    '唐': "The Tang dynasty (618–907) was one of China's greatest imperial ages, with its capital at Chang'an. The Zhenguan and Kaiyuan eras saw unprecedented prosperity, and poetry, calligraphy, and painting reached their zenith, profoundly influencing East Asian civilization.",
    '元': 'The Yuan dynasty (1271–1368) was the Mongol-established unified empire with its capital at Dadu (Beijing). Its vast territory spanned Eurasia, facilitating East-West cultural exchange, and its provincial administration system had lasting influence.',
    '明': 'The Ming dynasty (1368–1644) was founded by Zhu Yuanzhang, with its capital first at Nanjing then Beijing. The Yongle era and Zheng He\'s voyages projected Chinese power overseas, while later periods saw eunuch dominance and factional strife.',
}

DYN_REGION = {
    '贏秦': 'qin-dynasty', '秦漢': 'qin-dynasty',
    '西漢': 'han-dynasty', '漢前': 'han-dynasty',
    '西夏': 'western-xia',
    '唐': 'tang-dynasty', '元': 'yuan-dynasty', '明': 'ming-dynasty',
}

DYN_DISPLAY = {
    '贏秦': '秦', '秦漢': '秦汉',
    '西漢': '西汉', '漢前': '西汉',
    '西夏': '西夏',
    '唐': '唐', '元': '元', '明': '明',
}

# ==================== Phase 3a: Rescue (no LIMIT) ====================
PHASE3A_DYNS = ['贏秦', '秦漢', '西漢', '漢前', '西夏']

# ==================== Phase 3b: Expand (with LIMIT) ====================
PHASE3B_DYNS = {
    '唐': 6000,
    '元': 10000,
    '明': 10000,
}

ALL_DYNS = PHASE3A_DYNS + list(PHASE3B_DYNS.keys())

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

dyn_placeholders = ','.join([f"'{d}'" for d in ALL_DYNS])

# Query ALL tiers for these dynasties
cursor.execute(f"""
    SELECT b.c_personid, b.c_name_chn, b.c_name, b.c_birthyear, b.c_deathyear, 
           d.c_dynasty_chn, b.c_female, b.c_index_year
    FROM BIOG_MAIN b
    JOIN DYNASTIES d ON b.c_dy = d.c_dy
    WHERE b.c_name_chn != '未詳'
    AND d.c_dynasty_chn IN ({dyn_placeholders})
    AND b.c_personid NOT IN (SELECT DISTINCT c_merged_from_personid FROM MERGED_PERSON_DATA)
    ORDER BY 
        CASE 
            WHEN b.c_birthyear > 0 AND b.c_deathyear > 0 THEN 1
            WHEN b.c_birthyear > 0 OR b.c_deathyear > 0 THEN 2
            WHEN b.c_index_year > 0 THEN 3
            ELSE 4
        END,
        b.c_birthyear, b.c_personid
""")

candidates = cursor.fetchall()
cursor.execute("SELECT c_personid, COUNT(*) FROM POSTING_DATA GROUP BY c_personid")
posting_counts = dict(cursor.fetchall())
conn.close()

print(f"// {len(candidates):,} total candidates from CBDB", file=sys.stderr)

# Track per-dynasty counts for Phase 3b LIMIT
dyn_counts = {d: 0 for d in ALL_DYNS}

seens = set()
entries = []
stats = {}

for row in candidates:
    personid, name_chn, name_en, birth, death, dynasty, female, index_year = row

    # Check LIMIT for Phase 3b dynasties
    if dynasty in PHASE3B_DYNS:
        limit = PHASE3B_DYNS[dynasty]
        if dyn_counts[dynasty] >= limit:
            continue

    name_simp = cc.convert(name_chn)
    if (name_chn in existing_names or name_simp in existing_names_simp
        or name_chn in seens or name_simp in seens):
        continue
    if len(name_chn) < 2:
        continue

    seens.add(name_chn)
    dyn_counts[dynasty] = dyn_counts.get(dynasty, 0) + 1

    region = DYN_REGION.get(dynasty, 'china')
    display_dyn = DYN_DISPLAY.get(dynasty, dynasty)
    stats[display_dyn] = stats.get(display_dyn, 0) + 1

    # Determine effective years
    has_birth = birth and birth > 0
    has_death = death and death > 0

    if not has_birth and not has_death and index_year and index_year > 0:
        birth = index_year
        has_birth = True
        is_approximate = True
    else:
        is_approximate = not (has_birth and has_death)

    # English name
    if not name_en or name_en == name_chn:
        name_display_en = ' '.join(lazy_pinyin(name_chn)).title()
    else:
        name_display_en = name_en

    pid = to_pinyin_id(name_chn, birth if has_birth else 0)
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

    # Year info
    if has_birth and has_death:
        year_info = f"{birth}—{death}年"
        year_info_en = f"{birth}–{death}"
        lived_info = f"生于{year_info}"
        lived_info_en = f"lived {year_info_en}"
    elif has_birth and not has_death:
        year_info = f"约{birth}年"
        year_info_en = f"c. {birth}"
        lived_info = f"约生于{birth}年"
        lived_info_en = f"born c. {birth}"
    elif not has_birth and has_death:
        year_info = f"?—{death}年"
        year_info_en = f"?–{death}"
        lived_info = f"卒于{death}年"
        lived_info_en = f"died {death}"
    else:
        year_info = "年代不详"
        year_info_en = "dates unknown"
        lived_info = ""
        lived_info_en = ""

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

    if lived_info:
        summary_zh = f"{period_name}时期{female_note}历史人物，{lived_info}{career_note}。其事迹见于相关史料记载。"
        summary_en = f"Historical figure of the {period_name} period{female_note_en}, {lived_info_en}{career_note_en}. Documented in historical sources."
    else:
        summary_zh = f"{period_name}时期{female_note}历史人物{career_note}。其事迹见于相关史料记载。"
        summary_en = f"Historical figure of the {period_name} period{female_note_en}{career_note_en}. Documented in historical sources."

    if is_approximate:
        desc_zh = f'{name_chn}（约{year_info}），{period_name}人物。{context_zh}关于其生平与事迹的记载，散见于相关史籍文献之中，反映了当时的历史风貌与社会环境。'
        desc_en = f'{name_chn} (c. {year_info_en}) was a figure of the {period_name} period. {context_en} Records of their life and deeds are preserved in historical texts and documents, reflecting the historical context and social environment of the era.'
    else:
        desc_zh = f'{name_chn}（{year_info}），{period_name}人物。{context_zh}关于其生平与事迹的记载，散见于相关史籍文献之中，反映了当时的历史风貌与社会环境。'
        desc_en = f'{name_chn} ({year_info_en}) was a figure of the {period_name} period. {context_en} Records of their life and deeds are preserved in historical texts and documents, reflecting the historical context and social environment of the era.'

    # Determine confidence
    if has_birth and has_death:
        confidence = 0.8  # Tier 1
    elif has_birth or has_death:
        confidence = 0.65  # Tier 2
    elif index_year and index_year > 0:
        confidence = 0.65  # Tier 3 (using index_year as approximation)
    else:
        confidence = 0.5  # No date at all

    entry = {
        "id": pid, "name": name_chn, "nameEn": name_display_en,
        "regionId": region, "occupations": occs,
        "tags": tags, "tagsEn": tags_en,
        "summary": summary_zh, "summaryEn": summary_en,
        "description": desc_zh, "descriptionEn": desc_en,
        "alternativeNames": [],
        "sourceIds": ["src-cbdb"],
        "wikidataQid": "",
        "dataStatus": "published",
        "confidenceScore": confidence,
        "externalReferences": [],
    }
    # Only include year fields if known
    if has_birth:
        entry["birthYear"] = birth
    if has_death:
        entry["deathYear"] = death

    entries.append(entry)

out_path = 'src/data/people/_rescueAndExpandPeople.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"\n✅ Phase 3: Written {len(entries):,} entries to {out_path}", file=sys.stderr)
print()

# Show Phase 3a results
print("=== Phase 3a: Rescue Dynasties ===", file=sys.stderr)
for dyn in PHASE3A_DYNS:
    display = DYN_DISPLAY.get(dyn, dyn)
    cnt = stats.get(display, 0)
    print(f"  {dyn:12s} ({display:4s}): {cnt:>6,} 人", file=sys.stderr)

# Show Phase 3b results
print("\n=== Phase 3b: Expand Dynasties ===", file=sys.stderr)
for dyn in PHASE3B_DYNS:
    display = DYN_DISPLAY.get(dyn, dyn)
    cnt = stats.get(display, 0)
    limit = PHASE3B_DYNS[dyn]
    print(f"  {dyn:12s} ({display:4s}): {cnt:>6,} 人 (limit: {limit:,})", file=sys.stderr)

# Quality breakdown
t1 = sum(1 for e in entries if e.get("birthYear") and e.get("deathYear"))
t2 = sum(1 for e in entries if (e.get("birthYear") or e.get("deathYear")) and not (e.get("birthYear") and e.get("deathYear")))
t3 = sum(1 for e in entries if not e.get("birthYear") and not e.get("deathYear"))
print(f"\n=== Quality ===", file=sys.stderr)
print(f"  Tier 1 (birth+death): {t1:,}", file=sys.stderr)
print(f"  Tier 2 (one year):    {t2:,}", file=sys.stderr)
print(f"  Tier 3 (no date):     {t3:,}", file=sys.stderr)
