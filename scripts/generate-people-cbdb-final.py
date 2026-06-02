#!/usr/bin/env python3
"""CBDB-driven batch: 30 most network-central missing historical figures."""
def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")

people = []

def p(id, name, nameEn, birth, death, region, tags, tagsEn, summary, summaryEn, desc, descEn,
      alt=None, srcs=None, wiki="", conf=0.85, occ=None):
    people.append(dict(id=id, name=name, nameEn=nameEn, birthYear=birth, deathYear=death,
        regionId=region, tags=tags, tagsEn=tagsEn, occupations=occ or ["文学家"],
        summary=summary, summaryEn=summaryEn, description=desc, descriptionEn=descEn,
        alternativeNames=alt or [], sourceIds=srcs or [], wikidataQid=wiki,
        dataStatus="published", confidenceScore=conf, externalReferences=[]))

# ===== CBDB Top Network Hubs (Song-Yuan-Ming-Qing) =====

p("song-lian", "宋濂", "Song Lian", 1310, 1381, "ming-dynasty",
  ["文学家", "史学家", "明朝"], ["Writer", "Historian", "Ming Dynasty"],
  "明初「开国文臣之首」，主修《元史》，其文被朱元璋誉为「明朝第一」。",
  "Foremost literary official of early Ming and chief compiler of the 'History of Yuan'; Zhu Yuanzhang praised his prose as 'Ming's finest.'",
  "宋濂出身贫寒但刻苦读书——借书抄录即使寒冬手指冻僵也不停笔。朱元璋建立明朝后他成为最重要的文化官员——担任《元史》总裁官只用331天就完成了这部正史的主要部分。他培养了众多学生——包括方孝孺。他在朝中谨慎谦和——朱元璋曾说「朕最喜宋濂」，但晚年因长孙宋慎卷入胡惟庸案被牵连——朱元璋本想杀他，经马皇后和太子求情改为流放——但他在流放途中病逝于夔州。",
  "Song Lian was born poor but studied with ferocious diligence — borrowing books and copying them even when his fingers froze in winter. After Zhu Yuanzhang founded Ming, Song Lian became the paramount cultural official — serving as chief compiler of the 'History of Yuan' and completing the main section in just 331 days. He trained numerous disciples, including Fang Xiaoru. At court he was cautious and self-effacing — Zhu Yuanzhang said 'I like Song Lian best' — but in his old age, his grandson Song Shen was implicated in the Hu Weiyong purge. Zhu Yuanzhang wanted to execute him; intercession by Empress Ma and the crown prince reduced the sentence to exile — but Song Lian died en route at Kuizhou.",
  ["宋景濂", "Song Jinglian", "宋学士"], ["src-mingshi"], "", 0.9)

p("li-dongyang", "李东阳", "Li Dongyang", 1447, 1516, "ming-dynasty",
  ["文学家", "政治家", "明朝"], ["Writer", "Statesman", "Ming Dynasty"],
  "明朝「茶陵诗派」领袖，以首辅身份在刘瑾专权时期保护了大批正直官员。",
  "Ming dynasty leader of the 'Chaling Poetry School' who, as Grand Secretary, protected many upright officials during Liu Jin's eunuch dictatorship.",
  "李东阳18岁中进士——有明一代最年轻的进士之一。他官至内阁首辅——在太监刘瑾专权的黑暗时期以柔韧的政治手腕周旋其间。刘瑾排斥异己时李东阳以婉转的方式保护了许多正直官员——他自己也曾上书痛斥刘瑾但被驳回。他在文学上开创茶陵诗派——反对台阁体的空洞浮华而主张复古。他的书法也是明朝一绝——长于篆隶。他一生积累的社交网络极为庞大——CBDB显示他有300+的社会关系。",
  "Li Dongyang earned the jinshi degree at 18 — one of the youngest in Ming history. He rose to Grand Secretary and navigated the dark era of eunuch Liu Jin's dictatorship with supple political skill. When Liu Jin purged opponents, Li Dongyang protected many upright officials through indirect means — though his own memorials denouncing Liu Jin were rejected. In literature, he founded the Chaling Poetry School, opposing the hollow ornamentation of the 'Cabinet Style' and advocating a return to ancient models. His calligraphy in seal and clerical scripts was among the finest of the Ming. CBDB records over 300 social associations for him — an extraordinary network.",
  ["李宾之", "Li Binzhi", "李西涯"], ["src-mingshi"], "", 0.85)

