#!/usr/bin/env python3
"""Generate detailed events for Yuan, Ming, Qing dynasties."""
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

# ==================== YUAN DYNASTY ====================

# Guo Shoujing (1231-1316)
add('evt-guoshoujing-calendar', '郭守敬编制《授时历》', 'Guo Shoujing Creates Shoushi Calendar', 1276, 1280, importance=5,
    summary='郭守敬在全国设27个观测站，编制《授时历》以365.2425天为一年，与现行公历相同但早了三个世纪。',
    summaryEn='Guo Shoujing set up 27 observatories nationwide and created the Shoushi Calendar, matching the Gregorian year length three centuries earlier.',
    tags=['科学', '天文学', '元朝'], tagsEn=['Science', 'Astronomy', 'Yuan Dynasty'],
    personIds=['guo-shoujing'], regionId='yuan-dynasty',
    sourceIds=['src-yuanshi'], placeName='大都（今北京）', placeNameEn='Dadu, modern Beijing', coords={'lat': 39.9, 'lng': 116.4})

add('evt-guoshoujing-canal', '郭守敬修建通惠河', 'Guo Shoujing Builds Tonghui Canal', 1291, 1293, importance=4,
    summary='郭守敬主持修建通惠河，使京杭大运河全线贯通直达大都城内的积水潭。',
    summaryEn='Guo Shoujing built the Tonghui Canal, completing the Grand Canal\'s direct connection to the heart of Dadu.',
    tags=['工程', '水利', '元朝'], tagsEn=['Engineering', 'Hydraulics', 'Yuan Dynasty'],
    personIds=['guo-shoujing'], regionId='yuan-dynasty',
    sourceIds=['src-yuanshi'], placeName='大都（今北京）', placeNameEn='Dadu, modern Beijing', coords={'lat': 39.9, 'lng': 116.4})

# Yuan Chengzong (1265-1307)
add('evt-yuanchengzong-reign', '元成宗守成之治', 'Emperor Chengzong\'s Conservative Rule', 1294, 1307, importance=3,
    summary='忽必烈之孙铁穆耳继承皇位，停止对外远征，基本维持忽必烈的制度框架。',
    summaryEn='Temur, Kublai\'s grandson, halted foreign expeditions and maintained Kublai\'s institutional framework.',
    tags=['政治', '元朝'], tagsEn=['Politics', 'Yuan Dynasty'],
    personIds=['yuan-chengzong'], regionId='yuan-dynasty',
    sourceIds=['src-yuanshi'], placeName='大都（今北京）', placeNameEn='Dadu, modern Beijing', coords={'lat': 39.9, 'lng': 116.4})

# Yuan Huizong (1320-1370)
add('evt-yuanhuizong-fall', '元惠宗——元朝末代皇帝', 'Emperor Huizong: Last Yuan Emperor', 1333, 1368, importance=4,
    summary='妥懽帖睦尔年少即位，初期励精图治但很快沉迷享乐。1368年徐达攻入大都，元朝在中原的统治终结。',
    summaryEn='Toghon Temur ascended young; after brief reform, he indulged in pleasure. In 1368, Xu Da captured Dadu, ending Yuan rule in China.',
    tags=['政治', '灭亡', '元朝'], tagsEn=['Politics', 'Fall', 'Yuan Dynasty'],
    personIds=['yuan-huizong'], regionId='yuan-dynasty',
    sourceIds=['src-yuanshi'], placeName='大都（今北京）', placeNameEn='Dadu, modern Beijing', coords={'lat': 39.9, 'lng': 116.4})

# ==================== MING DYNASTY ====================

