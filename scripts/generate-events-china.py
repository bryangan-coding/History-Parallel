#!/usr/bin/env python3
"""Key Chinese historical events. ~18 events."""
def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")

events = []

def e(id, title, titleEn, startYear, endYear, region, tags, tagsEn, importance, summary, summaryEn, desc, descEn,
      persons=None, place=None, placeEn=None, coords=None, srcs=None, wiki="", conf=0.85):
    events.append(dict(id=id, title=title, titleEn=titleEn, startYear=startYear, endYear=endYear,
        regionId=region, tags=tags, tagsEn=tagsEn, importance=importance,
        summary=summary, summaryEn=summaryEn, description=desc, descriptionEn=descEn,
        personIds=persons or [], placeName=place or None, placeNameEn=placeEn or None,
        coordinates=coords or None, sourceIds=srcs or [],
        datePrecision="year", isApproximate=startYear < 0,
        wikidataQid=wiki, dataStatus="published", confidenceScore=conf,
        externalReferences=[], relatedEventIds=[]))

# Warring States
e("evt-changping", "长平之战", "Battle of Changping", -260, -260, "china",
  ["战争", "军事", "战国"], ["War", "Military", "Warring States"],
  5,
  "秦国白起大败赵国赵括，坑杀降卒四十余万——中国冷兵器时代最惨烈的歼灭战，奠定秦统一天下的军事基础。",
  "Qin general Bai Qi annihilated Zhao's army under Zhao Kuo, burying over 400,000 surrendered soldiers alive — history's most devastating pre-gunpowder annihilation battle, cementing Qin's path to unification.",
  "长平之战由秦赵两国争夺上党郡引发。赵国最初以老将廉颇防守，采取深沟高垒的消耗战术——秦军三年不能前进一步。秦国使用反间计散布谣言说廉颇老矣不敢出战而赵括才是秦军所惧——赵孝成王中计以纸上谈兵的赵括取代廉颇。白起佯败诱赵括全军出击后以奇兵截断后路——赵军被围四十六日断粮后投降。白起担心降卒反复便「挟诈而尽坑杀之」——有记载称人数达四十五万。赵国经此一战精锐尽失，再无力与秦抗衡。",
  "The Battle of Changping erupted from Qin-Zhao rivalry over Shangdang Commandery. Zhao initially deployed the veteran Lian Po in a defensive war of attrition — Qin could not advance an inch in three years. Qin employed a disinformation campaign spreading rumors that the old Lian Po was too timid to fight and only Zhao Kuo was truly feared — King Xiaocheng of Zhao fell for it, replacing Lian Po with the armchair strategist Zhao Kuo. Bai Qi feigned retreat, lured Zhao Kuo into full pursuit, then cut his rear with a flanking force — the surrounded Zhao army starved for 46 days before surrendering. Fearing the surrendered troops would revolt, Bai Qi 'deceived and buried them all alive' — recorded numbers reach 450,000. With its elite forces annihilated, Zhao never again challenged Qin.",
  ["bai-qi"], "长平（今山西高平）", "Changping (modern Gaoping, Shanxi)", {"lat": 35.8, "lng": 112.9},
  ["src-shiji"], "", 0.9)

e("evt-hongmen", "鸿门宴", "Banquet at Hongmen", -206, -206, "china",
  ["政治", "军事", "楚汉"], ["Politics", "Military", "Chu-Han"],
  5,
  "项羽和刘邦在灭亡秦朝后的首次直面交锋——项庄舞剑意在沛公的血色宴席，决定了此后五年的楚汉格局。",
  "The first direct confrontation between Xiang Yu and Liu Bang after Qin's fall — a blood-soaked banquet where Xiang Zhuang's sword dance targeted Liu Bang, setting the stage for the Chu-Han Contention.",
  "秦朝灭亡后项羽率四十万大军驻鸿门，刘邦十万人驻灞上。刘邦的左司马曹无伤向项羽告密刘邦欲王关中——项羽大怒欲攻。项伯（项羽的叔父）因受过张良救命之恩连夜通知张良，刘邦次日亲自到鸿门道歉。宴席上范增数次举玉玦示意项羽动手，项羽犹豫不决。范增派项庄舞剑意图刺杀——项伯以身遮蔽。张良急召樊哙闯入——樊哙「瞋目视项王，头发上指，目眦尽裂」的刚烈震慑了项羽。刘邦借上厕所之机脱逃——留下张良献上白璧玉斗致歉。范增将玉斗摔碎：「竖子不足与谋！夺项王天下者必沛公也！」",
  "After Qin's fall, Xiang Yu camped at Hongmen with 400,000 troops, Liu Bang at Bashang with 100,000. Liu Bang's officer Cao Wushang informed Xiang Yu that Liu intended to claim Guanzhong as king — Xiang Yu flew into a rage. Xiang Bo (Xiang Yu's uncle), indebted to Zhang Liang for once saving his life, warned Zhang Liang that night. Liu Bang personally visited Hongmen the next day to apologize. At the banquet, Fan Zeng repeatedly raised his jade ring signaling Xiang Yu to strike — Xiang Yu hesitated. Fan Zeng sent Xiang Zhuang to perform a sword dance and assassinate Liu Bang — Xiang Bo shielded him with his own body. Zhang Liang summoned Fan Kuai, who burst in glaring with hair bristling and eyes blazing — his ferocity stunned Xiang Yu. Liu Bang excused himself to the latrine and escaped — leaving Zhang Liang to present jade gifts in apology. Fan Zeng smashed the jade goblet: 'A worthless boy unworthy of counsel! The one who seizes Xiang Yu's realm shall be the Lord of Pei!'",
  ["xiang-yu", "zhang-liang", "fan-zeng"], "鸿门（今陕西临潼）", "Hongmen (modern Lintong, Shaanxi)", {"lat": 34.3, "lng": 109.2},
  ["src-shiji"], "", 0.85)

