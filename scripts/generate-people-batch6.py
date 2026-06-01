#!/usr/bin/env python3
"""Batch 6: ~120 new Asian people — Chinese dynasties, Japan, Korea, India, SEA, Middle East"""
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

# ===== Chinese dynasties (30) =====
p("qin-shi-huang", "秦始皇", "Qin Shi Huang", -259, -210, "china",
  ["政治", "帝国", "统一", "秦朝"],
  ["Politics", "Empire", "Unification", "Qin Dynasty"],
  "中国历史上第一位皇帝，统一六国，建立了中国第一个中央集权的帝国，以兵马俑和焚书坑儒闻名。",
  "The first emperor of China who unified the Six Kingdoms, established China's first centralized empire, and is known for the Terracotta Army and the burning of books.",
  "嬴政13岁即位为秦王，22岁亲政后迅速灭掉六国，公元前221年统一了中国。他推行郡县制替代分封，统一文字、度量衡和车轨，北筑长城南征百越。但他也焚毁百家之书、坑杀儒生以统一思想，建造阿房宫和骊山陵（兵马俑为其陪葬）耗尽民力。公元前210年在出巡途中死于沙丘——随行的赵高和李斯篡改遗诏立胡亥为帝，秦朝二世而亡。",
  "Ying Zheng ascended the Qin throne at 13, personally assumed power at 22, and swiftly conquered the Six Kingdoms, unifying China in 221 BCE. He replaced feudal enfeoffment with commandery-county administration, standardized writing, measures, and axle widths, built the Great Wall northward, and conquered the Baiyue southward. But he also burned books and buried scholars alive to enforce ideological uniformity, and exhausted the people building the Epang Palace and Mount Li mausoleum (guarded by the Terracotta Army). He died at Shaqiu in 210 BCE while on imperial tour; accompanying officials Zhao Gao and Li Si forged his will to install Hu Hai as emperor — the Qin dynasty collapsed within three years.",
  [], [], "", 0.9)

p("han-wudi", "汉武帝", "Emperor Wu of Han", -156, -87, "china",
  ["政治", "军事", "汉朝", "丝绸之路"],
  ["Politics", "Military", "Han Dynasty", "Silk Road"],
  "西汉第七位皇帝，在位54年，北击匈奴、开通西域、独尊儒术，把汉朝推向鼎盛。",
  "The seventh emperor of Western Han, reigning 54 years, who defeated the Xiongnu, opened the Western Regions, and established Confucianism as state ideology, propelling Han to its zenith.",
  "刘彻16岁即位。他派卫青和霍去病北击匈奴，彻底解除了北方游牧民族的威胁；派张骞出使西域，开通了丝绸之路。在国内他接受董仲舒的建议'罢黜百家，独尊儒术'——确立儒学作为官方意识形态近两千年。但他晚年因'巫蛊之祸'导致太子起兵被杀，自己也陷入了深深的悔恨和反思之中。他下'轮台罪己诏'反思穷兵黩武之过。",
  "Liu Che ascended the throne at 16. He sent Wei Qing and Huo Qubing north to crush the Xiongnu, permanently removing the nomadic threat; he dispatched Zhang Qian to the Western Regions, opening the Silk Road. Domestically, he adopted Dong Zhongshu's advice to 'revere only Confucianism and proscribe all other schools' — establishing Confucianism as state orthodoxy for nearly two millennia. In his final years, the 'Witchcraft Scandal' led to the Crown Prince's rebellion and death, plunging the emperor into profound remorse. He issued the 'Luntai Edict of Self-Reproach' reflecting on the errors of his expansionist wars.",
  [], [], "", 0.9)

p("zhuge-liang", "诸葛亮", "Zhuge Liang", 181, 234, "china",
  ["军事", "政治", "三国", "蜀汉"],
  ["Military", "Politics", "Three Kingdoms", "Shu Han"],
  "三国时期蜀汉丞相，中国历史上最著名的谋略家和政治家之一，以'鞠躬尽瘁，死而后已'的精神流芳百世。",
  "Chancellor of Shu Han during the Three Kingdoms period, one of China's most celebrated strategists and statesmen, remembered for his spirit of 'giving one's all until death.'",
  "诸葛亮隐居隆中时被刘备三顾茅庐请出山。他为刘备规划了'隆中对'——占据荆益二州联吴抗曹的战略蓝图。赤壁之战中他出使东吴促成孙刘联盟。刘备去世后他受遗诏辅佐后主刘禅，总揽朝政。他平定南中叛乱，六出祁山北伐中原——但每次都因粮草不继而被迫退兵。234年在五丈原军中病逝，真正做到了'鞠躬尽瘁，死而后已'。",
  "Zhuge Liang was living in seclusion at Longzhong when Liu Bei visited him three times to recruit him. He devised the 'Longzhong Plan' — a strategic blueprint to occupy Jing and Yi provinces and ally with Wu against Cao Wei. At the Battle of Red Cliffs, he brokered the Sun-Liu alliance. After Liu Bei's death, he governed as regent for the young Liu Shan. He pacified the southern rebellion and launched six northern expeditions against Wei from Mount Qi — each time forced to retreat by supply shortages. He died of illness at Wuzhang Plains in 234, truly embodying his vow to 'give his all until his last breath.'",
  [], [], "", 0.85)