# Liu Bowen (1311-1375)
add('evt-liubowen-advisor', '刘伯温辅佐朱元璋', 'Liu Bowen Advises Zhu Yuanzhang', 1360, 1375, importance=4,
    summary='刘伯温是明朝开国第一谋臣，以神机妙算著称，民间传说中近乎半神化的军师形象。',
    summaryEn='Liu Bowen was the founding Ming dynasty\'s foremost strategist, mythologized in folklore as a semi-divine advisor.',
    tags=['政治', '开国', '明朝'], tagsEn=['Politics', 'Founding', 'Ming Dynasty'],
    personIds=['liu-bowen', 'ming-taizu'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='应天（今南京）', placeNameEn='Yingtian, modern Nanjing', coords={'lat': 32.0, 'lng': 118.7})

# Ming Yongle (1360-1424)
add('evt-mingyongle-coup', '靖难之役', 'Jingnan Campaign', 1399, 1402, importance=5,
    summary='燕王朱棣以「清君侧」为名发动靖难之役，四年后攻入南京夺取皇位。',
    summaryEn='Prince of Yan Zhu Di launched the Jingnan Campaign, capturing Nanjing after four years to seize the throne.',
    tags=['军事', '政变', '明朝'], tagsEn=['Military', 'Coup', 'Ming Dynasty'],
    personIds=['ming-yongle'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='北平至南京', placeNameEn='Beiping to Nanjing', coords={'lat': 36.0, 'lng': 117.0})

add('evt-mingyongle-beijing', '迁都北京与永乐盛世', 'Moving Capital to Beijing & Yongle Era', 1403, 1424, importance=5,
    summary='永乐帝迁都北京、五次亲征漠北、派郑和七下西洋、编纂《永乐大典》、修筑紫禁城。',
    summaryEn='Yongle moved the capital to Beijing, led five northern campaigns, dispatched Zheng He\'s voyages, compiled the Yongle Encyclopedia.',
    tags=['政治', '盛世', '明朝'], tagsEn=['Politics', 'Golden Age', 'Ming Dynasty'],
    personIds=['ming-yongle', 'zheng-he'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# Yu Qian (1398-1457)
add('evt-yuqian-defense', '于谦保卫北京', 'Yu Qian Defends Beijing', 1449, importance=5,
    summary='土木堡之变后于谦力排南迁之议，领导北京保卫战击退瓦剌大军，挽救了明朝。',
    summaryEn='After the Tumu Crisis, Yu Qian overrode calls to flee south, leading the defense of Beijing and saving the Ming dynasty.',
    tags=['军事', '明朝'], tagsEn=['Military', 'Ming Dynasty'],
    personIds=['yu-qian'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# Ming Xuande (1399-1435)
add('evt-mingxuande-reign', '明宣宗——仁宣之治', 'Emperor Xuande\'s Benevolent Rule', 1425, 1435, importance=4,
    summary='明宣宗延续仁政，裁撤冗员减轻赋税，宣德炉和宣德青花瓷至今仍是中国工艺美术的极致代表。',
    summaryEn='Xuande continued benevolent policies, and Xuande-era bronzes and blue-and-white porcelain remain pinnacles of Chinese craft.',
    tags=['政治', '艺术', '明朝'], tagsEn=['Politics', 'Art', 'Ming Dynasty'],
    personIds=['ming-xuande'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# Tang Yin (1470-1524)
add('evt-tangyin-fall', '唐伯虎——从解元到落魄才子', 'Tang Yin: From Top Scholar to Fallen Genius', 1498, 1499, importance=4,
    summary='唐寅乡试第一风光无限，但次年卷入科场舞弊案被终身剥夺考试资格，从此靠卖画为生。',
    summaryEn='Tang Yin placed first in provincial exams, but was banned for life after a cheating scandal, becoming a painter for hire.',
    tags=['艺术', '绘画', '明朝'], tagsEn=['Art', 'Painting', 'Ming Dynasty'],
    personIds=['tang-yin'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='南京至苏州', placeNameEn='Nanjing to Suzhou', coords={'lat': 31.3, 'lng': 120.6})

# Wang Yangming (1472-1529)
add('evt-wangyangming-philosophy', '王阳明龙场悟道', 'Wang Yangming\'s Enlightenment at Longchang', 1508, importance=5,
    summary='王阳明被贬贵州龙场驿，在困顿中顿悟「心即是理」，开创了心学。',
    summaryEn='Exiled to Longchang, Guizhou, Wang Yangming had his breakthrough: \'The mind is principle\' — founding the School of Mind.',
    tags=['哲学', '心学', '明朝'], tagsEn=['Philosophy', 'School of Mind', 'Ming Dynasty'],
    personIds=['wang-yangming'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='贵州龙场', placeNameEn='Longchang, Guizhou', coords={'lat': 26.6, 'lng': 106.7})

add('evt-wangyangming-rebellion', '王阳明平定宁王之乱', 'Wang Yangming Suppresses Prince of Ning', 1519, importance=5,
    summary='宁王朱宸濠在南昌叛乱，王阳明以临时拼凑的兵力仅43天就平定叛乱。',
    summaryEn='When Prince of Ning rebelled, Wang Yangming crushed the rebellion in just 43 days with hastily assembled forces.',
    tags=['军事', '明朝'], tagsEn=['Military', 'Ming Dynasty'],
    personIds=['wang-yangming'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='南昌', placeNameEn='Nanchang', coords={'lat': 28.7, 'lng': 115.9})

# Wu Chengen (1506-1582)
add('evt-wuchengen-novel', '吴承恩著《西游记》', 'Wu Chengen Writes Journey to the West', 1550, 1580, importance=5,
    summary='吴承恩在晚年创作了中国最伟大的神魔小说《西游记》，孙悟空成为中国文化最深入人心的形象之一。',
    summaryEn='Wu Chengen wrote Journey to the West, China\'s greatest mythological novel, creating the immortal Monkey King.',
    tags=['文学', '小说', '明朝'], tagsEn=['Literature', 'Novel', 'Ming Dynasty'],
    personIds=['wu-chengen'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='淮安', placeNameEn='Huai\'an', coords={'lat': 33.5, 'lng': 119.1})

# Hai Rui (1514-1587)
add('evt-hairui-memorial', '海瑞上《治安疏》', 'Hai Rui\'s Candid Memorial', 1566, importance=5,
    summary='海瑞备好棺材上《治安疏》痛斥嘉靖帝迷信道教不理朝政，成为中国历史上最著名的谏臣。',
    summaryEn='Hai Rui prepared his coffin and submitted a memorial harshly criticizing the Jiajing Emperor, becoming China\'s most famous remonstrator.',
    tags=['政治', '谏臣', '明朝'], tagsEn=['Politics', 'Remonstrator', 'Ming Dynasty'],
    personIds=['hai-rui'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# Xu Wei (1521-1593)
add('evt-xuwei-art', '徐渭——最不幸的天才', 'Xu Wei: The Most Unfortunate Genius', 1550, 1593, importance=4,
    summary='徐渭八次科举不第，一度精神失常九次自杀未遂，但在痛苦中开创了泼墨大写意花鸟画。',
    summaryEn='Xu Wei failed the exams eight times, went insane and attempted suicide nine times, yet pioneered splash-ink flower painting.',
    tags=['绘画', '艺术', '明朝'], tagsEn=['Painting', 'Art', 'Ming Dynasty'],
    personIds=['xu-wei'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='绍兴', placeNameEn='Shaoxing', coords={'lat': 30.0, 'lng': 120.5})

# Zhang Juzheng (1525-1582)
add('evt-zhangjuzheng-reform', '张居正改革', 'Zhang Juzheng\'s Reforms', 1572, 1582, importance=5,
    summary='张居正任首辅推行一条鞭法等重大改革，使明朝财政好转，是明朝最有权势的首辅。',
    summaryEn='Zhang Juzheng as Grand Secretary implemented the Single Whip Law and other reforms, reviving Ming finances.',
    tags=['政治', '改革', '明朝'], tagsEn=['Politics', 'Reform', 'Ming Dynasty'],
    personIds=['zhang-juzheng'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# Qi Jiguang (1528-1588)
add('evt-qijiguang-pirates', '戚继光抗倭', 'Qi Jiguang Fights Pirates', 1555, 1567, importance=5,
    summary='戚继光组建戚家军，在东南沿海九战九捷基本肃清倭患，著有《纪效新书》和《练兵实纪》。',
    summaryEn='Qi Jiguang formed the Qi Army, winning nine consecutive battles to clear the coast of pirates.',
    tags=['军事', '抗倭', '明朝'], tagsEn=['Military', 'Anti-Pirate', 'Ming Dynasty'],
    personIds=['qi-jiguang'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='浙江福建沿海', placeNameEn='Zhejiang-Fujian Coast', coords={'lat': 28.0, 'lng': 121.0})

# Ming Wanli (1563-1620)
add('evt-mingwanli-reign', '万历怠政', 'Wanli Emperor\'s Neglect', 1586, 1620, importance=4,
    summary='明神宗万历帝前期有张居正辅政，后期因国本之争长达三十年不上朝，明朝由此走向衰败。',
    summaryEn='Emperor Wanli, after Zhang Juzheng\'s death, refused to hold court for 30 years over a succession dispute.',
    tags=['政治', '明朝'], tagsEn=['Politics', 'Ming Dynasty'],
    personIds=['ming-wanli'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# Yuan Chonghuan (1584-1630)
add('evt-yuanchonghuan-ningyuan', '宁远大捷', 'Victory at Ningyuan', 1626, importance=5,
    summary='袁崇焕在宁远以红夷大炮命中努尔哈赤，后者不久伤重而死，是明军对后金的第一次重大胜利。',
    summaryEn='Yuan Chonghuan used Portuguese cannons at Ningyuan, mortally wounding Nurhaci — Ming\'s first major victory against the Later Jin.',
    tags=['军事', '明朝'], tagsEn=['Military', 'Ming Dynasty'],
    personIds=['yuan-chonghuan', 'nurhaci'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='宁远（今辽宁兴城）', placeNameEn='Ningyuan, modern Xingcheng', coords={'lat': 40.6, 'lng': 120.7})

add('evt-yuanchonghuan-death', '袁崇焕被凌迟', 'Yuan Chonghuan\'s Execution', 1630, importance=5,
    summary='皇太极利用反间计，多疑的崇祯帝将袁崇焕凌迟处死，北京百姓争食其肉——中国历史上最黑暗的忠臣悲剧之一。',
    summaryEn='Hong Taiji\'s disinformation led the paranoid Chongzhen Emperor to have Yuan Chonghuan executed by slow slicing — one of history\'s darkest loyalist tragedies.',
    tags=['政治', '冤狱', '明朝'], tagsEn=['Politics', 'Miscarriage of Justice', 'Ming Dynasty'],
    personIds=['yuan-chonghuan', 'ming-chongzhen'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# Song Yingxing (1587-1666)
add('evt-songyingxing-book', '宋应星著《天工开物》', 'Song Yingxing Writes Tiangong Kaiwu', 1637, importance=5,
    summary='宋应星编著《天工开物》——中国第一部综合性工业技术百科全书，记录了明代的农业和手工业技术。',
    summaryEn='Song Yingxing compiled Tiangong Kaiwu — China\'s first comprehensive encyclopedia of industrial technology.',
    tags=['科技', '著作', '明朝'], tagsEn=['Technology', 'Scholarship', 'Ming Dynasty'],
    personIds=['song-yingxing'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='江西', placeNameEn='Jiangxi', coords={'lat': 28.0, 'lng': 116.0})

# Ming Chongzhen (1611-1644)
add('evt-mingchongzhen-fall', '崇祯帝煤山自缢', 'Chongzhen Emperor Hangs Himself', 1644, importance=5,
    summary='李自成攻破北京，崇祯帝在煤山自缢身亡，明朝灭亡。死前写下「任贼分裂朕尸，勿伤百姓一人」。',
    summaryEn='Li Zicheng captured Beijing; the Chongzhen Emperor hanged himself on Coal Hill, ending the Ming dynasty.',
    tags=['政治', '灭亡', '明朝'], tagsEn=['Politics', 'Fall', 'Ming Dynasty'],
    personIds=['ming-chongzhen'], regionId='ming-dynasty',
    sourceIds=['src-mingshi'], placeName='北京煤山（今景山）', placeNameEn='Coal Hill, Beijing', coords={'lat': 39.9, 'lng': 116.4})

# ==================== QING DYNASTY ====================

# Qing Huangtaiji (1592-1643)
add('evt-qinghuangtaiji-reform', '皇太极建立大清', 'Hong Taiji Proclaims the Qing Dynasty', 1636, importance=5,
    summary='皇太极在盛京称帝改国号为「大清」，改革八旗制度、重用汉人降将，做好了入主中原的一切准备。',
    summaryEn='Hong Taiji proclaimed the Qing dynasty at Shengjing, reformed the Banner system, and prepared for the conquest of China.',
    tags=['政治', '开国', '清朝'], tagsEn=['Politics', 'Founding', 'Qing Dynasty'],
    personIds=['qing-huangtaiji'], regionId='qing-dynasty',
    sourceIds=['src-qingshigao'], placeName='盛京（今沈阳）', placeNameEn='Shengjing, modern Shenyang', coords={'lat': 41.8, 'lng': 123.4})

# Ba Da Shanren (1626-1705)
add('evt-badashanren-art', '八大山人的白眼鱼鸟', 'Ba Da Shanren\'s Scornful Fish and Birds', 1660, 1705, importance=4,
    summary='明宗室后裔朱耷出家为僧，以翻白眼的鱼鸟和大面积留白表达亡国之痛。',
    summaryEn='Zhu Da, Ming imperial descendant turned monk, expressed his grief through fish and birds with scornful white eyes.',
    tags=['绘画', '艺术', '清朝'], tagsEn=['Painting', 'Art', 'Qing Dynasty'],
    personIds=['ba-da-shanren'], regionId='qing-dynasty',
    sourceIds=['src-qingshigao'], placeName='南昌', placeNameEn='Nanchang', coords={'lat': 28.7, 'lng': 115.9})

# Qing Shunzhi (1638-1661)
add('evt-qingshunzhi-conquest', '清军入关', 'Qing Forces Enter the Pass', 1644, importance=5,
    summary='吴三桂引清兵入关，清军迅速占领北京并迁都，开始了清朝对中国的统治。',
    summaryEn='Wu Sangui opened Shanhai Pass; Qing forces quickly captured Beijing and moved the capital, beginning Qing rule over China.',
    tags=['政治', '入关', '清朝'], tagsEn=['Politics', 'Conquest', 'Qing Dynasty'],
    personIds=['qing-shunzhi', 'wu-sangui'], regionId='qing-dynasty',
    sourceIds=['src-qingshigao'], placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# Pu Songling (1640-1715)
add('evt-pusongling-stories', '蒲松龄著《聊斋志异》', 'Pu Songling Writes Strange Tales', 1680, 1715, importance=5,
    summary='蒲松龄科举屡试不第，在乡村教书之余搜集民间鬼狐故事，著成中国最伟大的文言短篇小说集。',
    summaryEn='Failing the exams repeatedly, Pu Songling collected ghost and fox spirit tales, creating China\'s greatest classical short story collection.',
    tags=['文学', '小说', '清朝'], tagsEn=['Literature', 'Novel', 'Qing Dynasty'],
    personIds=['pu-songling'], regionId='qing-dynasty',
    sourceIds=['src-qingshigao'], placeName='山东淄川', placeNameEn='Zichuan, Shandong', coords={'lat': 36.6, 'lng': 117.9})

# Qing Yongzheng (1678-1735)
add('evt-qingyongzheng-reform', '雍正帝改革', 'Yongzheng Emperor\'s Reforms', 1723, 1735, importance=5,
    summary='雍正帝推行摊丁入亩、耗羡归公、改土归流等重大改革，设立军机处强化皇权，是清朝最有效率的皇帝。',
    summaryEn='Yongzheng implemented sweeping fiscal and administrative reforms, establishing the Grand Council and strengthening imperial power.',
    tags=['政治', '改革', '清朝'], tagsEn=['Politics', 'Reform', 'Qing Dynasty'],
    personIds=['qing-yongzheng'], regionId='qing-dynasty',
    sourceIds=['src-qingshigao'], placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# Zheng Banqiao (1693-1766)
add('evt-zhengbanqiao-art', '郑板桥——扬州八怪之首', 'Zheng Banqiao: Leader of the Eight Eccentrics', 1736, 1765, importance=4,
    summary='郑板桥以画竹闻名，题诗「衙斋卧听萧萧竹，疑是民间疾苦声」表达对百姓的深切关怀。',
    summaryEn='Zheng Banqiao, famed for bamboo paintings, wrote: \'Lying in my office, I hear the rustling bamboo — could it be the sound of the people\'s suffering?\'',
    tags=['绘画', '书法', '清朝'], tagsEn=['Painting', 'Calligraphy', 'Qing Dynasty'],
    personIds=['zheng-banqiao'], regionId='qing-dynasty',
    sourceIds=['src-qingshigao'], placeName='扬州', placeNameEn='Yangzhou', coords={'lat': 32.4, 'lng': 119.4})

# Liu Yong (1719-1805) - 刘墉 (宰相刘罗锅)
add('evt-liuyong-official', '刘墉——浓墨宰相', 'Liu Yong: The Ink-Dark Chancellor', 1751, 1805, importance=4,
    summary='刘墉是乾隆朝名臣，以书法和清廉著称，民间传说中「刘罗锅」形象深入人心。',
    summaryEn='Liu Yong was a famed Qianlong-era official, renowned for his calligraphy and incorruptibility.',
    tags=['政治', '书法', '清朝'], tagsEn=['Politics', 'Calligraphy', 'Qing Dynasty'],
    personIds=['liu-yong'], regionId='qing-dynasty',
    sourceIds=['src-qingshigao'], placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# Ji Xiaolan (1724-1805)
add('evt-jixiaolan-compile', '纪晓岚编纂《四库全书》', 'Ji Xiaolan Compiles Siku Quanshu', 1773, 1782, importance=5,
    summary='纪晓岚任《四库全书》总纂官，历时十年完成这部中国历史上规模最大的丛书。',
    summaryEn='Ji Xiaolan served as chief editor of the Siku Quanshu, completing the largest book collection in Chinese history over ten years.',
    tags=['学术', '编纂', '清朝'], tagsEn=['Scholarship', 'Compilation', 'Qing Dynasty'],
    personIds=['ji-xiaolan'], regionId='qing-dynasty',
    sourceIds=['src-qingshigao'], placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# Lin Zexu (1785-1850)
add('evt-linzexu-opium', '林则徐虎门销烟', 'Lin Zexu Destroys Opium at Humen', 1839, importance=5,
    summary='林则徐在虎门海滩当众销毁英国鸦片两万余箱，成为中国近代史上最壮烈的抵抗外来侵略的象征。',
    summaryEn='Lin Zexu publicly destroyed over 20,000 chests of British opium at Humen Beach, becoming a national hero.',
    tags=['政治', '禁烟', '清朝'], tagsEn=['Politics', 'Anti-Opium', 'Qing Dynasty'],
    personIds=['lin-zexu'], regionId='qing-dynasty',
    sourceIds=['src-qingshigao'], placeName='虎门（今广东东莞）', placeNameEn='Humen, modern Dongguan', coords={'lat': 22.8, 'lng': 113.6})

# Zeng Guofan (1811-1872)
add('evt-zengguofan-taiping', '曾国藩平定太平天国', 'Zeng Guofan Defeats the Taiping', 1853, 1864, importance=5,
    summary='曾国藩组建湘军，经过十余年苦战最终攻破天京平定太平天国，挽救了清朝。',
    summaryEn='Zeng Guofan raised the Hunan Army and after a decade of bitter warfare captured Nanjing, crushing the Taiping Rebellion.',
    tags=['军事', '清朝'], tagsEn=['Military', 'Qing Dynasty'],
    personIds=['zeng-guofan'], regionId='qing-dynasty',
    sourceIds=['src-qingshigao'], placeName='天京（今南京）', placeNameEn='Nanjing', coords={'lat': 32.0, 'lng': 118.7})

# Zuo Zongtang (1812-1885)
add('evt-zuozongtang-xinjiang', '左宗棠收复新疆', 'Zuo Zongtang Recovers Xinjiang', 1875, 1878, importance=5,
    summary='左宗棠抬棺出征收复新疆，粉碎了阿古柏分裂政权，为中华民族保住了六分之一的国土。',
    summaryEn='Zuo Zongtang marched west with his coffin, recovering Xinjiang from Yakub Beg and preserving one-sixth of China\'s territory.',
    tags=['军事', '清朝'], tagsEn=['Military', 'Qing Dynasty'],
    personIds=['zuo-zongtang'], regionId='qing-dynasty',
    sourceIds=['src-qingshigao'], placeName='新疆', placeNameEn='Xinjiang', coords={'lat': 43.8, 'lng': 87.6})

# Qing Guangxu (1871-1908)
add('evt-qingguangxu-reform', '戊戌变法', 'Hundred Days\' Reform', 1898, importance=5,
    summary='光绪帝和康有为梁启超推动103天改革，企图将中国从君主专制转向君主立宪，被慈禧政变镇压。',
    summaryEn='Emperor Guangxu with Kang Youwei and Liang Qichao launched 103 days of reforms, crushed by Empress Dowager Cixi\'s coup.',
    tags=['政治', '改革', '清朝'], tagsEn=['Politics', 'Reform', 'Qing Dynasty'],
    personIds=['qing-guangxu', 'kang-youwei', 'liang-qichao'], regionId='qing-dynasty',
    sourceIds=['src-qingshigao'], placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# Qing Puyi (1906-1967)
add('evt-qingpuyi-abdicate', '溥仪退位——清朝灭亡', 'Puyi Abdicates: End of Qing Dynasty', 1912, importance=5,
    summary='辛亥革命后六岁的溥仪颁布退位诏书，清朝灭亡，中国两千多年的帝制终结。',
    summaryEn='After the Xinhai Revolution, the six-year-old Puyi issued the abdication edict, ending both the Qing dynasty and imperial China.',
    tags=['政治', '灭亡', '清朝'], tagsEn=['Politics', 'Fall', 'Qing Dynasty'],
    personIds=['qing-puyi'], regionId='qing-dynasty',
    sourceIds=['src-qingshigao'], placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

output_file = os.path.join(OUTPUT_DIR, '_detailedEvents_yuan_ming_qing.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_events, f, ensure_ascii=False, indent=2)
print(f"Yuan/Ming/Qing: {len(all_events)} detailed events written to {output_file}")
