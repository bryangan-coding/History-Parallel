#!/usr/bin/env python3
"""
修复 grand-timeline 中 32 条过短/空/损坏的 summary
策略：优先使用 GTL 原始数据的生卒年 + 手动映射表
"""
import json, glob, sys, os

PEOPLE_DIR = '/Users/bryangan/Documents/Projects/历史平行线/src/data/people'

# 手动映射表：name → (new_summary, [new_regionId, new_tags, new_occupations])
FIXES = {
    # === 年号格式 → 还原为有意义的摘要 ===
    '夏襄宗': (
        '西夏皇帝，夏仁宗之子。在位期间使用应天（1206-1209）等年号，继续与金朝修好。',
        'western-xia', ['皇帝', '政治人物'], ['monarch']
    ),
    '周静帝': (
        '北周末代皇帝，宇文赟之子。在位期间使用大象（579-580）年号，后被杨坚（隋文帝）篡位，北周亡。',
        'sui-dynasty', ['皇帝', '政治人物'], ['monarch']
    ),
    '慕容熙': (
        '后燕末代君主，慕容垂之孙。在位期间使用光始（401-406）等年号，因暴虐失民心而被杀。',
        'sixteen-kingdoms', ['皇帝', '政治人物'], ['monarch']
    ),
    '李势': (
        '成汉末代君主，李寿之子。在位期间使用太和（344-346）年号，后被东晋桓温所灭，成汉亡。',
        'sixteen-kingdoms', ['皇帝', '政治人物'], ['monarch']
    ),
    '石虎': (
        '后赵皇帝，石勒之侄。在位期间使用建武（335-348）等年号，以残暴著称，佛教在其治下得到发展。',
        'sixteen-kingdoms', ['皇帝', '政治人物'], ['monarch']
    ),
    '刘子业': (
        '南朝宋废帝，孝武帝刘骏之子。在位期间使用永光（465）等年号，以荒淫暴虐著称，后被弑杀。',
        'northern-southern-dynasties', ['皇帝', '政治人物'], ['monarch']
    ),
    '陈文帝': (
        '南朝陈第二位皇帝陈蒨，陈霸先之侄。在位期间使用天嘉（560-566）等年号，恢复江南经济，政治较为清明。',
        'northern-southern-dynasties', ['皇帝', '政治人物'], ['monarch']
    ),
    '魏孝庄帝': (
        '北魏皇帝元子攸，献文帝之孙。在位期间使用建义（528）等年号，在尔朱荣控制下短暂执政，后被弑。',
        'northern-southern-dynasties', ['皇帝', '政治人物'], ['monarch']
    ),
    '魏献文帝': (
        '北魏皇帝拓跋弘，文成帝之子。在位期间使用天安（466-467）等年号，后被文明太后鸩杀，由幼子孝文帝即位。',
        'northern-southern-dynasties', ['皇帝', '政治人物'], ['monarch']
    ),
    
    # === "子：女：" 损坏数据 → 重要历史人物 ===
    '宋光宗': (
        '南宋第三位皇帝赵惇，宋孝宗之子。在位期间朝政为皇后李氏与韩侂胄所掌控，晚年因精神疾病禅位于宁宗。',
        'song-dynasty', ['皇帝', '政治人物'], ['monarch']
    ),
    '宋孝宗': (
        '南宋第二位皇帝赵昚，宋太祖赵匡胤七世孙。在位期间为岳飞平反，发动隆兴北伐力图收复中原，被誉为南宋最有作为的皇帝。',
        'song-dynasty', ['皇帝', '政治人物'], ['monarch']
    ),
    '宋钦宗': (
        '北宋末代皇帝赵桓，宋徽宗之子。在位仅一年多即遭遇靖康之变，与徽宗一同被金人掳往北方，北宋灭亡。',
        'song-dynasty', ['皇帝', '政治人物'], ['monarch']
    ),
    
    # === 过短但可接受 ===
    '许奕': (
        '南宋政治人物，字成子，简州（今四川简阳）人。官至吏部侍郎，以直言敢谏著称。',
        'song-dynasty', ['政治人物'], ['politician']
    ),
    '朱伺': (
        '西晋将领，字仲文，安陆（今湖北安陆）人。陶侃部属，参与平定杜弢之乱。',
        'western-jin', ['军事人物'], ['general']
    ),
    '东方朔': (
        '西汉文学家、辞赋家。汉武帝时曾任常侍郎、太中大夫等职。以诙谐多智著称，代表作有《答客难》《非有先生论》等。',
        'han-dynasty', ['文学家', '政治人物'], ['poet', 'writer', 'politician']
    ),
    
    # === 空 summary ===
    '大希律王': (
        '犹太王国希律王朝的建立者，前37-前4年在位。以大规模建筑工程闻名，包括扩建第二圣殿。亦以多疑残暴著称。',
        'middle-east', ['政治人物'], ['politician']
    ),
    '莎乐美': (
        '希律王朝的犹太公主，希律·安提帕的继女。据《圣经》记载，因母亲唆使要求施洗约翰的头颅。西方艺术中常见题材。',
        'middle-east', ['政治人物'], ['politician']
    ),
}

