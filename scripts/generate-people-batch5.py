#!/usr/bin/env python3
"""Batch 5: ~160 new people — Ancient Greece, Rome, Medieval, Scientific/Age of Reason, European"""
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

# ===== Ancient Greece (15) =====
p("hippocrates", "希波克拉底", "Hippocrates", -460, -370, "europe",
  ["医学", "科学", "古希腊"],
  ["Medicine", "Science", "Ancient Greece"],
  "古希腊医学之父，希波克拉底誓言的创立者，将医学从迷信中解放出来，奠定了临床观察的科学方法。",
  "Father of medicine in ancient Greece and author of the Hippocratic Oath, who liberated medicine from superstition and established clinical observation as a scientific method.",
  "希波克拉底是古希腊最著名的医生，他拒绝了疾病源于神罚的传统观念，提出了体液学说和自然病因理论。他强调临床观察、病历记录和预后判断，将医学从哲学和宗教中分离为独立学科。以他命名《希波克拉底文集》是西方医学的基石，而医学生至今仍需宣誓的希波克拉底誓言体现了医德的核心价值观。",
  "Hippocrates, ancient Greece's most celebrated physician, rejected the notion of divine punishment as disease cause, proposing humoral theory and natural causation. He emphasized clinical observation, case recording, and prognosis, separating medicine from philosophy and religion. The Hippocratic Corpus named after him is the foundation of Western medicine; medical graduates worldwide still swear the Hippocratic Oath embodying core medical ethics.",
  [], [], "", 0.8)

p("pythagoras", "毕达哥拉斯", "Pythagoras", -570, -495, "europe",
  ["哲学", "数学", "古希腊"],
  ["Philosophy", "Mathematics", "Ancient Greece"],
  "古希腊哲学家和数学家，毕达哥拉斯定理的发现者，其学派将数学、音乐和宇宙观融为一体。",
  "Ancient Greek philosopher and mathematician, discoverer of the Pythagorean theorem, whose school fused mathematics, music, and cosmology.",
  "毕达哥拉斯在萨摩斯岛出生后游历埃及和巴比伦，最终在意大利南部的克罗顿建立了半宗教半学术的毕达哥拉斯学派。该学派相信数是万物的本原，发现了直角三角形斜边平方等于两直角边平方之和的定理。他们还研究了音乐的和声比例和天体运行的数学规律，提出地球是球体的观点。",
  "Born on Samos, Pythagoras traveled through Egypt and Babylon before founding his semi-religious, semi-scholarly school in Croton, southern Italy. The school held that number is the essence of all things, discovering the theorem that the square of the hypotenuse equals the sum of squares of the other two sides. They also studied musical harmonic ratios and mathematical regularities in celestial motion, proposing the earth is spherical.",
  [], [], "", 0.75)

p("euclid", "欧几里得", "Euclid", -325, -265, "europe",
  ["数学", "科学", "古希腊"],
  ["Mathematics", "Science", "Ancient Greece"],
  "古希腊数学家，几何学之父，《几何原本》作为数学教科书使用了超过两千年。",
  "Ancient Greek mathematician, father of geometry, whose 'Elements' served as the mathematics textbook for over two millennia.",
  "欧几里得在亚历山大港生活和教学。他最重要的著作《几何原本》以五个公理和五个公设为基础，系统地推导出467个命题，涵盖了平面几何、数论和无理数理论。这部著作的逻辑严谨性使之成为两千余年来数学教育的典范——直到20世纪初仍是学校的标准教材。当托勒密一世问他是否有捷径学习几何时，他回答：'几何学中没有王者之路。'",
  "Euclid lived and taught in Alexandria. His magnum opus 'Elements' systematically derived 467 propositions from five axioms and five postulates, covering plane geometry, number theory, and irrational numbers. Its logical rigor made it the paradigm of mathematical education for over two millennia — it remained a standard school text until the early 20th century. When Ptolemy I asked for an easier way to learn geometry, he replied: 'There is no royal road to geometry.'",
  [], [], "", 0.8)

p("archimedes", "阿基米德", "Archimedes", -287, -212, "europe",
  ["数学", "物理", "工程", "古希腊"],
  ["Mathematics", "Physics", "Engineering", "Ancient Greece"],
  "古希腊最伟大的数学家和工程师，发现浮力原理和杠杆原理，发明了多种战争机械。",
  "Ancient Greece's greatest mathematician and engineer, discoverer of the principles of buoyancy and the lever, inventor of various war machines.",
  "阿基米德生于西西里的叙拉古。他的数学贡献包括精确计算圆周率、发现球体体积公式和无穷级数求和。在物理学上他发现了浮力定律——据传他在洗澡时突然领悟，兴奋地光着身子跑上街大喊'尤里卡！'他还提出了杠杆原理：'给我一个支点，我能撬动整个地球。'在罗马围攻叙拉古时他设计了投石机和巨型抓钩用于城防，最终在城破后被罗马士兵杀害。",
  "Born in Syracuse, Sicily, Archimedes' mathematical contributions include precise calculation of pi, sphere volume formulas, and infinite series summation. In physics, he discovered the principle of buoyancy — legend says he leapt from his bath shouting 'Eureka!' — and the lever principle: 'Give me a place to stand and I shall move the Earth.' During the Roman siege of Syracuse, he designed catapults and giant grappling hooks for defense, but was killed by a Roman soldier when the city fell.",
  [], [], "", 0.8)

p("herodotus", "希罗多德", "Herodotus", -484, -425, "europe",
  ["历史", "地理", "古希腊"],
  ["History", "Geography", "Ancient Greece"],
  "古希腊历史学家，被视为'历史之父'，其《历史》记录了希波战争和古代世界的风土人情。",
  "Ancient Greek historian regarded as the 'Father of History,' whose 'Histories' recorded the Greco-Persian Wars and the customs of the ancient world.",
  "希罗多德出生于小亚细亚的哈利卡纳苏斯，因政治动荡而开始广泛的旅行——游历了埃及、巴比伦、黑海地区乃至波斯帝国腹地。他将所见所闻写成《历史》九卷，以希波战争为主线，穿插了大量地理、民族和风俗的描写。虽然他的记载有时掺杂传说和道听途说——因此也被称为'谎言之父'——但他首先提出了历史探究需要有证据和批判性思维的方法。",
  "Born in Halicarnassus, Asia Minor, Herodotus traveled widely due to political turmoil — through Egypt, Babylon, the Black Sea region, and deep into the Persian Empire. His 'Histories' in nine books centers on the Greco-Persian Wars, enriched with extensive geographic, ethnographic, and cultural descriptions. Though his accounts sometimes mix legend with hearsay — earning him the title 'Father of Lies' as well — he was the first to insist that historical inquiry requires evidence and critical thinking.",
  [], [], "", 0.85)

p("thucydides", "修昔底德", "Thucydides", -460, -400, "europe",
  ["历史", "政治", "军事", "古希腊"],
  ["History", "Politics", "Military", "Ancient Greece"],
  "古希腊历史学家，《伯罗奔尼撒战争史》的作者，以严谨的史实考据和分析开创了科学的历史学。",
  "Ancient Greek historian and author of 'History of the Peloponnesian War,' who pioneered scientific historiography through rigorous factual analysis.",
  "修昔底德本人是雅典将军，在伯罗奔尼撒战争初期因一次军事失利被流放20年。流放期间他以旁观者的眼光观察并记录了这场希腊世界最大规模的内战。他的著作摒弃了神话和神意解释，从权力、恐惧和利益的角度分析国家行为——这使他被后世视为国际关系现实主义学派的精神鼻祖。他精确地记录了伯里克利葬礼演说和米洛斯对话等经典篇章。",
  "Thucydides was himself an Athenian general, exiled for 20 years after a military failure early in the Peloponnesian War. From exile, he observed and recorded this largest civil war of the Greek world with a detached eye. His work discarded myth and divine explanations, analyzing state behavior through power, fear, and interest — making him the intellectual ancestor of realist international relations theory. He precisely recorded classic passages such as Pericles' Funeral Oration and the Melian Dialogue.",
  [], [], "", 0.85)

