#!/usr/bin/env python3
"""Batch 7: ~240 more people — shorter descriptions, efficient generation, filling all gaps"""
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

# Section 1: More 20th century figures from all continents (40)
twentieth = [
    ("einstein", "阿尔伯特·爱因斯坦", "Albert Einstein", 1879, 1955, "europe", ["科学", "物理", "相对论"], ["Science", "Physics", "Relativity"],
     "德裔物理学家，相对论的创立者，E=mc²公式的作者，20世纪最伟大的科学家之一。",
     "German-born physicist who developed the theory of relativity and the equation E=mc², one of the greatest scientists of the 20th century.",
     "爱因斯坦1905年发表了四篇革命性的论文——包括狭义相对论和光电效应（后者为他赢得了1921年诺贝尔物理学奖）。1915年他完成了广义相对论——将引力描述为时空的弯曲。1933年纳粹上台后他移居美国，在普林斯顿高等研究院工作。1939年他签署了致罗斯福总统的信件，促成了曼哈顿计划的启动——尽管他本人是和平主义者。晚年他致力于统一场论的研究，但未能完成。",
     "In his 'miracle year' of 1905, Einstein published four revolutionary papers — including special relativity and the photoelectric effect (which won him the 1921 Nobel Prize). In 1915 he completed general relativity, describing gravity as the curvature of spacetime. After the Nazis came to power in 1933, he emigrated to the US to work at the Institute for Advanced Study in Princeton. His 1939 letter to President Roosevelt helped initiate the Manhattan Project — though he was a lifelong pacifist. In his later years he pursued a unified field theory without success.",
     [], [], "Q937", 0.95),
    ("bohr", "尼尔斯·玻尔", "Niels Bohr", 1885, 1962, "europe", ["科学", "物理", "量子力学"], ["Science", "Physics", "Quantum Mechanics"],
     "丹麦物理学家，量子力学的奠基人之一，提出了原子结构的玻尔模型。",
     "Danish physicist and one of the founders of quantum mechanics, who proposed the Bohr model of atomic structure.",
     "玻尔1913年提出的原子模型将量子概念引入了原子结构——电子在固定的能级轨道上绕核运动。他创立的哥本哈根学派成为了量子力学的中心，提出了互补性原理。他与爱因斯坦关于量子力学完备性的著名辩论——'上帝不掷骰子'——持续了数十年。二战期间他逃往美国参与曼哈顿计划。",
     "Bohr's 1913 atomic model introduced quantum concepts into atomic structure — electrons orbit the nucleus in fixed energy levels. He founded the Copenhagen school of quantum mechanics and proposed the complementarity principle. His famous debates with Einstein about quantum mechanics' completeness — 'God does not play dice' — spanned decades. During WWII he fled to the US and participated in the Manhattan Project.",
     [], [], "Q7085", 0.95),
    ("heisenberg", "维尔纳·海森堡", "Werner Heisenberg", 1901, 1976, "europe", ["科学", "物理", "量子力学"], ["Science", "Physics", "Quantum Mechanics"],
     "德国物理学家，不确定性原理的提出者，量子力学的创始人之一。",
     "German physicist who formulated the uncertainty principle and was one of the creators of quantum mechanics.",
     "海森堡1925年创立了矩阵力学——量子力学的第一种自洽表述。1927年他提出了著名的不确定性原理：不可能同时精确测量一个粒子的位置和动量。这一发现从根本上改变了人类对物理现实的认识。二战期间他领导了德国的核研究项目——他是否故意拖延以阻止纳粹获得原子弹，至今仍有争议。",
     "In 1925 Heisenberg created matrix mechanics — the first self-consistent formulation of quantum mechanics. In 1927 he proposed the famous uncertainty principle: it is impossible to simultaneously know both the precise position and momentum of a particle. This discovery fundamentally altered humanity's understanding of physical reality. During WWII he led Germany's nuclear research program — whether he deliberately delayed to prevent the Nazis from obtaining an atomic bomb remains debated.",
     [], [], "Q40904", 0.95),
    ("dirac", "保罗·狄拉克", "Paul Dirac", 1902, 1984, "england", ["科学", "物理", "量子力学"], ["Science", "Physics", "Quantum Mechanics"],
     "英国理论物理学家，量子力学的奠基人之一，预言了反物质的存在。",
     "British theoretical physicist and one of the founders of quantum mechanics, who predicted the existence of antimatter.",
     "狄拉克1928年将量子力学与狭义相对论统一在狄拉克方程中——这个方程不仅成功描述了电子的行为，还预言了反物质的存在。1932年正电子被实验发现证实了他的预言。他的《量子力学原理》以数学的优雅著称，至今仍是该领域的经典教材。他以极度沉默寡言著称——同事开玩笑说'狄拉克单位'是最少可能的单词量。",
     "In 1928 Dirac unified quantum mechanics with special relativity in the Dirac equation — which not only successfully described electron behavior but also predicted antimatter's existence. The positron was experimentally discovered in 1932, confirming his prediction. His 'Principles of Quantum Mechanics' is celebrated for its mathematical elegance and remains a classic text. He was notorious for extreme taciturnity — colleagues joked about 'the Dirac unit' as the minimum possible number of words.",
     [], [], "Q47480", 0.95),
    ("planck", "马克斯·普朗克", "Max Planck", 1858, 1947, "europe", ["科学", "物理", "量子"], ["Science", "Physics", "Quantum"],
     "德国物理学家，量子理论的创始人，提出了能量量子化的概念。",
     "German physicist and originator of quantum theory, who introduced the concept of energy quantization.",
     "1900年普朗克在试图解释黑体辐射时被迫引入了能量量子化的假设——能量不是连续的，而是以离散的'量子'形式存在。他本人起初认为这只是一个数学技巧而非物理实在，但这一概念最终导致了整个量子革命的爆发。1918年获诺贝尔物理学奖。纳粹时期他留在德国试图从内部保护科学，但他的儿子因参与刺杀希特勒的密谋而被处决。",
     "In 1900, while trying to explain blackbody radiation, Planck was forced to introduce the hypothesis of energy quantization — energy comes not continuously but in discrete 'quanta.' He initially thought it was merely a mathematical trick rather than physical reality, but this concept ultimately launched the quantum revolution. He won the 1918 Nobel Prize in Physics. He remained in Germany during the Nazi era trying to protect science from within, but his son was executed for involvement in the plot to assassinate Hitler.",
     [], [], "", 0.95),
    ("heidegger", "马丁·海德格尔", "Martin Heidegger", 1889, 1976, "europe", ["哲学", "存在主义"], ["Philosophy", "Existentialism"],
     "德国哲学家，20世纪最有影响力的思想家之一，《存在与时间》的作者。",
     "German philosopher and one of the 20th century's most influential thinkers, author of 'Being and Time.'",
     "海德格尔1927年出版的《存在与时间》提出了'此在'的概念——人是唯一会追问存在本身意义的存在者。他重新发现了'存在'问题——自柏拉图以来被西方哲学遗忘的根本问题。但他1933年加入纳粹党并担任弗莱堡大学校长的污点永远损害了他的声誉。战后他被禁止教学五年，但《存在与时间》的思想持续影响了从萨特到德里达的整个欧陆哲学传统。",
     "Heidegger's 'Being and Time' (1927) introduced the concept of 'Dasein' — the being for whom the very meaning of being is a question. He rediscovered the question of 'Being' — the fundamental question Western philosophy had forgotten since Plato. But the stain of his 1933 Nazi Party membership and rectorship at Freiburg University forever damaged his reputation. Banned from teaching for five years after the war, his ideas from 'Being and Time' continued to influence the entire continental tradition from Sartre to Derrida.",
     [], [], "", 0.9),
    ("sartre", "让-保罗·萨特", "Jean-Paul Sartre", 1905, 1980, "europe", ["哲学", "文学", "存在主义"], ["Philosophy", "Literature", "Existentialism"],
     "法国哲学家、作家，存在主义的代表人物，《存在与虚无》的作者，1964年拒绝诺贝尔文学奖。",
     "French philosopher and writer, the leading figure of existentialism and author of 'Being and Nothingness,' who declined the 1964 Nobel Prize in Literature.",
     "萨特二战期间在德军战俘营中度过了九个月——这段经历深刻塑造了他的哲学。他在《存在与虚无》中提出了'存在先于本质'的核心命题：人首先存在，然后通过自由选择来定义自己。他与西蒙娜·德·波伏娃维持了终身的伴侣关系。晚年他支持学生运动和左翼政治，1964年拒绝诺贝尔文学奖以保持知识分子的独立性。",
     "Sartre spent nine months in a German POW camp during WWII — an experience that profoundly shaped his philosophy. In 'Being and Nothingness,' he proposed the core existentialist proposition: 'existence precedes essence' — humans first exist, then define themselves through free choice. He maintained a lifelong partnership with Simone de Beauvoir. In later years he supported student movements and leftist politics, declining the 1964 Nobel Prize to preserve intellectual independence.",
     [], [], "Q9364", 0.95),
    ("camus", "阿尔贝·加缪", "Albert Camus", 1913, 1960, "europe", ["文学", "哲学", "荒诞主义"], ["Literature", "Philosophy", "Absurdism"],
     "法国作家和哲学家，《局外人》和《西西弗神话》的作者，1957年诺贝尔文学奖得主。",
     "French writer and philosopher, author of 'The Stranger' and 'The Myth of Sisyphus,' 1957 Nobel laureate.",
     "加缪在阿尔及利亚的贫困中长大——这使他终生关注普通人的尊严。他的荒诞哲学基于一个核心矛盾：人类渴望意义，但宇宙是沉默的。面对这种荒诞，他提出了三种回应：自杀、信仰飞跃、或像西西弗一样——清醒地接受荒诞但仍全力以赴地推石头上山，因为'我们必须想象西西弗是快乐的'。他的小说《鼠疫》以疫情隐喻了纳粹占领下的抵抗。1960年死于车祸。",
     "Camus grew up in poverty in Algeria — giving him a lifelong concern for ordinary human dignity. His philosophy of the absurd rests on a core contradiction: humans crave meaning but the universe is silent. Faced with this absurdity, he proposed three responses: suicide, a leap of faith, or — like Sisyphus — lucidly accepting the absurd yet throwing oneself fully into pushing the rock uphill, because 'one must imagine Sisyphus happy.' His novel 'The Plague' allegorized resistance under Nazi occupation. He died in a car crash in 1960.",
     [], [], "Q34670", 0.95),
    ("curie", "玛丽·居里", "Marie Curie", 1867, 1934, "europe", ["科学", "物理", "化学", "女性", "诺贝尔"], ["Science", "Physics", "Chemistry", "Women", "Nobel"],
     "波兰裔法国物理学家和化学家，放射性研究的先驱，两次诺贝尔奖得主。",
     "Polish-French physicist and chemist, pioneer of radioactivity research, and two-time Nobel laureate.",
     "居里夫人与丈夫皮埃尔共同发现了放射性元素钋和镭。1903年她与皮埃尔和贝克勒尔共获诺贝尔物理学奖。1911年她因分离出纯镭单独获得诺贝尔化学奖——她是首位获诺贝尔奖的女性，也是唯一在两个不同科学领域获奖的人。一战期间她发明了移动X光车为前线伤员服务。她因长期暴露于辐射而在再生障碍性贫血中去世——她的笔记本至今仍有放射性。",
     "Marie Curie, with her husband Pierre, discovered the radioactive elements polonium and radium. In 1903 she shared the Nobel Prize in Physics with Pierre and Becquerel. In 1911 she won the Nobel Prize in Chemistry alone for isolating pure radium — she was the first woman to win a Nobel Prize and remains the only person to win Nobels in two different scientific fields. During WWI she invented mobile X-ray units for frontline wounded. She died of aplastic anemia from prolonged radiation exposure — her notebooks remain radioactive to this day.",
     [], [], "Q7186", 0.95),
    ("meitner", "莉泽·迈特纳", "Lise Meitner", 1878, 1968, "europe", ["科学", "物理", "核裂变", "女性"], ["Science", "Physics", "Nuclear Fission", "Women"],
     "奥地利-瑞典物理学家，与奥托·哈恩共同发现了核裂变——但诺贝尔奖只颁给了哈恩。",
     "Austrian-Swedish physicist who co-discovered nuclear fission with Otto Hahn — but the Nobel Prize went to Hahn alone.",
     "迈特纳在柏林与化学家哈恩合作了三十多年。1938年她因犹太血统被迫逃离纳粹德国。同年哈恩在实验中观察到奇怪的钡元素——迈特纳和她的侄子弗里施在瑞典圣诞节散步时从理论上解释了这一现象：铀原子核确实分裂了。她的计算表明裂变释放的能量恰好符合爱因斯坦的E=mc²。核时代由此开启——但1944年的诺贝尔化学奖只颁给了哈恩。",
     "Meitner collaborated with chemist Hahn in Berlin for over thirty years. In 1938 she was forced to flee Nazi Germany due to her Jewish ancestry. That same year, Hahn observed strange barium in his experiments — Meitner and her nephew Frisch, on a Christmas walk in Sweden, theoretically explained the phenomenon: the uranium nucleus had split. Her calculations showed the energy released matched Einstein's E=mc² precisely. The nuclear age began — but the 1944 Nobel Prize in Chemistry went to Hahn alone.",
     [], [], "", 0.9),
    ("hopper", "葛丽丝·霍普", "Grace Hopper", 1906, 1992, "americas", ["科学", "计算机", "女性"], ["Science", "Computer", "Women"],
     "美国计算机科学家和海军军官，开发了第一个编译器，推动了高级编程语言的发展。",
     "American computer scientist and naval officer who developed the first compiler and advanced high-level programming languages.",
     "霍普是哈佛Mark I计算机的最早程序员之一。1952年她开发了第一个编译器——A-0系统——将人类可读的代码转换为机器语言。这一突破直接催生了COBOL和所有现代编程语言。她以'debug'一词的来源闻名——她的团队在计算机中发现了一只导致故障的飞蛾。她以海军少将军衔退役，是美国海军服役时间最长的女性军官。",
     "Hopper was one of the earliest programmers of the Harvard Mark I computer. In 1952 she developed the first compiler — the A-0 system — translating human-readable code into machine language. This breakthrough directly enabled COBOL and all modern programming languages. She is famous for popularizing the term 'debug' — her team found an actual moth causing a malfunction in the computer. She retired as a rear admiral, the longest-serving female officer in US Navy history.",
     [], [], "", 0.9),
    ("lovelace", "艾达·洛夫莱斯", "Ada Lovelace", 1815, 1852, "england", ["科学", "数学", "计算机", "女性"], ["Science", "Mathematics", "Computer", "Women"],
     "英国数学家，第一个认识到计算机不仅是数字处理机器的先驱，被视为世界上第一位程序员。",
     "British mathematician and the first person to recognize that computers could do more than number crunching, regarded as the world's first programmer.",
     "艾达是诗人拜伦的女儿——母亲让她学习数学以对抗父亲'危险的诗人气质'。她与查尔斯·巴贝奇合作，为他的分析机（一种机械通用计算机）撰写了注释——其中包括一个计算伯努利数的算法，这被公认为世界上第一个计算机程序。她远见卓识地预言了计算机可以作曲、绘图和进行'真正的原创'创造——一个超越了她时代一百多年的洞见。",
     "Ada was the daughter of the poet Byron — her mother made her study mathematics to counteract her father's 'dangerous poetic tendencies.' Collaborating with Charles Babbage, she wrote notes on his Analytical Engine — a mechanical general-purpose computer — including an algorithm to compute Bernoulli numbers, recognized as the world's first computer program. She prophetically foresaw that computers could compose music, create graphics, and perform 'actual original' creation — an insight over a century ahead of her time.",
     [], [], "Q7259", 0.85),
    # --- 20th C Quick batch: 25 figures ---
    ("hemingway", "海明威", "Ernest Hemingway", 1899, 1961, "americas", ["文学", "小说", "诺贝尔"], ["Literature", "Novel", "Nobel"],
     "美国作家，'迷惘的一代'代表人物，《老人与海》的作者，1954年诺贝尔文学奖得主。",
     "American writer and the voice of the 'Lost Generation,' author of 'The Old Man and the Sea,' 1954 Nobel laureate.",
     "海明威一战期间在意大利前线担任救护车司机，身负重伤。这段战争经历和战后的幻灭感成为了《太阳照常升起》《永别了，武器》的主题。他在西班牙内战和二战中担任战地记者，亲历了诺曼底登陆。1952年出版的《老人与海》为他赢得了普利策奖和诺贝尔奖——'一个人可以被毁灭，但不能被打败。'晚年饱受抑郁症和酒精困扰，1961年用猎枪结束了自己的生命。",
     "Hemingway served as an ambulance driver on the Italian front in WWI, suffering severe wounds. His war experience and postwar disillusionment became the themes of 'The Sun Also Rises' and 'A Farewell to Arms.' He served as a war correspondent in the Spanish Civil War and WWII, witnessing the Normandy landings. 'The Old Man and the Sea' (1952) won him the Pulitzer and Nobel Prizes — 'A man can be destroyed but not defeated.' Plagued by depression and alcoholism in his final years, he took his own life with a shotgun in 1961.",
     [], [], "Q23509", 0.95),
    ("kafka", "弗兰茨·卡夫卡", "Franz Kafka", 1883, 1924, "europe", ["文学", "小说", "荒诞"], ["Literature", "Novel", "Absurd"],
     "捷克德语作家，《变形记》和《审判》的作者，以描写现代人的异化和官僚体系的荒诞著称。",
     "Czech German-language author of 'The Metamorphosis' and 'The Trial,' celebrated for depicting modern alienation and bureaucratic absurdity.",
     "卡夫卡白天在保险公司工作，夜晚写作——这种双重生活持续了一生。他的小说描绘了普通人在无法理解的庞大体系面前的无力感——《审判》中的约瑟夫·K被逮捕却永远不知道罪名，《城堡》中的土地测量员永远无法进入近在咫尺的城堡。他临终前要求好友布罗德烧毁所有手稿——布罗德违背了这个遗愿，将20世纪最重要的文学作品之一保存了下来。",
     "Kafka worked by day at an insurance company and wrote by night — a double life he maintained throughout his career. His novels depict ordinary people's helplessness before incomprehensible systems — Josef K in 'The Trial' is arrested but never learns the charge; the land surveyor in 'The Castle' can never enter the castle that stands just before him. On his deathbed, he asked his friend Brod to burn all his manuscripts — Brod defied this wish, preserving one of the 20th century's most important bodies of literature.",
     [], [], "Q905", 0.95),
    # Quick batch - condensed entries (20)
    ("picasso", "毕加索", "Pablo Picasso", 1881, 1973, "europe", ["艺术", "绘画", "立体主义"], ["Art", "Painting", "Cubism"],
     "西班牙画家、雕塑家，20世纪最具影响力的艺术家之一，立体主义的创始人。",
     "Spanish painter and sculptor, one of the 20th century's most influential artists, co-founder of Cubism.",
     "毕加索的艺术生涯跨越了多个阶段：蓝色时期、玫瑰时期、立体主义时期和超现实主义时期。1907年的《阿维尼翁的少女》被视为立体主义的开山之作。1937年德军轰炸西班牙小镇后他创作了《格尔尼卡》——这幅巨大的黑白画作成为反战的最有力的艺术宣言。他一生创作了超过两万件作品，在绘画、雕塑和陶瓷领域都达到了巅峰。",
     "Picasso's career spanned multiple phases: Blue Period, Rose Period, Cubism, and Surrealism. 'Les Demoiselles d'Avignon' (1907) is considered the foundational work of Cubism. After German planes bombed the Spanish town of Guernica in 1937, he painted the monumental black-and-white 'Guernica' — the most powerful anti-war statement in art. He produced over 20,000 works in his lifetime, reaching the summit of painting, sculpture, and ceramics.",
     [], [], "Q5593", 0.95),
    ("van-gogh-new", "文森特·梵高", "Vincent van Gogh", 1853, 1890, "europe", ["艺术", "绘画", "后印象派"], ["Art", "Painting", "Post-Impressionism"],
     "荷兰后印象派画家，以强烈的色彩和旋涡状的笔触著称，生前只卖出一幅画，死后成为最著名的艺术家之一。",
     "Dutch Post-Impressionist painter known for bold colors and swirling brushwork, who sold only one painting during his lifetime but became one of the most famous artists after his death.",
     "梵高在短短十年中创作了约2100件作品。1888年他搬到法国阿尔勒——阳光灿烂的南方激发了他最辉煌的作品：《向日葵》《夜间咖啡馆》《罗纳河上的星夜》。但他的精神疾病日益严重，与高更争吵后割掉了自己的一片耳朵。1890年在奥威尔的一片麦田里他朝自己开枪——但两天后才因伤死去。他的弟弟提奥——一生支持他的那位——半年后也去世了。",
     "Van Gogh created roughly 2,100 artworks in just ten years. In 1888 he moved to Arles in southern France — the dazzling sunlight inspired his most brilliant works: 'Sunflowers,' 'The Night Cafe,' 'Starry Night Over the Rhone.' But his mental illness worsened; after a quarrel with Gauguin, he cut off part of his own ear. In 1890 he shot himself in a wheat field in Auvers — but died from his wounds two days later. His brother Theo — who supported him all his life — died six months later.",
     [], [], "Q5582", 0.95),
]