p("cao-cao", "曹操", "Cao Cao", 155, 220, "china",
  ["军事", "政治", "文学", "三国", "曹魏"],
  ["Military", "Politics", "Literature", "Three Kingdoms", "Cao Wei"],
  "东汉末年杰出的军事家、政治家和诗人，三国曹魏政权的奠基者，'治世之能臣，乱世之奸雄'。",
  "Outstanding military leader, statesman, and poet of the late Eastern Han, founder of the Cao Wei state, described as 'a capable minister in peaceful times, a cunning hero in chaotic times.'",
  "曹操出身宦官家庭，黄巾起义时崭露头角。196年他迎汉献帝于许昌——'挟天子以令诸侯'——占据了政治上的主动权。官渡之战以少胜多击败袁绍，统一了北方。但他南征时在赤壁被孙刘联军击败，三国鼎立的格局由此形成。曹操不仅是军事家——他的诗作《短歌行》《观沧海》《龟虽寿》是建安文学的代表，慷慨悲凉、气韵沉雄。",
  "Born to a eunuch family, Cao Cao rose to prominence during the Yellow Turban Rebellion. In 196, he took Emperor Xian under his protection in Xuchang — 'holding the emperor to command the feudal lords' — gaining political initiative. He defeated Yuan Shao at the Battle of Guandu against overwhelming odds, unifying the north. But his southern campaign was thwarted at Red Cliffs by the Sun-Liu alliance, establishing the Three Kingdoms pattern. Cao Cao was not only a military leader — his poems such as 'Short Song Style,' 'Gazing at the Blue Sea,' and 'Though the Tortoise Lives Long' are highpoints of Jian'an literature: heroic, somber, and powerful.",
  [], [], "", 0.9)

p("li-bai", "李白", "Li Bai", 701, 762, "tang-dynasty",
  ["文学", "诗歌", "唐朝"],
  ["Literature", "Poetry", "Tang Dynasty"],
  "唐代最伟大的浪漫主义诗人，'诗仙'，以豪放飘逸的诗风和超凡脱俗的想象力著称。",
  "The greatest Romantic poet of the Tang Dynasty, known as the 'Immortal of Poetry,' celebrated for his free-spirited style and transcendent imagination.",
  "李白自称是李广的后裔，一生大部分时间在漫游中度过。他的诗歌充满了对自然、酒和自由的赞美——'天生我材必有用，千金散尽还复来'——以及对仙境的瑰丽想象。唐玄宗曾召他入宫供奉翰林，但李白不拘礼法的性格使他很快被'赐金放还'。传说他在安徽当涂酒醉后跳入水中捞月而溺亡——这个浪漫的传说比他真实的死亡更配他的诗意人生。",
  "Li Bai claimed descent from the Han general Li Guang and spent most of his life wandering. His poetry brims with celebration of nature, wine, and freedom — 'Heaven gave me talents for a purpose; a thousand gold coins spent, they'll come back again' — and dazzling visions of immortal realms. Emperor Xuanzong summoned him to court as a Hanlin academician, but his free-spirited character quickly led to his dismissal with a 'golden handshake.' Legend says he drowned while drunkenly trying to embrace the moon's reflection in a river — a romantic end far more fitting to his poetic life than historical fact.",
  [], [], "Q7071", 0.9)

p("du-fu", "杜甫", "Du Fu", 712, 770, "tang-dynasty",
  ["文学", "诗歌", "唐朝"],
  ["Literature", "Poetry", "Tang Dynasty"],
  "唐代最伟大的现实主义诗人，'诗圣'，以沉郁顿挫的风格深刻记录了安史之乱前后的社会苦难。",
  "The greatest realist poet of the Tang Dynasty, known as the 'Sage of Poetry,' who deeply recorded social suffering before and after the An Lushan Rebellion.",
  "杜甫的一生恰逢唐朝由盛转衰的转折点——安史之乱。他早年漫游豪放，中年目睹了战争的惨烈和人民的苦难，诗风转向沉郁顿挫。《春望》中'国破山河在，城春草木深'、《三吏》《三别》中对战乱中普通百姓的同情，使他成为'诗史'——用诗歌记录了时代的悲欢。他晚年漂泊西南，在成都筑草堂而居，最终在一条破船上贫病而终。",
  "Du Fu's life coincided with the Tang dynasty's turning point from prosperity to decline — the An Lushan Rebellion. His early years were carefree and wandering; in middle age, witnessing war's brutality and the people's suffering, his style turned grave and profound. 'The nation is shattered, yet hills and rivers remain; spring fills the city, grass and trees grow dense' from 'Spring View,' and his 'Three Officials' and 'Three Partings' expressing compassion for common people in wartime, earned him the title 'poet-historian' — chronicling his era's joys and sorrows in verse. In his final years he wandered in the southwest, built a thatched cottage in Chengdu, and died in poverty and illness on a broken boat.",
  [], [], "Q33772", 0.9)

p("yue-fei", "岳飞", "Yue Fei", 1103, 1142, "song-dynasty",
  ["军事", "民族英雄", "南宋"],
  ["Military", "National Hero", "Southern Song"],
  "南宋抗金名将，中国历史上最著名的民族英雄之一，以'精忠报国'的精神和冤死风波亭的悲剧闻名。",
  "Southern Song general who led the resistance against Jin invaders, one of China's most celebrated national heroes, remembered for his 'serve the country with utmost loyalty' spirit and tragic execution.",
  "岳飞在北宋灭亡后加入抗金队伍，率领岳家军屡次击败金军——'撼山易，撼岳家军难'。他收复了大量失地，一度打到距故都开封仅四十五里的朱仙镇。但宋高宗和宰相秦桧一心求和，以十二道金牌将他从前线召回，以'莫须有'的罪名在风波亭处死。二十年后平反，至今西湖边的岳王庙香火不断——秦桧夫妇的铁铸跪像世世代代受人唾弃。",
  "After the fall of Northern Song, Yue Fei joined the resistance and led the 'Yue Family Army' to repeated victories over the Jin — 'It is easier to shake a mountain than the Yue army.' He recovered vast territories and once advanced to Zhuxian Town, just 22 kilometers from the old capital Kaifeng. But Emperor Gaozong and Chancellor Qin Hui, bent on peace, recalled him from the front with twelve imperial gold tablets and executed him at Wind and Wave Pavilion on the fabricated charge of 'maybe there was something.' He was posthumously rehabilitated 20 years later; his temple by West Lake in Hangzhou still receives constant visitors — while the iron kneeling statues of Qin Hui and his wife are cursed by generation after generation.",
  [], [], "", 0.9)