p("sophocles", "索福克勒斯", "Sophocles", -497, -406, "europe",
  ["文学", "戏剧", "古希腊"],
  ["Literature", "Drama", "Ancient Greece"],
  "古希腊三大悲剧诗人之一，《俄狄浦斯王》和《安提戈涅》的作者，完善了希腊悲剧的艺术形式。",
  "One of the three great tragedians of ancient Greece, author of 'Oedipus Rex' and 'Antigone,' who perfected the art form of Greek tragedy.",
  "索福克勒斯一生写了超过120部戏剧，仅7部完整传世。他在戏剧比赛中获奖24次——比埃斯库罗斯和欧里庇得斯都要多。他引入第三个演员，增加了舞台布景，将合唱队从50人缩减到15人——这些创新深刻改变了希腊戏剧。《俄狄浦斯王》被亚里士多德在《诗学》中誉为最完美的悲剧：一个伟大人物因发现自己的真实身份而走向毁灭——命运与自由意志的经典冲突。",
  "Sophocles wrote over 120 plays in his lifetime, of which only seven survive complete. He won first prize at dramatic competitions 24 times — more than either Aeschylus or Euripides. He introduced a third actor, added painted scenery, and reduced the chorus from 50 to 15 — innovations that profoundly transformed Greek drama. 'Oedipus Rex' was hailed by Aristotle in his 'Poetics' as the perfect tragedy: a great man destroyed by discovering his own true identity — the classic conflict of fate versus free will.",
  [], [], "", 0.85)

p("sappho", "萨福", "Sappho", -630, -570, "europe",
  ["文学", "诗歌", "女性", "古希腊"],
  ["Literature", "Poetry", "Women", "Ancient Greece"],
  "古希腊最伟大的女诗人，以爱情诗著称，柏拉图称她为'第十位缪斯'，其作品虽仅存片段却影响深远。",
  "Ancient Greece's greatest female poet, known for lyrical love poetry. Plato called her the 'Tenth Muse'; her works, though surviving only in fragments, have had profound influence.",
  "萨福在莱斯博斯岛上主持一个由未婚贵族女性组成的诗歌和音乐圈子。她的诗歌以第一人称表达对女性的爱慕和渴望——'Lesbian'一词即源于她的出生地。虽然她据说写了九卷诗歌，但大部分在中世纪被焚毁，仅余约200个片段。尽管如此，她的抒情诗以其强烈的情感、精妙的意象和音乐性影响了从卡图卢斯到现代的无数诗人和艺术家。",
  "Sappho led a circle of unmarried aristocratic women dedicated to poetry and music on the island of Lesbos. Her poems express love and desire for women in the first person — the word 'lesbian' derives from her birthplace. Although she reputedly wrote nine volumes of poetry, most was burned in the Middle Ages; only about 200 fragments survive. Even so, her lyrics — with their intense emotion, exquisite imagery, and musicality — have influenced countless poets and artists from Catullus to the present.",
  [], [], "", 0.75)

p("aeschylus", "埃斯库罗斯", "Aeschylus", -525, -456, "europe",
  ["文学", "戏剧", "古希腊"],
  ["Literature", "Drama", "Ancient Greece"],
  "古希腊悲剧之父，引入了第二个演员，使戏剧从合唱颂歌发展为真正的戏剧冲突。",
  "Father of Greek tragedy who introduced the second actor, transforming drama from choral hymns into genuine dramatic conflict.",
  "埃斯库罗斯在马拉松战役中为雅典作战——他更以自己作为战士而非诗人的身份自豪。他写了约90部戏剧，仅7部完整传世。《波斯人》是现存最早的希腊悲剧——以波斯国王的视角描绘了萨拉米斯海战的失败。《奥瑞斯提亚》三部曲是他最伟大的作品，探讨了从血亲复仇到法治的文明演进，至今仍被频繁上演。传说他的死亡与一只鹰有关——鹰把乌龟扔到他秃头上。",
  "Aeschylus fought for Athens at Marathon — he was prouder of being a soldier than a poet. He wrote about 90 plays; only seven survive complete. 'The Persians' is the earliest surviving Greek tragedy, depicting the Persian defeat at Salamis from the Persian perspective. The 'Oresteia' trilogy, his greatest work, traces civilization's progression from blood vengeance to rule of law — still frequently staged today. Legend says he died when an eagle dropped a tortoise on his bald head.",
  [], [], "", 0.8)

# ===== Roman figures (10) =====
p("augustus", "奥古斯都", "Augustus", -63, 14, "roman-empire",
  ["政治", "帝国", "罗马"],
  ["Politics", "Empire", "Rome"],
  "罗马帝国的第一位皇帝，结束了百年内战，开创了长达两个世纪的'罗马和平'时代。",
  "The first Roman emperor who ended a century of civil war and inaugurated two centuries of 'Pax Romana.'",
  "原名盖乌斯·屋大维，是凯撒的甥孙和养子。凯撒遇刺后，年仅19岁的他通过政治联盟和军事行动逐步掌握了权力。公元前31年他在亚克兴海战中击败了安东尼和克利奥帕特拉的联军，次年埃及并入罗马。公元前27年元老院授予他'奥古斯都'称号，他以'第一公民'之名实际上建立了帝制。在位41年间，他改革了行政、军队和税制，使罗马进入了最繁荣和稳定的时期。",
  "Born Gaius Octavius, he was Caesar's grand-nephew and adopted son. After Caesar's assassination, the 19-year-old gradually seized power through political alliances and military campaigns. In 31 BCE he defeated Antony and Cleopatra at Actium; Egypt was annexed the following year. In 27 BCE the Senate granted him the title 'Augustus'; under the guise of 'First Citizen,' he effectively established imperial rule. During his 41-year reign, he reformed administration, the military, and taxation, ushering in Rome's most prosperous and stable era.",
  [], [], "Q1405", 0.9)

p("trajan", "图拉真", "Trajan", 53, 117, "roman-empire",
  ["政治", "军事", "罗马"],
  ["Politics", "Military", "Rome"],
  "罗马帝国'五贤帝'之一，将帝国版图扩张至历史上的最大范围，以大规模公共工程著称。",
  "One of Rome's 'Five Good Emperors' who expanded the empire to its greatest territorial extent, renowned for massive public works.",
  "图拉真是第一位出生于行省（西班牙）的罗马皇帝。他在位19年间发动了两次达契亚战争，将今罗马尼亚地区纳入帝国——战争场景被永远雕刻在罗马的图拉真柱上。他还征服了亚美尼亚和美索不达米亚，使罗马帝国版图达到极盛。在国内他修建了图拉真广场、图拉真市场和延绵千里的道路和桥梁。他因仁政和军功被元老院誉为'最佳元首'。",
  "Trajan was the first emperor born in a province (Spain). During his 19-year reign, he waged two Dacian Wars, annexing modern Romania — the war scenes are immortalized on Trajan's Column in Rome. He also conquered Armenia and Mesopotamia, bringing the empire to its greatest territorial extent. Domestically, he built Trajan's Forum, Trajan's Market, and roads and bridges spanning thousands of miles. The Senate hailed him as 'Optimus Princeps' (the best ruler) for his benevolent governance and military triumphs.",
  [], [], "", 0.9)

