#!/usr/bin/env python3
"""Generate ~100 new Person entries for mockData.ts"""
def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'")

people = []

def p(id, name, nameEn, birth, death, regionId, tags, tagsEn, summary, summaryEn, desc, descEn,
      altNames=None, sources=None, wikidata=None, confidence=0.85):
    people.append({
        "id": id, "name": name, "nameEn": nameEn, "birthYear": birth, "deathYear": death,
        "regionId": regionId, "tags": tags, "tagsEn": tagsEn,
        "summary": summary, "summaryEn": summaryEn, "description": desc, "descriptionEn": descEn,
        "alternativeNames": altNames or [],
        "sourceIds": sources or [],
        "wikidataQid": wikidata or "",
        "dataStatus": "published",
        "confidenceScore": confidence,
        "externalReferences": []
    })

# ===== ANCIENT BCE =====
p("cleopatra-vii", "克利奥帕特拉七世", "Cleopatra VII", -69, -30, "roman-empire",
  ["政治", "埃及", "托勒密"],
  ["Politics", "Egypt", "Ptolemaic"],
  "古埃及托勒密王朝最后一任法老，以智慧、外交手腕和与罗马将领的传奇关系闻名。",
  "The last active ruler of Ptolemaic Egypt, known for her intelligence, diplomacy, and legendary relationships with Roman generals.",
  "克利奥帕特拉七世是托勒密王朝最后一位女法老，精通九种语言，是当时唯一学会埃及语的托勒密统治者。她先后与凯撒和安东尼结盟以维护埃及的独立，但在亚克兴海战失败后自杀，标志着托勒密王朝与法老时代的终结。",
  "Cleopatra VII, the last Ptolemaic pharaoh, spoke nine languages and was the only Ptolemaic ruler to learn Egyptian. She allied with Caesar and later Antony to preserve Egypt's independence. After Octavian's victory at Actium, she committed suicide, ending both the Ptolemaic dynasty and the age of pharaohs.",
  [], [], "O56", 0.9)

p("cicero", "西塞罗", "Cicero", -106, -43, "roman-empire",
  ["哲学", "政治", "修辞", "罗马"],
  ["Philosophy", "Politics", "Rhetoric", "Rome"],
  "罗马共和国末期最伟大的演说家、哲学家和政治家，其著作深刻影响了西方思想。",
  "The greatest orator, philosopher, and statesman of the late Roman Republic, whose writings profoundly shaped Western thought.",
  "马库斯·图利乌斯·西塞罗是罗马共和国末期最著名的政治家和思想家之一，以抨击喀提林阴谋和反对凯撒独裁而闻名。他的哲学、修辞学和政治学著作为西方古典传统奠定了基础。公元前43年被政敌安东尼下令处死，其头颅和双手被钉在罗马广场的讲坛上。",
  "Marcus Tullius Cicero was among the most celebrated figures of the late Republic, known for exposing the Catiline conspiracy and opposing Caesar's dictatorship. His writings on philosophy, rhetoric, and political theory became cornerstones of the Western classical tradition.",
  [], [], "O1541", 0.95)

p("liu-bang", "刘邦", "Liu Bang (Emperor Gaozu of Han)", -256, -195, "china",
  ["政治", "汉朝", "开国皇帝"],
  ["Politics", "Han Dynasty", "Founding Emperor"],
  "汉高祖，出身平民，在秦末农民起义中崛起，击败项羽建立汉朝。",
  "Emperor Gaozu of Han, who rose from peasant origins during the Qin collapse to defeat Xiang Yu and found the Han Dynasty.",
  "刘邦出身沛县农家，曾任泗水亭长。秦末天下大乱，他聚众起义，与项羽联手灭秦。在四年楚汉战争中，刘邦知人善任（萧何、张良、韩信），最终在垓下之战中击败项羽。公元前202年称帝，建立汉朝，实行郡国并行制，与民休息，为汉代四百年基业奠基。",
  "Born to a peasant family in Pei County, Liu Bang rose during the chaos of the collapsing Qin Empire. After a four-year Chu-Han war, he defeated Xiang Yu at Gaixia and founded the Han Dynasty in 202 BCE, adopting a mixed feudal-county system that stabilized the realm.",
  [], [], "", 0.9)

p("zhang-qian", "张骞", "Zhang Qian", -164, -114, "china",
  ["探索", "外交", "丝绸之路", "汉朝"],
  ["Exploration", "Diplomacy", "Silk Road", "Han Dynasty"],
  "汉代外交家、探险家，奉汉武帝之命出使西域，开辟丝绸之路的先驱。",
  "Han diplomat and explorer who opened the Silk Road by traveling from China to Central Asia on an imperial mission.",
  "公元前138年，张骞奉汉武帝之命出使西域，旨在联合大月氏夹击匈奴。途中被匈奴扣留十年，逃脱后翻越葱岭到达大宛、康居、大月氏等国。虽未达成军事联盟，但他带回大量西域地理和物产信息，为汉朝打开西方大门。司马迁赞其\"凿空\"之功。",
  "Dispatched by Emperor Wu in 138 BCE to forge an anti-Xiongnu alliance, Zhang Qian was captured by the Xiongnu for ten years. After escaping, he traversed the Pamirs to reach Ferghana, Sogdiana, and Bactria. Though no military pact materialized, his journey laid the foundation for the Silk Road.",
  [], [], "", 0.85)

p("zhuangzi", "庄子", "Zhuangzi", -369, -286, "china",
  ["哲学", "道家", "文学"],
  ["Philosophy", "Taoism", "Literature"],
  "战国时期道家学派代表人物，与老子并称'老庄'，以逍遥自由和齐物哲学闻名。",
  "Warring States Taoist philosopher, known alongside Laozi as co-founder of philosophical Taoism, celebrated for his advocacy of spiritual freedom.",
  "庄子名周，宋国蒙人。他继承和发展了老子'道法自然'的思想，主张万物齐一、逍遥无待。其著作《庄子》以汪洋恣肆的寓言和想象闻名，如《逍遥游》《齐物论》《庖丁解牛》等篇章，将深邃的哲学思想寓于生动的文学叙述之中，对中国文学和哲学影响深远。",
  "Zhuangzi (Zhuang Zhou) inherited and expanded Laozi's philosophy, advocating the unity of all things and spiritual freedom. His eponymous work uses brilliant allegories and fantastical narratives — among Chinese literature's finest — to convey profound philosophical insights through vivid storytelling.",
  [], [], "", 0.8)

# ===== ANCIENT NON-CHINESE =====
p("homer", "荷马", "Homer", -800, -700, "europe",
  ["文学", "史诗", "古希腊"],
  ["Literature", "Epic", "Ancient Greece"],
  "古希腊盲诗人，传统上被认为是《伊利亚特》和《奥德赛》的作者，西方文学之父。",
  "Ancient Greek poet traditionally credited with composing the Iliad and Odyssey, foundational works of Western literature.",
  "荷马是否真实存在历来有争议，但以他为名的两部史诗——《伊利亚特》（特洛伊战争）和《奥德赛》（奥德修斯的归途）——是西方文学的奠基之作。这些口头传统史诗约在公元前8世纪成形，探讨了英雄主义、命运与人性等永恒主题，至今仍是世界文学的巅峰。",
  "Whether Homer was a historical figure remains debated, but the two epics attributed to him — the 'Iliad' and 'Odyssey' — are foundational works of Western literature, exploring timeless themes of heroism, fate, and humanity.",
  [], [], "O6691", 0.7)

p("pericles", "伯里克利", "Pericles", -495, -429, "europe",
  ["政治", "民主", "军事", "古希腊"],
  ["Politics", "Democracy", "Military", "Ancient Greece"],
  "雅典黄金时代的政治领袖，推动民主改革，主持帕特农神庙等宏伟建筑的建设。",
  "Leading statesman of Athens' Golden Age who advanced democratic reforms and oversaw the construction of the Parthenon.",
  "伯里克利担任雅典将军三十余年（约公元前461-429年），其治下的雅典达到了政治、文化和军事的巅峰。他推行公民津贴制度使穷人也能参与政治，推动了雅典民主的深化。在他的领导下，雅典建成了帕特农神庙等不朽建筑。伯罗奔尼撒战争期间死于瘟疫。",
  "As Athens' strategos for over thirty years, Pericles deepened democracy by introducing stipends for citizens so the poor could participate. Under his leadership, Athens reached its political, cultural, and architectural zenith, culminating in the Parthenon.",
  [], [], "", 0.9)

p("darius-i", "大流士一世", "Darius I", -550, -486, "middle-east",
  ["政治", "帝国", "波斯", "行政"],
  ["Politics", "Empire", "Persia", "Administration"],
  "波斯阿契美尼德王朝最伟大的帝王之一，改革行政体系，建立行省（总督）制度，修建皇家大道。",
  "One of the greatest Achaemenid kings who reformed the Persian administration with satrapies and built the Royal Road.",
  "大流士一世（公元前522-486年在位）在平定帝国内乱后推行了一系列改革：将帝国划分为二十个行省，各省设置总督、将军和监察官三权分立；统一货币（大流克金币）；修建从苏萨到小亚细亚的'皇家大道'；开挖连接尼罗河和红海的运河。其统治奠定了波斯帝国的全盛基础。",
  "After quelling revolts, Darius I (r. 522-486 BCE) divided the empire into twenty satrapies with separated military and civil authority, unified the currency system, built the Royal Road, and dug a canal between the Nile and Red Sea, laying the foundation for the Achaemenid Empire's zenith.",
  [], [], "", 0.85)