p("zheng-he", "郑和", "Zheng He", 1371, 1433, "ming-dynasty",
  ["航海", "探索", "外交", "明朝"],
  ["Navigation", "Exploration", "Diplomacy", "Ming Dynasty"],
  "明朝太监和航海家，七次率领庞大舰队下西洋，到达了东南亚、印度、阿拉伯和东非。",
  "Ming dynasty eunuch and navigator who led seven massive maritime expeditions to Southeast Asia, India, Arabia, and East Africa.",
  "郑和原名马和，是云南穆斯林，幼年被明军俘虏后阉为太监。他忠诚服务于永乐帝朱棣——因在靖难之役中立功而受重用。1405年他率领由300多艘船只、27000余人组成的庞大船队首次下西洋。在28年间他七次出航，最远到达非洲东海岸和红海。他的宝船据记载长达100多米——是当时世界最大的船只。1433年第七次下西洋途中病逝。",
  "Born Ma He to a Muslim family in Yunnan, he was captured as a boy by Ming forces and castrated to serve as a eunuch. He served Yongle Emperor Zhu Di loyally and was rewarded for his role in the Jingnan Campaign. In 1405 he led the first of seven voyages with a fleet of over 300 ships and 27,000 men. Over 28 years, his seven expeditions reached as far as the east coast of Africa and the Red Sea. His treasure ships, recorded as over 100 meters long, were the largest vessels in the world at the time. He died during the seventh voyage in 1433.",
  [], [], "", 0.9)

p("kangxi", "康熙帝", "Kangxi Emperor", 1654, 1722, "china",
  ["政治", "军事", "清朝"],
  ["Politics", "Military", "Qing Dynasty"],
  "清朝第四位皇帝，在位61年——中国历史上在位时间最长的皇帝，开创了康乾盛世的基业。",
  "The fourth emperor of the Qing Dynasty, reigning 61 years — the longest-reigning emperor in Chinese history — who laid the foundations of the High Qing era.",
  "康熙8岁即位，14岁亲政后迅速铲除权臣鳌拜。他平定三藩之乱、收复台湾、击退沙俄（签订《尼布楚条约》）、三次亲征准噶尔——巩固了清朝对全中国的统治和多民族帝国的疆域。他热衷学习——通晓满汉蒙藏多种语言，主持编纂《康熙字典》和《古今图书集成》。他六次南巡、开放海禁，并邀请西方传教士入宫教授天文数学，但同时以'礼仪之争'为由限制基督教传播。",
  "Kangxi ascended at 8 and assumed personal rule at 14, swiftly eliminating the powerful regent Oboi. He suppressed the Revolt of the Three Feudatories, recovered Taiwan, repelled Russia (signing the Treaty of Nerchinsk), and personally led three campaigns against the Dzungars — consolidating Qing rule over all China and its multi-ethnic imperial borders. Passionate about learning, he mastered Manchu, Chinese, Mongolian, and Tibetan, and commissioned the 'Kangxi Dictionary' and 'Complete Collection of Illustrations and Writings.' He made six southern tours, lifted the maritime ban, and invited Jesuit missionaries to teach astronomy and mathematics — while simultaneously restricting Christianity over the Rites Controversy.",
  [], [], "", 0.9)

p("cixi", "慈禧太后", "Empress Dowager Cixi", 1835, 1908, "china",
  ["政治", "女性", "清朝"],
  ["Politics", "Women", "Qing Dynasty"],
  "清朝的实际统治者长达47年，是中国近代史上最有权势也最具争议的女性。",
  "The de facto ruler of Qing China for 47 years, the most powerful and controversial woman in modern Chinese history.",
  "慈禧以咸丰帝妃子身份入宫，在同治帝年幼时发动政变夺取权力，从此'垂帘听政'近半个世纪。她一面推动洋务运动——支持曾国藩、李鸿章等改革派引进西方技术，一面又极度保守——扼杀了戊戌维新，囚禁光绪皇帝于瀛台。1900年她支持义和团向列强宣战，八国联军攻入北京后仓皇西逃——清朝的最后一点底气也在这场浩劫中丧失殆尽。",
  "Cixi entered the palace as a consort of the Xianfeng Emperor, then seized power in a coup when her son, the Tongzhi Emperor, was still a child — thereafter ruling 'from behind the curtain' for nearly half a century. She simultaneously promoted the Self-Strengthening Movement — backing reformers like Zeng Guofan and Li Hongzhang — while being deeply conservative, crushing the Hundred Days' Reform and imprisoning the Guangxu Emperor. In 1900 she backed the Boxer Rebellion and declared war on foreign powers, then fled in panic when the Eight-Nation Alliance captured Beijing — the Qing's last shred of authority was lost in this catastrophe.",
  [], [], "", 0.9)

p("sun-yat-sen", "孙中山", "Sun Yat-sen", 1866, 1925, "china",
  ["政治", "革命", "民国", "国父"],
  ["Politics", "Revolution", "Republic of China", "Father of the Nation"],
  "中国民主革命的先行者，推翻了两千多年的帝制，建立了亚洲第一个共和国——中华民国。",
  "Pioneer of China's democratic revolution who overthrew over two millennia of imperial rule and founded Asia's first republic — the Republic of China.",
  "孙中山早年学医，后来投身推翻清朝的革命。1894年他在檀香山创立兴中会。1905年联合各革命团体在东京成立同盟会，提出了'驱除鞑虏，恢复中华，创立民国，平均地权'的革命纲领和三民主义思想。1911年武昌起义成功后他当选为中华民国临时大总统。但不久后被迫将总统职位让给袁世凯。此后他继续为维护共和而奋斗，提出联俄联共扶助农工的三大政策。1925年在北京病逝。",
  "Sun Yat-sen studied medicine before dedicating himself to overthrowing the Qing dynasty. In 1894 he founded the Revive China Society in Honolulu. In 1905 he united revolutionary groups in Tokyo to form the Tongmenghui (United League), advocating 'expel the Manchus, restore China, establish a republic, and equalize land rights' and his Three Principles of the People. After the 1911 Wuchang Uprising, he was elected provisional president of the Republic of China — but soon had to cede the presidency to Yuan Shikai. He continued fighting to preserve the republic, later proposing the Three Great Policies of alliance with Russia and the communists and support for peasants and workers. He died in Beijing in 1925.",
  [], [], "Q8573", 0.95)