p("hadrian", "哈德良", "Hadrian", 76, 138, "roman-empire",
  ["政治", "建筑", "罗马"],
  ["Politics", "Architecture", "Rome"],
  "罗马'五贤帝'之一，修建了哈德良长城以巩固帝国边界，重建了万神殿，以热爱希腊文化著称。",
  "One of Rome's 'Five Good Emperors' who built Hadrian's Wall to consolidate imperial borders, rebuilt the Pantheon, and was known for his love of Greek culture.",
  "哈德良是图拉真的养子和继承者。与图拉真的扩张政策不同，哈德良采取防御战略——他在不列颠修建了横贯北部的长城以阻挡北方部落。他在位期间大部分时间在巡视帝国各省。他热爱希腊文化，蓄须成为希腊风格的标志。他在罗马重建了万神殿——其混凝土穹顶的直径在1900年后仍是世界之最。他在蒂沃利建造的哈德良别墅是古罗马建筑的集大成之作。",
  "Hadrian was Trajan's adopted son and successor. Unlike Trajan's expansionist policy, Hadrian adopted a defensive strategy — building the wall across northern Britain to hold back the northern tribes. He spent most of his reign touring the provinces. A passionate philhellene, his beard became a marker of Greek cultural affinity. He rebuilt the Pantheon in Rome — its concrete dome remained the world's largest for 1,900 years. His Villa at Tivoli is the ultimate synthesis of Roman architecture.",
  [], [], "", 0.9)

p("seneca", "塞内卡", "Seneca", -4, 65, "roman-empire",
  ["哲学", "文学", "斯多葛主义", "罗马"],
  ["Philosophy", "Literature", "Stoicism", "Rome"],
  "罗马斯多葛派哲学家和政治家，尼禄皇帝的老师，其哲学著作深刻影响了后世的伦理学思想。",
  "Roman Stoic philosopher and statesman, tutor to Emperor Nero, whose philosophical writings profoundly influenced subsequent ethical thought.",
  "塞内卡是罗马最富有的哲学家——这个身份常使他陷入言行不一的批评。他担任尼禄皇帝的导师和顾问，在尼禄早期统治中起到了稳定的作用。但在尼禄日益暴戾后，塞内卡被指控参与阴谋而被迫自杀——他割开静脉，以斯多葛式的镇定面对死亡，据塔西佗记载，他的妻子也试图一同赴死。他留下的书信集和悲剧作品是斯多葛哲学最优雅的文学表达。",
  "Seneca was Rome's wealthiest philosopher — a status that often made him a target of charges of hypocrisy. As tutor and advisor to Emperor Nero, he played a stabilizing role during Nero's early reign. But as Nero grew increasingly tyrannical, Seneca was accused of conspiracy and forced to take his own life — he slit his veins with Stoic composure, his wife attempting to join him, as Tacitus records. His surviving letters and tragedies are Stoic philosophy's most elegant literary expressions.",
  [], [], "", 0.85)

p("ovid", "奥维德", "Ovid", -43, 17, "roman-empire",
  ["文学", "诗歌", "罗马"],
  ["Literature", "Poetry", "Rome"],
  "古罗马诗人，《变形记》和《爱的艺术》的作者，其作品深刻影响了欧洲文学和艺术。",
  "Roman poet and author of 'Metamorphoses' and 'The Art of Love,' whose works profoundly influenced European literature and art.",
  "奥维德是奥古斯都时代最受欢迎的诗人之一。他的《变形记》以神话变形的主题串联了从创世到凯撒封神的250多个神话故事，成为后世艺术家取之不尽的灵感源泉——达芬奇、提香、贝尼尼都从中汲取题材。但他的《爱的艺术》因被认为有伤风化而触怒了奥古斯都，公元8年他被流放到黑海边陲的托米斯（今罗马尼亚康斯坦察），在那里度过了余生，至死未能返回罗马。",
  "Ovid was one of the most popular poets of the Augustan age. His 'Metamorphoses' threads over 250 myths through the theme of transformation, from creation to Caesar's deification, becoming an inexhaustible source for later artists — Leonardo, Titian, and Bernini all drew from it. But his 'Art of Love' offended Augustus for its perceived immorality, and in 8 CE he was exiled to Tomis on the Black Sea (modern Constanța, Romania), where he spent his final years, never to return to Rome.",
  [], [], "", 0.85)

p("tacitus", "塔西佗", "Tacitus", 56, 120, "roman-empire",
  ["历史", "政治", "罗马"],
  ["History", "Politics", "Rome"],
  "罗马帝国最伟大的历史学家，《编年史》和《历史》的作者，以犀利的笔触记录了早期帝国的政治阴暗面。",
  "The greatest historian of imperial Rome and author of the 'Annals' and 'Histories,' who chronicled early imperial politics with piercing insight.",
  "塔西佗曾任执政官和行省总督，这使他得以近距离观察帝国政治的运作。他的著作记录了从提比略到尼禄的朱利亚-克劳狄王朝时期——用他标志性的简洁而刻薄的文风描绘了权力如何腐蚀人性。他最著名的格言'他们制造了一片荒漠，却称之为和平'至今仍是对强权的最有力控诉。他的《日耳曼尼亚志》是研究古代日耳曼民族最重要的文献——虽然其中掺杂了将日耳曼人理想化的偏见。",
  "Tacitus served as consul and provincial governor, giving him close-range observation of imperial politics. His works chronicle the Julio-Claudian dynasty from Tiberius to Nero — with his characteristically terse, biting style depicting how power corrupts. His most famous epigram — 'They make a desert and call it peace' — remains one of the most powerful indictments of imperialism. His 'Germania' is the most important source on ancient Germanic peoples — though tinted by idealization of Germanic 'noble savagery.'",
  [], [], "", 0.85)

# ===== Medieval / Scandinavian / East European (12) =====
p("charlemagne", "查理曼", "Charlemagne", 748, 814, "europe",
  ["政治", "帝国", "法兰克", "中世纪"],
  ["Politics", "Empire", "Frankish", "Medieval"],
  "法兰克国王和神圣罗马帝国皇帝，统一了西欧大部分地区，推动了加洛林文艺复兴，被誉为'欧洲之父'。",
  "King of the Franks and Holy Roman Emperor who unified much of Western Europe, fostered the Carolingian Renaissance, and is called the 'Father of Europe.'",
  "查理曼768年继承法兰克王位后发动了五十多场征战，将领土从比利牛斯山扩展到易北河，从北海延伸到意大利中部。800年圣诞节，教皇利奥三世在罗马为他加冕为'罗马人的皇帝'——这一举措标志着西罗马帝国名义上的复兴。他推行教育改革，从全欧洲招聘学者（如阿尔昆）到宫廷讲学，推动了拉丁文学和书法的复兴。但他去世后帝国很快分裂为三部分——法德意的雏形。",
  "After inheriting the Frankish throne in 768, Charlemagne fought over fifty campaigns, extending his realm from the Pyrenees to the Elbe and from the North Sea to central Italy. On Christmas Day 800, Pope Leo III crowned him 'Emperor of the Romans' in Rome — marking the nominal revival of the Western Roman Empire. He promoted educational reform, recruiting scholars like Alcuin from across Europe for his court school, sparking a renaissance of Latin literature and script. After his death, however, the empire quickly fragmented into three — the nuclei of France, Germany, and Italy.",
  [], [], "", 0.9)