p("vedic-seers", "吠陀仙人", "Vedic Rishis", -1500, -500, "india",
  ["宗教", "文学", "哲学", "印度教"],
  ["Religion", "Literature", "Philosophy", "Hinduism"],
  "吠陀经典的编纂者，创作了《梨俱吠陀》等印度教最古老的圣典。",
  "The compilers of the Vedas who created the Rigveda and other foundational Hindu scriptures.",
  "吠陀时期（约公元前1500-500年），无数无名的'仙人'在印度河-恒河平原创作并口耳相传了大量宗教诗歌和祭祀经文。这些作品最终汇编为四部吠陀经典：《梨俱吠陀》《娑摩吠陀》《夜柔吠陀》和《阿闼婆吠陀》，构成了印度教哲学、仪式和社会组织的根基。",
  "During the Vedic period (~1500-500 BCE), anonymous 'rishis' composed and orally transmitted religious poetry across the Indus-Ganges plain, eventually compiled into the four Vedas that form the foundation of Hindu philosophy and ritual.",
  [], [], "", 0.6)

# ===== EARLY MEDIEVAL (1-10th century) =====
p("justinian", "查士丁尼一世", "Justinian I", 482, 565, "byzantine",
  ["政治", "法律", "建筑", "拜占庭"],
  ["Politics", "Law", "Architecture", "Byzantine"],
  "拜占庭帝国最伟大的皇帝之一，编撰了《查士丁尼法典》，建造了圣索菲亚大教堂，试图恢复罗马帝国的辉煌。",
  "One of Byzantium's greatest emperors who codified Roman law into the Corpus Juris Civilis, built Hagia Sophia, and sought to restore the Roman Empire.",
  "查士丁尼一世（527-565年在位）以三个伟大成就闻名：委任法学家特里波尼安汇编罗马法为《民法大全》（影响后世欧洲法律体系）；修建了宏伟的圣索菲亚大教堂；派遣将军贝利撒留收复北非和意大利，短暂恢复了部分西罗马故土。其统治被视为拜占庭帝国的第一个黄金时代。",
  "Justinian's reign (527-565 CE) was marked by three monumental achievements: commissioning the Corpus Juris Civilis (the foundation of European civil law), constructing Hagia Sophia, and sending Belisarius to reconquer North Africa and Italy — briefly restoring parts of the Western Roman Empire.",
  [], [], "", 0.9)

p("gregory-great", "教宗额我略一世", "Pope Gregory I (Gregory the Great)", 540, 604, "europe",
  ["宗教", "政治", "音乐", "中世纪"],
  ["Religion", "Politics", "Music", "Middle Ages"],
  "罗马教皇，教会圣师，派遣传教士到英格兰传教，改革教会礼仪，对中世纪欧洲的基督教化影响深远。",
  "Pope and Doctor of the Church who sent missionaries to England, reformed the liturgy, and profoundly shaped the Christianization of medieval Europe.",
  "教宗额我略一世（590-604年在位）出身罗马贵族，曾担任罗马行政长官，后变卖家产投身修道。在职期间他派遣奥古斯丁赴英格兰传教，改革教会礼仪（额我略圣咏以他命名），并在此起彼伏的蛮族入侵中维持了罗马的秩序，被誉为'教宗国的奠基人'。",
  "Born to a Roman senatorial family, Gregory sold his property to found monasteries before becoming Pope. He sent Augustine to evangelize England, reformed the liturgy, and maintained order in Rome amid barbarian invasions, earning him the title 'Father of the Papacy.'",
  [], [], "", 0.85)

p("xuanzang", "玄奘", "Xuanzang", 602, 664, "china",
  ["宗教", "翻译", "旅行", "佛教"],
  ["Religion", "Translation", "Travel", "Buddhism"],
  "唐代高僧，历经十七年孤身西行至印度取经，带回大量佛经并翻译成中文，《大唐西域记》的作者。",
  "Tang Dynasty monk who journeyed alone to India for seventeen years, bringing back and translating Buddhist scriptures into Chinese.",
  "玄奘（602-664年）因对当时汉译佛经的歧义不满，于629年违反禁令孤身从长安出发，穿越河西走廊、中亚沙漠，翻越帕米尔高原，历经四年抵达印度。他遍学印度诸派佛学，在那烂陀寺成为荣誉住持。645年回到长安，带回657部梵文佛经，此后十九年翻译了75部1335卷经文。",
  "Dissatisfied with existing Chinese translations of Buddhist texts, Xuanzang defied a travel ban in 629 CE to journey alone across the Hexi Corridor, Central Asian deserts, and Pamir Mountains, reaching India after four years. He studied at Nalanda Monastery and returned in 645 with 657 Sanskrit texts, translating 75 works over the next 19 years.",
  [], [], "O9208", 0.9)

p("wu-zetian", "武则天", "Wu Zetian", 624, 705, "china",
  ["政治", "女性", "唐朝"],
  ["Politics", "Women", "Tang Dynasty"],
  "中国历史上唯一的正统女皇帝，改国号为周，推行科举制改革和人才选拔。",
  "China's only reigning female emperor, who changed the dynasty name to Zhou and reformed the civil service examination system.",
  "武则天原是唐太宗才人，后成为唐高宗皇后，并在高宗病重期间开始参与朝政。高宗去世后她先后废立两个儿子，于690年正式称帝，改国号为周。她在位期间大兴科举、发展经济、巩固边防，任用狄仁杰等贤臣。705年'神龙政变'后退位，与高宗合葬乾陵。",
  "Originally a concubine of Emperor Taizong, Wu became Empress to Emperor Gaozong and gradually assumed the reins of power. In 690 she proclaimed herself Emperor of a new Zhou dynasty — the only woman in Chinese history to hold the imperial title in her own right. Her reign saw expanded civil service examinations and stable governance.",
  [], [], "O1706", 0.9)

p("harun-al-rashid", "哈伦·拉希德", "Harun al-Rashid", 766, 809, "middle-east",
  ["政治", "文化", "阿拔斯", "黄金时代"],
  ["Politics", "Culture", "Abbasid", "Golden Age"],
  "阿拔斯哈里发国第五任哈里发，其统治时期是伊斯兰黄金时代的顶峰，《一千零一夜》中的传奇君主。",
  "The fifth Abbasid Caliph whose reign marked the zenith of the Islamic Golden Age, immortalized as the legendary ruler in 'One Thousand and One Nights.'",
  "哈伦·拉希德（786-809年在位）治下的巴格达是当时世界最繁华的城市。他建立了'智慧之家'，赞助翻译运动和科学研究，使巴格达成为东西方知识的交汇中心。他派遣使节到查理曼的宫廷（赠送大象和钟表），其统治的辉煌后来在《一千零一夜》中得到文学升华。",
  "Under Harun al-Rashid (r. 786-809 CE), Baghdad was the world's most cosmopolitan city. He founded the 'House of Wisdom,' sponsored translation movements, and made Baghdad a nexus of knowledge between East and West. He sent envoys bearing gifts to Charlemagne, and his reign's splendor was later immortalized in 'One Thousand and One Nights.'",
  [], [], "", 0.85)

# ===== SONG / HIGH MEDIEVAL (10-15th century) =====
p("zhu-xi", "朱熹", "Zhu Xi", 1130, 1200, "china",
  ["哲学", "教育", "理学", "儒学"],
  ["Philosophy", "Education", "Neo-Confucianism", "Confucianism"],
  "南宋理学家，集程朱理学之大成，其《四书章句集注》成为元明清科举考试的标准教材。",
  "Southern Song Neo-Confucian philosopher who synthesized the Cheng-Zhu school; his commentaries on the Four Books became the standard for imperial examinations.",
  "朱熹继承和发展了程颢、程颐的理学思想，提出'理在气先'的本体论和'格物致知'的认识论。《四书章句集注》系统注释了《大学》《中庸》《论语》《孟子》，从元代开始成为科举考试的标准答案。他的思想后来传入日本、朝鲜和越南，形成了'朱子学'的传统。",
  "Zhu Xi developed the Cheng brothers' Neo-Confucianism, proposing 'principle (li) precedes material force (qi)' and 'investigation of things to extend knowledge.' His commentaries on the Four Books became the orthodox curriculum for civil service examinations from the Yuan through Qing dynasties, and his philosophy spread to Japan, Korea, and Vietnam.",
  ["zhuzi"], [], "O9391", 0.9)

p("sima-guang", "司马光", "Sima Guang", 1019, 1086, "song-dynasty",
  ["历史", "政治", "北宋"],
  ["History", "Politics", "Northern Song"],
  "北宋政治家、史学家，《资治通鉴》的主编，保守派的代表人物。",
  "Northern Song statesman and historian, chief editor of the 'Zizhi Tongjian,' a leader of the conservative faction.",
  "司马光以主编中国最伟大的编年体通史《资治通鉴》而闻名，全书294卷，涵盖公元前403年至公元959年1362年的历史。在政治上他是保守派领袖，强烈反对王安石的变法，认为祖宗之法不可轻改。神宗去世后他短暂担任宰相，废除了大部分新法。",
  "Sima Guang is best known for editing the 'Zizhi Tongjian,' a 294-volume chronicle covering 1,362 years of Chinese history. Politically, he led the conservative opposition against Wang Anshi's reforms. After Emperor Shenzong's death, he briefly served as chancellor and reversed most of the New Policies.",
  [], [], "", 0.95)