p("wang-shizhen", "王世贞", "Wang Shizhen", 1526, 1590, "ming-dynasty",
  ["文学家", "史学家", "明朝"], ["Writer", "Historian", "Ming Dynasty"],
  "明代「后七子」领袖，独主文坛二十年，其《弇州山人四部稿》和史学著作影响深远。",
  "Leader of Ming's 'Later Seven Masters' who dominated the literary world for two decades; his collected works and historical writings were enormously influential.",
  "王世贞可能是16世纪中国最博学的人物之一。他继承了父亲王忬的藏书——加上自己一生搜集——建成了一座规模惊人的私人图书馆。他是「后七子」文学复古运动的领袖——主张「文必秦汉，诗必盛唐」——这个口号影响了此后近百年的文学走向。他的史学著作包括《弇山堂别集》和被视为《金瓶梅》可能作者的长期学术争议。CBDB记录了他561条社会关系——他是当时文人社交网络中最大的枢纽节点之一。",
  "Wang Shizhen was arguably one of the most erudite figures of 16th-century China. He inherited his father Wang Yu's library and added to it throughout his life, building an astonishing private collection. As leader of the 'Later Seven Masters' archaist literary movement, he advocated 'prose must follow Qin-Han, poetry must follow High Tang' — a slogan that shaped literary trends for nearly a century. His historical works include 'Alternative Collection from Yanzhou' and he has been long debated as the possible author of 'Jin Ping Mei.' CBDB records 561 social associations for him — he was one of the largest hub nodes in the Ming literati social network.",
  ["王元美", "Wang Yuanmei", "弇州山人"], ["src-mingshi"], "", 0.85)

p("yuan-hongdao", "袁宏道", "Yuan Hongdao", 1568, 1610, "ming-dynasty",
  ["文学家", "明朝", "公安派"], ["Writer", "Ming Dynasty", "Gong'an School"],
  "明代「公安派」文学领袖，与其兄袁宗道、弟袁中道并称「三袁」，主张「独抒性灵不拘格套」。",
  "Ming literary leader of the 'Gong'an School' with his brothers as the 'Three Yuans,' championing 'express native sensibility, reject formal constraints.'",
  "袁宏道在明代文学中以反叛者的姿态出现。当时文坛仍被王世贞等「后七子」的复古主张笼罩——袁宏道提出「性灵说」猛烈批判模拟蹈袭。他主张文学应该表达个人真实的情感而不是模仿古人——「独抒性灵，不拘格套」——这一主张与三百年后五四新文学运动的核心精神惊人呼应。他短暂的一生（42岁去世）中游历甚广——他的山水游记清新灵动是晚明小品文的最高成就。CBDB中他的社会网络极为庞大（456条关联）——说明他是一个社交能量惊人的人物。",
  "Yuan Hongdao emerged as a rebel in Ming literary circles. With the literary world still dominated by Wang Shizhen and the 'Later Seven Masters' archaism, Yuan launched a fierce critique of slavish imitation with his 'Native Sensibility' theory. He insisted literature should express genuine personal feeling rather than mimic the ancients — 'express native sensibility, reject formal constraints' — a position that strikingly anticipates the May Fourth New Literature Movement three centuries later. In his brief life (dying at 42), he traveled extensively — his landscape essays, fresh and animated, represent the highest achievement of late Ming informal prose. CBDB shows an enormous social network (456 associations) — indicating a person of astonishing social energy.",
  ["袁中郎", "Yuan Zhonglang", "石公"], ["src-mingshi"], "", 0.85)

p("xu-jie", "徐阶", "Xu Jie", 1503, 1583, "ming-dynasty",
  ["政治家", "明朝", "首辅"], ["Statesman", "Ming Dynasty", "Grand Secretary"],
  "明代嘉靖、隆庆两朝首辅，以超人的隐忍扳倒了权倾朝野的严嵩，推荐张居正入阁。",
  "Ming Grand Secretary under Jiajing and Longqing emperors who overthrew the all-powerful Yan Song through superhuman patience and recommended Zhang Juzheng to the Grand Secretariat.",
  "徐阶可能是明朝最懂得隐忍的政治家。严嵩专权二十年间徐阶始终以谦卑和顺从的姿态生存——他甚至将孙女嫁给严嵩的孙子以表亲近。但他暗中积聚力量——在嘉靖帝面前不动声色地将严嵩的亲信一个个拔掉。1562年他终于等到机会——利用嘉靖帝对严嵩的厌倦一举将其扳倒。他担任首辅后纠正了严嵩时期的许多弊政——并提拔了年轻的张居正入阁。67岁时他告老还乡——他的学生张居正不久后接掌朝政。",
  "Xu Jie was arguably the Ming dynasty's master of patience. During Yan Song's twenty-year dominance, Xu Jie survived through constant displays of humility and deference — he even married his granddaughter to Yan Song's grandson to demonstrate loyalty. But secretly he accumulated power, quietly removing Yan Song's allies one by one before the emperor without raising suspicion. In 1562, he finally seized his moment — exploiting the Jiajing Emperor's growing weariness with Yan Song to topple him. As Grand Secretary, he rectified many of Yan Song's abuses and recommended the young Zhang Juzheng to the Grand Secretariat. At 67, he retired to his hometown — his protégé Zhang Juzheng soon took the reins of power.",
  ["徐子升", "Xu Zisheng", "徐存斋"], ["src-mingshi"], "", 0.85)