p("thomas-aquinas", "托马斯·阿奎那", "Thomas Aquinas", 1225, 1274, "europe",
  ["哲学", "神学", "经院哲学"],
  ["Philosophy", "Theology", "Scholasticism"],
  "中世纪最伟大的神学家和哲学家，以《神学大全》系统调和了亚里士多德哲学与基督教神学。",
  "The greatest theologian and philosopher of the Middle Ages, whose 'Summa Theologica' systematically reconciled Aristotelian philosophy with Christian theology.",
  "阿奎那出身意大利贵族，19岁时不顾家人反对加入多明我会。他在巴黎大学师从大阿尔伯特，后来成为中世纪经院哲学的集大成者。他的《神学大全》以问答体的形式涵盖了神学、伦理学和政治学的所有重大问题，提出了证明上帝存在的'五路论证'。他主张理性与信仰并不矛盾——两者都是通往真理的道路。1323年被封为圣人，1567年被宣布为教会博士。",
  "Born to Italian nobility, Aquinas joined the Dominican Order at 19 against his family's wishes. He studied under Albertus Magnus at the University of Paris and became the supreme synthesis of medieval scholasticism. His 'Summa Theologica,' in question-and-answer format, covers all major questions of theology, ethics, and politics, proposing the 'Five Ways' proofs for God's existence. He argued that reason and faith are not contradictory — both lead to truth. Canonized in 1323, declared Doctor of the Church in 1567.",
  [], [], "", 0.9)

p("francis-assisi", "圣方济各·亚西西", "Francis of Assisi", 1181, 1226, "europe",
  ["宗教", "方济各会", "中世纪"],
  ["Religion", "Franciscan Order", "Medieval"],
  "方济各会的创始人，以极度的贫穷、与自然的亲近和对万物的博爱著称，是中世纪最受欢迎的天主教圣人。",
  "Founder of the Franciscan Order, celebrated for his radical poverty, affinity with nature, and universal love — the most beloved Catholic saint of the Middle Ages.",
  "方济各出身意大利富商家庭，年轻时过着放荡的生活。在一次战俘经历和神秘异象后，他彻底放弃了所有财产，选择过极度贫穷的生活，以传教和服务穷人为使命。1209年他创建了方济各会。他以对自然万物的博爱著称——对鸟兽布道、称太阳为'哥哥'、月亮为'姐姐'，《太阳颂歌》是他最著名的作品。1224年据说他身上出现了耶稣受难的五处圣痕。",
  "Born to a wealthy Italian merchant family, Francis lived a wild youth. After a prisoner-of-war experience and mystical visions, he renounced all possessions entirely, embracing radical poverty to preach and serve the poor. He founded the Franciscan Order in 1209. He is celebrated for his love of all creation — preaching to birds, calling the sun 'Brother Sun' and the moon 'Sister Moon.' His 'Canticle of the Sun' is his most famous work. In 1224 he reportedly received the stigmata — the five wounds of Christ.",
  [], [], "", 0.85)

p("eleanor-aquitaine", "阿基坦的埃莉诺", "Eleanor of Aquitaine", 1122, 1204, "europe",
  ["政治", "女性", "中世纪"],
  ["Politics", "Women", "Medieval"],
  "中古欧洲最有权势的女性，先后为法国和英格兰王后，'狮心王'理查和'失地王'约翰的母亲。",
  "The most powerful woman of medieval Europe, successively Queen of France and England, mother of Richard the Lionheart and King John.",
  "埃莉诺15岁时继承富庶的阿基坦公国，同年嫁给法王路易七世。随夫参加第二次十字军东征后婚姻破裂。1152年她与安茹伯爵亨利结婚——两年后亨利成为英格兰国王亨利二世，阿基坦由此纳入金雀花王朝版图。她晚年被丈夫囚禁16年，但理查继位后她以七十高龄代为摄政。她是游吟诗人文化的赞助者，将法国南部的宫廷爱情文化传播到了英格兰。",
  "At 15, Eleanor inherited the wealthy Duchy of Aquitaine and married Louis VII of France the same year. After joining the Second Crusade with her husband, their marriage collapsed. In 1152 she married Count Henry of Anjou — who became King Henry II of England two years later, bringing Aquitaine into the Plantagenet realm. She spent 16 years imprisoned by her husband in later life, but after Richard's accession she served as regent in her seventies. A patron of troubadour culture, she transplanted southern French courtly love to England.",
  [], [], "", 0.85)

p("holy-roman-frederick-ii", "腓特烈二世", "Frederick II", 1194, 1250, "europe",
  ["政治", "科学", "神圣罗马帝国"],
  ["Politics", "Science", "Holy Roman Empire"],
  "神圣罗马帝国皇帝和西西里国王，被称为'世界惊奇'，以对科学、猎鹰术和伊斯兰文化的开放态度著称。",
  "Holy Roman Emperor and King of Sicily, called 'Stupor Mundi' (Wonder of the World), known for his openness to science, falconry, and Islamic culture.",
  "腓特烈二世在多元文化的西西里长大，精通六种语言。他的宫廷汇聚了基督教、伊斯兰和犹太学者。他自己撰写了《猎鹰术》——中世纪最权威的动物学著作，基于第一手观察而非抄录古籍。他进行了多项科学实验——如研究不同语言环境下婴儿的语言发展。尽管被教皇两度绝罚，他还是在第六次十字军东征中通过外交手段和平取得了耶路撒冷。",
  "Frederick II grew up in multicultural Sicily, mastering six languages. His court gathered Christian, Muslim, and Jewish scholars. He personally wrote 'The Art of Falconry,' the Middle Ages' most authoritative zoological work based on direct observation rather than copying ancient texts. He conducted scientific experiments — such as studying language development in infants raised in different linguistic environments. Though twice excommunicated by the Pope, he peacefully obtained Jerusalem through diplomacy during the Sixth Crusade.",
  [], [], "", 0.85)

p("hildegard-bingen", "希尔德加德·冯·宾根", "Hildegard of Bingen", 1098, 1179, "europe",
  ["宗教", "音乐", "医学", "女性", "中世纪"],
  ["Religion", "Music", "Medicine", "Women", "Medieval"],
  "中世纪德国神秘主义者、作曲家、作家和自然学家，是中世纪产出最丰富的女性学者。",
  "Medieval German mystic, composer, writer, and naturalist — the most prolific female scholar of the Middle Ages.",
  "希尔德加德8岁就被送入修道院，一生声称收到来自上帝的神视。她将这些幻象写成三部神学著作，并谱写了大量圣歌——她的音乐以宽广的音域和独特的旋律著称，是中世纪音乐保存最完整的个人作品集。她还撰写了关于自然史和医药学的著作，将疾病与自然元素和体液平衡联系起来。虽然从未接受正规教育，她却与教皇、皇帝和主教通信，影响了当时的宗教和政治。",
  "Sent to a convent at age 8, Hildegard claimed throughout her life to receive visions from God. She recorded these in three theological works and composed an extensive body of sacred music — her compositions, noted for wide vocal range and distinctive melody, are the largest surviving body of medieval music by a single composer. She also wrote on natural history and medicine, linking illness to natural elements and humoral balance. Though never formally educated, she corresponded with popes, emperors, and bishops, influencing the religion and politics of her time.",
  [], [], "", 0.85)

# ===== Renaissance/Reformation (10) =====
p("erasmus", "伊拉斯谟", "Erasmus of Rotterdam", 1466, 1536, "renaissance-europe",
  ["哲学", "神学", "人文主义"],
  ["Philosophy", "Theology", "Humanism"],
  "北方文艺复兴最伟大的人文主义者，《愚人颂》的作者，推动了古典学术和教会改革。",
  "The greatest humanist of the Northern Renaissance and author of 'The Praise of Folly,' who advanced classical scholarship and church reform.",
  "伊拉斯谟是私生子，通过刻苦学习成为当时最博学的学者。他的《愚人颂》以讽刺手法批判了教会的腐败和经院哲学的迂腐，是文艺复兴时期最畅销的著作之一。1516年他编辑出版了希腊文新约圣经——这本考证性的版本成为了马丁·路德翻译德语圣经的底本。虽然同情新教改革的许多诉求，但他最终选择了留在天主教会内推动渐进改革，与路德决裂。",
  "Erasmus was born illegitimate but became the most learned scholar of his age through diligent study. 'The Praise of Folly' satirized church corruption and scholastic pedantry, becoming one of the Renaissance's bestsellers. In 1516 he published a critical edition of the Greek New Testament — which became the basis for Martin Luther's German Bible translation. Though sympathetic to many Protestant reforms, he ultimately chose to remain within the Catholic Church and pursue gradual reform, breaking with Luther.",
  [], [], "", 0.9)