# 未在 GTL 中找到的，需要在已加载的 JSON 中搜索并修复
MISSING_FIXES = {
    '乞伏炽磐': (
        '西秦皇帝，乞伏乾归之子。在位期间使用永康（412-419）等年号，灭南凉，与北凉、夏国争雄陇右。',
        'sixteen-kingdoms', ['皇帝', '政治人物'], ['monarch']
    ),
    '晋哀帝': (
        '东晋皇帝司马丕，晋成帝之子。在位期间使用隆和（362-363）等年号，崇信道教，因服食丹药中毒而死。',
        'eastern-jin', ['皇帝', '政治人物'], ['monarch']
    ),
    '晋成帝': (
        '东晋皇帝司马衍，晋明帝之子。在位期间使用咸和（326-334）等年号，幼年即位由庾太后临朝，庾亮、王导相继辅政。',
        'eastern-jin', ['皇帝', '政治人物'], ['monarch']
    ),
    '晋穆帝': (
        '东晋皇帝司马聃，晋康帝之子。在位期间使用永和（345-356）等年号，桓温北伐一度收复洛阳，是中国历史上最年轻的皇帝之一。',
        'eastern-jin', ['皇帝', '政治人物'], ['monarch']
    ),
    '石鉴': (
        '后赵皇帝，石虎之子。在位仅数月在太寧（349）年号间，旋即被石闵（冉闵）废弑。',
        'sixteen-kingdoms', ['皇帝', '政治人物'], ['monarch']
    ),
    '刘继元': (
        '北汉末代皇帝刘继恩之弟。在位期间使用天会（968-973）等年号，后因宋太宗亲征而降宋，北汉灭亡。',
        'ten-kingdoms', ['皇帝', '政治人物'], ['monarch']
    ),
}

def fix_short_summaries():
    files_modified = set()
    fixes_applied = 0
    
    for fp in sorted(glob.glob(f'{PEOPLE_DIR}/*.json')):
        with open(fp, encoding='utf-8') as f:
            data = json.load(f)
        
        modified = False
        for p in data:
            if 'src-grand-timeline' not in p.get('sourceIds', []):
                continue
            
            name = p['name']
            
            # Check manual fix table
            if name in FIXES:
                new_summary, new_region, new_tags, new_occ = FIXES[name]
                p['summary'] = new_summary
                p['regionId'] = new_region
                p['tags'] = new_tags
                p['occupations'] = new_occ
                modified = True
                fixes_applied += 1
                print(f"  Fixed: {name} → {new_region} ({len(new_summary)} chars)", file=sys.stderr)
            elif name in MISSING_FIXES:
                new_summary, new_region, new_tags, new_occ = MISSING_FIXES[name]
                p['summary'] = new_summary
                p['regionId'] = new_region
                p['tags'] = new_tags
                p['occupations'] = new_occ
                modified = True
                fixes_applied += 1
                print(f"  Fixed (missing): {name} → {new_region} ({len(new_summary)} chars)", file=sys.stderr)
        
        if modified:
            with open(fp, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            files_modified.add(fp)
    
    print(f"\n✅ Fixed {fixes_applied} entries across {len(files_modified)} files", file=sys.stderr)
    return files_modified

if __name__ == '__main__':
    fix_short_summaries()