e("evt-wen-jing", "文景之治", "Rule of Wen and Jing", -180, -141, "han-dynasty",
  ["政治", "经济", "汉朝"], ["Politics", "Economy", "Han Dynasty"],
  4,
  "汉文帝和汉景帝四十年的轻徭薄赋休养生息政策，积累了汉朝强盛的国力基础。",
  "Four decades of light taxation and laissez-faire policy under Emperors Wen and Jing, accumulating the national strength for Han's golden age.",
  "文景之治是中国历史上第一个被后世称颂的「治世」。汉文帝即位后废除连坐法和肉刑、将田租从十五税一减为三十税一、甚至十三年不征田租。他本人节俭——一件龙袍穿二十余年，宫殿不加修缮。汉景帝延续其政策，虽经历了七国之乱的动荡，但仅三个月便平定叛乱并趁机大幅度削弱诸侯王权力。两代四十余年的积累使国家仓库的粮食「陈陈相因，至腐败不可食」、国库的铜钱「贯朽而不可校」——汉武帝正是凭借这份雄厚的家底发动了大规模的外征和文化建设。",
  "The Rule of Wen and Jing is Chinese history's first celebrated era of good governance. Emperor Wen abolished collective punishment and mutilation, reduced the land tax from 1/15 to 1/30 of harvest, and even suspended it entirely for thirteen years. He was personally frugal — wearing the same dragon robe for twenty years and refusing palace renovations. Emperor Jing continued these policies; though the Rebellion of the Seven States erupted, he crushed it in three months and used the opportunity to drastically curtail princely power. Four decades of accumulation filled state granaries until grain 'piled layer upon layer, rotting beyond edibility,' and treasury coins 'had their strings rot uncounted.' It was precisely this accumulated wealth that Emperor Wu deployed for his massive external campaigns and cultural projects.",
  ["han-wendi", "han-jingdi"], "长安", "Chang'an", {"lat": 34.3, "lng": 108.9},
  ["src-shiji", "src-hanshu"], "", 0.9)

e("evt-guangwu", "光武中兴", "Guangwu Restoration", 25, 57, "han-dynasty",
  ["政治", "东汉"], ["Politics", "Eastern Han"],
  4,
  "刘秀推翻王莽新朝重建汉室，以柔道治国恢复社会秩序，开创了稳定的东汉王朝。",
  "Liu Xiu overthrew Wang Mang's Xin dynasty, restored the Han, and governed with moderation to rebuild social order and inaugurate the stable Eastern Han.",
  "王莽改制的失败导致了全国性的大动乱——赤眉、绿林等农民起义席卷各地，天下群雄割据。刘秀是汉景帝的后代但家道已衰落为地方豪族。昆阳之战中他以不足万人击溃王莽四十二万大军——奠定声名。更始帝杀其兄刘縯后他强忍悲痛不露声色——随后在河北发展势力。公元25年他称帝重建汉朝、定都洛阳。此后他用了十二年逐一扫平赤眉、隗嚣、公孙述等割据势力——统一全国。他采取「退功臣而进文吏」的政策——以和平手段解除了开国将领的军权——避免了刘邦和后世朱元璋那样的血腥清洗。他释放奴婢、精兵简政、减免赋税——「光武中兴」在历代王朝的开国治理中堪称典范。",
  "Wang Mang's failed reforms triggered nationwide chaos — the Red Eyebrows, Lulin, and other peasant armies swept the land as warlords carved up the realm. Liu Xiu, descended from Emperor Jing but reduced to provincial gentry, won a stunning victory at Kunyang — routing Wang Mang's 420,000 troops with under 10,000. After the Gengshi Emperor executed his brother Liu Yan, Liu Xiu suppressed his grief and built power in Hebei. In 25 CE, he proclaimed himself emperor and established the capital at Luoyang. Over the next twelve years, he systematically eliminated the Red Eyebrows, Wei Xiao, Gongsun Shu, and other warlords — reunifying the realm. He adopted a 'retire martial meritocrats, advance civil officials' policy — peacefully retiring his founding generals and avoiding the bloody purges of Liu Bang or the later Zhu Yuanzhang. He freed slaves, streamlined the military and bureaucracy, and reduced taxes — the 'Guangwu Restoration' is exemplary among dynastic foundings.",
  ["han-guangwudi"], "洛阳", "Luoyang", {"lat": 34.6, "lng": 112.4},
  ["src-hanshu"], "", 0.9)

e("evt-guandu", "官渡之战", "Battle of Guandu", 200, 200, "china",
  ["战争", "军事", "三国"], ["War", "Military", "Three Kingdoms"],
  5,
  "曹操以少胜多大破袁绍——中国战争史上最经典的以弱胜强战例之一，奠定了曹操统一北方的基础。",
  "Cao Cao's decisive victory over Yuan Shao's numerically superior army — one of history's classic underdog triumphs, cementing Cao Cao's control of North China.",
  "200年袁绍率精兵十万南下进攻曹操——曹操仅有约两万人。曹操先以声东击西斩颜良解白马之围，又在延津以辎重诱敌阵斩文丑——袁绍两员大将被杀严重打击了士气。双方在官渡对峙——袁绍筑土山射箭入曹营使曹军「皆蒙楯而行」——曹操以抛石车（霹雳车）破解。最关键的时刻到来了——袁绍谋士许攸因家属在后方犯法被审配收押而投奔曹操，告诉了袁绍粮草屯于乌巢的秘密。曹操亲率精兵五千夜袭乌巢尽烧粮草——袁军顷刻崩溃，袁绍仅带八百骑逃回河北。此战之后曹操再无北方之敌。",
  "In 200 CE, Yuan Shao marched south with 100,000 elite troops against Cao Cao's roughly 20,000. Cao Cao first used a diversion to behead Yan Liang and lift the siege of Baima, then lured and killed Wen Chou at Yanjin with a supply-train trap — losing two top generals devastated Yuan Shao's morale. The armies stalemated at Guandu — Yuan Shao built earthen ramparts to rain arrows into Cao's camp, forcing soldiers to 'walk with shields overhead' — Cao Cao countered with trebuchets. The decisive moment came when Yuan Shao's advisor Xu You, whose family had been persecuted by Shen Pei back home, defected to Cao Cao and revealed that Yuan Shao's grain was stored at Wuchao. Cao Cao personally led 5,000 picked troops in a night raid, burning the entire supply depot. Yuan Shao's army collapsed instantly; he fled back to Hebei with only 800 cavalry. After Guandu, Cao Cao had no serious rival in North China.",
  [], "官渡（今河南中牟）", "Guandu (modern Zhongmu, Henan)", {"lat": 34.7, "lng": 114.0},
  ["src-sanguozhi"], "", 0.9)

