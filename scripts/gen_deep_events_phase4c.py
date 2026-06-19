#!/usr/bin/env python3
"""Phase 4 Part 3: More deep events for Tang/Song/Ming/Qing figures"""
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

SOS = ['src-ss']; MS = ['src-mingshi']; QS = ['src-qingshigao']
JS = ['src-jiutangshu']; SS = ['src-xintangshu']; YS = ['src-yuanshi']

# ===== TANG =====

# 姚崇 (650-721) - 开元名相
add('evt-yaochong-chancellor', '姚崇拜相', 'Yao Chong Becomes Chancellor', 713, 716, importance=5,
    summary='姚崇是开元盛世的首席设计师，向唐玄宗提出「十事要说」作为施政纲领。',
    summaryEn='Yao Chong was the chief architect of the Kaiyuan Golden Age, presenting a ten-point governing platform to Emperor Xuanzong.',
    desc='713年唐玄宗任命姚崇为宰相。姚崇提出了十条施政纲领（「十事要说」）——包括禁止宦官干政、停建佛寺道观、广开言路等。玄宗全部接受。姚崇在相位三年，奠定了开元盛世的基础。他与宋璟并称「姚宋」，是中国历史上最负盛名的宰相组合之一。',
    tags=['政治', '宰相', '唐朝'], tagsEn=['Politics', 'Chancellor', 'Tang Dynasty'],
    personIds=['yao-chong-650'], regionId='tang-dynasty', sourceIds=JS + SS + ['src-zztj'],
    placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# 宋璟 (663-737)
add('evt-songjing-chancellor', '宋璟守正不阿', 'Song Jing the Incorruptible Chancellor', 716, 720, importance=4,
    summary='宋璟继姚崇之后为相，以刚正不阿著称，与姚崇并称「姚宋」。',
    summaryEn='Song Jing succeeded Yao Chong as chancellor, famed for his incorruptible rectitude.',
    desc='宋璟继姚崇之后为相，继续推进开元之治。他为人刚正——曾当面拒绝玄宗为表彰其功绩而立的碑文。他对选拔官吏极为严格，从不私授官职。司马光在《资治通鉴》中评价「姚宋相继为相……使赋役宽平，刑罚清省，百姓富庶」。',
    tags=['政治', '宰相', '唐朝'], tagsEn=['Politics', 'Chancellor', 'Tang Dynasty'],
    personIds=['song-jing-663'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# 张九龄 (678-740)
add('evt-zhangjiuling-chancellor', '张九龄——开元最后一位贤相', 'Zhang Jiuling: Last Wise Chancellor of Kaiyuan', 733, 736, importance=4,
    summary='张九龄以「海上生明月，天涯共此时」传世，是开元盛世最后一位贤相，后为李林甫所排挤。',
    summaryEn='Zhang Jiuling, famed for his poetry, was the last wise chancellor of the Kaiyuan era before being sidelined by Li Linfu.',
    desc='张九龄以进士入仕，733年拜相。他为人正直——察觉安禄山有反相后曾向玄宗警告，但未被采纳。736年被李林甫排挤出朝，此后李林甫独揽朝政十九年——开元之治由此走向衰落。他的《感遇》十二首和《望月怀远》是唐诗中的珍品。',
    tags=['政治', '文学', '唐朝'], tagsEn=['Politics', 'Literature', 'Tang Dynasty'],
    personIds=['zhang-jiu-ling-678'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# 王维 (701-761)
add('evt-wangwei-jinshi', '王维进士及第', 'Wang Wei Passes Imperial Exam', 721, importance=3,
    summary='王维二十一岁中进士，任太乐丞，是盛唐山水田园诗派的代表。',
    summaryEn='Wang Wei passed the imperial exam at 21 and became Director of the Imperial Music Bureau.',
    tags=['科举', '唐朝'], tagsEn=['Civil Exam', 'Tang Dynasty'],
    personIds=['wang-wei-701'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

add('evt-wangwei-exile', '王维陷贼与免罪', 'Wang Wei Captured During Rebellion', 756, importance=4,
    summary='安史之乱中王维被叛军俘虏，被迫接受伪职。乱平后因《凝碧池》诗中的忠诚之意得以免罪。',
    summaryEn='Captured by An Lushan\'s rebels, Wang Wei was forced to serve. After the rebellion, his poem at Ningbi Pool proved his loyalty and saved him.',
    desc='安禄山攻陷长安后王维被俘。叛军在凝碧池设宴庆祝，乐工雷海青摔碎乐器痛哭——被当场肢解。王维闻之写下「万户伤心生野烟，百僚何日更朝天」。乱平后这首诗成为他为唐朝效忠的铁证。加上其弟王缙愿削官赎兄之罪，王维仅被降职，未被处死。',
    tags=['政治', '安史之乱', '唐朝'], tagsEn=['Politics', 'An Lushan Rebellion', 'Tang Dynasty'],
    personIds=['wang-wei-701'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

add('evt-wangwei-poetry', '王维——诗中有画画中有诗', 'Wang Wei: Poetry in Painting, Painting in Poetry', 740, 761, importance=4,
    summary='王维的诗画被苏轼评为「诗中有画，画中有诗」，是盛唐山水诗和南宗文人画的双重高峰。',
    summaryEn='Su Shi praised Wang Wei\'s work as \'poetry in painting, painting in poetry\' — a dual master of landscape verse and literati painting.',
    desc='王维晚年隐居终南山辋川别业，过着半官半隐的生活。他开创了水墨山水画——被董其昌推为南宗鼻祖。他的诗以空灵禅意著称，《山居秋暝》「明月松间照，清泉石上流」、《使至塞上》「大漠孤烟直，长河落日圆」都是不朽名句。',
    tags=['文学', '绘画', '唐朝'], tagsEn=['Literature', 'Painting', 'Tang Dynasty'],
    personIds=['wang-wei-701'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='辋川（今陕西蓝田）', placeNameEn='Wangchuan, modern Lantian', coords={'lat': 34.1, 'lng': 109.3})

# 岑参 (715-770)
add('evt-censhen-frontier', '岑参边塞诗人', 'Cen Shen: Frontier Poet', 749, 756, importance=4,
    summary='岑参两度出塞，以「忽如一夜春风来，千树万树梨花开」等边塞诗与高适齐名。',
    summaryEn='Cen Shen served twice on the frontier; his poetry like \'Suddenly as spring breeze comes overnight, thousands of pear trees bloom\' made him Gao Shi\'s peer.',
    desc='岑参两度出塞——先在安西节度使高仙芝幕府，后在北庭节度使封常清幕府。西域的奇丽风光和艰苦的军旅生活成为他诗歌的灵魂。《白雪歌送武判官归京》《走马川行奉送封大夫出师西征》以瑰丽的想象和磅礴的气势在中国诗歌史上独树一帜。',
    tags=['文学', '诗歌', '唐朝'], tagsEn=['Literature', 'Poetry', 'Tang Dynasty'],
    personIds=['cen-shen-715'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='西域', placeNameEn='Western Regions', coords={'lat': 42.0, 'lng': 86.0})

# 贾岛 (779-843)
add('evt-jiadao-poetry', '贾岛——推敲', 'Jia Dao: The \'Push-Knock\' Poet', 810, 843, importance=4,
    summary='贾岛以「鸟宿池边树，僧敲月下门」中「推敲」二字的反复斟酌，成为汉语中「推敲」一词的典故来源。',
    summaryEn='Jia Dao\'s agonizing over the words \'push\' versus \'knock\' in his poem gave Chinese the word \'tuīqiāo\' (to deliberate).',
    desc='贾岛早年出家为僧，后还俗参加科举屡试不第。他是唐代最极端的苦吟诗人——传说他在长安街头骑驴苦吟「鸟宿池边树，僧推月下门」时，为推敲「推」与「敲」二字，冲撞了京兆尹韩愈的仪仗队。韩愈不但不怪罪反而帮他选定「敲」字。汉语中「推敲」一词由此而来。',
    tags=['文学', '诗歌', '唐朝'], tagsEn=['Literature', 'Poetry', 'Tang Dynasty'],
    personIds=['jia-dao-779'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# 李贺 (790-816)
add('evt-lihe-poetry', '李贺——诗鬼', 'Li He: The Ghostly Poet', 808, 816, importance=4,
    summary='李贺是唐代最富想象力的诗人之一，以奇诡凄艳的风格被称为「诗鬼」，二十七岁英年早逝。',
    summaryEn='Li He was one of the Tang\'s most imaginative poets, known as the \'Ghostly Poet\' for his bizarre, haunting style. He died at 27.',
    desc='李贺是唐宗室远支，因父名「晋肃」与「进士」谐音，被妒才者以此为由剥夺了科举资格。他年仅二十七岁就因病去世——但在短暂的生命中留下了「大漠沙如雪，燕山月似钩」「衰兰送客咸阳道，天若有情天亦老」等不朽诗句。',
    tags=['文学', '诗歌', '唐朝'], tagsEn=['Literature', 'Poetry', 'Tang Dynasty'],
    personIds=['li-he-790'], regionId='tang-dynasty', sourceIds=JS + SS,
    placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# ===== SONG =====

# 欧阳询 (557-641) was already done, let's add more Song figures

# 秦观 (1049-1100)
add('evt-qinguan-poetry', '秦观——婉约词宗', 'Qin Guan: Master of Subtle Lyrics', 1070, 1100, importance=4,
    summary='秦观是苏门四学士之一，以婉约词著称，「两情若是久长时，又岂在朝朝暮暮」传诵千古。',
    summaryEn='Qin Guan, one of Su Shi\'s four disciples, was a master of subtle love lyrics.',
    desc='秦观是苏轼最赏识的门生之一。他的词以婉约深婉著称——《鹊桥仙》「纤云弄巧飞星传恨」、《踏莎行》「郴江幸自绕郴山，为谁流下潇湘去」都是千古名篇。苏轼对他的词评价极高。他一生仕途坎坷，屡遭贬谪。',
    tags=['文学', '词', '宋朝'], tagsEn=['Literature', 'Lyrics', 'Song Dynasty'],
    personIds=['qin-guan-1049'], regionId='song-dynasty', sourceIds=SOS,
    placeName='开封', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

# 杨万里 (1127-1206)
add('evt-yangwanli-poetry', '杨万里——诚斋体', 'Yang Wanli Creates the Chengzhai Style', 1160, 1206, importance=4,
    summary='杨万里与陆游、范成大、尤袤并称「中兴四大诗人」，以清新活泼的「诚斋体」独树一帜。',
    summaryEn='Yang Wanli was one of the \'Four Great Poets of the Southern Song Restoration\', famous for his fresh, lively Chengzhai style.',
    desc='杨万里绍兴二十四年进士，历任国子博士、秘书少监等职。他一生作诗两万余首——虽然大部分已佚失——但他的「诚斋体」以浅近自然的语言捕捉自然万物的生动瞬间。「小荷才露尖尖角，早有蜻蜓立上头」「接天莲叶无穷碧，映日荷花别样红」至今脍炙人口。',
    tags=['文学', '诗歌', '宋朝'], tagsEn=['Literature', 'Poetry', 'Song Dynasty'],
    personIds=['yang-wan-li-1127'], regionId='song-dynasty', sourceIds=SOS,
    placeName='临安（今杭州）', placeNameEn='Lin\'an, modern Hangzhou', coords={'lat': 30.2, 'lng': 120.2})

# 范成大 (1126-1193)
add('evt-fanchengda-poetry', '范成大——田园诗巨匠', 'Fan Chengda: Master of Pastoral Poetry', 1160, 1193, importance=4,
    summary='范成大是中兴四大诗人之一，其《四时田园杂兴》六十首是中国田园诗的巅峰之作。',
    summaryEn='Fan Chengda wrote 60 Seasonal Pastoral Poems — the pinnacle of Chinese pastoral verse.',
    desc='范成大绍兴二十四年进士。1170年他出使金国不辱使命，归来后写下了《揽辔录》。晚年隐居苏州石湖，自号石湖居士。他的《四时田园杂兴》六十首以白描手法记录了江南农民一年四季的劳动生活——是中国文学史上最系统的田园诗组。',
    tags=['文学', '诗歌', '宋朝'], tagsEn=['Literature', 'Poetry', 'Song Dynasty'],
    personIds=['fan-cheng-da-1126'], regionId='song-dynasty', sourceIds=SOS,
    placeName='苏州石湖', placeNameEn='Stone Lake, Suzhou', coords={'lat': 31.3, 'lng': 120.6})

# 姜夔 (1155-1221)
add('evt-jiangkui-poetry', '姜夔——清空骚雅', 'Jiang Kui: The Pure and Elegant Lyricist', 1180, 1221, importance=4,
    summary='姜夔是南宋格律词派的代表，精通音律，能自度曲。其词清空骚雅，开后世词学一派。',
    summaryEn='Jiang Kui led the Southern Song formalist lyric school, composing both lyrics and music. His pure, elegant style founded a major tradition.',
    desc='姜夔终身布衣，以卖字和朋友接济为生。他精通音律，能自己作曲——《扬州慢》《暗香》《疏影》都是他的自度曲。他的词不追求苏辛的豪放也不效仿柳周的俚俗，而是以「清空」「骚雅」自成一派。1176年过扬州见金兵洗劫后的荒凉景象，写下了「自胡马窥江去后，废池乔木，犹厌言兵」的千古名篇。',
    tags=['文学', '词', '音乐', '宋朝'], tagsEn=['Literature', 'Lyrics', 'Music', 'Song Dynasty'],
    personIds=['jiang-kui-1155'], regionId='song-dynasty', sourceIds=SOS,
    placeName='扬州', placeNameEn='Yangzhou', coords={'lat': 32.4, 'lng': 119.4})

# ===== MING =====

# 李东阳 (1447-1516) - 茶陵派领袖
add('evt-lidongyang-literature', '李东阳——茶陵派领袖', 'Li Dongyang: Leader of Chaling School', 1470, 1516, importance=4,
    summary='李东阳历仕四朝官至内阁首辅，其诗文开创茶陵派，是台阁体到前七子的过渡人物。',
    summaryEn='Li Dongyang served four emperors as Grand Secretary and led the Chaling literary school, bridging early and mid-Ming literary movements.',
    tags=['政治', '文学', '明朝'], tagsEn=['Politics', 'Literature', 'Ming Dynasty'],
    personIds=['li-dong-yang-1447'], regionId='ming-dynasty', sourceIds=MS,
    placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# 王世贞 (1526-1590)
add('evt-wangshizhen-literature', '王世贞——后七子领袖', 'Wang Shizhen: Leader of the Latter Seven Masters', 1550, 1590, importance=4,
    summary='王世贞是后七子的领袖，独主文坛二十年，其史学著作《弇山堂别集》和文学评论影响深远。',
    summaryEn='Wang Shizhen led the Latter Seven Masters, dominating the literary world for 20 years.',
    desc='王世贞嘉靖二十六年进士。他继李攀龙之后主盟文坛二十年，推动文学复古运动到达顶峰。他著作等身——除诗文外还有史学著作《弇山堂别集》《嘉靖以来首辅传》。据说他是《金瓶梅》的可能作者之一（此说虽有争议但流传甚广）。',
    tags=['文学', '史学', '明朝'], tagsEn=['Literature', 'Historiography', 'Ming Dynasty'],
    personIds=['wang-shi-zhen-1526'], regionId='ming-dynasty', sourceIds=MS,
    placeName='太仓', placeNameEn='Taicang', coords={'lat': 31.4, 'lng': 121.1})

# ===== QING =====

# 孔尚任 (1648-1718)
add('evt-kongshangren-drama', '孔尚任著《桃花扇》', 'Kong Shangren Writes Peach Blossom Fan', 1699, importance=5,
    summary='孔尚任经十年三易其稿完成历史剧《桃花扇》，以侯方域和李香君的爱情写南明兴亡。',
    summaryEn='Kong Shangren spent a decade writing Peach Blossom Fan, a historical drama about love and the fall of the Southern Ming.',
    desc='孔尚任是孔子六十四代孙。1684年康熙南巡至曲阜祭孔时他奉命讲经，被破格提拔为国子监博士。他历时十年三易其稿完成了《桃花扇》——以明末复社文人侯方域与秦淮名妓李香君的爱情为线索，全景式展现了南明弘光朝的政治腐败和灭亡过程。《桃花扇》与洪昇的《长生殿》并称清代传奇双璧。',
    tags=['文学', '戏曲', '清朝'], tagsEn=['Literature', 'Drama', 'Qing Dynasty'],
    personIds=['kong-shang-ren-1648'], regionId='qing-dynasty', sourceIds=QS,
    placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# 洪昇 (1645-1704)
add('evt-hongsheng-drama', '洪昇著《长生殿》', 'Hong Sheng Writes Palace of Eternal Life', 1688, importance=5,
    summary='洪昇历时十余年完成传奇《长生殿》，以唐玄宗和杨贵妃的爱情写历史兴亡。',
    summaryEn='Hong Sheng spent over a decade writing Palace of Eternal Life about Tang Xuanzong and Yang Guifei.',
    desc='洪昇出身钱塘世家，国子监生。他历时十余年三易其稿，在1688年完成《长生殿》。该剧以唐玄宗与杨贵妃的爱情为主线，以白居易《长恨歌》为蓝本，融合了安史之乱的历史背景。该剧一出便轰动京师——「家家收拾起，户户不提防」成为流行语。与孔尚任的《桃花扇》并称为清代传奇双璧。',
    tags=['文学', '戏曲', '清朝'], tagsEn=['Literature', 'Drama', 'Qing Dynasty'],
    personIds=['hong-sheng-1645'], regionId='qing-dynasty', sourceIds=QS,
    placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# 袁枚 (1716-1797)
add('evt-yuanmei-literature', '袁枚——性灵派', 'Yuan Mei: The Nature and Spirit School', 1740, 1797, importance=4,
    summary='袁枚是乾隆诗坛三大家之一，倡导性灵说，其《随园诗话》和《随园食单》影响深远。',
    summaryEn='Yuan Mei was one of the three great poets of the Qianlong era, advocating the \'Nature and Spirit\' theory.',
    desc='袁枚乾隆四年进士，曾任县令数年后辞官归隐，在南京购置随园。他倡导「性灵说」——主张诗歌应抒发真性情而非模拟古人。他的《随园诗话》是清代最重要的诗论著作之一，《随园食单》则是中国古代最著名的美食著作。',
    tags=['文学', '诗歌', '清朝'], tagsEn=['Literature', 'Poetry', 'Qing Dynasty'],
    personIds=['yuan-mei-1716'], regionId='qing-dynasty', sourceIds=QS,
    placeName='南京随园', placeNameEn='Sui Garden, Nanjing', coords={'lat': 32.0, 'lng': 118.7})

# 顾炎武 (1613-1682)
add('evt-guyanwu-scholarship', '顾炎武——天下兴亡匹夫有责', 'Gu Yanwu: Every Man Responsible for His Country', 1645, 1682, importance=5,
    summary='顾炎武是明末清初三大家之一，提出「天下兴亡，匹夫有责」，其《日知录》开创了清代朴学。',
    summaryEn='Gu Yanwu, one of the three great scholars of the Ming-Qing transition, coined \'every man bears responsibility for the fate of his country.\'',
    desc='顾炎武本名顾绛，明亡后改名炎武。他拒绝仕清，遍游华北各地考察地理民生——「以二马二骡载书自随」。他的《日知录》三十二卷是积三十余年之功写成的读书札记，内容涵盖经学、史学、地理、经济——被视为清代考据学的开山之作。他的《天下郡国利病书》则是一部系统的政治地理学著作。',
    tags=['学术', '思想', '明末清初'], tagsEn=['Scholarship', 'Thought', 'Ming-Qing Transition'],
    personIds=['gu-yan-wu-1613'], regionId='qing-dynasty', sourceIds=QS,
    placeName='昆山', placeNameEn='Kunshan', coords={'lat': 31.4, 'lng': 120.9})

# 黄宗羲 (1610-1695)
add('evt-huangzongxi-thought', '黄宗羲著《明夷待访录》', 'Huang Zongxi: A Plan for the Prince', 1663, importance=5,
    summary='黄宗羲的《明夷待访录》批判君主专制，提出「天下为主君为客」，是中国早期启蒙思想的代表作。',
    summaryEn='Huang Zongxi\'s \'Waiting for the Dawn\' criticized absolute monarchy, arguing \'the realm is the master, the ruler the guest.\'',
    desc='黄宗羲的抗清经历极为传奇——他曾组织义军在四明山抵抗清兵。失败后隐居著述。《明夷待访录》以犀利的笔锋批判了两千年的君主专制——「为天下之大害者，君而已矣」。他还编纂了《明儒学案》——中国第一部系统的学术思想史。他与顾炎武、王夫之并称明末清初三大家。',
    tags=['学术', '思想', '明末清初'], tagsEn=['Scholarship', 'Thought', 'Ming-Qing Transition'],
    personIds=['huang-zong-xi-1610'], regionId='qing-dynasty', sourceIds=QS,
    placeName='余姚', placeNameEn='Yuyao', coords={'lat': 30.0, 'lng': 121.1})

# ===== YUAN =====

# 王实甫 (1260-1336)
add('evt-wangshifu-drama', '王实甫著《西厢记》', 'Wang Shifu Writes Romance of the Western Chamber', 1295, 1307, importance=5,
    summary='王实甫的《西厢记》是中国最伟大的爱情戏曲，以「愿天下有情人终成眷属」的主题影响深远。',
    summaryEn='Wang Shifu\'s Western Chamber is China\'s greatest love drama, with its wish that \'all lovers under heaven be united.\'',
    desc='《西厢记》改编自元稹的《莺莺传》，讲述了张生与崔莺莺在红娘帮助下冲破礼教束缚的爱情故事。王实甫以优美的文辞和精妙的结构将简单的故事升华为中国戏曲史上的巅峰之作——全剧五本二十一折，体制之宏大在元杂剧中独一无二。',
    tags=['文学', '戏曲', '元朝'], tagsEn=['Literature', 'Drama', 'Yuan Dynasty'],
    personIds=['wang-shi-fu-1260'], regionId='yuan-dynasty', sourceIds=YS,
    placeName='大都（今北京）', placeNameEn='Dadu, modern Beijing', coords={'lat': 39.9, 'lng': 116.4})

# 马致远 (1250-1321)
add('evt-mazhiyuan-drama', '马致远——《汉宫秋》与《天净沙·秋思》', 'Ma Zhiyuan: Autumn in the Han Palace', 1280, 1321, importance=4,
    summary='马致远是元曲四大家之一，《汉宫秋》写王昭君故事，《天净沙·秋思》被誉为「秋思之祖」。',
    summaryEn='Ma Zhiyuan was one of the Four Great Yuan Playwrights; his \'Autumn Thoughts\' is hailed as the ancestor of all autumn poems.',
    desc='马致远的《汉宫秋》以王昭君出塞为题材，借古讽今表达了民族情感。他的散曲成就甚至高过杂剧——《天净沙·秋思》「枯藤老树昏鸦，小桥流水人家，古道西风瘦马。夕阳西下，断肠人在天涯」全篇仅二十八字却写尽了漂泊与悲凉，被推为「秋思之祖」。',
    tags=['文学', '戏曲', '元朝'], tagsEn=['Literature', 'Drama', 'Yuan Dynasty'],
    personIds=['ma-zhi-yuan-1250'], regionId='yuan-dynasty', sourceIds=YS,
    placeName='大都（今北京）', placeNameEn='Dadu, modern Beijing', coords={'lat': 39.9, 'lng': 116.4})

print(f"Part 3 events: {len(all_events)}")

output_file = os.path.join(OUTPUT_DIR, '_deepEvents_phase4c.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_events, f, ensure_ascii=False, indent=2)
print(f"Written to {output_file}")