p("lu-xun", "鲁迅", "Lu Xun", 1881, 1936, "china",
  ["文学", "思想", "现代中国"],
  ["Literature", "Thought", "Modern China"],
  "中国现代文学的奠基人，《狂人日记》《阿Q正传》的作者，以犀利的笔触批判国民性和社会弊病。",
  "Founder of modern Chinese literature and author of 'A Madman's Diary' and 'The True Story of Ah Q,' celebrated for his piercing critique of national character and social ills.",
  "鲁迅原名周树人，早年在日本学医——观看日俄战争幻灯片时他意识到'医治国民的精神'比医治身体更重要，从此弃医从文。1918年他在《新青年》上发表了中国第一篇白话小说《狂人日记》，以'救救孩子'的呐喊震撼了文坛。《阿Q正传》以精神胜利法这一形象深刻揭示了国民性的弱点。他的杂文犹如投枪匕首，直指时弊。1936年去世时棺木上覆盖着'民族魂'的旗帜。",
  "Lu Xun, born Zhou Shuren, studied medicine in Japan — but while watching a slide show of the Russo-Japanese War, he realized that 'curing the national spirit' mattered more than curing bodies, and abandoned medicine for literature. In 1918 he published China's first vernacular short story 'A Madman's Diary' in 'New Youth' magazine, shaking the literary world with its closing cry of 'Save the children!' 'The True Story of Ah Q' exposed weaknesses in the national character through the concept of 'spiritual victory.' His essays were like daggers aimed at contemporary ills. When he died in 1936, his coffin was draped with a banner reading 'Soul of the Nation.'",
  [], [], "Q23114", 0.95)

p("mao-zedong", "毛泽东", "Mao Zedong", 1893, 1976, "china",
  ["政治", "革命", "新中国", "共产党"],
  ["Politics", "Revolution", "New China", "Communist Party"],
  "中国共产党、中国人民解放军和中华人民共和国的主要创立者，深刻改变了20世纪中国的历史进程。",
  "The principal founder of the Communist Party of China, the People's Liberation Army, and the People's Republic of China, who profoundly transformed 20th-century Chinese history.",
  "毛泽东出身湖南农民家庭，1921年参加中共一大，成为党的创始人之一。他领导了秋收起义，在井冈山开辟了农村包围城市的革命道路。长征中遵义会议确立了他的领导地位。1949年10月1日他在天安门城楼上宣布中华人民共和国成立。在他的领导下中国进行了土地改革、抗美援朝和社会主义改造。晚年他发动了'文化大革命'——这一时期至今仍是中国现代史上最具争议的篇章。",
  "Born to a Hunan peasant family, Mao attended the CPC's First Congress in 1921, becoming a party founder. He led the Autumn Harvest Uprising and pioneered the strategy of encircling the cities from the countryside at Jinggangshan. During the Long March, the Zunyi Conference established his leadership. On October 1, 1949, he proclaimed the founding of the People's Republic of China from Tiananmen. Under his leadership, China conducted land reform, fought in the Korean War, and carried out socialist transformation. In his later years, he launched the Cultural Revolution — a period that remains the most contested chapter in modern Chinese history.",
  [], [], "Q5816", 0.95)

p("deng-xiaoping", "邓小平", "Deng Xiaoping", 1904, 1997, "china",
  ["政治", "改革开放", "现代化"],
  ["Politics", "Reform and Opening", "Modernization"],
  "中国改革开放的总设计师，将中国从计划经济转向市场经济，开启了人类历史上最大规模的经济腾飞。",
  "The chief architect of China's reform and opening-up, who transitioned China from a planned economy to a market economy, launching the largest economic takeoff in human history.",
  "邓小平在文革中两次被打倒又两次复出——他的名言'不管黑猫白猫，捉到老鼠就是好猫'体现了他的务实精神。1978年十一届三中全会后他成为实际最高领导人，推行改革开放政策：农村实行家庭联产承包责任制，设立经济特区引进外资。1984年他会见英国首相撒切尔夫人敲定了香港'一国两制'的回归方案——'主权问题不是一个可以讨论的问题。'1992年南巡讲话再次推动了市场化改革。",
  "Deng was twice purged and twice rehabilitated during the Cultural Revolution — his famous maxim 'It does not matter whether a cat is black or white, as long as it catches mice' captures his pragmatism. After the 1978 Third Plenum, he became de facto top leader and launched reform and opening-up: household responsibility system in agriculture, special economic zones to attract foreign investment. In 1984 he met British PM Thatcher to finalize Hong Kong's handover under 'one country, two systems' — declaring that 'sovereignty is not a matter for discussion.' His 1992 Southern Tour speeches re-ignited market-oriented reforms.",
  [], [], "Q16977", 0.95)

# ===== More Chinese (5) =====
p("bai-juyi", "白居易", "Bai Juyi", 772, 846, "tang-dynasty",
  ["文学", "诗歌", "唐朝"],
  ["Literature", "Poetry", "Tang Dynasty"],
  "唐代诗人，以通俗易懂的语言创作了大量反映民生疾苦和社会现实的诗歌，《长恨歌》为其代表作。",
  "Tang Dynasty poet who wrote in deliberately accessible language about the hardships of ordinary people, with 'Song of Everlasting Sorrow' as his masterpiece.",
  "白居易是唐代创作量最丰富的诗人之一——现存诗近三千首。他刻意追求语言的平易近人，据说每写一首诗都要读给老妇人听，听不懂就改。他的讽喻诗如《卖炭翁》揭露了社会不公，《琵琶行》以'同是天涯沦落人，相逢何必曾相识'的深沉共鸣打动了无数读者。《长恨歌》以唐玄宗与杨贵妃的爱情悲剧为题材，是中国叙事诗的巅峰。",
  "Bai Juyi was one of the Tang's most prolific poets — nearly 3,000 of his poems survive. He deliberately pursued accessible language; legend says he read each poem to an old woman and revised anything she couldn't understand. His satirical poems like 'The Old Charcoal Seller' exposed social injustice, while 'Song of the Pipa' — with its famous line 'Both of us are strangers here, drifting at the world's end; why need we have known each other before we met?' — moved countless readers. 'Song of Everlasting Sorrow,' set to the tragic love of Emperor Xuanzong and Yang Guifei, is the apex of Chinese narrative poetry.",
  [], [], "", 0.9)

