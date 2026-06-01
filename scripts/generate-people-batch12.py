#!/usr/bin/env python3
import sys
def esc(s): return s.replace("\\\\", "\\\\\\\\").replace("'", "\\'")
data = [
("meitner-lise", "迈特纳", "Lise Meitner", 1878, 1968, "europe", "科学,物理,核裂变,女性", "Science,Physics,Nuclear Fission,Women", "奥地利-瑞典物理学家，与哈恩共同发现核裂变但诺贝尔奖只颁给了哈恩。", "Austrian-Swedish physicist who co-discovered nuclear fission with Hahn, but the Nobel went to Hahn alone."),
("noether", "诺特", "Emmy Noether", 1882, 1935, "europe", "数学,物理,女性", "Mathematics,Physics,Women", "德国数学家，诺特定理揭示了对称性与守恒定律之间的深刻联系，被誉为最伟大的女数学家。", "German mathematician whose Noether\'s Theorem revealed the profound link between symmetry and conservation laws."),
("hypatia", "希帕提娅", "Hypatia", 370, 415, "europe", "数学,哲学,女性,古希腊", "Mathematics,Philosophy,Women,Ancient Greece", "古埃及希腊裔女数学家、天文学家和哲学家，在古代世界最黑暗的时期守护了古典学问。", "Ancient Egyptian-Greek woman mathematician, astronomer, and philosopher who preserved classical learning in antiquity\'s darkest period."),
("babbage", "巴贝奇", "Charles Babbage", 1791, 1871, "england", "数学,计算机,发明", "Mathematics,Computer,Invention", "英国数学家，设计了差分机和分析机，被公认为计算机之父。", "English mathematician who designed the Difference Engine and Analytical Engine, widely regarded as the father of computing."),
("planck-max", "普朗克", "Max Planck", 1858, 1947, "europe", "科学,物理,量子,诺贝尔", "Science,Physics,Quantum,Nobel", "德国物理学家，量子理论的创始人，提出能量量子化的概念。", "German physicist and originator of quantum theory, who introduced the concept of energy quantization."),
("bohr-niels", "玻尔", "Niels Bohr", 1885, 1962, "europe", "科学,物理,量子力学,诺贝尔", "Science,Physics,Quantum Mechanics,Nobel", "丹麦物理学家，量子力学的奠基人之一，提出了原子结构的玻尔模型。", "Danish physicist and co-founder of quantum mechanics, who proposed the Bohr model of atomic structure."),
("dirac-paul", "狄拉克", "Paul Dirac", 1902, 1984, "england", "科学,物理,量子力学,诺贝尔", "Science,Physics,Quantum Mechanics,Nobel", "英国理论物理学家，预言了反物质的存在，量子电动力学的先驱。", "British theoretical physicist who predicted antimatter, a pioneer of quantum electrodynamics."),
("de-broglie", "德布罗意", "Louis de Broglie", 1892, 1987, "europe", "科学,物理,波粒二象性,诺贝尔", "Science,Physics,Wave-Particle Duality,Nobel", "法国物理学家，提出物质波理论，揭示了所有物质具有波粒二象性。", "French physicist who proposed matter wave theory, revealing that all matter exhibits wave-particle duality."),
("pauli", "泡利", "Wolfgang Pauli", 1900, 1958, "europe", "科学,物理,泡利不相容原理,诺贝尔", "Science,Physics,Pauli Exclusion Principle,Nobel", "奥地利物理学家，提出泡利不相容原理，预言了中微子的存在。", "Austrian physicist who proposed the Pauli exclusion principle and predicted the existence of the neutrino."),
("born-max", "玻恩", "Max Born", 1882, 1970, "europe", "科学,物理,量子力学,诺贝尔", "Science,Physics,Quantum Mechanics,Nobel", "德国物理学家，对量子力学的统计诠释做出了关键贡献。", "German physicist who made crucial contributions to the statistical interpretation of quantum mechanics."),
("thales", "泰勒斯", "Thales of Miletus", -624, -546, "europe", "哲学,数学,古希腊", "Philosophy,Mathematics,Ancient Greece", "古希腊哲学家和数学家，被认为是最早的西方哲学家，预测了公元前585年的日食。", "Ancient Greek philosopher and mathematician, considered the first Western philosopher, who predicted a solar eclipse in 585 BCE."),
("anaximander", "阿那克西曼德", "Anaximander", -610, -546, "europe", "哲学,科学,古希腊", "Philosophy,Science,Ancient Greece", "古希腊哲学家，制作了最早的世界地图，提出宇宙起源于无定形的无限。", "Ancient Greek philosopher who created the earliest world map and proposed the universe originated from the boundless."),
("parmenides", "巴门尼德", "Parmenides", -515, -450, "europe", "哲学,古希腊", "Philosophy,Ancient Greece", "古希腊哲学家，提出存在是一、不变和永恒的理论，深刻影响了柏拉图和西方形而上学。", "Ancient Greek philosopher who argued being is one, unchanging, and eternal, profoundly influencing Plato and Western metaphysics."),
("zeno-elea", "芝诺", "Zeno of Elea", -490, -430, "europe", "哲学,数学,悖论,古希腊", "Philosophy,Mathematics,Paradoxes,Ancient Greece", "古希腊哲学家，以阿喀琉斯与乌龟等著名悖论探讨了无限与运动的本质。", "Ancient Greek philosopher who explored infinity and motion through famous paradoxes like Achilles and the tortoise."),
("empedocles", "恩培多克勒", "Empedocles", -494, -434, "europe", "哲学,科学,古希腊", "Philosophy,Science,Ancient Greece", "古希腊哲学家，提出四元素说（土、水、气、火），认为爱和斗争是宇宙的动力。", "Ancient Greek philosopher who proposed the four-element theory (earth, water, air, fire) and held love and strife as cosmic forces."),
("protagoras", "普罗泰戈拉", "Protagoras", -490, -420, "europe", "哲学,智者,古希腊", "Philosophy,Sophist,Ancient Greece", "古希腊智者，提出人是万物的尺度，是最早的相对主义者。", "Ancient Greek sophist who declared man is the measure of all things, the earliest relativist."),
("epicurus", "伊壁鸠鲁", "Epicurus", -341, -270, "europe", "哲学,快乐主义,古希腊", "Philosophy,Hedonism,Ancient Greece", "古希腊哲学家，伊壁鸠鲁学派的创始人，主张通过追求心灵的宁静而非肉体享乐来获得幸福。", "Ancient Greek philosopher and founder of Epicureanism, who advocated happiness through mental tranquility rather than physical pleasure."),
("zeno-citium", "芝诺（斯多葛）", "Zeno of Citium", -334, -262, "europe", "哲学,斯多葛主义,古希腊", "Philosophy,Stoicism,Ancient Greece", "斯多葛学派的创始人，在雅典的彩绘柱廊下授徒，主张顺应自然和理性生活。", "Founder of Stoicism, who taught at Athens\' Painted Porch, advocating living in accordance with nature and reason."),
("lucretius", "卢克莱修", "Lucretius", -99, -55, "roman-empire", "哲学,诗歌,伊壁鸠鲁", "Philosophy,Poetry,Epicureanism", "罗马诗人和哲学家，《物性论》以优美诗歌阐述了伊壁鸠鲁的原子论哲学。", "Roman poet and philosopher whose On the Nature of Things expounded Epicurean atomism in beautiful verse."),
("boethius", "波爱修斯", "Boethius", 480, 524, "roman-empire", "哲学,音乐,中世纪", "Philosophy,Music,Medieval", "罗马哲学家，在狱中等待处决时写下《哲学的慰藉》，是中世纪最具影响力的哲学著作之一。", "Roman philosopher who wrote The Consolation of Philosophy in prison awaiting execution, one of the Middle Ages\' most influential philosophical works."),
("duns-scotus", "邓斯·司各脱", "Duns Scotus", 1266, 1308, "europe", "哲学,神学,经院哲学", "Philosophy,Theology,Scholasticism", "中世纪苏格兰经院哲学家和神学家，精微博士，对自由意志和圣母无原罪说做出了重要贡献。", "Medieval Scottish scholastic philosopher and theologian, the Subtle Doctor, who made key contributions on free will and the Immaculate Conception."),
("ockham", "奥卡姆", "William of Ockham", 1287, 1347, "england", "哲学,逻辑,中世纪", "Philosophy,Logic,Medieval", "英国方济各会哲学家，以奥卡姆剃刀原则闻名：如无必要，勿增实体。", "English Franciscan philosopher famous for Ockham\'s Razor: entities should not be multiplied beyond necessity."),
("meister-eckhart", "埃克哈特", "Meister Eckhart", 1260, 1328, "europe", "宗教,神秘主义,中世纪", "Religion,Mysticism,Medieval", "德国神学家和神秘主义者，以关于灵魂与神合一的深刻论述著称。", "German theologian and mystic celebrated for his profound teachings on the soul\'s union with God."),
("john-wycliffe", "威克里夫", "John Wycliffe", 1328, 1384, "england", "宗教,改革,圣经翻译", "Religion,Reform,Bible Translation", "英国神学家，宗教改革的晨星，第一个将圣经全文翻译成英语的人。", "English theologian and morning star of the Reformation, the first to translate the complete Bible into English."),
("jan-hus", "胡斯", "Jan Hus", 1372, 1415, "europe", "宗教,改革,捷克", "Religion,Reform,Czech", "捷克宗教改革家，因批评天主教会而被康斯坦茨公会议判处火刑处死。", "Czech religious reformer burned at the stake by the Council of Constance for criticizing the Catholic Church."),
("francesco-petrarca", "彼特拉克", "Petrarch", 1304, 1374, "renaissance-europe", "文学,诗歌,人文主义", "Literature,Poetry,Humanism", "意大利学者和诗人，文艺复兴人文主义之父，以其献给劳拉的十四行诗闻名。", "Italian scholar and poet, father of Renaissance humanism, celebrated for his sonnets to Laura."),
("boccaccio", "薄伽丘", "Giovanni Boccaccio", 1313, 1375, "renaissance-europe", "文学,小说,意大利", "Literature,Novel,Italy", "意大利作家，《十日谈》的作者，与但丁、彼特拉克并称意大利文学三杰。", "Italian writer and author of The Decameron, alongside Dante and Petrarch as one of Italy\'s three literary crowns."),
("el-greco", "埃尔·格列柯", "El Greco", 1541, 1614, "europe", "艺术,绘画,西班牙", "Art,Painting,Spain", "希腊裔西班牙画家，以修长的人体和强烈的宗教情感为特征的表现主义先驱。", "Greek-Spanish painter and precursor of Expressionism, characterized by elongated figures and intense religious emotion."),
("jan-van-eyck", "凡·艾克", "Jan van Eyck", 1390, 1441, "europe", "艺术,绘画,尼德兰", "Art,Painting,Netherlandish", "尼德兰画家，油画的完善者，《根特祭坛画》的创作者。", "Netherlandish painter who perfected oil painting technique, creator of the Ghent Altarpiece."),
("bruegel", "勃鲁盖尔", "Pieter Bruegel the Elder", 1525, 1569, "europe", "艺术,绘画,尼德兰", "Art,Painting,Netherlandish", "尼德兰文艺复兴画家，以描绘农民生活和风景著称，《巴别塔》是其代表作。", "Netherlandish Renaissance painter celebrated for peasant scenes and landscapes, with The Tower of Babel as his masterpiece."),
("bernini", "贝尼尼", "Gian Lorenzo Bernini", 1598, 1680, "europe", "艺术,雕塑,建筑,巴洛克", "Art,Sculpture,Architecture,Baroque", "意大利巴洛克雕塑家和建筑师，圣彼得广场和《圣特蕾莎的狂喜》的创作者。", "Italian Baroque sculptor and architect, creator of St. Peter\'s Square and The Ecstasy of Saint Teresa."),
("rubens", "鲁本斯", "Peter Paul Rubens", 1577, 1640, "europe", "艺术,绘画,巴洛克", "Art,Painting,Baroque", "佛兰德斯巴洛克画家，以丰满的人体和宗教神话题材的宏大场景著称。", "Flemish Baroque painter celebrated for voluptuous figures and grand mythological and religious scenes."),
("velazquez", "委拉斯开兹", "Diego Velazquez", 1599, 1660, "europe", "艺术,绘画,西班牙,巴洛克", "Art,Painting,Spain,Baroque", "西班牙巴洛克画家，《宫娥》的创作者，被誉为画家中的画家。", "Spanish Baroque painter and creator of Las Meninas, hailed as the painter of painters."),
("titian", "提香", "Titian", 1488, 1576, "renaissance-europe", "艺术,绘画,威尼斯", "Art,Painting,Venetian", "意大利威尼斯画派最伟大的画家，以对色彩的革新性运用和对人物心理的深刻描绘著称。", "The greatest painter of the Venetian school, celebrated for his revolutionary use of color and profound psychological portraiture."),
("botticelli", "波提切利", "Sandro Botticelli", 1445, 1510, "renaissance-europe", "艺术,绘画,佛罗伦萨", "Art,Painting,Florentine", "意大利文艺复兴画家，《春》和《维纳斯的诞生》是最具代表性的文艺复兴作品之一。", "Italian Renaissance painter whose Primavera and The Birth of Venus are among the most iconic Renaissance works."),
("giotto", "乔托", "Giotto di Bondone", 1267, 1337, "renaissance-europe", "艺术,绘画,意大利", "Art,Painting,Italy", "意大利画家和建筑师，被认为是最早摆脱拜占庭僵化风格、开创文艺复兴绘画的艺术家。", "Italian painter and architect, considered the first to break from Byzantine rigidity and pioneer Renaissance painting."),
("donatello", "多纳泰罗", "Donatello", 1386, 1466, "renaissance-europe", "艺术,雕塑,佛罗伦萨", "Art,Sculpture,Florentine", "意大利文艺复兴雕塑家，复兴了古典雕塑的独立人体表现，《大卫》是其代表作。", "Italian Renaissance sculptor who revived classical free-standing nude sculpture, with David as his masterwork."),
("masaccio", "马萨乔", "Masaccio", 1401, 1428, "renaissance-europe", "艺术,绘画,佛罗伦萨", "Art,Painting,Florentine", "意大利文艺复兴画家，最早系统地运用透视法，在27岁早逝前已改变了绘画的面貌。", "Italian Renaissance painter and the first to systematically use perspective, who transformed painting before his early death at 27."),
("piero-francesca", "皮耶罗·德拉·弗朗切斯卡", "Piero della Francesca", 1415, 1492, "renaissance-europe", "艺术,数学,透视", "Art,Mathematics,Perspective", "意大利文艺复兴画家和数学家，以对几何透视的精确运用和宁静庄严的风格著称。", "Italian Renaissance painter and mathematician celebrated for his precise geometric perspective and serene, monumental style."),
("mantegna", "曼特尼亚", "Andrea Mantegna", 1431, 1506, "renaissance-europe", "艺术,绘画,透视", "Art,Painting,Perspective", "意大利文艺复兴画家，以大胆的透视缩短技法和对古典考古学的精通著称。", "Italian Renaissance painter celebrated for his daring foreshortening technique and deep knowledge of classical archaeology."),
("bellini-giovanni", "贝利尼", "Giovanni Bellini", 1430, 1516, "renaissance-europe", "艺术,绘画,威尼斯", "Art,Painting,Venetian", "意大利威尼斯画派的奠基人，其色彩和光影的革新为乔尔乔内和提香铺平了道路。", "Founder of the Venetian school of painting, whose innovations in color and light paved the way for Giorgione and Titian."),
("correggio", "科雷乔", "Correggio", 1489, 1534, "renaissance-europe", "艺术,绘画,帕尔马", "Art,Painting,Parma", "意大利文艺复兴画家，以对天顶画透视的惊人掌控和感官性的人物描绘著称。", "Italian Renaissance painter celebrated for his astonishing mastery of ceiling perspective and sensuous figure painting."),
("holbein", "霍尔拜因", "Hans Holbein the Younger", 1497, 1543, "renaissance-europe", "艺术,绘画,肖像", "Art,Painting,Portraiture", "德国文艺复兴画家，以精确写实的肖像画著称，长期担任英王亨利八世的宫廷画师。", "German Renaissance painter celebrated for his precise, realistic portraiture, long serving as court painter to Henry VIII of England."),
("vermeer", "维米尔", "Johannes Vermeer", 1632, 1675, "europe", "艺术,绘画,荷兰", "Art,Painting,Dutch", "荷兰黄金时代画家，《戴珍珠耳环的少女》和《倒牛奶的女仆》的作者，光影的大师。", "Dutch Golden Age painter of Girl with a Pearl Earring and The Milkmaid, a master of light."),
("toulouse-lautrec", "劳特累克", "Henri de Toulouse-Lautrec", 1864, 1901, "europe", "艺术,绘画,海报,法国", "Art,Painting,Poster,France", "法国后印象派画家，以对巴黎蒙马特夜生活的生动描绘和开创性的海报艺术著称。", "French Post-Impressionist painter celebrated for his vivid depictions of Montmartre nightlife and pioneering poster art."),
("modigliani", "莫迪利亚尼", "Amedeo Modigliani", 1884, 1920, "europe", "艺术,绘画,雕塑", "Art,Painting,Sculpture", "意大利画家和雕塑家，以修长的肖像画和忧郁的女性裸体著称，35岁英年早逝。", "Italian painter and sculptor celebrated for his elongated portraits and melancholic female nudes, who died tragically at 35."),
("marcel-duchamp", "杜尚", "Marcel Duchamp", 1887, 1968, "europe", "艺术,达达主义,现成品", "Art,Dada,Readymade", "法裔美国艺术家，以小便池《泉》等现成品彻底颠覆了艺术的概念。", "French-American artist who radically subverted the concept of art through readymades like the urinal Fountain."),
("mondrian", "蒙德里安", "Piet Mondrian", 1872, 1944, "europe", "艺术,绘画,抽象", "Art,Painting,Abstract", "荷兰画家，风格派创始人之一，以红黄蓝黑白方块构成的纯粹抽象绘画著称。", "Dutch painter and co-founder of De Stijl, celebrated for pure abstract compositions of red, yellow, blue, black, and white blocks."),
("kandinsky", "康定斯基", "Wassily Kandinsky", 1866, 1944, "europe", "艺术,绘画,抽象", "Art,Painting,Abstract", "俄罗斯画家，抽象艺术的先驱，将色彩和形式从具象表现中彻底解放。", "Russian painter and pioneer of abstract art, who liberated color and form from representational depiction."),
("klee", "克利", "Paul Klee", 1879, 1940, "europe", "艺术,绘画,包豪斯", "Art,Painting,Bauhaus", "瑞士裔德国画家，以梦幻般的抽象构图和在包豪斯的教学影响了现代艺术的发展。", "Swiss-German painter whose dreamlike abstract compositions and teaching at the Bauhaus shaped modern art\'s development."),
("munch", "蒙克", "Edvard Munch", 1863, 1944, "europe", "艺术,绘画,表现主义", "Art,Painting,Expressionism", "挪威画家，《呐喊》的创作者，表现主义的先驱，以对焦虑和死亡的心理探索著称。", "Norwegian painter and creator of The Scream, a pioneer of Expressionism celebrated for his psychological exploration of anxiety and death."),
("seurat", "修拉", "Georges Seurat", 1859, 1891, "europe", "艺术,绘画,点彩派", "Art,Painting,Pointillism", "法国后印象派画家，点彩派的创始人，《大碗岛的星期天下午》是点描法的巅峰之作。", "French Post-Impressionist painter and founder of Pointillism, whose A Sunday Afternoon on the Island of La Grande Jatte is the apogee of the dot technique."),
("gauguin", "高更", "Paul Gauguin", 1848, 1903, "europe", "艺术,绘画,后印象派", "Art,Painting,Post-Impressionism", "法国后印象派画家，放弃文明社会前往塔希提，以鲜艳色彩和原始风格革新了现代艺术。", "French Post-Impressionist painter who abandoned civilization for Tahiti, revolutionizing modern art with vivid colors and primitivist style."),
("matisse", "马蒂斯", "Henri Matisse", 1869, 1954, "europe", "艺术,绘画,野兽派", "Art,Painting,Fauvism", "法国画家，野兽派的创始人，以对色彩的大胆解放和晚年剪纸艺术著称。", "French painter and founder of Fauvism, celebrated for his bold liberation of color and late-life paper cutouts."),
("klimt", "克里姆特", "Gustav Klimt", 1862, 1918, "europe", "艺术,绘画,分离派", "Art,Painting,Secession", "奥地利象征主义画家，《吻》的创作者，以金箔和华丽的装饰图案著称。", "Austrian Symbolist painter and creator of The Kiss, celebrated for gold leaf and ornate decorative patterns."),
("rodin", "罗丹", "Auguste Rodin", 1840, 1917, "europe", "艺术,雕塑,法国", "Art,Sculpture,France", "法国雕塑家，现代雕塑之父，《思想者》和《地狱之门》的创作者。", "French sculptor and father of modern sculpture, creator of The Thinker and The Gates of Hell."),
("michelangelo-b", "布纳罗蒂", "Michelangelo Buonarroti", 1475, 1564, "renaissance-europe", "艺术,雕塑,绘画,建筑", "Art,Sculpture,Painting,Architecture", "意大利文艺复兴三杰之一，《大卫》和西斯廷教堂天顶画的创作者。", "One of the three giants of Italian Renaissance, creator of David and the Sistine Chapel ceiling."),
("volta", "伏打", "Alessandro Volta", 1745, 1827, "europe", "科学,物理,电学", "Science,Physics,Electricity", "意大利物理学家，发明了世界上第一个电池（伏打电堆），电压单位伏特以他命名。", "Italian physicist who invented the first electric battery (voltaic pile), after whom the volt is named."),
("ohm", "欧姆", "Georg Ohm", 1789, 1854, "europe", "科学,物理,电学", "Science,Physics,Electricity", "德国物理学家，发现了欧姆定律，描述了电流、电压和电阻之间的关系。", "German physicist who discovered Ohm\'s Law, describing the relationship between current, voltage, and resistance."),
("ampere", "安培", "Andre-Marie Ampere", 1775, 1836, "europe", "科学,物理,电磁学", "Science,Physics,Electromagnetism", "法国物理学家，电动力学之父，电流单位安培以他命名。", "French physicist and father of electrodynamics, after whom the ampere is named."),
("coulomb", "库仑", "Charles-Augustin de Coulomb", 1736, 1806, "europe", "科学,物理,电学", "Science,Physics,Electricity", "法国物理学家，发现了库仑定律，描述了电荷间的作用力。", "French physicist who discovered Coulomb\'s Law, describing the force between electric charges."),
("robert-hooke", "胡克", "Robert Hooke", 1635, 1703, "england", "科学,物理,生物,显微", "Science,Physics,Biology,Microscopy", "英国博学家，用显微镜发现了细胞，提出了弹性定律，与牛顿在引力问题上激烈争论。", "English polymath who discovered cells with his microscope, proposed Hooke\'s Law of elasticity, and fiercely disputed with Newton over gravitation."),
("tycho", "第谷", "Tycho Brahe", 1546, 1601, "europe", "科学,天文学", "Science,Astronomy", "丹麦天文学家，进行了前望远镜时代最精确的天文观测，其数据成为开普勒三大定律的基础。", "Danish astronomer who made the most precise pre-telescope observations, his data forming the basis for Kepler\'s three laws."),
("kelvin", "开尔文", "Lord Kelvin (William Thomson)", 1824, 1907, "england", "科学,物理,热力学", "Science,Physics,Thermodynamics", "英国物理学家，提出了绝对温标（开氏温标），在大西洋电缆铺设和热力学方面做出重要贡献。", "British physicist who proposed the absolute temperature scale (Kelvin), making key contributions to Atlantic cabling and thermodynamics."),
("boltzmann", "玻尔兹曼", "Ludwig Boltzmann", 1844, 1906, "europe", "科学,物理,统计力学", "Science,Physics,Statistical Mechanics", "奥地利物理学家，统计力学之父，用概率解释了热力学第二定律。", "Austrian physicist and father of statistical mechanics, who explained the second law of thermodynamics through probability."),
("edwin-land", "兰德", "Edwin Land", 1909, 1991, "americas", "发明,摄影,宝丽来", "Invention,Photography,Polaroid", "美国发明家，宝丽来即时相机的发明者，持有超过500项专利。", "American inventor of the Polaroid instant camera, holder of over 500 patents."),
("berners-lee", "伯纳斯-李", "Tim Berners-Lee", 1955, None, "england", "发明,互联网,万维网", "Invention,Internet,World Wide Web", "英国计算机科学家，万维网的发明者，无偿将这一改变世界的技术贡献给全人类。", "British computer scientist and inventor of the World Wide Web, who freely gave this world-changing technology to humanity."),
("shannon", "香农", "Claude Shannon", 1916, 2001, "americas", "科学,信息论,数学", "Science,Information Theory,Mathematics", "美国数学家和工程师，信息论之父，将信息量化为比特，奠定了数字时代的基础。", "American mathematician and engineer, father of information theory, who quantified information in bits, laying the foundation for the digital age."),
("nash", "纳什", "John Nash", 1928, 2015, "americas", "数学,博弈论,诺贝尔", "Mathematics,Game Theory,Nobel", "美国数学家，提出了纳什均衡，深刻改变了经济学和博弈论，与精神分裂症抗争数十年。", "American mathematician who proposed Nash equilibrium, profoundly transforming economics and game theory, while battling schizophrenia for decades."),
("mandelbrot", "曼德博", "Benoit Mandelbrot", 1924, 2010, "europe", "数学,分形几何", "Mathematics,Fractal Geometry", "波兰裔法国数学家，分形几何的创始人，揭示了自然界中自相似模式的数学之美。", "Polish-French mathematician and founder of fractal geometry, who revealed the mathematical beauty of self-similar patterns in nature."),
("goodall-jane", "古道尔", "Jane Goodall", 1934, None, "england", "科学,灵长类学,动物保护", "Science,Primatology,Animal Conservation", "英国灵长类动物学家，以在坦桑尼亚对黑猩猩长达60年的革命性研究奠定了灵长类学。", "British primatologist whose revolutionary 60-year study of chimpanzees in Tanzania founded modern primatology."),
("fossey", "弗西", "Dian Fossey", 1932, 1985, "americas", "科学,灵长类学,动物保护", "Science,Primatology,Animal Conservation", "美国灵长类动物学家，以在卢旺达对山地大猩猩的研究和保护工作而闻名，1985年被谋杀。", "American primatologist known for her study and conservation of mountain gorillas in Rwanda, murdered in 1985."),
("nadar", "纳达尔", "Nadar (Gaspard-Felix Tournachon)", 1820, 1910, "europe", "摄影,艺术,肖像", "Photography,Art,Portrait", "法国摄影师和漫画家，开创了人像摄影和航空摄影的先河。", "French photographer and caricaturist who pioneered portrait photography and aerial photography."),
("ansel-adams", "安塞尔·亚当斯", "Ansel Adams", 1902, 1984, "americas", "摄影,环境,美国", "Photography,Environment,USA", "美国摄影师和环保主义者，以美国西部特别是优胜美地的黑白风景照片著称。", "American photographer and environmentalist celebrated for his black-and-white landscapes of the American West, especially Yosemite."),
("cartier-bresson", "布列松", "Henri Cartier-Bresson", 1908, 2004, "europe", "摄影,纪实", "Photography,Documentary", "法国摄影师，现代新闻摄影之父，马格南图片社联合创始人，以决定性瞬间的概念著称。", "French photographer and father of modern photojournalism, Magnum Photos co-founder, celebrated for the concept of the decisive moment."),
]
people = []
for item in data:
    (pid, name, nameEn, birth, death, rid, tags_str, tagsEn_str, summary, summaryEn) = item[:10]
    death_str = str(death) if death is not None else 'undefined'
    people.append({"id": pid, "name": name, "nameEn": nameEn, "birthYear": birth, "deathYear": death, "deathStr": death_str, "regionId": rid, "tags": tags_str.split(","), "tagsEn": tagsEn_str.split(","), "summary": summary, "summaryEn": summaryEn})