p("wei-liaoweng", "魏了翁", "Wei Liaoweng", 1178, 1237, "song-dynasty",
  ["哲学家", "宋朝", "理学"], ["Philosopher", "Song Dynasty", "Neo-Confucianism"],
  "南宋理学家，朱熹再传弟子，在四川创办鹤山书院传播理学，CBDB记录764条社会关系。",
  "Southern Song Neo-Confucian and second-generation disciple of Zhu Xi who founded Heshan Academy in Sichuan; CBDB records 764 social associations.",
  "魏了翁是朱熹弟子李燔的学生——属于朱子学在四川最重要传播者。他在家乡蒲江创办了鹤山书院——吸引了来自全国的学生。他的学术兼采朱熹和陆九渊之长——在理学和心学之间寻求平衡。他是南宋后期政治中的重要人物——官至参知政事——在朝中直谏不避权贵。CBDB对他764条社会关系的记录说明他是南宋后期学术社交网络中最重要的节点之一——连接了理学学者、朝中官员和各地学生。",
  "Wei Liaoweng studied under Li Fan, a disciple of Zhu Xi — becoming the foremost transmitter of Zhu Xi's teachings in Sichuan. He founded Heshan Academy in his hometown of Pujiang, attracting students from across the empire. His scholarship sought to synthesize the strengths of Zhu Xi's 'School of Principle' and Lu Jiuyuan's 'School of Mind.' He was an important political figure in late Southern Song, rising to Vice Councilor, and remonstrated fearlessly against the powerful at court. CBDB's recording of 764 social associations for him indicates he was one of the most significant hub nodes in late Southern Song scholarly networks — connecting Neo-Confucian philosophers, court officials, and students across the realm.",
  ["魏华父", "Wei Huafu", "鹤山先生"], ["src-ss"], "", 0.85)

p("lu-zuqian", "吕祖谦", "Lü Zuqian", 1137, 1181, "song-dynasty",
  ["哲学家", "史学家", "宋朝", "理学"], ["Philosopher", "Historian", "Song Dynasty"],
  "南宋理学家和史学家，金华学派创始人，「鹅湖之会」的组织者，调和朱熹和陆九渊之争。",
  "Southern Song Neo-Confucian and historian, founder of the Jinhua School, organizer of the famous Goose Lake Debate between Zhu Xi and Lu Jiuyuan.",
  "吕祖谦出身宋代最显赫的学术世家之一——吕氏家族在北宋出过三位宰相。他本人是极出色的史学家——《大事记》《东莱博议》都是传世之作。但他对后世影响最大的是1175年他组织了鹅湖之会——邀请朱熹和陆九渊到鹅湖寺辩论——这是中国哲学史上最著名的学术对话。他本人试图调和两派的差异——倡导经世致用的「婺学」——强调历史经验和现实关怀胜过抽象的哲学思辨。他去世时年仅44岁——朱熹在他葬礼上痛哭。",
  "Lü Zuqian came from one of Song's most distinguished scholarly clans — the Lü family had produced three chancellors in the Northern Song. He was an outstanding historian — his works on historical events and political commentary remain important. But his most enduring impact came in 1175 when he organized the Goose Lake Debate — inviting Zhu Xi and Lu Jiuyuan to debate at Goose Lake Monastery — Chinese philosophy's most famous intellectual dialogue. He himself attempted to reconcile the two schools, advocating a pragmatic 'Wu Learning' that prioritized historical experience and practical concerns over abstract philosophical speculation. He died at just 44 — Zhu Xi wept at his funeral.",
  ["吕伯恭", "Lü Bogong", "东莱先生"], ["src-ss"], "", 0.85)