e("evt-eight-princes", "八王之乱", "War of the Eight Princes", 291, 306, "china",
  ["政治", "内乱", "西晋"], ["Politics", "Civil War", "Western Jin"],
  4,
  "西晋宗室诸王为争夺中央权力进行的持续十六年的大混战，直接导致了西晋的灭亡和五胡乱华。",
  "A sixteen-year internecine struggle among Western Jin imperial princes for central power, directly causing the dynasty's collapse and the Wu Hu invasion.",
  "西晋统一仅十一年后宗室内战便爆发了——根源在于司马炎的分封政策和将皇位传给智力有缺陷的司马衷。这场战乱始于291年贾皇后联合楚王司马玮杀辅政大臣杨骏、随后翻脸杀司马玮——此后赵王司马伦、齐王司马冏、长沙王司马乂、成都王司马颖、河间王司马颙、东海王司马越等相继卷入——结盟、背叛、谋杀不断循环。洛阳城被反复焚烧、中原大地赤地千里。到306年动乱基本结束时西晋的精锐部队已在内耗中消耗殆尽——十年后匈奴人刘渊建立的汉赵政权攻破洛阳俘虏晋怀帝（永嘉之乱）——中国进入了长达近三百年的分裂动荡时期。",
  "Just eleven years after unification, Western Jin's civil war erupted — rooted in Sima Yan's enfeoffment policy and his decision to pass the throne to his mentally disabled son Sima Zhong. The conflict began in 291 when Empress Jia allied with Prince Wei (Sima Wei) to kill the regent Yang Jun, then turned on and killed Sima Wei. Thereafter Prince Zhao (Sima Lun), Prince Qi (Sima Jiong), Prince Changsha (Sima Yi), Prince Chengdu (Sima Ying), Prince Hejian (Sima Yong), Prince Donghai (Sima Yue), and others plunged in — an endless cycle of alliance, betrayal, and murder. Luoyang was repeatedly burned; the Central Plains bled dry. By 306 when the chaos subsided, Western Jin's elite forces had been consumed by infighting — a decade later, the Xiongnu leader Liu Yuan's Han-Zhao regime sacked Luoyang and captured Emperor Huai (the Disaster of Yongjia) — China entered nearly three centuries of division and turmoil.",
  ["sima-yan"], "洛阳及中原地区", "Luoyang and Central Plains", {"lat": 34.6, "lng": 112.4},
  ["src-sanguozhi"], "", 0.85)

e("evt-feishui", "淝水之战", "Battle of Fei River", 383, 383, "china",
  ["战争", "军事", "东晋", "南北朝"], ["War", "Military", "Eastern Jin", "Southern Dynasties"],
  5,
  "东晋谢安以八万北府兵大败前秦苻坚八十余万大军——中国战争史上最具戏剧性的以少胜多战例。",
  "Eastern Jin's Xie An with 80,000 Beifu troops routed Former Qin's Fu Jian with over 800,000 — the most dramatic underdog victory in Chinese military history.",
  "苻坚统一北方后志在一举吞并东晋，不顾大多数臣僚反对——「投鞭于江，足断其流」自负溢于言表。东晋由谢安坐镇后方调度——他悠闲地下棋以稳定人心——前线由谢玄、谢石指挥八万北府兵迎战。两军隔淝水对峙——谢玄要求苻坚略退后让晋军渡河决战——苻坚想在晋军半渡时攻击便应允后撤。但撤退命令在庞大而纪律松散的各族联军中引发了恐慌——降将朱序在阵后大喊「秦军败了」——顷刻间八十余万大军兵败如山倒——苻坚中箭负伤，逃回北方时百万大军仅剩十余万。这场战役保全了南方华夏文明的正统——为南北朝对峙格局定下基调。成语「风声鹤唳」「草木皆兵」均出自此战。",
  "After unifying the north, Fu Jian was determined to swallow Eastern Jin in one gulp, overriding near-unanimous opposition — 'throwing our riding crops into the Yangtze would be enough to stop its flow.' Xie An managed the rear, famously playing weiqi with unruffled calm to project confidence, while Xie Xuan and Xie Shi commanded the 80,000 Beifu troops at the front. The armies faced each other across the Fei River. Xie Xuan requested Fu Jian retreat slightly to allow the Jin army to cross for a decisive battle — Fu Jian, planning to attack mid-crossing, agreed. But the retreat order triggered panic in the huge, ethnically diverse, poorly disciplined coalition forces — the turncoat general Zhu Xu shouted from the rear: 'The Qin army is routed!' — and 800,000 men collapsed in an instant. Fu Jian was wounded by an arrow; when he reached the north, his million-man army had shrunk to barely 100,000. This battle preserved the southern Han Chinese cultural sphere and set the north-south division pattern. The idioms 'startled by every sound of wind and crane' and 'seeing soldiers in every bush and tree' both originate here.",
  [], "淝水（今安徽寿县）", "Fei River (modern Shou County, Anhui)", {"lat": 32.5, "lng": 116.7},
  [], "", 0.85)

