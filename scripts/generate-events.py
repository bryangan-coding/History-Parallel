#!/usr/bin/env python3
"""Generate TypeScript event entries for mockData.ts"""
import json

# Escape single quotes for TypeScript strings
def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'")

events = []

def evt(id, title, titleEn, startYear, endYear, regionId, placeName, placeNameEn, lat, lng,
        personIds, tags, tagsEn, importance, summary, summaryEn, description, descriptionEn,
        sourceIds, relatedEventIds, confidenceScore=0.85, datePrecision="year", isApproximate=False,
        externalRefs=None, endYearApprox=False):
    """Generate a single event entry"""
    e = {
        "id": id,
        "title": title,
        "titleEn": titleEn,
        "startYear": startYear,
        "endYear": endYear,
        "regionId": regionId,
        "placeName": placeName,
        "placeNameEn": placeNameEn,
        "lat": lat,
        "lng": lng,
        "personIds": personIds,
        "tags": tags,
        "tagsEn": tagsEn,
        "importance": importance,
        "summary": summary,
        "summaryEn": summaryEn,
        "description": description,
        "descriptionEn": descriptionEn,
        "sourceIds": sourceIds,
        "relatedEventIds": relatedEventIds,
        "confidenceScore": confidenceScore,
        "datePrecision": datePrecision,
        "isApproximate": isApproximate,
        "externalRefs": externalRefs or []
    }
    events.append(e)

# ==================== ANCIENT BCE EVENTS ====================

# Qin unification
evt(
    "evt-qin-unification",
    "秦统一六国",
    "Qin Unification of China",
    -221, -221,
    "china", "咸阳", "Xianyang",
    34.3, 108.9,
    ["qin-shi-huang"],
    ["政治", "战争", "统一", "秦朝"],
    ["Politics", "War", "Unification", "Qin Dynasty"],
    5,
    "秦王嬴政灭六国，建立中国历史上第一个大一统中央集权帝国，自称始皇帝。",
    "King Zheng of Qin conquered the six rival states, establishing China's first unified centralized empire, proclaiming himself the First Emperor.",
    "公元前221年，秦王嬴政先后灭韩、赵、魏、楚、燕、齐六国，结束了春秋战国五百余年的分裂局面。他废除分封制，推行郡县制，统一文字（小篆）、度量衡和车轨，建立了中国历史上第一个大一统王朝——秦朝。",
    "In 221 BCE, King Zheng of Qin conquered the six rival states of Han, Zhao, Wei, Chu, Yan, and Qi, ending over 500 years of division since the Spring and Autumn period. He abolished the feudal system, implemented the commandery-county system, and standardized writing, weights, measures, and axle widths.",
    ["src-shiji"], [],
    datePrecision="year", confidenceScore=0.9
)

# Great Wall construction
evt(
    "evt-great-wall",
    "修筑万里长城",
    "Construction of the Great Wall Begins",
    -221, -206,
    "china", "北方边境", "Northern Frontier",
    40.0, 116.0,
    ["qin-shi-huang"],
    ["建筑", "军事", "秦朝"],
    ["Architecture", "Military", "Qin Dynasty"],
    4,
    "秦始皇下令连接和扩建北方战国旧长城，形成绵延万里的防御工事。",
    "Qin Shi Huang ordered the connection and expansion of the northern warring states' walls, creating a continuous defensive fortification spanning thousands of miles.",
    "为防御北方匈奴，秦始皇命蒙恬率三十万大军北逐匈奴，并征发数十万民工将原先秦、赵、燕三国的北边长城连接起来，西起临洮，东至辽东，形成最早的万里长城。",
    "To defend against the northern Xiongnu, Qin Shi Huang dispatched General Meng Tian with 300,000 troops to repel them, and conscripted hundreds of thousands of laborers to connect the existing walls of Qin, Zhao, and Yan, stretching from Lintao in the west to Liaodong in the east.",
    ["src-shiji"], [],
    datePrecision="range", confidenceScore=0.8
)

# Burning of books
evt(
    "evt-burning-books",
    "焚书坑儒",
    "Burning of Books and Burying of Scholars",
    -213, -212,
    "china", "咸阳", "Xianyang",
    34.3, 108.9,
    ["qin-shi-huang", "li-si"],
    ["政治", "文化", "秦朝", "思想控制"],
    ["Politics", "Culture", "Qin Dynasty", "Thought Control"],
    4,
    "秦始皇采纳李斯建议，焚烧除秦记、医药、卜筮、农书之外的所有书籍，并坑杀四百六十余名儒生。",
    "Following Li Si's advice, Qin Shi Huang ordered the burning of all books except those on Qin history, medicine, divination, and agriculture, and the execution of over 460 scholars.",
    "公元前213年，博士淳于越反对郡县制，主张恢复分封。丞相李斯驳斥其说，建议焚毁民间所藏《诗》、《书》、百家语等，以统一思想。次年，秦始皇以'为妖言以乱黔首'的罪名，坑杀方士和儒生四百六十余人。",
    "In 213 BCE, scholar Chunyu Yue opposed the commandery system, advocating for feudalism. Chancellor Li Si refuted him and proposed burning privately held copies of the Book of Songs, Book of Documents, and works of the Hundred Schools. The following year, Qin Shi Huang buried alive over 460 scholars and alchemists accused of 'spreading seditious talk.'",
    ["src-shiji"], [],
    datePrecision="range", confidenceScore=0.85
)

# Han Dynasty founding
evt(
    "evt-han-founding",
    "汉朝建立",
    "Founding of the Han Dynasty",
    -206, -202,
    "china", "长安", "Chang'an",
    34.3, 108.9,
    ["liu-bang"],
    ["政治", "朝代更替", "汉朝"],
    ["Politics", "Dynastic Change", "Han Dynasty"],
    5,
    "刘邦击败项羽，建立汉朝，定都长安，开启了中国历史上最辉煌的王朝之一。",
    "Liu Bang defeated Xiang Yu, founded the Han Dynasty with its capital at Chang'an, inaugurating one of the most glorious dynasties in Chinese history.",
    "秦末天下大乱，刘邦与项羽并起抗秦。秦亡后，楚汉相争四年。公元前202年，刘邦在垓下之战中击败项羽，统一天下，建立汉朝。汉朝延续四百余年，是中国历史上影响最为深远的王朝之一，'汉族'之名即由此而来。",
    "After the fall of Qin, Liu Bang and Xiang Yu emerged as the two major contenders. Following four years of Chu-Han contention, Liu Bang defeated Xiang Yu at the Battle of Gaixia in 202 BCE and unified the realm. The Han Dynasty endured for over 400 years, becoming one of the most influential dynasties in Chinese history.",
    ["src-shiji"], ["evt-chu-han"],
    datePrecision="range", confidenceScore=0.9
)

# Zhang Qian's mission
evt(
    "evt-zhang-qian",
    "张骞出使西域",
    "Zhang Qian's Mission to the Western Regions",
    -138, -126,
    "china", "西域", "Western Regions (Central Asia)",
    40.0, 80.0,
    ["zhang-qian"],
    ["外交", "探索", "丝绸之路", "汉朝"],
    ["Diplomacy", "Exploration", "Silk Road", "Han Dynasty"],
    5,
    "汉武帝派遣张骞出使西域，开辟丝绸之路，联通中国与中亚、西亚乃至地中海世界。",
    "Emperor Wu of Han sent Zhang Qian as an envoy to the Western Regions, opening the Silk Road that connected China with Central Asia, Western Asia, and the Mediterranean world.",
    "汉武帝为联合大月氏夹击匈奴，派遣张骞率百余人出使西域。张骞途中被匈奴扣留十年，逃脱后继续西行，到达大宛、康居、大月氏等国。虽然未能促成军事联盟，但他的探险带回大量西域地理和物产信息，为丝绸之路的开辟奠定了基础。",
    "Emperor Wu sent Zhang Qian with over 100 men to forge an alliance with the Yuezhi against the Xiongnu. Captured by the Xiongnu for ten years, Zhang Qian escaped and continued westward, reaching Ferghana, Sogdiana, and Bactria. Though no military alliance materialized, his journey brought back invaluable geographical and commercial intelligence that laid the foundation for the Silk Road.",
    ["src-shiji"], [],
    datePrecision="range", confidenceScore=0.85
)

# Julius Caesar assassinated
evt(
    "evt-caesar-assassination",
    "凯撒遇刺",
    "Assassination of Julius Caesar",
    -44, -44,
    "roman-empire", "罗马", "Rome",
    41.9, 12.5,
    ["julius-caesar"],
    ["政治", "刺杀", "罗马"],
    ["Politics", "Assassination", "Rome"],
    5,
    "罗马终身独裁官凯撒在元老院被刺杀，标志着罗马共和国向帝国过渡的关键转折点。",
    "Julius Caesar, dictator perpetuo of Rome, was assassinated in the Senate, marking a pivotal turning point in the transition from Republic to Empire.",
    "公元前44年3月15日（'三月十五日'），六十余名元老院议员以恢复共和为名，在庞培剧院旁的元老院会议厅刺杀了凯撒。凯撒身中二十三刀。刺杀者以为除掉凯撒就能恢复共和，却引发了新的一轮内战，最终凯撒的养子屋大维建立罗马帝国。",
    "On the Ides of March (March 15), 44 BCE, over sixty senators, claiming to restore the Republic, stabbed Caesar 23 times in the Senate chamber adjoining the Theatre of Pompey. The assassins believed that killing Caesar would restore the Republic, but it instead triggered a new civil war that ended with Caesar's adopted son Octavian establishing the Roman Empire.",
    [], [],
    confidenceScore=0.95, datePrecision="year"
)

# Battle of Actium
evt(
    "evt-actium",
    "亚克兴海战",
    "Battle of Actium",
    -31, -31,
    "roman-empire", "亚克兴（希腊西海岸）", "Actium (western coast of Greece)",
    38.9, 20.7,
    ["augustus", "cleopatra"],
    ["战争", "海战", "罗马"],
    ["War", "Naval Battle", "Rome"],
    5,
    "屋大维在亚克兴海战中击败安东尼和克利奥帕特拉联军，终结了罗马内战，开启了罗马帝国时代。",
    "Octavian defeated the combined fleet of Mark Antony and Cleopatra at the Battle of Actium, ending the Roman civil wars and inaugurating the Roman Empire.",
    "公元前31年9月2日，屋大维的舰队在亚克兴海峡与安东尼和埃及女王克利奥帕特拉的联合舰队展开决战。安东尼舰队战败，次年两人在亚历山大自杀身亡。屋大维成为罗马世界唯一的主人，公元前27年被授予'奥古斯都'称号，罗马帝国正式建立。",
    "On September 2, 31 BCE, Octavian's fleet engaged the combined forces of Mark Antony and Cleopatra at the mouth of the Ambracian Gulf. Antony's fleet was decisively defeated; the following year, both Antony and Cleopatra committed suicide in Alexandria. Octavian became the sole master of the Roman world, receiving the title 'Augustus' in 27 BCE, formally establishing the Roman Empire.",
    [], [],
    confidenceScore=0.95, datePrecision="year"
)

# Roman Empire founding
evt(
    "evt-pax-romana",
    "罗马帝国建立（奥古斯都）",
    "Establishment of the Roman Empire (Augustus)",
    -27, -27,
    "roman-empire", "罗马", "Rome",
    41.9, 12.5,
    ["augustus"],
    ["政治", "帝国", "罗马"],
    ["Politics", "Empire", "Rome"],
    5,
    "屋大维被授予'奥古斯都'称号，罗马共和国转变为帝国，开启了长达两个世纪的'罗马和平'。",
    "Octavian received the title 'Augustus,' transforming the Roman Republic into an Empire and inaugurating two centuries of the 'Pax Romana' (Roman Peace).",
    "公元前27年1月16日，屋大维在元老院宣布'恢复共和'，实际上却接受了'奥古斯都'（意为'神圣者'）的称号和一系列终身权力，成为罗马第一位皇帝。他改革行政体系，建立常备军，开创了长达两百余年的'罗马和平'时期，地中海世界进入空前的繁荣与统一。",
    "On January 16, 27 BCE, Octavian declared in the Senate that he was 'restoring the Republic,' while in fact receiving the title 'Augustus' (meaning 'the revered one') and a range of lifelong powers, becoming Rome's first emperor. He reformed the administration, established a standing army, and inaugurated over two centuries of Pax Romana.",
    [], [],
    confidenceScore=0.9, datePrecision="year"
)