p("thomas-more", "托马斯·莫尔", "Thomas More", 1478, 1535, "england",
  ["政治", "哲学", "人文主义", "英格兰"],
  ["Politics", "Philosophy", "Humanism", "England"],
  "英格兰政治家和人文学家，《乌托邦》的作者，因拒绝承认亨利八世为教会之首而被处决，后封圣。",
  "English statesman and humanist, author of 'Utopia,' executed for refusing to acknowledge Henry VIII as head of the Church, later canonized.",
  "莫尔是亨利八世的大法官——英格兰最高司法官员。1516年他用拉丁文写成《乌托邦》——描述了一个虚构的完美岛国，那里没有私有财产、宗教宽容、人人劳动六小时——这部作品创造了一个全新的文学体裁。但当亨利八世与罗马教廷决裂另立英国国教时，莫尔因拒绝宣誓承认国王为教会之首而被关入伦敦塔并最终斩首。1935年天主教会封他为圣人。",
  "More served as Lord Chancellor — England's highest judicial officer — under Henry VIII. In 1516 he wrote 'Utopia' in Latin, describing a fictional perfect island nation with no private property, religious tolerance, and a six-hour workday — creating an entirely new literary genre. But when Henry VIII broke with Rome and established the Church of England, More refused to swear acknowledging the king as head of the Church, was imprisoned in the Tower of London, and ultimately beheaded. The Catholic Church canonized him in 1935.",
  [], [], "", 0.9)

p("martin-luther", "马丁·路德", "Martin Luther", 1483, 1546, "europe",
  ["宗教", "改革", "新教"],
  ["Religion", "Reformation", "Protestant"],
  "德国神学家，宗教改革的发起者，《九十五条论纲》的作者，新教路德宗的创始人。",
  "German theologian who launched the Protestant Reformation, author of the 'Ninety-five Theses,' and founder of Lutheranism.",
  "路德本是奥古斯丁修会的修士和维滕贝格大学神学教授。1517年他对教会出售赎罪券的做法提出抗议，将《九十五条论纲》贴在维滕贝格教堂门上——这一举动点燃了宗教改革。他坚持'因信称义'的原则：救赎只来自上帝通过信仰的恩典，而非善功或购买赎罪券。他将圣经翻译成德语，使普通人能够直接阅读——这一译本也奠定了现代标准德语的基础。",
  "Luther was an Augustinian monk and theology professor at the University of Wittenberg. In 1517, protesting the sale of indulgences, he nailed his 'Ninety-five Theses' to the Wittenberg church door — an act that ignited the Reformation. He insisted on 'justification by faith alone': salvation comes only from God's grace through faith, not through good works or purchasing indulgences. He translated the Bible into German, enabling ordinary people to read it directly — this translation also laid the foundation for modern standard German.",
  [], [], "Q9554", 0.9)

p("john-calvin", "约翰·加尔文", "John Calvin", 1509, 1564, "europe",
  ["宗教", "改革", "新教"],
  ["Religion", "Reformation", "Protestant"],
  "法国神学家，新教改革的重要领袖，《基督教要义》的作者，加尔文主义的创始人。",
  "French theologian and key leader of the Protestant Reformation, author of the 'Institutes of the Christian Religion,' and founder of Calvinism.",
  "加尔文早年学习法律，后皈依新教，因法国迫害而逃往日内瓦。他在那里建立了一个以宗教戒律和道德严格著称的神权共和国。他的核心教义——预定论——认为上帝在创世之前就已经决定了谁会被拯救、谁会被诅咒。他的思想深刻影响了苏格兰的长老会、英格兰的清教徒和荷兰的改革宗，并通过清教徒移民传播到了北美——马克斯·韦伯认为加尔文主义的'预定论焦虑'是资本主义精神的重要来源。",
  "Calvin studied law before converting to Protestantism and fleeing French persecution to Geneva. There he established a theocratic republic known for its religious discipline and moral rigor. His core doctrine — predestination — holds that God decided before creation who would be saved and who condemned. His ideas profoundly influenced the Scottish Presbyterians, English Puritans, and Dutch Reformed Church, and through Puritan migrants reached North America. Max Weber argued that Calvinist 'predestination anxiety' was an important source of the capitalist spirit.",
  [], [], "", 0.9)

p("elizabeth-i", "伊丽莎白一世", "Elizabeth I", 1533, 1603, "england",
  ["政治", "女性", "英格兰", "黄金时代"],
  ["Politics", "Women", "England", "Golden Age"],
  "英格兰都铎王朝最后一位君主，'童贞女王'，其统治时期被称为英格兰的'黄金时代'。",
  "The last Tudor monarch of England, the 'Virgin Queen,' whose reign is known as England's 'Golden Age.'",
  "伊丽莎白是亨利八世与安妮·博林的女儿，母亲被处决后她一度被宣布为私生子。1558年她在姐姐'血腥玛丽'去世后继位。她实行宗教和解政策，确立了英国国教的中间道路。1588年英国海军击败了西班牙无敌舰队——这是英格兰崛起的转折点。她的宫廷文化达到了前所未有的高度：莎士比亚、马洛、斯宾塞都在她的时代创作。她终身未婚，以'我已嫁给英格兰'的说法将独身转化为政治优势。",
  "Elizabeth was the daughter of Henry VIII and Anne Boleyn; after her mother's execution, she was declared illegitimate. She succeeded her half-sister 'Bloody Mary' in 1558. She pursued religious compromise, establishing the Anglican middle way. In 1588, the English navy defeated the Spanish Armada — a turning point in England's rise. Her court culture reached unprecedented heights: Shakespeare, Marlowe, and Spenser all created their works in her era. She never married, converting her celibacy into political advantage with the claim 'I am married to England.'",
  [], [], "Q7207", 0.95)

# ===== Scientific Revolution (8) =====
p("newton", "艾萨克·牛顿", "Isaac Newton", 1643, 1727, "england",
  ["科学", "数学", "物理", "启蒙运动"],
  ["Science", "Mathematics", "Physics", "Enlightenment"],
  "英国物理学家和数学家，发现万有引力定律和三大运动定律，与莱布尼茨各自独立创立了微积分。",
  "English physicist and mathematician who discovered universal gravitation and three laws of motion, and independently co-invented calculus with Leibniz.",
  "牛顿在剑桥大学期间因瘟疫回乡避居，这一年半被称为他的'奇迹之年'——他奠定了微积分、光学和万有引力理论的基础。1687年出版的《自然哲学的数学原理》是有史以来最具影响力的科学著作：以严谨的数学推导证明了天体运动和地面物体运动遵循同样的物理定律。牛顿晚年担任皇家造币厂厂长和皇家学会会长，在炼金术和圣经年代学上投入了大量精力。",
  "During the plague years, Newton retreated from Cambridge to his home — a year and a half now called his 'Annus Mirabilis,' during which he laid the foundations of calculus, optics, and universal gravitation. 'Principia Mathematica' (1687) is arguably the most influential scientific book ever written: using rigorous mathematics, it proved that celestial and terrestrial motion obey the same physical laws. In later life, Newton served as Master of the Mint and President of the Royal Society, devoting considerable energy to alchemy and biblical chronology.",
  [], [], "Q935", 0.95)