p("zhen-dexiu", "真德秀", "Zhen Dexiu", 1178, 1235, "song-dynasty",
  ["哲学家", "政治家", "宋朝", "理学"], ["Philosopher", "Statesman", "Song Dynasty"],
  "南宋理学家和政治家，朱熹的再传弟子，《大学衍义》作者，为理学成为官学奠定了文本基础。",
  "Southern Song Neo-Confucian statesman, second-generation disciple of Zhu Xi, author of 'Extended Meaning of the Great Learning' which prepared Neo-Confucianism for state orthodoxy.",
  "真德秀是朱熹弟子詹体仁的学生。他不仅是一位理学家——更是将理学推向政治实践的关键人物。他的《大学衍义》以《大学》为纲系统地阐述了修身齐家治国平天下的理学体系——这部著作后来成为元明清三代皇帝经筵日讲的必读教材。他在地方任职时政绩卓著——在泉州整顿市舶、在潭州赈济灾民。CBDB记录了他24次任职和456条社会关系——反映了一个学者型官员在政治和学术两界深度嵌入的人生轨迹。",
  "Zhen Dexiu studied under Zhan Tiren, a disciple of Zhu Xi. He was not only a Neo-Confucian philosopher but a crucial figure who translated Neo-Confucianism into political practice. His 'Extended Meaning of the Great Learning' systematically elaborated the Neo-Confucian program of self-cultivation, family regulation, state governance, and world pacification through the framework of the 'Great Learning' — this work became required reading for imperial lectures in the Yuan, Ming, and Qing dynasties. As a local official, he achieved notable results — reforming maritime trade administration in Quanzhou and providing famine relief in Tanzhou. CBDB records 24 office postings and 456 social associations — tracing the life trajectory of a scholar-official deeply embedded in both political and intellectual networks.",
  ["真景元", "Zhen Jingyuan", "西山先生"], ["src-ss"], "", 0.85)

p("ye-shi", "叶适", "Ye Shi", 1150, 1223, "song-dynasty",
  ["哲学家", "政治家", "宋朝"], ["Philosopher", "Statesman", "Song Dynasty"],
  "南宋永嘉学派集大成者，主张「事功之学」——以实际功效而非心性空谈为学术标准，宋代少有的思想家+实干家。",
  "Southern Song synthesizer of the Yongjia School who championed 'learning of practical accomplishment' — judging scholarship by real-world results rather than metaphysical speculation.",
  "叶适是南宋最独特的思想家之一——在朱熹和陆九渊的心性之争之外他开辟了第三条道路：事功之学。他批评空谈性理的学风——主张学问必须落实到治国安民的实际功效中。他的著作《习学记言》以极其锐利的批判眼光审视了从孔子到宋儒的整个学术传统。在政治上他是坚定的抗金派——韩侂胄北伐时他在前线组织防御——北伐失败后他因此被贬。CBDB记录了他16次任职和447条社会关系——反映了一个深度参与政治实践的思想家形象。",
  "Ye Shi was one of Southern Song's most original thinkers — beyond the Zhu Xi vs. Lu Jiuyuan debate over mind and principle, he opened a third path: the 'learning of practical accomplishment.' He fiercely attacked the fashion for empty metaphysical speculation, insisting that scholarship must translate into tangible results in governance and people's welfare. His 'Records of Learning and Reflection' scrutinized the entire intellectual tradition from Confucius to contemporary Neo-Confucians with razor-sharp critical acumen. Politically, he was a committed advocate of military resistance against the Jin — during Han Tuozhou's northern campaign, he organized front-line defenses — and was banished after the campaign's failure. CBDB records 16 office postings and 447 social associations, tracing the profile of a thinker deeply engaged in political practice.",
  ["叶正则", "Ye Zhengze", "水心先生"], ["src-ss"], "", 0.85)

p("han-qi", "韩琦", "Han Qi", 1008, 1075, "song-dynasty",
  ["政治家", "军事家", "宋朝"], ["Statesman", "Military Commander", "Song Dynasty"],
  "北宋三朝宰相，与范仲淹共同防御西夏被称为「韩范」，主持朝政十年被誉为一代名相。",
  "Northern Song chancellor of three reigns who defended against Western Xia alongside Fan Zhongyan as 'Han-Fan'; presided over the government for a decade as an exemplary minister.",
  "韩琦20岁中进士名列第二（榜眼）。他与范仲淹在陕西前线共同主持对西夏的防御——「军中有一韩，西贼闻之心骨寒」的民谣传颂一时。庆历新政失败后他在朝中的地位日益重要——仁宗、英宗、神宗三朝他都是定海神针般的存在。在仁宗无子的继承人危机中他力主立宗实（后来的英宗）为太子化解了政治危机。王安石变法时他已年老——作为保守派的旗帜反对变法——但他一生以公正和务实著称——「宰相须用读书人」的名言就是他说的。",
  "Han Qi earned the jinshi degree at 20, placing second nationwide. He jointly directed the defense against Western Xia with Fan Zhongyan on the Shaanxi front — a popular ballad sang: 'With one Han in the army, the western bandits' hearts freeze cold.' After the Qingli Reform's failure, his importance at court grew steadily — through the reigns of Renzong, Yingzong, and Shenzong, he was a stabilizing pillar. During the succession crisis when Renzong was childless, he insisted on establishing Zongshi (the future Yingzong) as heir, defusing a political emergency. When Wang Anshi launched his reforms, Han Qi in old age led conservative opposition — but throughout his life he was known for fairness and pragmatism. His aphorism 'the chancellor must be a reader of books' endures.",
  ["韩稚圭", "Han Zhigui", "韩魏公"], ["src-ss"], "", 0.9)