# Ashoka's conversion
evt(
    "evt-ashoka-conversion",
    "阿育王皈依佛教",
    "Ashoka's Conversion to Buddhism",
    -261, -261,
    "india", "羯陵伽（今奥里萨邦）", "Kalinga (present-day Odisha)",
    20.9, 85.9,
    ["ashoka"],
    ["宗教", "佛教", "印度"],
    ["Religion", "Buddhism", "India"],
    5,
    "目睹羯陵伽战争的惨状后，孔雀王朝阿育王皈依佛教，推行'以法教化'，将佛教传播到亚洲各地。",
    "After witnessing the carnage of the Kalinga War, Mauryan Emperor Ashoka converted to Buddhism, promoting 'Dhamma' and spreading Buddhism across Asia.",
    "公元前261年，阿育王征服羯陵伽，战争造成十余万人死亡。惨烈的杀戮令阿育王深受震撼，他放弃武力征服的国策，皈依佛教，推行'正法'（Dhamma）统治。他在全国树立石柱和摩崖石刻诏书，派遣传教使团前往斯里兰卡、中亚、希腊化王国等地，使佛教从一个地方宗教发展为世界性宗教。",
    "In 261 BCE, Ashoka's conquest of Kalinga resulted in over 100,000 deaths. Deeply moved by the carnage, he renounced conquest by force, converted to Buddhism, and promoted rule by 'Dhamma' (righteousness). He erected pillars and rock edicts throughout the empire and sent missionary embassies to Sri Lanka, Central Asia, and Hellenistic kingdoms, transforming Buddhism from a local faith into a world religion.",
    [], [],
    confidenceScore=0.85, datePrecision="year"
)

# Silk Road opening
evt(
    "evt-silk-road",
    "丝绸之路开通",
    "The Silk Road Opens",
    -130, -100,
    "china", "河西走廊", "Hexi Corridor (Gansu Corridor)",
    39.0, 100.0,
    ["zhang-qian"],
    ["贸易", "文化", "丝绸之路", "汉朝"],
    ["Trade", "Culture", "Silk Road", "Han Dynasty"],
    5,
    "张骞凿空西域后，丝绸之路正式开通，东西方贸易与文化从此大规模交流。",
    "Following Zhang Qian's pioneering journey to the Western Regions, the Silk Road formally opened, enabling large-scale trade and cultural exchange between East and West.",
    "张骞通西域后，汉武帝在河西走廊设立四郡（武威、张掖、酒泉、敦煌），控制了通往西域的咽喉要道。中国的丝绸、漆器、铁器西传，西域的葡萄、胡桃、苜蓿、良马和佛教文化东来。丝绸之路不仅是一条商路，更是连接欧亚大陆上中华文明、印度文明、波斯文明和地中海文明的纽带。",
    "After Zhang Qian's mission, Emperor Wu established four commanderies along the Hexi Corridor, controlling the vital passage to the Western Regions. Chinese silk, lacquerware, and ironwork traveled westward, while grapes, walnuts, alfalfa, fine horses, and Buddhism came eastward along the Silk Road—a conduit connecting Chinese, Indian, Persian, and Mediterranean civilizations.",
    ["src-shiji"], ["evt-zhang-qian"],
    datePrecision="range", confidenceScore=0.8
)

# Colosseum
evt(
    "evt-colosseum",
    "罗马斗兽场建成",
    "Completion of the Roman Colosseum",
    80, 80,
    "roman-empire", "罗马", "Rome",
    41.89, 12.49,
    [],
    ["建筑", "文化", "罗马"],
    ["Architecture", "Culture", "Rome"],
    4,
    "罗马斗兽场（弗拉维安露天剧场）在提图斯皇帝统治下建成，成为罗马帝国最宏伟的建筑象征。",
    "The Colosseum (Flavian Amphitheatre) was completed under Emperor Titus, becoming the grandest architectural symbol of the Roman Empire.",
    "斗兽场于公元72年韦斯帕芗皇帝在位时动工，公元80年由其子提图斯完成。这座椭圆形建筑长189米、宽156米、高48米，可容纳五万观众，用于角斗士比赛、动物狩猎和模拟海战等表演。它是古罗马工程技术的巅峰之作，至今仍是罗马最具标志性的建筑。",
    "Construction began under Emperor Vespasian in 72 CE and was completed by his son Titus in 80 CE. The elliptical structure, 189m long, 156m wide, and 48m high, seated 50,000 spectators for gladiatorial contests, animal hunts, and mock naval battles. It remains the iconic symbol of ancient Roman engineering.",
    [], [],
    confidenceScore=0.95, datePrecision="year"
)

# ==================== EARLY MEDIEVAL (1st-10th century) ====================

# Fall of Han
evt(
    "evt-fall-of-han",
    "汉朝灭亡 / 三国鼎立",
    "Fall of the Han Dynasty / Three Kingdoms Begins",
    220, 220,
    "china", "洛阳", "Luoyang",
    34.7, 112.4,
    ["cao-cao"],
    ["政治", "朝代更替", "战争"],
    ["Politics", "Dynastic Change", "War"],
    5,
    "曹丕篡汉称帝，东汉灭亡，中国进入魏蜀吴三国鼎立的分裂时代。",
    "Cao Pi forced the last Han emperor to abdicate, ending the Eastern Han Dynasty and beginning the Three Kingdoms period of Wei, Shu, and Wu.",
    "公元220年，曹操之子曹丕逼迫汉献帝禅让，建立魏国，定都洛阳。次年刘备在成都称帝建立蜀汉，229年孙权在建业称帝建立东吴。三国鼎立局面形成，持续约六十年。这一时期虽战乱频繁，但在政治、军事和文化上留下了深远影响，《三国演义》更是让这段历史家喻户晓。",
    "In 220 CE, Cao Pi, son of Cao Cao, forced Emperor Xian of Han to abdicate and founded the Wei dynasty at Luoyang. The following year, Liu Bei declared himself emperor of Shu Han in Chengdu, and in 229 CE, Sun Quan proclaimed himself emperor of Eastern Wu. The Three Kingdoms period lasted about 60 years, leaving a profound cultural legacy immortalized in 'Romance of the Three Kingdoms.'",
    [], [],
    confidenceScore=0.9, datePrecision="year"
)

# Fall of Western Rome
evt(
    "evt-fall-western-rome",
    "西罗马帝国灭亡",
    "Fall of the Western Roman Empire",
    476, 476,
    "roman-empire", "拉文纳", "Ravenna",
    44.4, 12.2,
    [],
    ["政治", "帝国崩溃", "罗马", "中世纪"],
    ["Politics", "Imperial Collapse", "Rome", "Middle Ages"],
    5,
    "日耳曼将领奥多亚塞废黜末代皇帝罗慕路斯·奥古斯都，西罗马帝国灭亡，欧洲进入中世纪。",
    "The Germanic commander Odoacer deposed the last emperor, Romulus Augustulus, ending the Western Roman Empire and marking the beginning of the Middle Ages in Europe.",
    "公元476年，日耳曼雇佣兵首领奥多亚塞废黜了年仅16岁的西罗马末代皇帝罗慕路斯·奥古斯都，将皇权标志送往东罗马首都君士坦丁堡，宣称不再需要西罗马皇帝。这一事件传统上被视为古典时代的终结和中世纪的开始。东罗马（拜占庭）帝国则继续存在了近一千年。",
    "In 476 CE, the Germanic mercenary leader Odoacer deposed the 16-year-old Romulus Augustulus, sending the imperial regalia to Constantinople and declaring there was no need for a Western emperor. This event traditionally marks the end of classical antiquity and the beginning of the Middle Ages. The Eastern Roman (Byzantine) Empire endured for nearly another thousand years.",
    [], [],
    confidenceScore=0.9, datePrecision="year"
)

# Tang Dynasty founding
evt(
    "evt-tang-founding",
    "唐朝建立",
    "Founding of the Tang Dynasty",
    618, 618,
    "tang-dynasty", "长安", "Chang'an",
    34.3, 108.9,
    ["li-shimin", "li-yuan"],
    ["政治", "朝代更替", "唐朝"],
    ["Politics", "Dynastic Change", "Tang Dynasty"],
    5,
    "李渊在长安称帝，建立唐朝。李世民通过玄武门之变继位，开创贞观之治。",
    "Li Yuan declared himself emperor at Chang'an, founding the Tang Dynasty. Li Shimin seized power through the Xuanwu Gate Incident, inaugurating the Zhenguan era of prosperity.",
    "公元617年，隋末天下大乱，太原留守李渊起兵反隋，次年攻占长安，立隋炀帝之孙杨侑为帝。618年隋炀帝被杀后，李渊称帝，国号唐。626年其次子李世民发动玄武门之变，杀死太子建成和齐王元吉，迫使李渊退位。李世民即位后开创贞观之治，使唐朝成为当时世界上最强大的帝国。",
    "In 618, amid the chaos of the collapsing Sui Dynasty, Li Yuan declared himself emperor at Chang'an, establishing the Tang Dynasty. In 626, his son Li Shimin staged the Xuanwu Gate coup, killing his brothers and forcing his father to abdicate. As Emperor Taizong, Li Shimin inaugurated the Zhenguan era, making Tang China the most powerful empire in the world.",
    [], [],
    confidenceScore=0.9, datePrecision="year"
)

# Rise of Islam
evt(
    "evt-rise-of-islam",
    "伊斯兰教兴起",
    "Rise of Islam",
    610, 632,
    "middle-east", "麦加 / 麦地那", "Mecca / Medina",
    24.5, 39.6,
    [],
    ["宗教", "伊斯兰", "中东"],
    ["Religion", "Islam", "Middle East"],
    5,
    "先知穆罕默德在阿拉伯半岛传播伊斯兰教，建立了统一阿拉伯半岛的政教合一政权。",
    "Prophet Muhammad spread Islam across the Arabian Peninsula, establishing a unified religio-political state.",
    "公元610年，穆罕默德在麦加城外希拉山洞首次接受天使加百列的启示。622年，他率领追随者从麦加迁徙至麦地那（希吉拉），这一年被定为伊斯兰历元年。至632年穆罕默德去世时，阿拉伯半岛大部分已皈依伊斯兰教。此后，阿拉伯帝国（倭马亚和阿拔斯哈里发国）迅速扩张，伊斯兰教传播到亚非欧三大洲。",
    "In 610 CE, Muhammad received his first revelation from the Angel Gabriel in the Cave of Hira near Mecca. In 622, he and his followers migrated to Medina (the Hijra), marking year one of the Islamic calendar. By his death in 632, most of the Arabian Peninsula had embraced Islam. The Arab empires (Umayyad and Abbasid Caliphates) rapidly expanded, spreading Islam across three continents.",
    [], [],
    datePrecision="range", confidenceScore=0.9, isApproximate=True
)

# Battle of Tours
evt(
    "evt-battle-tours",
    "图尔战役（普瓦捷战役）",
    "Battle of Tours (Battle of Poitiers)",
    732, 732,
    "europe", "图尔（今法国）", "Tours (present-day France)",
    47.4, 0.7,
    ["charles-martel"],
    ["战争", "宗教", "欧洲", "伊斯兰扩张"],
    ["War", "Religion", "Europe", "Islamic Expansion"],
    4,
    "法兰克王国宫相查理·马特在图尔附近击败倭马亚哈里发国的军队，阻止了伊斯兰势力向欧洲腹地的扩张。",
    "Frankish ruler Charles Martel defeated the Umayyad army near Tours, halting the Islamic expansion into the heart of Europe.",
    "公元732年，倭马亚哈里发国的阿拉伯-柏柏尔军队越过比利牛斯山，深入法兰克王国腹地。宫相查理·马特在图尔和普瓦捷之间组织防御，以重装步兵方阵击溃了阿拉伯骑兵。这场战役被许多西方史学家视为决定欧洲命运的关键一战，查理·马特也因此获得'铁锤'（Martel）的称号。",
    "In 732 CE, the Arab-Berber army of the Umayyad Caliphate crossed the Pyrenees deep into Frankish territory. Charles Martel, Mayor of the Palace, organized a defensive line of heavy infantry between Tours and Poitiers, repelling the Arab cavalry. Many Western historians consider this a decisive battle for the fate of Europe.",
    [], [],
    confidenceScore=0.8, datePrecision="year"
)