e("evt-grand-canal", "开凿大运河", "Construction of the Grand Canal", 605, 610, "sui-dynasty",
  ["工程", "交通", "隋朝"], ["Engineering", "Transport", "Sui Dynasty"],
  5,
  "隋炀帝征发数百万民夫开凿连接南北的大运河——世界上最长的古代人工水道，深刻改变了中国的经济地理格局。",
  "Emperor Yang of Sui mobilized millions to dig the Grand Canal connecting north and south — the world's longest ancient artificial waterway, profoundly reshaping China's economic geography.",
  "隋炀帝杨广在位期间完成了中国古代规模最大的基础设施工程——大运河全长约2700公里，连接了海河、黄河、淮河、长江和钱塘江五大水系。工程分三部分：通济渠连接洛阳到淮河、邗沟连接淮河到长江、永济渠连接洛阳到涿郡（今北京）。大运河的修建使用了超过五百万民工——以极其惨重的人力代价完成——但它的历史价值超越了修建时的暴虐：运河使南方的粮食和物资可以大规模输送到北方——此后一千年中中国再也没有出现分裂为南北两个政权的情况——大运河是维系中国统一的物质纽带。",
  "Emperor Yang of Sui completed the largest infrastructure project of ancient China — the Grand Canal, spanning roughly 2,700 kilometers and linking five major river systems: the Hai, Yellow, Huai, Yangtze, and Qiantang. The project came in three sections: the Tongji Canal linking Luoyang to the Huai, the Hangou Canal linking the Huai to the Yangtze, and the Yongji Canal linking Luoyang to Zhuo Commandery (modern Beijing). Over five million laborers were conscripted for its construction — completed at staggering human cost. Yet its historical value transcends the brutality of its making: the canal allowed southern grain and goods to flow northward at scale — for the next millennium, China would never again split into separate northern and southern regimes — the Grand Canal was the physical bond holding China together.",
  ["sui-yangdi"], "以洛阳为中心连接南北", "Central axis from Luoyang connecting north and south", {"lat": 34.6, "lng": 112.4},
  ["src-suisheshu"], "", 0.9)

e("evt-zhenguan", "贞观之治", "Reign of Zhenguan", 627, 649, "tang-dynasty",
  ["政治", "唐朝", "盛世"], ["Politics", "Tang Dynasty", "Golden Age"],
  5,
  "唐太宗李世民统治的贞观年间，政治清明、社会安定、边疆稳固——被后世视为中国古代治理的黄金标准。",
  "The Zhenguan reign of Emperor Taizong of Tang — an era of clean governance, social stability, and secure frontiers, regarded as the gold standard of ancient Chinese statecraft.",
  "贞观之治的核心是唐太宗的人格和治国理念。他以「水能载舟亦能覆舟」自警——将人民视为政权合法性的最终来源。他重用魏征——一个曾经效力于他政敌李建成的谋士——并容忍魏征当众的面折廷争。他完善了三省六部制和科举制度、轻徭薄赋、精简中央机构（贞观初年中央官员仅643人）。他击败了东突厥被各部尊为「天可汗」——实现了前所未有的多民族共主。他对外来文化持开放态度——长安城中居住着波斯、阿拉伯、印度、日本等各国商人、僧侣和留学生。贞观之治的理想在后世不断被追忆——成为中国政治文化中「好政府」的永恒范本。",
  "The essence of the Zhenguan era was Tang Taizong's personality and governing philosophy. He warned himself that 'water can both bear the boat and overturn it' — viewing the people as the ultimate source of political legitimacy. He promoted Wei Zheng — a strategist who had once served his archrival Li Jiancheng — and tolerated Wei Zheng's public confrontations at court. He perfected the three-department system and imperial examinations, reduced taxes, and streamlined the central bureaucracy (only 643 officials at court in early Zhenguan). He defeated the Eastern Turks and was acclaimed 'Heavenly Khan' by the steppe tribes — achieving unprecedented multi-ethnic co-sovereignty. He was open to foreign cultures — Chang'an teemed with Persian, Arab, Indian, and Japanese merchants, monks, and students. The Zhenguan ideal was endlessly recalled by later generations — becoming the eternal template of 'good government' in Chinese political culture.",
  [], "长安", "Chang'an", {"lat": 34.3, "lng": 108.9},
  ["src-jiutangshu"], "", 0.9)

