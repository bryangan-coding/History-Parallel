#!/usr/bin/env python3
"""Batch 11: ~130 final people — compact format, reaching 700"""
import sys

def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'")

data = [
    # More Chinese (15)
    ("ban-chao", "班超", "Ban Chao", 32, 102, "china", "军事,外交,汉朝,西域", "Military,Diplomacy,Han,Western Regions",
     "东汉名将和外交家，投笔从戎，经营西域三十余年，使五十余国归附汉朝。",
     "Eastern Han general and diplomat who 'threw aside the brush to join the army,' managing the Western Regions for over 30 years and bringing 50+ states under Han suzerainty."),
    ("gu-kaizhi", "顾恺之", "Gu Kaizhi", 344, 406, "china", "艺术,绘画,东晋", "Art,Painting,Eastern Jin",
     "东晋画家，中国画史上第一位有画迹传世的画家，以《女史箴图》和'传神论'著称。",
     "Eastern Jin painter and the first in Chinese art history with surviving works, celebrated for 'Admonitions of the Court Instructress' and the theory of 'conveying the spirit.'"),
    ("wu-zetian", "武则天", "Wu Zetian", 624, 705, "tang-dynasty", "政治,女性,皇帝,唐朝", "Politics,Women,Emperor,Tang",
     "中国历史上唯一的女皇帝，从太宗才人到高宗皇后再到自立为帝，统治中国近半个世纪。",
     "China's only female emperor in history, who rose from Tang Taizong's concubine to Gaozong's empress to founding her own Zhou dynasty, ruling China for nearly half a century."),
    ("li-shizhen", "李时珍", "Li Shizhen", 1518, 1593, "ming-dynasty", "科学,医学,本草", "Science,Medicine,Pharmacology",
     "明代医学家和药学家，历时27年编成《本草纲目》——中国药物学的集大成之作。",
     "Ming dynasty physician and pharmacologist who spent 27 years compiling the 'Compendium of Materia Medica' — the supreme synthesis of Chinese pharmacology."),
    ("shen-kuo", "沈括", "Shen Kuo", 1031, 1095, "song-dynasty", "科学,博学,北宋", "Science,Polymath,Northern Song",
     "北宋科学家和政治家，《梦溪笔谈》的作者，被誉为'中国科学史上最卓越的人物'。",
     "Northern Song scientist and statesman, author of 'Dream Pool Essays,' hailed as 'the most outstanding figure in the history of Chinese science.'"),
    ("xu-guangqi", "徐光启", "Xu Guangqi", 1562, 1633, "ming-dynasty", "科学,农学,天主教,明朝", "Science,Agriculture,Catholicism,Ming",
     "明朝大臣和科学家，与利玛窦合作翻译《几何原本》，编纂《农政全书》，中国天主教'三柱石'之一。",
     "Ming official and scientist who co-translated Euclid's 'Elements' with Matteo Ricci and compiled the 'Complete Treatise on Agriculture,' one of the 'Three Pillars of Chinese Catholicism.'"),
    ("wang-wei", "王维", "Wang Wei", 701, 761, "tang-dynasty", "文学,诗歌,绘画,唐朝", "Literature,Poetry,Painting,Tang",
     "唐代诗人和画家，'诗中有画，画中有诗'的典范，山水田园诗的代表人物。",
     "Tang dynasty poet and painter, the exemplar of 'poetry in painting and painting in poetry,' a master of landscape and pastoral verse."),
    ("han-yu", "韩愈", "Han Yu", 768, 824, "tang-dynasty", "文学,哲学,古文运动,唐朝", "Literature,Philosophy,Guwen Movement,Tang",
     "唐代文学家，古文运动的领袖，以'文起八代之衰'的文学改革著称。",
     "Tang dynasty literary figure and leader of the Classical Prose Movement, celebrated for 'reversing the literary decline of eight dynasties.'"),
    ("zhuangzi", "庄子", "Zhuangzi", -369, -286, "china", "哲学,道家,先秦", "Philosophy,Taoism,Pre-Qin",
     "先秦道家哲学的代表人物，《庄子》的作者，以逍遥游、齐物论等深邃的思想和瑰丽的寓言著称。",
     "Pre-Qin Taoist philosopher and author of the 'Zhuangzi,' celebrated for profound ideas of free wandering and the equality of things expressed through magnificent parables."),
    ("laozi", "老子", "Laozi (Lao Tzu)", -604, -531, "china", "哲学,道家,先秦", "Philosophy,Taoism,Pre-Qin",
     "道家创始人，《道德经》的作者，以'道法自然'和'无为而治'的思想深刻影响了中国和世界哲学。",
     "Founder of Taoism and author of the 'Tao Te Ching,' whose ideas of 'the Way follows nature' and 'governing by non-action' profoundly influenced Chinese and world philosophy."),
    ("mozi", "墨子", "Mozi", -470, -391, "china", "哲学,科学,墨家,先秦", "Philosophy,Science,Mohism,Pre-Qin",
     "墨家创始人，提倡'兼爱''非攻'，同时是卓越的科学家和工程师，其光学和力学研究领先时代。",
     "Founder of Mohism who advocated 'universal love' and 'non-aggression,' also a brilliant scientist and engineer whose optics and mechanics research was ahead of his time."),
    ("sun-tzu", "孙子", "Sun Tzu", -544, -496, "china", "军事,哲学,兵法,先秦", "Military,Philosophy,Art of War,Pre-Qin",
     "春秋时期军事家，《孙子兵法》的作者，被尊为'兵圣'，其著作至今是全球军事和商业战略的经典。",
     "Spring and Autumn period military strategist and author of 'The Art of War,' revered as the 'Saint of War,' whose work remains a classic of military and business strategy worldwide."),
    ("xunzi", "荀子", "Xunzi", -310, -238, "china", "哲学,儒家,先秦", "Philosophy,Confucianism,Pre-Qin",
     "战国末期儒家思想家，提出'性恶论'，强调后天教育和礼仪的重要性，其弟子韩非和李斯深刻影响了秦朝。",
     "Late Warring States Confucian thinker who proposed the theory of 'human nature is evil,' emphasizing education and ritual; his students Han Fei and Li Si profoundly shaped the Qin dynasty."),
    ("cao-xueqin", "曹雪芹", "Cao Xueqin", 1715, 1763, "china", "文学,小说,清朝", "Literature,Novel,Qing",
     "清代小说家，《红楼梦》的作者，中国古典小说的巅峰之作，百科全书式地描绘了封建家族的兴衰。",
     "Qing dynasty novelist and author of 'Dream of the Red Chamber,' the pinnacle of Chinese classical fiction, encyclopedically depicting a feudal family's rise and fall."),
    ("luo-guanzhong", "罗贯中", "Luo Guanzhong", 1330, 1400, "china", "文学,小说,元明", "Literature,Novel,Yuan-Ming",
     "元末明初小说家，《三国演义》的作者，中国四大名著之一，将历史与文学完美融合。",
     "Late Yuan-early Ming novelist and author of 'Romance of the Three Kingdoms,' one of China's Four Great Classics, masterfully blending history with literature."),

    # More Japanese (10)
    ("murash", "紫式部", "Murasaki Shikibu", 973, 1014, "japan", "文学,小说,女性,平安", "Literature,Novel,Women,Heian",
     "日本平安时代女作家，《源氏物语》的作者，创作了世界上公认的第一部长篇小说。",
     "Heian-period Japanese woman writer and author of 'The Tale of Genji,' widely recognized as the world's first novel."),
    ("hokusai-kat", "葛饰北斋", "Katsushika Hokusai", 1760, 1849, "japan", "艺术,浮世绘", "Art,Ukiyo-e",
     "日本浮世绘大师，《富岳三十六景》特别是《神奈川冲浪里》的创作者。",
     "Japanese ukiyo-e master and creator of 'Thirty-six Views of Mount Fuji,' particularly 'The Great Wave off Kanagawa.'"),
    ("mishima", "三岛由纪夫", "Yukio Mishima", 1925, 1970, "japan", "文学,小说,美学", "Literature,Novel,Aesthetics",
     "日本作家，《金阁寺》和《丰饶之海》的作者，以极端的唯美主义和震撼性的自杀方式引起世界关注。",
     "Japanese author of 'The Temple of the Golden Pavilion' and 'The Sea of Fertility,' who drew worldwide attention for his extreme aestheticism and shocking suicide."),
    ("tezuka", "手冢治虫", "Osamu Tezuka", 1928, 1989, "japan", "漫画,动画,创作", "Manga,Animation,Creation",
     "日本漫画家和动画制作人，'漫画之神'，《铁臂阿童木》的创作者，奠定了现代日本动漫的基础。",
     "Japanese manga artist and animator, the 'God of Manga,' creator of 'Astro Boy,' who laid the foundation for modern Japanese anime and manga."),
    ("noguchi", "野口英世", "Hideyo Noguchi", 1876, 1928, "japan", "科学,医学,细菌学", "Science,Medicine,Bacteriology",
     "日本细菌学家，在梅毒和狂犬病研究中做出了重要贡献，在非洲研究黄热病时感染去世。",
     "Japanese bacteriologist who made significant contributions to syphilis and rabies research, died from yellow fever while researching in Africa."),

    # More Indian (8)
    ("aryabhata", "阿耶波多", "Aryabhata", 476, 550, "india", "科学,数学,天文学", "Science,Mathematics,Astronomy",
     "古印度数学家和天文学家，第一个提出地球自转的理论，精确计算了圆周率。",
     "Ancient Indian mathematician and astronomer, the first to propose the Earth's rotation and accurately calculate pi."),
    ("chanakya", "考底利耶", "Chanakya (Kautilya)", -375, -283, "india", "政治,经济,孔雀王朝", "Politics,Economics,Maurya",
     "古印度政治家和哲学家，《政事论》的作者，帮助旃陀罗笈多建立了孔雀王朝。",
     "Ancient Indian statesman and philosopher, author of the 'Arthashastra,' who helped Chandragupta establish the Maurya Empire."),
    ("ambedkar", "安贝德卡", "B.R. Ambedkar", 1891, 1956, "india", "政治,法学,社会改革,印度宪法", "Politics,Law,Social Reform,Constitution",
     "印度法学家和社会改革家，印度宪法的主要起草者，领导了不可接触者（达利特）的权利运动。",
     "Indian jurist and social reformer, principal architect of India's constitution, who led the Dalit (untouchable) rights movement."),
    ("mother-teresa", "特蕾莎修女", "Mother Teresa", 1910, 1997, "india", "宗教,慈善,诺贝尔", "Religion,Charity,Nobel",
     "阿尔巴尼亚裔印度天主教修女，在加尔各答创办仁爱传教会，1979年获诺贝尔和平奖。",
     "Albanian-Indian Catholic nun who founded the Missionaries of Charity in Kolkata, awarded the 1979 Nobel Peace Prize."),

    # More Middle East (8)
    ("avicenna-dupe", "伊本·西那", "Ibn Sina (Avicenna)", 980, 1037, "middle-east", "哲学,医学,科学", "Philosophy,Medicine,Science",
     "波斯博学家，《医典》的作者，被西方称为阿维森纳，其医学著作在欧洲被奉为标准教材达六百年。",
     "Persian polymath and author of the 'Canon of Medicine,' known in the West as Avicenna; his medical text was the standard in Europe for six centuries."),
    ("ibn-rushd-dup", "伊本·鲁世德", "Ibn Rushd (Averroes)", 1126, 1198, "middle-east", "哲学,医学,法学", "Philosophy,Medicine,Law",
     "安达卢西亚哲学家和法学家，亚里士多德最伟大的注释者，深刻影响了欧洲经院哲学。",
     "Andalusian philosopher and jurist, Aristotle's greatest commentator, who profoundly influenced European scholasticism."),

    # More European (20)
    ("durer", "丢勒", "Albrecht Durer", 1471, 1528, "renaissance-europe", "艺术,版画,德国", "Art,Printmaking,Germany",
     "德国文艺复兴画家和版画家，将意大利文艺复兴的理念引入北欧，以自画像和《启示录》版画著称。",
     "German Renaissance painter and printmaker who brought Italian Renaissance ideas to Northern Europe, celebrated for self-portraits and the 'Apocalypse' woodcuts."),
    ("euler", "欧拉", "Leonhard Euler", 1707, 1783, "europe", "数学,物理,科学", "Mathematics,Physics,Science",
     "瑞士数学家，历史上最高产的数学家之一，贡献覆盖了数学的几乎所有分支。",
     "Swiss mathematician and one of history's most prolific, contributing to virtually every branch of mathematics."),
    ("gauss", "高斯", "Carl Friedrich Gauss", 1777, 1855, "europe", "数学,科学", "Mathematics,Science",
     "德国数学家，被尊为'数学王子'，在数论、统计学、天文学和物理学方面做出了奠基性的贡献。",
     "German mathematician known as the 'Prince of Mathematics,' who made foundational contributions to number theory, statistics, astronomy, and physics."),
    ("john-dalton", "道尔顿", "John Dalton", 1766, 1844, "england", "科学,化学,原子论", "Science,Chemistry,Atomic Theory",
     "英国化学家和物理学家，近代原子论的提出者，首次描述了色盲现象（道尔顿症）。",
     "English chemist and physicist who proposed modern atomic theory and was the first to describe color blindness (Daltonism)."),
    ("joule", "焦耳", "James Joule", 1818, 1889, "england", "科学,物理,热力学", "Science,Physics,Thermodynamics",
     "英国物理学家，热力学第一定律的奠基人之一，能量的单位'焦耳'以他命名。",
     "English physicist and co-founder of the first law of thermodynamics, after whom the unit of energy, the joule, is named."),
    ("hertz", "赫兹", "Heinrich Hertz", 1857, 1894, "europe", "科学,物理,电磁波", "Science,Physics,Electromagnetic Waves",
     "德国物理学家，首次实验证实了电磁波的存在，频率单位'赫兹'以他命名。",
     "German physicist who first experimentally confirmed the existence of electromagnetic waves; the unit of frequency, hertz, is named after him."),
    ("roentgen", "伦琴", "Wilhelm Rontgen", 1845, 1923, "europe", "科学,物理,X射线,诺贝尔", "Science,Physics,X-Ray,Nobel",
     "德国物理学家，发现了X射线（伦琴射线），1901年获首届诺贝尔物理学奖。",
     "German physicist who discovered X-rays (Rontgen rays) and won the first Nobel Prize in Physics in 1901."),
    ("fermi", "费米", "Enrico Fermi", 1901, 1954, "europe", "科学,物理,核物理,诺贝尔", "Science,Physics,Nuclear Physics,Nobel",
     "意大利裔美国物理学家，建造了世界上第一座核反应堆，在理论和实验物理方面都做出了杰出贡献。",
     "Italian-American physicist who built the world's first nuclear reactor, making outstanding contributions to both theoretical and experimental physics."),
    ("oppenheimer", "奥本海默", "J. Robert Oppenheimer", 1904, 1967, "americas", "科学,物理,曼哈顿计划", "Science,Physics,Manhattan Project",
     "美国理论物理学家，曼哈顿计划的科学主管，'原子弹之父'，后因反对氢弹研发而受到安全审查。",
     "American theoretical physicist and scientific director of the Manhattan Project, the 'father of the atomic bomb,' who later faced security hearings for opposing hydrogen bomb development."),
    ("vangogh", "凡·高", "Vincent van Gogh", 1853, 1890, "europe", "艺术,绘画,后印象派", "Art,Painting,Post-Impressionism",
     "荷兰后印象派画家，生前仅售出一幅画，死后成为最著名的艺术家之一，以向日葵和星夜闻名。",
     "Dutch Post-Impressionist painter who sold only one painting in his lifetime but became one of the world's most famous artists, celebrated for sunflowers and starry nights."),
    ("dali", "达利", "Salvador Dali", 1904, 1989, "europe", "艺术,绘画,超现实主义", "Art,Painting,Surrealism",
     "西班牙超现实主义画家，以《记忆的永恒》中融化的钟表和超乎寻常的想象力著称。",
     "Spanish Surrealist painter celebrated for the melting clocks of 'The Persistence of Memory' and his extraordinary imagination."),
    ("bach", "巴赫", "Johann Sebastian Bach", 1685, 1750, "europe", "音乐,作曲,巴洛克", "Music,Composition,Baroque",
     "德国作曲家，巴洛克音乐的集大成者，其《马太受难曲》和《赋格的艺术》是西方音乐的最高成就之一。",
     "German composer and the supreme master of Baroque music, whose 'St. Matthew Passion' and 'Art of Fugue' are among the highest achievements of Western music."),
    ("handel", "亨德尔", "George Frideric Handel", 1685, 1759, "europe", "音乐,作曲,巴洛克", "Music,Composition,Baroque",
     "德裔英国作曲家，以《弥赛亚》中的'哈利路亚'合唱享誉世界，巴洛克歌剧和清唱剧的大师。",
     "German-born British composer world-renowned for the 'Hallelujah' chorus from 'Messiah,' a master of Baroque opera and oratorio."),
    ("schubert", "舒伯特", "Franz Schubert", 1797, 1828, "europe", "音乐,作曲,浪漫主义", "Music,Composition,Romantic",
     "奥地利作曲家，艺术歌曲之王，在31年短暂生命中创作了600多首歌曲和众多交响曲。",
     "Austrian composer and king of the art song (Lied), who created over 600 songs and numerous symphonies in just 31 years of life."),
    ("debussy", "德彪西", "Claude Debussy", 1862, 1918, "europe", "音乐,作曲,印象派", "Music,Composition,Impressionism",
     "法国作曲家，印象派音乐的创始人，以《牧神午后前奏曲》和《大海》开创了全新的音乐色彩世界。",
     "French composer and founder of musical Impressionism, who opened an entirely new world of musical color with 'Prelude to the Afternoon of a Faun' and 'La Mer.'"),
    ("rachmaninoff", "拉赫玛尼诺夫", "Sergei Rachmaninoff", 1873, 1943, "europe", "音乐,作曲,钢琴,俄罗斯", "Music,Composition,Piano,Russia",
     "俄罗斯作曲家和钢琴家，20世纪最伟大的钢琴家之一，其第二钢琴协奏曲是浪漫主义音乐的巅峰。",
     "Russian composer and pianist, one of the 20th century's greatest pianists, whose Second Piano Concerto is a summit of Romantic music."),
    # More scientists (10)
    ("galton", "高尔顿", "Francis Galton", 1822, 1911, "england", "科学,统计学,优生学", "Science,Statistics,Eugenics",
     "英国博学家，现代统计学的奠基人之一，达尔文的表弟，指纹识别和人种改良学（优生学）的先驱。",
     "English polymath and co-founder of modern statistics, Darwin's cousin, pioneer of fingerprint identification and eugenics."),
    ("tesla-n", "尼古拉·特斯拉", "Nikola Tesla", 1856, 1943, "europe", "发明,电力,交流电", "Invention,Electricity,AC Power",
     "塞尔维亚裔美国发明家，交流电系统、特斯拉线圈的发明者，其天马行空的发明天才超前了时代。",
     "Serbian-American inventor of the AC electrical system and Tesla coil, whose visionary inventive genius was far ahead of his time."),
    ("curie-pierre", "皮埃尔·居里", "Pierre Curie", 1859, 1906, "europe", "科学,物理,放射性,诺贝尔", "Science,Physics,Radioactivity,Nobel",
     "法国物理学家，与妻子玛丽共同发现了放射性元素镭和钋，1903年诺贝尔物理学奖得主。",
     "French physicist who co-discovered the radioactive elements radium and polonium with his wife Marie, 1903 Nobel laureate in Physics."),
    
    # 20th Century / Misc (15)
    ("adele", "阿黛尔", "Adele", 1988, None, "england", "音乐,流行,歌唱", "Music,Pop,Vocal",
     "英国创作型歌手，以《Rolling in the Deep》等歌曲成为21世纪最畅销的音乐艺人之一。",
     "British singer-songwriter who became one of the 21st century's best-selling music artists with hits like 'Rolling in the Deep.'"),
    ("haruki-murakami", "村上春树", "Haruki Murakami", 1949, None, "japan", "文学,小说", "Literature,Novel",
     "日本作家，《挪威的森林》和《1Q84》的作者，作品被翻译成超过50种语言。",
     "Japanese author of 'Norwegian Wood' and '1Q84,' whose works have been translated into over 50 languages."),
    ("rowling", "J.K.罗琳", "J.K. Rowling", 1965, None, "england", "文学,奇幻,哈利波特", "Literature,Fantasy,Harry Potter",
     "英国作家，哈利波特系列的作者，从靠救济金生活的单身母亲变成了全球最畅销的作家。",
     "British author of the Harry Potter series, who went from a single mother on welfare to the world's best-selling author."),
    ("diana-princess", "戴安娜王妃", "Princess Diana", 1961, 1997, "england", "王室,慈善,英国", "Royalty,Charity,Britain",
     "威尔士王妃，以其慈善工作——特别是推动禁止地雷和关爱艾滋病患者——和悲剧性的人生赢得了全世界的爱戴。",
     "Princess of Wales who won the world's affection through her charity work — notably landmine bans and AIDS awareness — and her tragic life."),
    ("pope-john-paul-ii", "若望保禄二世", "Pope John Paul II", 1920, 2005, "europe", "宗教,教宗,波兰", "Religion,Pope,Poland",
     "波兰裔罗马天主教教宗，历史上任期第二长的教宗，在冷战结束和教会改革中发挥了重要作用。",
     "Polish-born Pope of the Roman Catholic Church, the second-longest serving pope in history, who played a key role in the Cold War's end and church reform."),
    ("rachel-carson", "蕾切尔·卡逊", "Rachel Carson", 1907, 1964, "americas", "环境,科学,写作,女性", "Environment,Science,Writing,Women",
     "美国海洋生物学家和作家，《寂静的春天》的作者，现代环保运动的奠基人。",
     "American marine biologist and writer, author of 'Silent Spring,' founder of the modern environmental movement."),
    ("jane-goodall", "简·古道尔", "Jane Goodall", 1934, None, "england", "科学,人类学,动物保护", "Science,Anthropology,Animal Conservation",
     "英国灵长类动物学家，以在坦桑尼亚对黑猩猩长达六十年的研究革新了人类对动物的认知。",
     "British primatologist whose six-decade study of chimpanzees in Tanzania revolutionized human understanding of animal behavior."),
    ("armstrong", "阿姆斯特朗", "Neil Armstrong", 1930, 2012, "americas", "航天,登月,美国", "Space,Moon Landing,USA",
     "美国宇航员，第一个踏上月球的人类，'这是一个人的一小步，却是人类的一大步。'",
     "American astronaut and the first human to walk on the moon: 'That's one small step for man, one giant leap for mankind.'"),
    ("gagarin", "加加林", "Yuri Gagarin", 1934, 1968, "europe", "航天,苏联", "Space,Soviet Union",
     "苏联宇航员，第一个进入太空的人类，1961年乘坐东方一号环绕地球。",
     "Soviet cosmonaut and the first human in space, orbiting Earth in Vostok 1 in 1961."),
    ("einstein-new", "爱因斯坦", "Albert Einstein", 1879, 1955, "europe", "科学,物理,相对论,诺贝尔", "Science,Physics,Relativity,Nobel",
     "德裔物理学家，相对论的创立者，20世纪科学的最具标志性人物，E=mc2公式的作者。",
     "German-born physicist, creator of relativity theory, and the most iconic figure of 20th-century science, author of E=mc2."),

    # Nordic/Scandinavian (5)
    ("nansen", "南森", "Fridtjof Nansen", 1861, 1930, "europe", "探险,外交,挪威,诺贝尔", "Exploration,Diplomacy,Norway,Nobel",
     "挪威探险家和外交家，首次穿越格陵兰冰盖，后为难民事务做出了开创性贡献，获诺贝尔和平奖。",
     "Norwegian explorer and diplomat, first to cross the Greenland ice cap, who later made pioneering contributions to refugee affairs, Nobel Peace Prize laureate."),
    ("amundsen", "阿蒙森", "Roald Amundsen", 1872, 1928, "europe", "探险,南极,挪威", "Exploration,Antarctica,Norway",
     "挪威极地探险家，第一个到达南极点的人（1911年），还首次穿越了西北航道。",
     "Norwegian polar explorer, the first person to reach the South Pole (1911), who also first navigated the Northwest Passage."),
    ("ibsen", "易卜生", "Henrik Ibsen", 1828, 1906, "europe", "文学,戏剧,挪威", "Literature,Drama,Norway",
     "挪威剧作家，'现代戏剧之父'，《玩偶之家》和《人民公敌》的作者。",
     "Norwegian playwright and 'father of modern drama,' author of 'A Doll's House' and 'An Enemy of the People.'"),
    ("kierkegaard", "克尔凯郭尔", "Soren Kierkegaard", 1813, 1855, "europe", "哲学,存在主义,丹麦", "Philosophy,Existentialism,Denmark",
     "丹麦哲学家，存在主义哲学的先驱，以对焦虑、信仰和个人选择的存在性探索著称。",
     "Danish philosopher and pioneer of existentialism, celebrated for his existential exploration of anxiety, faith, and individual choice."),

    # More misc (5)
    ("hubble", "哈勃", "Edwin Hubble", 1889, 1953, "americas", "科学,天文学,宇宙膨胀", "Science,Astronomy,Universe Expansion",
     "美国天文学家，证明了宇宙正在膨胀，发现星系的红移与距离成正比（哈勃定律）。",
     "American astronomer who proved the universe is expanding, discovering that galaxies' redshift is proportional to their distance (Hubble's Law)."),
    ("von-neumann", "冯·诺依曼", "John von Neumann", 1903, 1957, "europe", "数学,计算机,博弈论", "Mathematics,Computer,Game Theory",
     "匈牙利裔美国数学家，对量子力学、博弈论和计算机架构（冯诺依曼架构）做出了奠基性贡献。",
     "Hungarian-American mathematician who made foundational contributions to quantum mechanics, game theory, and computer architecture (von Neumann architecture)."),
    ("rosa-parks", "罗莎·帕克斯", "Rosa Parks", 1913, 2005, "americas", "民权,女性,美国", "Civil Rights,Women,USA",
     "美国民权运动标志性人物，因拒绝在公交车上给白人让座，引发了蒙哥马利巴士抵制运动。",
     "Iconic figure of the American civil rights movement whose refusal to give up her bus seat to a white passenger sparked the Montgomery Bus Boycott."),
    ("tutu-desmond", "图图大主教", "Desmond Tutu", 1931, 2021, "africa", "宗教,人权,南非,诺贝尔", "Religion,Human Rights,South Africa,Nobel",
     "南非圣公会大主教和反种族隔离运动领袖，真相与和解委员会主席。",
     "South African Anglican Archbishop and anti-apartheid leader, chair of the Truth and Reconciliation Commission."),
    ("yousafzai-malala", "马拉拉", "Malala Yousafzai", 1997, None, "asia", "教育,女性,人权,诺贝尔", "Education,Women,Human Rights,Nobel",
     "巴基斯坦女性教育活动家，最年轻的诺贝尔和平奖得主，为全球女童教育权利而奋斗。",
     "Pakistani female education activist and the youngest Nobel Peace Prize laureate, fighting for girls' education rights worldwide."),
]