# Charlemagne crowned
evt(
    "evt-charlemagne",
    "查理曼加冕为罗马皇帝",
    "Charlemagne Crowned Holy Roman Emperor",
    800, 800,
    "europe", "罗马", "Rome",
    41.9, 12.5,
    ["charlemagne"],
    ["政治", "宗教", "帝国", "欧洲"],
    ["Politics", "Religion", "Empire", "Europe"],
    5,
    "教皇利奥三世在罗马为法兰克国王查理曼加冕为'罗马人的皇帝'，开启了神圣罗马帝国的传统。",
    "Pope Leo III crowned the Frankish king Charlemagne as 'Emperor of the Romans' in Rome, inaugurating the tradition of the Holy Roman Empire.",
    "公元800年圣诞节，查理曼在罗马圣彼得大教堂参加弥撒时，教皇利奥三世突然将一顶皇冠戴在他头上，宣布他为'罗马人的皇帝'。这一举动既承认了查理曼作为西欧统治者的地位，也标志着西欧在罗马帝国灭亡三个多世纪后的政治复兴，同时也加剧了东西教会的分裂趋势。",
    "On Christmas Day 800 CE, as Charlemagne knelt in prayer at St. Peter's Basilica, Pope Leo III placed a crown on his head and proclaimed him 'Emperor of the Romans.' This act recognized Charlemagne's supremacy in Western Europe, marked a political revival three centuries after Rome's fall, and deepened the rift between Eastern and Western Christianity.",
    [], [],
    confidenceScore=0.9, datePrecision="year"
)

# An Lushan Rebellion
evt(
    "evt-an-lushan",
    "安史之乱",
    "An Lushan Rebellion",
    755, 763,
    "tang-dynasty", "洛阳 / 长安", "Luoyang / Chang'an",
    34.7, 112.4,
    ["li-bai", "du-fu"],
    ["战争", "叛乱", "唐朝", "转折点"],
    ["War", "Rebellion", "Tang Dynasty", "Turning Point"],
    5,
    "安禄山起兵反唐，席卷北方，导致唐朝由盛转衰，成为中国历史的重要转折点。",
    "An Lushan's rebellion against the Tang swept through northern China, marking the dynasty's irreversible decline and a major turning point in Chinese history.",
    "公元755年，身兼范阳、平卢、河东三镇节度使的安禄山以讨伐杨国忠为名，在范阳起兵反唐，很快攻占洛阳和长安。唐玄宗仓皇逃往四川，太子李亨在灵武即位（唐肃宗）。叛乱持续八年，虽最终平定，但唐朝从此由盛转衰，藩镇割据局面形成，中央权威一蹶不振。",
    "In 755 CE, An Lushan, military governor of three strategic border commands, rose in rebellion, quickly capturing Luoyang and Chang'an. Emperor Xuanzong fled to Sichuan while his son assumed the throne at Lingwu. Though the rebellion was quelled after eight years, the Tang Dynasty never recovered its former glory, as regional warlords gained de facto independence.",
    [], [],
    datePrecision="range", confidenceScore=0.9
)

# Battle of Talas
evt(
    "evt-battle-talas",
    "怛罗斯战役",
    "Battle of Talas",
    751, 751,
    "middle-east", "怛罗斯（今吉尔吉斯斯坦）", "Talas (present-day Kyrgyzstan)",
    42.5, 71.3,
    [],
    ["战争", "唐朝", "阿拉伯", "文化交流"],
    ["War", "Tang Dynasty", "Arab", "Cultural Exchange"],
    4,
    "唐朝安西都护府军队与阿拔斯哈里发军队在怛罗斯交战，唐军战败，造纸术由此西传。",
    "The Tang Anxi Protectorate army clashed with the Abbasid Caliphate forces at Talas. The Tang defeat inadvertently led to the westward transmission of papermaking technology.",
    "公元751年，唐安西节度使高仙芝率军远征石国（今塔什干），石国求援于阿拔斯哈里发。双方在怛罗斯河畔激战五日，唐军因葛逻禄部临阵倒戈而大败。被俘的唐军工匠将造纸术传入阿拉伯世界，再由阿拉伯人传到欧洲。这场战役标志着唐朝在中亚扩张的终点，也意外促进了文明的交流。",
    "In 751 CE, Tang general Gao Xianzhi led an expedition against the Kingdom of Shash (Tashkent), which appealed to the Abbasid Caliphate for help. After five days of battle along the Talas River, the Tang army was defeated when Qarluq mercenaries defected. Chinese prisoners of war introduced papermaking to the Islamic world, from where it eventually reached Europe.",
    [], [],
    confidenceScore=0.8, datePrecision="year"
)

# ==================== SONG / MEDIEVAL (11th-13th century) ====================

# Norman Conquest
evt(
    "evt-norman-conquest",
    "诺曼征服英格兰",
    "Norman Conquest of England",
    1066, 1066,
    "england", "黑斯廷斯", "Hastings",
    50.9, 0.5,
    ["william-conqueror"],
    ["战争", "征服", "英格兰", "诺曼"],
    ["War", "Conquest", "England", "Norman"],
    5,
    "诺曼底公爵威廉在黑斯廷斯战役中击败英王哈罗德，征服英格兰，重塑了英国的政治、语言和文化。",
    "Duke William of Normandy defeated King Harold at the Battle of Hastings, conquering England and reshaping its politics, language, and culture.",
    "1066年1月英王忏悔者爱德华去世，哈罗德·戈德温森继位。诺曼底公爵威廉以爱德华曾许诺王位为由，率军渡海入侵英格兰。10月14日在黑斯廷斯战役中，哈罗德战死，威廉于圣诞节在威斯敏斯特加冕为英格兰国王。诺曼征服将法语和封建制度带入英格兰，深远影响了英语和英国制度的发展。",
    "When Edward the Confessor died childless in January 1066, Harold Godwinson assumed the throne. Duke William of Normandy, claiming Edward had promised him the crown, invaded England. At the Battle of Hastings on October 14, Harold was killed, and William was crowned king at Westminster on Christmas Day. The Norman Conquest brought French language and feudalism to England.",
    [], [],
    confidenceScore=0.95, datePrecision="year"
)

# First Crusade
evt(
    "evt-first-crusade",
    "第一次十字军东征",
    "First Crusade",
    1096, 1099,
    "middle-east", "耶路撒冷", "Jerusalem",
    31.8, 35.2,
    [],
    ["宗教", "战争", "十字军", "中东", "欧洲"],
    ["Religion", "War", "Crusades", "Middle East", "Europe"],
    5,
    "教皇乌尔班二世号召收复圣地，十字军攻占耶路撒冷，建立四个十字军王国，开启近200年的十字军运动。",
    "Pope Urban II called for the liberation of the Holy Land; Crusaders captured Jerusalem and established four Crusader states, initiating nearly two centuries of the Crusading movement.",
    "1095年，拜占庭皇帝阿莱克修斯一世向教皇求援对抗塞尔柱突厥人。教皇乌尔班二世在克莱蒙会议上号召基督徒武装收复耶路撒冷。1099年7月15日，经过三年艰苦远征，十字军攻破耶路撒冷，进行了大规模屠杀。他们在黎凡特建立了耶路撒冷王国、安条克公国、埃德萨伯国和的黎波里伯国四个十字军国家。",
    "In 1095, Byzantine Emperor Alexios I appealed to the Pope for aid against the Seljuk Turks. Pope Urban II at the Council of Clermont called for an armed pilgrimage to liberate Jerusalem. On July 15, 1099, after three years of arduous journey, the Crusaders breached Jerusalem's walls and massacred its inhabitants. They established four Crusader states in the Levant.",
    [], [],
    datePrecision="range", confidenceScore=0.9
)

# Genghis Khan unification
evt(
    "evt-genghis-unification",
    "成吉思汗统一蒙古",
    "Genghis Khan Unifies the Mongols",
    1206, 1206,
    "mongol-empire", "斡难河源头", "Headwaters of the Onon River",
    48.6, 110.1,
    ["genghis-khan"],
    ["政治", "统一", "蒙古", "帝国"],
    ["Politics", "Unification", "Mongol", "Empire"],
    5,
    "铁木真在忽里勒台大会上被推举为成吉思汗，统一蒙古各部，建立了人类历史上最大的陆地帝国之基础。",
    "Temüjin was proclaimed Genghis Khan at a Kurultai assembly, uniting all Mongol tribes and laying the foundation for the largest contiguous land empire in history.",
    "经过二十余年的征战，铁木真先后击败了塔塔儿部、克烈部、乃蛮部和蔑儿乞部等对手，统一了蒙古高原。1206年春，他在斡难河源头召开忽里勒台（部落大会），被推举为'成吉思汗'（意为'海洋般的大汗'），建立大蒙古国。他颁布《大札撒》法典，创立千户制，组建了当时世界上最强大的骑兵军团。",
    "After over twenty years of warfare, Temüjin defeated the Tatars, Kereyids, Naimans, Merkits, and other rivals, unifying the Mongolian plateau. In spring 1206, at a Kurultai (tribal assembly) at the headwaters of the Onon River, he was proclaimed 'Genghis Khan' ('Oceanic Ruler'), establishing the Great Mongol State with a new legal code (Yassa) and a decimal military organization.",
    [], [],
    confidenceScore=0.85, datePrecision="year"
)

# Magna Carta
evt(
    "evt-magna-carta",
    "大宪章签署",
    "Signing of Magna Carta",
    1215, 1215,
    "england", "兰尼米德", "Runnymede",
    51.4, -0.5,
    [],
    ["政治", "法律", "宪政", "英格兰"],
    ["Politics", "Law", "Constitutionalism", "England"],
    5,
    "英格兰贵族迫使约翰王签署大宪章，确立了'王在法下'的原则，成为现代宪政的基石。",
    "English barons forced King John to sign Magna Carta, establishing the principle that the king is subject to the law—a cornerstone of modern constitutionalism.",
    "英王约翰穷兵黩武且横征暴敛，引发贵族大规模叛乱。1215年6月15日，反叛贵族在兰尼米德草地迫使约翰王签署《大宪章》。文件共63条，限制了王权对贵族和自由民的任意处置，确立了正当法律程序、陪审团审判等原则。虽然后来被约翰王废除，但其精神成为英美宪政传统的源头。",
    "King John's costly wars and arbitrary taxation provoked a baronial rebellion. On June 15, 1215, at Runnymede meadow, the rebel barons forced John to seal Magna Carta. Its 63 clauses limited the king's arbitrary power over nobles and freemen, establishing due process and trial by jury. Though soon annulled, its principles became the foundation of Anglo-American constitutional tradition.",
    [], [],
    confidenceScore=0.9, datePrecision="year"
)

# Mongol sack of Baghdad
evt(
    "evt-sack-baghdad",
    "蒙古攻陷巴格达",
    "Mongol Sack of Baghdad",
    1258, 1258,
    "mongol-empire", "巴格达", "Baghdad",
    33.3, 44.4,
    ["hulegu"],
    ["战争", "征服", "蒙古", "伊斯兰", "文化毁灭"],
    ["War", "Conquest", "Mongol", "Islam", "Cultural Destruction"],
    5,
    "旭烈兀率领蒙古军攻陷巴格达，灭亡阿拔斯哈里发国，伊斯兰黄金时代宣告终结。",
    "Hülegü Khan's Mongol army sacked Baghdad, extinguishing the Abbasid Caliphate and bringing the Islamic Golden Age to an end.",
    "1258年1月，成吉思汗之孙旭烈兀率蒙古大军围攻阿拔斯哈里发国首都巴格达。哈里发穆斯台绥木拒绝投降。2月10日城破后，蒙古军展开了七天的大屠杀和破坏，数十万人遇难，智慧宫、图书馆和灌溉系统被摧毁。五百年的阿拔斯哈里发国灭亡，伊斯兰文明的古典黄金时代戛然而止。",
    "In January 1258, Hülegü Khan, grandson of Genghis Khan, besieged Baghdad, capital of the Abbasid Caliphate. Caliph Al-Musta'sim refused to surrender. When the city fell on February 10, the Mongols unleashed seven days of massacre and destruction; hundreds of thousands perished, the House of Wisdom and libraries were razed, and irrigation systems destroyed. The five-century Abbasid Caliphate collapsed.",
    [], [],
    confidenceScore=0.9, datePrecision="year"
)

# Marco Polo
evt(
    "evt-marco-polo",
    "马可·波罗抵达中国",
    "Marco Polo Arrives in China",
    1275, 1275,
    "mongol-empire", "上都", "Shangdu (Xanadu)",
    42.3, 116.1,
    ["marco-polo", "kublai-khan"],
    ["旅行", "探索", "文化交流", "蒙古"],
    ["Travel", "Exploration", "Cultural Exchange", "Mongol"],
    4,
    "威尼斯商人马可·波罗沿丝绸之路抵达元上都，在忽必烈汗宫廷服务17年，其游记引发了欧洲对东方的向往。",
    "Venetian merchant Marco Polo reached Shangdu via the Silk Road, serving Kublai Khan's court for 17 years. His travelogue ignited European fascination with the East.",
    "1271年，17岁的马可·波罗随父亲和叔叔从威尼斯出发，经丝绸之路穿越中亚，于1275年抵达元上都，受到忽必烈汗的接见。马可·波罗在元朝为官十七年，游历中国各地。1295年返回威尼斯后，他在热那亚狱中口述了《马可·波罗游记》，首次向欧洲详细描述了远东的富庶与文明，启发了后来的大航海时代。",
    "In 1271, the 17-year-old Marco Polo set out with his father and uncle from Venice, traveling via the Silk Road through Central Asia to reach Shangdu in 1275, where he was received by Kublai Khan. He served in the Yuan court for 17 years, traveling extensively across China. His dictated account, 'The Travels of Marco Polo,' gave Europe its first detailed description of the Far East.",
    [], [],
    confidenceScore=0.75, datePrecision="year"
)

