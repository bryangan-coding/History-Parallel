#!/usr/bin/env python3
"""Generate ~350 new Person entries for mockData.ts — Batch 4: filling gaps"""
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

# ========================================
# SECTION 1: AFRICA (sub-Saharan + North Africa beyond Egypt)
# ========================================

p("sunni-ali", "桑尼·阿里", "Sunni Ali", 1440, 1492, "africa",
  ["政治", "军事", "桑海帝国", "非洲"],
  ["Politics", "Military", "Songhai Empire", "Africa"],
  "桑海帝国的第一位伟大君主，征服了廷巴克图和杰内，建立了西非历史上最大的帝国。",
  "The first great ruler of the Songhai Empire who conquered Timbuktu and Jenne, building West Africa's largest empire.",
  "桑尼·阿里于1464年登上桑海王位，随后发动了一系列征服战争。1468年他攻占廷巴克图，1473年占领杰内。他将尼日尔河中游的贸易城市统一在桑海的统治之下，创建了强大的骑兵和水军。他以铁腕统治闻名，被穆斯林学者称为暴君，但他奠定了桑海帝国的军事和经济基础。",
  "Sunni Ali ascended the Songhai throne in 1464 and launched a series of conquests: Timbuktu in 1468, Jenne in 1473. He unified the Niger Bend trading cities under Songhai rule, building a powerful cavalry and river navy. Known for his iron-fisted rule, he was branded a tyrant by Muslim scholars but laid the military and economic foundations of the empire.",
  [], [], "", 0.75)

p("askia-muhammad", "阿斯基亚·穆罕默德", "Askia Muhammad I", 1443, 1538, "africa",
  ["政治", "行政", "伊斯兰", "桑海帝国"],
  ["Politics", "Administration", "Islam", "Songhai Empire"],
  "桑海帝国阿斯基亚王朝的建立者，以卓越的行政改革和推动伊斯兰学术闻名，将桑海推向鼎盛。",
  "Founder of the Askia dynasty of the Songhai Empire, celebrated for his administrative reforms and promotion of Islamic scholarship, bringing Songhai to its zenith.",
  "1493年穆罕默德·杜尔（后称阿斯基亚·穆罕默德）击败桑尼·阿里的儿子夺取王位。他建立了中央集权的行政体系，将帝国划分为多个省份，任命忠诚的总督管理。他大规模赞助伊斯兰学术，使廷巴克图的桑科雷大学达到鼎盛。1495-1497年他前往麦加朝圣，哈里发授予他'苏丹地区哈里发'的头衔。",
  "In 1493 Muhammad Turé defeated Sunni Ali's son to seize the throne. He established a centralized administration dividing the empire into provinces under loyal governors. He patronized Islamic scholarship on a grand scale, making Timbuktu's Sankore University flourish. His 1495-1497 pilgrimage to Mecca earned him the title 'Caliph of the Sudan' from the Abbasid caliph.",
  [], [], "", 0.8)

p("shaka-zulu", "恰卡·祖鲁", "Shaka Zulu", 1787, 1828, "africa",
  ["军事", "政治", "祖鲁", "非洲"],
  ["Military", "Politics", "Zulu", "Africa"],
  "祖鲁王国的缔造者，军事天才，改革了非洲的战争方式，创建了南部非洲最强大的王国。",
  "Founder of the Zulu Kingdom and a military genius who revolutionized African warfare, creating southern Africa's most powerful kingdom.",
  "恰卡从一个小部落首领起家，通过军事改革将一个不起眼的氏族变成了强大的祖鲁王国。他发明了新型短刺矛（iklwa）、牛角阵形战术，实行严格的军事训练制度。他的扩张战争（称为'姆菲卡内'或'大分散'）深刻改变了南部非洲的人口和政治版图，数百万人因此迁徙。1828年他被同父异母的兄弟丁冈刺杀。",
  "Shaka rose from a minor chieftain to forge the Zulu kingdom through military innovation: the short stabbing spear (iklwa), the 'buffalo horns' formation, and rigorous training. His expansionist wars — the 'Mfecane' or 'Crushing' — reshaped southern Africa's demographic and political landscape, displacing millions. He was assassinated by his half-brother Dingane in 1828.",
  [], [], "Q27695", 0.85)

p("menelik-ii", "孟尼利克二世", "Menelik II", 1844, 1913, "africa",
  ["政治", "军事", "埃塞俄比亚", "独立"],
  ["Politics", "Military", "Ethiopia", "Independence"],
  "埃塞俄比亚皇帝，在阿杜瓦战役中击败意大利侵略军，使埃塞俄比亚成为非洲唯一未被殖民的国家。",
  "Emperor of Ethiopia who defeated Italian invaders at the Battle of Adwa, making Ethiopia the only African nation to resist colonization.",
  "孟尼利克二世于1889年成为皇帝，迅速推行现代化改革：建立电报和铁路，引入现代教育，创建国家首都亚的斯亚贝巴。1896年3月，他在阿杜瓦战役中率领十万大军击败意大利军队——这是非洲军队对欧洲殖民者最大规模的胜利。战后欧洲列强纷纷承认埃塞俄比亚的独立，他成为了全非洲抵抗殖民主义的精神象征。",
  "Menelik II became emperor in 1889 and quickly launched modernization: telegraph, railways, modern education, and founding the capital Addis Ababa. In March 1896, at the Battle of Adwa, his 100,000-strong army decisively defeated Italian forces — the largest African victory over European colonizers. European powers subsequently recognized Ethiopian independence, and Menelik became a beacon of anti-colonial resistance.",
  [], [], "", 0.9)

p("haile-selassie", "海尔·塞拉西", "Haile Selassie", 1892, 1975, "africa",
  ["政治", "非洲统一", "改革"],
  ["Politics", "African Unity", "Reform"],
  "埃塞俄比亚末代皇帝，非洲统一组织的主要推动者，拉斯塔法里运动尊其为神。",
  "Ethiopia's last emperor, a driving force behind the Organization of African Unity and revered as divine by the Rastafari movement.",
  "海尔·塞拉西1930年加冕为埃塞俄比亚皇帝。1935年意大利入侵埃塞俄比亚时，他在国际联盟发表了感人的呼吁——虽未获得实质援助，却成为反法西斯主义的标志性时刻。1941年盟军帮助他复国。战后他推动非洲独立与团结，1963年非洲统一组织在亚的斯亚贝巴成立。1974年军事政变推翻其统治，次年去世。",
  "Haile Selassie was crowned in 1930. When Italy invaded Ethiopia in 1935, his emotional appeal to the League of Nations — though fruitless — became an iconic anti-fascist moment. Allied forces helped restore him in 1941. Postwar, he championed African independence and unity; the Organization of African Unity was founded in Addis Ababa in 1963. A 1974 military coup deposed him; he died the following year.",
  [], [], "", 0.9)