lines = []
for p in people:
    l = []
    l.append("  // --- %s ---" % p["nameEn"])
    l.append("  {")
    l.append("    id: '%s'," % esc(p["id"]))
    l.append("    name: '%s'," % esc(p["name"]))
    l.append("    nameEn: '%s'," % esc(p["nameEn"]))
    l.append("    birthYear: %s," % p["birthYear"])
    l.append("    deathYear: %s," % p["deathStr"])
    l.append("    regionId: '%s'," % p["regionId"])
    l.append("    alternativeNames: [],")
    l.append("    tags: [%s]," % ", ".join("'%s'" % esc(t.strip()) for t in p["tags"]))
    l.append("    tagsEn: [%s]," % ", ".join("'%s'" % esc(t.strip()) for t in p["tagsEn"]))
    l.append("    summary: '%s'," % esc(p["summary"]))
    l.append("    summaryEn: '%s'," % esc(p["summaryEn"]))
    l.append("    description: '%s'," % esc(p["summary"]))
    l.append("    descriptionEn: '%s'," % esc(p["summaryEn"]))
    l.append("    sourceIds: [],")
    l.append("    occupations: [],")
    l.append("    birthDatePrecision: 'year' as const,")
    l.append("    deathDatePrecision: 'year' as const,")
    l.append("    dataStatus: 'published' as const,")
    l.append("    confidenceScore: 0.9,")
    l.append("    externalReferences: [],")
    l.append("  },")
    lines.append("\n".join(l))
print("\n\n".join(lines))
print("\n// Total: %d new people" % len(people))