p("minamoto-yoritomo", "源赖朝", "Minamoto no Yoritomo", 1147, 1199, "japan",
  ["政治", "军事", "幕府", "日本"],
  ["Politics", "Military", "Shogunate", "Japan"],
  "镰仓幕府的创建者，日本历史上第一个征夷大将军，开创了武士政治的时代。",
  "Founder of the Kamakura Shogunate and Japan's first Seii Taishogun, inaugurating the era of samurai rule.",
  "源赖朝在源平合战（1180-1185年）中击败平氏，随后在镰仓建立幕府，获得了任命全国守护和地头的权力。1192年获天皇任命为征夷大将军。镰仓幕府的建立标志着日本从贵族政治（平安时代）向武士政治的转型，这一体制延续了近七百年。",
  "After defeating the Taira clan in the Genpei War (1180-1185), Yoritomo established the Kamakura Shogunate, gaining authority over military governors and land stewards nationwide. Named Seii Taishogun in 1192, he inaugurated nearly 700 years of samurai governance.",
  [], [], "", 0.9)

p("joan-of-arc", "圣女贞德", "Joan of Arc", 1412, 1431, "europe",
  ["军事", "宗教", "女性", "法国"],
  ["Military", "Religion", "Women", "France"],
  "法国民族英雄，自称受神启示率军解奥尔良之围，扭转百年战争局势，终被俘火刑。",
  "French national heroine who led the relief of Orléans after claiming divine visions, turning the tide of the Hundred Years' War before being captured and burned at the stake.",
  "1429年，17岁的农家女孩贞德声称得到天使启示，要求率军解救被英军围困的奥尔良。她穿着男装说服了王太子查理，率军成功解围，随后护送查理到兰斯加冕为查理七世。1430年在贡比涅被勃艮第军队俘虏，转卖给英国人后在鲁昂以异端罪名被烧死。",
  "In 1429, the 17-year-old peasant girl Joan claimed divine visions instructing her to relieve English-besieged Orléans. Dressed in armor, she convinced the Dauphin Charles, led the successful relief, and escorted him to Reims for his coronation. Captured in 1430 and sold to the English, she was burned as a heretic in Rouen.",
  [], [], "O7226", 0.95)

p("gutenberg", "古腾堡", "Johannes Gutenberg", 1400, 1468, "renaissance-europe",
  ["发明", "印刷", "科技"],
  ["Invention", "Printing", "Technology"],
  "德国金匠，发明金属活字印刷术，印刷了《古腾堡圣经》，开启了信息传播的革命。",
  "German goldsmith who invented movable metal type printing, producing the Gutenberg Bible and igniting an information revolution.",
  "约1450年，古腾堡在美因茨发明了金属活字印刷术，结合活字、油墨和螺旋压印机。1455年他完成了约180本《四十二行圣经》的印刷，是西方第一本大规模生产的书籍。印刷术使书籍成本急剧下降，知识传播速度空前加快，为宗教改革和科学革命奠定了基础。",
  "Around 1450, Gutenberg invented movable metal type printing in Mainz, combining type, oil-based ink, and a screw press. By 1455 he had printed about 180 copies of the 'Gutenberg Bible' — the West's first mass-produced book, dramatically reducing costs and accelerating the spread of knowledge.",
  [], [], "", 0.9)

# ===== RENAISSANCE / EARLY MODERN (15-17th century) =====
p("columbus", "哥伦布", "Christopher Columbus", 1451, 1506, "renaissance-europe",
  ["探索", "航海", "殖民"],
  ["Exploration", "Navigation", "Colonization"],
  "意大利航海家，1492年横渡大西洋发现美洲大陆，开启了欧洲殖民扩张的大航海时代。",
  "Italian navigator who crossed the Atlantic in 1492 and reached the Americas, inaugurating the Age of Discovery and European colonization.",
  "哥伦布出生于热那亚，深信向西航行可以到达亚洲。1492年获得西班牙王室资助，率三艘帆船从帕洛斯港出发，10月12日到达巴哈马群岛。他先后进行了四次美洲航行，虽然至死认为他到达的是亚洲，其航行却永久改变了世界格局，开启了哥伦布大交换。",
  "Born in Genoa, Columbus firmly believed that sailing west would reach Asia. In 1492, funded by the Spanish Crown, he set sail with three ships from Palos and reached the Bahamas on October 12. His four voyages permanently reconnected the hemispheres, launching the Columbian Exchange.",
  [], [], "O7322", 0.9)

p("medici-lorenzo", "洛伦佐·德·美第奇", "Lorenzo de' Medici", 1449, 1492, "renaissance-europe",
  ["政治", "艺术", "赞助", "文艺复兴"],
  ["Politics", "Art", "Patronage", "Renaissance"],
  "佛罗伦萨的美第奇家族统治者，'豪华者'洛伦佐，文艺复兴时期最重要的艺术赞助人。",
  "Ruler of Florence and the Medici family, 'Lorenzo the Magnificent,' the most important art patron of the Renaissance.",
  "洛伦佐从20岁开始统治佛罗伦萨共和国，以精明的政治手腕维持了意大利的势力均衡。更重要的是他作为艺术赞助人的角色：米开朗基罗、达·芬奇和波提切利都曾在美第奇宫中受到支持。他在诗歌和哲学上也卓有成就，被认为体现了文艺复兴的理想——全面发展的人。",
  "Lorenzo ruled Florence from age 20, skillfully maintaining the Italian balance of power. More importantly, as a patron, he supported Michelangelo, Leonardo da Vinci, and Botticelli. A poet and philosopher himself, he embodied the Renaissance ideal of the 'universal man.'",
  [], [], "", 0.9)

p("shakespeare", "莎士比亚", "William Shakespeare", 1564, 1616, "england",
  ["文学", "戏剧", "诗歌"],
  ["Literature", "Theatre", "Poetry"],
  "英语文学史上最伟大的作家，创作了37部戏剧和154首十四行诗。",
  "The greatest writer in the English language, author of 37 plays and 154 sonnets.",
  "威廉·莎士比亚出生于埃文河畔斯特拉特福，后赴伦敦成为演员和剧作家。他创作的戏剧涵盖悲剧（《哈姆雷特》《李尔王》《麦克白》）、喜剧（《仲夏夜之梦》）、历史剧（《亨利五世》）等多种类型，深刻描绘了人性的复杂。他的词汇量远超同时代作家，对英语语言产生了无与伦比的影响。",
  "Born in Stratford-upon-Avon, Shakespeare went to London and rose to acclaim as an actor and playwright. His works — spanning tragedies (Hamlet, King Lear, Macbeth), comedies (A Midsummer Night's Dream), and histories — explore the full complexity of human nature with unparalleled linguistic inventiveness.",
  [], [], "Q692", 0.95)

p("galileo", "伽利略", "Galileo Galilei", 1564, 1642, "renaissance-europe",
  ["科学", "天文学", "物理学"],
  ["Science", "Astronomy", "Physics"],
  "意大利科学家，近代实验科学的奠基人，改进了望远镜并发现木星卫星，因支持哥白尼日心说受审。",
  "Italian scientist and founder of modern experimental science, who improved the telescope, discovered Jupiter's moons, and was tried for supporting Copernican heliocentrism.",
  "伽利略在力学（如落体定律）、天文学和科学方法论上都有革命性贡献。1609年他改进望远镜，首次观测到月球环形山、木星的卫星和金星相位。1633年因在《关于两大世界体系的对话》中支持日心说而被宗教裁判所审判，被迫公开认错，传说低声说了'但它确实在动'。",
  "Galileo made revolutionary contributions to physics, astronomy, and scientific methodology. In 1609 he improved the telescope, observing lunar craters, Jupiter's moons, and the phases of Venus. Tried by the Inquisition in 1633 for advocating heliocentrism, he was forced to recant — allegedly whispering 'E pur si muove.'",
  [], [], "", 0.95)

p("louis-xiv", "路易十四", "Louis XIV", 1638, 1715, "europe",
  ["政治", "君主制", "法国", "巴洛克"],
  ["Politics", "Monarchy", "France", "Baroque"],
  "法国波旁王朝的太阳王，在位72年，建造凡尔赛宫，确立了绝对君主制的顶峰。",
  "The 'Sun King' of France's Bourbon dynasty, reigning 72 years, who built Versailles and established the apogee of absolute monarchy.",
  "路易十四5岁即位，23岁亲政后宣称'朕即国家'，建立了欧洲最强大的绝对君主制。他在凡尔赛建造了最奢华的宫殿，将法国贵族制于宫廷之下。在他的统治下，法国成为欧洲的文化和军事中心。然而长期的战争（如西班牙王位继承战争）耗竭了国库，为后来的法国大革命埋下伏笔。",
  "Louis XIV ascended the throne at age five and began his personal rule at twenty-three, declaring 'L'État, c'est moi.' He built Versailles as the ultimate symbol of absolutism and made France Europe's preeminent military and cultural power — though his endless wars depleted the treasury and sowed seeds for revolution.",
  [], [], "", 0.95)

