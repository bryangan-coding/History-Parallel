#!/usr/bin/env python3
"""
CBDB 条目合规处理脚本

将 mockData.ts 中的 cbdb-N 条目转换为 CC BY-SA 4.0 兼容格式：
1. 重命名 ID (cbdb-N → 姓名拼音+生卒年)
2. 去除 summary/description 中的 "CBDB" 直接引用
3. 生成原创历史叙述（基于姓名、朝代、生卒年等事实信息）
4. 添加 sourceIds: ['src-cbdb']
5. 降低 confidenceScore 为 0.65（自动生成）

处理原则：
- 只提取历史事实（姓名、生卒年、朝代归属）——无版权
- 原创文本生成——不复制 CBDB 描述性文字
- 模板化描述基于历史时期特征，为后续人工优化留出空间
"""

import re
import sys
import json
from pathlib import Path
from pypinyin import pinyin, Style

PROJECT_ROOT = Path(__file__).parent.parent
MOCKDATA_PATH = PROJECT_ROOT / "src" / "data" / "mockData.ts"

# Occupation English translations for ID/summary purposes
OCCUPATION_EN = {
    '政治家': 'statesman',
    '文学家': 'writer',
    '学者': 'scholar',
    '军事家': 'military',
    '书法家': 'calligrapher',
    '画家': 'painter',
    '诗人': 'poet',
    '哲学家': 'philosopher',
    '科学家': 'scientist',
    '医学家': 'physician',
    '女性': 'woman',
    '宋': 'Song',
    '唐': 'Tang',
    '元': 'Yuan',
    '明': 'Ming', 
    '清': 'Qing',
}

def get_pinyin(name):
    """Get pinyin from Chinese name using pypinyin library"""
    if not name:
        return 'unknown'
    # pypinyin returns list of lists, join tones without numbers
    result = pinyin(name, style=Style.NORMAL)
    # Join: for compound surnames, keep hyphenated
    parts = []
    for py_list in result:
        p = py_list[0]  # Take first pronunciation
        parts.append(p)
    return '-'.join(parts)

def generate_id(name, birth_year, existing_ids):
    """Generate a unique ID from name + birth year"""
    base = get_pinyin(name)
    if birth_year and birth_year not in ('undefined', 'null', None):
        pid = f'{base}-{birth_year}'
    else:
        pid = base
    
    # Ensure uniqueness
    if pid in existing_ids:
        for suffix in range(2, 100):
            candidate = f'{pid}-{suffix}'
            if candidate not in existing_ids:
                return candidate
    return pid

# Dynasty context mapping for generating descriptions
DYNASTY_CONTEXT = {
    'tang-dynasty': {
        'zh': '唐代（618—907年）是中国历史上文化繁荣、国力强盛的时期。',
        'en': 'The Tang dynasty (618–907) was a period of cultural flourishing and national strength in Chinese history.',
        'era_zh': '唐代',
        'era_en': 'the Tang dynasty',
    },
    'song-dynasty': {
        'zh': '宋代（960—1279年）是中国历史上文治兴盛、科技发展的时期。',
        'en': 'The Song dynasty (960–1279) was a period of civil governance, cultural achievement, and technological advancement in Chinese history.',
        'era_zh': '宋代',
        'era_en': 'the Song dynasty',
    },
    'yuan-dynasty': {
        'zh': '元代（1271—1368年）是中国历史上民族融合、东西交流空前活跃的时期。',
        'en': 'The Yuan dynasty (1271–1368) was a period of unprecedented cultural exchange between East and West in Chinese history.',
        'era_zh': '元代',
        'era_en': 'the Yuan dynasty',
    },
    'ming-dynasty': {
        'zh': '明代（1368—1644年）是中国历史上中央集权强化、商品经济蓬勃发展的时期。',
        'en': 'The Ming dynasty (1368–1644) was a period of centralized governance and thriving commercial economy in Chinese history.',
        'era_zh': '明代',
        'era_en': 'the Ming dynasty',
    },
    'qing-dynasty': {
        'zh': '清代（1644—1912年）是中国最后一个封建王朝，经历了由盛转衰的历史进程。',
        'en': 'The Qing dynasty (1644–1912) was the last imperial dynasty of China, witnessing the transition from prosperity to decline.',
        'era_zh': '清代',
        'era_en': 'the Qing dynasty',
    },
}

