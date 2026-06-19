#!/usr/bin/env python3
"""
Phase 4: 为唐宋元明清重要人物生成深度多事件生平
基于二十四史等正史来源，每人生平拆分为3-8个关键事件节点
"""
import json, os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'data', 'events')
os.makedirs(OUTPUT_DIR, exist_ok=True)

all_events = []

def add(id, title, titleEn, startYear, endYear=None, importance=3,
        summary='', summaryEn='', desc='', descEn='', tags=None, tagsEn=None,
        personIds=None, regionId='', sourceIds=None, isApprox=False,
        placeName=None, placeNameEn=None, coords=None):
    all_events.append({
        'id': id, 'title': title, 'titleEn': titleEn,
        'startYear': startYear, 'endYear': endYear,
        'importance': importance,
        'summary': summary, 'summaryEn': summaryEn,
        'description': desc if desc else summary,
        'descriptionEn': descEn if descEn else summaryEn,
        'tags': tags or [], 'tagsEn': tagsEn or [],
        'personIds': personIds or [], 'regionId': regionId,
        'sourceIds': sourceIds or [], 'relatedEventIds': [],
        'datePrecision': 'year', 'isApproximate': isApprox,
        'dataStatus': 'published', 'confidenceScore': 0.9,
        'externalReferences': [],
        'placeName': placeName, 'placeNameEn': placeNameEn,
        'coordinates': coords,
    })

# Source abbreviations
SS = ['src-xintangshu']     # 新唐书
JS = ['src-jiutangshu']     # 旧唐书  
SOS = ['src-ss']            # 宋史
YS = ['src-yuanshi']        # 元史
MS = ['src-mingshi']        # 明史
QS = ['src-qingshigao']     # 清史稿
ZZTJ = ['src-zztj']         # 资治通鉴

# ================================================================
# TANG DYNASTY
# ================================================================