# ==================== RENAISSANCE / EARLY MODERN (14th-16th century) ====================

# Black Death
evt(
    "evt-black-death",
    "黑死病大流行",
    "The Black Death",
    1347, 1351,
    "europe", "欧洲全境", "All of Europe",
    45.0, 10.0,
    [],
    ["瘟疫", "灾难", "人口", "欧洲"],
    ["Plague", "Disaster", "Demographics", "Europe"],
    5,
    "鼠疫从亚洲经丝绸之路和贸易路线传入欧洲，在四年内夺走约三分之一欧洲人口，彻底改变了欧洲社会结构。",
    "The bubonic plague traveled from Asia along the Silk Road and trade routes to Europe, killing roughly one-third of the European population in four years and transforming the continent's social structure.",
    "1347年，鼠疫从克里米亚的卡法传入地中海世界，随后沿贸易路线迅速席卷整个欧洲。四年间，约2500万人死亡，占欧洲人口的三分之一。这场浩劫动摇了封建制度的基础：劳动力锐减提高了幸存者的议价能力，对教会的信仰产生怀疑，推动了医学和公共卫生的发展，间接为文艺复兴和宗教改革创造了条件。",
    "In 1347, the plague entered the Mediterranean world from Kaffa in Crimea and quickly spread along trade routes across Europe. In four years, roughly 25 million people—one-third of Europe's population—perished. The catastrophe shook feudalism's foundations: labor scarcity improved survivors' bargaining power, faith in the Church eroded, and the disaster spurred advances in medicine and public health.",
    [], [],
    datePrecision="range", confidenceScore=0.9
)

# Hundred Years War
evt(
    "evt-hundred-years-war",
    "百年战争",
    "Hundred Years' War",
    1337, 1453,
    "europe", "法国", "France",
    48.9, 2.4,
    ["joan-of-arc"],
    ["战争", "英法", "民族国家", "中世纪"],
    ["War", "England-France", "Nation-State", "Middle Ages"],
    5,
    "英法之间断续持续116年的王朝战争，催生了两个现代民族国家的意识，以法国的最终胜利告终。",
    "A dynastic conflict between England and France lasting intermittently for 116 years, which gave birth to modern national consciousness in both countries, ending in French victory.",
    "1337年，英王爱德华三世以母亲的血统为由宣称法国王位，百年战争爆发。战争经历了英军节节胜利（克雷西战役1346、普瓦捷战役1356）、法国反攻（查理五世时期）和最终的法国翻盘。1429年圣女贞德解奥尔良之围，成为战争的转折点。1453年英军在卡斯蒂永战役中溃败，除加来外失去全部大陆领地。",
    "In 1337, Edward III of England claimed the French throne through his mother's lineage, launching the Hundred Years' War. The war saw English triumphs at Crécy (1346) and Poitiers (1356), a French resurgence under Charles V, and ultimately a French reversal. Joan of Arc's relief of Orléans in 1429 was the turning point. In 1453, the English were decisively defeated at Castillon.",
    [], [],
    datePrecision="range", confidenceScore=0.9
)

# Fall of Constantinople
evt(
    "evt-fall-constantinople",
    "君士坦丁堡陷落",
    "Fall of Constantinople",
    1453, 1453,
    "byzantine", "君士坦丁堡（今伊斯坦布尔）", "Constantinople (present-day Istanbul)",
    41.0, 28.9,
    ["mehmed-ii"],
    ["战争", "征服", "拜占庭", "奥斯曼"],
    ["War", "Conquest", "Byzantine", "Ottoman"],
    5,
    "奥斯曼苏丹穆罕默德二世攻陷君士坦丁堡，拜占庭帝国灭亡。希腊学者携带古典文献逃往意大利，推动了文艺复兴。",
    "Ottoman Sultan Mehmed II captured Constantinople, ending the Byzantine Empire. Greek scholars fled to Italy with classical manuscripts, fueling the Renaissance.",
    "1453年4月，年仅21岁的奥斯曼苏丹穆罕默德二世率八万大军和巨型火炮围攻君士坦丁堡。守城的拜占庭皇帝君士坦丁十一世仅有七千守军。5月29日城破，拜占庭末代皇帝战死。延续1123年的罗马帝国（东罗马）至此终结。大批希腊学者携古典手稿逃往意大利，为方兴未艾的文艺复兴注入了古希腊学术的源泉。",
    "In April 1453, the 21-year-old Sultan Mehmed II besieged Constantinople with 80,000 troops and massive cannons. Emperor Constantine XI had only 7,000 defenders. The city fell on May 29; the last Byzantine emperor died in battle. The Roman Empire (Eastern), which had endured for 1,123 years, was extinguished. Greek scholars fleeing to Italy brought classical manuscripts that enriched the Renaissance.",
    [], [],
    confidenceScore=0.95, datePrecision="year"
)

# Gutenberg printing
evt(
    "evt-gutenberg",
    "古腾堡发明活字印刷",
    "Gutenberg's Printing Press",
    1450, 1455,
    "renaissance-europe", "美因茨", "Mainz",
    50.0, 8.3,
    ["johannes-gutenberg"],
    ["科技", "印刷", "文艺复兴", "信息传播"],
    ["Technology", "Printing", "Renaissance", "Information"],
    5,
    "约翰内斯·古腾堡发明金属活字印刷术，印刷了《古腾堡圣经》，开启了知识传播的革命。",
    "Johannes Gutenberg invented movable metal type printing and produced the Gutenberg Bible, igniting a revolution in knowledge dissemination.",
    "约1450年，德国金匠古腾堡在美因茨发明了金属活字印刷术，结合了活字、油墨和螺旋压印机。1455年，他印刷了180本《四十二行圣经》（古腾堡圣经），是西方第一本大规模生产的书籍。印刷术使书籍成本大幅降低，知识传播速度空前加快，为宗教改革、科学革命和大众教育奠定了基础。",
    "Around 1450, the German goldsmith Gutenberg invented movable metal type printing in Mainz, combining movable type, oil-based ink, and a screw press. By 1455, he had printed 180 copies of the 42-line 'Gutenberg Bible'—the first mass-produced book in the West. Printing dramatically reduced book costs and accelerated knowledge dissemination, laying foundations for the Reformation, Scientific Revolution, and mass education.",
    [], [],
    datePrecision="range", confidenceScore=0.9, isApproximate=True
)

# Columbus
evt(
    "evt-columbus",
    "哥伦布发现新大陆",
    "Columbus Reaches the Americas",
    1492, 1492,
    "renaissance-europe", "瓜纳哈尼岛（今巴哈马）", "Guanahani (present-day Bahamas)",
    24.0, -75.0,
    ["christopher-columbus"],
    ["探索", "地理大发现", "殖民", "全球化"],
    ["Exploration", "Age of Discovery", "Colonization", "Globalization"],
    5,
    "哥伦布率领西班牙船队横渡大西洋抵达美洲，开启了欧洲殖民扩张和全球贸易的新纪元。",
    "Columbus, sailing for Spain, crossed the Atlantic and reached the Americas, inaugurating the era of European colonial expansion and global trade.",
    "1492年8月3日，哥伦布得到西班牙王室资助，率三艘帆船从帕洛斯港出发。10月12日，船队抵达巴哈马群岛中的一个小岛（哥伦布命名为'圣萨尔瓦多'）。尽管哥伦布至死认为他到达了亚洲，但他的航行开启了持续数世纪的'哥伦布大交换'——人员、动植物、疾病和文化在欧亚非美各大洲间的剧烈交流。",
    "On August 3, 1492, Columbus sailed from Palos with three ships, funded by the Spanish Crown. On October 12, the fleet reached an island in the Bahamas (which Columbus named 'San Salvador'). Though Columbus died believing he had reached Asia, his voyages initiated the centuries-long 'Columbian Exchange'—the massive transfer of people, plants, animals, diseases, and cultures between continents.",
    [], [],
    confidenceScore=0.9, datePrecision="year"
)

# Zheng He voyages
evt(
    "evt-zheng-he",
    "郑和下西洋",
    "Zheng He's Treasure Voyages",
    1405, 1433,
    "ming-dynasty", "印度洋", "Indian Ocean",
    5.0, 60.0,
    ["zheng-he"],
    ["航海", "探索", "明朝", "外交"],
    ["Maritime", "Exploration", "Ming Dynasty", "Diplomacy"],
    5,
    "明成祖派遣郑和率领庞大舰队七次远航西洋，到达东南亚、印度、阿拉伯和东非，展示了明朝的海上力量。",
    "Emperor Yongle dispatched Zheng He with a massive fleet on seven voyages across the 'Western Ocean,' reaching Southeast Asia, India, Arabia, and East Africa, demonstrating Ming China's maritime power.",
    "1405年至1433年间，明朝三宝太监郑和在明成祖和明宣宗的支持下，七次率领庞大舰队远航西洋。舰队拥有数百艘船只和两万七千余名船员，宝船长约125米。船队访问了三十多个国家和地区，最远到达非洲东海岸。这些航行比哥伦布横渡大西洋早近一个世纪，但明朝随后实施了海禁政策，主动退出了海洋。",
    "Between 1405 and 1433, the Ming eunuch-admiral Zheng He, under Emperors Yongle and Xuande, led seven expeditions with a fleet of hundreds of ships and over 27,000 crew—treasure ships measuring up to 125 meters. The fleet visited over 30 states and regions, reaching as far as the East African coast. These voyages preceded Columbus by nearly a century, but Ming China subsequently adopted a policy of maritime prohibition.",
    [], [],
    datePrecision="range", confidenceScore=0.85
)

# Protestant Reformation
evt(
    "evt-reformation",
    "马丁·路德发动宗教改革",
    "Martin Luther Launches the Reformation",
    1517, 1517,
    "renaissance-europe", "维滕贝格", "Wittenberg",
    51.9, 12.6,
    ["martin-luther"],
    ["宗教", "改革", "基督教", "欧洲"],
    ["Religion", "Reformation", "Christianity", "Europe"],
    5,
    "马丁·路德在维滕贝格教堂门上张贴《九十五条论纲》，公开质疑天主教会赎罪券的合法性，点燃了欧洲宗教改革运动。",
    "Martin Luther posted his 'Ninety-Five Theses' on the door of the Wittenberg Castle Church, publicly challenging the legitimacy of indulgences and igniting the Protestant Reformation.",
    "1517年10月31日，奥古斯丁会修士马丁·路德在维滕贝格城堡教堂门上张贴《九十五条论纲》，核心是质疑教皇出售赎罪券以赦免罪过的做法。路德后来提出'因信称义'的教义，主张信徒可直接通过圣经与上帝沟通，无需教会作为中介。宗教改革永久性地分裂了西方基督教世界，产生了新教（路德宗、加尔文宗、英国国教等）。",
    "On October 31, 1517, the Augustinian monk Martin Luther posted his 'Ninety-Five Theses' on the door of Wittenberg's Castle Church, primarily challenging the papal sale of indulgences for the remission of sins. Luther later articulated the doctrine of 'justification by faith alone,' arguing that believers could access God directly through Scripture without ecclesiastical mediation. The Reformation permanently fractured Western Christendom.",
    [], [],
    confidenceScore=0.95, datePrecision="year"
)