p("nkrumah", "克瓦米·恩克鲁玛", "Kwame Nkrumah", 1909, 1972, "africa",
  ["政治", "独立", "泛非主义"],
  ["Politics", "Independence", "Pan-Africanism"],
  "加纳独立运动领袖和首任总统，泛非主义的主要理论家和实践者，非洲独立运动的旗手。",
  "Leader of Ghana's independence movement and its first president, a key theorist and practitioner of Pan-Africanism and a standard-bearer for African independence.",
  "恩克鲁玛在美国和英国接受教育，深受泛非主义思想影响。1951年他的政党在大选中获胜，1957年加纳成为撒哈拉以南非洲第一个独立的国家。他提出了'非洲合众国'的宏伟设想，积极推动非洲统一。在国内推行工业化和社会改革，但因经济困难和独裁倾向而在1966年军事政变中被推翻。",
  "Educated in the US and UK, Nkrumah was deeply influenced by Pan-Africanist thought. His party won elections in 1951, and in 1957 Ghana became sub-Saharan Africa's first independent nation. He proposed a visionary 'United States of Africa' and championed continental unity. Domestically, he pursued industrialization but was overthrown by a military coup in 1966 amid economic difficulties and authoritarian tendencies.",
  [], [], "", 0.9)

p("kenyatta", "乔莫·肯雅塔", "Jomo Kenyatta", 1897, 1978, "africa",
  ["政治", "独立", "肯尼亚"],
  ["Politics", "Independence", "Kenya"],
  "肯尼亚独立运动领袖和首任总统，'肯尼亚国父'，领导了茅茅起义后的和平独立进程。",
  "Leader of Kenya's independence movement and its founding president, known as the 'Father of Kenya,' who guided the nation to independence after the Mau Mau uprising.",
  "肯雅塔在伦敦留学期间出版了人类学著作《面向肯尼亚山》，成为肯尼亚民族主义的理论基础。1952年他被英国殖民当局以策划茅茅起义的罪名逮捕，监禁七年。获释后他领导了与英国的宪法谈判，1963年肯尼亚独立，他成为首任总统。他推行'哈兰贝'（齐心协力）的建国精神，使肯尼亚成为非洲相对稳定的国家。",
  "While studying in London, Kenyatta published 'Facing Mount Kenya,' an anthropological work that became the theoretical basis for Kenyan nationalism. Arrested by British authorities in 1952 for allegedly orchestrating the Mau Mau uprising, he spent seven years in detention. After release, he led constitutional negotiations, and Kenya became independent in 1963 with him as its first president. His 'Harambee' (pulling together) philosophy fostered relative stability.",
  [], [], "", 0.9)

p("mandela", "曼德拉", "Nelson Mandela", 1918, 2013, "africa",
  ["政治", "反种族隔离", "人权", "诺贝尔"],
  ["Politics", "Anti-Apartheid", "Human Rights", "Nobel"],
  "南非反种族隔离革命家，被囚禁27年后成为南非首位黑人总统，和解与宽容的全球象征。",
  "South African anti-apartheid revolutionary who became the country's first Black president after 27 years in prison, a global symbol of reconciliation.",
  "曼德拉早年投身反种族隔离斗争，1962年被判终身监禁。在罗本岛监狱的27年中，他成为全球反种族隔离运动的象征。1990年获释后，他选择以和解而非复仇的方式领导南非向民主过渡。1994年当选为南非首位黑人总统，1993年与德克勒克共获诺贝尔和平奖。他的'彩虹之国'理念代表了包容与多元。",
  "Mandela was sentenced to life imprisonment in 1962 for his anti-apartheid activism. Through 27 years in Robben Island prison, he became the global symbol of the anti-apartheid movement. After release in 1990, he chose reconciliation over revenge, guiding South Africa's democratic transition and becoming its first Black president in 1994. He shared the 1993 Nobel Peace Prize with F.W. de Klerk.",
  [], [], "Q8023", 0.95)

p("desmond-tutu", "德斯蒙德·图图", "Desmond Tutu", 1931, 2021, "africa",
  ["宗教", "人权", "反种族隔离", "诺贝尔"],
  ["Religion", "Human Rights", "Anti-Apartheid", "Nobel"],
  "南非圣公会大主教，反种族隔离斗争的精神领袖，真相与和解委员会主席，诺贝尔和平奖得主。",
  "South African Anglican Archbishop, spiritual leader of the anti-apartheid struggle, chair of the Truth and Reconciliation Commission, and Nobel Peace Prize laureate.",
  "图图大主教在南非种族隔离时期以非暴力方式领导教会抵抗运动，被称为'南非的良心'。1984年获诺贝尔和平奖，1986年成为开普敦首位黑人大主教。种族隔离结束后，他主持了真相与和解委员会，以'没有宽恕就没有未来'的理念推动国家愈合，而非以暴制暴。其道德勇气和幽默感使他成为全球最受尊敬的精神领袖之一。",
  "Archbishop Tutu led the church's nonviolent resistance during apartheid, earning the title 'South Africa's conscience.' He won the Nobel Peace Prize in 1984 and became Cape Town's first Black archbishop in 1986. After apartheid, he chaired the Truth and Reconciliation Commission, promoting healing through his credo: 'No future without forgiveness.' His moral courage and humor made him one of the world's most revered spiritual leaders.",
  [], [], "", 0.95)