p("li-qingzhao", "李清照", "Li Qingzhao", 1084, 1155, "song-dynasty",
  ["文学", "诗词", "女性", "南宋"],
  ["Literature", "Poetry", "Women", "Southern Song"],
  "中国文学史上最杰出的女词人，婉约派的代表人物，以细腻的情感和精湛的词艺著称。",
  "The most outstanding female poet in Chinese literary history and a leading figure of the 'delicate restraint' school, celebrated for her exquisite emotional refinement.",
  "李清照出身书香门第，与丈夫赵明诚共同热衷于金石收藏和研究。靖康之变后北宋灭亡，她随南宋朝廷南渡——颠沛流离中丈夫去世，毕生收藏的书画金石也散失殆尽。她的前期词作清新婉约，如'知否？知否？应是绿肥红瘦'；南渡后词风转为沉痛苍凉，如'寻寻觅觅，冷冷清清，凄凄惨惨戚戚'——叠字的运用在中国诗词中空前绝后。",
  "Born to a literary family, Li Qingzhao shared a passion for bronze and stone inscription collecting with her husband Zhao Mingcheng. After the Jingkang Incident and the fall of Northern Song, she fled south with the court — amid the chaos, her husband died and their life's collection of art and antiquities was scattered. Her early lyrics were fresh and delicate: 'Don't you know? Don't you know? The green should be plump, the red thin.' After the southward flight, her style turned sorrowful: 'Searching, seeking; cold, lonely; miserable, wretched, sad' — her use of reduplicated characters is unmatched in Chinese poetry.",
  [], [], "", 0.9)

p("wang-yangming", "王阳明", "Wang Yangming", 1472, 1529, "ming-dynasty",
  ["哲学", "军事", "明朝", "心学"],
  ["Philosophy", "Military", "Ming Dynasty", "Heart-Mind School"],
  "明代哲学家、军事家和政治家，心学的集大成者，提出'知行合一'和'致良知'的思想。",
  "Ming dynasty philosopher, general, and statesman who synthesized the School of Heart-Mind, proposing 'unity of knowledge and action' and 'extension of innate knowledge.'",
  "王阳明既平定过宁王之乱，又镇压过西南民变——但他在中国思想史上的地位来自他的哲学。他反对朱熹的'格物致知'——认为心即是理，真理不在外部而在每个人的心中。'知行合一'意味着真正的知必然包含行——知道孝顺却不行孝，就不是真正的知。他的思想不仅深刻影响了明清两代的儒学，还在日本明治维新中发挥了重要作用，至今仍是东亚文化的重要思想资源。",
  "Wang Yangming suppressed the Prince of Ning's rebellion and quelled southwestern uprisings — but his place in Chinese intellectual history rests on his philosophy. Against Zhu Xi's 'investigation of things,' he held that the heart-mind is principle itself and truth resides within, not externally. His 'unity of knowledge and action' means genuine knowledge necessarily includes action — claiming to know filial piety without practicing it is not real knowledge. His thought not only profoundly shaped Ming-Qing Confucianism but also played a key role in Japan's Meiji Restoration, remaining an important intellectual resource in East Asian culture.",
  [], [], "", 0.9)

# ===== Japan (10) =====
p("shotoku-taishi", "圣德太子", "Prince Shotoku", 574, 622, "japan",
  ["政治", "佛教", "改革", "飞鸟时代"],
  ["Politics", "Buddhism", "Reform", "Asuka Period"],
  "日本飞鸟时代的政治家和改革者，制定了十七条宪法，推广佛教和中国文化，奠定了日本中央集权国家的基础。",
  "Statesman and reformer of Japan's Asuka period who instituted the Seventeen-Article Constitution, promoted Buddhism and Chinese culture, laying the foundation for a centralized Japanese state.",
  "圣德太子（厩户皇子）在推古天皇时期担任摄政。603年他制定了官位十二阶，604年颁布十七条宪法——将佛教伦理、儒家治国理念和日本本土传统融为一炉。他派出了遣隋使，系统学习中国的政治制度和文字。他亲自注释了三部佛经，在奈良地区建造了法隆寺——至今仍是世界上现存最古老的木结构建筑。",
  "Prince Shotoku (Umayado no Miko) served as regent under Empress Suiko. In 603 he established the Twelve Level Cap and Rank System; in 604 he promulgated the Seventeen-Article Constitution, blending Buddhist ethics, Confucian governance, and native Japanese traditions. He dispatched envoys to Sui China to systematically study Chinese political institutions and writing. He personally wrote commentaries on three Buddhist sutras and built Horyu-ji Temple in Nara — still the world's oldest surviving wooden structure.",
  [], [], "", 0.8)

p("oda-nobunaga", "织田信长", "Oda Nobunaga", 1534, 1582, "japan",
  ["军事", "政治", "战国", "统一"],
  ["Military", "Politics", "Sengoku", "Unification"],
  "日本战国时代最强大的大名之一，以铁炮和军事创新打破了旧秩序，为日本统一奠定了基础。",
  "One of the most powerful daimyo of Japan's Warring States period, who shattered the old order through firearms and military innovation, paving the way for Japanese unification.",
  "织田信长是尾张国的一个小大名。1560年他在桶狭间以数千兵力奇袭并击溃了拥有两万余人的今川义元——这一战使他名声大噪。他率先大规模使用铁炮，在长篠之战中以三段射击战术消灭了武田骑兵。他废除了阻碍商业发展的关卡，推行乐市乐座政策。1582年部将明智光秀叛变，他在本能寺被困自焚——'敌在本能寺！'至今仍是日本历史上最著名的悲叹。",
  "Oda Nobunaga began as a minor daimyo of Owari province. In 1560, with a few thousand men, he ambushed and crushed Imagawa Yoshimoto's 25,000-strong army at Okehazama — a victory that made his name. He pioneered the large-scale use of firearms, annihilating the Takeda cavalry with rotating volley fire at Nagashino. He abolished trade-impeding checkpoints and promoted free markets. In 1582, his general Akechi Mitsuhide rebelled; trapped at Honno-ji temple, Nobunaga perished in the flames — 'The enemy is at Honno-ji!' remains Japanese history's most famous lament.",
  [], [], "", 0.9)