e("evt-chenqiao", "陈桥兵变", "Chen Bridge Mutiny", 960, 960, "china",
  ["政治", "军事", "宋朝"], ["Politics", "Military", "Song Dynasty"],
  5,
  "赵匡胤在陈桥驿被部下黄袍加身拥立为帝——几乎不流血的政变开启了三百年赵宋王朝。",
  "Zhao Kuangyin was draped in the imperial yellow robe by his troops at Chen Bridge and proclaimed emperor — a nearly bloodless coup that inaugurated three centuries of Song rule.",
  "960年正月初一——后周朝廷收到辽国和北汉联合入侵的紧急军报——七岁的恭帝和符太后急派殿前都点检赵匡胤率军北上御敌。但这份军报很可能是赵匡胤集团伪造的。军队行至开封城北二十里的陈桥驿时驻扎——次日凌晨赵匡胤的弟弟赵光义和幕僚赵普煽动士兵将预先准备好的黄袍披在刚刚酒醒的赵匡胤身上——全军山呼万岁。赵匡胤率军返京时唯一抵抗的侍卫亲军副都指挥使韩通被军校王彦升杀死——年仅七岁的周恭帝被迫禅让。赵匡胤建立宋朝后以杯酒释兵权的方式解除了将领的威胁——开启了北宋167年的统治。",
  "On the first day of 960, the Later Zhou court received an urgent military report: the Liao and Northern Han were jointly invading. The seven-year-old Emperor Gong and Empress Dowager Fu dispatched Commander-in-Chief Zhao Kuangyin northward to meet the threat. But the report was almost certainly fabricated by Zhao's faction. The army camped at Chen Bridge, twenty li north of Kaifeng. At dawn the next day, Zhao's younger brother Zhao Guangyi and strategist Zhao Pu incited the troops to drape a pre-prepared yellow imperial robe over the just-awakened Zhao Kuangyin — the entire army roared 'Long Live the Emperor!' When Zhao marched back to the capital, the only resistance came from Han Tong, vice-commander of the Palace Guard, who was killed by officer Wang Yansheng. The seven-year-old Emperor Gong was forced to abdicate. After founding Song, Zhao Kuangyin famously 'relieved his generals of command over a cup of wine' — peacefully retiring his military leaders — and inaugurated 167 years of Northern Song rule.",
  ["song-taizu"], "陈桥驿（今河南开封北）", "Chen Bridge (north of modern Kaifeng)", {"lat": 34.8, "lng": 114.3},
  ["src-ss"], "", 0.9)

e("evt-chanyuan", "澶渊之盟", "Treaty of Chanyuan", 1004, 1004, "song-dynasty",
  ["政治", "外交", "宋朝"], ["Politics", "Diplomacy", "Song Dynasty"],
  4,
  "北宋与辽国签订的和平条约——以岁币换取了宋辽百余年的和平，开启了一个经济文化高度繁荣的时代。",
  "Peace treaty between Northern Song and Liao that purchased over a century of peace with annual payments, ushering in an era of extraordinary economic and cultural prosperity.",
  "1004年辽国萧太后和辽圣宗率大军南下——兵临黄河北岸的重镇澶州。宋朝朝廷一片恐慌——多数大臣主张迁都南逃。宰相寇准力排众议坚持宋真宗御驾亲征——当真宗出现在澶州城头时宋军士气大振。辽军主将萧挞凛在视察地形时被宋军弩箭射杀——辽军失去了最强的统帅。双方都有意愿议和：宋朝以每年输送绢二十万匹、银十万两的代价换取了和平。这笔钱不到宋朝财政收入的百分之一——而维持边境军队的费用是岁币的数十倍。澶渊之盟后宋辽维持了约120年的和平——在此期间北宋的经济文化达到了中国历史上前所未有的高度。",
  "In 1004, Empress Dowager Xiao and Emperor Shengzong of Liao led a massive invasion south, reaching Chanyuan on the Yellow River's north bank. The Song court panicked — most officials urged abandoning the capital. Chancellor Kou Zhun overrode them all, insisting Emperor Zhenzong personally lead the defense — when the emperor appeared on Chanyuan's walls, Song troop morale soared. The Liao commander Xiao Talin was killed by a Song crossbow bolt while reconnoitering — the Liao lost their best general. Both sides wanted peace: Song agreed to pay 200,000 bolts of silk and 100,000 taels of silver annually. This sum was less than one percent of Song's fiscal revenue — while maintaining border armies cost dozens of times more. After Chanyuan, Song and Liao maintained roughly 120 years of peace — during which Northern Song's economy and culture reached unprecedented heights.",
  ["kou-zhun"], "澶州（今河南濮阳）", "Chanyuan (modern Puyang, Henan)", {"lat": 35.7, "lng": 115.0},
  ["src-ss"], "", 0.9)

e("evt-jingkang", "靖康之耻", "Jingkang Incident", 1127, 1127, "song-dynasty",
  ["战争", "宋朝", "金朝"], ["War", "Song Dynasty", "Jin Dynasty"],
  5,
  "金兵攻破开封俘虏徽钦二帝和后妃宗室三千余人北去——北宋灭亡，是宋人心中永远的国耻。",
  "Jin troops sacked Kaifeng and marched the two emperors Huizong and Qinzong plus 3,000 imperial captives northward — the fall of Northern Song and the eternal national shame of the Song people.",
  "1126年金兵第一次围攻开封时宋朝以割地和巨额赔款换取了退兵——但金兵撤退后宋朝却联络契丹余部企图夹击金国——这给了金朝口实。1127年初金兵再次南下包围开封。此时开封城中守军虽人数尚可但已军心涣散——迷信的钦宗竟相信一个自称能召唤天兵天将的骗子郭京——打开城门让郭京的「神兵」出击——结果金兵趁势涌入城中。开封城破后金兵大肆劫掠——徽宗、钦宗二帝和后妃、皇子、公主、宗室、朝臣、工匠、乐师等三千余人被押解北上——「二圣」在五国城受尽屈辱。侥幸逃脱的徽宗第九子赵构在南方即位延续宋朝——史称南宋。岳飞在《满江红》中「靖康耻，犹未雪，臣子恨，何时灭」的呐喊至今令人震撼。",
  "In 1126, Jin's first siege of Kaifeng was lifted after Song agreed to territorial cession and massive indemnities — but after Jin withdrew, Song secretly contacted Khitan remnants to attack Jin, giving Jin a casus belli. In early 1127, Jin besieged Kaifeng again. Though Kaifeng had defenders, morale had collapsed — the superstitious Emperor Qinzong believed a fraud named Guo Jing who claimed he could summon celestial soldiers — the city gates were opened for Guo Jing's 'divine troops' — and Jin forces poured in. After the sack, Jin troops marched north with over 3,000 captives: the two emperors Huizong and Qinzong, empresses, princes, princesses, imperial clansmen, ministers, artisans, and musicians — the 'Two Sovereigns' suffered untold humiliation in the far north. The ninth son of Huizong, Zhao Gou, escaped and established the Southern Song. Yue Fei's cry in 'River All Red' — 'The Jingkang shame remains unavenged; when will a subject's hatred end?' — still shakes the reader today.",
  ["song-huizong", "song-gaozong"], "开封（今河南开封）", "Kaifeng (modern Kaifeng, Henan)", {"lat": 34.8, "lng": 114.3},
  ["src-ss"], "", 0.9)