p("ibn-battuta", "伊本·白图泰", "Ibn Battuta", 1304, 1369, "africa",
  ["探索", "旅行", "伊斯兰", "地理"],
  ["Exploration", "Travel", "Islam", "Geography"],
  "摩洛哥旅行家，历时近三十年游历了伊斯兰世界和更远的地方，行程远超马可·波罗。",
  "Moroccan traveler who journeyed across the Islamic world and beyond for nearly thirty years, covering distances far exceeding Marco Polo.",
  "伊本·白图泰1325年从摩洛哥丹吉尔出发前往麦加朝圣，此后的29年中他游历了北非、东非、阿拉伯半岛、波斯、中亚、印度、东南亚和中国，行程约12万公里。晚年回国后他口述了《游记》，书中对各地风土人情的详细记载是14世纪伊斯兰世界最珍贵的史料之一。他最远到达了泉州、杭州和北京。",
  "Ibn Battuta set out from Tangier in 1325 for the Hajj, then spent 29 years traveling through North and East Africa, Arabia, Persia, Central Asia, India, Southeast Asia, and China — roughly 120,000 km. His dictated 'Rihla' (Travels) remains one of the most valuable records of the 14th-century Islamic world. He reached as far as Quanzhou, Hangzhou, and Beijing.",
  [], [], "", 0.85)

p("leo-africanus", "利奥·阿非利加努斯", "Leo Africanus", 1494, 1554, "africa",
  ["地理", "历史", "旅行", "文艺复兴"],
  ["Geography", "History", "Travel", "Renaissance"],
  "安达卢西亚裔摩洛哥旅行家和学者，其《非洲描述》是欧洲了解非洲内陆最重要的资料长达数百年。",
  "Andalusian-Moroccan traveler and scholar whose 'Description of Africa' was Europe's primary source on the African interior for centuries.",
  "哈桑·阿尔-瓦赞（后改名乔瓦尼·利奥）生于格拉纳达，在摩洛哥非斯接受教育。16世纪初他以外交使节身份游历了西非的加纳、马里和桑海帝国。1518年被西西里海盗俘虏并献给教皇利奥十世，他皈依基督教后以拉丁文撰写了《非洲描述》，详尽记载了撒哈拉以南非洲的地理、文化和经济，直至19世纪仍是欧洲了解非洲的主要参考书。",
  "Born Hassan al-Wazzan in Granada and educated in Fez, he traveled as a diplomat through the Ghana, Mali, and Songhai empires. Captured by Sicilian pirates in 1518 and presented to Pope Leo X, he converted and wrote 'Description of Africa' in Latin — a comprehensive account of sub-Saharan geography, culture, and economy that remained Europe's primary African reference into the 19th century.",
  [], [], "", 0.8)

# ========================================
# SECTION 2: AMERICAS (Pre-Columbian + colonial + modern)
# ========================================

p("pachacuti", "帕查库特克", "Pachacuti", 1418, 1471, "americas",
  ["政治", "帝国", "印加", "建筑"],
  ["Politics", "Empire", "Inca", "Architecture"],
  "印加帝国的缔造者，将一个小王国扩张为安第斯山脉的大帝国，建造了马丘比丘。",
  "Founder of the Inca Empire who transformed a small kingdom into an Andean superpower and built Machu Picchu.",
  "帕查库特克（意为'撼动大地者'）1438年即位前，印加只是库斯科谷地的一个小王国。他在抵御昌卡人入侵的战役中崭露头角，随后发动了一系列扩张战争，将印加领土扩展到从厄瓜多尔到智利的广大地区。他重组了帝国的行政和宗教体系，修建了宏伟的石城——马丘比丘就是在他统治期间建造的皇家行宫。",
  "Pachacuti ('Earth Shaker') transformed the Inca from a small Cusco valley kingdom into a vast empire stretching from Ecuador to Chile. After repelling the Chanka invasion, he launched expansion campaigns and reorganized the imperial administration and religion. He commissioned magnificent stone cities — Machu Picchu was built as a royal estate during his reign.",
  [], [], "", 0.7)

p("montezuma-ii", "蒙特祖马二世", "Moctezuma II", 1466, 1520, "americas",
  ["政治", "阿兹特克", "西班牙征服"],
  ["Politics", "Aztec", "Spanish Conquest"],
  "阿兹特克帝国的第九位皇帝，在西班牙征服者科尔特斯到来时统治着中美洲最强大的帝国。",
  "The ninth Aztec emperor who ruled Mesoamerica's most powerful empire when Spanish conquistador Cortés arrived.",
  "蒙特祖马二世1502年即位时，阿兹特克帝国处于鼎盛——统治着从墨西哥湾到太平洋的数百万人口。1519年科尔特斯率领西班牙人登陆，蒙特祖马起初以礼相待——部分原因是阿兹特克预言中羽蛇神将从东方归来。西班牙人将他作为人质囚禁在自己的宫殿中，1520年在一次冲突中他被自己的人民用石头砸死——也有说法是西班牙人杀了他。",
  "When Moctezuma II ascended in 1502, the Aztec Empire was at its height, ruling millions from the Gulf of Mexico to the Pacific. Cortés arrived in 1519; Moctezuma initially welcomed him — partly because of the prophecy that Quetzalcoatl would return from the east. The Spanish took him hostage in his own palace. In 1520 he was killed, either by stones from his own people or by the Spanish.",
  [], [], "", 0.8)

p("malinche", "马林切", "La Malinche", 1500, 1529, "americas",
  ["翻译", "女性", "西班牙征服", "阿兹特克"],
  ["Translation", "Women", "Spanish Conquest", "Aztec"],
  "埃尔南·科尔特斯的翻译和顾问，在西班牙征服阿兹特克帝国中扮演了关键角色。",
  "Hernán Cortés' interpreter and advisor who played a crucial role in the Spanish conquest of the Aztec Empire.",
  "马林切（马林琴）原为阿兹特克贵族之女，被卖为奴隶后精通纳瓦特尔语和玛雅语。1519年她被赠给科尔特斯，迅速学会了西班牙语，成为征服者与中美洲诸民族之间不可或缺的翻译和顾问。她的语言和文化知识帮助科尔特斯建立了反阿兹特克联盟。在墨西哥历史上她是一个充满争议的人物：叛徒还是受害者？",
  "Born to Aztec nobility and sold into slavery, Malinche was fluent in Nahuatl and Maya. Given to Cortés in 1519, she quickly learned Spanish and became the conquerors' indispensable interpreter and advisor. Her linguistic and cultural knowledge helped Cortés forge anti-Aztec alliances. She remains a deeply contested figure in Mexican history: traitor or victim?",
  [], [], "", 0.7)