# ===== MODERN (18-20th century) =====
p("voltaire", "伏尔泰", "Voltaire", 1694, 1778, "europe",
  ["哲学", "文学", "启蒙运动"],
  ["Philosophy", "Literature", "Enlightenment"],
  "法国启蒙思想家，以机智和犀利的笔锋批判教会和国家专制，倡导思想自由和宗教宽容。",
  "French Enlightenment thinker whose wit and sharp pen challenged ecclesiastical and state authority, championing freedom of thought and religious tolerance.",
  "伏尔泰本名弗朗索瓦-马利·阿鲁埃，是启蒙运动最著名的人物之一。他以辛辣的文笔撰写了大量哲学、历史和文学作品，包括《老实人》《哲学通信》和《路易十四时代》。他猛烈批判天主教会（'砸烂丑恶'），为宗教宽容大声疾呼，其思想深刻影响了法国大革命和美国独立。",
  "Born François-Marie Arouet, Voltaire was the Enlightenment's most celebrated figure. His vast output — including 'Candide,' 'Philosophical Letters,' and 'The Age of Louis XIV' — attacked the Catholic Church and championed religious tolerance. His ideas profoundly influenced the French and American Revolutions.",
  [], [], "O9068", 0.95)

p("marie-curie", "居里夫人", "Marie Curie", 1867, 1934, "europe",
  ["科学", "物理学", "化学", "女性", "诺贝尔"],
  ["Science", "Physics", "Chemistry", "Women", "Nobel"],
  "波兰裔法国科学家，放射性研究的先驱，历史上唯一两次获得不同科学领域诺贝尔奖的人。",
  "Polish-French scientist and pioneer of radioactivity research, the only person to win Nobel Prizes in two different scientific fields.",
  "玛丽·居里和丈夫皮埃尔·居里发现了镭和钋两种放射性元素，开创了放射性研究的新领域。她于1903年和1911年分别获得诺贝尔物理学奖和化学奖。第一次世界大战期间她发展了移动式X射线设备（'小居里'）协助战地外科手术。她因长期接触放射性物质导致再生障碍性贫血而去世。",
  "Marie Curie, with her husband Pierre, discovered radium and polonium, pioneering the field of radioactivity research. She won the Nobel Prize in Physics (1903) and Chemistry (1911). During WWI, she developed mobile X-ray units ('petites Curies') for battlefield surgery. She died of aplastic anemia from prolonged radiation exposure.",
  [], [], "Q7186", 0.95)

p("fdr", "富兰克林·罗斯福", "Franklin D. Roosevelt", 1882, 1945, "europe",
  ["政治", "美国", "二战", "新政"],
  ["Politics", "United States", "WWII", "New Deal"],
  "美国第32任总统，推行新政应对大萧条，领导美国度过二战，唯一连任四届的总统。",
  "32nd US President who introduced the New Deal to combat the Great Depression and led the nation through WWII, the only president to serve four terms.",
  "罗斯福在大萧条最严重的1933年就任总统，推行'新政'——通过大规模公共工程、金融改革和社会保障制度重建经济。1941年珍珠港事件后他领导美国加入二战，与丘吉尔和斯大林共同制定了盟军的战略。他倡导的'四大自由'和联合国的成立深刻影响了战后世界秩序。",
  "Taking office at the depths of the Great Depression, Roosevelt's New Deal rebuilt the economy through public works and Social Security. After Pearl Harbor, he led America in WWII alongside Churchill and Stalin. His 'Four Freedoms' speech and advocacy for the United Nations shaped the postwar world order.",
  [], [], "Q8007", 0.95)

p("mandela", "曼德拉", "Nelson Mandela", 1918, 2013, "africa",
  ["政治", "反种族隔离", "人权", "诺贝尔"],
  ["Politics", "Anti-Apartheid", "Human Rights", "Nobel"],
  "南非反种族隔离革命家，被囚禁27年后成为南非首位黑人总统，和解与宽容的全球象征。",
  "South African anti-apartheid revolutionary who became the country's first Black president after 27 years in prison, a global symbol of reconciliation and forgiveness.",
  "曼德拉早年投身反种族隔离斗争，1962年被判终身监禁。在罗本岛监狱的27年中，他成为全球反种族隔离运动的象征。1990年获释后，他选择以和解而非复仇的方式领导南非向民主过渡，1994年当选为南非首位黑人总统。1993年与德克勒克共获诺贝尔和平奖。",
  "Mandela was sentenced to life imprisonment in 1962 for his anti-apartheid activism. Through 27 years in Robben Island prison, he became the global symbol of the anti-apartheid movement. After his release in 1990, he chose reconciliation over revenge, guiding South Africa's transition to democracy and becoming its first Black president in 1994.",
  [], [], "Q8023", 0.95)

# ===== ASIAN FIGURES =====
p("akbar-great", "阿克巴大帝", "Akbar the Great", 1542, 1605, "india",
  ["政治", "莫卧儿", "宗教宽容"],
  ["Politics", "Mughal", "Religious Tolerance"],
  "莫卧儿帝国第三位也是最有作为的皇帝，推行宗教宽容，建立了帝国的高效行政体系。",
  "The third and most accomplished Mughal Emperor, who promoted religious tolerance and built an efficient imperial administration.",
  "阿克巴13岁即位，逐步将莫卧儿帝国从德里周边扩张到几乎整个印度次大陆。他废除了对非穆斯林征收的人头税（吉兹亚），邀请印度教、伊斯兰教、基督教和耆那教等各教代表进行宗教对话。他建立了一套高效的曼萨布达尔（官僚等级）体系，使帝国在政治、经济和文化上都达到了鼎盛。",
  "Akbar ascended at age 13 and expanded the Mughal Empire across almost the entire subcontinent. He abolished the jizya tax on non-Muslims and hosted interfaith dialogues. His mansabdari bureaucratic system brought the empire to its political, economic, and cultural zenith.",
  [], [], "", 0.9)

p("meiji", "明治天皇", "Emperor Meiji", 1852, 1912, "japan",
  ["政治", "改革", "现代化", "日本"],
  ["Politics", "Reform", "Modernization", "Japan"],
  "日本第122代天皇，领导明治维新，日本在三十年内从一个封建国家转变为近代工业强国。",
  "The 122nd Emperor of Japan who presided over the Meiji Restoration, transforming Japan from a feudal state into a modern industrial power within thirty years.",
  "1868年明治天皇即位后，日本在'富国强兵'的口号下推行全面西化改革。废藩置县建立了中央集权政府，颁布宪法（1889）建立君主立宪制，引进现代产业技术建立工厂和铁路网，建立义务教育和帝国大学。到20世纪初，日本已成为亚洲唯一的工业化强国。",
  "After Emperor Meiji's accession in 1868, Japan launched comprehensive modernization under the slogan 'enrich the country, strengthen the military.' The Meiji Restoration abolished feudal domains, established a constitutional monarchy (1889), built modern industry, and introduced compulsory education, making Japan Asia's sole industrial power by 1900.",
  [], [], "", 0.95)

p("tokugawa-ieyasu", "德川家康", "Tokugawa Ieyasu", 1543, 1616, "japan",
  ["政治", "军事", "幕府", "日本"],
  ["Politics", "Military", "Shogunate", "Japan"],
  "德川幕府（江户幕府）的创建者，终结了战国时代，建立了长达260余年的和平统一政权。",
  "Founder of the Tokugawa (Edo) Shogunate, who ended the Warring States period and established over 260 years of unified peace.",
  "德川家康在战国乱世中展现了非凡的耐心和政治智慧。1600年他在关原之战中击败所有反对势力，1603年被任命为征夷大将军，在江户（今东京）建立幕府。他制定了一套精密的制度（参勤交代、锁国令），确保了长期的内部稳定，但也在一定程度上导致了日本的长期孤立。",
  "Tokugawa Ieyasu demonstrated extraordinary patience and political acumen through decades of civil war. After defeating all rivals at the Battle of Sekigahara in 1600, he was appointed Shogun in 1603 and established his capital at Edo (Tokyo). His policies ensured two and a half centuries of peace, though also isolation.",
  [], [], "", 0.9)

p("lincoln", "亚伯拉罕·林肯", "Abraham Lincoln", 1809, 1865, "europe",
  ["政治", "美国", "奴隶制", "内战"],
  ["Politics", "United States", "Slavery", "Civil War"],
  "美国第16任总统，领导北方赢得南北战争，颁布《解放奴隶宣言》，拯救联邦并废除奴隶制。",
  "16th US President who led the Union to victory in the Civil War, issued the Emancipation Proclamation, saved the Union, and abolished slavery.",
  "林肯出身肯塔基州贫困家庭，自学成为律师。1861年就任总统后，南方蓄奴州脱离联邦，南北战争爆发。1863年他发布《解放奴隶宣言》，将废除奴隶制纳入战争目标。1865年4月战争结束之际在福特剧院被暗杀。其葛底斯堡演说'民有、民治、民享'成为民主政治的经典定义。",
  "Born in a Kentucky log cabin and self-educated, Lincoln became president as Southern states seceded. His 1863 Emancipation Proclamation made abolition a war aim. Assassinated at Ford's Theatre in April 1865 just as the war ended, his Gettysburg Address defined democracy as 'government of the people, by the people, for the people.'",
  [], [], "Q91", 0.95)

p("bolivar", "西蒙·玻利瓦尔", "Simón Bolívar", 1783, 1830, "americas",
  ["政治", "独立", "革命", "南美"],
  ["Politics", "Independence", "Revolution", "South America"],
  "南美独立运动的领袖，领导委内瑞拉、哥伦比亚、秘鲁、玻利维亚等国脱离西班牙统治。",
  "Leader of South American independence movements who freed Venezuela, Colombia, Peru, Bolivia, and others from Spanish rule.",
  "玻利瓦尔出生于委内瑞拉贵族家庭，受启蒙思想影响投身独立运动。经过十余年艰苦征战（横穿安第斯山脉的壮举尤为传奇），他领导解放了从加勒比海到安第斯山脉的广大地区，被称为'解放者'。他梦想建立拉丁美洲联邦（大哥伦比亚共和国），但因内部冲突最终破灭。",
  "Born to a wealthy Venezuelan family, Bolívar was inspired by Enlightenment ideals to join the independence movement. After over a decade of grueling campaigns — famously crossing the Andes — he liberated territories from the Caribbean to the high Andes, earning the title 'El Libertador.' His dream of a united Latin America ultimately collapsed amid regional conflicts.",
  [], [], "Q8605", 0.9)