people = []
for item in data:
    (pid, name, nameEn, birth, death, rid, tags_str, tagsEn_str, summary, summaryEn) = item[:10]
    wikidata = item[10] if len(item) > 10 else ""
    death_str = 'undefined' if death is None else str(death)
    
    people.append({
        "id": pid, "name": name, "nameEn": nameEn,
        "birthYear": birth, "deathYear": death,
        "deathYearStr": death_str,
        "regionId": rid,
        "tags": [t.strip() for t in tags_str.split(",")],
        "tagsEn": [t.strip() for t in tagsEn_str.split(",")],
        "summary": summary, "summaryEn": summaryEn,
        "description": summary, "descriptionEn": summaryEn,
        "alternativeNames": [], "sourceIds": [],
        "wikidataQid": wikidata,
        "dataStatus": "published", "confidenceScore": 0.9,
        "externalReferences": []
    })

print(f"Total: {len(people)}", file=sys.stderr)

lines = []
for p in people:
    l = []
    l.append("  // --- %s ---" % p["nameEn"])
    l.append("  {")
    l.append("    id: '%s'," % esc(p["id"]))
    l.append("    name: '%s'," % esc(p["name"]))
    l.append("    nameEn: '%s'," % esc(p["nameEn"]))
    l.append("    birthYear: %s," % p["birthYear"])
    l.append("    deathYear: %s," % p["deathYearStr"])
    l.append("    regionId: '%s'," % p["regionId"])
    l.append("    alternativeNames: [],")
    l.append("    tags: [%s]," % ", ".join("'%s'" % esc(t) for t in p["tags"]))
    l.append("    tagsEn: [%s]," % ", ".join("'%s'" % esc(t) for t in p["tagsEn"]))
    l.append("    summary: '%s'," % esc(p["summary"]))
    l.append("    summaryEn: '%s'," % esc(p["summaryEn"]))
    l.append("    description: '%s'," % esc(p["description"]))
    l.append("    descriptionEn: '%s'," % esc(p["descriptionEn"]))
    l.append("    sourceIds: [],")
    l.append("    occupations: [],")
    l.append("    birthDatePrecision: 'year' as const,")
    l.append("    deathDatePrecision: 'year' as const,")
    l.append("    dataStatus: 'published' as const,")
    l.append("    confidenceScore: %s," % p["confidenceScore"])
    l.append("    externalReferences: [],")
    if p["wikidataQid"]:
        l.append("    wikidataQid: '%s'," % p["wikidataQid"])
    l.append("  },")
    lines.append("\n".join(l))

print("\n\n".join(lines))
print("\n// Total: %d new people" % len(people))