p("tupac-amaru-ii", "图帕克·阿马鲁二世", "Túpac Amaru II", 1738, 1781, "americas",
  ["革命", "独立", "印加", "殖民抵抗"],
  ["Revolution", "Independence", "Inca", "Colonial Resistance"],
  "秘鲁印第安人起义领袖，自称印加皇帝后裔，领导了西班牙美洲殖民地最大规模的土著起义。",
  "Leader of a Peruvian indigenous rebellion who claimed descent from Inca emperors and led the largest native uprising in Spanish America.",
  "何塞·加夫列尔·孔多尔坎基（自称图帕克·阿马鲁二世——末代印加皇帝之名）1780年在秘鲁发动起义，抗议西班牙殖民当局对印第安人的残酷剥削。起义迅速蔓延到整个安第斯地区，数万印第安人加入。1781年他被俘，在库斯科广场被当众处决——四肢被马匹撕裂。起义虽然失败，却成为了拉丁美洲独立运动的先声。",
  "José Gabriel Condorcanqui, adopting the name Túpac Amaru II (the last Inca emperor's name), launched a rebellion in 1780 against brutal Spanish colonial exploitation. The uprising spread across the Andes with tens of thousands of indigenous followers. Captured in 1781, he was publicly executed in Cusco's plaza — drawn and quartered by horses. Though defeated, the rebellion foreshadowed Latin American independence.",
  [], [], "", 0.8)

p("san-martin", "何塞·德·圣马丁", "José de San Martín", 1778, 1850, "americas",
  ["军事", "独立", "阿根廷", "解放者"],
  ["Military", "Independence", "Argentina", "Liberator"],
  "阿根廷将军，南美独立战争的关键领袖，解放了阿根廷、智利和秘鲁，与玻利瓦尔齐名。",
  "Argentine general and key leader of South American independence who liberated Argentina, Chile, and Peru, renowned alongside Bolívar.",
  "圣马丁在西班牙军队服役二十年后回到南美投身独立事业。他认识到从阿根廷翻越安第斯山脉奇袭智利是击败西班牙人的关键——1817年他率军完成了这一史诗般的翻越。解放智利后他北上攻入秘鲁，1821年宣布秘鲁独立。1822年他与玻利瓦尔在瓜亚基尔秘密会晤后主动退出，将未竟事业交给玻利瓦尔完成。",
  "After 20 years in the Spanish army, San Martín returned to South America for the independence cause. He realized the key was a surprise crossing of the Andes from Argentina into Chile — an epic feat he accomplished in 1817. After liberating Chile, he marched into Peru, declaring its independence in 1821. After a secret 1822 meeting with Bolívar in Guayaquil, he voluntarily stepped aside.",
  [], [], "", 0.9)

p("ouspensky-juarez", "贝尼托·华雷斯", "Benito Juárez", 1806, 1872, "americas",
  ["政治", "改革", "墨西哥", "印第安"],
  ["Politics", "Reform", "Mexico", "Indigenous"],
  "墨西哥首位原住民总统，领导了自由改革，击败法国干涉，建立了现代墨西哥的世俗国家基础。",
  "Mexico's first indigenous president who led liberal reforms, defeated French intervention, and laid the foundations of modern Mexico's secular state.",
  "华雷斯出身萨波特克印第安农家，靠自学成为律师和政治家。1858年成为总统后推行'改革法'，将教会财产国有化，实行政教分离。1861年法国以讨债为名入侵墨西哥，扶植奥地利大公马克西米连为皇帝。华雷斯领导游击队抵抗五年，1867年最终收复墨西哥城并处决了马克西米连。'尊重他人的权利就是和平'是他的名言。",
  "Born to Zapotec indigenous farmers, Juárez rose through self-education to become a lawyer and statesman. As president from 1858, he enacted the Reform Laws nationalizing church property and separating church and state. When France invaded in 1861 and installed Maximilian as emperor, Juárez led guerrilla resistance for five years, retaking Mexico City in 1867. 'Respect for the rights of others is peace' is his enduring maxim.",
  [], [], "", 0.9)

p("zapata", "埃米利亚诺·萨帕塔", "Emiliano Zapata", 1879, 1919, "americas",
  ["革命", "农民", "土地改革", "墨西哥"],
  ["Revolution", "Peasants", "Land Reform", "Mexico"],
  "墨西哥革命中的农民领袖，'土地与自由'口号的象征，为无地农民争取土地权利的斗士。",
  "Peasant leader of the Mexican Revolution and symbol of 'Land and Liberty,' a fighter for landless farmers' rights.",
  "萨帕塔是墨西哥莫雷洛斯州的农民领袖，1910年加入推翻独裁者迪亚斯的革命。当革命后的政府未能兑现土地改革的承诺时，他起草了'阿亚拉计划'——要求将大庄园土地归还给农民。他的南解放军的口号是'土地与自由'。1919年他被政府军伏击杀害，但他的土地改革理想最终被写入1917年宪法，至今仍是墨西哥社会正义的象征。",
  "Zapata, a peasant leader from Morelos state, joined the 1910 revolution to overthrow dictator Díaz. When the post-revolutionary government failed to deliver land reform, he drafted the 'Plan of Ayala' demanding return of hacienda lands to peasants. His Liberation Army of the South fought under 'Land and Liberty.' Ambushed and killed in 1919, his ideals were enshrined in Mexico's 1917 constitution.",
  [], [], "", 0.9)

p("evita-peron", "伊娃·庇隆", "Eva Perón", 1919, 1952, "americas",
  ["政治", "女性", "社会福利", "阿根廷"],
  ["Politics", "Women", "Social Welfare", "Argentina"],
  "阿根廷第一夫人，'艾薇塔'，以社会福利工作和为穷人、妇女争取权利的不懈奋斗成为拉丁美洲的传奇。",
  "Argentina's First Lady, 'Evita,' who became a Latin American legend through her social welfare work and tireless advocacy for the poor and women.",
  "伊娃出身贫寒，从演员成为胡安·庇隆的妻子和阿根廷第一夫人。她创立了伊娃·庇隆基金会，大规模开展社会福利项目——建医院、学校和住房。她推动通过了阿根廷妇女选举权法案。虽然从未担任正式政治职务，她却是庇隆政府中最受民众爱戴的人物。33岁因宫颈癌英年早逝，举国哀悼——数百万人排队瞻仰她的遗体。",
  "Born in poverty, Eva rose from actress to become Juan Perón's wife and Argentina's First Lady. She created the Eva Perón Foundation undertaking massive social welfare: hospitals, schools, housing. She championed women's suffrage, which became law in 1947. Though never holding formal office, she was the most beloved figure in Perón's government. She died of cervical cancer at 33, with millions filing past her coffin.",
  [], [], "", 0.9)

