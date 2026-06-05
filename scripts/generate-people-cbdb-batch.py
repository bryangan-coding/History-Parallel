#!/usr/bin/env python3
"""Generate person entries from CBDB SQLite database — CC-friendly, no direct CBDB references.
Adapted for new CBDB schema (BIOG_MAIN, DYNASTIES, POSTING_DATA, etc.)

Usage:
  python3 scripts/generate-people-cbdb-batch.py --batch-size 5000 --offset 0 > /tmp/cbdb_batch.ts
"""
import sqlite3, re, sys, argparse, os
from pypinyin import lazy_pinyin, Style
from opencc import OpenCC

cc = OpenCC('t2s')  # traditional → simplified converter

parser = argparse.ArgumentParser()
parser.add_argument('--batch-size', type=int, default=5000)
parser.add_argument('--offset', type=int, default=0)
parser.add_argument('--db', default='/tmp/cbdb_20260530.sqlite3')
parser.add_argument('--mockdata', default='src/data/mockData.ts')
args = parser.parse_args()

def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")

def to_pinyin_id(name, birth):
    """Generate pinyin-based ID like 'chen-zhizhong-990'"""
    py = lazy_pinyin(name, style=Style.TONE3)
    # Convert tone numbers to normal pinyin without tones
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

# Dynasty descriptions (period context, no CBDB references)
DYNASTY_CONTEXT = {
    '唐': '唐代（618—907年）是中国历史上文化繁荣、国力强盛的时期，诗歌、书法、绘画等艺术达到高峰。',
    '宋': '宋代（960—1279年）是中国历史上经济文化高度发达的时期，理学兴起，科举制度完善，市民文化繁荣。',
    '元': '元代（1271—1368年）是中国历史上疆域最广的时期之一，民族融合加强，戏曲、书画等艺术蓬勃发展。',
    '明': '明代（1368—1644年）是中国历史上中央集权强化、商品经济蓬勃发展的时期，市井文化兴起。',
    '清': '清代（1644—1912年）是中国历史上最后一个封建王朝，前期国力强盛，晚期面临内忧外患与社会变革。',
    '隋': '隋代（581—618年）虽短暂但意义重大，开创科举制度，修建大运河，为唐代繁荣奠定基础。',
}

DYNASTY_CONTEXT_EN = {
    '唐': 'The Tang dynasty (618–907) was a period of cultural flourishing and national strength, with poetry, calligraphy, and painting reaching their zenith.',
    '宋': 'The Song dynasty (960–1279) was a highly developed period in Chinese economic and cultural history, marked by the rise of Neo-Confucianism, the perfection of the civil examination system, and the prosperity of urban culture.',
    '元': 'The Yuan dynasty (1271–1368) was one of the largest empires in Chinese history, characterized by enhanced ethnic integration and the flourishing of drama, calligraphy, and painting.',
    '明': 'The Ming dynasty (1368–1644) was a period of strengthened centralization and thriving commercial economy, with the rise of popular urban culture.',
    '清': 'The Qing dynasty (1644–1912) was the last imperial dynasty in Chinese history, with strong national power in its early period and internal and external challenges in its later years.',
    '隋': 'The Sui dynasty (581–618) was brief but significant, establishing the civil examination system and building the Grand Canal, laying the foundation for Tang prosperity.',
}

# Dynasty → regionId mapping
DYN_REGION = {
    '唐': 'tang-dynasty', '宋': 'song-dynasty', '元': 'yuan-dynasty',
    '明': 'ming-dynasty', '清': 'qing-dynasty', '隋': 'sui-dynasty',
    '漢': 'han-dynasty', '西汉': 'han-dynasty', '东汉': 'han-dynasty',
    '西漢': 'han-dynasty', '東漢': 'han-dynasty',
    '三國': 'three-kingdoms', '三國魏': 'three-kingdoms',
    '三國吳': 'three-kingdoms', '三國蜀': 'three-kingdoms',
    '南北朝': 'china', '隋': 'sui-dynasty',
    '秦': 'qin-dynasty', '周': 'china',
}

# Load existing names from mockData.ts
with open(args.mockdata) as f:
    content = f.read()

people_section = content[content.find('export const _peoplePart1'):content.find('export const events')]
existing_names = set()
existing_names_simp = set()  # Simplified version for cross-matching
for m in re.finditer(r"name:\s*'([^']+)'", people_section):
    name = m.group(1)
    existing_names.add(name)
    existing_names_simp.add(cc.convert(name))

# Also track existing IDs to avoid collisions
existing_ids = set()
for m in re.finditer(r"id:\s*'([^']+)'", people_section):
    existing_ids.add(m.group(1))

print(f"// Existing names: {len(existing_names)}, IDs: {len(existing_ids)}",
      file=sys.stderr)

# Connect to CBDB
conn = sqlite3.connect(args.db)
cursor = conn.cursor()

# Get merged person IDs to skip
cursor.execute("SELECT DISTINCT c_merged_from_personid FROM MERGED_PERSON_DATA")
merged_ids = set(row[0] for row in cursor.fetchall())
print(f"// Merged IDs to skip: {len(merged_ids)}", file=sys.stderr)

# Major dynasties prioritized
major_dynasties = list(DYN_REGION.keys())
dyn_placeholders = ','.join([f"'{d}'" for d in major_dynasties])

# Query candidates with birth+death years, not merged, major dynasties
cursor.execute(f"""
    SELECT b.c_personid, b.c_name_chn, b.c_name, b.c_birthyear, b.c_deathyear, 
           d.c_dynasty_chn, b.c_female
    FROM BIOG_MAIN b
    JOIN DYNASTIES d ON b.c_dy = d.c_dy
    WHERE b.c_birthyear > 0 
    AND b.c_deathyear > 0
    AND b.c_name_chn != '未詳'
    AND d.c_dynasty_chn IN ({dyn_placeholders})
    AND b.c_personid NOT IN (SELECT DISTINCT c_merged_from_personid FROM MERGED_PERSON_DATA)
    ORDER BY b.c_personid
""")