p("toyotomi-hideyoshi", "丰臣秀吉", "Toyotomi Hideyoshi", 1537, 1598, "japan",
  ["军事", "政治", "战国"],
  ["Military", "Politics", "Sengoku"],
  "日本战国时代的统一者，从最低层出身的农民之子到关白——掌握最高权力，实现了日本的统一。",
  "The unifier of Japan's Warring States period, who rose from a peasant background to become Kampaku — the highest civil office — and unified Japan.",
  "秀吉出身贫寒，从织田信长的草履取（提鞋的小厮）做到了控制全日本的大名。信长死后他迅速行动，在山崎之战中击败明智光秀为旧主复仇。1590年他最终统一了日本全境。他推行太阁检地——详细丈量全国土地，奠定了幕藩体制的经济基础；颁布刀狩令收缴农民武器。但他晚年发动了两次入侵朝鲜的战争——虽以失败告终，却深刻影响了东亚格局。",
  "Born to a peasant family, Hideyoshi rose from being Nobunaga's sandal-bearer to the daimyo controlling all Japan. After Nobunaga's death, he moved swiftly, defeating Akechi Mitsuhide at Yamazaki to avenge his lord. By 1590 he had unified the entire country. He conducted the Taiko Land Survey — a comprehensive cadastral survey that laid the economic foundation for the bakuhan system — and issued the Sword Hunt edict to disarm the peasantry. In his final years, he launched two invasions of Korea; though ultimately unsuccessful, they profoundly impacted the East Asian order.",
  [], [], "", 0.9)

p("tokugawa-ieyasu", "德川家康", "Tokugawa Ieyasu", 1543, 1616, "japan",
  ["政治", "幕府", "江户"],
  ["Politics", "Shogunate", "Edo"],
  "德川幕府的创立者，结束了长达一个多世纪的战国乱世，开创了持续260年的江户和平时期。",
  "Founder of the Tokugawa Shogunate who ended over a century of Warring States chaos and inaugurated 260 years of Edo-period peace.",
  "家康是战国三杰中最能忍耐的一位——他做过今川义元的人质，也在丰臣秀吉手下蛰伏多年。1600年关原之战他以少胜多击败了石田三成的西军，成为全日本的实际掌控者。1603年被任命为征夷大将军，在江户（今东京）建立幕府。1615年大阪夏之阵中彻底消灭了丰臣氏残余。他建立了等级森严的幕藩体制和锁国政策，使日本进入了长达两个半世纪的稳定——虽然代价是与外部世界的隔绝。",
  "Ieyasu was the most patient of the three Sengoku unifiers — having been a hostage to the Imagawa clan and biding his time under Toyotomi Hideyoshi. In 1600, his Eastern Army defeated Ishida Mitsunari's larger Western Army at Sekigahara, making him the de facto ruler of Japan. Appointed Seii Taishogun in 1603, he established the shogunate in Edo (modern Tokyo). In the 1615 Summer Siege of Osaka, he obliterated the last Toyotomi remnants. He instituted a rigid bakuhan system and a policy of national seclusion, ushering in two and a half centuries of stability — at the cost of isolation from the outside world.",
  [], [], "", 0.9)

p("murasaki-shikibu2", "清少纳言", "Sei Shonagon", 966, 1025, "japan",
  ["文学", "女性", "平安", "随笔"],
  ["Literature", "Women", "Heian", "Essay"],
  "日本平安时代的女作家，《枕草子》的作者，与紫式部并称平安文学双璧，以敏锐的观察和机智的笔触著称。",
  "Heian-period Japanese court lady and author of 'The Pillow Book,' celebrated alongside Murasaki Shikibu as twin pillars of Heian literature, known for her keen observation and wit.",
  "清少纳言在一条天皇的中宫定子身边担任女官。她在日常宫廷生活中随手记下的随笔——《枕草子》——以独特的'事物清单'（如'令人心动的事''令人扫兴的事'）和对自然景物的诗意描写开创了日本随笔文学的先河。她与紫式部互为竞争对手——紫式部在日记中批评清少纳言'自以为是的女人'——但两人共同奠定了日本国风文学的基础。",
  "Sei Shonagon served as lady-in-waiting to Empress Teishi. The casual notes she jotted down about daily court life — 'The Pillow Book' — pioneered Japanese essay literature through unique 'lists of things' ('things that make the heart beat faster,' 'things that arouse a fond memory') and poetic descriptions of nature. She and Murasaki Shikibu were rivals — Murasaki criticized Sei in her diary as 'a woman who thinks too much of herself' — but together they laid the foundation of Japanese vernacular literature.",
  [], [], "", 0.8)

# ===== Korean (8) =====
p("gwangaeto", "广开土大王", "Gwanggaeto the Great", 374, 413, "asia",
  ["政治", "军事", "高句丽"],
  ["Politics", "Military", "Goguryeo"],
  "高句丽第十九代君主，大幅扩张了高句丽的领土，其功业刻于著名的广开土大王碑上。",
  "The 19th ruler of Goguryeo who greatly expanded the kingdom's territory, his achievements inscribed on the famous Gwanggaeto Stele.",
  "广开土大王（高谈德）18岁即位，在位的22年中将高句丽从一个地区强国扩张为东北亚最强大的国家。他南征百济和新罗，北击契丹和鲜卑，将疆域推进到了辽河流域和朝鲜半岛中南部。他去世后其子长寿王在今天的吉林省集安市立碑纪功——这块4米多高的石碑是研究古代东北亚历史最重要的文献之一。",
  "Gwanggaeto (Go Damdeok) ascended at 18; during his 22-year reign, he transformed Goguryeo from a regional power into Northeast Asia's most formidable state. He campaigned south against Baekje and Silla, and north against the Khitan and Xianbei, pushing Goguryeo's borders to the Liao River basin and the central-southern Korean Peninsula. After his death, his son King Jangsu erected a stele in modern Ji'an, Jilin Province — this 4-meter-tall monument is one of the most important documents for studying ancient Northeast Asian history.",
  [], [], "", 0.8)

