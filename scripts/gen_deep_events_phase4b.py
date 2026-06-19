#!/usr/bin/env python3
"""
Phase 4 Part 2: Song/Ming/Qing dynasty deep biographical events
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

SOS = ['src-ss']         # 宋史
MS = ['src-mingshi']      # 明史
QS = ['src-qingshigao']   # 清史稿
YS = ['src-yuanshi']      # 元史

# ================================================================
# SONG DYNASTY (continued)
# ================================================================

# 梅尧臣 (1002-1060) - 宋诗开山祖师
add('evt-meiyaochen-poetry', '梅尧臣——宋诗开山', 'Mei Yaochen: Pioneer of Song Poetry', 1030, 1060, importance=4,
    summary='梅尧臣与苏舜钦齐名，倡导平淡含蓄的诗风，被尊为宋诗的开山祖师。',
    summaryEn='Mei Yaochen pioneered the restrained, subtle style of Song poetry, honored as the founding father of Song verse.',
    desc='梅尧臣以恩荫入仕，官至尚书都官员外郎。他反对西昆体的浮艳诗风，倡导平淡含蓄之美。欧阳修称他「穷而后工」——仕途越不顺诗写得越好。他的《田家语》《汝坟贫女》等诗反映了民间疾苦，《鲁山山行》则是山水诗的代表作。南宋刘克庄称他为宋诗的「开山祖师」。',
    tags=['文学', '诗歌', '宋朝'], tagsEn=['Literature', 'Poetry', 'Song Dynasty'],
    personIds=['mei-yao-chen-1002'], regionId='song-dynasty', sourceIds=SOS,
    placeName='宣城', placeNameEn='Xuancheng', coords={'lat': 30.9, 'lng': 118.7})

# 晏殊 (991-1055)
add('evt-yanshu-chancellor', '晏殊——太平宰相', 'Yan Shu: Chancellor of Peace', 1020, 1055, importance=4,
    summary='晏殊七岁能文，十四岁以神童召试赐同进士出身。官至宰相，提拔了范仲淹、欧阳修等一批人才。',
    summaryEn='Yan Shu was a child prodigy who passed the exam at 14, rose to chancellor, and mentored Fan Zhongyan and Ouyang Xiu.',
    desc='晏殊十四岁以神童身份被召试，赐同进士出身。他历仕真宗、仁宗两朝，官至同平章事兼枢密使。虽为人谨慎保守，但乐于提携后进——范仲淹、欧阳修、韩琦、富弼等一代名臣皆出其门下。他的词以婉约含蓄著称，《浣溪沙》「无可奈何花落去，似曾相识燕归来」流传千古。',
    tags=['政治', '文学', '宋朝'], tagsEn=['Politics', 'Literature', 'Song Dynasty'],
    personIds=['yan-shu-991'], regionId='song-dynasty', sourceIds=SOS,
    placeName='开封', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

# 柳永 (987-1053)
add('evt-liuyong-lyrics', '柳永——凡有井水处即能歌柳词', 'Liu Yong: The People\'s Lyricist', 1010, 1053, importance=4,
    summary='柳永是北宋第一位专业词人，大量创作慢词，其词在当时「凡有井水处即能歌柳词」。',
    summaryEn='Liu Yong was the Northern Song\'s first professional lyricist, pioneering the slow-ci form. His lyrics were sung wherever people gathered.',
    desc='柳永原名柳三变，因科举落第自称「奉旨填词柳三变」混迹于歌楼酒肆。他大量创作慢词——扩展了词的表现力和容量。《雨霖铃》「今宵酒醒何处？杨柳岸晓风残月」、《望海潮》「有三秋桂子十里荷花」都是千古名篇。他的词在当时传唱极广——「凡有井水处即能歌柳词」。',
    tags=['文学', '词', '宋朝'], tagsEn=['Literature', 'Lyrics', 'Song Dynasty'],
    personIds=['liu-yong-987'], regionId='song-dynasty', sourceIds=SOS,
    placeName='汴京', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

# 周邦彦 (1056-1121)
add('evt-zhoubangyan-music', '周邦彦——词中老杜', 'Zhou Bangyan: Master of Musical Lyrics', 1080, 1121, importance=4,
    summary='周邦彦精通音律，主持大晟府，规范词调音律，被尊为「词中老杜」。',
    summaryEn='Zhou Bangyan was a master of musical prosody who headed the Imperial Music Bureau and standardized lyric forms.',
    desc='周邦彦少年时博览百家之书，但因性格疏放不为州里推重。后献《汴都赋》受宋神宗赏识，由太学生升为太学正。宋徽宗时他主持大晟府——朝廷音乐机构——整理古调、创制新声、规范词律。他的词以格律精严著称，王国维称其「词中老杜」。',
    tags=['文学', '音乐', '宋朝'], tagsEn=['Literature', 'Music', 'Song Dynasty'],
    personIds=['zhou-bang-yan-1056'], regionId='song-dynasty', sourceIds=SOS,
    placeName='开封', placeNameEn='Kaifeng', coords={'lat': 34.8, 'lng': 114.3})

# ================================================================
# MING DYNASTY
# ================================================================

# 陈献章 (1428-1500) - 白沙先生
add('evt-chenxianzhang-philosophy', '陈献章——岭南第一大儒', 'Chen Xianzhang: Greatest Confucian of Lingnan', 1460, 1500, importance=4,
    summary='陈献章开创江门学派，是明代心学的先驱。他是岭南唯一从祀孔庙的学者。',
    summaryEn='Chen Xianzhang founded the Jiangmen School and pioneered Ming Dynasty philosophy of mind. He was the only Lingnan scholar enshrined in the Confucian Temple.',
    desc='陈献章两次会试不第后绝意科举，回乡潜心学问。他主张「学贵自得」，强调内心体验，是王阳明心学的重要先驱。他用圭峰山茅草自制「茅龙笔」，书法苍劲有力。万历年间被批准从祀孔庙，是岭南唯一获此殊荣的学者。',
    tags=['哲学', '心学', '明朝'], tagsEn=['Philosophy', 'School of Mind', 'Ming Dynasty'],
    personIds=['chen-xian-zhang-1428'], regionId='ming-dynasty', sourceIds=MS,
    placeName='广东新会', placeNameEn='Xinhui, Guangdong', coords={'lat': 22.5, 'lng': 113.0})

# 李梦阳 (1473-1529) - 前七子领袖
add('evt-limengyang-literature', '李梦阳——前七子领袖', 'Li Mengyang: Leader of the Former Seven Masters', 1493, 1529, importance=4,
    summary='李梦阳是明代文学复古运动「前七子」的领袖，主张「文必秦汉，诗必盛唐」。',
    summaryEn='Li Mengyang led the Former Seven Masters\' classical revival movement, advocating \'prose must emulate Qin-Han, poetry must emulate High Tang.\'',
    desc='李梦阳弘治六年进士，官至江西提学副使。他反对台阁体的空洞文风，与何景明、徐祯卿等并称「前七子」，掀起明代文学复古运动。他性格刚烈，因弹劾外戚张鹤龄而入狱，又因得罪刘瑾被罢官。其诗文沉雄豪放，是明代文学变革的关键人物。',
    tags=['文学', '复古运动', '明朝'], tagsEn=['Literature', 'Revival Movement', 'Ming Dynasty'],
    personIds=['li-meng-yang-1473'], regionId='ming-dynasty', sourceIds=MS,
    placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# 杨慎 (1488-1559) - 明代三大才子之首
add('evt-yangsheng-exile', '杨慎——大礼议事件被贬云南', 'Yang Shen Exiled Over Great Rites Controversy', 1524, importance=5,
    summary='杨慎因「大礼议」事件触怒嘉靖帝，被廷杖后流放云南永昌卫三十余年，在贬所著作等身。',
    summaryEn='Yang Shen angered the Jiajing Emperor in the Great Rites Controversy, was beaten at court and exiled to Yunnan for over 30 years.',
    desc='1524年杨慎因率领群臣在左顺门哭谏反对嘉靖帝尊生父为皇考（大礼议事件），被廷杖几乎打死，随后流放云南永昌卫。他在流放地度过了后半生——三十余年间博览群书著作等身。《临江仙·滚滚长江东逝水》即创作于此期间——后被罗贯中置于《三国演义》卷首，成为中国人最熟悉的词之一。',
    tags=['政治', '文学', '明朝'], tagsEn=['Politics', 'Literature', 'Ming Dynasty'],
    personIds=['yang-shen-1488'], regionId='ming-dynasty', sourceIds=MS,
    placeName='云南永昌', placeNameEn='Yongchang, Yunnan', coords={'lat': 25.1, 'lng': 99.1})

# 归有光 (1507-1571) - 唐宋派代表
add('evt-guiyouguang-prose', '归有光——唐宋派散文大家', 'Gui Youguang: Master of Tang-Song Style Prose', 1530, 1571, importance=4,
    summary='归有光以清新质朴的散文著称，《项脊轩志》「庭有枇杷树，吾妻死之年所手植也，今已亭亭如盖矣」传诵千古。',
    summaryEn='Gui Youguang was famed for his fresh, simple prose. His \'Record of Xiangji Studio\' contains one of Chinese literature\'s most moving passages.',
    desc='归有光八次会试不第，六十岁才中进士。他反对前后七子的拟古风气，推崇唐宋古文传统。《项脊轩志》《先妣事略》等散文以家常琐事抒写深情——看似平淡却感人至深。清人将其与唐顺之、王慎中并称「嘉靖三大家」，后又被列入「唐宋派」。',
    tags=['文学', '散文', '明朝'], tagsEn=['Literature', 'Prose', 'Ming Dynasty'],
    personIds=['gui-you-guang-1507'], regionId='ming-dynasty', sourceIds=MS,
    placeName='昆山', placeNameEn='Kunshan', coords={'lat': 31.4, 'lng': 120.9})

# 徐光启 (1562-1633)
add('evt-xuguangqi-science', '徐光启——中西科学交流先驱', 'Xu Guangqi: Pioneer of Sino-Western Science', 1600, 1633, importance=5,
    summary='徐光启是明代最杰出的科学家，与利玛窦合作翻译《几何原本》，编纂《农政全书》。',
    summaryEn='Xu Guangqi was Ming\'s greatest scientist, translating Euclid with Matteo Ricci and compiling the Complete Treatise on Agriculture.',
    desc='徐光启1600年在南京结识利玛窦后皈依天主教。他与利玛窦合作将欧几里得《几何原本》前六卷译成中文——点、线、面、直角等几何术语至今沿用。他主持编纂的《崇祯历书》系统引进了西方天文学。晚年编撰的《农政全书》60卷是古代中国最完备的农业百科全书。',
    tags=['科学', '天文学', '数学', '明朝'], tagsEn=['Science', 'Astronomy', 'Mathematics', 'Ming Dynasty'],
    personIds=['xu-guang-qi-1562'], regionId='ming-dynasty', sourceIds=MS,
    placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# 董其昌 (1555-1636)
add('evt-dongqichang-art', '董其昌——松江画派领袖', 'Dong Qichang: Leader of Songjiang School', 1580, 1636, importance=4,
    summary='董其昌是晚明最著名的书画家和艺术理论家，其「南北宗论」影响了此后三百年的中国绘画史。',
    summaryEn='Dong Qichang was the late Ming\'s most influential painter-calligrapher and theorist; his \'Southern and Northern Schools\' theory shaped three centuries of Chinese art.',
    desc='董其昌万历十七年进士，官至南京礼部尚书。他在书画上集大成——书法博采众长自成一家，绘画融会宋元开创松江画派。他的「南北宗论」将中国山水画分为南北两宗，推崇南宗文人画为「正宗」——这一理论影响了此后三百年的中国绘画审美。',
    tags=['绘画', '书法', '艺术', '明朝'], tagsEn=['Painting', 'Calligraphy', 'Art', 'Ming Dynasty'],
    personIds=['dong-qi-chang-1555'], regionId='ming-dynasty', sourceIds=MS,
    placeName='松江（今上海）', placeNameEn='Songjiang, modern Shanghai', coords={'lat': 31.0, 'lng': 121.2})

# ================================================================
# QING DYNASTY
# ================================================================

# 张廷玉 (1672-1755)
add('evt-zhangtingyu-official', '张廷玉——三朝元老', 'Zhang Tingyu: Elder Statesman of Three Reigns', 1700, 1755, importance=5,
    summary='张廷玉历仕康雍乾三朝，任《明史》总纂官，完善军机处制度，是清朝唯一配享太庙的汉臣。',
    summaryEn='Zhang Tingyu served three emperors, compiled the Ming History, perfected the Grand Council system, and was the only Han official enshrined in the Qing Imperial Ancestral Temple.',
    desc='张廷玉康熙三十九年中进士。雍正朝极受重用——任保和殿大学士、军机大臣，完善了军机处的各项规章制度。乾隆初年以大学士掌翰林院。他是《明史》的总纂官。死后配享太庙——是清朝唯一获此殊荣的汉人。他的「为官之道」是「万言万当，不如一默」。',
    tags=['政治', '编纂', '清朝'], tagsEn=['Politics', 'Compilation', 'Qing Dynasty'],
    personIds=['zhang-ting-yu-1672'], regionId='qing-dynasty', sourceIds=QS,
    placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# 吴三桂 (1612-1678)
add('evt-wusangui-surrender', '吴三桂降清', 'Wu Sangui Surrenders to Qing', 1644, importance=5,
    summary='吴三桂引清兵入关，联合清军击败李自成，被封为平西王。此举被视为汉族士大夫最大的历史污点之一。',
    summaryEn='Wu Sangui opened Shanhai Pass to the Qing army, jointly defeating Li Zicheng. He was enfeoffed as Prince Who Pacifies the West.',
    desc='1644年李自成攻破北京，崇祯帝自缢。吴三桂本欲投降李自成，但听说爱妾陈圆圆被刘宗敏所夺（「冲冠一怒为红颜」），转而降清。他引清兵入山海关大败李自成，清军由此入主中原。',
    tags=['军事', '明末清初'], tagsEn=['Military', 'Ming-Qing Transition'],
    personIds=['wu-san-gui-1612'], regionId='qing-dynasty', sourceIds=QS + MS,
    placeName='山海关', placeNameEn='Shanhai Pass', coords={'lat': 40.0, 'lng': 119.7})

add('evt-wusangui-rebellion', '三藩之乱', 'Revolt of the Three Feudatories', 1673, 1678, importance=5,
    summary='吴三桂在云南起兵反清，自称周王，席卷南方数省，最终在衡州称帝后病亡。',
    summaryEn='Wu Sangui rebelled against the Qing in Yunnan, proclaiming himself King of Zhou. He swept through southern China before dying of illness.',
    desc='1673年康熙帝决定撤藩，吴三桂在云南起兵反清，自称「天下都招讨兵马大元帅」。耿精忠在福建、尚之信在广东响应，史称「三藩之乱」。吴三桂一度占领长江以南大半地区，1678年在衡州称帝，国号周。但不久病逝，其孙吴世璠继位后兵败自杀。',
    tags=['军事', '叛乱', '清朝'], tagsEn=['Military', 'Rebellion', 'Qing Dynasty'],
    personIds=['wu-san-gui-1612'], regionId='qing-dynasty', sourceIds=QS + MS,
    placeName='衡州（今湖南衡阳）', placeNameEn='Hengzhou, modern Hengyang', coords={'lat': 26.9, 'lng': 112.6})

# 纳兰性德 (1655-1685)
add('evt-nalanxingde-poetry', '纳兰性德——满清第一词人', 'Nalan Xingde: Greatest Manchu Poet', 1676, 1685, importance=4,
    summary='纳兰性德是清代最杰出的词人，其词哀感顽艳，「人生若只如初见」传诵至今。',
    summaryEn='Nalan Xingde was the Qing\'s greatest lyricist; his line \'If life could remain as first meeting\' is immortal.',
    desc='纳兰性德是康熙朝大学士明珠之子，二十二岁中进士。他出身满洲贵族却倾心汉文化，与顾贞观、朱彝尊等汉族文人交厚。他的词以真情见长——《饮水词》三百余首多写离愁别恨与人生感悟。「人生若只如初见，何事秋风悲画扇」「赌书消得泼茶香，当时只道是寻常」皆为千古名句。三十一岁英年早逝。',
    tags=['文学', '词', '清朝'], tagsEn=['Literature', 'Lyrics', 'Qing Dynasty'],
    personIds=['na-lan-xing-de-1655'], regionId='qing-dynasty', sourceIds=QS,
    placeName='北京', placeNameEn='Beijing', coords={'lat': 39.9, 'lng': 116.4})

# 曹雪芹 (1715-1763)
add('evt-caoxueqin-novel', '曹雪芹著《红楼梦》', 'Cao Xueqin Writes Dream of the Red Chamber', 1745, 1763, importance=5,
    summary='曹雪芹在贫病交加中创作《红楼梦》，是中国文学史上最伟大的小说，被誉为中国封建社会的百科全书。',
    summaryEn='Cao Xueqin wrote Dream of the Red Chamber in poverty and illness — the greatest novel in Chinese literature.',
    desc='曹雪芹出身江宁织造世家，少年时经历过极致的富贵繁华。雍正年间曹家被抄，他移居北京西郊黄叶村，靠卖画和朋友接济度日。他在「蓬牖茅椽、绳床瓦灶」的困苦中「披阅十载，增删五次」创作了《红楼梦》前八十回。幼子夭折后他在除夕之夜病逝，留下未完成的千古杰作。',
    tags=['文学', '小说', '清朝'], tagsEn=['Literature', 'Novel', 'Qing Dynasty'],
    personIds=['cao-xue-qin-1715', 'cao-xueqin'], regionId='qing-dynasty', sourceIds=QS,
    placeName='北京西郊', placeNameEn='Western Suburbs of Beijing', coords={'lat': 39.9, 'lng': 116.2})

# 吴敬梓 (1701-1754)
add('evt-wujingzi-novel', '吴敬梓著《儒林外史》', 'Wu Jingzi Writes The Scholars', 1736, 1754, importance=5,
    summary='吴敬梓创作了讽刺小说《儒林外史》，以辛辣笔触揭露科举制度对人性的扭曲。',
    summaryEn='Wu Jingzi wrote The Scholars, a satirical novel exposing the civil examination system\'s corruption of human nature.',
    desc='吴敬梓出身科举世家但乡试屡次落第。他将家产挥霍殆尽后移居南京，靠卖文和朋友周济为生。在穷困中他创作了《儒林外史》——以讽刺笔法刻画了科举制度下形形色色的文人丑态。「范进中举」至今仍是中国人最熟悉的文学形象之一。鲁迅称其为「秉持公心，指摘时弊」的杰作。',
    tags=['文学', '小说', '清朝'], tagsEn=['Literature', 'Novel', 'Qing Dynasty'],
    personIds=['wu-jing-zi-1701'], regionId='qing-dynasty', sourceIds=QS,
    placeName='南京', placeNameEn='Nanjing', coords={'lat': 32.0, 'lng': 118.7})

# ================================================================
# YUAN DYNASTY
# ================================================================

# 赵孟頫 (1254-1322)
add('evt-zhaomengfu-art', '赵孟頫——元代艺坛领袖', 'Zhao Mengfu: Yuan Dynasty Art Leader', 1286, 1322, importance=5,
    summary='赵孟頫是宋宗室后裔出仕元朝，其书法和绘画开创了元代新风，楷书被列为「赵体」。',
    summaryEn='Zhao Mengfu, a Song imperial descendant who served the Yuan, revolutionized calligraphy and painting; his regular script became known as \'Zhao Style\'.',
    desc='赵孟頫是宋太祖赵匡胤十一世孙，南宋灭亡后隐居在家。1286年被忽必烈征召入朝，因宋宗室身份备受争议。他的书法圆润秀美——「赵体」与欧、颜、柳并称楷书四大家。绘画上他倡导「复古」，以书法笔意入画，开创了元代文人画的新风格。妻子管道升也是著名画家。',
    tags=['书法', '绘画', '元朝'], tagsEn=['Calligraphy', 'Painting', 'Yuan Dynasty'],
    personIds=['zhao-meng-fu-1254'], regionId='yuan-dynasty', sourceIds=YS,
    placeName='大都（今北京）', placeNameEn='Dadu, modern Beijing', coords={'lat': 39.9, 'lng': 116.4})

# 关汉卿 (1210-1300)
add('evt-guanhanqing-drama', '关汉卿——元曲四大家之首', 'Guan Hanqing: Greatest Yuan Playwright', 1250, 1300, importance=5,
    summary='关汉卿是元代最伟大的戏曲家，《窦娥冤》《单刀会》等剧作至今仍在舞台上演。',
    summaryEn='Guan Hanqing was the Yuan\'s greatest playwright; his \'Snow in Midsummer\' and other plays remain on stage today.',
    desc='关汉卿是「元曲四大家」之首。他长期生活在大都，与歌伎伶人为伍，自称「普天下郎君领袖，盖世界浪子班头」。他一生创作杂剧六十余种——《窦娥冤》中的六月飞雪、《单刀会》中关羽的孤胆英雄、《救风尘》中赵盼儿的机智——塑造了中国戏剧史上最生动的人物群像。',
    tags=['文学', '戏曲', '元朝'], tagsEn=['Literature', 'Drama', 'Yuan Dynasty'],
    personIds=['guan-han-qing-1210'], regionId='yuan-dynasty', sourceIds=YS,
    placeName='大都（今北京）', placeNameEn='Dadu, modern Beijing', coords={'lat': 39.9, 'lng': 116.4})

# 黄公望 (1269-1354)
add('evt-huanggongwang-painting', '黄公望绘《富春山居图》', 'Huang Gongwang Paints Dwelling in the Fuchun Mountains', 1347, 1350, importance=5,
    summary='黄公望在八旬高龄创作《富春山居图》，被后世尊为中国山水画第一神品。',
    summaryEn='Huang Gongwang painted Dwelling in the Fuchun Mountains at age 80 — revered as the greatest Chinese landscape painting.',
    desc='黄公望早年曾任小吏，中年入全真教，晚年隐居富春江畔。1347年开始为师弟郑樗（无用师）绘制《富春山居图》，历时三四年才完成。画卷以干笔皴擦描绘富春江两岸的初秋景色——山峰起伏林峦深秀。这幅画被誉为中国山水画史上第一神品，后世分为两段分藏海峡两岸。',
    tags=['绘画', '元朝'], tagsEn=['Painting', 'Yuan Dynasty'],
    personIds=['huang-gong-wang-1269'], regionId='yuan-dynasty', sourceIds=YS,
    placeName='富春江', placeNameEn='Fuchun River', coords={'lat': 30.0, 'lng': 119.9})

print(f"Part 2 events: {len(all_events)}")

output_file = os.path.join(OUTPUT_DIR, '_deepEvents_phase4b.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_events, f, ensure_ascii=False, indent=2)
print(f"Written to {output_file}")