p("sitting-bull", "坐牛", "Sitting Bull", 1831, 1890, "americas",
  ["政治", "军事", "印第安", "抵抗"],
  ["Politics", "Military", "Native American", "Resistance"],
  "拉科塔苏族的精神领袖和军事首领，领导了抵抗美国西进运动的小大角战役。",
  "Lakota Sioux spiritual leader and war chief who led resistance against US westward expansion at the Battle of Little Bighorn.",
  "坐牛（塔坦卡·约塔克）是洪克帕帕拉科塔部落的圣人，以无畏和智慧著称。1876年他与疯马联手在小大角战役中歼灭了卡斯特将军的第七骑兵团——这是印第安人对抗美军的最大胜利。此后他逃亡加拿大数年，最终投降。1890年在逮捕过程中被印第安警察射杀。",
  "Sitting Bull was a holy man of the Hunkpapa Lakota, renowned for bravery and wisdom. In 1876, together with Crazy Horse, he annihilated General Custer's 7th Cavalry at Little Bighorn — the greatest Native American victory over US forces. He surrendered after years in exile and was killed during an arrest attempt in 1890.",
  [], [], "", 0.85)

p("ataturk", "凯末尔·阿塔图尔克", "Mustafa Kemal Atatürk", 1881, 1938, "middle-east",
  ["政治", "改革", "土耳其", "世俗化"],
  ["Politics", "Reform", "Turkey", "Secularization"],
  "土耳其共和国的缔造者和首任总统，推行激进的世俗化、现代化改革，被誉为'土耳其之父'。",
  "Founder and first president of the Republic of Turkey, who implemented radical secularizing and modernizing reforms, revered as 'Father of the Turks.'",
  "凯末尔在第一次世界大战后领导土耳其民族独立战争，废除了《色佛尔条约》，于1923年建立土耳其共和国。他推行了包括废除哈里发制度、采用拉丁字母、关闭宗教法庭、给予妇女选举权等一系列激进改革，将奥斯曼帝国的残余改造为一个世俗的现代民族国家。",
  "After WWI, Kemal led the Turkish War of Independence, repudiated the Treaty of Sèvres, and founded the Republic of Turkey in 1923. His radical reforms — abolishing the caliphate, adopting the Latin alphabet, closing religious courts, granting women's suffrage — transformed the Ottoman remnant into a secular modern nation-state.",
  [], [], "Q5152", 0.95)

# ===== AFRICAN FIGURES =====
p("mansas-musa", "曼萨·穆萨", "Mansa Musa", 1280, 1337, "africa",
  ["政治", "经济", "马里帝国", "伊斯兰"],
  ["Politics", "Economy", "Mali Empire", "Islam"],
  "马里帝国的皇帝，历史上最富有的人之一，其前往麦加的朝圣之旅震惊了中世纪的伊斯兰和欧洲世界。",
  "Emperor of the Mali Empire and one of the wealthiest individuals in history, whose pilgrimage to Mecca astounded the medieval Islamic and European world.",
  "曼萨·穆萨统治着西非最大的帝国马里帝国（以廷巴克图为首都）。1324年他前往麦加朝圣，随行队伍包括数万士兵、奴隶和骆驼，携带的黄金之多在到达埃及开罗时导致当地金价暴跌十余年。他归国后大力建设清真寺和学府（如桑科雷大学），使廷巴克图成为了伊斯兰学术中心。",
  "Mansa Musa ruled the Mali Empire, West Africa's largest state. His 1324 pilgrimage to Mecca with tens of thousands of attendants and so much gold that it caused a decade-long price crash in Cairo is legendary. He returned to build mosques and the University of Sankore, making Timbuktu a center of Islamic scholarship.",
  [], [], "", 0.8)

p("hatshepsut", "哈特谢普苏特", "Hatshepsut", -1507, -1458, "africa",
  ["政治", "埃及", "女性", "建筑"],
  ["Politics", "Egypt", "Women", "Architecture"],
  "古埃及第十八王朝女法老，以男性形象统治埃及二十余年，建造了壮丽的代尔-巴哈里神庙。",
  "Female pharaoh of Egypt's 18th Dynasty who ruled for over twenty years, often depicted in masculine regalia, and built the magnificent temple at Deir el-Bahari.",
  "哈特谢普苏特是图特摩斯一世的女儿，嫁给了同父异母的兄弟图特摩斯二世。丈夫去世后她作为年幼的图特摩斯三世的摄政，随后以法老身份亲政。她大量建造神庙和纪念碑，派遣远征队到蓬特（今索马里一带）进行贸易。死后她的雕像和名字被图特摩斯三世试图从历史上抹去。",
  "Hatshepsut, daughter of Thutmose I, became regent for her stepson Thutmose III after her husband's death, then assumed the full powers of pharaoh. She built extensively and dispatched trading expeditions to Punt (modern Somalia). After her death, Thutmose III attempted to erase her from history by defacing her monuments.",
  [], [], "", 0.8)

p("nefertiti", "纳芙蒂蒂", "Nefertiti", -1370, -1330, "africa",
  ["政治", "宗教", "埃及", "艺术"],
  ["Politics", "Religion", "Egypt", "Art"],
  "古埃及王后，与丈夫阿肯那顿推行宗教改革，其半身雕像成为古埃及艺术中最著名的形象。",
  "Egyptian queen who, with her husband Akhenaten, led a religious revolution; her bust is among the most iconic images of ancient art.",
  "纳芙蒂蒂是法老阿肯那顿的'伟大的王后'，与丈夫一起将埃及从多神教转变为崇拜唯一的太阳神阿吞。她在政治和宗教事务中扮演了前所未有的积极角色，其著名的石灰岩半身雕像（现藏于柏林新博物馆）以其完美的对称和优雅成为古埃及艺术的象征。",
  "Nefertiti, 'Great Royal Wife' of Pharaoh Akhenaten, co-led Egypt's revolutionary shift from polytheism to worship of the sun disk Aten. She played an unprecedentedly active role in political and religious affairs. Her limestone bust (Neues Museum, Berlin) remains the iconic image of ancient Egyptian artistry.",
  [], [], "", 0.75)

# ===== MORE FIGURES (batch 2) =====

p("socrates", "苏格拉底", "Socrates", -470, -399, "europe",
  ["哲学", "伦理", "古希腊"],
  ["Philosophy", "Ethics", "Ancient Greece"],
  "古希腊哲学家，西方哲学奠基人之一，以苏格拉底式对话法和为真理献身闻名。",
  "Ancient Greek philosopher and founding figure of Western philosophy, known for the Socratic method and his martyrdom for truth.",
  "苏格拉底没有留下任何著作，其思想主要通过弟子柏拉图和色诺芬的记载流传。他以在雅典广场上通过提问引导人们反思的'苏格拉底式对话'闻名。公元前399年被指控'腐蚀青年'和'不敬神'，拒绝逃跑，饮毒堇汁而死。'未经审视的人生不值得活'是他的名言。",
  "Socrates left no writings; his thought survives through Plato and Xenophon. Famous for his 'Socratic method' of questioning in the Athenian agora, he was tried and executed in 399 BCE for 'corrupting youth' and 'impiety.' His defiant death made him philosophy's first martyr.",
  [], [], "Q913", 0.85)

p("plato", "柏拉图", "Plato", -428, -348, "europe",
  ["哲学", "政治", "教育", "古希腊"],
  ["Philosophy", "Politics", "Education", "Ancient Greece"],
  "苏格拉底的学生，亚里士多德的老师，创办雅典学院，著作《理想国》影响西方思想两千余年。",
  "Pupil of Socrates and teacher of Aristotle who founded the Academy in Athens; his 'Republic' has shaped Western thought for over two millennia.",
  "柏拉图出身雅典贵族，苏格拉底被处死后遍游地中海各地学习，后回雅典创办'学院'（西方第一所高等学府）。其著作以对话体写成，探讨了正义（《理想国》）、知识论（洞穴比喻）、爱情（《会饮篇》）和灵魂不朽等主题。怀特海说：'欧洲哲学传统不过是对柏拉图的一系列脚注。'",
  "Born to Athenian aristocracy, Plato traveled widely after Socrates' death before founding the Academy — the West's first institution of higher learning. His dialogues explore justice (the 'Republic'), epistemology (the cave allegory), love (the 'Symposium'), and immortality. Whitehead noted: 'All of Western philosophy is footnotes to Plato.'",
  [], [], "O859", 0.9)

p("aristotle", "亚里士多德", "Aristotle", -384, -322, "europe",
  ["哲学", "科学", "逻辑", "古希腊"],
  ["Philosophy", "Science", "Logic", "Ancient Greece"],
  "古希腊百科全书式的学者，逻辑学、生物学、政治学和伦理学的奠基人，亚历山大大帝的老师。",
  "Encyclopedic ancient Greek scholar who founded logic, biology, politics, and ethics; tutor of Alexander the Great.",
  "亚里士多德是柏拉图最杰出的学生，但他的思想走了不同的方向——从抽象理念转向经验观察。他在逻辑学（三段论）、生物学（动物分类）、政治学（《政治学》）、伦理学（《尼各马可伦理学》）和形而上学等众多领域都做出了奠基性贡献。其著作构成了中世纪经院哲学的基础。",
  "Aristotle, Plato's greatest student, departed from his teacher's abstract idealism toward empirical observation. He made foundational contributions to logic (syllogism), biology, politics, ethics, and metaphysics. His works formed the basis of medieval scholasticism, and his scientific framework dominated Western thought for nearly two millennia.",
  [], [], "Q868", 0.9)