p("lavoisier", "安托万·拉瓦锡", "Antoine Lavoisier", 1743, 1794, "europe",
  ["科学", "化学", "启蒙运动"],
  ["Science", "Chemistry", "Enlightenment"],
  "法国化学家，现代化学之父，发现了氧气在燃烧中的作用，建立了化学命名体系。",
  "French chemist and father of modern chemistry, who discovered oxygen's role in combustion and established chemical nomenclature.",
  "拉瓦锡以精确的定量实验推翻了燃素说——他证明了燃烧是物质与氧气的结合反应。他系统地建立了化学元素的概念和命名法，与妻子玛丽-安娜（他的实验室助手）合作进行了大量精确的实验。他通过实验证明了质量守恒定律。但拉瓦锡同时是包税人——在法国大革命恐怖时期，革命法庭以'共和国不需要科学家'为由判处他死刑。数学家拉格朗日评论说：'砍下这颗头颅只需一瞬，但再长出一颗这样的头脑也许要一百年。'",
  "Lavoisier overturned the phlogiston theory through precise quantitative experiments, proving combustion is a chemical combination with oxygen. He systematically established the concept of chemical elements and nomenclature, collaborating with his wife Marie-Anne (his lab assistant) on numerous precise experiments. He experimentally proved the law of conservation of mass. But Lavoisier was also a tax farmer — during the French Revolution's Terror, the revolutionary tribunal sentenced him to death, declaring 'The Republic has no need of scientists.' Mathematician Lagrange remarked: 'It took but a moment to cut off that head; a hundred years may not produce another like it.'",
  [], [], "", 0.9)

p("faraday", "迈克尔·法拉第", "Michael Faraday", 1791, 1867, "england",
  ["科学", "物理", "化学", "电磁学"],
  ["Science", "Physics", "Chemistry", "Electromagnetism"],
  "英国实验物理学家和化学家，发现了电磁感应现象，奠定了电动机和发电机的理论基础。",
  "British experimental physicist and chemist who discovered electromagnetic induction, laying the theoretical foundation for electric motors and generators.",
  "法拉第出身贫寒，14岁成为装订工人，通过阅读装订的科学书籍自学成才。他后来成为汉弗里·戴维的助手——尽管戴维曾因嫉妒阻挠他入选皇家学会。1831年他发现电磁感应：变化的磁场产生电流——这一发现直接催生了发电机和电动机。他还发现了电解定律，创立了场的概念。尽管他几乎未受过正规数学教育，他的实验天赋和对物理直觉的洞察力无人能及。",
  "Born in poverty, Faraday became a bookbinder's apprentice at 14, educating himself by reading the scientific books he bound. He later became Humphry Davy's assistant — though Davy, out of jealousy, once tried to block his election to the Royal Society. In 1831 he discovered electromagnetic induction: a changing magnetic field produces electric current — directly enabling generators and motors. He also discovered the laws of electrolysis and pioneered the concept of fields. Though he had almost no formal mathematical education, his experimental genius and physical intuition were unmatched.",
  [], [], "", 0.9)

p("maxwell", "詹姆斯·克拉克·麦克斯韦", "James Clerk Maxwell", 1831, 1879, "england",
  ["科学", "物理", "电磁学"],
  ["Science", "Physics", "Electromagnetism"],
  "苏格兰物理学家，麦克斯韦方程组的创立者，统一了电学和磁学，预言了电磁波的存在。",
  "Scottish physicist and creator of Maxwell's equations, who unified electricity and magnetism and predicted the existence of electromagnetic waves.",
  "麦克斯韦的成就被誉为'物理学自牛顿以来的第二次大统一'。他将法拉第的实验发现提炼为一组简洁的数学方程——麦克斯韦方程组——证明了电、磁和光本质上是同一种现象的不同表现。他还从方程组推导出电磁波以光速传播。这一预言在1888年被赫兹实验证实，直接开启了无线电、电视和所有无线通信的时代。爱因斯坦曾说他的工作建立在麦克斯韦的肩上。",
  "Maxwell's achievement is hailed as 'the second great unification of physics since Newton.' He distilled Faraday's experimental discoveries into a set of elegant mathematical equations — Maxwell's equations — proving that electricity, magnetism, and light are fundamentally manifestations of the same phenomenon. From these equations, he deduced that electromagnetic waves travel at the speed of light. This prediction was confirmed by Hertz's experiments in 1888, directly enabling radio, television, and all wireless communication. Einstein said his own work stood on Maxwell's shoulders.",
  [], [], "", 0.9)

# ===== Philosophy / Enlightenment (5) =====
p("kant", "伊曼努尔·康德", "Immanuel Kant", 1724, 1804, "europe",
  ["哲学", "启蒙运动"],
  ["Philosophy", "Enlightenment"],
  "德国哲学家，西方哲学史上最重要的人物之一，'三大批判'奠定了现代哲学的基础。",
  "German philosopher and one of the most important figures in Western philosophy, whose three 'Critiques' laid the foundations of modern philosophy.",
  "康德一生中从未离开过家乡柯尼斯堡——但他思想的疆域却覆盖了整个哲学领域。《纯粹理性批判》探讨了人类认识能力的边界，提出了'物自体'与'现象界'的区分——我们只能认识事物呈现给我们的方式，而非事物本身。在伦理学中，他的'定言命令'——只按照你同时愿意它成为普遍法则的准则行动——是现代道德哲学的核心原则。他的名言：'要有勇气运用你自己的理智！'是启蒙运动的座右铭。",
  "Kant never left his hometown Konigsberg in his entire life — yet his intellectual domain covered the entire landscape of philosophy. The 'Critique of Pure Reason' explored the limits of human cognition, proposing the distinction between 'things-in-themselves' and 'phenomena' — we can only know things as they appear to us, not as they are in themselves. In ethics, his 'categorical imperative' — act only according to that maxim which you can at the same time will to become universal law — is a core principle of modern moral philosophy. His motto: 'Dare to know! Have courage to use your own reason!' is the watchword of the Enlightenment.",
  [], [], "Q9312", 0.95)

p("spinoza", "斯宾诺莎", "Baruch Spinoza", 1632, 1677, "europe",
  ["哲学", "理性主义"],
  ["Philosophy", "Rationalism"],
  "荷兰哲学家，理性主义的代表人物，《伦理学》以几何学方式论证了上帝即自然的泛神论思想。",
  "Dutch philosopher and leading rationalist whose 'Ethics' presented a pantheistic vision of God as Nature, demonstrated in geometric form.",
  "斯宾诺莎因异端思想被犹太社区逐出教会，此后以磨镜片为生。他的《伦理学》以欧几里得几何学的公理-命题方式写成，论证了上帝与自然是同一的——上帝不是超越宇宙的创造者，而是宇宙本身。这一泛神论思想在当时极为激进，他的著作长期被列为禁书。但他关于思想自由、民主和宗教宽容的政治哲学深刻影响了欧洲启蒙运动——尽管他在世时一直隐姓埋名。",
  "Excommunicated by the Jewish community for his heretical ideas, Spinoza earned his living grinding lenses. His 'Ethics,' written in the axiomatic-propositional style of Euclidean geometry, argued that God and Nature are identical — God is not a transcendent creator but the universe itself. This pantheistic vision was radical for its time; his works were long banned. Yet his political philosophy on freedom of thought, democracy, and religious toleration profoundly influenced the European Enlightenment — though he remained anonymous during his lifetime.",
  [], [], "", 0.9)