# Fetch all candidates into memory first (before running other queries on the cursor)
candidates = cursor.fetchall()

# For efficiency, also fetch posting counts in bulk
cursor.execute("SELECT c_personid, COUNT(*) FROM POSTING_DATA GROUP BY c_personid")
posting_counts = dict(cursor.fetchall())

# Filter and generate
generated = 0
seen_names = set()
batch_start = args.offset
batch_end = args.offset + args.batch_size

print(f"""// Auto-generated historical figures — data sourced from historical records, transformed for CC BY-SA 4.0 compliance
// Batch: {args.batch_size} entries (offset {args.offset})
// Database: cbdb_20260530.sqlite3
export const _cbdb_batch_{args.offset} = [""")

entries = []
for row in candidates:
    personid, name_chn, name_en, birth, death, dynasty, female = row
    
    # Convert to simplified for matching (CBDB uses traditional)
    name_simp = cc.convert(name_chn)
    
    # Skip if already in our system (check both traditional and simplified)
    if (name_chn in existing_names or name_simp in existing_names_simp 
        or name_chn in seen_names or name_simp in seen_names):
        continue
    if len(name_chn) < 2:
        continue
    
    # Offset/batch filtering (only count new, non-duplicate candidates)
    seen_names.add(name_chn)
    generated += 1
    
    if generated <= batch_start:
        continue
    if generated > batch_end:
        break
    
    # Map region
    region = DYN_REGION.get(dynasty, 'china')
    
    # Name for English display
    if not name_en or name_en == name_chn:
        # Generate pinyin for English name
        py = lazy_pinyin(name_chn)
        name_display_en = ' '.join(py).title()
    else:
        name_display_en = name_en
    
    # Generate pinyin ID
    pid = to_pinyin_id(name_chn, birth)
    # Ensure uniqueness
    base_pid = pid
    suffix = 1
    while pid in existing_ids:
        suffix += 1
        pid = f"{base_pid}-{suffix}"
    existing_ids.add(pid)
    
    # Posting count
    num_postings = posting_counts.get(personid, 0)
    
    # Tags and occupations
    tags = []
    tags_en = []
    occs = []
    
    if num_postings >= 10:
        tags.append('官员')
        tags_en.append('Official')
        occs.append('官员')
    elif num_postings >= 3:
        tags.append('官员')
        tags_en.append('Official')
        occs.append('官员')
    
    if dynasty in ['唐', '宋'] and num_postings >= 5:
        tags.insert(0, '文人')
        tags_en.insert(0, 'Scholar-Official')
        if '文人' not in occs:
            occs.insert(0, '文人')
    
    # Add dynasty tag
    tags.insert(0, dynasty)
    tags_en.insert(0, dynasty)
    
    if not occs:
        occs.append('历史人物')
    
    # Generate CC-friendly summary (no CBDB references)
    period = dynasty
    
    birth_str = str(birth) if birth else '不详'
    death_str = str(death) if death else '不详'
    
    if num_postings >= 20:
        career_note = "，仕途显达"
        career_note_en = ", held numerous official positions"
    elif num_postings >= 5:
        career_note = "，有仕宦经历"
        career_note_en = ", held official positions"
    else:
        career_note = ""
        career_note_en = ""
    
    summary_zh = f"{period}时期{'女性' if female else ''}历史人物，生于{name_chn}（{birth_str}—{death_str}年）{career_note}。其事迹见于相关史料记载。"
    summary_en = f"Historical figure of the {period} dynasty{' (female)' if female else ''}, lived {birth_str}–{death_str}{career_note_en}. Documented in historical sources."
    
    # Description with dynasty context
    context_zh = DYNASTY_CONTEXT.get(dynasty, f'{dynasty}是中国历史上的重要时期。')
    context_en = DYNASTY_CONTEXT_EN.get(dynasty, f'The {dynasty} dynasty was an important period in Chinese history.')
    
    desc_zh = f'{name_chn}（{birth_str}—{death_str}年），{dynasty}人物。{context_zh}关于其生平与事迹的记载，散见于相关史籍文献之中，反映了当时的历史风貌与社会环境。'
    desc_en = f'{name_chn} ({birth_str}–{death_str}) was a figure of the {dynasty} dynasty. {context_en} Records of their life and deeds are preserved in historical texts and documents, reflecting the historical context and social environment of the era.'
    
    entry = f"""  {{
    id: '{pid}',
    name: '{esc(name_chn)}',
    nameEn: '{esc(name_display_en)}',
    birthYear: {birth},
    deathYear: {death},
    regionId: '{region}',
    occupations: [{', '.join(f"'{o}'" for o in occs)}],
    tags: [{', '.join(f"'{t}'" for t in tags)}],
    tagsEn: [{', '.join(f"'{t}'" for t in tags_en)}],
    summary: '{esc(summary_zh)}',
    summaryEn: '{esc(summary_en)}',
    description: '{esc(desc_zh)}',
    descriptionEn: '{esc(desc_en)}',
    alternativeNames: [],
    sourceIds: ['src-cbdb'],
    wikidataQid: '',
    dataStatus: 'published',
    confidenceScore: 0.65,
    externalReferences: [],
  }},"""
    entries.append(entry)

conn.close()

# Output
print('\n'.join(entries))
print("];")
print(f"\n// Generated {len(entries)} entries", file=sys.stderr)