e("evt-yuefei", "岳飞北伐与风波亭", "Yue Fei's Northern Campaigns and Execution", 1134, 1142, "song-dynasty",
  ["战争", "南宋", "民族英雄"], ["War", "Southern Song", "National Hero"],
  5,
  "岳飞率岳家军北伐连战连捷直抵朱仙镇——却被宋高宗以十二道金牌召回以莫须有罪名处死，成为中国历史上最令人扼腕的忠臣悲剧。",
  "Yue Fei's Yue Army swept north in a string of victories reaching Zhuxian Town — only for Emperor Gaozong to recall him with twelve gold medallions and execute him on fabricated charges — Chinese history's most heartbreaking loyalist tragedy.",
  "岳飞从一名普通士兵成长为南宋最杰出的统帅。他的岳家军军纪严明——「冻死不拆屋，饿死不掳掠」——赢得了北方沦陷区百姓的广泛支持。1140年他率军北进，在郾城大破金军主力拐子马、在颍昌再获大捷、前锋直达距离开封仅四十五里的朱仙镇。但宋高宗和秦桧力主和议——在一天之内连下十二道金牌强令他班师。岳飞仰天长叹：「十年之功，废于一旦！」回朝后他被以「莫须有」罪名陷害——1142年除夕夜被赐死于大理寺风波亭——年仅39岁。他的《满江红》「三十功名尘与土，八千里路云和月」成为此后近千年中国人面对外侮时的精神力量源泉。",
  "Yue Fei rose from a common soldier to Southern Song's greatest commander. His Yue Army, with iron discipline — 'would rather freeze than break into a house, rather starve than loot' — won widespread support among the northern population under Jin occupation. In 1140, he marched north, shattering the Jin main force at Yancheng, winning again at Yingchang, and reaching Zhuxian Town, just 45 li from Kaifeng. But Emperor Gaozong and Qin Hui were determined to sue for peace — twelve gold medallions arrived in a single day ordering his immediate withdrawal. Yue Fei looked skyward and sighed: 'Ten years of effort wasted in a single day!' Returning to court, he was framed on the 'dubious' charge — and on New Year's Eve of 1142, executed at Fengbo Pavilion, age 39. His 'River All Red' — 'Thirty years of fame, dust and dirt; eight thousand li of road, clouds and moon' — became the spiritual wellspring for Chinese facing foreign aggression for nearly a millennium.",
  [], "朱仙镇 — 临安（杭州）", "Zhuxian Town to Lin'an (Hangzhou)", {"lat": 34.7, "lng": 114.2},
  ["src-ss"], "", 0.9)

e("evt-hongjin", "红巾军起义", "Red Turban Rebellion", 1351, 1368, "yuan-dynasty",
  ["起义", "元朝", "明朝"], ["Rebellion", "Yuan Dynasty", "Ming Dynasty"],
  5,
  "元末以红巾为标志的全国性农民大起义，朱元璋即由此起家，最终推翻了元朝统治。",
  "A nationwide peasant uprising marked by red turbans from which Zhu Yuanzhang rose to overthrow the Mongol Yuan dynasty.",
  "红巾军起义的直接导火索是元朝政府强征十七万民夫修黄河——白莲教首领韩山童和刘福通趁机在黄河工地上埋下一个独眼石人——上面刻着「莫道石人一只眼，挑动黄河天下反」——以此号召起义。起义军头裹红巾为号，迅速发展为燎原之势——刘福通在北方拥立韩林儿为「小明王」建立了大宋政权。南方的徐寿辉、陈友谅、张士诚、方国珍等也纷纷响应。朱元璋最初在郭子兴部下——郭死后他独立发展，采纳朱升「高筑墙广积粮缓称王」的策略。他先后消灭陈友谅（鄱阳湖大战）和张士诚，于1368年在应天府（南京）称帝建立明朝——随后派徐达北伐攻克大都（北京），元朝在中原的统治终结。",
  "The Red Turban Rebellion's immediate spark was the Yuan government's conscription of 170,000 laborers to repair the Yellow River. White Lotus leaders Han Shantong and Liu Futong buried a one-eyed stone figure at the worksite engraved with: 'Mock not the stone man's single eye — stirring the Yellow River, the realm shall defy.' The rebels tied red turbans around their heads and spread like wildfire — Liu Futong in the north enthroned Han Lin'er as the 'Lesser Ming King.' In the south, Xu Shouhui, Chen Youliang, Zhang Shicheng, and Fang Guozhen all rose in response. Zhu Yuanzhang began under Guo Zixing; after Guo's death, he developed independently, adopting Zhu Sheng's strategy: 'Build high walls, stockpile grain, delay claiming the throne.' He eliminated Chen Youliang (at the epic Lake Poyang battle) and Zhang Shicheng in turn, proclaimed the Ming dynasty at Yingtian (Nanjing) in 1368, then dispatched Xu Da north to capture Dadu (Beijing) — ending Mongol rule over China.",
  [], "黄河流域至长江流域", "Yellow River to Yangtze basin", {"lat": 34.0, "lng": 116.0},
  ["src-yuanshi", "src-mingshi"], "", 0.9)