p("jeong-yakyong", "丁若镛", "Jeong Yak-yong (Dasan)", 1762, 1836, "asia",
  ["哲学", "科学", "朝鲜", "实学"],
  ["Philosophy", "Science", "Joseon", "Silhak"],
  "朝鲜后期实学派的集大成者，百科全书式的学者，试图用实用知识改革朝鲜社会。",
  "The supreme synthesis of the late Joseon Silhak (Practical Learning) school, an encyclopedic scholar who sought to reform Korean society through practical knowledge.",
  "丁若镛（号茶山）早年因参与天主教活动而被流放18年。在流放期间他写下了500多卷著作，涵盖经学、政治、经济、法律、医学、建筑和农业。他批判僵化的性理学脱离实际，主张技术是'利国便民'的关键——他设计了水原城的起重机，撰写农业技术手册。他的思想虽然生前未能广泛实施，却成为了韩国现代化思维的先声。",
  "Jeong Yak-yong (pen name Dasan) was exiled for 18 years due to his involvement with Catholicism. During exile, he wrote over 500 volumes covering classics, politics, economics, law, medicine, architecture, and agriculture. He criticized ossified Neo-Confucianism for its detachment from reality and argued that technology was key to 'benefiting the nation and the people' — he designed the crane used to build Suwon Fortress and wrote agricultural manuals. Though his ideas were not widely implemented in his lifetime, they foreshadowed Korean modernization.",
  [], [], "", 0.85)

# ===== India (10) =====
p("ashoka", "阿育王", "Ashoka the Great", -304, -232, "india",
  ["政治", "佛教", "孔雀王朝"],
  ["Politics", "Buddhism", "Maurya Empire"],
  "孔雀王朝最伟大的君主，在目睹战争的残酷后皈依佛教，以佛法而非武力治理帝国。",
  "The greatest Mauryan emperor who converted to Buddhism after witnessing war's cruelty and governed through Dharma rather than force.",
  "阿育王在公元前260年征服羯陵伽的战争中目睹了超过10万人丧生的惨状——这一震撼使他彻底转变。他放弃武力征服，转而推行以佛教伦理为基础的'正法'统治：刻石勒碑宣扬慈悲、宽容和非暴力；派遣僧团到斯里兰卡和东南亚传播佛教；修建了数千座佛塔和寺院。他可能是人类历史上第一位将道德原则而非武力作为帝国统治基础的君主。",
  "In his 260 BCE conquest of Kalinga, Ashoka witnessed over 100,000 deaths — a shock that transformed him completely. He renounced conquest by force and instead pursued rule through 'Dharma' based on Buddhist ethics: inscribing edicts on stone pillars promoting compassion, tolerance, and non-violence; sending Buddhist missions to Sri Lanka and Southeast Asia; building thousands of stupas and monasteries. He may be the first ruler in human history to base imperial governance on moral principles rather than military force.",
  [], [], "", 0.85)

p("guru-nanak", "古鲁那纳克", "Guru Nanak", 1469, 1539, "india",
  ["宗教", "锡克教"],
  ["Religion", "Sikhism"],
  "锡克教的创始人，教导世人超越印度教与伊斯兰教的对立，皈依唯一的无形之神。",
  "Founder of Sikhism who taught humanity to transcend the Hindu-Muslim divide and devote themselves to the one formless God.",
  "那纳克生于印度旁遮普的印度教家庭，但在伊斯兰统治的环境中长大。30岁时他在一次神秘的濒死体验后宣称'没有印度教徒，也没有穆斯林——只有神才是真实的。'他此后的二十多年中游历了整个南亚和中东，教导人们一神信仰、人人平等和服务他人。他的教义被记录在锡克教圣书《古鲁·格兰特·萨希卜》中——这也使他成为极少数在世时就开始编纂自己宗教经典的创始人之一。",
  "Nanak was born to a Hindu family in Punjab but grew up under Islamic rule. At 30, after a mystical near-death experience, he proclaimed: 'There is no Hindu, there is no Muslim — only God is real.' He spent the next two decades traveling across South Asia and the Middle East, teaching monotheism, equality, and service to others. His teachings are recorded in the Sikh scripture Guru Granth Sahib — making him one of the very few founders who began compiling their religion's sacred text during their own lifetime.",
  [], [], "", 0.85)

p("akbar", "阿克巴大帝", "Akbar the Great", 1542, 1605, "india",
  ["政治", "莫卧儿", "宗教宽容"],
  ["Politics", "Mughal", "Religious Tolerance"],
  "莫卧儿帝国最伟大的皇帝，以宗教宽容和文化融合政策创建了跨越印度教与伊斯兰教鸿沟的统一帝国。",
  "The greatest Mughal emperor who created a unified empire bridging the Hindu-Muslim divide through religious tolerance and cultural synthesis.",
  "阿克巴13岁即位，但迅速证明了自己是军事和管理天才。他征服了印度次大陆的大部分地区，但真正的革命性在于他的治理理念：他废除了对非穆斯林征收的'吉兹亚'人头税，娶了印度教拉杰普特公主，邀请各宗教代表在宫廷讨论神学，甚至创建了一种综合各宗教的'神一教'。他推动波斯、印度和中亚文化的融合——莫卧儿细密画和建筑风格在他的时期达到巅峰。",
  "Akbar ascended at 13 but quickly proved a military and administrative genius. He conquered most of the Indian subcontinent, but his true revolutionary contribution lay in his governance philosophy: he abolished the jizya tax on non-Muslims, married Hindu Rajput princesses, invited representatives of all religions to debate theology at court, and even created a syncretic 'Divine Faith.' He fostered a fusion of Persian, Indian, and Central Asian cultures — Mughal miniature painting and architecture reached their zenith under his patronage.",
  [], [], "", 0.9)

