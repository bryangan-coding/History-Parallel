#!/usr/bin/env python3
"""
从 grand-timeline 导入各朝代数据
使用年份范围精确分类，与已有数据去重
"""
import json, re, sys, os, glob
from opencc import OpenCC

SRC_PATH = '/tmp/people-ancient-china.json'
OUT_DIR = '/Users/bryangan/Documents/Projects/历史平行线/src/data/people'
os.makedirs(OUT_DIR, exist_ok=True)

cc = OpenCC('t2s')

def parse_year(val):
    """解析年份，返回整数（BCE为负数），无效返回 None"""
    if not val or val in ('?', '不详', '', None):
        return None
    try:
        return int(val)
    except (ValueError, TypeError):
        nums = re.findall(r'\d+', str(val))
        if nums:
            year = int(nums[0])
            if '前' in str(val) or '－' in str(val):
                return -year
        return None

# 朝代年份范围 → 对应项目的 regionId
DYNASTY_MAP = {
    'han-dynasty':             (-202, 220),
    'qin-dynasty':             (-221, -206),
    'three-kingdoms':          (220, 280),
    'sixteen-kingdoms':       (304, 439),
    'sui-dynasty':             (581, 618),
    'northern-southern-dynasties': (420, 589),
    'western-xia':             (1038, 1227),
    'liao-dynasty':            (916, 1125),
    'jin-dynasty-period':      (1115, 1234),
}

# tags → occupations 映射（英文）
OCC_MAP = {
    '皇帝':       ['monarch'],
    '军事人物':   ['general'],
    '文学家':     ['poet', 'writer'],
    '学者':       ['scholar'],
    '政治人物':   ['politician'],
}

def classify_by_years(born, died):
    """根据生卒年返回 regionId，无法判断返回 None"""
    year = died if died is not None else born
    if year is None:
        return None
    for rid, (start, end) in DYNASTY_MAP.items():
        if start <= year <= end:
            return rid
    return None

def load_existing_names():
    """加载所有已有客户端人物姓名（去重用）"""
    existing = set()
    for fp in glob.glob(os.path.join(OUT_DIR, '*.json')):
        try:
            with open(fp, encoding='utf-8') as f:
                for p in json.load(f):
                    existing.add(p['name'])
        except Exception as e:
            print(f"  Warning reading {fp}: {e}", file=sys.stderr)
    return existing

print("Loading grand-timeline data...", file=sys.stderr)
with open(SRC_PATH, encoding='utf-8') as f:
    src_data = json.load(f)
print(f"  Source entries: {len(src_data):,}", file=sys.stderr)

existing_names = load_existing_names()
print(f"  Existing names (dedup): {len(existing_names):,}", file=sys.stderr)

# 分类存储
classified = {rid: [] for rid in DYNASTY_MAP.keys()}
skipped_no_year = 0
skipped_dup = 0
skipped_out_of_range = 0

for name, entry in src_data.items():
    if name in existing_names:
        skipped_dup += 1
        continue

    born = parse_year(entry.get('born', '?'))
    died = parse_year(entry.get('died', '?'))

    rid = classify_by_years(born, died)
    if rid is None:
        skipped_out_of_range += 1
        continue

    # 生成 ID（拼音）
    name_simp = cc.convert(name)
    pinyin_id = name_simp

    # 摘要处理（CC BY-SA 合规：截取前 80 字符）
    summary = entry.get('summary', '')
    summary_clean = summary[:80] + ('...' if len(summary) > 80 else '')

    # 根据 summary 自动判断 tags
    tags = []
    s = summary
    if any(kw in s for kw in ['将军', '将领', '率军', '征战', '兵法']):
        tags.append('军事人物')
    if any(kw in s for kw in ['诗人', '文学', '著有', '文集', '书法', '绘画']):
        tags.append('文学家')
    if any(kw in s for kw in ['皇帝', '武帝', '文帝', '景帝', '太祖', '高祖']):
        tags.append('皇帝')
    if any(kw in s for kw in ['丞相', '尚书', '刺史', '太守', '县令', '谏议']):
        tags.append('政治人物')
    if any(kw in s for kw in ['学者', '经学', '注', '传', '论语', '周易', '著']):
        tags.append('学者')
    if not tags:
        tags = ['政治人物']

    # 根据 tags 推导 occupations（英文）
    occupations = []
    for t in tags:
        if t in OCC_MAP:
            for o in OCC_MAP[t]:
                if o not in occupations:
                    occupations.append(o)
    if not occupations:
        occupations = ['politician']

    # 构建 person 对象 —— 仅当值非 None 时才添加年份字段
    person = {
        "id": pinyin_id,
        "name": name_simp,
        "alternativeNames": [name] if name != name_simp else [],
        "regionId": rid,
        "occupations": occupations,
        "tags": list(dict.fromkeys(tags)),  # 去重保持顺序
        "summary": summary_clean,
        "sourceIds": ["src-grand-timeline"],
        "dataStatus": "imported",
        "confidenceScore": 0.65,
        "externalReferences": []
    }
    if born is not None:
        person["birthYear"] = born
    if died is not None:
        person["deathYear"] = died

    classified[rid].append(person)

print(f"\n✅ Classification complete", file=sys.stderr)
print(f"   Skipped duplicates: {skipped_dup}", file=sys.stderr)
print(f"   Skipped out of range: {skipped_out_of_range}", file=sys.stderr)

# 写 JSON 文件
FILE_NAME_MAP = {
    'han-dynasty':                  '_hanDynastyPeople.json',
    'qin-dynasty':                  '_qinDynastyPeople.json',
    'three-kingdoms':              '_threeKingdomsPeople.json',
    'sixteen-kingdoms':           '_sixteenKingdomsPeople.json',
    'sui-dynasty':                 '_suiDynastyPeople.json',
    'northern-southern-dynasties': '_northernSouthernDynastiesPeople.json',
    'western-xia':                 '_westernXiaPeople.json',
    'liao-dynasty':                '_liaoDynastyPeople.json',
    'jin-dynasty-period':          '_jinDynastyPeriodPeople.json',
}

total_written = 0
for rid, people in classified.items():
    if not people:
        continue
    fname = FILE_NAME_MAP.get(rid, f"_{rid}People.json")
    out_path = os.path.join(OUT_DIR, fname)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(people, f, ensure_ascii=False, indent=2)
    print(f"  {rid:35s}: {len(people):>6,} 人 → {fname}", file=sys.stderr)
    total_written += len(people)

print(f"\n✅ Total written: {total_written:,} new entries", file=sys.stderr)
print(f"   Output directory: {OUT_DIR}", file=sys.stderr)