# Da Vinci / Renaissance high
evt(
    "evt-renaissance-high",
    "文艺复兴鼎盛期",
    "High Renaissance",
    1495, 1527,
    "renaissance-europe", "佛罗伦萨 / 罗马", "Florence / Rome",
    43.8, 11.3,
    ["leonardo-da-vinci", "michelangelo", "raphael"],
    ["艺术", "文化", "文艺复兴", "欧洲"],
    ["Art", "Culture", "Renaissance", "Europe"],
    5,
    "达·芬奇、米开朗基罗和拉斐尔等大师在意大利创作了一批划时代的艺术杰作，将文艺复兴推向顶峰。",
    "Masters like Leonardo da Vinci, Michelangelo, and Raphael created epoch-making artistic masterpieces in Italy, bringing the Renaissance to its zenith.",
    "1495年至1527年间（从达·芬奇创作《最后的晚餐》到罗马之劫），意大利经历了文艺复兴的鼎盛期。达·芬奇创作了《蒙娜丽莎》，米开朗基罗完成了西斯廷教堂天顶画和《大卫》雕像，拉斐尔绘制了《雅典学院》。这一时期融合了古典人文主义、科学观察和艺术创造力，定义了西方艺术的基本范式。",
    "Between 1495 (Leonardo's 'Last Supper') and 1527 (the Sack of Rome), Italy experienced the zenith of the Renaissance. Leonardo painted the 'Mona Lisa,' Michelangelo completed the Sistine Chapel ceiling and 'David,' and Raphael created 'The School of Athens.' This period fused classical humanism, scientific observation, and artistic creativity, defining Western art's fundamental paradigm.",
    [], [],
    datePrecision="range", confidenceScore=0.9
)

# ==================== MODERN (17th-20th century) ====================

# Thirty Years' War
evt(
    "evt-thirty-years-war",
    "三十年战争",
    "Thirty Years' War",
    1618, 1648,
    "europe", "神圣罗马帝国（中欧地区）", "Holy Roman Empire (Central Europe)",
    49.5, 11.0,
    [],
    ["战争", "宗教", "政治", "欧洲"],
    ["War", "Religion", "Politics", "Europe"],
    5,
    "始于波希米亚的新教叛乱，蔓延为全欧洲的宗教-政治大混战，以《威斯特伐利亚和约》确立了现代主权国家体系。",
    "Beginning as a Protestant revolt in Bohemia, the war escalated into a pan-European religious-political conflict, ending with the Peace of Westphalia, which established the modern system of sovereign states.",
    "1618年，波希米亚新教徒将哈布斯堡皇帝的使者抛出窗外（'布拉格抛窗事件'），战争爆发。冲突逐步将西班牙、法国、瑞典、丹麦等欧洲主要国家卷入，德意志地区成为主战场，人口损失近三分之一。1648年《威斯特伐利亚和约》结束了战争，在国际关系中确立了国家主权、领土完整和不干涉内政的原则。",
    "In 1618, Bohemian Protestants defenestrated Habsburg imperial envoys ('Defenestration of Prague'), triggering the war. The conflict gradually drew in Spain, France, Sweden, Denmark, and other major European powers; the German lands, the main battleground, lost nearly a third of their population. The 1648 Peace of Westphalia established the principles of national sovereignty and non-interference.",
    [], [],
    datePrecision="range", confidenceScore=0.9
)

# English Civil War
evt(
    "evt-english-civil-war",
    "英国内战",
    "English Civil War",
    1642, 1651,
    "england", "英格兰", "England",
    52.0, -1.0,
    ["oliver-cromwell"],
    ["战争", "革命", "政治", "英格兰"],
    ["War", "Revolution", "Politics", "England"],
    5,
    "议会派与国王查理一世之间的内战，以国王被处决和短暂的共和国（英联邦）建立告终，确立了议会至上的原则。",
    "The civil war between Parliamentarians and King Charles I ended with the king's execution and a brief republic (the Commonwealth), establishing the principle of parliamentary supremacy.",
    "查理一世推行'君权神授'的专制统治，与议会围绕税收和宗教问题矛盾激化。1642年内战爆发，克伦威尔领导的新模范军在纳斯比战役（1645年）中决定性击败王军。1649年查理一世被审判并处决，英国宣布为共和国（英联邦）。1660年王政复辟，但1688年'光荣革命'最终确立了君主立宪制。",
    "Charles I's assertion of 'divine right' absolutism brought him into conflict with Parliament over taxation and religion. Civil war erupted in 1642; Cromwell's New Model Army decisively defeated the Royalists at Naseby (1645). Charles I was tried and executed in 1649, and England was declared a Commonwealth. Though the monarchy was restored in 1660, the 1688 Glorious Revolution permanently established constitutional monarchy.",
    [], [],
    datePrecision="range", confidenceScore=0.9
)

# Qing conquers China
evt(
    "evt-qing-conquest",
    "清军入关",
    "Qing Conquest of China",
    1644, 1644,
    "china", "北京", "Beijing",
    39.9, 116.4,
    [],
    ["政治", "朝代更替", "清朝", "征服"],
    ["Politics", "Dynastic Change", "Qing Dynasty", "Conquest"],
    5,
    "李自成攻破北京，明崇祯帝自缢。吴三桂引清军入关，多尔衮率满洲八旗占领北京，清朝开始统治中国。",
    "Li Zicheng captured Beijing; the last Ming emperor hanged himself. Wu Sangui opened Shanhai Pass to the Qing forces, and Dorgon's Manchu banner army occupied Beijing, beginning Qing rule over China.",
    "1644年，李自成率领大顺农民军攻破北京，崇祯帝在煤山自缢，明朝中央政权灭亡。山海关总兵吴三桂原欲投降李自成，后转而求助于关外的清军。摄政王多尔衮率满洲八旗入关，与吴三桂联军在山海关击败李自成，随即占领北京。顺治帝迁都北京，清朝开始了对中国的268年统治。",
    "In 1644, Li Zicheng's peasant army captured Beijing; the Chongzhen Emperor hanged himself at Coal Hill, ending the Ming central government. Wu Sangui, commander of Shanhai Pass, initially prepared to surrender to Li but instead sought help from the Manchus. Regent Dorgon led the Manchu banners through the pass, defeated Li Zicheng's forces, and occupied Beijing, inaugurating 268 years of Qing rule.",
    [], [],
    confidenceScore=0.9, datePrecision="year"
)

# Newton's Principia
evt(
    "evt-newton-principia",
    "牛顿发表《自然哲学的数学原理》",
    "Newton Publishes the Principia",
    1687, 1687,
    "europe", "剑桥", "Cambridge",
    52.2, 0.1,
    ["isaac-newton"],
    ["科学", "物理学", "科学革命", "启蒙"],
    ["Science", "Physics", "Scientific Revolution", "Enlightenment"],
    5,
    "牛顿发表《原理》，提出万有引力定律和三大运动定律，奠定了经典物理学的基础。",
    "Newton's 'Principia' presented the law of universal gravitation and three laws of motion, laying the foundation of classical physics.",
    "1687年，牛顿在哈雷的鼓励和资助下出版了《自然哲学的数学原理》，用数学语言系统阐述了力学的基本定律。书中提出了万有引力定律和三大运动定律，统一了天上和地上的力学。这一成就标志着科学革命的顶峰，牛顿力学在此后两个多世纪中一直是物理学不可动摇的基础，直到爱因斯坦相对论的出现。",
    "In 1687, with Edmond Halley's encouragement and funding, Newton published 'Philosophiæ Naturalis Principia Mathematica,' systematically presenting the fundamental laws of mechanics in mathematical language. The book unified celestial and terrestrial mechanics with the law of universal gravitation and three laws of motion. This achievement crowned the Scientific Revolution, and Newtonian mechanics remained physics' unshakeable foundation for over two centuries.",
    [], [],
    confidenceScore=0.95, datePrecision="year"
)

# American Revolution
evt(
    "evt-american-revolution",
    "美国独立战争",
    "American Revolution",
    1775, 1783,
    "europe", "北美十三殖民地", "Thirteen Colonies (North America)",
    40.0, -75.0,
    ["george-washington"],
    ["战争", "革命", "独立", "美国"],
    ["War", "Revolution", "Independence", "America"],
    5,
    "北美十三殖民地反抗英国统治的独立战争，建立了美利坚合众国，深刻影响了全球的政治思潮。",
    "The Thirteen Colonies' war of independence against British rule established the United States of America, profoundly influencing global political thought.",
    "1775年，列克星敦和康科德的枪声拉开了独立战争的序幕。1776年7月4日，大陆会议通过《独立宣言》（杰斐逊起草），宣告'人人生而平等'的天赋人权理念。在华盛顿的领导下，大陆军经历艰难曲折，1777年萨拉托加大捷后获得法国公开支持，1781年约克镇战役击败英军主力。1783年《巴黎条约》承认美国独立。",
    "In 1775, shots at Lexington and Concord began the Revolutionary War. On July 4, 1776, the Continental Congress adopted the Declaration of Independence (drafted by Jefferson), proclaiming natural rights and that 'all men are created equal.' Under Washington's leadership, the Continental Army endured hardships, securing French support after Saratoga (1777) and defeating the main British army at Yorktown (1781). The 1783 Treaty of Paris recognized American independence.",
    [], [],
    datePrecision="range", confidenceScore=0.9
)

# French Revolution
evt(
    "evt-french-revolution",
    "法国大革命",
    "French Revolution",
    1789, 1799,
    "europe", "巴黎", "Paris",
    48.9, 2.4,
    ["napoleon"],
    ["革命", "政治", "法国", "民主"],
    ["Revolution", "Politics", "France", "Democracy"],
    5,
    "巴黎民众攻占巴士底狱，推翻法国君主制，宣告'自由、平等、博爱'，深刻改变了欧洲和世界的政治格局。",
    "Parisians stormed the Bastille, overthrew the French monarchy, and proclaimed 'Liberty, Equality, Fraternity,' fundamentally altering the political landscape of Europe and the world.",
    "1789年，法国面临严重的财政危机和社会矛盾。5月三级会议召开后，第三等级代表宣布成立国民议会。7月14日，巴黎民众攻占巴士底狱（象征王权专制的要塞），革命全面爆发。8月通过《人权宣言》。1792年废除君主制，1793年处决路易十六。革命历经吉伦特派、雅各宾派（恐怖统治）、督政府等阶段，1799年以拿破仑发动雾月政变而告一段落。",
    "In 1789, France faced severe fiscal crisis and social unrest. After the Estates-General convened in May, the Third Estate declared itself the National Assembly. On July 14, Parisians stormed the Bastille (symbol of royal absolutism), and the Revolution erupted. The Declaration of the Rights of Man followed in August. The monarchy was abolished in 1792, Louis XVI executed in 1793, and after phases of Girondin, Jacobin (Reign of Terror), and Directory rule, the Revolution culminated in Napoleon's coup of Brumaire in 1799.",
    [], [],
    datePrecision="range", confidenceScore=0.95
)

# Napoleon wars
evt(
    "evt-napoleon-wars",
    "拿破仑战争",
    "Napoleonic Wars",
    1803, 1815,
    "europe", "欧洲全境", "All of Europe",
    48.9, 2.4,
    ["napoleon"],
    ["战争", "帝国", "法国", "欧洲"],
    ["War", "Empire", "France", "Europe"],
    5,
    "拿破仑率法国军队横扫欧洲大陆，建立庞大的法兰西帝国，最终在滑铁卢战役中失败。",
    "Napoleon led French armies across the European continent, building a vast French Empire, before his final defeat at the Battle of Waterloo.",
    "1804年拿破仑加冕为法兰西皇帝后，对欧洲各国发动了一系列战争。奥斯特里茨战役（1805年）是其军事天才的巅峰。拿破仑帝国鼎盛时控制了从西班牙到波兰的广大地区。1812年远征俄国惨败后局势逆转。1814年反法同盟占领巴黎，拿破仑被流放厄尔巴岛。1815年他短暂复辟（百日王朝），但在滑铁卢战役（1815年6月18日）中遭遇最终失败。",
    "After crowning himself Emperor in 1804, Napoleon waged a series of wars across Europe. The Battle of Austerlitz (1805) marked the zenith of his military genius. At its height, the Napoleonic Empire controlled territory from Spain to Poland. The disastrous 1812 Russian campaign reversed his fortunes; the Allies occupied Paris in 1814, and Napoleon was exiled to Elba. His brief return in 1815 (the Hundred Days) ended in final defeat at Waterloo.",
    [], [],
    datePrecision="range", confidenceScore=0.95
)

