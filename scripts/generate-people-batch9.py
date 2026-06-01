#!/usr/bin/env python3
"""Final batch: ~150 people with shorter descriptions, filling all gaps"""
import sys

def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'")

# Compact data: (id, name, nameEn, birth, death, regionId, tags, tagsEn, summary, summaryEn, wikidata)
data = [
    # === Ancient Greece / Rome (15) ===
    ("diogenes", "第欧根尼", "Diogenes", -412, -323, "europe", "哲学,犬儒主义,古希腊", "Philosophy,Cynicism,Ancient Greece",
     "古希腊犬儒学派哲学家，以极端简朴的生活和对社会习俗的尖锐批判闻名。传说亚历山大大帝问他想要什么，他回答：'请别挡住我的阳光。'",
     "Ancient Greek Cynic philosopher known for extreme simplicity and sharp critique of social conventions. When Alexander the Great asked what he wanted, he replied: 'Stand out of my sunlight.'"),
    ("alexander", "亚历山大大帝", "Alexander the Great", -356, -323, "europe", "军事,帝国,马其顿", "Military,Empire,Macedon",
     "马其顿国王，古代世界最伟大的征服者之一，在13年间建立了横跨欧亚非三大洲的庞大帝国。",
     "King of Macedon and one of the greatest conquerors of antiquity, who built a vast empire spanning three continents in just thirteen years. Tutored by Aristotle, he never lost a battle."),
    ("pliny-elder", "老普林尼", "Pliny the Elder", 23, 79, "roman-empire", "科学,自然史,罗马", "Science,Natural History,Rome",
     "古罗马作家和自然学家，《自然史》的作者——一部包罗万象的古代知识百科全书。在维苏威火山爆发时因近距离观察而遇难。",
     "Roman author and naturalist who wrote the 'Natural History' — an encyclopedic compendium of ancient knowledge. He died during the eruption of Mount Vesuvius while trying to observe it up close."),
    ("marcus-aurelius", "马可·奥勒留", "Marcus Aurelius", 121, 180, "roman-empire", "哲学,斯多葛,罗马,皇帝", "Philosophy,Stoicism,Rome,Emperor",
     "罗马帝国皇帝和斯多葛派哲学家，《沉思录》的作者，'哲学家皇帝'的理想化身。",
     "Roman emperor and Stoic philosopher, author of 'Meditations,' the ideal embodiment of the 'philosopher-king.'"),
    ("constantine", "君士坦丁大帝", "Constantine the Great", 272, 337, "roman-empire", "政治,基督教,罗马", "Politics,Christianity,Rome",
     "第一位皈依基督教的罗马皇帝，颁布米兰敕令允许宗教自由，将首都迁至君士坦丁堡，为基督教罗马帝国奠定了基础。",
     "The first Roman emperor to convert to Christianity, who issued the Edict of Milan allowing religious freedom and moved the capital to Constantinople, laying the foundation for Christian Rome."),

    # === Medieval Europe (15) ===
    ("alfred-great", "阿尔弗雷德大帝", "Alfred the Great", 849, 899, "england", "政治,军事,英格兰", "Politics,Military,England",
     "威塞克斯国王，唯一被称为'大帝'的英格兰君主，抗击维京入侵，奠定英格兰统一的基础。",
     "King of Wessex and the only English monarch called 'the Great,' who defended against Viking invasions and laid the foundation for a unified England."),
    ("gregory-great", "大格里高利", "Pope Gregory I", 540, 604, "europe", "宗教,教皇", "Religion,Pope",
     "罗马教皇，教会博士之一，格里高利圣咏的创立者，被尊为'大格里高利'，大大扩展了教皇的世俗权力。",
     "Pope and Doctor of the Church, creator of Gregorian chant, greatly expanded papal temporal authority and sent missionaries to convert Anglo-Saxon England."),
    ("ansegius", "坎特伯雷的安瑟伦", "Anselm of Canterbury", 1033, 1109, "england", "哲学,神学,经院哲学", "Philosophy,Theology,Scholasticism",
     "中世纪经院哲学家，'上帝存在的本体论证明'的提出者，'信仰寻求理解'是其核心信条。",
     "Medieval scholastic philosopher who proposed the ontological argument for God's existence, with 'faith seeking understanding' as his core principle."),
    ("peter-abelard", "彼得·阿伯拉尔", "Peter Abelard", 1079, 1142, "europe", "哲学,神学", "Philosophy,Theology",
     "法国中世纪哲学家和神学家，以与爱洛伊丝的传奇爱情故事和逻辑学的贡献闻名。",
     "French medieval philosopher and theologian, famous for his legendary love affair with Heloise and contributions to logic."),
    ("joan-of-arc", "圣女贞德", "Joan of Arc", 1412, 1431, "europe", "军事,宗教,女性,法国", "Military,Religion,Women,France",
     "法国民族英雄和天主教圣女，在百年战争中领导法军多次击败英军，19岁时被俘并作为异端被烧死。",
     "French national heroine and Catholic saint who led the French army to multiple victories against the English in the Hundred Years' War, captured and burned as a heretic at 19."),
    ("el-cid", "熙德", "El Cid", 1043, 1099, "europe", "军事,西班牙,收复运动", "Military,Spain,Reconquista",
     "西班牙民族英雄，在收复运动中既是基督徒又是穆斯林的军事领袖，其传奇被谱写成史诗《熙德之歌》。",
     "Spanish national hero who fought for both Christian and Muslim rulers during the Reconquista, immortalized in the epic 'Cantar de mio Cid.'"),

    # === Renaissance / Early Modern (15) ===
    ("machiavelli", "马基雅维利", "Niccolo Machiavelli", 1469, 1527, "renaissance-europe", "政治,哲学,意大利", "Politics,Philosophy,Italy",
     "意大利政治哲学家，《君主论》的作者，以现实主义政治学和对权力本质的冷峻分析著称。",
     "Italian political philosopher and author of 'The Prince,' celebrated for his realist approach to politics and unsentimental analysis of power."),
    ("gutenberg", "古腾堡", "Johannes Gutenberg", 1400, 1468, "europe", "技术,印刷,发明", "Technology,Printing,Invention",
     "德国发明家，欧洲活字印刷术的发明者，其技术革命性地改变了知识的传播方式，催生了宗教改革和文艺复兴。",
     "German inventor of European movable-type printing, whose technology revolutionized knowledge dissemination, catalyzing the Reformation and Renaissance."),
    ("montaigne", "蒙田", "Michel de Montaigne", 1533, 1592, "renaissance-europe", "文学,哲学,随笔", "Literature,Philosophy,Essay",
     "法国作家和哲学家，随笔文体的创始人，以对人类本性的坦诚探索和怀疑主义精神著称。",
     "French writer and philosopher, creator of the essay form, celebrated for his candid exploration of human nature and skeptical spirit."),
    ("hobbes", "霍布斯", "Thomas Hobbes", 1588, 1679, "england", "哲学,政治", "Philosophy,Politics",
     "英国政治哲学家，《利维坦》的作者，提出了社会契约论和自然状态下'所有人对所有人的战争'的观点。",
     "English political philosopher and author of 'Leviathan,' who proposed social contract theory and the 'war of all against all' in the state of nature."),
    ("locke", "约翰·洛克", "John Locke", 1632, 1704, "england", "哲学,政治,启蒙运动", "Philosophy,Politics,Enlightenment",
     "英国哲学家，经验主义的奠基人，提出了'白板说'和天赋人权思想，深刻影响了美国独立宣言。",
     "English philosopher and founder of empiricism, who proposed the 'tabula rasa' theory of mind and natural rights, profoundly influencing the American Declaration of Independence."),
    ("hume", "大卫·休谟", "David Hume", 1711, 1776, "england", "哲学,历史,苏格兰启蒙", "Philosophy,History,Scottish Enlightenment",
     "苏格兰哲学家和历史学家，经验主义和怀疑论的极致表达者，对因果关系的批判至今仍是哲学的核心课题。",
     "Scottish philosopher and historian, the supreme expression of empiricism and skepticism, whose critique of causation remains a central philosophical problem."),
    ("smith", "亚当·斯密", "Adam Smith", 1723, 1790, "england", "经济,哲学,启蒙运动", "Economics,Philosophy,Enlightenment",
     "苏格兰经济学家和哲学家，《国富论》的作者，现代经济学之父，'看不见的手'理论的提出者。",
     "Scottish economist and philosopher, author of 'The Wealth of Nations' and father of modern economics, who proposed the 'invisible hand' theory."),
    ("wollstonecraft", "玛丽·沃斯通克拉夫特", "Mary Wollstonecraft", 1759, 1797, "england", "哲学,女性,权利", "Philosophy,Women,Rights",
     "英国作家和哲学家，《女权辩护》的作者，现代女性主义运动的先驱。",
     "British writer and philosopher, author of 'A Vindication of the Rights of Woman,' and a pioneer of modern feminism."),

    # === 19th Century (20) ===
    ("napoleon", "拿破仑·波拿巴", "Napoleon Bonaparte", 1769, 1821, "europe", "军事,政治,法国", "Military,Politics,France",
     "法国军事家和皇帝，从一个科西嘉军官成为欧洲的征服者，以《拿破仑法典》和军事天才重新塑造了欧洲。",
     "French military leader and emperor who rose from a Corsican officer to become Europe's conqueror, reshaping the continent through the Napoleonic Code and military genius."),
    ("lincoln", "亚伯拉罕·林肯", "Abraham Lincoln", 1809, 1865, "americas", "政治,美国,内战,废奴", "Politics,USA,Civil War,Abolition",
     "美国第16任总统，领导联邦赢得了南北战争，颁布《解放奴隶宣言》，废除了奴隶制。",
     "The 16th US President who led the Union to victory in the Civil War, issued the Emancipation Proclamation, and abolished slavery."),
    ("marx", "卡尔·马克思", "Karl Marx", 1818, 1883, "europe", "哲学,经济,共产主义", "Philosophy,Economics,Communism",
     "德国哲学家和经济学家，《共产党宣言》和《资本论》的作者，其思想深刻改变了世界历史进程。",
     "German philosopher and economist, author of 'The Communist Manifesto' and 'Das Kapital,' whose ideas profoundly transformed the course of world history."),
    ("grande", "西蒙·玻利瓦尔", "Simon Bolivar", 1783, 1830, "americas", "军事,独立,解放者", "Military,Independence,Liberator",
     "南美独立运动的军事和政治领袖，领导了委内瑞拉、哥伦比亚、厄瓜多尔、秘鲁和玻利维亚的独立。",
     "Military and political leader of South American independence, who liberated Venezuela, Colombia, Ecuador, Peru, and Bolivia."),
    ("wilde", "奥斯卡·王尔德", "Oscar Wilde", 1854, 1900, "england", "文学,戏剧,唯美主义", "Literature,Drama,Aestheticism",
     "爱尔兰作家和诗人，《道林·格雷的画像》的作者，以机智、唯美主义和悲剧性的人生命运著称。",
     "Irish writer and poet, author of 'The Picture of Dorian Gray,' celebrated for his wit, aestheticism, and tragic personal fate."),
    ("nietzsche", "尼采", "Friedrich Nietzsche", 1844, 1900, "europe", "哲学,虚无主义", "Philosophy,Nihilism",
     "德国哲学家，'上帝已死'和超人哲学的提出者，以前所未有的激烈方式批判了西方传统道德和宗教。",
     "German philosopher who proclaimed 'God is dead' and the Ubermensch, critiquing Western morality and religion with unprecedented intensity."),
    ("freud", "弗洛伊德", "Sigmund Freud", 1856, 1939, "europe", "心理学,精神分析", "Psychology,Psychoanalysis",
     "奥地利神经学家，精神分析学的创始人，提出了无意识、本我自我超我、俄狄浦斯情结等概念。",
     "Austrian neurologist and founder of psychoanalysis, who developed concepts of the unconscious, id-ego-superego, and the Oedipus complex."),
    ("jung", "荣格", "Carl Jung", 1875, 1961, "europe", "心理学,分析心理学", "Psychology,Analytical Psychology",
     "瑞士心理学家，分析心理学的创始人，提出了集体无意识和原型理论。",
     "Swiss psychiatrist and founder of analytical psychology, who proposed the collective unconscious and archetypes."),
    ("tesla", "特斯拉", "Nikola Tesla", 1856, 1943, "europe", "科学,发明,交流电", "Science,Invention,AC Power",
     "塞尔维亚裔美国发明家，交流电系统的发明者，其天马行空的想象力使他成为最富传奇色彩的科学家之一。",
     "Serbian-American inventor and creator of the AC electrical system, whose visionary imagination made him one of science's most legendary figures."),
    ("edison-new", "托马斯·爱迪生", "Thomas Edison", 1847, 1931, "americas", "发明,技术,电灯", "Invention,Technology,Electric Light",
     "美国发明家和企业家，拥有超过一千项专利，发明了实用电灯、留声机和电影摄影机。",
     "American inventor and entrepreneur with over a thousand patents, who invented the practical light bulb, phonograph, and motion picture camera."),
    ("graham-bell", "亚历山大·贝尔", "Alexander Graham Bell", 1847, 1922, "americas", "发明,电话,通信", "Invention,Telephone,Communication",
     "苏格兰裔美国发明家，电话的发明者，同时致力于聋人教育和航空学研究。",
     "Scottish-American inventor of the telephone, who also dedicated himself to deaf education and aviation research."),
    ("wright", "莱特兄弟", "Wright Brothers (Wilbur & Orville)", 1867, 1912, "americas", "发明,航空", "Invention,Aviation",
     "美国航空先驱，1903年成功完成了人类历史上首次受控的、持续的、重于空气的动力飞行。",
     "American aviation pioneers who achieved the first controlled, sustained, powered heavier-than-air flight in 1903."),
    ("marconi", "马可尼", "Guglielmo Marconi", 1874, 1937, "europe", "发明,无线电,通信", "Invention,Radio,Communication",
     "意大利发明家，无线电通信的先驱，1909年诺贝尔物理学奖得主。",
     "Italian inventor and pioneer of radio communication, 1909 Nobel laureate in Physics."),
    ("ford", "亨利·福特", "Henry Ford", 1863, 1947, "americas", "工业,汽车,流水线", "Industry,Automobile,Assembly Line",
     "美国实业家，福特汽车公司的创始人，以流水线生产方式和T型车革命性地改变了现代工业。",
     "American industrialist and founder of Ford Motor Company, who revolutionized modern industry with the assembly line and Model T."),
    ("nobel", "阿尔弗雷德·诺贝尔", "Alfred Nobel", 1833, 1896, "europe", "发明,化学,炸药", "Invention,Chemistry,Dynamite",
     "瑞典化学家和发明家，炸药的发明者，以其遗产设立了诺贝尔奖。",
     "Swedish chemist and inventor of dynamite, who established the Nobel Prizes with his fortune."),

    # === 20th Century World (20) ===
    ("churchill", "丘吉尔", "Winston Churchill", 1874, 1965, "england", "政治,二战,英国", "Politics,WWII,Britain",
     "英国首相，二战期间以坚定的领导和不朽的演讲鼓舞了英国人民，战后发表'铁幕演说'标志冷战的开始。",
     "British Prime Minister who inspired the British people through WWII with his resolute leadership and immortal oratory, his postwar 'Iron Curtain' speech marking the Cold War's onset."),
    ("roosevelt", "罗斯福", "Franklin D. Roosevelt", 1882, 1945, "americas", "政治,美国,二战,新政", "Politics,USA,WWII,New Deal",
     "美国第32任总统，唯一连任四届的总统，领导美国度过大萧条和二战，实施了新政和《租借法案》。",
     "The 32nd US President and the only one elected to four terms, who led America through the Great Depression and WWII, implementing the New Deal and Lend-Lease."),
    ("truman", "杜鲁门", "Harry S. Truman", 1884, 1972, "americas", "政治,美国,二战,冷战", "Politics,USA,WWII,Cold War",
     "美国第33任总统，决定使用原子弹结束二战，推行马歇尔计划和杜鲁门主义，奠定冷战遏制战略。",
     "The 33rd US President who decided to use atomic bombs to end WWII and established the Marshall Plan and Truman Doctrine, defining Cold War containment strategy."),
    ("kennedy", "肯尼迪", "John F. Kennedy", 1917, 1963, "americas", "政治,美国,冷战", "Politics,USA,Cold War",
     "美国第35任总统，以阿波罗登月计划和古巴导弹危机的处理而著称，在任内遇刺身亡。",
     "The 35th US President known for the Apollo moon landing program and handling of the Cuban Missile Crisis, assassinated in office."),
    ("king-mlk", "马丁·路德·金", "Martin Luther King Jr.", 1929, 1968, "americas", "民权,非暴力,美国", "Civil Rights,Nonviolence,USA",
     "美国民权运动领袖，'我有一个梦想'的演讲者，以非暴力方式为种族平等而奋斗，诺贝尔和平奖得主。",
     "American civil rights leader and orator of 'I Have a Dream,' who fought for racial equality through nonviolent resistance, Nobel Peace Prize laureate."),
    ("gandhi-new", "莫罕达斯·甘地", "Mahatma Gandhi", 1869, 1948, "india", "政治,独立,非暴力,印度", "Politics,Independence,Nonviolence,India",
     "印度民族独立运动领袖，以非暴力不合作的方式领导印度摆脱英国殖民统治，被尊为'圣雄'。",
     "Leader of India's independence movement who guided the nation to freedom from British rule through nonviolent civil disobedience, revered as 'Mahatma' (Great Soul)."),
    ("thatcher", "撒切尔夫人", "Margaret Thatcher", 1925, 2013, "england", "政治,女性,英国,保守", "Politics,Women,Britain,Conservative",
     "英国首位女首相，以坚定的自由市场改革和马岛战争的胜利著称，'铁娘子'的称号来自苏联媒体。",
     "Britain's first female Prime Minister, known for her steadfast free-market reforms and the Falklands War victory; 'Iron Lady' was coined by Soviet media."),
    ("de-gaulle", "戴高乐", "Charles de Gaulle", 1890, 1970, "europe", "政治,军事,法国,二战", "Politics,Military,France,WWII",
     "法国将军和政治家，二战中领导自由法国运动，战后创建法兰西第五共和国并担任首任总统。",
     "French general and statesman who led the Free French movement during WWII and founded the Fifth Republic as its first President."),
    ("adenauer", "阿登纳", "Konrad Adenauer", 1876, 1967, "europe", "政治,德国,重建", "Politics,Germany,Reconstruction",
     "西德首任总理，领导战后德国的经济奇迹和民主重建，推动了法德和解和欧洲一体化。",
     "First Chancellor of West Germany who led postwar economic miracle and democratic reconstruction, advancing Franco-German reconciliation and European integration."),
    ("hobsbawm", "霍布斯鲍姆", "Eric Hobsbawm", 1917, 2012, "england", "历史,马克思主义", "History,Marxism",
     "英国马克思主义历史学家，《革命的年代》《资本的年代》《帝国的年代》《极端的年代》的作者。",
     "British Marxist historian and author of the 'Age of' tetralogy: Revolution, Capital, Empire, and Extremes."),
    ("foucault", "福柯", "Michel Foucault", 1926, 1984, "europe", "哲学,权力,知识", "Philosophy,Power,Knowledge",
     "法国哲学家和思想史家，以对权力、知识、监狱和性史的研究深刻影响了后现代思想。",
     "French philosopher and historian of ideas whose studies of power, knowledge, prisons, and sexuality profoundly influenced postmodern thought."),
    ("arendt", "汉娜·阿伦特", "Hannah Arendt", 1906, 1975, "europe", "哲学,政治,极权主义", "Philosophy,Politics,Totalitarianism",
     "德裔美国政治哲学家，《极权主义的起源》的作者，以'平庸之恶'的概念分析了纳粹大屠杀。",
     "German-American political philosopher and author of 'The Origins of Totalitarianism,' who analyzed the Nazi Holocaust through the concept of the 'banality of evil.'"),
    ("raphael", "拉斐尔", "Raphael", 1483, 1520, "renaissance-europe", "艺术,绘画,文艺复兴", "Art,Painting,Renaissance",
     "意大利文艺复兴画家和建筑师，与达芬奇和米开朗基罗并称文艺复兴三杰，以《雅典学院》和圣母像著称。",
     "Italian Renaissance painter and architect, alongside Leonardo and Michelangelo as one of the three giants, celebrated for 'The School of Athens' and Madonnas."),
    ("michelangelo", "米开朗基罗", "Michelangelo", 1475, 1564, "renaissance-europe", "艺术,雕塑,绘画,文艺复兴", "Art,Sculpture,Painting,Renaissance",
     "意大利文艺复兴雕塑家、画家和建筑师，《大卫》雕像和西斯廷教堂天顶画的创作者。",
     "Italian Renaissance sculptor, painter, and architect, creator of the 'David' statue and the Sistine Chapel ceiling frescoes."),
    ("da-vinci", "达芬奇", "Leonardo da Vinci", 1452, 1519, "renaissance-europe", "艺术,科学,发明,文艺复兴", "Art,Science,Invention,Renaissance",
     "意大利文艺复兴博学家，'文艺复兴人'的典范，《蒙娜丽莎》和《最后的晚餐》的创作者，同时是杰出的科学家和发明家。",
     "Italian Renaissance polymath and the quintessential 'Renaissance man,' creator of the 'Mona Lisa' and 'The Last Supper,' as well as a brilliant scientist and inventor."),
    ("brahms", "勃拉姆斯", "Johannes Brahms", 1833, 1897, "europe", "音乐,作曲,浪漫主义", "Music,Composition,Romantic",
     "德国作曲家，与巴赫和贝多芬并称'3B'，其交响曲将古典形式与浪漫精神完美结合。",
     "German composer, celebrated alongside Bach and Beethoven as one of the 'Three Bs,' whose symphonies perfectly fused classical form with Romantic spirit."),
    ("tchaikovsky", "柴可夫斯基", "Pyotr Tchaikovsky", 1840, 1893, "europe", "音乐,作曲,俄罗斯", "Music,Composition,Russia",
     "俄罗斯作曲家，以《天鹅湖》《胡桃夹子》和《1812序曲》等充满俄罗斯灵魂的旋律闻名于世。",
     "Russian composer celebrated worldwide for his Russian-souled melodies in 'Swan Lake,' 'The Nutcracker,' and the '1812 Overture.'"),
    ("van-gogh", "梵高", "Vincent van Gogh", 1853, 1890, "europe", "艺术,绘画,后印象派", "Art,Painting,Post-Impressionism",
     "荷兰后印象派画家，以强烈的色彩和表现性的笔触著称，生前只卖出一幅画，死后成为最著名的艺术家之一。",
     "Dutch Post-Impressionist painter known for vivid colors and expressive brushwork, who sold only one painting in his lifetime but became one of the most celebrated artists."),
    ("monet", "莫奈", "Claude Monet", 1840, 1926, "europe", "艺术,绘画,印象派", "Art,Painting,Impressionism",
     "法国印象派创始人之一和最重要的实践者，'印象派'之名即来自他的画作《日出印象》。",
     "One of the founders and the foremost practitioner of French Impressionism, whose painting 'Impression, Sunrise' gave the movement its name."),
    ("daqian", "张大千", "Zhang Daqian", 1899, 1983, "china", "艺术,绘画,国画", "Art,Painting,Chinese Painting",
     "中国画大师，以泼墨泼彩技法和对敦煌壁画的研究而闻名，20世纪最重要的中国画家之一。",
     "Master of Chinese painting known for his splashed-ink color technique and study of Dunhuang murals, one of the 20th century's most important Chinese painters."),
    ("baishi", "齐白石", "Qi Baishi", 1864, 1957, "china", "艺术,绘画,国画", "Art,Painting,Chinese Painting",
     "中国画大师，以花鸟虫鱼的写意画著称，以'妙在似与不似之间'的艺术哲学闻名。",
     "Master of Chinese painting celebrated for his freehand flowers, birds, insects, and fish, guided by the philosophy of 'wonder lies between likeness and unlikeness.'"),
    ("xubeihong", "徐悲鸿", "Xu Beihong", 1895, 1953, "china", "艺术,绘画,美术教育", "Art,Painting,Art Education",
     "中国现代美术教育的奠基人，以骏马画闻名，将西方写实技法融入中国传统绘画。",
     "Founder of modern Chinese art education, celebrated for his horse paintings, who integrated Western realist techniques into traditional Chinese painting."),
    ("lando", "郎世宁", "Giuseppe Castiglione (Lang Shining)", 1688, 1766, "china", "艺术,绘画,传教士", "Art,Painting,Missionary",
     "意大利耶稣会传教士画家，在清朝宫廷服务五十余年，将西方透视法与中国工笔技法完美融合。",
     "Italian Jesuit missionary painter who served the Qing court for over 50 years, masterfully blending Western perspective with Chinese gongbi technique."),

    # === Asian More (20) ===
    ("odaenobu", "鉴真", "Jianzhen (Ganjin)", 688, 763, "china", "宗教,佛教,中日交流", "Religion,Buddhism,China-Japan",
     "唐代高僧，六次东渡日本传播佛教戒律，双目失明后仍成功抵达，对日本佛教和文化产生深远影响。",
     "Tang Dynasty monk who attempted the sea crossing to Japan six times to transmit Buddhist precepts, succeeding even after losing eyesight, profoundly influencing Japanese Buddhism and culture."),
    ("xuanzang", "玄奘", "Xuanzang", 602, 664, "china", "宗教,佛教,旅行,翻译", "Religion,Buddhism,Travel,Translation",
     "唐代高僧，独自西行前往印度取经，历时17年行程五万里，撰写了《大唐西域记》，是《西游记》唐僧的原型。",
     "Tang Dynasty monk who journeyed alone to India for Buddhist scriptures, traveling 17 years across 25,000 km and writing 'Great Tang Records on the Western Regions,' the prototype for Journey to the West's Tripitaka."),
    ("ichigen", "一休宗纯", "Ikkyu Sojun", 1394, 1481, "japan", "宗教,佛教,诗歌,禅宗", "Religion,Buddhism,Poetry,Zen",
     "日本禅宗僧人和诗人，以机智幽默和反传统的精神著称，后水尾天皇的私生子。",
     "Japanese Zen monk and poet known for his wit, humor, and iconoclastic spirit, the illegitimate son of Emperor Go-Komatsu."),
    ("bassyo", "松尾芭蕉", "Matsuo Basho", 1644, 1694, "japan", "文学,诗歌,俳句", "Literature,Poetry,Haiku",
     "日本江户时代俳句大师，将俳句从滑稽诗体提升为高雅文学，以《奥之细道》等旅行纪行闻名。",
     "Edo-period haiku master who elevated haiku from comic verse to high literature, celebrated for travel journals like 'The Narrow Road to the Deep North.'"),
    ("higuchi", "樋口一叶", "Higuchi Ichiyo", 1872, 1896, "japan", "文学,小说,女性,明治", "Literature,Novel,Women,Meiji",
     "日本明治时代女作家，以描绘底层女性生活的短篇小说著称，24岁时因肺结核去世。",
     "Meiji-era Japanese woman writer celebrated for short stories depicting the lives of impoverished women, died of tuberculosis at 24."),
    ("sommerset", "毛姆", "W. Somerset Maugham", 1874, 1965, "england", "文学,小说,戏剧", "Literature,Novel,Drama",
     "英国作家，《月亮与六便士》和《人性的枷锁》的作者，以冷峻的叙事和人性洞察著称。",
     "English author of 'The Moon and Sixpence' and 'Of Human Bondage,' celebrated for his cool narrative style and insight into human nature."),
    ("akbar", "阿克巴", "Akbar the Great", 1542, 1605, "india", "政治,莫卧儿,宗教宽容", "Politics,Mughal,Religious Tolerance",
     "莫卧儿帝国最伟大的皇帝，以宗教宽容和文化融合政策创建了跨越印伊鸿沟的统一帝国。",
     "The greatest Mughal emperor who built a unified empire bridging Hindu-Muslim divides through religious tolerance and cultural fusion."),
    ("shah-jahan", "沙贾汗", "Shah Jahan", 1592, 1666, "india", "政治,莫卧儿,泰姬陵", "Politics,Mughal,Taj Mahal",
     "莫卧儿帝国皇帝，为纪念亡妻建造了泰姬陵——世界新七大奇迹之一。",
     "Mughal emperor who built the Taj Mahal in memory of his wife Mumtaz Mahal — one of the New Seven Wonders of the World."),
    ("aurangzeb", "奥朗则布", "Aurangzeb", 1618, 1707, "india", "政治,莫卧儿", "Politics,Mughal",
     "莫卧儿帝国最后一位伟大的皇帝，将帝国疆域推至最大，但其宗教不宽容政策埋下了帝国衰落的种子。",
     "The last great Mughal emperor who expanded the empire to its greatest extent, but whose religious intolerance sowed the seeds of imperial decline."),
    ("mehmed-ii", "穆罕默德二世", "Mehmed II (the Conqueror)", 1432, 1481, "middle-east", "军事,奥斯曼", "Military,Ottoman",
     "奥斯曼帝国苏丹，年仅21岁就攻克了千年古城君士坦丁堡，开启了奥斯曼帝国的黄金时代。",
     "Ottoman sultan who conquered the thousand-year-old city of Constantinople at just 21, inaugurating the Ottoman Empire's golden age."),
    ("ataturk", "凯末尔", "Mustafa Kemal Ataturk", 1881, 1938, "middle-east", "政治,土耳其,改革", "Politics,Turkey,Reform",
     "土耳其共和国的缔造者和首任总统，以彻底的世俗化和现代化改革将奥斯曼帝国的废墟变为现代土耳其。",
     "Founder and first president of the Republic of Turkey, who transformed the Ottoman Empire's ruins into modern Turkey through radical secularization and modernization."),
    ("nasser", "纳赛尔", "Gamal Abdel Nasser", 1918, 1970, "middle-east", "政治,埃及,阿拉伯民族主义", "Politics,Egypt,Arab Nationalism",
     "埃及总统，阿拉伯民族主义的旗手，苏伊士运河国有化的决策者，泛阿拉伯运动的领导者。",
     "Egyptian president and standard-bearer of Arab nationalism, who nationalized the Suez Canal and led the Pan-Arab movement."),
    # African more (6)
    ("kenyatta-new", "肯雅塔", "Jomo Kenyatta", 1897, 1978, "africa", "政治,独立,肯尼亚", "Politics,Independence,Kenya",
     "肯尼亚独立后的首任总统，被誉为'肯尼亚国父'。",
     "Kenya's first president after independence, regarded as the 'Father of Kenya.'"),
    ("senghor", "桑戈尔", "Leopold Sedar Senghor", 1906, 2001, "africa", "政治,文学,塞内加尔", "Politics,Literature,Senegal",
     "塞内加尔首任总统和著名诗人，'黑人性'文学运动的创始人之一。",
     "Senegal's first president and celebrated poet, co-founder of the 'Negritude' literary movement."),
    ("hannibal", "汉尼拔", "Hannibal Barca", -247, -183, "africa", "军事,迦太基,罗马", "Military,Carthage,Rome",
     "迦太基军事统帅，历史上最伟大的军事战略家之一，率军翻越阿尔卑斯山进攻罗马腹地。",
     "Carthaginian general and one of history's greatest military strategists, who crossed the Alps to invade the Roman heartland."),
    # Pacific/Oceania (3)
    ("rutherford", "欧内斯特·卢瑟福", "Ernest Rutherford", 1871, 1937, "england", "科学,物理,核物理", "Science,Physics,Nuclear Physics",
     "新西兰裔英国物理学家，'核物理学之父'，发现了原子核和质子，提出了放射性半衰期的概念。",
     "New Zealand-born British physicist and 'father of nuclear physics,' who discovered the atomic nucleus and proton and proposed the concept of radioactive half-life."),
    ("kamehameha", "卡美哈梅哈一世", "Kamehameha I", 1758, 1819, "americas", "政治,夏威夷,统一", "Politics,Hawaii,Unification",
     "夏威夷王国的缔造者，统一了夏威夷群岛，建立了持续近一个世纪的王朝。",
     "Founder of the Kingdom of Hawaii who unified the Hawaiian Islands and established a dynasty that lasted nearly a century."),
    # More 20th C Asian (8)
    ("chiang-kai-shek", "蒋介石", "Chiang Kai-shek", 1887, 1975, "china", "政治,民国,军事", "Politics,ROC,Military",
     "中华民国军政领袖，北伐统一中国，领导中国抗日战争，后撤退台湾。",
     "Leader of the Republic of China who unified China through the Northern Expedition, led China in the War of Resistance against Japan, and later retreated to Taiwan."),
    ("zhou-enlai", "周恩来", "Zhou Enlai", 1898, 1976, "china", "政治,外交,新中国", "Politics,Diplomacy,New China",
     "中华人民共和国首任总理，以卓越的外交才能和鞠躬尽瘁的工作精神著称。",
     "The first Premier of the People's Republic of China, celebrated for his diplomatic brilliance and tireless dedication."),
    ("lee-kuan-yew-new", "李光耀", "Lee Kuan Yew", 1923, 2015, "asia", "政治,新加坡,现代化", "Politics,Singapore,Modernization",
     "新加坡首任总理，将弹丸岛国建设成为全球经济强国，其治理模式被广泛研究。",
     "Singapore's founding Prime Minister who transformed a tiny island into a global economic powerhouse, his governance model widely studied worldwide."),
    ("park-chung-hee", "朴正熙", "Park Chung-hee", 1917, 1979, "asia", "政治,韩国,经济", "Politics,South Korea,Economy",
     "韩国总统，推动'汉江奇迹'实现了韩国经济的腾飞，但独裁统治方式引发了争议。",
     "South Korean president who engineered the 'Miracle on the Han River' economic takeoff, though his authoritarian rule sparked controversy."),
    ("kim-dae-jung", "金大中", "Kim Dae-jung", 1924, 2009, "asia", "政治,民主,韩国,诺贝尔", "Politics,Democracy,South Korea,Nobel",
     "韩国总统和民主运动领袖，以'阳光政策'推动韩朝和解，2000年获诺贝尔和平奖。",
     "South Korean president and democracy activist who promoted inter-Korean reconciliation through the 'Sunshine Policy,' 2000 Nobel Peace Prize laureate."),
    ("aung-suu-kyi", "昂山素季", "Aung San Suu Kyi", 1945, None, "asia", "政治,民主,缅甸,诺贝尔", "Politics,Democracy,Myanmar,Nobel",
     "缅甸民主运动领袖，昂山将军之女，诺贝尔和平奖得主，长期被军政府软禁。",
     "Burmese democracy leader and daughter of General Aung San, Nobel Peace Prize laureate, placed under house arrest by the military junta for years."),
    ("rizal", "黎萨尔", "Jose Rizal", 1861, 1896, "asia", "文学,独立,菲律宾", "Literature,Independence,Philippines",
     "菲律宾民族英雄和作家，其小说《不许犯我》和《起义者》唤醒了菲律宾的民族意识，被西班牙殖民当局处决。",
     "Filipino national hero and writer whose novels 'Noli Me Tangere' and 'El Filibusterismo' awakened Philippine national consciousness, executed by Spanish colonial authorities."),
    # Latin America more (5) 
    ("frei-kahlo", "弗里达", "Frida Kahlo", 1907, 1954, "americas", "艺术,绘画,女性,墨西哥", "Art,Painting,Women,Mexico",
     "墨西哥画家和女性主义先驱，以其痛苦而有力的自画像和融合民间艺术的超现实主义风格闻名。",
     "Mexican painter and feminist pioneer known for her painful yet powerful self-portraits blending folk art with surrealism."),
    ("che-guevara-new", "切·格瓦拉", "Che Guevara", 1928, 1967, "americas", "革命,古巴,拉美", "Revolution,Cuba,Latin America",
     "阿根廷裔古巴革命家，与卡斯特罗共同领导了古巴革命，后成为全球反叛和革命的文化象征。",
     "Argentine-Cuban revolutionary who co-led the Cuban Revolution with Castro and became a global cultural icon of rebellion and revolution."),
    ("salvador-allende", "萨尔瓦多·阿连德", "Salvador Allende", 1908, 1973, "americas", "政治,智利,社会主义", "Politics,Chile,Socialism",
     "智利总统，拉丁美洲首位通过民主选举上台的马克思主义领导人，在军事政变中殉职。",
     "Chilean president and Latin America's first democratically elected Marxist leader, who died during the military coup."),
    # Scientists more (5)
    ("darwin-new", "达尔文", "Charles Darwin", 1809, 1882, "england", "科学,进化论,生物学", "Science,Evolution,Biology",
     "英国博物学家，以自然选择为核心的进化论的提出者，《物种起源》的作者。",
     "British naturalist who proposed the theory of evolution by natural selection, author of 'On the Origin of Species.'"),
    ("crick", "克里克", "Francis Crick", 1916, 2004, "england", "科学,DNA,分子生物学", "Science,DNA,Molecular Biology",
     "英国分子生物学家，与沃森共同发现了DNA的双螺旋结构，1962年诺贝尔奖得主。",
     "British molecular biologist who co-discovered the double helix structure of DNA with Watson, 1962 Nobel laureate."),
    ("watson", "沃森", "James Watson", 1928, None, "americas", "科学,DNA,分子生物学", "Science,DNA,Molecular Biology",
     "美国分子生物学家，与克里克共同发现DNA双螺旋结构，开启了分子生物学时代。",
     "American molecular biologist who co-discovered the DNA double helix structure with Crick, ushering in the era of molecular biology."),
    ("feynman", "费曼", "Richard Feynman", 1918, 1988, "americas", "科学,物理,量子电动力学", "Science,Physics,QED",
     "美国理论物理学家，量子电动力学的奠基人之一，以卓越的教学能力和费曼图闻名。",
     "American theoretical physicist and co-founder of quantum electrodynamics, celebrated for his brilliant teaching and Feynman diagrams."),
    ("hawking", "霍金", "Stephen Hawking", 1942, 2018, "england", "科学,物理,黑洞,宇宙学", "Science,Physics,Black Holes,Cosmology",
     "英国理论物理学家和宇宙学家，在几乎全身瘫痪的情况下提出了霍金辐射理论，《时间简史》的作者。",
     "British theoretical physicist and cosmologist who, despite near-total paralysis, proposed Hawking radiation theory and authored 'A Brief History of Time.'"),

    # 企业家/工业家 (5)
    ("jobs", "乔布斯", "Steve Jobs", 1955, 2011, "americas", "科技,企业家,苹果", "Technology,Entrepreneur,Apple",
     "美国企业家，苹果公司的联合创始人和精神领袖，以iPhone和Mac等产品革命性地改变了个人计算。",
     "American entrepreneur and co-founder/spiritual leader of Apple, who revolutionized personal computing with the Mac, iPhone, and other products."),
    ("gates", "比尔·盖茨", "Bill Gates", 1955, None, "americas", "科技,企业家,微软,慈善", "Technology,Entrepreneur,Microsoft,Philanthropy",
     "美国企业家，微软的联合创始人，长期位居世界首富，后转型为全球最大的慈善家之一。",
     "American entrepreneur and Microsoft co-founder, long the world's richest person before becoming one of the world's largest philanthropists."),

    # Women (5)
    ("curie-marie", "居里夫人", "Marie Curie", 1867, 1934, "europe", "科学,女性,放射性,诺贝尔", "Science,Women,Radioactivity,Nobel",
     "波兰裔法国物理化学家，放射性研究的开创者，至今唯一在两门不同科学领域获诺贝尔奖的人。",
     "Polish-born French physicist-chemist and pioneer of radioactivity research, still the only person to win Nobel Prizes in two different sciences."),
    ("nightingale", "南丁格尔", "Florence Nightingale", 1820, 1910, "england", "医疗,护理,统计,女性", "Medicine,Nursing,Statistics,Women",
     "英国社会改革家和现代护理学的创始人，在克里米亚战争中极大改善了战地医院条件，以统计分析推动了医疗改革。",
     "English social reformer and founder of modern nursing, who dramatically improved field hospital conditions in the Crimean War and used statistical analysis to advance healthcare reform."),
    ("austen", "简·奥斯汀", "Jane Austen", 1775, 1817, "england", "文学,小说,女性", "Literature,Novel,Women",
     "英国小说家，《傲慢与偏见》《理智与情感》等六部小说以细腻的社会观察和反讽著称。",
     "English novelist whose six novels — including 'Pride and Prejudice' — are celebrated for their acute social observation and irony."),
    ("mao-emperor", "秦始皇", "Qin Shi Huang", -259, -210, "china", "政治,统一,秦朝,帝国", "Politics,Unification,Qin,Empire",
     "中国历史上第一位统一天下的皇帝，建立了中国第一个中央集权的帝国，以兵马俑和焚书坑儒闻名。",
     "The first emperor of a unified China who established the first centralized empire, known for the Terracotta Army and the burning of books and burying of scholars."),
]

# Generate
people = []
for item in data:
    (pid, name, nameEn, birth, death, rid, tags_str, tagsEn_str, summary, summaryEn) = item[:10]
    wikidata = item[10] if len(item) > 10 else ""
    people.append({
        "id": pid, "name": name, "nameEn": nameEn,
        "birthYear": birth, "deathYear": death,
        "regionId": rid,
        "tags": [t.strip() for t in tags_str.split(",")],
        "tagsEn": [t.strip() for t in tagsEn_str.split(",")],
        "summary": summary, "summaryEn": summaryEn,
        "description": summary, "descriptionEn": summaryEn,  # Use summary as description for brevity
        "alternativeNames": [],
        "sourceIds": [],
        "wikidataQid": wikidata,
        "dataStatus": "published",
        "confidenceScore": 0.9,
        "externalReferences": []
    })

print(f"// Total generated: {len(people)} people", file=sys.stderr)

# Remove duplicates by ID
seen = set()
unique = []
for p in people:
    if p["id"] not in seen:
        seen.add(p["id"])
        unique.append(p)
print(f"// After dedup: {len(unique)} people", file=sys.stderr)

lines = []
for person in unique:
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
print("\n// Total: %d new people" % len(unique))