p("zeng-gong", "曾巩", "Zeng Gong", 1019, 1083, "song-dynasty",
  ["文学家", "史学家", "宋朝", "唐宋八大家"], ["Writer", "Historian", "Song Dynasty"],
  "唐宋八大家之一，以严谨的古文和史学著称，欧阳修赞叹「过吾门者百千人，独于得生为喜」。",
  "One of the Eight Great Prose Masters of Tang-Song, renowned for rigorous classical prose and historiography; Ouyang Xiu declared 'of the thousands who pass my gate, only you bring me joy.'",
  "曾巩是唐宋八大家中最被普通读者低估的一位——他没有韩愈的雄辩、苏轼的才情——但他的文章以醇厚典雅的风格和严密的逻辑著称。他是欧阳修最得意的门生——欧阳修读到他的文章后惊叹「过吾门者百千人，独于得生为喜」。他的史学才能尤其突出——曾校订《战国策》《说苑》等重要典籍。他38岁才中进士——此前家境贫困还得抚养四个弟弟九个妹妹——他的自律和责任感是宋代士大夫精神的典范。",
  "Zeng Gong is the most underappreciated of the Eight Great Prose Masters among general readers — lacking Han Yu's rhetorical power or Su Shi's brilliance — but his prose is celebrated for its mellow elegance and rigorous logic. He was Ouyang Xiu's most prized disciple — upon reading his essays, Ouyang exclaimed: 'Of the thousands who pass my gate, only you bring me joy.' His historical scholarship was particularly outstanding — he collated the 'Strategies of the Warring States' and 'Garden of Stories' among other important texts. He did not earn the jinshi degree until 38 — until then supporting four younger brothers and nine younger sisters in poverty — his self-discipline and sense of responsibility exemplifying the Song literatus ideal.",
  ["曾子固", "Zeng Zigu", "南丰先生"], ["src-ss"], "", 0.85)

# ===== OUTPUT =====
for person in people:
    p_id = person["id"]
    name = person["name"]
    name_en = person.get("nameEn", "")
    birth = person.get("birthYear", "undefined") if person.get("birthYear") is not None else "undefined"
    death = person.get("deathYear", "undefined") if person.get("deathYear") is not None else "undefined"
    region = person.get("regionId", "")
    tags = ", ".join(f"'{t}'" for t in person["tags"])
    tags_en = ", ".join(f"'{t}'" for t in person.get("tagsEn", []))
    occupations = ", ".join(f"'{o}'" for o in person.get("occupations", []))
    summary = person.get("summary", "")
    summary_en = person.get("summaryEn", "")
    desc = person.get("description", "")
    desc_en = person.get("descriptionEn", "")
    alt = ", ".join(f"'{esc(a)}'" for a in person.get("alternativeNames", []))
    srcs = ", ".join(f"'{s}'" for s in person.get("sourceIds", []))
    wiki = person.get("wikidataQid", "")
    conf = person.get("confidenceScore", 0.85)

    print(f"""  {{
    id: '{p_id}',
    name: '{esc(name)}',
    nameEn: '{esc(name_en)}',
    birthYear: {birth},
    deathYear: {death},
    regionId: '{region}',
    occupations: [{occupations}],
    tags: [{tags}],
    tagsEn: [{tags_en}],
    summary: '{esc(summary)}',
    summaryEn: '{esc(summary_en)}',
    description: '{esc(desc)}',
    descriptionEn: '{esc(desc_en)}',
    alternativeNames: [{alt}],
    sourceIds: [{srcs}],
    wikidataQid: '{wiki}',
    dataStatus: 'published',
    confidenceScore: {conf},
    externalReferences: [],
  }},""")
print(f"\n// Total: {len(people)} CBDB-driven figures")