p("archimedes", "阿基米德", "Archimedes", -287, -212, "europe",
  ["科学", "数学", "工程"],
  ["Science", "Mathematics", "Engineering"],
  "古希腊最伟大的数学家和工程师，发现浮力原理（'尤里卡！'），发明杠杆定律和多种战争机械。",
  "Ancient Greece's greatest mathematician and engineer who discovered the buoyancy principle ('Eureka!'), formulated the law of the lever, and invented war machines.",
  "阿基米德出生于西西里岛的叙拉古，在亚历山大城求学后回到故乡。他的科学成就令人惊叹：计算圆周率的近似值、发现浮力原理、证明杠杆定律（'给我一个支点，我能撬动地球'）。在罗马围攻叙拉古时，他设计了投石机、抓船器等机械，最终在城破时被一名不识识的罗马士兵杀死。",
  "Born in Syracuse, Sicily, Archimedes studied in Alexandria before returning home. His achievements are staggering: approximating pi, discovering buoyancy ('Eureka!'), and the law of the lever. During the Roman siege of Syracuse, he designed catapults and ship-grabbing cranes. He was killed by a Roman soldier who didn't recognize him.",
  [], [], "O8739", 0.85)

p("marcus-aurelius", "马可·奥勒留", "Marcus Aurelius", 121, 180, "roman-empire",
  ["哲学", "政治", "斯多亚"],
  ["Philosophy", "Politics", "Stoicism"],
  "罗马帝国'五贤帝'中的最后一位，斯多亚派哲学家皇帝，著有《沉思录》。",
  "The last of Rome's 'Five Good Emperors' and a Stoic philosopher-emperor, author of the 'Meditations.'",
  "马可·奥勒留（161-180年在位）在帝国面临瘟疫、战争和经济困难的多事之秋登基。他在行军帐篷中用希腊文写下的私人笔记——《沉思录》——记录了斯多亚派的核心思想：接受命运、履行责任、保持内心的宁静。他是一位罕见的'哲学家王'，将哲学智慧运用于实际统治。",
  "Marcus Aurelius (r. 161-180 CE) ascended during a period of plague, war, and economic strain. His private notes written in Greek on campaign — the 'Meditations' — record Stoic core principles: accept fate, fulfill duty, maintain inner tranquility. He was that rare 'philosopher-king' who applied wisdom to governance.",
  [], [], "Q1430", 0.9)

p("constantine", "君士坦丁大帝", "Constantine the Great", 272, 337, "roman-empire",
  ["政治", "宗教", "基督教", "罗马"],
  ["Politics", "Religion", "Christianity", "Rome"],
  "罗马帝国第一位皈依基督教的皇帝，颁布米兰敕令使基督教合法化，建立君士坦丁堡作为新都。",
  "The first Roman emperor to convert to Christianity, issued the Edict of Milan legalizing Christianity, and founded Constantinople as the new capital.",
  "君士坦丁大帝于312年米尔维安大桥战役前夕声称看到十字架异象，获胜后皈依基督教。313年他与李锡尼共同颁布《米兰敕令》，结束了三世纪以来对基督徒的迫害。330年他将帝国都城从罗马迁往拜占庭，改名为君士坦丁堡。这些决策深刻改变了欧洲和基督教的历史走向。",
  "Before the Battle of Milvian Bridge in 312 CE, Constantine claimed to see a vision of the cross and converted after victory. The Edict of Milan (313) with Licinius ended persecution of Christians. In 330 he moved the capital from Rome to Byzantium, renaming it Constantinople — decisions that reshaped both Europe and Christianity.",
  [], [], "Q8413", 0.9)

p("sun-tzu", "孙子（孙武）", "Sun Tzu", -544, -496, "china",
  ["军事", "哲学", "战略"],
  ["Military", "Philosophy", "Strategy"],
  "春秋时期军事家，《孙子兵法》的作者，被誉为兵学圣典，影响后世两千余年。",
  "Spring and Autumn period military strategist and author of 'The Art of War,' revered as the supreme classic of military science.",
  "孙武（孙子）为吴王阖闾训练军队，以严明的军纪和卓越的谋略闻名。《孙子兵法》十三篇系统论述了战争的本质——'兵者，诡道也'——强调'不战而屈人之兵'的至善境界和'知彼知己，百战不殆'的认识论原则。此书不仅是军事经典，其策略思想更被广泛应用于商业和管理领域。",
  "Sun Tzu trained the army of King Helü of Wu, renowned for his strict discipline and strategic genius. The 'Art of War' — thirteen chapters — analyzes the nature of conflict ('warfare is the way of deception'), prizing victory without battle and emphasizing knowledge of self and enemy. Its teachings extend beyond war to business and management.",
  [], [], "Q37151", 0.75)

p("mencius", "孟子", "Mencius", -372, -289, "china",
  ["哲学", "政治", "儒学"],
  ["Philosophy", "Politics", "Confucianism"],
  "战国儒家代表人物，继承并发展了孔子的思想，提出'性善论'和'民贵君轻'的政治理念。",
  "Warring States Confucian who developed Confucius' thought, proposing the 'innate goodness of human nature' and the doctrine that 'the people are the most important element.'",
  "孟子（孟轲）被认为是孔子的私淑弟子，其著作《孟子》七篇是儒家'四书'之一。他提出'人性本善'的命题（以'恻隐之心，人皆有之'论证），主张'仁政'和'王道'政治，坚决反对霸道和战争。'民为贵，社稷次之，君为轻'的政治思想具有超越时代的意义。",
  "Mencius is considered Confucius' spiritual successor. His seven-chapter work (one of the 'Four Books') argues that human nature is innately good — all possess 'a heart that cannot bear to see others suffer.' He advocated 'benevolent government,' declaring 'the people are most important, the state next, the ruler least' — remarkably ahead of its time.",
  [], [], "Q188977", 0.85)

p("han-fei", "韩非", "Han Feizi", -280, -233, "china",
  ["哲学", "政治", "法家"],
  ["Philosophy", "Politics", "Legalism"],
  "战国末期法家集大成者，综合商鞅的'法'、申不害的'术'和慎到的'势'，为秦统一提供了理论基础。",
  "The synthesizer of Legalist thought who combined Shang Yang's 'law,' Shen Buhai's 'method,' and Shen Dao's 'authority,' laying the theoretical foundation for Qin unification.",
  "韩非出身韩国贵族，师从荀子，但走向了与儒家截然不同的方向。他主张人性本恶，必须通过严刑峻法来治理。其著作《韩非子》系统阐述了以法治国、君主驾驭臣下的权术和国家实力至上的理念。秦王嬴政读其文章后感叹：'寡人得见此人与之游，死不恨矣！'但因李斯嫉妒而被陷害致死。",
  "Born to Korean nobility, Han Feizi studied under Xunzi but took Legalism in a different direction, arguing human nature is inherently selfish and must be governed through strict laws and punishments. His writings so impressed King Zheng of Qin that he exclaimed: 'If I could meet this man and walk with him, I would die without regret!' He was framed by jealous Li Si and died in prison.",
  [], [], "Q28987", 0.85)

p("virgil", "维吉尔", "Virgil", -70, -19, "roman-empire",
  ["文学", "史诗", "罗马"],
  ["Literature", "Epic", "Rome"],
  "古罗马最伟大的诗人，创作了罗马民族史诗《埃涅阿斯纪》，但丁《神曲》中的引路人。",
  "Ancient Rome's greatest poet who composed the national epic 'Aeneid' — and serves as Dante's guide through Hell and Purgatory.",
  "维吉尔创作了三部不朽作品：《牧歌》（田园诗）、《农事诗》（农事教诲诗）和《埃涅阿斯纪》（民族史诗）。《埃涅阿斯纪》讲述特洛伊英雄埃涅阿斯在特洛伊陷落后流亡意大利的旅程，追溯罗马的起源到神话时代，为奥古斯都的统治提供了神圣的合法性。在《神曲》中他作为理性的化身引导但丁。",
  "Virgil created three monumental works: the 'Eclogues' (pastoral), 'Georgics' (agricultural poetry), and the 'Aeneid' (national epic). The Aeneid traces Aeneas' journey from fallen Troy to Italy, linking Rome's origins to the mythical past and providing divine legitimacy for Augustus' rule. In Dante's 'Divine Comedy,' Virgil guides the pilgrim as the embodiment of reason.",
  [], [], "Q1398", 0.9)

# ===== MORE FIGURES (batch 3) =====