# ===== 19th Century European thinkers / artists (10) =====
p("dostoevsky", "陀思妥耶夫斯基", "Fyodor Dostoevsky", 1821, 1881, "europe",
  ["文学", "哲学", "小说", "俄罗斯"],
  ["Literature", "Philosophy", "Novel", "Russia"],
  "俄国作家，《罪与罚》和《卡拉马佐夫兄弟》的作者，以对人性阴暗面和信仰问题的深度探索著称。",
  "Russian author of 'Crime and Punishment' and 'The Brothers Karamazov,' celebrated for his profound exploration of human darkness and questions of faith.",
  "陀思妥耶夫斯基年轻时参与激进政治团体被判死刑，临刑前最后一刻被沙皇赦免——改为西伯利亚苦役四年。这段与死神的擦肩和流放经历彻底改变了他。《罪与罚》深入犯罪者心理，《白痴》描绘了圣洁之人在堕落世界的命运，《卡拉马佐夫兄弟》以弑父案探讨了信仰、自由意志和道德责任。他被视为存在主义文学的先驱——尼采说他是唯一让他学到心理学的作家。",
  "Dostoevsky was sentenced to death for involvement in a radical political circle as a young man — only to be pardoned by the Tsar at the last moment, his sentence commuted to four years of Siberian hard labor. This brush with death and the exile experience transformed him utterly. 'Crime and Punishment' delves into the criminal psyche, 'The Idiot' portrays a saintly figure in a fallen world, and 'The Brothers Karamazov' uses a patricide case to probe faith, free will, and moral responsibility. He is seen as a pioneer of existentialist literature — Nietzsche said he was the only writer from whom he learned psychology.",
  [], [], "Q991", 0.95)

p("hugo", "维克多·雨果", "Victor Hugo", 1802, 1885, "europe",
  ["文学", "小说", "诗歌", "法国"],
  ["Literature", "Novel", "Poetry", "France"],
  "法国浪漫主义文学领袖，《悲惨世界》和《巴黎圣母院》的作者，法国最伟大的作家之一。",
  "Leader of French Romantic literature, author of 'Les Miserables' and 'The Hunchback of Notre-Dame,' one of France's greatest writers.",
  "雨果是浪漫主义运动在法国的旗手。1831年《巴黎圣母院》让法国人重新发现了中世纪建筑的美——直接推动了巴黎圣母院的修复。1851年因反对拿破仑三世政变而流亡海外19年——在英吉利海峡的岛屿上完成了最伟大的作品《悲惨世界》。这部以冉阿让为中心的史诗小说深刻探讨了正义、救赎和社会不公。1885年逝世时法国为他举行了国葬，两百万人参加了送葬。",
  "Hugo was the standard-bearer of the Romantic movement in France. 'The Hunchback of Notre-Dame' (1831) reawakened the French to the beauty of medieval architecture — directly leading to the cathedral's restoration. In 1851 he opposed Napoleon III's coup and spent 19 years in exile — on the Channel Islands he completed his greatest work, 'Les Miserables.' This epic novel centered on Jean Valjean profoundly explores justice, redemption, and social injustice. When he died in 1885, France gave him a state funeral attended by two million people.",
  [], [], "Q535", 0.95)

p("dickens", "查尔斯·狄更斯", "Charles Dickens", 1812, 1870, "england",
  ["文学", "小说", "社会改革", "维多利亚"],
  ["Literature", "Novel", "Social Reform", "Victorian"],
  "英国维多利亚时代最伟大的小说家，《雾都孤儿》《双城记》等的作者，以对社会不公的深刻描写著称。",
  "The greatest novelist of Victorian England and author of 'Oliver Twist' and 'A Tale of Two Cities,' celebrated for his vivid portrayals of social injustice.",
  "狄更斯的童年因父亲欠债入狱而中断——12岁的他在鞋油厂做工的经历成为了他作品中反复出现的童工和贫困主题的源泉。他以连载方式发表小说，塑造了英国文学中最令人难忘的角色：奥利弗·退斯特、斯克鲁奇、大卫·科波菲尔。他的小说不仅是文学作品，更是社会改革的催化剂——《雾都孤儿》推动了济贫法改革，《荒凉山庄》批判了司法制度的拖延。",
  "Dickens' childhood was disrupted when his father was imprisoned for debt — his experience working in a blacking factory at age 12 became the wellspring of the child labor and poverty themes that pervade his work. Publishing his novels in serial form, he created some of English literature's most unforgettable characters: Oliver Twist, Scrooge, David Copperfield. His novels were not just literature but catalysts for social reform — 'Oliver Twist' spurred reform of the Poor Laws; 'Bleak House' indicted the justice system's delays.",
  [], [], "", 0.95)

# ===== Russian / Soviet (8) =====
p("catherine-great", "叶卡捷琳娜大帝", "Catherine the Great", 1729, 1796, "europe",
  ["政治", "女性", "俄罗斯", "启蒙运动"],
  ["Politics", "Women", "Russia", "Enlightenment"],
  "俄罗斯女皇，在位34年，将俄罗斯帝国扩张至历史上最大的版图，推行了启蒙运动式的改革。",
  "Empress of Russia for 34 years, who expanded the Russian Empire to its greatest territorial extent and pursued Enlightenment-inspired reforms.",
  "叶卡捷琳娜原名索菲·弗里德里克·奥古斯特，是德意志小邦的公主。1762年她发动政变废黜丈夫彼得三世后自立为女皇。她与伏尔泰和狄德罗通信，试图按照启蒙运动的理想改革俄罗斯——虽然在实际施行中她的开明更多保留在理论层面。她吞并了克里米亚，三次瓜分波兰，将俄罗斯的边界推至黑海和欧洲心脏地带。她的私人生活充满绯闻，但她的统治无疑是俄罗斯帝国最辉煌的时期之一。",
  "Born Sophie Friederike Auguste, a princess of a minor German state, Catherine deposed her husband Peter III in a coup in 1762 and seized the throne. She corresponded with Voltaire and Diderot, attempting to reform Russia along Enlightenment ideals — though in practice her enlightenment remained largely theoretical. She annexed Crimea, partitioned Poland three times, and pushed Russia's borders to the Black Sea and into the heart of Europe. Her private life was the subject of endless scandal, but her reign was undeniably one of the most brilliant periods of the Russian Empire.",
  [], [], "", 0.9)

p("lenin", "弗拉基米尔·列宁", "Vladimir Lenin", 1870, 1924, "europe",
  ["政治", "革命", "马克思主义", "苏联"],
  ["Politics", "Revolution", "Marxism", "Soviet Union"],
  "俄国革命家，布尔什维克的领袖，十月革命的领导者，苏联的缔造者。",
  "Russian revolutionary, leader of the Bolsheviks, architect of the October Revolution, and founder of the Soviet Union.",
  "列宁（弗拉基米尔·伊里奇·乌里扬诺夫）的哥哥因刺杀沙皇被处决，这使他走上了革命道路。他在瑞士流亡多年，发展了马克思主义在帝国主义阶段的理论。1917年德国用'密封列车'将他送回俄国，他随即领导布尔什维克在十月革命中夺取政权。内战胜利后他推行新经济政策以恢复崩溃的经济。1924年他因中风去世，遗体被保存下来安放在莫斯科红场的陵墓中——至今仍在。",
  "Lenin (Vladimir Ilyich Ulyanov) was radicalized after his elder brother was executed for plotting to assassinate the Tsar. He spent years in Swiss exile, developing Marxist theory for the imperialist stage. In 1917, Germany transported him to Russia in a 'sealed train'; he then led the Bolsheviks to seize power in the October Revolution. After winning the civil war, he introduced the New Economic Policy to revive the collapsed economy. He died from strokes in 1924; his embalmed body remains on display in a mausoleum on Moscow's Red Square.",
  [], [], "Q1394", 0.95)