# 高力士 (684-762) - 唐代最著名的宦官
add('evt-gaolishi-castration', '高力士入宫为宦官', 'Gao Lishi Enters the Palace as a Eunuch', 693, importance=3,
    summary='高力士原名冯元一，岭南豪族出身。因父罪被抄家，年未满十岁受宫刑入宫。',
    summaryEn='Born Feng Yuanyi to a powerful Lingnan family, he was castrated and entered palace service before age ten after his father was convicted.',
    desc='高力士本名冯元一，先祖为北燕皇族长乐冯氏，曾祖冯盎为岭南高州豪酋。年未满十岁时因父罪被抄家，受宫刑入宫。虽为宦官，但在内廷学文习武，射箭百发百中，人称「冯力士」。',
    tags=['早年', '宦官', '唐朝'], tagsEn=['Early Life', 'Eunuch', 'Tang Dynasty'],
    personIds=['gao-li-shi-684'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

add('evt-gaolishi-xuanzong', '高力士辅佐唐玄宗', 'Gao Lishi Serves Emperor Xuanzong', 710, 760, importance=5,
    summary='高力士参与唐隆政变，深得唐玄宗信任，成为唐代权势最大的宦官。四方奏表先经其手再呈皇帝。',
    summaryEn='Gao Lishi participated in the Tanglong Coup and became Emperor Xuanzong\'s most trusted eunuch, handling all memorials before they reached the emperor.',
    desc='高力士参与710年唐隆政变诛杀韦后，深得唐玄宗信任。开元天宝年间权倾朝野——四方奏表先经其手再呈皇帝，小事可自行裁决。太子呼其为「二兄」，诸王公主称其为「阿翁」，驸马辈称其为「爷」。但他为人谨慎忠诚，始终未越权篡政。',
    tags=['政治', '宦官', '唐朝'], tagsEn=['Politics', 'Eunuch', 'Tang Dynasty'],
    personIds=['gao-li-shi-684', 'tang-xuanzong'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

add('evt-gaolishi-exile', '高力士被流放', 'Gao Lishi Exiled', 760, importance=4,
    summary='安史之乱后高力士随玄宗返长安，后被宦官李辅国陷害流放巫州。',
    summaryEn='After the An Lushan Rebellion, Gao Lishi was framed by eunuch Li Fuguo and exiled to Wuzhou.',
    desc='安史之乱中高力士随玄宗逃往四川。返京后玄宗成为太上皇，高力士被新得势的宦官李辅国陷害，760年被流放巫州（今湖南黔阳）。他在流放地写下《感巫州荠菜》诗。762年遇赦返京途中，听闻玄宗已逝，悲痛呕血而死。',
    tags=['政治', '流放', '唐朝'], tagsEn=['Politics', 'Exile', 'Tang Dynasty'],
    personIds=['gao-li-shi-684'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='巫州（今湖南黔阳）', placeNameEn='Wuzhou, modern Qianyang', coords={'lat': 27.2, 'lng': 109.8})

# 高适 (700-765) - 边塞诗人
add('evt-gaoshi-youth', '高适早年漫游', 'Gao Shi\'s Early Wanderings', 720, 749, importance=3,
    summary='高适早年家贫，在宋城以耕钓为生，后漫游燕赵边塞，开始创作边塞诗。',
    summaryEn='Gao Shi lived in poverty in his early years, farming and fishing, then traveled the northern frontiers where he began writing frontier poetry.',
    tags=['早年', '文学', '唐朝'], tagsEn=['Early Life', 'Literature', 'Tang Dynasty'],
    personIds=['gao-shi-700', 'gao-shi'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='宋城（今河南商丘）', placeNameEn='Songcheng, modern Shangqiu', coords={'lat': 34.4, 'lng': 115.6})

add('evt-gaoshi-anshi', '高适平定永王之乱', 'Gao Shi Suppresses Prince Yong\'s Rebellion', 756, importance=5,
    summary='高适在安史之乱中出任淮南节度使，平定永王李璘之乱，展现军事才能。',
    summaryEn='During the An Lushan Rebellion, Gao Shi served as military governor of Huainan and suppressed Prince Yong\'s rebellion.',
    desc='756年安史之乱爆发后，玄宗诸子分镇各地。永王李璘在江陵起兵欲割据江南，李白也被卷入其幕府。高适被任命为淮南节度使，率军讨平永王之乱。这是他一生中最重要的军事成就。此后他历任彭、蜀二州刺史，剑南节度使。',
    tags=['军事', '唐朝'], tagsEn=['Military', 'Tang Dynasty'],
    personIds=['gao-shi-700', 'gao-shi'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='淮南', placeNameEn='Huainan', coords={'lat': 32.4, 'lng': 117.0})

add('evt-gaoshi-poetry', '高适——边塞诗人之冠', 'Gao Shi: Master of Frontier Poetry', 730, 765, importance=4,
    summary='高适与岑参并称「高岑」，《燕歌行》等边塞诗气势雄浑慷慨悲壮，是盛唐边塞诗派的代表。',
    summaryEn='Gao Shi and Cen Shen led the Tang frontier poetry school; his \'Song of Yan\' is a masterpiece of the genre.',
    tags=['文学', '诗歌', '唐朝'], tagsEn=['Literature', 'Poetry', 'Tang Dynasty'],
    personIds=['gao-shi-700', 'gao-shi'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# 陆贽 (754-805) - 唐代名相
add('evt-luzhi-jinshi', '陆贽进士及第', 'Lu Zhi Passes Imperial Exam', 773, importance=3,
    summary='陆贽十八岁进士及第，以博学宏词科登科，少年成名。',
    summaryEn='Lu Zhi passed the imperial examination at 18, earning early fame through the erudite scholars examination.',
    tags=['科举', '唐朝'], tagsEn=['Civil Exam', 'Tang Dynasty'],
    personIds=['lu-zhi-754'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

add('evt-luzhi-chancellor', '陆贽拜相', 'Lu Zhi Becomes Chancellor', 792, 795, importance=5,
    summary='陆贽被唐德宗任命为宰相，以直言极谏著称。他为德宗起草的罪己诏感动天下将士。',
    summaryEn='Lu Zhi became chancellor under Emperor Dezong, famed for his frank remonstrance. His self-critical edict for the emperor moved the entire army.',
    desc='792年陆贽被唐德宗任命为中书侍郎同平章事（宰相）。他为德宗起草的《罪己诏》情真意切——据说宣读后「士卒皆感泣」。他主张广开言路、轻徭薄赋，但因屡次直言触怒德宗。795年被罢相贬为忠州别驾，在贬所闭门著书十年。',
    tags=['政治', '宰相', '唐朝'], tagsEn=['Politics', 'Chancellor', 'Tang Dynasty'],
    personIds=['lu-zhi-754'], regionId='tang-dynasty', sourceIds=JS + SS + ZZTJ,
    placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# 虞世南 (558-638) - 初唐书法家
add('evt-yushinan-calligraphy', '虞世南——初唐四大家', 'Yu Shinan: Master of Early Tang Calligraphy', 620, 638, importance=4,
    summary='虞世南与欧阳询、褚遂良、薛稷并称「初唐四大家」，其书法得王羲之七世孙智永真传。',
    summaryEn='Yu Shinan was one of the \'Four Great Calligraphers of Early Tang\', inheriting Wang Xizhi\'s tradition through the monk Zhiyong.',
    desc='虞世南早年师从王羲之七世孙智永禅师学书，深得二王笔法精髓。唐太宗酷爱书法，常与虞世南讨论书艺。他编有《北堂书钞》160卷，是现存最早的类书之一。唐太宗称其有五绝：德行、忠直、博学、文辞、书翰。',
    tags=['书法', '文学', '唐朝'], tagsEn=['Calligraphy', 'Literature', 'Tang Dynasty'],
    personIds=['yu-shi-nan-558'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# 薛涛 (770-832) - 唐代女诗人
add('evt-xuetao-poetry', '薛涛居成都以诗闻名', 'Xue Tao: Poetess of Chengdu', 790, 832, importance=4,
    summary='薛涛是唐代最著名的女诗人之一，与元稹、白居易、刘禹锡等名士交往唱和，创制薛涛笺。',
    summaryEn='Xue Tao was one of the Tang\'s most famous female poets, exchanging poems with Yuan Zhen, Bai Juyi, and Liu Yuxi. She invented the Xue Tao writing paper.',
    desc='薛涛因父早逝而沦为乐籍，但以诗才闻名蜀中。节度使韦皋曾奏请授她「校书郎」之职（虽未获准但「女校书」之名流传开来）。她与元稹、白居易、刘禹锡、杜牧等名士多有唱和。晚年居成都浣花溪畔，创制深红色小笺写诗——「薛涛笺」成为后世文人雅士珍爱的文房用品。',
    tags=['文学', '诗歌', '女性', '唐朝'], tagsEn=['Literature', 'Poetry', 'Female', 'Tang Dynasty'],
    personIds=['xue-tao-770'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='成都', placeNameEn='Chengdu', coords={'lat': 30.6, 'lng': 104.1})

print(f"Tang dynasty events: {len(all_events)}")

# ================================================================
# SONG DYNASTY
# ================================================================

# 种世衡 (985-1045) - 北宋名将
add('evt-zhongshiheng-fort', '种世衡筑青涧城', 'Zhong Shiheng Builds Qingjian Fort', 1040, importance=4,
    summary='种世衡在延州东北筑青涧城，巩固西北边防，招抚羌人，是种家将的开山人物。',
    summaryEn='Zhong Shiheng built Qingjian Fort northeast of Yanzhou, consolidating the northwest frontier. He founded the Zhong military lineage.',
    desc='1040年西夏李元昊大举攻宋。种世衡在范仲淹提拔下，于延州东北200里处筑青涧城，开营田、募商贾、通贸易，使荒凉的边塞成为坚固的前线据点。他还深入羌人部落招抚，羌人感其恩德愿为效死。种世衡与其子孙种谔、种师道等成为北宋著名的「种家将」。',
    tags=['军事', '边防', '宋朝'], tagsEn=['Military', 'Border Defense', 'Song Dynasty'],
    personIds=['zhong-shi-heng-985'], regionId='song-dynasty', sourceIds=SOS,
    placeName='青涧城（今陕西清涧）', placeNameEn='Qingjian Fort, modern Qingjian', coords={'lat': 37.1, 'lng': 110.1})

print(f"Phase 4 total so far: {len(all_events)}")

# Write output
output_file = os.path.join(OUTPUT_DIR, '_deepEvents_phase4.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_events, f, ensure_ascii=False, indent=2)
print(f"Written {len(all_events)} events to {output_file}")
print("This is Part 1 of Phase 4. Continue with gen_deep_events_phase4b.py")