# Opium War
evt(
    "evt-opium-war",
    "第一次鸦片战争",
    "First Opium War",
    1839, 1842,
    "china", "广州 / 南京", "Guangzhou / Nanjing",
    32.1, 118.8,
    ["lin-zexu"],
    ["战争", "殖民", "清朝", "不平等条约"],
    ["War", "Colonialism", "Qing Dynasty", "Unequal Treaty"],
    5,
    "林则徐虎门销烟引发中英战争，清政府战败后签订《南京条约》，中国被迫打开国门，进入'百年国耻'的近代史。",
    "Lin Zexu's destruction of opium at Humen triggered war with Britain; China's defeat and the Treaty of Nanjing opened the country by force, beginning the 'century of humiliation.'",
    "1839年，钦差大臣林则徐在广东虎门销毁收缴的鸦片，英国以此为借口发动战争。英军凭借坚船利炮先后攻占定海、广州、厦门、宁波、上海、镇江，兵临南京城下。1842年8月，清政府被迫签订中国近代第一个不平等条约《南京条约》：割让香港岛，开放五口通商，赔款2100万银元。中国由此被卷入世界资本主义体系。",
    "In 1839, Imperial Commissioner Lin Zexu destroyed confiscated opium at Humen, prompting Britain to wage war. British naval and military superiority overwhelmed Chinese coastal defenses; after capturing key cities from Guangzhou to Zhenjiang, British forces reached Nanjing. In August 1842, the Qing signed the Treaty of Nanjing (China's first unequal treaty): ceding Hong Kong, opening five treaty ports, and paying 21 million silver dollars in indemnity.",
    [], [],
    datePrecision="range", confidenceScore=0.95
)

# Meiji Restoration
evt(
    "evt-meiji",
    "明治维新",
    "Meiji Restoration",
    1868, 1868,
    "japan", "东京（江户）", "Tokyo (Edo)",
    35.7, 139.8,
    [],
    ["改革", "现代化", "日本", "工业革命"],
    ["Reform", "Modernization", "Japan", "Industrial Revolution"],
    5,
    "倒幕派拥立明治天皇，推翻德川幕府，推行全面西化改革，使日本在三十年内从封建国家转变为近代工业强国。",
    "Reformers restored Emperor Meiji to power, overthrew the Tokugawa Shogunate, and launched comprehensive Western-style modernization that transformed Japan from a feudal state into a modern industrial power within thirty years.",
    "1868年1月，倒幕派（萨摩、长州等藩）发动政变，宣布'王政复古'，废除幕府，建立以天皇为核心的新政府。明治天皇发布《五条誓文》，推行一系列改革：废藩置县（1871年）、建立新式陆海军、普及义务教育、引进西方技术和制度、扶持近代工业。到19世纪末，日本已成为亚洲唯一的工业化国家，1895年击败清朝，1905年击败俄国。",
    "In January 1868, reformist domains (Satsuma, Chōshū) staged a coup, proclaiming the 'restoration' of imperial rule and abolishing the shogunate. Emperor Meiji issued the Charter Oath and launched sweeping reforms: abolishing feudal domains for prefectures (1871), creating a modern army and navy, introducing compulsory education, adopting Western technology, and nurturing modern industry. By century's end, Japan had become Asia's only industrialized nation.",
    [], [],
    confidenceScore=0.9, datePrecision="year"
)

# World War I
evt(
    "evt-wwi",
    "第一次世界大战",
    "World War I",
    1914, 1918,
    "europe", "欧洲全境", "Europe",
    48.0, 10.0,
    [],
    ["战争", "世界战争", "20世纪", "全球"],
    ["War", "World War", "20th Century", "Global"],
    5,
    "第一次全球规模的大战，以萨拉热窝事件为导火索，同盟国与协约国厮杀四年，造成约1600万人死亡，终结了四大帝国。",
    "The first truly global war, triggered by the assassination in Sarajevo, pitted the Allies against the Central Powers for four years, resulting in roughly 16 million deaths and the collapse of four empires.",
    "1914年6月28日，奥匈帝国皇储斐迪南在萨拉热窝遇刺，同盟国与协约国的对抗机制启动，欧洲各国在数周内全面开战。战争从运动战陷入惨烈的堑壕战（马恩河、凡尔登、索姆河）。1917年美国参战，俄国爆发革命退出。1918年11月11日德国投降。战后奥匈、奥斯曼、俄罗斯和德意志四大帝国解体，中东和欧洲版图被彻底重划。",
    "On June 28, 1914, Archduke Franz Ferdinand of Austria-Hungary was assassinated in Sarajevo, triggering the alliance system that plunged European powers into war within weeks. The conflict devolved into brutal trench warfare (the Marne, Verdun, the Somme). The United States entered in 1917; Russia withdrew after its revolution. Germany surrendered on November 11, 1918. Four empires collapsed, and the maps of Europe and the Middle East were redrawn.",
    [], [],
    datePrecision="range", confidenceScore=0.95
)

# October Revolution
evt(
    "evt-october-revolution",
    "俄国十月革命",
    "Russian October Revolution",
    1917, 1917,
    "europe", "彼得格勒（今圣彼得堡）", "Petrograd (present-day St. Petersburg)",
    59.9, 30.3,
    ["lenin"],
    ["革命", "社会主义", "俄国", "20世纪"],
    ["Revolution", "Socialism", "Russia", "20th Century"],
    5,
    "列宁领导布尔什维克党武装夺取政权，建立了世界上第一个社会主义国家，深刻影响了整个20世纪。",
    "Lenin led the Bolsheviks in an armed seizure of power, establishing the world's first socialist state and profoundly shaping the entire 20th century.",
    "1917年，俄国在第一次世界大战中损失惨重，经济崩溃，社会矛盾激化。二月革命推翻了沙皇专制，随即出现资产阶级临时政府和工兵苏维埃两个政权并存的局面。11月7日（俄历10月25日），列宁领导的布尔什维克党发动武装起义，攻占冬宫，推翻临时政府。随后建立了苏维埃政权，退出一战，开始建设世界上第一个社会主义国家。",
    "In 1917, Russia's catastrophic losses in World War I, economic collapse, and social unrest led to the February Revolution, which overthrew the tsar, creating dual power: the Provisional Government and the Soviets of Workers' and Soldiers' Deputies. On November 7 (October 25 O.S.), Lenin's Bolsheviks seized power, storming the Winter Palace and overthrowing the Provisional Government. They established Soviet power and withdrew from WWI.",
    [], [],
    confidenceScore=0.95, datePrecision="year"
)

# World War II
evt(
    "evt-wwii",
    "第二次世界大战",
    "World War II",
    1939, 1945,
    "europe", "全球", "Global",
    51.0, 10.0,
    [],
    ["战争", "世界战争", "20世纪", "全球"],
    ["War", "World War", "20th Century", "Global"],
    5,
    "人类历史上规模最大的全球战争，轴心国与同盟国在欧亚非三大洲血战六年，造成约7000万人死亡，彻底重塑了世界秩序。",
    "The largest and most destructive conflict in human history, pitting the Axis against the Allies across Europe, Asia, and Africa for six years with roughly 70 million deaths, fundamentally reshaping the global order.",
    "1939年9月1日，纳粹德国入侵波兰，英法对德宣战，二战全面爆发。德国以'闪电战'迅速占领西欧，1941年入侵苏联。日本于1941年12月7日偷袭珍珠港，美国参战。战争在斯大林格勒（1942-43）、诺曼底登陆（1944年6月6日）等战役中逆转。1945年5月8日德国投降，8月广岛和长崎原子弹爆炸后日本投降。战后建立了联合国，美苏冷战格局形成。",
    "On September 1, 1939, Nazi Germany invaded Poland; Britain and France declared war, beginning WWII. Germany's 'Blitzkrieg' rapidly overran Western Europe before invading the Soviet Union in 1941. Japan's attack on Pearl Harbor (December 7, 1941) brought the U.S. into the war. The tide turned at Stalingrad (1942-43) and D-Day (June 6, 1944). Germany surrendered May 8, 1945; Japan surrendered after the atomic bombings of Hiroshima and Nagasaki.",
    [], [],
    datePrecision="range", confidenceScore=0.95
)

# UN founded
evt(
    "evt-un-founded",
    "联合国成立",
    "Founding of the United Nations",
    1945, 1945,
    "europe", "旧金山", "San Francisco",
    37.8, -122.4,
    [],
    ["政治", "国际组织", "和平", "全球治理"],
    ["Politics", "International Organization", "Peace", "Global Governance"],
    4,
    "51个国家签署《联合国宪章》，联合国正式成立，旨在维护国际和平与安全，促进国际合作。",
    "Fifty-one nations signed the UN Charter, formally establishing the United Nations with the aims of maintaining international peace and security and promoting international cooperation.",
    "1945年4月至6月，50个国家的代表在旧金山召开联合国国际组织会议，起草了《联合国宪章》。6月26日，51个创始成员国签署宪章。联合国于10月24日正式成立（这一天被定为'联合国日'），宗旨包括维护国际和平与安全、发展各国友好关系、促进国际合作。联合国取代了失败的国联，成为二战后全球治理的核心机构。",
    "From April to June 1945, representatives of 50 nations met at the United Nations Conference on International Organization in San Francisco, drafting the UN Charter. On June 26, 51 founding members signed the Charter. The UN officially came into existence on October 24 (celebrated as UN Day), with purposes including maintaining international peace and security, developing friendly relations among nations, and promoting international cooperation.",
    [], [],
    confidenceScore=0.95, datePrecision="year"
)

# ==================== Additional key events ====================

# Battle of Marathon
evt(
    "evt-marathon",
    "马拉松战役",
    "Battle of Marathon",
    -490, -490,
    "europe", "马拉松（希腊）", "Marathon (Greece)",
    38.1, 23.9,
    [],
    ["战争", "希腊", "波斯", "古典时代"],
    ["War", "Greece", "Persia", "Classical Antiquity"],
    4,
    "雅典军队在马拉松平原击败波斯入侵军，保卫了希腊城邦的独立，奠定了西方文明的独立发展道路。",
    "The Athenian army defeated the invading Persian force on the plain of Marathon, preserving the independence of the Greek city-states and ensuring the independent development of Western civilization.",
    "公元前490年，波斯帝国大流士一世派遣远征军横渡爱琴海，意在惩罚支持小亚细亚希腊城邦起义的雅典。波斯军队在马拉松平原登陆。雅典将军米太亚德以一万一千重装步兵对抗约两万五千波斯军，利用中央薄弱、两翼加强的战术取得决定性胜利。传说一名士兵跑了42公里回雅典报捷后力竭而死，今天的马拉松赛跑起源于此。",
    "In 490 BCE, Darius I of Persia sent an expeditionary force across the Aegean to punish Athens for supporting a revolt by Greek cities in Asia Minor. The Persians landed on the plain of Marathon. Athenian general Miltiades deployed 11,000 hoplites against roughly 25,000 Persians, winning a decisive victory using a weak-center, strong-wings tactic. Legend says a messenger ran 42 km to Athens with news of victory and collapsed dead.",
    [], [],
    confidenceScore=0.8, datePrecision="year"
)

# Building of the Pyramids
evt(
    "evt-great-pyramid",
    "胡夫金字塔建成",
    "Completion of the Great Pyramid of Giza",
    -2560, -2560,
    "middle-east", "吉萨（今埃及）", "Giza (present-day Egypt)",
    29.98, 31.13,
    [],
    ["建筑", "工程", "古埃及"],
    ["Architecture", "Engineering", "Ancient Egypt"],
    5,
    "埃及第四王朝法老胡夫建造了古代世界七大奇迹中最古老也是唯一保存至今的金字塔。",
    "Pharaoh Khufu of Egypt's Fourth Dynasty built the oldest and only surviving wonder of the ancient world—the Great Pyramid of Giza.",
    "约公元前2560年，胡夫法老在吉萨高原建造了世界上最大的金字塔。这座金字塔原高146.6米，由约230万块巨石组成，每块平均重2.5吨。金字塔的建造展现了古埃及人惊人的数学、天文和工程水平。它作为古代世界七大奇迹之首，也是其中唯一保存至今的伟大建筑。",
    "Around 2560 BCE, Pharaoh Khufu built the largest pyramid in the world on the Giza plateau. Originally standing 146.6m tall, it consists of about 2.3 million stone blocks, each averaging 2.5 tons. The pyramid's construction demonstrates the ancient Egyptians' remarkable mastery of mathematics, astronomy, and engineering. It is the oldest and only surviving wonder of the ancient world.",
    [], [],
    confidenceScore=0.7, datePrecision="year", isApproximate=True
)