p("frida-kahlo", "弗里达·卡洛", "Frida Kahlo", 1907, 1954, "americas",
  ["艺术", "绘画", "女性", "墨西哥"],
  ["Art", "Painting", "Women", "Mexico"],
  "墨西哥画家，以超现实主义自画像著称，用艺术表达身体痛苦和情感挣扎的女性主义先驱。",
  "Mexican painter known for surrealist self-portraits, a feminist pioneer who channeled physical pain and emotional struggle into art.",
  "弗里达·卡洛18岁时遭遇一场几乎致命的车祸，此后一生经历了三十多次手术。在漫长的康复期她开始画自画像——'我画自己是因为我最了解自己。'她的作品融合了墨西哥民间艺术、超现实主义和强烈的个人叙事。她与壁画家迭戈·里维拉的动荡婚姻、对共产主义的信仰以及顽强的生存意志使她成为20世纪最具标志性的女性艺术家。",
  "Frida Kahlo suffered a near-fatal bus accident at 18, enduring over 30 surgeries throughout her life. During her long recovery, she began painting self-portraits: 'I paint myself because I am the subject I know best.' Her work blends Mexican folk art, surrealism, and intensely personal narrative. Her turbulent marriage to muralist Diego Rivera, communist beliefs, and indomitable will made her the 20th century's most iconic female artist.",
  [], [], "", 0.9)

p("neruda", "巴勃罗·聂鲁达", "Pablo Neruda", 1904, 1973, "americas",
  ["文学", "诗歌", "诺贝尔", "政治"],
  ["Literature", "Poetry", "Nobel", "Politics"],
  "智利诗人，诺贝尔文学奖得主，20世纪西班牙语文学最伟大的诗人之一。",
  "Chilean poet and Nobel laureate, one of the greatest poets of 20th-century Spanish-language literature.",
  "聂鲁达13岁就开始发表诗歌，20岁时出版的《二十首情诗和一首绝望的歌》成为全世界最畅销的诗集之一。作为外交官，他在亚洲和欧洲任职；作为共产党员，他亲历了西班牙内战并写下了《西班牙在我心中》。晚年任智利驻法国大使期间获诺贝尔奖。他最宏大的作品《漫歌》以史诗般的篇幅歌颂了整个美洲大陆。",
  "Neruda began publishing poetry at 13; 'Twenty Love Poems and a Song of Despair,' published at 20, became one of the world's best-selling poetry collections. As a diplomat, he served in Asia and Europe; as a communist, he witnessed the Spanish Civil War and wrote 'Spain in My Heart.' He won the Nobel Prize while serving as ambassador to France. His magnum opus 'Canto General' is an epic celebration of the Americas.",
  [], [], "Q34189", 0.95)

p("garcia-marquez", "加西亚·马尔克斯", "Gabriel García Márquez", 1927, 2014, "americas",
  ["文学", "小说", "魔幻现实主义", "诺贝尔"],
  ["Literature", "Novel", "Magical Realism", "Nobel"],
  "哥伦比亚作家，魔幻现实主义的代表人物，《百年孤独》的作者，诺贝尔文学奖得主。",
  "Colombian writer and the preeminent figure of magical realism, author of 'One Hundred Years of Solitude' and Nobel laureate.",
  "加西亚·马尔克斯早年作为记者游历了拉丁美洲和欧洲。1967年出版的《百年孤独》讲述了布恩迪亚家族七代人的故事，以魔幻现实主义的手法折射了拉丁美洲的百年沧桑。小说在全球畅销超过五千万册。1982年获诺贝尔文学奖。他的其他重要作品包括《霍乱时期的爱情》和《族长的秋天》。",
  "García Márquez traveled across Latin America and Europe as a young journalist. In 1967, 'One Hundred Years of Solitude' — the seven-generation saga of the Buendía family — became the defining work of magical realism and a mirror of Latin America's history. It has sold over 50 million copies worldwide. He received the Nobel Prize in 1982. Other major works include 'Love in the Time of Cholera.'",
  [], [], "Q5878", 0.95)

p("borges", "博尔赫斯", "Jorge Luis Borges", 1899, 1986, "americas",
  ["文学", "诗歌", "哲学", "阿根廷"],
  ["Literature", "Poetry", "Philosophy", "Argentina"],
  "阿根廷作家，20世纪最重要的短篇小说家之一，以迷宫、镜子、无限等主题探索现实与虚构的边界。",
  "Argentine writer and one of the 20th century's most important short story writers, exploring the boundaries of reality and fiction through labyrinths, mirrors, and infinity.",
  "博尔赫斯从青年时代起就近乎失明，但这并未阻碍他成为阿根廷国家图书馆馆长和最博学的作家。他的短篇小说集《虚构集》和《阿莱夫》以哲学深度和精密的文学结构著称，预见了后现代主义的许多思潮。他从未写过长篇小说，但每个短篇都像是被压缩的世界——用他的话说，'长篇小说的想法是贫穷的想法'。",
  "Nearly blind from his youth, Borges nevertheless became director of Argentina's National Library and its most erudite writer. His collections 'Ficciones' and 'The Aleph' are celebrated for their philosophical depth and precise literary architecture, anticipating many postmodernist currents. He never wrote a novel, believing each short story is a compressed world: 'The idea of a long novel is a poor idea.'",
  [], [], "Q909", 0.9)

# ========================================
# SECTION 3: MORE ASIAN FIGURES (Korea, Southeast Asia, Central Asia)
# ========================================

p("wang-geon", "王建", "Wang Geon (Taejo of Goryeo)", 877, 943, "asia",
  ["政治", "朝鲜", "高丽", "开国君主"],
  ["Politics", "Korea", "Goryeo", "Founder"],
  "高丽王朝的建立者，统一了后三国时期的朝鲜半岛，奠定了近五百年高丽王朝的基础。",
  "Founder of the Goryeo Dynasty who unified the Korean Peninsula after the Later Three Kingdoms period, laying the foundation for nearly 500 years of Goryeo rule.",
  "王建出身松岳（今开城）豪族，在后三国（新罗、后百济、泰封）混战中崛起。918年他推翻泰封暴君弓裔，建立高丽王朝。935年新罗末代国王主动归附，936年攻灭后百济，统一了朝鲜半岛。他推行包容政策——吸纳新罗贵族、佛教为国教、鼓励与中国的文化交流——使高丽成为东亚最繁荣的国家之一。",
  "Wang Geon rose from a powerful Songak (Kaesong) family during the Later Three Kingdoms chaos. He overthrew the tyrannical Gung Ye in 918 to found Goryeo. Silla's last king voluntarily submitted in 935, and Wang conquered Later Baekje in 936, unifying the peninsula. His inclusive policies — absorbing Silla aristocracy, adopting Buddhism, encouraging Chinese cultural exchange — made Goryeo one of East Asia's most prosperous states.",
  [], [], "", 0.8)