p("copernicus", "哥白尼", "Nicolaus Copernicus", 1473, 1543, "renaissance-europe",
  ["科学", "天文学", "科学革命"],
  ["Science", "Astronomy", "Scientific Revolution"],
  "波兰天文学家，提出日心说（太阳而非地球是宇宙中心），引发了近代科学革命。",
  "Polish astronomer who proposed the heliocentric theory — that the Sun, not Earth, is the center of the universe — launching the Scientific Revolution.",
  "哥白尼在弗龙堡任教士期间，花了近三十年完成《天体运行论》。他打破了一千五百年来托勒密地心说的统治，论证太阳位于宇宙的中心，地球是一颗围绕太阳运转的行星。这部著作于1543年他临终前出版，虽然当时未引起巨大反响，但为伽利略、开普勒和牛顿的工作奠定基础，被公认为近代科学革命的起点。",
  "During three decades as a canon in Frombork, Copernicus completed 'On the Revolutions of the Heavenly Spheres,' challenging Ptolemy's 1,500-year-old geocentric model. Published on his deathbed in 1543, the work established heliocentrism and laid the foundation for Galileo, Kepler, and Newton — the acknowledged starting point of the Scientific Revolution.",
  [], [], "Q619", 0.9)

p("kepler", "开普勒", "Johannes Kepler", 1571, 1630, "renaissance-europe",
  ["科学", "天文学", "数学"],
  ["Science", "Astronomy", "Mathematics"],
  "德国天文学家和数学家，发现行星运动三大定律，为牛顿万有引力定律奠定了基础。",
  "German astronomer and mathematician who discovered the three laws of planetary motion, paving the way for Newton's law of universal gravitation.",
  "开普勒师从第谷·布拉赫，继承了老师数十年精密的天文观测数据。经过艰苦的数学推算，他发现了行星运动三大定律：（1）行星轨道是椭圆而非圆形；（2）行星与太阳的连线在相等时间内扫过相等面积；（3）行星公转周期的平方与轨道半长轴的立方成正比。这些发现彻底推翻了自希腊以来的圆轨道完美论。",
  "Inheriting Tycho Brahe's decades of precise observations, Kepler mathematically derived his three laws: (1) planetary orbits are elliptical, not circular; (2) a line joining a planet to the Sun sweeps equal areas in equal times; (3) the square of a planet's orbital period is proportional to the cube of its semi-major axis. These shattered millennia of circular-orbit dogma.",
  [], [], "Q8964", 0.9)

p("magellan", "麦哲伦", "Ferdinand Magellan", 1480, 1521, "renaissance-europe",
  ["探索", "航海", "环球航行"],
  ["Exploration", "Navigation", "Circumnavigation"],
  "葡萄牙航海家，领导了人类首次环球航行，虽然本人在菲律宾被杀，但其船队证明了地圆说。",
  "Portuguese navigator who led the first circumnavigation of the globe; though killed in the Philippines, his expedition proved the Earth was round.",
  "1519年9月，麦哲伦率五艘帆船从西班牙出发，横渡大西洋，发现了麦哲伦海峡（南美洲南端），进入了他命名为'太平洋'的辽阔海域。1521年他在菲律宾因介入部落冲突被杀。剩下的船员在埃尔卡诺的率领下于1522年返回西班牙——完成了人类首次环球航行，无可辩驳地证明了地球是圆的。",
  "In September 1519, Magellan sailed from Spain with five ships, crossed the Atlantic, discovered the strait at South America's tip (the Strait of Magellan), and entered the vast ocean he named 'Pacific.' Killed in the Philippines during a tribal conflict in 1521, his surviving crew under Elcano returned to Spain in 1522 — completing the first circumnavigation.",
  [], [], "Q1496", 0.9)

p("machiavelli", "马基雅维利", "Niccolò Machiavelli", 1469, 1527, "renaissance-europe",
  ["哲学", "政治", "文艺复兴"],
  ["Philosophy", "Politics", "Renaissance"],
  "意大利政治思想家，《君主论》的作者，以现实主义政治哲学闻名，被视为近代政治学之父。",
  "Italian political thinker and author of 'The Prince,' known for his realist political philosophy and regarded as the father of modern political science.",
  "马基雅维利曾担任佛罗伦萨共和国的外交官和秘书。1513年美第奇家族复辟后他被免职并遭酷刑。隐居期间他写下了《君主论》——一部关于获取和维持政治权力的冷酷分析。他主张政治应从道德和宗教中分离出来，以效果而非意图来评判。'马基雅维利主义'后来成为为达目的不择手段的同义词。",
  "Machiavelli served as a diplomat and secretary in the Florentine Republic until the Medici restoration (1513) stripped him of office and subjected him to torture. In exile, he wrote 'The Prince' — a coldly analytical treatise on acquiring and maintaining political power separate from moral or religious considerations, judged by results rather than intentions.",
  [], [], "Q1399", 0.9)

p("pasteur", "巴斯德", "Louis Pasteur", 1822, 1895, "europe",
  ["科学", "微生物", "医学", "疫苗"],
  ["Science", "Microbiology", "Medicine", "Vaccine"],
  "法国微生物学家，创立了微生物学，发明巴氏消毒法和狂犬病疫苗，彻底改变了医学。",
  "French microbiologist who founded the germ theory, invented pasteurization and the rabies vaccine, and revolutionized medicine.",
  "巴斯德通过实验彻底否定了'自然发生说'，证明微生物是导致发酵和疾病的元凶。他发明了巴氏消毒法（用于保存牛奶和酒），研发了鸡霍乱、炭疽和狂犬病疫苗，开创了免疫学。1885年他成功救治了被疯狗咬伤的9岁男孩约瑟夫·迈斯特尔——这是人类疫苗史上的里程碑。巴黎巴斯德研究所至今仍是全球医学研究中心。",
  "Pasteur disproved 'spontaneous generation' through rigorous experiments, demonstrating that microorganisms cause fermentation and disease. He developed pasteurization, vaccines for chicken cholera, anthrax, and rabies (saving 9-year-old Joseph Meister in 1885 — a milestone in vaccinology), and founded immunology. The Pasteur Institute remains a global biomedical research center.",
  [], [], "Q529", 0.95)

p("tesla", "特斯拉", "Nikola Tesla", 1856, 1943, "europe",
  ["科学", "电气", "发明", "交流电"],
  ["Science", "Electrical", "Invention", "AC Power"],
  "塞尔维亚裔美籍发明家，交流电系统的主要设计者，一生获得三百多项专利的天才工程师。",
  "Serbian-American inventor, chief architect of the alternating current (AC) system, and a genius engineer with over 300 patents.",
  "特斯拉开发了交流电发电、传输和应用的完整系统，在与爱迪生的'电流之战'中最终胜出——今天全世界的电网都采用交流电。他的其他发明包括特斯拉线圈、无线电的早期实验和无线输电的构想。尽管晚年贫困潦倒，他的远见和创造力使他成为科学文化的标志性人物。",
  "Tesla developed the complete alternating current system for generation, transmission, and application, winning the 'War of Currents' against Edison — today's global power grids run on AC. His other inventions include the Tesla coil and pioneering work on radio and wireless energy transmission. An impoverished end belied a visionary legacy.",
  [], [], "Q9036", 0.95)

p("marx", "卡尔·马克思", "Karl Marx", 1818, 1883, "europe",
  ["哲学", "经济学", "政治", "社会主义"],
  ["Philosophy", "Economics", "Politics", "Socialism"],
  "德国哲学家和经济学家，《共产党宣言》和《资本论》的作者，深刻影响了世界历史进程。",
  "German philosopher and economist who wrote 'The Communist Manifesto' and 'Das Kapital,' profoundly shaping the course of world history.",
  "马克思吸收了德国古典哲学（黑格尔）、英国政治经济学（亚当·斯密）和法国空想社会主义的思想，创立了历史唯物主义和剩余价值学说。《共产党宣言》（1848年与恩格斯合著）呼吁'全世界无产者联合起来'，《资本论》（1867年）系统分析了资本主义的运作规律和内在矛盾。他的思想直接和间接影响了20世纪全球三分之一的人口。",
  "Marx synthesized German classical philosophy (Hegel), British political economy (Smith), and French utopian socialism into historical materialism and the theory of surplus value. 'The Communist Manifesto' (1848, with Engels) called for workers' solidarity; 'Das Kapital' (1867) systematically analyzed capitalism's mechanisms and contradictions. His ideas directly or indirectly affect a third of 20th-century humanity.",
  [], [], "Q9061", 0.95)

p("tolstoy", "托尔斯泰", "Leo Tolstoy", 1828, 1910, "europe",
  ["文学", "小说", "哲学", "和平主义"],
  ["Literature", "Novel", "Philosophy", "Pacifism"],
  "俄罗斯文学巨匠，代表作《战争与和平》和《安娜·卡列尼娜》是世界文学的最高成就之一。",
  "Russian literary titan whose 'War and Peace' and 'Anna Karenina' are among the supreme achievements of world literature.",
  "托尔斯泰出身贵族，早年从军经历（克里米亚战争）为其写作提供了丰富素材。他的两部巨著——《战争与和平》（描写拿破仑战争期间的俄罗斯社会全景）和《安娜·卡列尼娜》——以无与伦比的深度刻画了人性的复杂和社会的全景。晚年他经历了精神危机，倡导非暴力抵抗（深刻影响甘地），放弃贵族生活方式。",
  "Born to nobility, Tolstoy's early military experiences informed his writing. His two masterpieces — 'War and Peace' (an epic panorama of Russian society during the Napoleonic wars) and 'Anna Karenina' — probe human complexity with unmatched psychological depth. In his later years, he experienced a spiritual crisis, advocated nonviolent resistance (profoundly influencing Gandhi), and renounced aristocratic privilege.",
  [], [], "Q7243", 0.95)