# Gupta Empire golden age
evt(
    "evt-gupta-golden",
    "笈多王朝黄金时代",
    "Gupta Empire Golden Age",
    320, 550,
    "india", "华氏城（今巴特那）", "Pataliputra (present-day Patna)",
    25.6, 85.1,
    ["kalidasa"],
    ["文化", "科学", "数学", "印度"],
    ["Culture", "Science", "Mathematics", "India"],
    5,
    "笈多王朝时期印度在数学（发明零的概念）、天文学、医学和文学方面取得了辉煌成就，被称为印度的'黄金时代'。",
    "Under the Gupta Empire, India achieved brilliant advances in mathematics (inventing the concept of zero), astronomy, medicine, and literature, earning it the name India's 'Golden Age.'",
    "公元320年—550年间，笈多王朝统一了北印度大部分地区。这一时期印度在科学和艺术上达到了古代世界的巅峰：数学家阿耶波多计算出π值、提出地动说、发明了'零'的十进制概念；医学著作《阇罗迦集》和《妙闻集》系统记载了外科和内科知识；诗人迦梨陀娑创作了《沙恭达罗》等梵语文学巨著。",
    "Between 320-550 CE, the Gupta Empire unified much of northern India. This period saw India reach ancient heights in science and art: mathematician Aryabhata calculated pi, proposed heliocentrism, and formalized the decimal system with zero; medical texts (Charaka Samhita, Sushruta Samhita) systematically documented surgery and internal medicine; poet Kalidasa composed 'Shakuntala' and other Sanskrit masterpieces.",
    [], [],
    datePrecision="range", confidenceScore=0.75, isApproximate=True
)

# Pearl Harbor
evt(
    "evt-pearl-harbor",
    "珍珠港事件",
    "Attack on Pearl Harbor",
    1941, 1941,
    "japan", "珍珠港（夏威夷）", "Pearl Harbor (Hawaii)",
    21.3, -157.9,
    [],
    ["战争", "日本", "美国", "二战"],
    ["War", "Japan", "United States", "WWII"],
    5,
    "日本海军突袭美国太平洋舰队基地珍珠港，促使美国正式加入第二次世界大战。",
    "The Imperial Japanese Navy launched a surprise attack on the U.S. Pacific Fleet at Pearl Harbor, bringing the United States into World War II.",
    "1941年12月7日清晨（夏威夷时间），日本海军航空兵对夏威夷珍珠港的美军基地发动了突然袭击。在约两小时的攻击中，日军击沉或重创了8艘战列舰、3艘巡洋舰、3艘驱逐舰，摧毁188架飞机，造成2403名美国人死亡。次日，美国对日宣战。三天后德国和意大利对美国宣战，美国正式全面投入二战。",
    "In the early morning of December 7, 1941 (Hawaii time), Japanese naval aircraft launched a surprise attack on the U.S. base at Pearl Harbor. In roughly two hours, they sank or severely damaged eight battleships, three cruisers, and three destroyers, destroyed 188 aircraft, and killed 2,403 Americans. The next day, the U.S. declared war on Japan; three days later, Germany and Italy declared war on the U.S.",
    [], ["evt-wwii"],
    confidenceScore=0.95, datePrecision="year"
)

# Moon landing
evt(
    "evt-moon-landing",
    "阿波罗11号登月",
    "Apollo 11 Moon Landing",
    1969, 1969,
    "europe", "月球静海基地", "Mare Tranquillitatis (Moon)",
    0.7, 23.5,
    [],
    ["科技", "太空探索", "美国", "20世纪"],
    ["Technology", "Space Exploration", "United States", "20th Century"],
    5,
    "美国宇航员尼尔·阿姆斯特朗成为第一个踏上月球的人类，'这是个人的一小步，却是人类的一大步'。",
    "American astronaut Neil Armstrong became the first human to set foot on the Moon: 'That's one small step for a man, one giant leap for mankind.'",
    "1969年7月20日，阿波罗11号登月舱'鹰号'在月球静海降落。宇航员尼尔·阿姆斯特朗在月球表面留下了人类的第一个脚印，说出了那句著名的'个人一小步，人类一大步'。巴兹·奥尔德林随后也踏上月面。这项成就标志着冷战时期美苏太空竞赛的巅峰，也是人类第一次踏上地球以外的天体。",
    "On July 20, 1969, the Apollo 11 lunar module 'Eagle' landed in the Sea of Tranquility. Astronaut Neil Armstrong left the first human footprint on the lunar surface, uttering the famous words about one small step for a man and one giant leap for mankind. Buzz Aldrin joined him shortly after. This achievement marked the pinnacle of the Cold War space race and humanity's first steps on another celestial body.",
    [], [],
    confidenceScore=0.95, datePrecision="year"
)

# Fall of Berlin Wall
evt(
    "evt-berlin-wall",
    "柏林墙倒塌",
    "Fall of the Berlin Wall",
    1989, 1989,
    "europe", "柏林", "Berlin",
    52.5, 13.4,
    [],
    ["政治", "冷战", "德国", "20世纪"],
    ["Politics", "Cold War", "Germany", "20th Century"],
    5,
    "分隔东西柏林28年的柏林墙被推倒，象征着冷战的结束和德国统一的开始。",
    "The Berlin Wall, which had divided East and West Berlin for 28 years, was torn down, symbolizing the end of the Cold War and the beginning of German reunification.",
    "1989年，东欧剧变浪潮席卷。11月9日晚，东德政府宣布开放边境。数以万计的东柏林民众涌向柏林墙的各个检查站，墙上凿开的缺口迅速扩大。接下来的数月中，柏林墙被民众一块块敲碎运走。1990年10月3日，两德正式统一。柏林墙的倒塌不仅标志着冷战的终结，也预示着苏联解体和世界格局的根本性改变。",
    "In 1989, a wave of change swept Eastern Europe. On the evening of November 9, the East German government announced the opening of its borders. Tens of thousands of East Berliners flooded to checkpoints, and breaches in the Wall rapidly widened. Over the following months, citizens chipped away at the Wall piece by piece. On October 3, 1990, Germany was formally reunified. The Wall's fall signaled not only the end of the Cold War.",
    [], [],
    confidenceScore=0.95, datePrecision="year"
)

# ==================== Additional events to reach 100+ ====================

# Alexander the Great
evt(
    "evt-alexander",
    "亚历山大大帝东征",
    "Alexander the Great's Conquests",
    -334, -323,
    "europe", "马其顿 → 印度", "Macedonia to India",
    40.0, 30.0,
    ["alexander-great"],
    ["战争", "征服", "希腊化", "古代"],
    ["War", "Conquest", "Hellenistic", "Ancient"],
    5,
    "马其顿国王亚历山大率军横扫波斯帝国，建立横跨欧亚非的庞大帝国，开启了希腊化时代。",
    "Macedonian king Alexander led his army in sweeping conquest of the Persian Empire, building a vast empire spanning Europe, Asia, and Africa, inaugurating the Hellenistic Age.",
    "公元前334年，年仅22岁的马其顿国王亚历山大率军渡过赫勒斯滂海峡，开始了对波斯帝国的征服。他在格拉尼库斯河、伊苏斯和高加米拉三次决定性战役中击败波斯大军，灭亡了阿契美尼德王朝。亚历山大一直打到印度河流域，建立了地跨欧亚非的庞大帝国。他33岁在巴比伦病逝，但其征服深刻改变了古代世界：希腊语成为地中海东部的通用语，希腊文化与东方文明融合形成了'希腊化文明'。",
    "In 334 BCE, the 22-year-old Macedonian king Alexander crossed the Hellespont, beginning his conquest of the Persian Empire. He defeated the Persian forces in three decisive battles at Granicus, Issus, and Gaugamela, extinguishing the Achaemenid dynasty. Alexander reached the Indus River before his troops refused to go further. He died in Babylon at 33, but his conquests fused Greek culture with Eastern civilizations, creating the 'Hellenistic' world.",
    [], [],
    datePrecision="range", confidenceScore=0.9
)

# Han Dynasty Silk Road peak
evt(
    "evt-han-golden",
    "汉武盛世",
    "Reign of Emperor Wu of Han",
    -141, -87,
    "china", "长安", "Chang'an",
    34.3, 108.9,
    ["zhang-qian"],
    ["政治", "扩张", "汉朝", "盛世"],
    ["Politics", "Expansion", "Han Dynasty", "Golden Age"],
    5,
    "汉武帝刘彻在位54年，北逐匈奴、南平百越、西通西域，奠定了中华帝国疆域的基本框架。",
    "Emperor Wu of Han (Liu Che) reigned for 54 years, driving back the Xiongnu, subduing the southern Yue, and opening the Western Regions, establishing the territorial framework of imperial China.",
    "汉武帝刘彻（公元前141年—前87年在位）是汉朝在位时间最长的皇帝。他在军事上派卫青、霍去病大破匈奴，将河西走廊纳入版图；在外交上派遣张骞出使西域，开辟丝绸之路；在国内推行推恩令削弱诸侯、盐铁官营加强中央财政、独尊儒术统一思想。汉武盛世使汉朝的国力达到顶峰，'汉'从此成为中华民族的代称。",
    "Emperor Wu (r. 141-87 BCE) was the longest-reigning Han emperor. Militarily, he sent Wei Qing and Huo Qubing to decisively defeat the Xiongnu, incorporating the Hexi Corridor. Diplomatically, he dispatched Zhang Qian to open the Silk Road. Domestically, he weakened feudal lords, established salt and iron monopolies, and made Confucianism the state orthodoxy. The Han reached its apex under his rule.",
    ["src-shiji"], ["evt-zhang-qian", "evt-silk-road"],
    datePrecision="range", confidenceScore=0.9
)

# Viking raids begin
evt(
    "evt-viking-raids",
    "维京时代开始",
    "Viking Age Begins",
    793, 793,
    "europe", "林迪斯法恩（英格兰）", "Lindisfarne (England)",
    55.7, -1.8,
    [],
    ["掠夺", "航海", "北欧", "中世纪"],
    ["Raiding", "Navigation", "Norse", "Middle Ages"],
    4,
    "北欧维京人袭击英格兰林迪斯法恩修道院，标志着长达两个多世纪的维京时代的开始。",
    "Norse Vikings raided the Lindisfarne monastery in England, marking the beginning of the Viking Age that would last over two centuries.",
    "793年6月8日，来自斯堪的纳维亚的维京人袭击了英格兰东北海岸林迪斯法恩岛上的修道院，屠杀了修士，抢走了金银财宝和圣物。这次袭击震惊了整个基督教欧洲。此后两个多世纪中，维京人以长船为工具，沿欧洲海岸线和内河进行劫掠、贸易和殖民，其影响范围从冰岛、格陵兰一直到俄罗斯、拜占庭和地中海。",
    "On June 8, 793, Vikings from Scandinavia raided the monastery on Lindisfarne island off the northeast coast of England, slaughtering monks and seizing gold, silver, and relics. The attack shocked Christian Europe. For over two centuries thereafter, Vikings used their longships to raid, trade, and colonize along European coasts and rivers, extending their reach from Iceland and Greenland to Russia, Byzantium, and the Mediterranean.",
    [], [],
    confidenceScore=0.85, datePrecision="year"
)

# Copernicus Revolution
evt(
    "evt-copernicus",
    "哥白尼发表日心说",
    "Copernicus Publishes the Heliocentric Theory",
    1543, 1543,
    "renaissance-europe", "弗龙堡（波兰）", "Frombork (Poland)",
    54.4, 19.7,
    ["nicolaus-copernicus"],
    ["科学", "天文学", "科学革命", "文艺复兴"],
    ["Science", "Astronomy", "Scientific Revolution", "Renaissance"],
    5,
    "哥白尼在临终前发表《天体运行论》，提出太阳而非地球是宇宙中心的革命性理论，开启了科学革命。",
    "Copernicus published 'On the Revolutions of the Heavenly Spheres' on his deathbed, proposing the revolutionary theory that the Sun, not the Earth, is the center of the universe—launching the Scientific Revolution.",
    "1543年，波兰天文学家哥白尼在临终前出版了《天体运行论》，系统阐述了日心说：太阳而非地球位于宇宙的中心，地球是一颗围绕太阳运转的行星。这一理论直接挑战了教会支持了一千五百余年的托勒密地心说。尽管哥白尼生前未受迫害，但其理论为伽利略、开普勒和牛顿的工作奠定了基础，被视为科学革命的开端。",
    "In 1543, Polish astronomer Copernicus published 'De Revolutionibus Orbium Coelestium' on his deathbed, systematically expounding the heliocentric theory: the Sun, not the Earth, is the center of the universe, and the Earth is a planet orbiting the Sun. This directly challenged the Ptolemaic geocentric model supported by the Church for over 1,500 years. Though Copernicus himself was not persecuted, his theory laid the foundation for Galileo, Kepler, and Newton.",
    [], [],
    confidenceScore=0.9, datePrecision="year"
)