OCCUPATION_DESC = {
    '政治家': {'zh': '在政坛上扮演了重要角色', 'en': 'played an important role in government and politics'},
    '文学家': {'zh': '在文学创作上有所成就', 'en': 'made contributions to literature'},
    '学者': {'zh': '在学术领域有深入研究', 'en': 'engaged in scholarly pursuits'},
    '军事家': {'zh': '在军事方面有所建树', 'en': 'made contributions to military affairs'},
    '书法家': {'zh': '以书法闻名于世', 'en': 'was renowned for calligraphy'},
    '画家': {'zh': '在绘画艺术上有卓越成就', 'en': 'achieved distinction in painting'},
    '诗人': {'zh': '创作了大量诗词作品', 'en': 'produced a substantial body of poetic works'},
    '哲学家': {'zh': '在思想领域产生了深远影响', 'en': 'had a profound influence on philosophical thought'},
    '科学家': {'zh': '在科学技术方面取得了重要成就', 'en': 'made important achievements in science and technology'},
    '医学家': {'zh': '在医学方面有突出贡献', 'en': 'made notable contributions to medicine'},
}

def generate_summary(name, dynasty, occupations, tags, birth_year, death_year):
    """Generate original summary based on facts only"""
    ctx = DYNASTY_CONTEXT.get(dynasty, {'era_zh': '中国历史', 'era_en': 'Chinese history'})
    era_zh = ctx['era_zh']
    era_en = ctx['era_en']
    
    # Build role description
    role_parts_zh = []
    role_parts_en = []
    for occ in occupations[:3]:
        if occ in OCCUPATION_DESC:
            role_parts_zh.append(occ)
            role_parts_en.append(OCCUPATION_EN.get(occ, occ))
    
    if not role_parts_zh and tags:
        for tag in tags:
            if tag in OCCUPATION_DESC:
                role_parts_zh.append(tag)
                role_parts_en.append(OCCUPATION_EN.get(tag, tag))
    
    role_zh = '、'.join(role_parts_zh[:2]) if role_parts_zh else '重要人物'
    role_en = ', '.join(role_parts_en[:2]) if role_parts_en else 'important figure'
    
    summary_zh = f'{era_zh}{role_zh}。生平记载于相关史料文献中。'
    summary_en = f'{era_en} {role_en}. Documented in relevant historical sources.'
    
    return summary_zh, summary_en

def generate_description(name, dynasty, occupations, tags, birth_year, death_year):
    """Generate original description based on factual information"""
    ctx = DYNASTY_CONTEXT.get(dynasty, {
        'zh': '中国历史上的重要时期。',
        'en': 'an important period in Chinese history.',
        'era_zh': '中国历史',
        'era_en': 'Chinese history'
    })
    
    era_zh = ctx['era_zh']
    era_en = ctx['era_en']
    context_zh = ctx.get('zh', '')
    context_en = ctx.get('en', '')
    
    # Life dates
    life_str = ''
    if birth_year and birth_year not in ('undefined', 'null', None):
        life_str = str(birth_year)
    if death_year and death_year not in ('undefined', 'null', None):
        life_str += f'\u2014{death_year}'
    
    dates_zh = f'\uff08{life_str}\u5e74\uff09' if life_str else ''
    dates_en = f' ({life_str})' if life_str else ''
    
    # Roles - Chinese
    roles = occupations if occupations else [t for t in tags if t in OCCUPATION_DESC]
    role_zh = '\u3001'.join(roles[:3]) if roles else '历史人物'
    
    # Roles - English
    role_en_parts = [OCCUPATION_EN.get(r, r) for r in (roles[:3] if roles else ['historical figure'])]
    role_en = ', '.join(role_en_parts)
    
    # Build description
    desc_zh = f'{name}{dates_zh}\uff0c{era_zh}{role_zh}\u3002' 
    desc_zh += f'{context_zh}\u5176\u751f\u5e73\u4e8b\u8ff9\u89c1\u4e8e\u76f8\u5173\u53f2\u6599\u8bb0\u8f7d\u3002'
    
    desc_en = f'{name}{dates_en} was a {role_en} of {era_en}. '
    desc_en += f'{context_en} Their life and activities are recorded in relevant historical sources.'
    
    return desc_zh, desc_en


