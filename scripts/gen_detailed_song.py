#!/usr/bin/env python3
"""Generate detailed events for Song dynasty figures."""
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
        'dataStatus': 'published', 'confidenceScore': 0.85,
        'externalReferences': [],
        'placeName': placeName, 'placeNameEn': placeNameEn,
        'coordinates': coords,
    })

# ==================== SONG DYNASTY ====================

# Song Taizu (927-976)
add('evt-songtaizu-coup', '陈桥兵变黄袍加身', 'Chen Bridge Mutiny', 960, importance=5,
    summary='赵匡胤在陈桥驿被部下黄袍加身拥立为帝，建立宋朝。',
    summaryEn='Zhao Kuangyin was draped in the imperial yellow robe by his troops and proclaimed emperor, founding Song.',
    tags=['政治', '开国', '宋朝'], tagsEn=['Politics', 'Founding', 'Song Dynasty'],
    personIds=['song-taizu', 'zhao-pu'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='陈桥驿（今开封北）', placeNameEn='Chen Bridge, north of Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

add('evt-songtaizu-wine', '杯酒释兵权', 'Relieving Generals Over Wine', 961, importance=5,
    summary='赵匡胤以宴请方式和平解除了开国将领的军权，避免重蹈五代军人专权的覆辙。',
    summaryEn='Zhao Kuangyin peacefully retired his founding generals over a banquet, preventing the cycle of military coups.',
    tags=['政治', '宋朝'], tagsEn=['Politics', 'Song Dynasty'],
    personIds=['song-taizu'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='开封', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

add('evt-songtaizu-reunify', '赵匡胤统一南方', 'Unification of the South', 963, 975, importance=4,
    summary='采取「先南后北」战略，先后灭荆南、后蜀、南汉、南唐等割据政权。',
    summaryEn='Adopting a \'south first\' strategy, Zhao successively conquered Jingnan, Later Shu, Southern Han, and Southern Tang.',
    tags=['军事', '统一', '宋朝'], tagsEn=['Military', 'Unification', 'Song Dynasty'],
    personIds=['song-taizu'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='开封', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

# Song Taizong (939-997)
add('evt-songtaizong-ascend', '斧声烛影——宋太宗即位', 'Zhao Guangyi\'s Controversial Succession', 976, importance=4,
    summary='太祖暴毙之夜「斧声烛影」疑云重重，其弟赵光义即位为宋太宗。',
    summaryEn='On the night of Taizu\'s sudden death, shrouded in mystery, his brother Zhao Guangyi ascended.',
    tags=['政治', '即位', '宋朝'], tagsEn=['Politics', 'Succession', 'Song Dynasty'],
    personIds=['song-taizong', 'song-taizu'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='开封', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

add('evt-songtaizong-conquer', '灭北汉与高梁河之败', 'Destruction of Northern Han & Gaoliang Defeat', 979, importance=4,
    summary='赵光义亲征灭北汉完成统一，但随后北伐辽国在高梁河大败，本人中箭乘驴车逃走。',
    summaryEn='Zhao Guangyi destroyed Northern Han, but his northern expedition against Liao ended in disaster at Gaoliang River.',
    tags=['军事', '宋朝'], tagsEn=['Military', 'Song Dynasty'],
    personIds=['song-taizong'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='太原至高梁河', placeNameEn='Taiyuan to Gaoliang River', coords={'lat': 39.9, 'lng': 116.3})

# Zhao Pu (922-992)
add('evt-zhaopu-chancellor', '赵普——半部《论语》治天下', 'Zhao Pu: Half the Analects to Govern', 960, 992, importance=4,
    summary='赵普是宋朝开国第一功臣，策划陈桥兵变、设计杯酒释兵权，三次拜相。',
    summaryEn='Zhao Pu was Song\'s founding strategist, architect of the coup and the wine-dismissal, serving as chancellor three times.',
    tags=['政治', '宰相', '宋朝'], tagsEn=['Politics', 'Chancellor', 'Song Dynasty'],
    personIds=['zhao-pu'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='开封', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

# Kou Zhun (961-1023)
add('evt-kouzhun-chanyuan', '寇准力主亲征与澶渊之盟', 'Kou Zhun and the Chanyuan Treaty', 1004, importance=5,
    summary='辽军南侵时满朝恐慌，寇准力排众议坚持宋真宗御驾亲征，最终达成澶渊之盟换取了百年和平。',
    summaryEn='When Liao invaded, Kou Zhun insisted the emperor personally lead the defense, resulting in the Chanyuan Treaty.',
    tags=['政治', '外交', '宋朝'], tagsEn=['Politics', 'Diplomacy', 'Song Dynasty'],
    personIds=['kou-zhun'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='澶州（今河南濮阳）', placeNameEn='Chanyuan, modern Puyang', coords={'lat': 35.7, 'lng': 115.0})

# Bi Sheng (972-1051)
add('evt-bisheng-invent', '毕昇发明活字印刷术', 'Bi Sheng Invents Movable Type', 1040, 1048, importance=5,
    summary='平民毕昇发明泥活字印刷术，用胶泥刻字火烧硬化排版印刷，比古腾堡铅活字早约400年。',
    summaryEn='Bi Sheng invented movable type with fired clay characters, predating Gutenberg\'s press by about 400 years.',
    tags=['科技', '发明', '宋朝'], tagsEn=['Technology', 'Invention', 'Song Dynasty'],
    personIds=['bi-sheng'], regionId='song-dynasty',
    sourceIds=['src-ss', 'src-mengxibitan'], placeName='北宋', placeNameEn='Northern Song', coords={'lat': 30.0, 'lng': 115.0})

# Fan Zhongyan (989-1052)
add('evt-fanzhongyan-youth', '范仲淹断齑画粥', 'Fan Zhongyan\'s Studious Youth', 1005, 1015, importance=3,
    summary='范仲淹两岁丧父，在醴泉寺刻苦读书，每天只煮一锅粥划为四块早晚各吃两块。',
    summaryEn='Orphaned at two, Fan Zhongyan studied under extreme hardship, surviving on one pot of congee divided into four.',
    tags=['早年', '宋朝'], tagsEn=['Early Life', 'Song Dynasty'],
    personIds=['fan-zhongyan'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='醴泉寺', placeNameEn='Liquan Temple', coords={'lat': 34.0, 'lng': 109.0})

add('evt-fanzhongyan-reform', '庆历新政', 'Qingli Reforms', 1043, 1044, importance=5,
    summary='范仲淹在仁宗支持下推行庆历新政，改革科举整顿吏治，但因触动官僚利益而失败。',
    summaryEn='Fan Zhongyan launched the Qingli Reforms to overhaul examinations and bureaucracy, but failed against vested interests.',
    tags=['政治', '改革', '宋朝'], tagsEn=['Politics', 'Reform', 'Song Dynasty'],
    personIds=['fan-zhongyan'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='开封', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

add('evt-fanzhongyan-yueyang', '《岳阳楼记》', 'Record of Yueyang Tower', 1046, importance=5,
    summary='被贬后范仲淹写下「先天下之忧而忧，后天下之乐而乐」——定义了中国士大夫两千年的精神追求。',
    summaryEn='In exile, Fan wrote: \'Be first to bear the world\'s troubles, last to enjoy its pleasures\' — defining the scholar-official\'s mission.',
    tags=['文学', '宋朝'], tagsEn=['Literature', 'Song Dynasty'],
    personIds=['fan-zhongyan'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='邓州', placeNameEn='Dengzhou', coords={'lat': 32.7, 'lng': 112.1})

# Bao Zheng (999-1062)
add('evt-baozheng-judge', '包拯铁面无私', 'Bao Zheng the Incorruptible Judge', 1030, 1062, importance=4,
    summary='包拯以铁面无私刚正不阿著称，是中国文化中「包青天」清官形象的永恒象征。',
    summaryEn='Bao Zheng, famed for incorruptible justice, became the eternal symbol of the upright official in Chinese culture.',
    tags=['政治', '清官', '宋朝'], tagsEn=['Politics', 'Upright Official', 'Song Dynasty'],
    personIds=['bao-zheng'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='开封', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

# Song Renzong (1010-1063)
add('evt-songrenzong-reign', '宋仁宗——千古仁君', 'Emperor Renzong\'s Benevolent Reign', 1022, 1063, importance=4,
    summary='宋仁宗在位四十二年，是宋朝文治的巅峰期，包拯、范仲淹、欧阳修、苏轼等群星璀璨。',
    summaryEn='Renzong\'s 42-year reign was the zenith of Song civil governance, producing an extraordinary constellation of talents.',
    tags=['政治', '皇帝', '宋朝'], tagsEn=['Politics', 'Emperor', 'Song Dynasty'],
    personIds=['song-renzong'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='开封', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

# Su Song (1020-1101)
add('evt-susong-clock', '苏颂建造水运仪象台', 'Su Song Builds the Cosmic Engine', 1088, importance=5,
    summary='苏颂主持建造了水运仪象台——世界上最古老的天文钟，集观测、演示、报时于一体。',
    summaryEn='Su Song built the Cosmic Engine — the world\'s oldest astronomical clock tower, integrating observation and timekeeping.',
    tags=['科技', '天文学', '宋朝'], tagsEn=['Technology', 'Astronomy', 'Song Dynasty'],
    personIds=['su-song'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='开封', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

# Song Shenzong (1048-1085)
add('evt-songshenzong-reform', '宋神宗与熙宁变法', 'Emperor Shenzong and Xining Reforms', 1069, 1085, importance=5,
    summary='宋神宗任用王安石推行大规模熙宁变法，力图富国强兵，新旧党争成为北宋后期政治主线。',
    summaryEn='Emperor Shenzong appointed Wang Anshi to implement sweeping reforms, dividing the court into reform and conservative factions.',
    tags=['政治', '改革', '宋朝'], tagsEn=['Politics', 'Reform', 'Song Dynasty'],
    personIds=['song-shenzong', 'wang-anshi'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='开封', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

# Song Huizong (1082-1135)
add('evt-songhuizong-art', '宋徽宗的艺术帝国', 'Emperor Huizong\'s Art Empire', 1100, 1126, importance=4,
    summary='宋徽宗是中国历史上艺术造诣最高的皇帝——独创瘦金体、推动翰林图画院，却是灾难性的皇帝。',
    summaryEn='Huizong was the most artistically accomplished emperor — creating Slender Gold script and the painting academy — but a disastrous ruler.',
    tags=['艺术', '书法', '宋朝'], tagsEn=['Art', 'Calligraphy', 'Song Dynasty'],
    personIds=['song-huizong'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='开封', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

# Li Qingzhao (1084-1155)
add('evt-liqingzhao-early', '李清照与赵明诚的金石姻缘', 'Li Qingzhao and Zhao Mingcheng', 1101, 1127, importance=4,
    summary='李清照与丈夫赵明诚共同热衷金石收藏研究，前期词作清新婉约，「知否知否应是绿肥红瘦」。',
    summaryEn='Li Qingzhao shared a passion for antiquities with her husband; her early lyrics were fresh and graceful.',
    tags=['文学', '婚姻', '宋朝'], tagsEn=['Literature', 'Marriage', 'Song Dynasty'],
    personIds=['li-qingzhao'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='汴京', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

add('evt-liqingzhao-exile', '南渡——李清照的流亡', 'Southern Flight and Exile', 1127, 1132, importance=5,
    summary='靖康之变后李清照南渡，丈夫去世、毕生收藏散失殆尽，词风转为「寻寻觅觅冷冷清清」的沉痛苍凉。',
    summaryEn='After the Jingkang Incident, Li Qingzhao fled south — her husband died and her collection was lost; her poetry turned to grief.',
    tags=['文学', '战乱', '宋朝'], tagsEn=['Literature', 'War', 'Song Dynasty'],
    personIds=['li-qingzhao'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='南渡途中', placeNameEn='Flight to the South', coords={'lat': 32.0, 'lng': 118.0})

# Zhang Zeduan (1085-1145)
add('evt-zhangzeduan-painting', '张择端绘《清明上河图》', 'Along the River During Qingming', 1100, 1120, importance=5,
    summary='张择端创作《清明上河图》，以百科全书式的精度记录了12世纪开封的城市生活。',
    summaryEn='Zhang Zeduan created the iconic scroll recording 12th-century Kaifeng urban life with encyclopedic precision.',
    tags=['绘画', '艺术', '宋朝'], tagsEn=['Painting', 'Art', 'Song Dynasty'],
    personIds=['zhang-zeduan'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='开封', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

# Yue Fei (1103-1142)
add('evt-yuefei-campaign', '岳飞北伐', 'Yue Fei\'s Northern Campaigns', 1134, 1140, importance=5,
    summary='岳飞率岳家军北伐，郾城大破金军拐子马，打到距开封仅四十五里的朱仙镇。',
    summaryEn='Yue Fei\'s army swept north, shattering the Jin at Yancheng and reaching Zhuxian Town, just 45 li from Kaifeng.',
    tags=['军事', '抗金', '宋朝'], tagsEn=['Military', 'Anti-Jin', 'Song Dynasty'],
    personIds=['yue-fei'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='郾城至朱仙镇', placeNameEn='Yancheng to Zhuxian Town', coords={'lat': 34.7, 'lng': 114.2})

add('evt-yuefei-death', '十二道金牌与风波亭', 'Twelve Gold Medallions and Execution', 1142, importance=5,
    summary='宋高宗以十二道金牌强令岳飞班师，随后以「莫须有」罪名在风波亭处死，年仅39岁。',
    summaryEn='Gaozong recalled Yue Fei with twelve gold medallions, then executed him on fabricated charges at Fengbo Pavilion.',
    tags=['政治', '冤狱', '宋朝'], tagsEn=['Politics', 'Miscarriage of Justice', 'Song Dynasty'],
    personIds=['yue-fei', 'song-gaozong', 'qin-hui'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='临安（杭州）', placeNameEn='Lin\'an (Hangzhou)', coords={'lat': 30.2, 'lng': 120.2})

# Song Gaozong (1107-1187)
add('evt-songgaozong-ascend', '宋高宗建立南宋', 'Emperor Gaozong Establishes Southern Song', 1127, importance=4,
    summary='靖康之变后赵构在南京应天府即位延续宋朝，后定都临安，开启南宋152年历史。',
    summaryEn='After the Jingkang Incident, Zhao Gou ascended and later moved the capital to Lin\'an, inaugurating Southern Song.',
    tags=['政治', '开国', '宋朝'], tagsEn=['Politics', 'Founding', 'Song Dynasty'],
    personIds=['song-gaozong'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='应天府（今商丘）', placeNameEn='Yingtian, modern Shangqiu', coords={'lat': 34.4, 'lng': 115.6})

# Lu You (1125-1210)
add('evt-luyou-poetry', '陆游——爱国诗人', 'Lu You: The Patriot Poet', 1150, 1210, importance=4,
    summary='陆游是中国存诗最多的诗人之一，85岁临终写下「王师北定中原日，家祭无忘告乃翁」。',
    summaryEn='Lu You, among China\'s most prolific poets, wrote on his deathbed: \'When the imperial army recovers the north, tell your father.\'',
    tags=['文学', '诗歌', '宋朝'], tagsEn=['Literature', 'Poetry', 'Song Dynasty'],
    personIds=['lu-you'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='山阴（今绍兴）', placeNameEn='Shanyin, modern Shaoxing', coords={'lat': 30.0, 'lng': 120.5})

# Xin Qiji (1140-1207)
add('evt-xinqiji-warrior-poet', '辛弃疾——词中之龙', 'Xin Qiji: Dragon Among Poets', 1161, 1207, importance=4,
    summary='辛弃疾22岁时率五十骑闯入五万金军大营擒拿叛徒，南归后将满腔悲愤倾注于词。',
    summaryEn='At 22, Xin Qiji led 50 riders into a 50,000-strong Jin camp to capture a traitor, later pouring his frustration into lyrics.',
    tags=['文学', '军事', '宋朝'], tagsEn=['Literature', 'Military', 'Song Dynasty'],
    personIds=['xin-qiji'], regionId='song-dynasty',
    sourceIds=['src-ss'], placeName='南宋', placeNameEn='Southern Song', coords={'lat': 30.0, 'lng': 117.0})

# Wen Tianxiang (1236-1283)
add('evt-wentianxiang-martyr', '文天祥——留取丹心照汗青', 'Wen Tianxiang: A Loyal Heart Illumines History', 1278, 1283, importance=5,
    summary='南宋灭亡后文天祥被俘，拒绝元朝劝降，在狱中写下《正气歌》后从容就义。',
    summaryEn='After Song\'s fall, Wen Tianxiang refused all Yuan offers, wrote \'Song of Righteousness\' in prison, and died a martyr.',
    tags=['政治', '忠臣', '宋朝'], tagsEn=['Politics', 'Loyalist', 'Song Dynasty'],
    personIds=['wen-tianxiang'], regionId='song-dynasty',
    sourceIds=['src-ss', 'src-songshi'], placeName='大都（今北京）', placeNameEn='Dadu, modern Beijing', coords={'lat': 39.9, 'lng': 116.4})

output_file = os.path.join(OUTPUT_DIR, '_detailedEvents_song.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_events, f, ensure_ascii=False, indent=2)
print(f"Song dynasty: {len(all_events)} detailed events written to {output_file}")