# Galileo trial
evt(
    "evt-galileo-trial",
    "伽利略受审",
    "Galileo's Trial",
    1633, 1633,
    "renaissance-europe", "罗马", "Rome",
    41.9, 12.5,
    ["galileo-galilei"],
    ["科学", "宗教", "审判", "科学革命"],
    ["Science", "Religion", "Trial", "Scientific Revolution"],
    4,
    "宗教裁判所以'涉嫌异端'罪名审判伽利略，迫使他公开放弃哥白尼学说，成为科学与宗教冲突的象征。",
    "The Roman Inquisition tried Galileo on suspicion of heresy, forcing him to publicly recant the Copernican theory—becoming a symbol of the conflict between science and religion.",
    "1632年，伽利略出版《关于托勒密和哥白尼两大世界体系的对话》，表面上中立地讨论两种宇宙模型，实则有力地论证了哥白尼的日心说。次年宗教裁判所传唤他到罗马受审，指控他违背1616年禁止宣扬哥白尼学说的命令。1633年6月22日，69岁的伽利略被迫跪着公开'放弃、诅咒和憎恶'自己的学说。传说他低声说了一句'但它确实在动'（E pur si muove）。",
    "In 1632, Galileo published his 'Dialogue Concerning the Two Chief World Systems,' ostensibly a neutral discussion but powerfully arguing for Copernican heliocentrism. The following year, the Roman Inquisition summoned him to trial, charging him with violating the 1616 injunction against teaching Copernican theory. On June 22, 1633, the 69-year-old Galileo knelt and publicly 'abjured, cursed, and detested' his own doctrines. He allegedly whispered 'E pur si muove' ('And yet it moves').",
    [], [],
    confidenceScore=0.9, datePrecision="year"
)

# Tang golden age
evt(
    "evt-tang-gaozong",
    "唐朝盛世（贞观—开元）",
    "Tang Golden Age (Zhenguan–Kaiyuan)",
    627, 755,
    "tang-dynasty", "长安", "Chang'an",
    34.3, 108.9,
    ["li-shimin", "li-bai", "du-fu"],
    ["政治", "文化", "繁荣", "唐朝"],
    ["Politics", "Culture", "Prosperity", "Tang Dynasty"],
    5,
    "从贞观之治到开元盛世的百余年间，唐朝成为当时世界上最先进、最开放、最繁荣的文明中心。",
    "From the Zhenguan era to the Kaiyuan zenith, spanning over a century, Tang China became the most advanced, open, and prosperous center of civilization in the world.",
    "唐太宗贞观年间（627-649）至唐玄宗开元年间（713-741），唐朝国力达到顶峰。长安是当时世界最大的城市，人口超过百万，来自波斯、阿拉伯、印度、日本、朝鲜的商人、学者和僧侣云集。唐诗以李白、杜甫、王维等为代表达到了中国文学的巅峰；丝绸之路贸易空前繁荣，唐朝的政治制度、法律和汉字文化深刻影响了日本、朝鲜和越南。",
    "From Emperor Taizong's Zhenguan era (627-649) to Emperor Xuanzong's Kaiyuan era (713-741), Tang power reached its zenith. Chang'an was the world's largest city with over a million residents, attracting merchants, scholars, and monks from Persia, Arabia, India, Japan, and Korea. Tang poetry (Li Bai, Du Fu, Wang Wei) marked the apex of Chinese literature; Tang institutions deeply influenced Japan, Korea, and Vietnam.",
    [], ["evt-tang-founding", "evt-silk-road"],
    datePrecision="range", confidenceScore=0.9
)

# Kublai Khan Yuan Dynasty
evt(
    "evt-yuan-founding",
    "元朝建立（忽必烈定都大都）",
    "Kublai Khan Establishes the Yuan Dynasty",
    1271, 1271,
    "mongol-empire", "大都（今北京）", "Dadu (present-day Beijing)",
    39.9, 116.4,
    ["kublai-khan", "marco-polo"],
    ["政治", "朝代更替", "元朝", "蒙古"],
    ["Politics", "Dynastic Change", "Yuan Dynasty", "Mongol"],
    5,
    "忽必烈汗改国号为'大元'，定都大都，元朝成为中国历史上第一个由少数民族建立的大一统王朝。",
    "Kublai Khan proclaimed the 'Great Yuan' dynasty with its capital at Dadu, making it the first unified Chinese dynasty founded by a non-Han people.",
    "1271年，忽必烈汗采纳汉臣刘秉忠的建议，取《易经》'大哉乾元'之意，改国号为'大元'，次年定都大都（今北京）。1279年元军在崖山海战中消灭南宋残余势力，完成中国自唐末以来近四百年来首次真正的大一统。元朝时期，西藏正式纳入中国版图，行省制度初步确立，海上和陆上丝绸之路空前畅通。",
    "In 1271, acting on the advice of his Chinese minister Liu Bingzhong, Kublai Khan adopted the dynastic name 'Great Yuan' (from the I Ching's 'Great is the Qian Yuan') and established his capital at Dadu (Beijing). In 1279, Yuan forces destroyed the last Song resistance at the Battle of Yamen, achieving the first true unification of China in nearly 400 years. Tibet was formally incorporated, and the Silk Road flourished as never before.",
    [], ["evt-marco-polo"],
    confidenceScore=0.9, datePrecision="year"
)

# Darwin evolution
evt(
    "evt-darwin-origin",
    "达尔文发表《物种起源》",
    "Darwin Publishes 'On the Origin of Species'",
    1859, 1859,
    "europe", "伦敦", "London",
    51.5, -0.1,
    ["charles-darwin"],
    ["科学", "生物学", "进化论", "19世纪"],
    ["Science", "Biology", "Evolution", "19th Century"],
    5,
    "达尔文发表《物种起源》，提出自然选择学说，彻底改变了人类对生命和自身起源的认识。",
    "Darwin published 'On the Origin of Species,' proposing the theory of natural selection, which fundamentally transformed humanity's understanding of life and its own origins.",
    "1859年11月24日，达尔文发表《论自然选择下的物种起源》（简称《物种起源》）。书中以翔实的证据论证了物种并非不变，而是通过自然选择和适应环境的漫长过程演化而来。这一理论挑战了神创论的根基，在维多利亚时代的英国引发了激烈争议。达尔文的进化论与哥白尼的日心说和弗洛伊德的精神分析并称为改变人类自我认知的三大思想革命。",
    "On November 24, 1859, Darwin published 'On the Origin of Species by Means of Natural Selection.' The book presented rigorous evidence that species are not immutable but evolve through natural selection and adaptation over vast timescales. The theory challenged the foundations of creationism, sparking fierce debate in Victorian Britain. Darwin's theory joins Copernicus's heliocentrism and Freud's psychoanalysis as one of the three great intellectual revolutions reshaping human self-understanding.",
    [], [],
    confidenceScore=0.95, datePrecision="year"
)

# American Civil War
evt(
    "evt-civil-war",
    "美国南北战争",
    "American Civil War",
    1861, 1865,
    "europe", "美国", "United States",
    39.0, -77.0,
    ["abraham-lincoln"],
    ["战争", "奴隶制", "美国", "19世纪"],
    ["War", "Slavery", "United States", "19th Century"],
    5,
    "南北战争以林肯为首的联邦政府胜利告终，废除了奴隶制，巩固了美国的联邦统一。",
    "The Civil War ended in victory for the Union under Lincoln, abolishing slavery and consolidating the federal unity of the United States.",
    "1861年，南方11个蓄奴州脱离联邦，组成'美利坚联盟国'，南北战争爆发。林肯领导的联邦政府以维护国家统一为目标，1863年发布《解放奴隶宣言》将废除奴隶制作为战争目标。1865年4月9日，南方军总司令李将军在阿波马托克斯投降。战争造成约62万人死亡，但终结了美国的奴隶制度，并通过宪法第十三、十四和十五修正案巩固了公民权利。",
    "In 1861, eleven Southern slaveholding states seceded to form the Confederacy, precipitating the Civil War. Lincoln's Union government initially fought to preserve the nation; the 1863 Emancipation Proclamation added abolition as a war aim. On April 9, 1865, Confederate commander Robert E. Lee surrendered at Appomattox. The war cost roughly 620,000 lives but ended American slavery and consolidated civil rights through the 13th, 14th, and 15th Amendments.",
    [], [],
    datePrecision="range", confidenceScore=0.95
)

# ==================== GENERATE OUTPUT ====================


# Duplicate IDs that already exist in mockData — skip these
DUPLICATE_IDS = {'evt-qin-unification', 'evt-norman-conquest', 'evt-marco-polo'}

# Person ID mapping: IDs used in event data → actual person IDs in the dataset
PERSON_ID_MAP = {
    'abraham-lincoln': 'lincoln',
    'charles-darwin': 'darwin',
    'galileo-galilei': 'galileo',
    'george-washington': 'washington',
    'isaac-newton': 'newton',
    'johannes-gutenberg': 'gutenberg',
    'kublai-khan': 'khubilai-khan',
    'li-shimin': 'emperor-taizong',
}

# Person IDs referenced in events but don't exist in the people array — remove them
NONEXISTENT_PERSON_IDS = {
    'cao-cao', 'charles-martel', 'christopher-columbus', 'cleopatra',
    'hulegu', 'kalidasa', 'li-si', 'li-yuan', 'lin-zexu', 'liu-bang',
    'martin-luther', 'mehmed-ii', 'nicolaus-copernicus', 'oliver-cromwell',
    'raphael', 'zhang-qian'
}

# Fix event data before output
events = [e for e in events if e['id'] not in DUPLICATE_IDS]
for e in events:
    e['personIds'] = [PERSON_ID_MAP.get(p, p) for p in e['personIds'] if p not in NONEXISTENT_PERSON_IDS]

# Generate TypeScript array entries
output_lines = []
for e in events:
    pid = e["id"]
    lines = []
    lines.append(f"  // --- {e['titleEn']} ---")
    lines.append("  {")
    lines.append(f"    id: '{e['id']}',")
    lines.append(f"    title: '{esc(e['title'])}',")
    lines.append(f"    titleEn: '{esc(e['titleEn'])}',")
    lines.append(f"    startYear: {e['startYear']},")
    if e["endYear"] != e["startYear"] or e["datePrecision"] == "range":
        lines.append(f"    endYear: {e['endYear']},")
    else:
        lines.append(f"    endYear: {e['endYear']},")
    lines.append(f"    regionId: '{e['regionId']}',")
    
    if e.get("placeName"):
        lines.append(f"    placeName: '{esc(e['placeName'])}',")
    if e.get("placeNameEn"):
        lines.append(f"    placeNameEn: '{esc(e['placeNameEn'])}',")
    
    lines.append(f"    coordinates: {{ lat: {e['lat']}, lng: {e['lng']} }},")
    
    if e["personIds"]:
        person_ids_str = ", ".join(f"'{p}'" for p in e["personIds"])
        lines.append(f"    personIds: [{person_ids_str}],")
    else:
        lines.append("    personIds: [],")
    
    tags_str = ", ".join(f"'{t}'" for t in e["tags"])
    lines.append(f"    tags: [{tags_str}],")
    tags_en_str = ", ".join(f"'{t}'" for t in e["tagsEn"])
    lines.append(f"    tagsEn: [{tags_en_str}],")
    
    lines.append(f"    datePrecision: '{e['datePrecision']}' as const,")
    if e.get("isApproximate"):
        lines.append(f"    isApproximate: true,")
    else:
        lines.append(f"    isApproximate: false,")
    
    lines.append(f"    importance: {e['importance']},")
    
    lines.append(f"    summary: '{esc(e['summary'])}',")
    lines.append(f"    summaryEn: '{esc(e['summaryEn'])}',")
    lines.append(f"    description: '{esc(e['description'])}',")
    lines.append(f"    descriptionEn: '{esc(e['descriptionEn'])}',")
    
    if e["sourceIds"]:
        src_str = ", ".join(f"'{s}'" for s in e["sourceIds"])
        lines.append(f"    sourceIds: [{src_str}],")
    else:
        lines.append("    sourceIds: [],")
    
    if e["relatedEventIds"]:
        rel_str = ", ".join(f"'{r}'" for r in e["relatedEventIds"])
        lines.append(f"    relatedEventIds: [{rel_str}],")
    else:
        lines.append("    relatedEventIds: [],")
    
    lines.append(f"    dataStatus: 'published' as const,")
    lines.append(f"    confidenceScore: {e['confidenceScore']},")
    
    if e.get("externalRefs"):
        ref_lines = []
        for ref in e["externalRefs"]:
            ref_lines.append(f"{{ id: '{ref['id']}', sourceType: '{ref['sourceType']}', title: '{ref['title']}', url: '{ref['url']}', license: '{ref['license']}' }}")
        ref_str = ", ".join(ref_lines)
        lines.append(f"    externalReferences: [{ref_str}],")
    else:
        lines.append("    externalReferences: [],")
    
    lines.append("  },")
    output_lines.append("\n".join(lines))

result = "\n\n".join(output_lines)
print(result)
print(f"\n\n// Total: {len(events)} events")