p("sejong", "世宗大王", "King Sejong the Great", 1397, 1450, "asia",
  ["政治", "语言", "科学", "朝鲜", "训民正音"],
  ["Politics", "Language", "Science", "Korea", "Hangul"],
  "朝鲜王朝第四代国王，创造了训民正音（韩文），推动科学和文化发展，朝鲜历史上最伟大的君主。",
  "The fourth king of the Joseon Dynasty who created Hangul (the Korean alphabet) and advanced science and culture — Korea's greatest monarch.",
  "世宗大王（1418-1450年在位）被视为朝鲜历史上最杰出的君主。最不朽的成就是1443年创制训民正音（今日韩文），让普通民众也能读写。他还发展了活字印刷、制作了农事历书、改进天文仪器、编纂《东国通鉴》等史书。他设立集贤殿，网罗全国才俊进行研究，奠定了朝鲜儒学与科学发展的黄金时代。",
  "King Sejong (r. 1418-1450) is regarded as Korea's greatest monarch. His most enduring achievement is the creation of Hangul in 1443, enabling literacy for common people. He also advanced movable-type printing, produced agricultural almanacs, improved astronomical instruments, and commissioned historical compilations. His Hall of Worthies gathered the nation's brightest minds, ushering in a golden age of Confucian scholarship and science.",
  [], [], "Q37624", 0.9)

p("yi-sun-sin", "李舜臣", "Yi Sun-sin", 1545, 1598, "asia",
  ["军事", "海军", "朝鲜", "龟船"],
  ["Military", "Navy", "Korea", "Turtle Ship"],
  "朝鲜海军名将，在壬辰战争中以寡敌众击败日本海军，从未打过败仗，被视为韩国最伟大的民族英雄。",
  "Joseon naval commander who defeated the Japanese navy against overwhelming odds during the Imjin War, never losing a single battle — Korea's greatest national hero.",
  "李舜臣在1592年丰臣秀吉入侵朝鲜的壬辰战争中成名。他发明的龟船——世界最早的铁甲舰——在闲山岛等海战中屡破日军。他以23战全胜的战绩保卫了朝鲜的海上补给线。然而朝中奸臣诬陷使他一度下狱。1598年最后一战露梁海战中壮烈殉国，临终遗言：'勿令敌人知我死讯。'据传他在被诬陷期间写了著名的《乱中日记》。",
  "Yi Sun-sin rose to fame during Hideyoshi's 1592 invasion of Korea. His turtle ships — the world's first ironclad vessels — repeatedly smashed Japanese fleets at battles like Hansan Island. With 23 victories and zero defeats, he protected Korea's maritime supply lines. Court intrigue landed him in prison, but he was reinstated for the final 1598 Battle of Noryang, where he died heroically — his last words: 'Do not let the enemy know of my death.'",
  [], [], "", 0.85)

p("trung-sisters", "征氏姐妹", "Trung Sisters", 12, 43, "asia",
  ["军事", "女性", "越南", "独立"],
  ["Military", "Women", "Vietnam", "Independence"],
  "越南民族英雄，征侧和征贰姐妹领导了反抗东汉统治的第一次大规模起义，成为越南独立的象征。",
  "Vietnamese national heroines — the Trung sisters (Trung Trac and Trung Nhi) — who led the first large-scale uprising against Han Chinese rule, becoming enduring symbols of Vietnamese independence.",
  "公元40年，因丈夫被东汉太守杀害，征侧与妹妹征贰起兵反抗汉朝统治。她们迅速聚集了数万军队，攻占了65座城池，征侧自立为王。东汉派伏波将军马援率大军镇压，公元43年起义失败，姐妹二人投河自尽。两千年来她们一直是越南民族独立精神的象征，河内至今有征王庙供奉她们。",
  "In 40 CE, after her husband was killed by a Han governor, Trung Trac and her sister Trung Nhi rose against Chinese rule. They quickly rallied tens of thousands, captured 65 citadels, and Trung Trac declared herself queen. The Han sent General Ma Yuan with a massive army; the rebellion fell in 43 CE, and the sisters drowned themselves. For two millennia they have remained Vietnam's preeminent symbols of national independence.",
  [], [], "", 0.7)

p("ho-chi-minh", "胡志明", "Ho Chi Minh", 1890, 1969, "asia",
  ["政治", "独立", "革命", "越南"],
  ["Politics", "Independence", "Revolution", "Vietnam"],
  "越南革命家和国父，领导越南摆脱法国殖民统治和抗击美国，建立越南民主共和国。",
  "Vietnamese revolutionary and founding father who led Vietnam's struggle against French colonial rule and American intervention, establishing the Democratic Republic of Vietnam.",
  "胡志明年轻时做过厨师、海员，游历了欧美多地，在巴黎加入法国共产党。1941年他回到越南创立越盟，领导抗日和抗法斗争。1945年日本投降后他在河内宣布越南独立，发表独立宣言（引用美国独立宣言的语句）。此后他领导了三十年的民族解放战争——先是对法国，后是对美国——直至生命的最后。",
  "Ho Chi Minh worked as a cook and sailor, traveling across Europe and America, joining the French Communist Party in Paris. Returning to Vietnam in 1941, he founded the Viet Minh and led resistance against Japan and France. In 1945, after Japan's surrender, he declared Vietnamese independence in Hanoi — quoting the US Declaration of Independence in his speech. He then led three decades of national liberation: first against France, then America.",
  [], [], "", 0.9)