e("evt-tumu", "土木堡之变", "Tumu Crisis", 1449, 1449, "ming-dynasty",
  ["战争", "明朝"], ["War", "Ming Dynasty"],
  5,
  "明英宗在太监王振怂恿下御驾亲征瓦剌遭全军覆没本人被俘——于谦领导的北京保卫战挽救了明朝免于重蹈北宋覆辙。",
  "Emperor Yingzong, egged on by eunuch Wang Zhen, led a personal campaign against the Oirats and was utterly crushed and captured at Tumu — only Yu Qian's defense of Beijing saved Ming from Northern Song's fate.",
  "1449年瓦剌首领也先率军南下。太监王振怂恿23岁的明英宗御驾亲征——二十余万明军仓促出征，指挥混乱粮草不继。行至土木堡时全军已被也先包围水源断绝——明军大溃英宗被俘、王振被愤怒的将领锤杀——随行文武百官大多战死。消息传到北京朝廷一片恐慌——有人主张迁都南京。于谦厉声道：「言南迁者可斩也！」他拥立英宗之弟为景泰帝、调集京畿军队、加固城防——当也先大军兵临城下时被猛烈炮火击退。也先围攻数日无法破城只得撤退——一年后因留着一个无用的俘虏释放了英宗。七年后英宗通过夺门之变复辟——第一件事就是杀了于谦。",
  "In 1449, the Oirat leader Esen marched south. The eunuch Wang Zhen goaded the 23-year-old Emperor Yingzong into leading a personal campaign — over 200,000 Ming troops hastily mobilized in chaos with collapsing supply lines. Reaching Tumu Fort, the entire army found itself surrounded by Esen's forces with no water source — the Ming army disintegrated, Yingzong was captured, and the enraged generals bludgeoned Wang Zhen to death — most accompanying civil and military officials perished. News reached Beijing and the court panicked — some urged abandoning the north for Nanjing. Yu Qian thundered: 'Those who speak of retreating south should be beheaded!' He enthroned Yingzong's younger brother as the Jingtai Emperor, mustered capital forces, and strengthened fortifications — when Esen's army reached Beijing's walls, fierce cannon fire drove them back. After days of futile siege, Esen withdrew — a year later, finding his hostage useless, he released Yingzong. Seven years later, Yingzong reclaimed the throne through the 'Wresting the Gate' coup — and his first act was executing Yu Qian.",
  ["yu-qian"], "土木堡（今河北怀来）", "Tumu Fort (modern Huailai, Hebei)", {"lat": 40.4, "lng": 115.5},
  ["src-mingshi"], "", 0.9)

e("evt-kangqian", "康乾盛世", "High Qing Era", 1661, 1796, "qing-dynasty",
  ["政治", "经济", "清朝", "盛世"], ["Politics", "Economy", "Qing Dynasty", "Golden Age"],
  4,
  "康熙、雍正、乾隆三朝持续一百三十余年的繁荣稳定——中国最后一个封建盛世，疆域、人口和经济总量达到传统社会的巅峰。",
  "Over 130 years of prosperity and stability under the Kangxi, Yongzheng, and Qianlong emperors — China's last feudal golden age, with territory, population, and economy at traditional society's peak.",
  "康乾盛世从1661年康熙亲政到1796年乾隆退位——是清朝乃至整个中国帝制时代最长久的一段繁荣期。康熙平三藩、收台湾、签订《尼布楚条约》稳固东北边疆；雍正改革财政整顿吏治——摊丁入亩和耗羡归公大大增加了中央财政收入；乾隆的十大武功将疆域扩展至空前——总面积超过1300万平方公里。人口从清初约7000万增长到18世纪末的3亿——占当时世界总人口的三分之一。但盛世的阴影同样深重：文字狱愈演愈烈、闭关锁国政策保守僵化、八旗制度腐败——1796年白莲教起义标志着盛世的终结。",
  "The High Qing Era stretched from Kangxi's personal rule in 1661 to Qianlong's abdication in 1796 — the longest period of prosperity in Qing and arguably all of late imperial Chinese history. Kangxi suppressed the Three Feudatories, recovered Taiwan, and signed the Treaty of Nerchinsk securing the northeastern frontier; Yongzheng reformed state finances and disciplined the bureaucracy — the merger of head tax into land tax and return of surcharges to the treasury massively increased central revenue; Qianlong's 'Ten Great Campaigns' expanded the realm to its greatest extent — over 13 million square kilometers. The population grew from roughly 70 million in the early Qing to 300 million by the late 18th century — one-third of the world's population. Yet the era's shadows were equally deep: literary inquisitions intensified, seclusion policies ossified, and the Banner system rotted — the White Lotus Rebellion of 1796 marked the era's end.",
  [], "全国", "Empire-wide", {"lat": 39.9, "lng": 116.4},
  ["src-qingshigao"], "", 0.9)

e("evt-humen", "虎门销烟", "Destruction of Opium at Humen", 1839, 1839, "qing-dynasty",
  ["政治", "清朝", "禁烟"], ["Politics", "Qing Dynasty", "Anti-Opium"],
  5,
  "林则徐在虎门海滩当众销毁收缴的英国鸦片两万余箱——中国近代史上最壮烈的抵抗外来侵略的象征性事件。",
  "Lin Zexu publicly destroyed over 20,000 chests of confiscated British opium on Humen Beach — modern China's most heroic symbol of resistance to foreign aggression.",
  "1839年林则徐被道光皇帝任命为钦差大臣前往广州禁烟。他雷厉风行——限令外国商人三日内交出所有鸦片并具结永不再贩。经过艰苦交涉英国驻华商务监督义律被迫交出鸦片两万零二百八十三箱。1839年6月3日至25日林则徐在虎门海滩上挖了两个大池引入海水和石灰——将鸦片投入池中搅拌销毁——最后打开闸门将残渣冲入大海。整个过程公开进行——邀请外国商人、记者和当地民众观看。销烟的壮举使林则徐成为民族英雄——但也成为英国发动第一次鸦片战争的借口。",
  "In 1839, Lin Zexu was appointed Imperial Commissioner and dispatched to Guangzhou to suppress the opium trade. He moved with lightning speed — ordering foreign merchants to surrender all opium within three days and sign bonds pledging never to trade it again. After bitter negotiations, British Superintendent of Trade Charles Elliot was forced to hand over 20,283 chests of opium. From June 3 to 25, 1839, Lin had two enormous pits dug on Humen Beach, filled with seawater and lime, into which the opium was dumped, stirred, and chemically destroyed — then the sluice gates were opened to flush the residue into the sea. The entire process was conducted publicly, with foreign merchants, journalists, and local residents invited to witness. The destruction made Lin Zexu a national hero — and gave Britain its casus belli for the First Opium War.",
  ["lin-zexu"], "虎门（今广东东莞）", "Humen (modern Dongguan, Guangdong)", {"lat": 22.8, "lng": 113.6},
  ["src-qingshigao"], "", 0.9)

