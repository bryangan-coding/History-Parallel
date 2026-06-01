#!/usr/bin/env python3
"""Batch 8: Programmatic bulk generation of ~200 people from concise data"""
import sys

def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'")

# Each entry: (id, name_zh, name_en, birth, death, region_id, tags_zh_str, tags_en_str, 
#              summary_zh, summary_en, desc_zh, desc_en, wikidata)
# Generate entries as structured tuples for efficiency

data = [
    # === Ancient World ===
    ("pericles", "伯里克利", "Pericles", -495, -429, "europe",
     "政治,民主,雅典", "Politics,Democracy,Athens",
     "雅典黄金时代的领袖，将雅典民主制度推向巅峰。",
     "Leader of Athens' Golden Age who brought Athenian democracy to its peak.",
     "伯里克利领导雅典近三十年，主持建造了帕特农神庙，将提洛同盟变成了雅典帝国。他的时代见证了苏格拉底、索福克勒斯和菲迪亚斯等天才的涌现。他在伯罗奔尼撒战争初期死于瘟疫——雅典失去他后逐渐走向失败。他的葬礼演说对雅典民主价值观的阐述是西方政治思想的经典文本。",
     "Pericles led Athens for nearly three decades, oversaw the construction of the Parthenon, and transformed the Delian League into an Athenian empire. His era witnessed the flowering of geniuses like Socrates, Sophocles, and Phidias. He died of plague early in the Peloponnesian War — Athens, without him, gradually slid toward defeat. His Funeral Oration articulating Athenian democratic values is a foundational text of Western political thought.",
     ""),

    ("democritus", "德谟克利特", "Democritus", -460, -370, "europe",
     "哲学,科学,原子论", "Philosophy,Science,Atomism",
     "古希腊哲学家，原子论的创立者，提出万物由不可分割的原子组成。",
     "Ancient Greek philosopher and founder of atomism, who proposed that all matter consists of indivisible atoms.",
     "德谟克利特提出了一种惊人的直觉：万物由在虚空中运动的不可分割的微小粒子——原子——组成。不同的原子形状和排列产生了不同的物质和感知。两千多年后，现代科学证实了他的原子论的核心洞见。他被称为'欢笑的哲学家'——因为他认为在原子和虚空的宇宙中，快乐是人生的最高目标。",
     "Democritus proposed an astonishing intuition: all things consist of indivisible tiny particles — atoms — moving through the void. Different atomic shapes and arrangements produce different substances and sensations. Over two millennia later, modern science confirmed the core insight of his atomism. He was called the 'laughing philosopher' — because in a universe of atoms and void, he held cheerfulness to be the highest goal of life.",
     ""),

    # === Roman ===
    ("nero", "尼禄", "Nero", 37, 68, "roman-empire",
     "政治,罗马,暴君", "Politics,Rome,Tyrant",
     "罗马帝国第五位皇帝，以暴政和奢华著称，传说在罗马大火时弹琴作乐。",
     "The fifth Roman emperor, notorious for tyranny and extravagance, legendarily 'fiddled while Rome burned.'",
     "尼禄17岁即位，早期在塞内卡等人的辅佐下治理尚可。但后来他处死了母亲阿格里皮娜和妻子，以残酷镇压反对者闻名。公元64年罗马大火——他嫁祸给基督徒进行了大规模迫害。他建造了奢华的'金宫'，其自我表演的欲望——参加奥运会的各种比赛——严重损害了皇帝尊严。68年军队叛乱，他自杀前说：'一个多么伟大的艺术家死去了！'",
     "Nero ascended at 17, and his early reign under Seneca's guidance was decent. But he later executed his mother Agrippina and his wife, and became known for brutal suppression of opponents. After Rome's great fire in 64 CE, he blamed and massively persecuted Christians. He built the extravagant 'Golden House'; his craving to perform — entering Olympic competitions — severely damaged imperial dignity. When the army rebelled in 68, he committed suicide, reportedly saying: 'What an artist dies in me!'",
     ""),

    ("justinian", "查士丁尼一世", "Justinian I", 482, 565, "byzantine",
     "政治,法律,拜占庭", "Politics,Law,Byzantine",
     "拜占庭帝国皇帝，编纂了《查士丁尼法典》，建造了圣索菲亚大教堂。",
     "Byzantine emperor who codified Roman law in the 'Corpus Juris Civilis' and built the Hagia Sophia.",
     "查士丁尼以'一个帝国、一个教会、一部法典'为理想统治帝国。他命特里波尼安编纂了《民法大全》——这部法学巨著成为后世欧洲大陆法系的基础。他建造了君士坦丁堡的圣索菲亚大教堂——其穹顶建筑千年无匹。他的将军贝利撒留收复了北非和意大利的部分领土。但在位期间帝国遭遇了毁灭性的大瘟疫——查士丁尼瘟疫——严重削弱了国力。",
     "Justinian ruled with the ideal of 'one empire, one church, one code of law.' He commissioned Tribonian to compile the 'Corpus Juris Civilis' — this monumental legal work became the foundation of continental European law. He built Constantinople's Hagia Sophia — its dome was architecturally unmatched for a millennium. His general Belisarius reconquered parts of North Africa and Italy. But the empire was devastated during his reign by the Justinianic Plague, severely weakening its power.",
     ""),

    # === Science/Philosophy ===
    ("copernicus", "哥白尼", "Nicolaus Copernicus", 1473, 1543, "renaissance-europe",
     "科学,天文学,日心说", "Science,Astronomy,Heliocentrism",
     "波兰天文学家，日心说的提出者，引发了改变人类宇宙观的科学革命。",
     "Polish astronomer who proposed the heliocentric model, sparking the scientific revolution that transformed humanity's view of the cosmos.",
     "哥白尼在生命的最后一年才敢发表《天体运行论》——他在书中将太阳而非地球置于宇宙的中心。这一观点彻底颠覆了统治西方思想一千四百年的托勒密地心体系。传说他在去世当天才看到印好的书。他的日心说为开普勒、伽利略和牛顿的工作奠定了基础——虽然他的模型仍然使用圆形轨道而非椭圆轨道。",
     "Copernicus only dared to publish 'On the Revolutions of the Heavenly Spheres' in the final year of his life — a book placing the sun, not the earth, at the center of the universe. This view completely overturned the Ptolemaic geocentric system that had dominated Western thought for 1,400 years. Legend says he received the printed copy on his deathbed. His heliocentrism laid the groundwork for Kepler, Galileo, and Newton — though his model still used circular rather than elliptical orbits.",
     ""),

    ("kepler", "约翰内斯·开普勒", "Johannes Kepler", 1571, 1630, "europe",
     "科学,天文学,数学", "Science,Astronomy,Mathematics",
     "德国天文学家和数学家，发现了行星运动三大定律，为牛顿万有引力理论奠定了基础。",
     "German astronomer and mathematician who discovered the three laws of planetary motion, laying the foundation for Newton's theory of gravitation.",
     "开普勒在丹麦天文学家第谷·布拉赫的精确观测数据基础上，发现行星绕太阳运行的轨道不是圆形而是椭圆——这是打破了两千年圆轨道教条的第一人。他的三大定律精确描述了行星的运动规律。他同时是占星家，在三十年战争的动荡中为多个贵族服务。他在讨薪途中病逝——墓志铭是他自己的诗：'我曾测量天空，现在测量大地；灵魂飞向天堂，身体安息于此。'",
     "Working from the precise observational data of Danish astronomer Tycho Brahe, Kepler discovered that planetary orbits are elliptical, not circular — the first person in two millennia to break the circular orbit dogma. His three laws precisely describe planetary motion. He was also an astrologer, serving various nobles amid the chaos of the Thirty Years' War. He died on a journey to collect unpaid salary — his epitaph was his own poem: 'I measured the skies, now the shadows I measure; sky-bound was the mind, earth-bound the body rests.'",
     ""),

    ("galileo", "伽利略", "Galileo Galilei", 1564, 1642, "renaissance-europe",
     "科学,天文学,物理", "Science,Astronomy,Physics",
     "意大利科学家，近代实验科学的奠基人，用望远镜发现木星卫星，因支持日心说受宗教审判。",
     "Italian scientist and founder of modern experimental science, who discovered Jupiter's moons through a telescope and was tried by the Inquisition for supporting heliocentrism.",
     "伽利略改进了望远镜并将其对准夜空——发现了木星的四颗卫星、金星的相位和太阳黑子。这些发现直接挑战了亚里士多德-托勒密的宇宙观。他在比萨斜塔上做了落体实验（传说），证明了物体下落速度与重量无关。1633年宗教裁判所迫使他公开宣布放弃日心说——据传他在审判后低声说：'然而它确实在转动。'他在软禁中度过了生命的最后八年。",
     "Galileo improved the telescope and aimed it at the night sky — discovering Jupiter's four moons, Venus's phases, and sunspots. These findings directly challenged the Aristotelian-Ptolemaic worldview. He (legendarily) dropped objects from the Leaning Tower of Pisa, proving falling speed is independent of weight. In 1633 the Inquisition forced him to publicly recant heliocentrism — supposedly muttering after his trial: 'And yet it moves.' He spent his final eight years under house arrest.",
     "Q307"),

    ("darwin", "查尔斯·达尔文", "Charles Darwin", 1809, 1882, "england",
     "科学,生物学,进化论", "Science,Biology,Evolution",
     "英国自然学家，进化论的提出者，《物种起源》的作者，彻底改变了人类对生命的理解。",
     "British naturalist who proposed the theory of evolution and authored 'On the Origin of Species,' which fundamentally transformed humanity's understanding of life.",
     "达尔文1831年随'小猎犬号'进行了五年的环球航行——加��帕戈斯群岛上不同岛屿的雀鸟喙型启发了他。经过二十年的研究和犹豫，1859年他终于出版了《物种起源》——提出自然选择是物种演化的机制。'适者生存'的概念不仅在科学界引发了革命，也深刻影响了社会思想。他自己形容发表这一理论'就像承认一桩谋杀案'——因为它动摇了一切生物由神特殊创造的教义。",
     "Darwin sailed for five years on HMS Beagle starting in 1831 — finches' beak variations across Galapagos islands inspired his insight. After two decades of research and hesitation, he finally published 'On the Origin of Species' in 1859 — proposing natural selection as the mechanism of evolution. The concept of 'survival of the fittest' not only revolutionized science but profoundly impacted social thought. He described publishing the theory as 'like confessing a murder' — because it undermined the doctrine of special creation.",
     "Q1035"),

    ("pasteur", "路易·巴斯德", "Louis Pasteur", 1822, 1895, "europe",
     "科学,微生物学,医学", "Science,Microbiology,Medicine",
     "法国化学家和微生物学家，微生物学的奠基人，发明了巴氏消毒法和狂犬病疫苗。",
     "French chemist and microbiologist, founder of microbiology, who invented pasteurization and the rabies vaccine.",
     "巴斯德用天鹅颈瓶实验最终否定了自然发生说——证明了微生物来自已有的微生物，而非从无生命中自发产生。他发明了巴氏消毒法以保存葡萄酒和牛奶，发现了蚕病的原因，并研制了炭疽和狂犬病疫苗。他抱着被疯狗咬伤的9岁男孩约瑟夫·麦斯特时，世人都在屏息注视——小男孩活了下来。巴斯德的名言：'机会偏爱有准备的头脑。'",
     "Pasteur definitively disproved spontaneous generation with his swan-neck flask experiment — proving microorganisms come from existing microorganisms, not spontaneously from non-living matter. He invented pasteurization to preserve wine and milk, discovered the cause of silkworm disease, and developed vaccines for anthrax and rabies. The world held its breath as he treated 9-year-old Joseph Meister, bitten by a rabid dog — and the boy survived. Pasteur's maxim: 'Chance favors the prepared mind.'",
     ""),

    ("mendel", "孟德尔", "Gregor Mendel", 1822, 1884, "europe",
     "科学,遗传学", "Science,Genetics",
     "奥地利修道士，遗传学之父，通过对豌豆的实验发现了遗传的基本规律。",
     "Austrian monk and father of genetics who discovered the fundamental laws of inheritance through pea plant experiments.",
     "孟德尔在布尔诺修道院的花园中花了八年时间种植和杂交了两万八千多株豌豆。他系统地追踪了七种性状的遗传模式——发现了显性和隐性遗传、分离定律和自由组合定律。但他1866年发表的论文在当时几乎无人注意。直到1900年——他去世16年后——三位科学家独立重新发现了他的定律，他的天才才被世人所认识。",
     "Mendel spent eight years in the garden of his Brno monastery, growing and cross-breeding over 28,000 pea plants. He systematically tracked the inheritance patterns of seven traits — discovering dominant and recessive inheritance, the law of segregation, and the law of independent assortment. But his 1866 paper went virtually unnoticed. Only in 1900 — 16 years after his death — when three scientists independently rediscovered his laws, did the world recognize his genius.",
     ""),

    # === Literature/Arts ===
    ("dante", "但丁", "Dante Alighieri", 1265, 1321, "renaissance-europe",
     "文学,诗歌,意大利", "Literature,Poetry,Italy",
     "意大利诗人，《神曲》的作者，意大利语文学的奠基人，中世纪文学的巅峰。",
     "Italian poet and author of 'The Divine Comedy,' founder of Italian vernacular literature and the summit of medieval literature.",
     "但丁因政治原因被家乡佛罗伦萨永久流放——正是在流放中他完成了人类文学史上最宏大的作品之一。《神曲》以第一人称叙述了穿越地狱、炼狱和天堂的旅程——维吉尔引领他穿过地狱和炼狱，贝雅特里齐引领他进入天堂。这部作品以严整的韵律结构和百科全书式的内容描绘了中世纪的世界观，同时为意大利语作为一种文学语言奠定了基础。",
     "Dante was permanently exiled from his native Florence for political reasons — it was in exile that he completed one of the most monumental works in literary history. 'The Divine Comedy' narrates in the first person a journey through Hell, Purgatory, and Paradise — Virgil guiding him through Hell and Purgatory, Beatrice through Paradise. The work, with its rigorous metrical structure and encyclopedic scope, captures the medieval worldview while establishing Italian as a literary language.",
     "Q1067"),

    ("cervantes", "塞万提斯", "Miguel de Cervantes", 1547, 1616, "europe",
     "文学,小说,西班牙", "Literature,Novel,Spain",
     "西班牙作家，《堂吉诃德》的作者，被视为现代小说的奠基人。",
     "Spanish author of 'Don Quixote,' regarded as the founder of the modern novel.",
     "塞万提斯的一生充满坎坷——他参加过勒班陀海战并失去了左手的活动能力，被海盗俘虏为奴隶五年，几次越狱失败，回国后做过税吏并被两次投入监狱。1605年他出版了《堂吉诃德》第一部——这部关于一个读骑士小说入迷的老绅士的喜剧式流浪小说成为了世界文学的一座丰碑。他与莎士比亚同一天去世——1616年4月23日。",
     "Cervantes' life was full of hardships — he fought at the Battle of Lepanto and lost the use of his left hand, was enslaved by pirates for five years, attempted escape several times, and was jailed twice as a tax collector. In 1605 he published Part One of 'Don Quixote' — a comic picaresque about an old gentleman addicted to chivalric romances that became a monument of world literature. He died on the same calendar date as Shakespeare — April 23, 1616.",
     "Q5682"),

    ("shakespeare", "威廉·莎士比亚", "William Shakespeare", 1564, 1616, "england",
     "文学,戏剧,诗歌", "Literature,Drama,Poetry",
     "英国最伟大的剧作家和诗人，创作了《哈姆雷特》《李尔王》《罗密欧与朱丽叶》等不朽名作。",
     "England's greatest playwright and poet, author of immortal works including 'Hamlet,' 'King Lear,' and 'Romeo and Juliet.'",
     "莎士比亚出身英格兰埃文河畔斯特拉特福的一个手套商家庭。他移居伦敦后在剧院工作——先是演员，后来成为剧作家。他在约二十年间创作了37部戏剧和154首十四行诗。他的作品涵盖了喜剧、历史剧和悲剧，其对人性的深刻洞察和语言的创造力达到了英语文学的巅峰。《哈姆雷特》的'生存还是毁灭'、《麦克白》的'人生不过是个行走的影子'成为世界文化中最著名的文本。",
     "Shakespeare was born in Stratford-upon-Avon to a glover's family. He moved to London, working in the theater — first as an actor, then as a playwright. Over roughly two decades, he wrote 37 plays and 154 sonnets. His works span comedy, history, and tragedy, their profound insight into human nature and linguistic creativity reaching the summit of English literature. 'To be or not to be' from 'Hamlet' and 'Life's but a walking shadow' from 'Macbeth' are among the most famous texts in world culture.",
     "Q692"),

    ("goethe", "歌德", "Johann Wolfgang von Goethe", 1749, 1832, "europe",
     "文学,诗歌,哲学", "Literature,Poetry,Philosophy",
     "德国最伟大的文学巨匠，《浮士德》和《少年维特之烦恼》的作者，浪漫主义运动的先驱。",
     "Germany's greatest literary figure and author of 'Faust' and 'The Sorrows of Young Werther,' a pioneer of the Romantic movement.",
     "歌德26岁时出版的《少年维特之烦恼》引发了席卷欧洲的'维特热'——据说不少年轻人效仿维特的自杀。他的毕生之作《浮士德》耗费了六十年——讲述了一个学者与魔鬼梅菲斯特缔约的故事，探讨了知识的限度和人类追求的意义。他同时是科学家——发现了人类颌间骨，提出了色彩理论。他与席勒的友谊和合作定义了德国的古典文学时代。",
     "Goethe's 'The Sorrows of Young Werther,' published when he was 26, sparked a 'Werther fever' across Europe — some young people reportedly imitated Werther's suicide. His lifelong project 'Faust,' completed over sixty years, tells of a scholar's pact with the devil Mephistopheles, exploring the limits of knowledge and the meaning of human striving. He was also a scientist — discovering the human intermaxillary bone and proposing a theory of color. His friendship and collaboration with Schiller defined Germany's classical literary era.",
     ""),

    ("tolstoy", "列夫·托尔斯泰", "Leo Tolstoy", 1828, 1910, "europe",
     "文学,小说,哲学,俄罗斯", "Literature,Novel,Philosophy,Russia",
     "俄国作家，《战争与和平》和《安娜·卡列尼娜》的作者，被公认为最伟大的小说家之一。",
     "Russian author of 'War and Peace' and 'Anna Karenina,' widely regarded as one of the greatest novelists of all time.",
     "托尔斯泰出身贵族，年轻时过着放荡的生活——赌博、决斗、从军。高加索和克里米亚战争的经历使他开始思考生命的意义。50岁后他经历了深刻的精神危机——几乎自杀——最终走向了基督教无政府主义和平主义。他放弃财产和版权，穿着农民的衣服劳动，其庄园雅斯纳亚·波良纳成为了全世界托尔斯泰主义者的朝圣地。1910年他以82岁高龄离家出走，死在了一个小火车站。",
     "Born to the aristocracy, Tolstoy lived a wild youth — gambling, dueling, soldiering. His experiences in the Caucasus and Crimean War led him to question life's meaning. After 50, he underwent a profound spiritual crisis — nearly suicidal — ultimately embracing Christian anarchism and pacifism. He renounced property and copyrights, labored in peasant clothes, and his estate Yasnaya Polyana became a pilgrimage site for Tolstoyans worldwide. In 1910, at 82, he fled home and died at a small railway station.",
     "Q7243"),

    ("mozart", "莫扎特", "Wolfgang Amadeus Mozart", 1756, 1791, "europe",
     "音乐,古典,作曲", "Music,Classical,Composition",
     "奥地利作曲家，古典主义音乐的代表人物，以神童之姿创作了600多部作品。",
     "Austrian composer and the supreme figure of Classical music, who produced over 600 works with prodigious genius.",
     "莫扎特3岁弹琴、5岁作曲、6岁开始欧洲巡演——音乐史上罕见的神童。他创作了歌剧《费加罗的婚礼》《唐璜》《魔笛》和41部交响曲。他的音乐以完美的形式、深邃的情感和自然的优雅著称——连对手萨列里也由衷敬佩。但他不善理财，35岁在贫困中去世，被葬于维也纳的一个无标记的公共墓地——这位璀璨天才的结局令人唏嘘。",
     "Mozart played piano at 3, composed at 5, and toured Europe at 6 — a child prodigy unrivaled in music history. He composed operas including 'The Marriage of Figaro,' 'Don Giovanni,' 'The Magic Flute,' and 41 symphonies. His music is celebrated for its perfect form, profound emotion, and natural grace — even his rival Salieri genuinely admired him. But he managed money poorly and died in poverty at 35, buried in an unmarked common grave in Vienna — a poignant end for such a brilliant genius.",
     ""),

    ("beethoven", "贝多芬", "Ludwig van Beethoven", 1770, 1827, "europe",
     "音乐,古典,浪漫,作曲", "Music,Classical,Romantic,Composition",
     "德国作曲家，古典主义与浪漫主义过渡时期的巨人，在逐渐失明失聪中创作了最具震撼力的音乐。",
     "German composer and the titan bridging Classicism and Romanticism, who created his most powerful music while progressively going deaf.",
     "贝多芬二十多岁时开始失去听力——对他这种天性的音乐家来说是毁灭性的打击。他在著名的《海利根施塔特遗书》中倾诉了绝望——但选择了'扼住命运的咽喉'继续创作。他的九部交响曲——尤其是'英雄'、'命运'和'合唱'——彻底改变了交响曲的创作方式。晚年的弦乐四重奏探索了人类灵魂最深处的领域。1827年他去世时，三万人参加了维也纳的葬礼。",
     "Beethoven began losing his hearing in his late twenties — a devastating blow for a musician of his nature. He poured his despair into the famous 'Heiligenstadt Testament' — then chose to 'seize fate by the throat' and continue composing. His nine symphonies — especially the 'Eroica,' 'Fate,' and 'Choral' — fundamentally transformed symphonic composition. His late string quartets explore the deepest regions of the human soul. When he died in 1827, 30,000 attended his Vienna funeral.",
     ""),
]

# Generate people from data
people = []
for item in data:
    (pid, name, nameEn, birth, death, rid, tags_str, tagsEn_str, 
     summary, summaryEn, desc, descEn, wikidata) = item
    people.append({
        "id": pid, "name": name, "nameEn": nameEn,
        "birthYear": birth, "deathYear": death,
        "regionId": rid,
        "tags": [t.strip() for t in tags_str.split(",")],
        "tagsEn": [t.strip() for t in tagsEn_str.split(",")],
        "summary": summary, "summaryEn": summaryEn,
        "description": desc, "descriptionEn": descEn,
        "alternativeNames": [],
        "sourceIds": [],
        "wikidataQid": wikidata,
        "dataStatus": "published",
        "confidenceScore": 0.9,
        "externalReferences": []
    })

print(f"// Total generated: {len(people)} people", file=sys.stderr)

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
print("\n// Total: %d new people (batch 8)" % len(people))