p("sukarno", "苏加诺", "Sukarno", 1901, 1970, "asia",
  ["政治", "独立", "印尼", "不结盟运动"],
  ["Politics", "Independence", "Indonesia", "Non-Aligned"],
  "印度尼西亚独立运动领袖和首任总统，1955年万隆会议的发起者，不结盟运动的奠基人之一。",
  "Leader of Indonesian independence and its first president, initiator of the 1955 Bandung Conference and co-founder of the Non-Aligned Movement.",
  "苏加诺从20世纪20年代开始领导印尼民族主义运动，数次被荷兰殖民当局逮捕流放。日本占领期间他与日本人合作以争取独立。1945年他宣布印尼独立，此后领导了四年武装斗争直至荷兰承认印尼主权。1955年他发起万隆会议——亚非29国首次联合发声，开创了'第三世界'的新国际秩序。1965年政变后被苏哈托逐步剥夺权力。",
  "Sukarno led Indonesia's nationalist movement from the 1920s, enduring multiple arrests and exiles under Dutch colonial rule. During Japanese occupation, he cooperated strategically for independence. He proclaimed independence in 1945, then led four years of armed struggle until Dutch recognition. The 1955 Bandung Conference — 29 Asian-African nations speaking as one — inaugurated the 'Third World' in international politics. He was gradually stripped of power after 1965's coup.",
  [], [], "", 0.9)

p("aung-san", "昂山", "Aung San", 1915, 1947, "asia",
  ["政治", "独立", "缅甸"],
  ["Politics", "Independence", "Myanmar"],
  "缅甸独立运动领袖，民族英雄，在缅甸即将独立前夕被暗杀，被誉为'缅甸国父'。",
  "Burmese independence leader and national hero, assassinated on the eve of independence, revered as the 'Father of Myanmar.'",
  "昂山在仰光大学求学期间成为学生运动领袖。二战期间他先与日本人合作组建缅甸独立军，后转向盟军阵营。战后他以卓越的外交才能与英国谈判独立事宜，1947年签订了确认缅甸独立的《昂山-艾德礼协定》。同年7月，他和六位内阁成员在开会时被政敌派枪手暗杀——距缅甸独立仅六个月。他的女儿昂山素季后来也成为缅甸民主运动的象征。",
  "Aung San became a student leader at Rangoon University. During WWII, he first collaborated with Japan to form the Burma Independence Army, then switched to the Allied side. Postwar, he skillfully negotiated independence with Britain, signing the Aung San-Attlee Agreement in 1947. That July, he and six cabinet members were assassinated by political rivals — just six months before Burmese independence. His daughter Aung San Suu Kyi later became the symbol of Myanmar's democracy movement.",
  [], [], "", 0.85)

p("jayavarman-vii", "阇耶跋摩七世", "Jayavarman VII", 1122, 1218, "asia",
  ["政治", "建筑", "佛教", "高棉帝国"],
  ["Politics", "Architecture", "Buddhism", "Khmer Empire"],
  "高棉帝国最伟大的国王之一，建造了吴哥通城和巴戎寺，将帝国从印度教转向大乘佛教。",
  "One of the Khmer Empire's greatest kings who built Angkor Thom and the Bayon Temple, shifting the empire from Hinduism to Mahayana Buddhism.",
  "阇耶跋摩七世在占婆人洗劫吴哥后于1181年登上王位。他击退了占婆入侵，并在位期间发动了一系列建筑工程——最著名的是吴哥通城（大吴哥）和其中的巴戎寺，寺塔上雕刻着闻名于世的四面'高棉微笑'佛像。他将国教从印度教改为大乘佛教，大量修建医院、驿站和水库——以佛教的慈悲理念治理国家。",
  "Jayavarman VII ascended in 1181 after the Cham sacked Angkor. He repelled Cham invasions and launched a massive building program — most famously Angkor Thom (the Great City) and the Bayon Temple with its iconic four-faced 'Khmer smile' Buddha sculptures. He converted the state religion from Hinduism to Mahayana Buddhism and built hospitals, rest houses, and reservoirs — governing through Buddhist compassion.",
  [], [], "", 0.8)

p("timur", "帖木儿", "Timur (Tamerlane)", 1336, 1405, "middle-east",
  ["军事", "帝国", "中亚", "征服者"],
  ["Military", "Empire", "Central Asia", "Conqueror"],
  "突厥化蒙古征服者，建立帖木儿帝国，以撒马尔罕为首都，其军事征服横跨中亚、波斯和印度。",
  "Turco-Mongol conqueror who founded the Timurid Empire, made Samarkand his capital, and conducted military campaigns across Central Asia, Persia, and India.",
  "帖木儿自称成吉思汗的后裔（虽然血统存疑），在察合台汗国废墟上崛起。他终身跛足（'跛子帖木儿'之名由此而来），但这并未阻碍他成为历史上最残暴也最辉煌的征服者之一。他的军队从德里烧到大马士革，从莫斯科打到安卡拉——在安卡拉战役中俘虏了奥斯曼苏丹巴耶济德一世。他在撒马尔罕汇集了各地的工匠和学者，建立了帖木儿文艺复兴。",
  "Timur claimed descent from Genghis Khan (though the lineage is disputed) and rose from the Chagatai Khanate's ruins. Lame from an arrow wound ('Timur the Lame' = Tamerlane), he nonetheless became one of history's most brilliant and brutal conquerors. His armies ranged from Delhi to Damascus, from Moscow to Ankara — where he captured the Ottoman Sultan Bayezid. In Samarkand, he gathered artisans and scholars from across his realm, sparking the Timurid Renaissance.",
  [], [], "", 0.85)

p("ulugh-beg", "兀鲁伯", "Ulugh Beg", 1394, 1449, "middle-east",
  ["科学", "天文学", "数学", "帖木儿"],
  ["Science", "Astronomy", "Mathematics", "Timurid"],
  "帖木儿帝国苏丹和天文学家，建造了撒马尔罕天文台，编制了中世纪最精确的星表。",
  "Timurid Sultan and astronomer who built the Samarkand Observatory and compiled the most accurate star catalog of the medieval period.",
  "兀鲁伯是帖木儿的孙子，但他对天文学的热爱远胜于征服。他在撒马尔罕建造了当时世界最大的六分仪（半径40米），带领团队测定了1018颗恒星的位置——精度在前望远镜时代无与伦比。他的《兀鲁伯星表》被翻译成拉丁文后影响了欧洲天文学。但他的科学追求与统治职责的矛盾最终导致悲剧：1449年被自己的儿子杀害。",
  "Ulugh Beg was Timur's grandson, but his passion lay in astronomy, not conquest. He built the world's largest sextant (40-meter radius) in Samarkand and with his team catalogued 1,018 stars with pre-telescope precision unmatched for centuries. His 'Zij-i Sultani' star tables, translated into Latin, influenced European astronomy. The tension between science and rule proved fatal: his own son had him killed in 1449.",
  [], [], "", 0.85)