e("evt-wuxu", "戊戌变法", "Hundred Days' Reform", 1898, 1898, "qing-dynasty",
  ["政治", "改革", "清朝"], ["Politics", "Reform", "Qing Dynasty"],
  5,
  "光绪帝和康有为梁启超推动的103天改革——企图将中国从君主专制转向君主立宪——被慈禧太后政变镇压，六君子血洒菜市口。",
  "The 103-day reform movement led by Emperor Guangxu with Kang Youwei and Liang Qichao attempting to transition China from autocracy to constitutional monarchy — crushed by Empress Dowager Cixi's coup, with the Six Gentlemen executed.",
  "1898年光绪帝目睹甲午战败后痛下变法决心。从6月11日到9月21日他发布了上百道改革诏令——废除八股文、创办京师大学堂（北京大学前身）、建立新式军队、精简官僚机构、鼓励实业和报业。但改革速度过快触动了太多既得利益——9月21日慈禧发动政变将光绪软禁于瀛台、重新垂帘听政。康梁逃亡海外——谭嗣同本可逃走却留下赴死：「各国变法无不从流血而成，今中国未闻有因变法而流血者——此国之所以不昌也。有之，请自嗣同始！」9月28日谭嗣同、林旭、杨锐、刘光第、杨深秀、康广仁六人在菜市口被斩首——史称「戊戌六君子」。",
  "In 1898, Emperor Guangxu, humiliated by China's defeat by Japan, resolved on sweeping reform. From June 11 to September 21, he issued over a hundred reform edicts — abolishing the eight-legged essay, founding the Imperial University of Peking (precursor to Peking University), creating a modern army, streamlining the bureaucracy, and encouraging industry and journalism. But the pace was too rapid, threatening too many entrenched interests — on September 21, Cixi launched her coup, confining Guangxu to Yingtai Pavilion and resuming her rule behind the curtain. Kang and Liang fled abroad — Tan Sitong could have escaped but stayed to die: 'All nations achieve reform through bloodshed; China has never had reformers who bled — that is why the nation does not prosper. Let it begin with Sitong!' On September 28, Tan Sitong, Lin Xu, Yang Rui, Liu Guangdi, Yang Shenxiu, and Kang Guangren — the 'Six Gentlemen of 1898' — were beheaded at the execution ground.",
  ["qing-guangxu", "liang-qichao"], "北京", "Beijing", {"lat": 39.9, "lng": 116.4},
  ["src-qingshigao"], "", 0.9)

# ===== OUTPUT =====
for evt in events:
    eid = evt["id"]
    title = evt["title"]
    titleEn = evt.get("titleEn", "")
    startY = evt.get("startYear", "undefined") if evt.get("startYear") is not None else "undefined"
    endY = evt.get("endYear", "undefined") if evt.get("endYear") is not None else "undefined"
    region = evt.get("regionId", "")
    tags = ", ".join(f"'{t}'" for t in evt["tags"])
    tagsEn = ", ".join(f"'{t}'" for t in evt.get("tagsEn", []))
    imp = evt.get("importance", 3)
    summary = evt.get("summary", "")
    summaryEn = evt.get("summaryEn", "")
    desc = evt.get("description", "")
    descEn = evt.get("descriptionEn", "")
    persons = ", ".join(f"'{p}'" for p in evt.get("personIds", []))
    place = evt.get("placeName", "undefined")
    placeEn = evt.get("placeNameEn", "undefined")
    coords = evt.get("coordinates")
    coord_str = "undefined"
    if coords:
        coord_str = f"{{ lat: {coords['lat']}, lng: {coords['lng']} }}"
    srcs = ", ".join(f"'{s}'" for s in evt.get("sourceIds", []))
    wiki = evt.get("wikidataQid", "")
    conf = evt.get("confidenceScore", 0.85)
    dp = evt.get("datePrecision", "year")
    approx = "true" if evt.get("isApproximate", False) else "false"

    print(f"""  {{
    id: '{eid}',
    title: '{esc(title)}',
    titleEn: '{esc(titleEn)}',
    startYear: {startY},
    endYear: {endY},
    datePrecision: '{dp}',
    isApproximate: {approx},
    regionId: '{region}',
    placeName: '{esc(place)}',
    placeNameEn: '{esc(placeEn)}',
    coordinates: {coord_str},
    personIds: [{persons}],
    tags: [{tags}],
    tagsEn: [{tagsEn}],
    importance: {imp},
    summary: '{esc(summary)}',
    summaryEn: '{esc(summaryEn)}',
    description: '{esc(desc)}',
    descriptionEn: '{esc(descEn)}',
    sourceIds: [{srcs}],
    relatedEventIds: [],
    wikidataQid: '{wiki}',
    dataStatus: 'published',
    confidenceScore: {conf},
    externalReferences: [],
  }},""")
print(f"\n// Total: {len(events)} Chinese historical events")