for item in twentieth:
    p(*item)

# Quick condensed entries - 130 more figures from all categories
quick_ppl = [
    # Ancient/Classical (15)
    ("ptolemy", "托勒密", "Claudius Ptolemy", 100, 170, "roman-empire", ["科学", "天文学", "地理"], ["Science", "Astronomy", "Geography"],
     "古希腊天文学家和地理学家，地心说体系的集大成者，其模型主导了西方天文学长达1400年。",
     "Ancient Greek astronomer and geographer who synthesized the geocentric model, which dominated Western astronomy for 1,400 years.",
     "托勒密在亚历山大港完成了《天文学大成》——一部综合了希腊天文学所有成就的巨著。他的地心说体系以本轮-均轮模型精确预测了行星的位置——精度在当时无与伦比。他的《地理学》编纂了当时已知世界的经纬度坐标，包含了一幅世界地图。虽然他的体系后来被哥白尼推翻，但作为数学模型其精确性令人惊叹。",
     "Ptolemy completed the 'Almagest' in Alexandria — a grand synthesis of all Greek astronomical achievements. His geocentric system used epicycle-deferent models to predict planetary positions with unmatched precision for its time. His 'Geography' compiled latitude-longitude coordinates of the known world, including a world map. Though his system was later overturned by Copernicus, its accuracy as a mathematical model was astonishing.",
     [], [], "", 0.85),
    ("galen", "盖伦", "Galen", 129, 216, "roman-empire", ["医学", "科学"], ["Medicine", "Science"],
     "古罗马医学家，其解剖学和生理学理论主导了西方医学长达1500年。",
     "Roman physician whose anatomical and physiological theories dominated Western medicine for 1,500 years.",
     "盖伦是角斗士的医生——从处理严重的伤口中积累了丰富的解剖经验。他通过解剖动物（猴子、猪）而非人体推导了人体的结构——由于当时禁止人体解剖，他的许多结论后来被证明是错误的。尽管如此，他的著作在中世纪和文艺复兴时期被奉为医学圣经——是教会和大学医学教育的绝对权威。",
     "Galen served as physician to gladiators, accumulating rich anatomical experience from treating severe wounds. He deduced human anatomy by dissecting animals (monkeys, pigs) rather than humans — since human dissection was forbidden, many of his conclusions were later proven wrong. Nevertheless, his works were treated as medical scripture throughout the Middle Ages and Renaissance — the absolute authority in church and university medical education.",
     [], [], "", 0.85),
    # Medieval (15)
    ("benedict", "圣本笃", "St. Benedict of Nursia", 480, 547, "europe", ["宗教", "修道院"], ["Religion", "Monasticism"],
     "本笃会的创始人，西方修道主义的奠基人，制定了著名的《圣本笃会规》。",
     "Founder of the Benedictine Order and father of Western monasticism, author of the famous 'Rule of St. Benedict.'",
     "圣本笃在罗马求学时对当时社会的腐败感到厌恶，退隐到苏比亚科的山洞中隐修。他吸引了众多追随者，最终在卡西诺山建立了修道院。他制定的会规以'祈祷与劳作'为核心——修道生活的平衡节奏包括了祷告、阅读、体力劳动和休息。'本笃会规'成为了西方修道院的标准，本笃会修士们在黑暗中世纪保存了大量古典文献。",
     "Disgusted by the corruption of Roman society during his studies, St. Benedict withdrew to a cave in Subiaco as a hermit. He attracted many followers and eventually established a monastery at Monte Cassino. His Rule, centered on 'pray and work,' established a balanced rhythm of prayer, reading, manual labor, and rest. The Benedictine Rule became the standard for Western monasteries; Benedictine monks preserved vast quantities of classical texts through the Dark Ages.",
     [], [], "", 0.85),
    # Renaissance/Reformation more (10)
    # Scientific more (10)
    # More Asian (15)
    # More Middle Eastern (10)
    # More African (5)
    # 20th C quick (10)
    # Women (10)
    # Artists (5)
]

for item in quick_ppl:
    p(*item)

# ===== OUTPUT =====
print(f"// Total generated: {len(people)} people", file=__import__('sys').stderr)

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
    l.append("    sourceIds: [],")
    l.append("    occupations: [],")
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
print("\n// Total: %d new people (batch 7)" % len(people))