p("al-khwarizmi", "花剌子密", "Al-Khwarizmi", 780, 850, "middle-east",
  ["科学", "数学", "天文学", "伊斯兰黄金时代"],
  ["Science", "Mathematics", "Astronomy", "Islamic Golden Age"],
  "波斯数学家和天文学家，'代数之父'，拉丁化名字成为了'算法'一词的来源。",
  "Persian mathematician and astronomer, the 'father of algebra' whose Latinized name gave us the word 'algorithm.'",
  "花剌子密在巴格达智慧之家工作，吸收了印度和希腊的数学传统。他的《代数学》一书系统阐述了二次方程的解法和代数运算，首次将代数作为独立学科呈现。'代数'一词就源自他书名中的'al-jabr'。他的另一部著作介绍了印度的十进制计数法，通过拉丁文译本传入欧洲。他的名字'al-Khwarizmi'拉丁化后成为'Algorithmi'——今日'算法'的词源。",
  "Al-Khwarizmi worked at Baghdad's House of Wisdom, synthesizing Indian and Greek mathematical traditions. His 'Kitab al-Jabr' systematically presented solutions to quadratic equations and algebraic operations, establishing algebra as an independent discipline — the word 'algebra' derives from 'al-jabr' in his title. Another work introduced the Indian decimal system to Europe through Latin translations. His name, Latinized as 'Algorithmi,' is the origin of today's 'algorithm.'",
  [], [], "", 0.85)

p("ibn-sina", "伊本·西那（阿维森纳）", "Ibn Sina (Avicenna)", 980, 1037, "middle-east",
  ["哲学", "医学", "科学", "伊斯兰黄金时代"],
  ["Philosophy", "Medicine", "Science", "Islamic Golden Age"],
  "波斯博学家，'医学之父'，《医典》在欧亚被用作标准医学教科书长达六百年。",
  "Persian polymath and 'father of medicine' whose 'Canon of Medicine' served as the standard medical textbook across Eurasia for six centuries.",
  "伊本·西那（拉丁名阿维森纳）是伊斯兰黄金时代的百科全书式学者。他的《医典》综合了希腊、波斯和印度医学知识，系统论述了数百种疾病的诊断和治疗，在欧洲和伊斯兰世界被奉为权威达六百年之久。在哲学上他调和亚里士多德与伊斯兰一神论，深刻影响了中世纪的基督教经院哲学——但丁《神曲》中将他置于冥界第一层，与柏拉图亚里士多德为伴。",
  "Ibn Sina (Avicenna) was the encyclopedic genius of the Islamic Golden Age. His 'Canon of Medicine' synthesized Greek, Persian, and Indian medical knowledge, systematically covering hundreds of diseases — serving as the authoritative medical text in both Europe and the Islamic world for six centuries. In philosophy, he reconciled Aristotle with Islamic monotheism, profoundly influencing medieval Christian scholasticism. Dante placed him in Limbo alongside Plato and Aristotle.",
  [], [], "Q8011", 0.9)

p("ibn-rushd", "伊本·鲁世德（阿威罗伊）", "Ibn Rushd (Averroes)", 1126, 1198, "middle-east",
  ["哲学", "医学", "法学", "伊斯兰黄金时代"],
  ["Philosophy", "Medicine", "Law", "Islamic Golden Age"],
  "安达卢西亚哲学家和法学家，亚里士多德著作最伟大的注释者，对欧洲经院哲学影响深远。",
  "Andalusian philosopher and jurist, Aristotle's greatest commentator, who profoundly influenced European scholasticism.",
  "伊本·鲁世德（拉丁名阿威罗伊）生于科尔多瓦，曾任首席法官和宫廷御医。他的亚里士多德注疏成为了中世纪欧洲经院哲学的标准参考——'阿威罗伊主义'引发了一场思想革命。他主张哲学与宗教并不矛盾：两者以不同方式通往同一真理。'双重真理'说在巴黎大学引发激烈争论。拉斐尔的《雅典学院》中描绘了他——与亚里士多德、柏拉图为伴的东方哲学家。",
  "Born in Cordoba, Ibn Rushd (Averroes) served as chief judge and court physician. His commentaries on Aristotle became the standard reference for medieval European scholasticism — 'Averroism' sparked an intellectual revolution. He argued philosophy and religion are not contradictory: both lead to the same truth by different paths. His 'double truth' theory ignited fierce debates at the University of Paris. Raphael's 'School of Athens' includes him among the great philosophers.",
  [], [], "Q36537", 0.9)

p("omar-khayyam", "欧玛尔·海亚姆", "Omar Khayyam", 1048, 1131, "middle-east",
  ["诗歌", "数学", "天文学", "波斯"],
  ["Poetry", "Mathematics", "Astronomy", "Persia"],
  "波斯诗人、数学家和天文学家，《鲁拜集》的作者，同时解决了三次方程的几何解法。",
  "Persian poet, mathematician, and astronomer, author of the 'Rubaiyat,' who simultaneously solved cubic equations geometrically.",
  "海亚姆在数学上的成就——解决三次方程的几何解法、改革历法——在当时堪称顶尖。但他对世界最深远的影响来自诗歌。《鲁拜集》以四行诗的形式咏叹人生的短暂、命运的无常和及时行乐的智慧。'一杯酒、一块面包和你'成为世界诗歌中最著名的意象之一。英国诗人菲茨杰拉德的翻译使他在西方名声大噪——尽管翻译更多是再创作。",
  "Khayyam's mathematical achievements — geometrically solving cubic equations, reforming the calendar — were cutting-edge. But his deepest impact came from poetry. The 'Rubaiyat,' composed in quatrains, meditates on life's brevity, fate's caprice, and carpe diem wisdom. 'A jug of wine, a loaf of bread — and thou' became one of world poetry's most famous images. Edward FitzGerald's celebrated English translation — more re-creation than translation — made him a Western phenomenon.",
  [], [], "Q35900", 0.9)

# ========================================
# OUTPUT
# ========================================
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