p("dostoevsky", "陀思妥耶夫斯基", "Fyodor Dostoevsky", 1821, 1881, "europe",
  ["文学", "哲学", "小说", "存在主义"],
  ["Literature", "Philosophy", "Novel", "Existentialism"],
  "俄罗斯小说家，以《罪与罚》和《卡拉马佐夫兄弟》等作品探索人性深渊，影响了存在主义和现代心理学。",
  "Russian novelist whose 'Crime and Punishment' and 'The Brothers Karamazov' plumb the depths of human nature, influencing existentialism and modern psychology.",
  "陀思妥耶夫斯基的一生极其戏剧性：因参与政治活动被判处死刑，在刑场上被特赦改判西伯利亚苦役。这段经历深刻改变了他的世界观。他的小说以人物的极端心理状态和存在的终极问题为核心——《罪与罚》探讨犯罪与救赎，《白痴》描摹纯真与堕落，《卡拉马佐夫兄弟》以信仰与怀疑的对抗为最终主题。尼采评价他为'唯一让我学到东西的心理学家'。",
  "Dostoevsky's life was intensely dramatic: sentenced to death for political activity, he was reprieved at the execution ground and sent to Siberia — an experience that transformed his worldview. His novels center on extreme psychological states and ultimate existential questions: crime and redemption ('Crime and Punishment'), innocence and corruption ('The Idiot'), faith and doubt ('The Brothers Karamazov'). Nietzsche called him 'the only psychologist from whom I have anything to learn.'",
  [], [], "Q991", 0.95)

p("mozart", "莫扎特", "Wolfgang Amadeus Mozart", 1756, 1791, "europe",
  ["音乐", "古典", "作曲"],
  ["Music", "Classical", "Composition"],
  "奥地利作曲家，古典时期最伟大的音乐天才之一，5岁开始作曲，35岁去世时留下600多部作品。",
  "Austrian composer and one of the greatest musical geniuses of the Classical period, composing from age five, leaving over 600 works at his death at 35.",
  "莫扎特是音乐史上罕见的神童：5岁作曲，6岁开始在父亲带领下在欧洲各国宫廷巡回演出。他的创作涵盖当时所有音乐体裁——交响曲（41部）、钢琴协奏曲（27部）、弦乐四重奏、歌剧（《费加罗的婚礼》《唐璜》《魔笛》）和安魂曲。他的音乐以完美的结构和丰沛的旋律著称，终其一生试图从萨尔茨堡大主教的束缚中解脱。",
  "Mozart was a prodigy without parallel: composing at five, touring Europe's courts from age six under his father's guidance. His output spans every contemporary genre — 41 symphonies, 27 piano concertos, string quartets, operas ('The Marriage of Figaro,' 'Don Giovanni,' 'The Magic Flute'), and a Requiem. His music combines perfection of form with inexhaustible melodic invention.",
  [], [], "Q254", 0.95)

p("beethoven", "贝多芬", "Ludwig van Beethoven", 1770, 1827, "europe",
  ["音乐", "古典", "浪漫", "作曲"],
  ["Music", "Classical", "Romantic", "Composition"],
  "德国作曲家，古典与浪漫主义音乐的桥梁，耳聋后仍创作了人类音乐史上最伟大的作品。",
  "German composer who bridged the Classical and Romantic eras, composing some of music's greatest works after going deaf.",
  "贝多芬在27岁左右开始失去听力，到46岁时完全聋了。但正是在耳聋期间——在寂静的世界里——他创作了划时代的作品：第九交响曲（合唱）以席勒的《欢乐颂》结尾，第三交响曲（英雄）打破了古典交响曲的形式，晚期弦乐四重奏达到了人类精神表达的极致。他以孤独的艺术家形象重新定义了作曲家的社会地位。",
  "Beethoven began losing his hearing around age 27 and was completely deaf by 46. Yet it was in silence that he created his most revolutionary works: the Ninth Symphony (choral, ending with Schiller's 'Ode to Joy'), the 'Eroica' Third Symphony, and late string quartets that reach the summit of human expression. He redefined the composer's role as the solitary artistic genius.",
  [], [], "Q255", 0.95)

p("peter-great", "彼得大帝", "Peter the Great", 1672, 1725, "europe",
  ["政治", "改革", "俄国", "现代化"],
  ["Politics", "Reform", "Russia", "Modernization"],
  "俄罗斯沙皇，以铁腕手段推行西化改革，建立圣彼得堡，将俄罗斯从内陆国家转变为欧洲强国。",
  "Russian Tsar who forcibly modernized Russia on Western lines, built St. Petersburg, and transformed Russia from a landlocked state into a European power.",
  "彼得一世以超乎想象的精力推行改革：他匿名游历西欧十八个月学习造船、军事和治理技术；回国后强制贵族剃须穿西服；建立了俄罗斯第一支海军；在大北方战争中击败瑞典，获得波罗的海出海口并建立新都圣彼得堡。他创建了参议院、官阶表和科学院，将俄罗斯从东方式的封闭王国推向了欧洲列强之列。",
  "Peter I's reformist energy was superhuman: he toured Western Europe incognito for 18 months studying shipbuilding and governance; upon return, forced nobles to shave and adopt Western dress; built Russia's first navy; defeated Sweden in the Great Northern War for Baltic access; founded St. Petersburg. He dragged Russia from Oriental isolation into the ranks of European powers.",
  [], [], "Q8479", 0.9)

p("vasco-da-gama", "达·伽马", "Vasco da Gama", 1460, 1524, "renaissance-europe",
  ["探索", "航海", "葡萄牙"],
  ["Exploration", "Navigation", "Portugal"],
  "葡萄牙航海家，第一个从欧洲直接航行到印度的人，开辟了绕过非洲好望角的东方航线。",
  "Portuguese navigator, the first European to sail directly from Europe to India, opening the Cape Route around Africa.",
  "1497年7月，达·伽马率四艘帆船从里斯本出发，绕过好望角（迪亚士十年前的发现），沿东非海岸北上，在阿拉伯领航员的帮助下穿越印度洋，于1498年5月到达印度卡利卡特。这条航线绕过了奥斯曼帝国控制的地中海贸易路线，使葡萄牙得以直接获得东方的香料和丝绸，开启了欧洲在亚洲的殖民时代。",
  "In July 1497, da Gama sailed from Lisbon, rounded the Cape of Good Hope (discovered by Dias ten years earlier), and with an Arab pilot's help crossed the Indian Ocean, reaching Calicut, India in May 1498. This route bypassed the Ottoman-controlled Mediterranean, giving Portugal direct access to eastern spices and silks — inaugurating Europe's colonial presence in Asia.",
  [], [], "Q7328", 0.9)

p("edison", "爱迪生", "Thomas Edison", 1847, 1931, "europe",
  ["发明", "科技", "电气"],
  ["Invention", "Technology", "Electrical"],
  "美国发明家，拥有超过一千项专利，发明留声机、改进电灯泡和电影摄影机，创办通用电气。",
  "American inventor with over one thousand patents who invented the phonograph, improved the electric light bulb, and founded General Electric.",
  "爱迪生在门洛帕克和新泽西建立了世界上第一个工业研究实验室。他的重要发明包括留声机（1877年）、实用的白炽灯泡、电影摄影机和碳粒电话送话器。他开发了整套发电和配电系统，但支持直流电（与特斯拉的交流电竞争并最终失败）。'天才是百分之一的灵感加上百分之九十九的汗水'是他的名言。",
  "Edison established the world's first industrial research laboratory at Menlo Park. His key inventions include the phonograph (1877), the practical incandescent light bulb, the motion picture camera, and the carbon telephone transmitter. He championed direct current (DC) against Tesla's AC — and lost. 'Genius is one percent inspiration and ninety-nine percent perspiration' is attributed to him.",
  [], [], "Q8743", 0.95)

# ===== OUTPUT =====
lines = []
for person in people:
    l = []
    l.append("  // --- %s ---" % person["nameEn"])
    l.append("  {")
    l.append("    id: '%s'," % esc(person["id"]))
    l.append("    name: '%s'," % esc(person["name"]))
    l.append("    nameEn: '%s'," % esc(person["nameEn"]))
    l.append("    birthYear: %s," % person["birthYear"])
    l.append("    deathYear: %s," % person["deathYear"])
    l.append("    regionId: '%s'," % person["regionId"])
    alt = ", ".join("'%s'" % esc(a) for a in person["alternativeNames"])
    l.append("    alternativeNames: [%s]," % alt)
    tags = ", ".join("'%s'" % esc(t) for t in person["tags"])
    l.append("    tags: [%s]," % tags)
    tagsEn = ", ".join("'%s'" % esc(t) for t in person["tagsEn"])
    l.append("    tagsEn: [%s]," % tagsEn)
    l.append("    summary: '%s'," % esc(person["summary"]))
    l.append("    summaryEn: '%s'," % esc(person["summaryEn"]))
    l.append("    description: '%s'," % esc(person["description"]))
    l.append("    descriptionEn: '%s'," % esc(person["descriptionEn"]))
    src = ", ".join("'%s'" % s for s in person["sourceIds"])
    l.append("    occupations: [],")
    l.append("    sourceIds: [%s]," % src)
    l.append("    birthDatePrecision: 'year' as const,")
    l.append("    deathDatePrecision: 'year' as const,")
    l.append("    dataStatus: '%s' as const," % person["dataStatus"])
    l.append("    confidenceScore: %s," % person["confidenceScore"])
    l.append("    externalReferences: [],")
    if person["wikidataQid"]:
        l.append("    wikidataQid: '%s'," % person["wikidataQid"])
    l.append("  },")
    lines.append("\n".join(l))

print("\n\n".join(lines))
print("\n// Total: %d new people" % len(people))