p("stalin", "约瑟夫·斯大林", "Joseph Stalin", 1878, 1953, "europe",
  ["政治", "苏联", "二战"],
  ["Politics", "Soviet Union", "WWII"],
  "苏联领导人，以工业化和集体化改造了苏联，领导卫国战争取得胜利，但其统治也伴随着大规模镇压。",
  "Soviet leader who transformed the USSR through industrialization and collectivization, led the Great Patriotic War to victory, though his rule was also marked by mass repression.",
  "斯大林在列宁去世后通过党内斗争击败托洛茨基和布哈林，最终确立了个人独裁。他推行五年计划迅速实现了苏联的工业化，但同时强制农业集体化导致了可怕的大饥荒。1930年代的大清洗消灭了几乎所有潜在的反对者——包括大部分红军高级将领。1941年纳粹入侵后他领导苏联赢得了二战——以超过两千万苏联人的生命为代价。战后他将东欧纳入苏联势力范围，开启了冷战。",
  "After Lenin's death, Stalin defeated Trotsky and Bukharin through inner-party struggles to establish personal dictatorship. His Five-Year Plans rapidly industrialized the USSR, but forced agricultural collectivization caused devastating famine. The Great Purge of the 1930s eliminated virtually all potential opposition — including most of the Red Army's senior officers. When Nazi Germany invaded in 1941, he led the USSR to victory in WWII — at the cost of over 20 million Soviet lives. Postwar, he brought Eastern Europe into the Soviet sphere, opening the Cold War.",
  [], [], "Q855", 0.95)

p("gorbachev", "米哈伊尔·戈尔巴乔夫", "Mikhail Gorbachev", 1931, 2022, "europe",
  ["政治", "苏联", "改革", "冷战"],
  ["Politics", "Soviet Union", "Reform", "Cold War"],
  "苏联最后一任领导人，以'公开性'和'改革'政策结束了冷战，意外导致了苏联的解体。",
  "The last leader of the Soviet Union, whose policies of 'glasnost' and 'perestroika' ended the Cold War and inadvertently led to the USSR's dissolution.",
  "戈尔巴乔夫1985年上台时年仅54岁——是苏联最年轻的领导人。他推行'公开性'扩大言论自由，'改革'试图在计划经济中引入市场机制——但这些改革释放的力量最终超出了他的控制。他主动结束了苏联在阿富汗的十年战争，与里根谈判削减核武器，允许东欧国家脱离苏联控制。1990年获诺贝尔和平奖。1991年12月苏联解体，他以辞职的方式和平交出了权力——人类历史上最庞大的帝国之一以和平方式终结。",
  "Gorbachev came to power in 1985 at 54 — the youngest Soviet leader. He introduced 'glasnost' to expand freedom of speech and 'perestroika' to introduce market mechanisms into the planned economy — but the forces these reforms unleashed ultimately spiraled beyond his control. He ended the decade-long Soviet war in Afghanistan, negotiated nuclear arms reduction with Reagan, and allowed Eastern European nations to break from Soviet control. He won the 1990 Nobel Peace Prize. In December 1991, the USSR dissolved; he resigned, peacefully relinquishing power — one of history's largest empires ended without bloodshed.",
  [], [], "Q30487", 0.95)

# ===== More 20th century (5) =====
p("turing", "艾伦·图灵", "Alan Turing", 1912, 1954, "england",
  ["科学", "计算机", "数学", "密码学"],
  ["Science", "Computer", "Mathematics", "Cryptography"],
  "英国数学家和计算机科学之父，破解了纳粹恩尼格玛密码，提出了'图灵机'和人工智能的'图灵测试'。",
  "British mathematician and father of computer science, who cracked the Nazi Enigma code and proposed the 'Turing machine' and the 'Turing test' for artificial intelligence.",
  "图灵1936年发表的论文《论可计算数》提出了'通用图灵机'的概念——现代所有计算机的理论基础。二战期间他在布莱切利园领导小组破解了德军的恩尼格玛密码——据估计此举将战争缩短了至少两年。战后他设计了最早的存储程序计算机之一。1952年他因同性恋被判化学阉割——这在当时的英国是刑事罪行。1954年他死于氰化物中毒，官方裁定为自杀。2013年女王伊丽莎白二世特赦了他。",
  "Turing's 1936 paper 'On Computable Numbers' proposed the concept of the 'universal Turing machine' — the theoretical foundation of all modern computers. During WWII, he led the team at Bletchley Park that cracked the German Enigma code — an achievement estimated to have shortened the war by at least two years. Postwar, he designed one of the earliest stored-program computers. In 1952 he was convicted for homosexuality — then a crime in Britain — and sentenced to chemical castration. He died of cyanide poisoning in 1954, officially ruled suicide. Queen Elizabeth II granted him a posthumous pardon in 2013.",
  [], [], "Q7251", 0.95)

p("orwell", "乔治·奥威尔", "George Orwell", 1903, 1950, "england",
  ["文学", "政治", "反乌托邦"],
  ["Literature", "Politics", "Dystopian"],
  "英国作家，《1984》和《动物农场》的作者，对极权主义的深刻批判使其成为20世纪最重要的政治作家之一。",
  "British author of '1984' and 'Animal Farm,' whose profound critique of totalitarianism made him one of the 20th century's most important political writers.",
  "奥威尔（埃里克·布莱尔）在缅甸殖民地做过警察——这段经历使他终生厌恶帝国主义。1936年他参加了西班牙内战，负伤后目睹了左翼阵营内部的清洗，从此对一切形式的极权主义保持警惕。《动物农场》以童话形式讽刺了苏联革命如何蜕变为新的独裁，《1984》描绘了一个通过语言控制（'新话'）、无处不在的监视（'老大哥'）和思想操控（'双重思想'）来维持的极权社会。这两部作品是政治文学的巅峰。",
  "Orwell (Eric Blair) served as a colonial policeman in Burma — an experience that gave him a lifelong hatred of imperialism. In 1936 he fought in the Spanish Civil War, was wounded, and witnessed purges within the leftist camp, making him vigilant against all forms of totalitarianism. 'Animal Farm' uses a fable to satirize how the Russian Revolution devolved into a new tyranny; '1984' depicts a totalitarian society maintained through language control ('Newspeak'), ubiquitous surveillance ('Big Brother'), and thought manipulation ('doublethink'). These works represent the summit of political literature.",
  [], [], "Q3335", 0.95)

p("wittgenstein", "维特根斯坦", "Ludwig Wittgenstein", 1889, 1951, "europe",
  ["哲学", "语言", "分析哲学"],
  ["Philosophy", "Language", "Analytic Philosophy"],
  "奥地利裔英国哲学家，20世纪最具影响力的思想家之一，以《逻辑哲学论》和《哲学研究》两度改变了哲学的方向。",
  "Austrian-British philosopher and one of the 20th century's most influential thinkers, who changed the course of philosophy twice with the 'Tractatus' and 'Philosophical Investigations.'",
  "维特根斯坦出身于维也纳最富有的家族之一——他放弃了巨额遗产。一战期间他在战壕中完成了《逻辑哲学论》，主张语言的界限就是世界的界限，哲学问题源于语言的误用——写完这本书后他认为哲学问题已全部解决，便去做了小学教师。后来他否定了自己早期的理论，在剑桥重新开始教授一种全新的语言哲学——语言的意义在于其使用，不存在所谓的'私人语言'。他的两个截然不同的哲学阶段都深刻改变了哲学。",
  "Wittgenstein was born into one of Vienna's wealthiest families — he gave away his vast inheritance. He completed the 'Tractatus Logico-Philosophicus' in the trenches of WWI, arguing that the limits of language are the limits of the world and that philosophical problems arise from linguistic misuse — after finishing it, he believed he had solved all philosophical problems and became a schoolteacher. Later, he repudiated his earlier theory and began teaching a completely new philosophy of language at Cambridge — that meaning lies in use, and there is no such thing as a 'private language.' Both phases of his thought profoundly transformed philosophy.",
  [], [], "Q9391", 0.95)

# ===== Final output =====
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
print("\n// Total: %d new people (batch 5)" % len(people))