p("ramanujan", "拉马努金", "Srinivasa Ramanujan", 1887, 1920, "india",
  ["数学", "天才"],
  ["Mathematics", "Genius"],
  "印度数学天才，几乎未受正规教育却独立发现了近4000个数学定理和公式，其笔记至今仍在被研究。",
  "Indian mathematical genius who, with virtually no formal training, independently discovered nearly 4,000 theorems and formulas — his notebooks are still being studied today.",
  "拉马努金出身印度南部一个贫穷的婆罗门家庭，15岁时借到一本过时的数学手册后自学成才。1913年他写信给剑桥大学的哈代——后者立即意识到这个印度青年是一个'最高级别的数学家'。在剑桥的五年中他与哈代合作发表了大量开创性的论文。但他不适应英国的气候和饮食——1920年回到印度后不久便因营养不良和疾病去世，年仅32岁。他留下的未解公式激发了整整一个世纪的研究。",
  "Born to a poor Brahmin family in southern India, Ramanujan was self-taught from an outdated mathematics handbook borrowed at 15. In 1913 he wrote to Hardy at Cambridge — who instantly recognized the young Indian as a 'mathematician of the highest order.' During five years at Cambridge, he co-published groundbreaking papers with Hardy. But he couldn't adapt to the English climate or diet — he returned to India and died shortly after in 1920 at just 32, from malnutrition and illness. His unsolved formulas have inspired a century of research.",
  [], [], "Q83163", 0.95)

# ===== Middle East (8) =====
p("saladin", "萨拉丁", "Saladin (Salah ad-Din)", 1137, 1193, "middle-east",
  ["军事", "政治", "十字军", "阿尤布"],
  ["Military", "Politics", "Crusades", "Ayyubid"],
  "阿尤布王朝的缔造者，从十字军手中收复了耶路撒冷，以骑士风度和宽宏大量赢得了敌人的尊敬。",
  "Founder of the Ayyubid dynasty who recaptured Jerusalem from the Crusaders and won the respect of his enemies for his chivalry and magnanimity.",
  "萨拉丁是库尔德人，起初为赞吉王朝的一位将领服务，后来在埃及建立了自己的阿尤布王朝。1187年在哈丁战役中他击败并几乎全歼了耶路撒冷王国的十字军。随后他收复了耶路撒冷——但与88年前十字军的血腥屠城不同，萨拉丁允许城中基督徒和平离开或缴纳赎金。他与狮心王理查的军事对抗和相互尊敬成为了中世纪骑士精神的传奇典范。",
  "Saladin was a Kurd who initially served as a general under the Zengid dynasty before establishing his own Ayyubid dynasty in Egypt. In 1187, at the Battle of Hattin, he defeated and virtually annihilated the Crusader army of the Kingdom of Jerusalem. He then recaptured Jerusalem — but unlike the Crusaders' bloody massacre 88 years earlier, Saladin allowed the city's Christians to leave peacefully or pay ransom. His military rivalry and mutual respect with Richard the Lionheart became a legendary exemplar of medieval chivalry.",
  [], [], "", 0.9)

p("suleiman", "苏莱曼大帝", "Suleiman the Magnificent", 1494, 1566, "middle-east",
  ["政治", "法律", "奥斯曼"],
  ["Politics", "Law", "Ottoman"],
  "奥斯曼帝国第十位苏丹，在位46年将帝国推向极盛——在军事、法律、建筑和艺术上都达到了巅峰。",
  "The tenth Ottoman Sultan, whose 46-year reign brought the empire to its zenith — in military power, law, architecture, and the arts.",
  "苏莱曼在位期间奥斯曼帝国几乎统治了地中海世界——从匈牙利到也门，从阿尔及利亚到伊拉克。他亲自指挥了13次大规模军事远征。但他同样以立法者闻名——'卡努尼'苏莱曼——他编纂并统一了奥斯曼帝国的世俗法律体系。在他的赞助下，建筑师锡南建造了伊斯坦布尔最壮观的清真寺。他的妻子许蕾姆苏丹——一个从乌克兰奴隶成为帝国最有权势女性的传奇——象征着苏莱曼宫廷的独特文化。",
  "Under Suleiman, the Ottoman Empire dominated the Mediterranean world — from Hungary to Yemen, from Algeria to Iraq. He personally led 13 major military campaigns. But he was equally known as 'Suleiman the Lawgiver' (Kanuni) — who codified and unified the empire's secular legal system. Under his patronage, architect Mimar Sinan built Istanbul's most magnificent mosques. His wife Hurrem Sultan — a Ukrainian slave who became the empire's most powerful woman — symbolizes the unique culture of Suleiman's court.",
  [], [], "", 0.9)

p("ibn-khaldun", "伊本·赫勒敦", "Ibn Khaldun", 1332, 1406, "middle-east",
  ["历史", "社会学", "哲学"],
  ["History", "Sociology", "Philosophy"],
  "阿拉伯历史学家和社会学家，《历史绪论》的作者，被视为现代社会学、历史学和经济学的前驱。",
  "Arab historian and sociologist, author of the 'Muqaddimah,' regarded as a precursor of modern sociology, historiography, and economics.",
  "伊本·赫勒敦出生在突尼斯，在动荡的政治生涯中先后为北非和安达卢西亚多个政权服务。他写作《历史绪论》的野心是创立一门全新的科学——他称之为'文明科学'——研究人类社会兴衰的规律。他提出了著名的'阿萨比亚'（群体凝聚力）理论：游牧部落因团结而崛起，在定居文明中逐渐腐化衰退。这一周期性的历史观领先于他同时代人几个世纪——汤因比称这部著作是'任何时代任何地方由任何头脑所产生的最伟大的历史哲学著作'。",
  "Born in Tunis, Ibn Khaldun served multiple North African and Andalusian regimes during a turbulent political career. His ambition in writing the 'Muqaddimah' was to found an entirely new science — what he called 'the science of civilization' — studying the laws of the rise and fall of human societies. He proposed the famous theory of 'asabiyyah' (group cohesion): nomadic tribes rise through solidarity, then gradually decay in settled civilization. This cyclical view of history was centuries ahead of its time — Toynbee called it 'the greatest work of its kind that has ever yet been created by any mind in any time or place.'",
  [], [], "", 0.85)

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
print("\n// Total: %d new people (batch 6)" % len(people))