def process_cbdb_entries(dry_run=False):
    """Main processing function"""
    with open(MOCKDATA_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Backup the content for diff
    original = content
    
    # Find all cbdb- entries (including cbdb-N-suffix variants like cbdb-1-2)
    cbdb_pattern = re.compile(r"id: 'cbdb-(\d+(?:-\d+)*)'")
    cbdb_entries = list(cbdb_pattern.finditer(content))
    
    if not cbdb_entries:
        print("No cbdb- entries found!")
        return
    
    print(f"Found {len(cbdb_entries)} cbdb- entries to process")
    
    # Extract all existing person IDs for collision checking
    people_section_start = content.find("export const people")
    people_section_start_2 = content.find("export const _peoplePart1")
    events_start = content.find("export const events")
    
    # Get all IDs from person sections
    if people_section_start_2 != -1:
        search_start = people_section_start_2
    elif people_section_start != -1:
        search_start = people_section_start
    else:
        print("Cannot find people section!")
        return
    
    all_ids = set()
    id_pattern = re.compile(r"id: '([^']+)'")
    
    # Collect ALL existing person IDs
    for m in id_pattern.finditer(content[search_start:events_start]):
        all_ids.add(m.group(1))
    
    # Also check _peoplePart1 if split
    if people_section_start_2 != -1:
        part1_end = content.find("export const _peoplePart2", people_section_start_2)
        if part1_end == -1:
            part1_end = events_start
        for m in id_pattern.finditer(content[people_section_start_2:part1_end]):
            all_ids.add(m.group(1))
    
    print(f"Existing unique person IDs: {len(all_ids)}")
    
    # Process entries in reverse to maintain positions
    replacements = []
    stats = {'renamed': 0, 'desc_updated': 0, 'summary_updated': 0, 'source_added': 0, 'confidence_updated': 0}
    
    # First pass: collect all entries and their boundaries
    entries = []
    for match in cbdb_entries:
        id_start = match.start()
        # Find the opening brace of this entry
        brace_start = content.rfind('{', 0, id_start)
        if brace_start == -1:
            continue
        # Find the closing brace (balanced)
        depth = 0
        brace_end = brace_start
        for i in range(brace_start, len(content)):
            c = content[i]
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
            if depth == 0:
                brace_end = i + 1
                break
        entry_text = content[brace_start:brace_end]
        entries.append((brace_start, brace_end, entry_text, match.group(1)))
    
    # Process from end to start to preserve positions
    for brace_start, brace_end, entry_text, cbdb_num in reversed(entries):
        modified = entry_text
        
        # Extract fields
        name_match = re.search(r"name:\s*'([^']*)'", modified)
        name = name_match.group(1) if name_match else 'unknown'
        
        birth_match = re.search(r"birthYear:\s*([^,\n]+)", modified)
        birth_year = birth_match.group(1).strip() if birth_match else None
        if birth_year in ('undefined', 'null'):
            birth_year = None
        
        death_match = re.search(r"deathYear:\s*([^,\n]+)", modified)
        death_year = death_match.group(1).strip() if death_match else None
        if death_year in ('undefined', 'null'):
            death_year = None
        
        region_match = re.search(r"regionId:\s*'([^']*)'", modified)
        region_id = region_match.group(1) if region_match else 'china'
        
        old_id = f'cbdb-{cbdb_num}'
        
        # Extract occupations and tags
        occ_match = re.search(r"occupations:\s*\[([^\]]*)\]", modified)
        occupations = []
        if occ_match:
            occ_text = occ_match.group(1)
            occupations = re.findall(r"'([^']*)'", occ_text)
        
        tag_match = re.search(r"tags:\s*\[([^\]]*)\]", modified)
        tags = []
        if tag_match:
            tag_text = tag_match.group(1)
            tags = re.findall(r"'([^']*)'", tag_text)
        
        # 1. Generate new ID
        new_id = generate_id(name, birth_year, all_ids)
        if new_id != old_id:
            # Replace only the cbdb-N id, not other occurrences
            modified = re.sub(r"id:\s*'cbdb-" + re.escape(cbdb_num) + r"'", f"id: '{new_id}'", modified)
            all_ids.add(new_id)
            stats['renamed'] += 1
        
        # 2. Replace summary - always regenerate for cbdb entries
        summary_zh, summary_en = generate_summary(name, region_id, occupations, tags, birth_year, death_year)
        
        # Replace summary (Chinese)
        modified = re.sub(
            r"summary:\s*'[^']*'",
            f"summary: '{summary_zh}'",
            modified, count=1
        )
        stats['summary_updated'] += 1
        
        # Replace summaryEn (English)
        modified = re.sub(
            r"summaryEn:\s*'[^']*'",
            f"summaryEn: '{summary_en}'",
            modified, count=1
        )
        
        # 3. Replace description - always regenerate for cbdb entries
        desc_zh, desc_en = generate_description(name, region_id, occupations, tags, birth_year, death_year)
        
        modified = re.sub(
            r"description:\s*'[^']*'",
            f"description: '{desc_zh}'",
            modified, count=1
        )
        stats['desc_updated'] += 1
        
        modified = re.sub(
            r"descriptionEn:\s*'[^']*'",
            f"descriptionEn: '{desc_en}'",
            modified, count=1
        )
        
        # 4. Add sourceIds
        if "sourceIds: []" in modified or "sourceIds: [" not in modified:
            modified = re.sub(r"sourceIds:\s*\[\s*\]", "sourceIds: ['src-cbdb']", modified)
            stats['source_added'] += 1
        
        # 5. Lower confidence score
        if "confidenceScore: 0.75" in modified:
            modified = modified.replace("confidenceScore: 0.75", "confidenceScore: 0.65")
            stats['confidence_updated'] += 1
        
        replacements.append((brace_start, brace_end, modified))
    
    # Apply replacements from end to start (so positions remain valid)
    new_content = content
    # Sort by position, apply from end to start
    for brace_start, brace_end, modified in sorted(replacements, key=lambda x: x[0], reverse=True):
        new_content = new_content[:brace_start] + modified + new_content[brace_end:]
    
    if dry_run:
        print("\n=== DRY RUN - No changes written ===")
        print(f"Stats: {stats}")
        # Show a sample entry
        if replacements:
            print("\n=== Sample processed entry ===")
            print(replacements[-1][2][:600])
        return
    
    # Write back
    with open(MOCKDATA_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n=== Processing Complete ===")
    print(f"IDs renamed: {stats['renamed']}")
    print(f"Summaries updated: {stats['summary_updated']}")
    print(f"Descriptions updated: {stats['desc_updated']}")
    print(f"Source IDs added: {stats['source_added']}")
    print(f"Confidence scores updated: {stats['confidence_updated']}")
    print(f"Total entries processed: {len(replacements)}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Clean CBDB entries in mockData.ts')
    parser.add_argument('--dry-run', '-d', action='store_true', help='Preview changes without writing')
    args = parser.parse_args()
    
    process_cbdb_entries(dry_run=args.dry_run)


if __name__ == '__main__':
    main()
