#!/usr/bin/env python3
"""Generate Chinese emperors/rulers data for History Parallel.
Outputs TypeScript Person[] entries to stdout."""
def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")

people = []

def p(id, name, nameEn, birth, death, region, tags, tagsEn, summary, summaryEn, desc, descEn,
      alt=None, srcs=None, wiki="", conf=0.85):
    people.append({
        "id": id, "name": name, "nameEn": nameEn, "birthYear": birth, "deathYear": death,
        "regionId": region, "tags": tags, "tagsEn": tagsEn, "occupations": ["君主", "统治者"],
        "summary": summary, "summaryEn": summaryEn,
        "description": desc, "descriptionEn": descEn,
        "alternativeNames": alt or [],
        "sourceIds": srcs or [],
        "wikidataQid": wiki,
        "dataStatus": "published",
        "confidenceScore": conf,
        "externalReferences": []
    })

# ============ QIN (1 new, 1 existing qin-shi-huang) ============
# qin-shi-huang already exists in mockData.ts
p("qin-er-shi", "秦二世", "Qin Er Shi", -230, -207, "qin-dynasty",
  ["君主", "皇帝", "秦朝"], ["Ruler", "Emperor", "Qin Dynasty"],
  "秦朝第二位皇帝，胡亥即位后朝政被赵高把持，暴政加速了秦朝的崩溃。",
  "Second emperor of Qin; Hu Hai's reign was dominated by the eunuch Zhao Gao, and his misrule accelerated Qin's collapse.",
  "胡亥在赵高和李斯的策划下篡改始皇遗诏，逼死长兄扶苏后即位。他在位期间大兴土木续建阿房宫，加重赋税徭役，赵高指鹿为马专权朝政。前209年陈胜吴广起义爆发，天下响应。前207年赵高逼迫胡亥自杀，秦朝随之灭亡——这个曾横扫六合的大帝国仅存在了15年。",
  "Hu Hai, manipulated by Zhao Gao and Li Si, forged the First Emperor's will and forced his elder brother Fusu to suicide. His reign saw continued massive construction projects, heavy taxation, and Zhao Gao's tyranny — epitomized by his 'pointing at a deer and calling it a horse' to test loyalty. The Dazexiang uprising erupted in 209 BCE; by 207 BCE, Zhao Gao forced Hu Hai to suicide, and Qin collapsed after just 15 years.",
  ["胡亥", "Hu Hai"], ["src-shiji"], "", 0.85)

# ============ WESTERN HAN (6 new, han-gaozu & han-wudi existing) ============
# han-gaozu (liu-bang) already exists as 'liu-bang' in mockData.ts
# han-wudi already exists in mockData.ts
p("han-wendi", "汉文帝", "Emperor Wen of Han", -203, -157, "han-dynasty",
  ["君主", "皇帝", "汉朝"], ["Ruler", "Emperor", "Han Dynasty"],
  "西汉第五位皇帝刘恒，开创「文景之治」，以节俭和仁政著称。",
  "The fifth Western Han emperor who inaugurated the 'Rule of Wen and Jing,' known for frugality and benevolent governance.",
  "刘恒原为代王，吕后死后被大臣迎立为帝。他以节俭著称——据说一件龙袍穿了二十余年，宫殿不加修缮。他废除连坐法和肉刑，减轻田租赋税，与民休息。他处理南越问题时以德服人、避免武力，开创了汉朝政治清明的第一个高峰。他与儿子景帝的统治合称「文景之治」，为武帝时代积累了雄厚的国力。",
  "Liu Heng, originally Prince of Dai, was chosen by ministers after Empress Lü's death. Renowned for frugality — legend says he wore the same robe for over 20 years and refused palace renovations. He abolished collective punishment and mutilation, reduced taxes, and resolved the Nanyue crisis through diplomacy rather than war. His reign, together with his son's, is called the 'Rule of Wen and Jing,' accumulating the national strength that Emperor Wu would later deploy.",
  ["刘恒", "Liu Heng"], ["src-shiji", "src-hanshu"], "", 0.85)

p("han-jingdi", "汉景帝", "Emperor Jing of Han", -188, -141, "han-dynasty",
  ["君主", "皇帝", "汉朝"], ["Ruler", "Emperor", "Han Dynasty"],
  "西汉第六位皇帝刘启，平定七国之乱，延续文景之治。",
  "Sixth Western Han emperor who crushed the Rebellion of the Seven States and continued the Wen-Jing prosperity.",
  "刘启继承父亲文帝的基业，继续休养生息政策。但他面临诸侯王势力坐大的危机——前154年，以吴王刘濞为首的七国发动叛乱。景帝在周亚夫等人辅佐下仅三个月便平定叛乱，随后大规模削减诸侯王的封地和权力，中央集权显著加强。他的统治与文帝合称「文景之治」，为后来的武帝盛世铺平了道路。",
  "Liu Qi continued his father's laissez-faire policies. When the Rebellion of the Seven States erupted in 154 BCE led by the Prince of Wu, he crushed it within three months with the help of general Zhou Yafu. He then systematically reduced princely territories and powers, significantly strengthening central authority. Together with his father's reign, this era of peace and prosperity set the stage for Emperor Wu's great campaigns.",
  ["刘启", "Liu Qi"], ["src-shiji", "src-hanshu"], "", 0.85)

p("han-zhaodi", "汉昭帝", "Emperor Zhao of Han", -94, -74, "han-dynasty",
  ["君主", "皇帝", "汉朝"], ["Ruler", "Emperor", "Han Dynasty"],
  "西汉第八位皇帝刘弗陵，幼年即位，在霍光辅政下延续休养生息。",
  "Eighth Western Han emperor, ascended as a child and, under Huo Guang's regency, continued recovery policies.",
  "刘弗陵8岁即位，由武帝托孤大臣霍光、金日磾、上官桀辅政。霍光在平息上官桀等人的政变后独揽大权，但施政稳健——轻徭薄赋、与民休息，对外与匈奴恢复和亲。昭帝在位期间社会趋于安定，为后来的「昭宣中兴」拉开序幕。他年仅21岁便病逝，无子嗣。",
  "Liu Fuling ascended at age 8, with regents Huo Guang, Jin Midi, and Shangguan Jie appointed by the late Emperor Wu. After suppressing a coup by Shangguan Jie, Huo Guang dominated but governed prudently — reducing taxes and labor, and restoring heqin (marriage alliance) with the Xiongnu. Society stabilized under Emperor Zhao, initiating the 'Zhao-Xuan Restoration.' He died childless at only 21.",
  ["刘弗陵", "Liu Fuling"], ["src-hanshu"], "", 0.8)

p("han-xuandi", "汉宣帝", "Emperor Xuan of Han", -91, -48, "han-dynasty",
  ["君主", "皇帝", "汉朝"], ["Ruler", "Emperor", "Han Dynasty"],
  "西汉第十位皇帝刘询，曾流落民间，即位后开创「昭宣中兴」盛世。",
  "Tenth Western Han emperor who grew up among commoners; his reign saw the 'Zhao-Xuan Restoration,' Han's last golden age.",
  "刘询原名刘病已，是武帝戾太子刘据之孙。「巫蛊之祸」后他在民间长大，深知百姓疾苦。霍光废黜昌邑王后迎立他为帝。他即位后逐步收回霍氏权力，亲政后整饬吏治、平理冤狱，对外联合乌孙大破匈奴，设立西域都护府正式将西域纳入版图。「昭宣中兴」时期是西汉国力最强盛的阶段之一。",
  "Originally named Liu Bingyi, he was the grandson of Emperor Wu's crown prince and survived the witchcraft purges, growing up among commoners and understanding their hardships. After Huo Guang deposed the Prince of Changyi, Liu Bingyi was enthroned. He gradually reclaimed power from the Huo clan, reformed governance, and allied with the Wusun to decisively defeat the Xiongnu, establishing the Protectorate of the Western Regions. The Zhao-Xuan Restoration marked the last peak of Western Han power.",
  ["刘询", "刘病已", "Liu Xun", "Liu Bingyi"], ["src-hanshu"], "", 0.85)

p("han-yuandi", "汉元帝", "Emperor Yuan of Han", -75, -33, "han-dynasty",
  ["君主", "皇帝", "汉朝"], ["Ruler", "Emperor", "Han Dynasty"],
  "西汉第十一位皇帝刘奭，崇尚儒学，但无力遏制外戚和宦官势力的膨胀。",
  "Eleventh Western Han emperor who championed Confucianism but failed to curb the rise of consort clans and eunuchs.",
  "刘奭是宣帝之子，性情仁厚、喜好儒学。他在位期间名臣辈出——萧望之、周堪等儒臣受重用，但外戚史高和宦官弘恭、石显也逐渐攫取权力。王昭君出塞和亲即发生在他执政期间。元帝朝标志着西汉由盛转衰的转折——儒家理想主义的治理未能阻止外戚王氏的崛起，最终将导致王莽篡汉。",
  "Son of Emperor Xuan, Liu Shi was gentle-natured and loved Confucian scholarship. His reign featured Confucian officials like Xiao Wangzhi and Zhou Kan, but consort clan members like Shi Gao and eunuchs Hong Gong and Shi Xian also gained power. Wang Zhaojun's diplomatic marriage to the Xiongnu occurred during his rule. Emperor Yuan's reign marks the turning point from Western Han's zenith — Confucian idealism could not prevent the Wang clan's rise, which would eventually lead to Wang Mang's usurpation.",
  ["刘奭", "Liu Shi"], ["src-hanshu"], "", 0.8)

# ============ EASTERN HAN (4) ============
p("han-guangwudi", "光武帝", "Emperor Guangwu of Han", -5, 57, "han-dynasty",
  ["君主", "皇帝", "东汉", "军事"], ["Ruler", "Emperor", "Eastern Han", "Military"],
  "东汉开国皇帝刘秀，推翻王莽新朝，重建汉室，开创「光武中兴」。",
  "Founder of the Eastern Han who overthrew Wang Mang's Xin dynasty, restored the Han, and inaugurated the 'Guangwu Restoration.'",
  "刘秀是汉景帝的后裔，但家道中落为南阳豪族。王莽末年天下大乱，他与兄长刘縯起兵。在昆阳之战中以少胜多击溃新莽主力，声名鹊起。更始帝杀其兄后，刘秀韬光养晦并最终自立。他先后扫平赤眉、隗嚣、公孙述等割据势力，在25年称帝重建汉朝，定都洛阳。他改革官制、精兵简政、释放奴婢，开创了稳定的东汉前期。",
  "Descended from Emperor Jing but born to a declining branch, Liu Xiu was a Nanyang gentry. When Wang Mang's regime crumbled, he and his brother Liu Yan rose in arms. His stunning victory at the Battle of Kunyang against overwhelming odds made his name. After the Gengshi Emperor executed his brother, Liu Xiu bided his time and ultimately declared himself emperor in 25 CE, settling the capital at Luoyang. He systematically defeated the Red Eyebrows, Wei Xiao, Gongsun Shu and other warlords, reformed the bureaucracy, and freed slaves, inaugurating a stable early Eastern Han.",
  ["刘秀", "Liu Xiu"], ["src-hanshu"], "", 0.9)

p("han-mingdi", "汉明帝", "Emperor Ming of Han", 28, 75, "han-dynasty",
  ["君主", "皇帝", "东汉"], ["Ruler", "Emperor", "Eastern Han"],
  "东汉第二位皇帝刘庄，佛教正式传入中国即在其在位期间。",
  "Second Eastern Han emperor during whose reign Buddhism was formally introduced to China.",
  "刘庄是光武帝之子，在位期间延续其父的谨慎政策。他严惩外戚和宗室不法行为，整顿吏治，派班超出使西域恢复对西域的控制。最著名的文化事件——传说他梦见金人，于是遣使西域求法，迎来了最早的佛教僧侣和经书，白马寺在洛阳建成，这标志着佛教正式传入中国的开始。",
  "Son of Guangwu, Liu Zhuang continued his father's cautious governance. He severely punished lawbreaking consort relatives and imperial princes, reformed the bureaucracy, and sent Ban Chao to restore Han control over the Western Regions. The most famous cultural event: legend says he dreamt of a golden figure and dispatched envoys to the Western Regions — they returned with the first Buddhist monks and scriptures, and the White Horse Temple was built in Luoyang, marking Buddhism's formal introduction to China.",
  ["刘庄", "Liu Zhuang"], ["src-hanshu"], "", 0.8)

p("han-zhangdi", "汉章帝", "Emperor Zhang of Han", 57, 88, "han-dynasty",
  ["君主", "皇帝", "东汉"], ["Ruler", "Emperor", "Eastern Han"],
  "东汉第三位皇帝刘炟，白虎观会议召开，儒学进一步经学化。",
  "Third Eastern Han emperor who presided over the White Tiger Hall Conference, further codifying Confucian orthodoxy.",
  "刘炟在位期间政治比较清明，但宽纵外戚——对母亲马太后的家族和皇后窦氏的家族都予以重用，埋下了东汉外戚专权的祸根。文化上最重大的事件是79年召集的白虎观会议——全国儒者讨论五经异同，班固将会议内容整理为《白虎通义》，确立了官方儒学的统一解释。章帝本人也是出色的书法家，章草书体即源于他。",
  "Liu Da's reign was comparatively well-governed, but his leniency toward consort clans — favoring both the Ma and Dou families — planted the seeds of Eastern Han's consort domination. Culturally, the most significant event was the White Tiger Hall Conference of 79 CE, where Confucian scholars debated scriptural interpretations; Ban Gu compiled the results into the 'Bai Hu Tong,' establishing official Confucian orthodoxy. Emperor Zhang was also an accomplished calligrapher, and the 'zhangcao' cursive script is named after him.",
  ["刘炟", "Liu Da"], ["src-hanshu"], "", 0.8)

p("han-xiandi", "汉献帝", "Emperor Xian of Han", 181, 234, "han-dynasty",
  ["君主", "皇帝", "东汉", "三国"], ["Ruler", "Emperor", "Eastern Han", "Three Kingdoms"],
  "东汉末代皇帝刘协，被曹操挟持以令诸侯，最终禅位于曹丕，标志着汉朝终结。",
  "Last emperor of Han, held hostage by Cao Cao to command the other warlords; his abdication to Cao Pi marked the end of 400 years of Han rule.",
  "刘协9岁被董卓立为皇帝，此后一生都是强臣手中的傀儡。先是董卓，后是李傕郭汜，而最知名的操控者是曹操——曹操迎献帝都许昌，「挟天子以令诸侯」。献帝在这种环境下生存了三十余年，多次尝试反抗而无果。220年曹操去世后，曹丕逼迫献帝禅让，汉朝正式终结。献帝被封为山阳公，又活了14年善终——这在末代帝王中极为罕见。",
  "Liu Xie was placed on the throne at age 9 by Dong Zhuo and spent his entire life as a puppet of powerful ministers — first Dong Zhuo, then Li Jue and Guo Si, and most famously Cao Cao, who 'held the emperor to command the warlords' from Xuchang. Emperor Xian survived over thirty years in this environment, attempting resistance multiple times without success. After Cao Cao's death in 220, Cao Pi forced his abdication, ending the Han dynasty. Ennobled as Duke of Shanyang, he lived peacefully for another 14 years — exceptionally rare for a final dynastic emperor.",
  ["刘协", "Liu Xie"], ["src-sanguozhi"], "", 0.85)

# ============ THREE KINGDOMS (4) ============
p("cao-pi", "曹丕", "Cao Pi", 187, 226, "three-kingdoms",
  ["君主", "皇帝", "三国", "魏"], ["Ruler", "Emperor", "Three Kingdoms", "Wei"],
  "曹魏开国皇帝，曹操之子，逼汉献帝禅让，建立魏国，也是杰出的文学评论家。",
  "Founding emperor of Cao Wei, son of Cao Cao, forced Emperor Xian's abdication; also an outstanding literary critic.",
  "曹丕是曹操的次子，在与弟弟曹植的继承权竞争中胜出。220年曹操去世后他继位为魏王，同年逼迫汉献帝禅让，正式建立魏国。他在政治上推行九品中正制，确立了门阀士族的政治地位。作为文人，他的《典论·论文》是中国文学批评的开山之作，提出「文以气为主」的观点。他的七言诗《燕歌行》也是传世名篇。",
  "Cao Pi, Cao Cao's second son, prevailed in the succession struggle against his younger brother Cao Zhi. After Cao Cao's death in 220, he succeeded as King of Wei and forced Emperor Xian's abdication the same year, formally establishing Wei. He instituted the nine-rank system that solidified the political dominance of aristocratic clans. As a scholar, his 'Discourse on Literature' pioneered Chinese literary criticism, arguing that 'literature is grounded in qi.' His seven-character poem 'Yan Ge Xing' remains a classic.",
  [], ["src-sanguozhi"], "", 0.85)

p("liu-bei", "刘备", "Liu Bei", 161, 223, "three-kingdoms",
  ["君主", "皇帝", "三国", "蜀汉"], ["Ruler", "Emperor", "Three Kingdoms", "Shu Han"],
  "蜀汉开国皇帝，以仁义著称，三顾茅庐请诸葛亮出山，在乱世中建立一方基业。",
  "Founder of Shu Han, renowned for benevolence, famously visited Zhuge Liang's thatched hut three times to recruit him.",
  "刘备自称汉景帝后代，早年以织席贩履为生。黄巾起义时起兵，辗转依附于公孙瓒、陶谦、曹操、袁绍、刘表等诸侯。207年三顾茅庐后得诸葛亮辅佐，在赤壁之战中联吴抗曹后占据荆州、益州，最终在221年称帝建立蜀汉。但为关羽报仇而发动的夷陵之战惨败，次年病逝于白帝城，临终托孤诸葛亮。",
  "Liu Bei, claiming descent from Emperor Jing of Han, started as a mat-weaver and sandal-seller. After the Yellow Turban Rebellion, he served under various warlords — Gongsun Zan, Tao Qian, Cao Cao, Yuan Shao, Liu Biao. After three visits to Zhuge Liang's hut in 207, he won the strategist's service and, following the Battle of Red Cliffs, seized Jing and Yi provinces. He declared himself emperor in 221, but his disastrous Yiling campaign to avenge Guan Yu ended in defeat; dying at Baidi Castle the following year, he entrusted his son and state to Zhuge Liang.",
  [], ["src-sanguozhi"], "", 0.85)

p("sun-quan", "孙权", "Sun Quan", 182, 252, "three-kingdoms",
  ["君主", "皇帝", "三国", "东吴"], ["Ruler", "Emperor", "Three Kingdoms", "Eastern Wu"],
  "东吴开国皇帝，继承父兄基业，赤壁之战联合刘备大破曹操，长期统治江东。",
  "Founder of Eastern Wu who inherited his father's and brother's legacy, defeated Cao Cao at Red Cliffs, and ruled the Jiangdong region for decades.",
  "孙权19岁继承兄长孙策之位，在张昭和周瑜的辅佐下稳定江东。208年他力排众议决定联刘抗曹，在赤壁之战中大败曹操，奠定了三国鼎立的格局。他善于用人，但晚年性格多疑，在继承人问题上反复无常，引发了朝廷内乱。他统治江东超过半个世纪，是三国中在位最长的君主。",
  "Sun Quan inherited his brother Sun Ce's position at 19 and, with the counsel of Zhang Zhao and Zhou Yu, stabilized the Jiangdong region. In 208, overruling his advisors, he allied with Liu Bei and decisively defeated Cao Cao at Red Cliffs, cementing the tripartite balance. Though skilled at employing talent, he grew paranoid in later years and vacillated on succession, causing court turmoil. He ruled Jiangdong for over half a century — the longest-reigning of the Three Kingdoms founders.",
  [], ["src-sanguozhi"], "", 0.85)

p("sima-yan", "司马炎", "Emperor Wu of Jin", 236, 290, "three-kingdoms",
  ["君主", "皇帝", "晋朝"], ["Ruler", "Emperor", "Jin Dynasty"],
  "晋朝开国皇帝，灭东吴统一三国，但分封宗室和传位弱智太子埋下八王之乱的祸根。",
  "Founder of the Jin dynasty who conquered Wu and reunified China, but his enfeoffment of princes and choice of heir planted the seeds of the War of Eight Princes.",
  "司马炎继承祖父司马懿、伯父司马师、父亲司马昭三代经营的政治遗产。265年他逼迫魏元帝禅让建立晋朝，280年灭东吴统一天下。统一后他骄奢淫逸——后宫佳丽过万，卖官鬻爵。更为致命的是他大封宗室诸王并赋予军权，又将皇位传给智力有缺陷的儿子司马衷，皇后贾南风专权，最终在291年爆发了导致西晋灭亡的「八王之乱」。",
  "Sima Yan inherited three generations of political groundwork by his grandfather Sima Yi, uncle Sima Shi, and father Sima Zhao. He forced the Wei emperor's abdication in 265 and conquered Wu in 280, reunifying China. But after unification he grew decadent — with thousands of concubines and openly selling offices. More fatally, he enfeoffed imperial princes with military power and chose his mentally disabled son Sima Zhong as heir, allowing Empress Jia Nanfeng to dominate. The 'War of Eight Princes' erupted in 291, ultimately destroying Western Jin.",
  [], ["src-sanguozhi"], "", 0.85)

# ============ SUI (1 new, sui-wendi existing) ============
# sui-wendi already exists in mockData.ts
p("sui-yangdi", "隋炀帝", "Emperor Yang of Sui", 569, 618, "sui-dynasty",
  ["君主", "皇帝", "隋朝"], ["Ruler", "Emperor", "Sui Dynasty"],
  "隋朝第二位皇帝杨广，开凿大运河、营建东都洛阳，但穷兵黩武导致隋朝迅速崩溃。",
  "Second Sui emperor who built the Grand Canal and the eastern capital Luoyang, but his militarism and extravagance caused the dynasty's rapid collapse.",
  "杨广弑父夺位后展现出不世出的雄心——营建东都洛阳、开凿大运河连接南北、创立进士科完善科举、三次远征高句丽、重修长城。每一项都是影响千年的重大工程，但短时间内同时推进造成了巨大的人力物力消耗，民变四起。618年他在江都（扬州）被部下宇文化及弑杀，隋朝仅存38年便告灭亡——一个功过均极端的帝王。",
  "After allegedly murdering his father, Yang Guang displayed extraordinary ambition — building the eastern capital Luoyang, digging the Grand Canal connecting north and south, creating the jinshi degree to perfect the exam system, launching three campaigns against Goguryeo, and rebuilding the Great Wall. Each was a millennium-defining project, but pursuing them simultaneously exhausted the population, sparking massive rebellions. In 618, he was murdered by his general Yuwen Huaji at Jiangdu — a ruler whose achievements and failures were equally extreme.",
  ["杨广", "Yang Guang"], ["src-suisheshu"], "", 0.85)

# ============ TANG (8 new, 2 existing) ============
p("tang-gaozu", "唐高祖", "Emperor Gaozu of Tang", 566, 635, "tang-dynasty",
  ["君主", "皇帝", "唐朝"], ["Ruler", "Emperor", "Tang Dynasty"],
  "唐朝开国皇帝李渊，趁隋末大乱起兵太原，建立中国历史上最辉煌的王朝之一。",
  "Founder of Tang; Li Yuan raised an army at Taiyuan amid Sui's collapse to establish one of China's most brilliant dynasties.",
  "李渊是隋朝的外戚贵族，担任太原留守。隋末天下大乱时，在次子李世民的极力劝说下起兵，仅一年便攻入长安。618年他接受隋恭帝禅让建立唐朝。但统一天下的大部分战功归于李世民——虎牢关之战等经典战役——导致太子李建成与秦王李世民的矛盾激化。626年玄武门之变后李渊被迫退位为太上皇。",
  "Li Yuan, a Sui consort relative serving as garrison commander at Taiyuan, raised an army at his second son Li Shimin's urging amid the Sui collapse and captured Chang'an within a year. He accepted the Sui emperor's abdication in 618. However, most military credit went to Li Shimin — the Battle of Hulao Pass and others — sharpening the rivalry between Crown Prince Li Jiancheng and the Prince of Qin. After the Xuanwu Gate Incident of 626, Li Yuan was forced to abdicate.",
  ["李渊", "Li Yuan"], ["src-jiutangshu"], "", 0.85)

p("tang-gaozong", "唐高宗", "Emperor Gaozong of Tang", 628, 683, "tang-dynasty",
  ["君主", "皇帝", "唐朝"], ["Ruler", "Emperor", "Tang Dynasty"],
  "唐朝第三位皇帝李治，在位期间唐朝疆域达到极盛，但权力逐渐旁落武则天。",
  "Third Tang emperor under whom the empire reached its greatest territorial extent, but power gradually shifted to Wu Zetian.",
  "李治是太宗第九子，为人仁弱，但在长孙无忌等大臣辅佐下前期颇有作为——灭西突厥、百济和高句丽，使得唐朝疆域东至朝鲜半岛、西达咸海。但他深爱武则天，不顾朝臣反对将她从感业寺接回宫中立为皇后。660年后他因风疾（中风）无法理政，武则天逐渐掌握实权，与高宗并称「二圣」。",
  "Li Zhi, Taizong's ninth son, was gentle-natured but made real achievements early in his reign with advisors like Zhangsun Wuji — conquering the Western Turks, Baekje, and Goguryeo, extending Tang borders from Korea to the Aral Sea. But his love for Wu Zetian led him to bring her back from the Buddhist convent and make her empress against all advice. After 660, a stroke left him incapacitated, and Wu Zetian gradually assumed real power, reigning jointly as the 'Two Sages.'",
  ["李治", "Li Zhi"], ["src-jiutangshu"], "", 0.85)

p("tang-xuanzong", "唐玄宗", "Emperor Xuanzong of Tang", 685, 762, "tang-dynasty",
  ["君主", "皇帝", "唐朝"], ["Ruler", "Emperor", "Tang Dynasty"],
  "唐朝第七位皇帝李隆基，开元盛世为唐朝巅峰，但天宝年间因安史之乱由盛转衰。",
  "Seventh Tang emperor; his Kaiyuan era marked Tang's peak, but the An Lushan Rebellion during his Tianbao era triggered the dynasty's decline.",
  "李隆基通过唐隆政变和先天政变铲除了韦后和太平公主集团，真正掌握大权。开元年间他任用姚崇、宋璟等贤相，唐朝达到全盛——长安是世界第一大都市、丝绸之路空前繁荣、诗歌艺术登峰造极。但天宝年间他沉迷于杨贵妃，委政于李林甫和杨国忠，最终在755年爆发安史之乱。他被迫逃往四川，途中发生马嵬坡兵变杨贵妃被缢死。他的悲剧在于：同一位帝王既创造了唐朝的巅峰，也开启了唐朝的衰落。",
  "Li Longji eliminated Empress Wei and Princess Taiping factions through coups to secure real power. During Kaiyuan, with capable chancellors like Yao Chong and Song Jing, Tang reached its zenith — Chang'an was the world's largest city, the Silk Road flourished, and poetry achieved unmatched heights. But in Tianbao, infatuated with Yang Guifei and delegating to Li Linfu and Yang Guozhong, the An Lushan Rebellion erupted in 755. He fled to Sichuan; at Mawei Slope, his guards mutinied and Yang Guifei was hanged. His tragedy: the same emperor created Tang's peak and triggered its decline.",
  ["李隆基", "Li Longji"], ["src-jiutangshu"], "", 0.9)

p("tang-xianzong", "唐宪宗", "Emperor Xianzong of Tang", 778, 820, "tang-dynasty",
  ["君主", "皇帝", "唐朝", "军事"], ["Ruler", "Emperor", "Tang Dynasty", "Military"],
  "唐朝第十一位皇帝李纯，平定藩镇割据，开创「元和中兴」。",
  "Eleventh Tang emperor who suppressed regional warlords, achieving the 'Yuanhe Restoration.'",
  "李纯即位时安史之乱已过去半个多世纪，但藩镇割据依然严重。他坚决采取军事手段削藩——重用裴度、李愬等将领，先后平定西川刘辟、镇海李锜、淮西吴元济等叛乱藩镇。雪夜入蔡州生擒吴元济是其中最精彩的战役。到819年全国藩镇表面上全部听命于中央。但他的「中兴」十分脆弱——他晚年沉迷丹药和宦官，最终被宦官陈弘志弑杀。",
  "When Li Chun ascended, over half a century had passed since the An Lushan Rebellion, but warlord separatism remained severe. He forcefully suppressed provincial governors — employing generals like Pei Du and Li Su to defeat rebel commands in Xichuan, Zhenhai, and Huaixi. The snow-night raid on Caizhou to capture Wu Yuanji was the campaign's most brilliant episode. By 819, all provinces nominally obeyed the center. But his 'restoration' proved fragile — he succumbed to elixir addiction and eunuchs, and was ultimately murdered by eunuch Chen Hongzhi.",
  ["李纯", "Li Chun"], ["src-jiutangshu"], "", 0.8)

# ============ SONG (8) ============
p("song-taizu", "宋太祖", "Emperor Taizu of Song", 927, 976, "song-dynasty",
  ["君主", "皇帝", "宋朝", "军事"], ["Ruler", "Emperor", "Song Dynasty", "Military"],
  "宋朝开国皇帝赵匡胤，陈桥兵变黄袍加身，杯酒释兵权以文治国。",
  "Founder of Song; Zhao Kuangyin seized power through the Chen Bridge Mutiny and famously relieved his generals of command over wine.",
  "赵匡胤原是后周禁军将领，960年在陈桥驿被部下黄袍加身拥立为帝，建立宋朝。他以「杯酒释兵权」的方式和平解除了开国将领的军权，避免重蹈五代军人专权的覆辙。他确立了「重文轻武」「强干弱枝」的国策，以科举制度广泛吸纳士人治理国家。宋朝从此成为中国历史上文化和经济最繁荣的朝代之一，但其军事上的弱势也始于太祖的制度设计。",
  "Zhao Kuangyin, a Later Zhou imperial guard commander, was draped in the imperial yellow robe by his troops at Chen Bridge in 960. He famously 'relieved his generals of command over a cup of wine' — peacefully retiring his founding marshals to prevent the military coups that plagued the Five Dynasties. He established the policy of 'emphasizing civil governance over military' and recruiting scholar-officials through expanded examinations. Song became one of history's most culturally and economically brilliant dynasties, though its military weakness was also rooted in Taizu's design.",
  ["赵匡胤", "Zhao Kuangyin"], ["src-ss"], "", 0.9)

p("song-taizong", "宋太宗", "Emperor Taizong of Song", 939, 997, "song-dynasty",
  ["君主", "皇帝", "宋朝"], ["Ruler", "Emperor", "Song Dynasty"],
  "宋朝第二位皇帝赵光义，完成统一大业但北伐辽国失败，确立科举取士制度。",
  "Second Song emperor who completed unification but failed in northern campaigns; solidified the imperial examination system.",
  "赵光义是太祖之弟，即位过程笼罩在「斧声烛影」的疑云中。他延续统一事业——979年灭北汉，基本完成中原统一。但随后两次北伐辽国均遭惨败，高粱河之战他本人中箭乘驴车逃走。此后宋朝对辽由攻转守。他对内大力发展科举——在位期间录取进士人数远超唐五代总和，文官政治格局正式确立。",
  "Zhao Guangyi, Taizu's younger brother, ascended amid the mysterious 'sound of an axe and shadow of a candle' incident. He continued unification — conquering the Northern Han in 979. But his two northern campaigns against the Liao ended disastrously; at the Battle of Gaoliang River he was wounded by an arrow and fled on a donkey cart. Thereafter Song shifted from offense to defense against Liao. Domestically, he dramatically expanded the examination system — enrolling more jinshi in his reign than all of Tang and the Five Dynasties combined — firmly establishing civil-bureaucratic governance.",
  ["赵光义", "赵炅", "Zhao Guangyi"], ["src-ss"], "", 0.85)

p("song-renzong", "宋仁宗", "Emperor Renzong of Song", 1010, 1063, "song-dynasty",
  ["君主", "皇帝", "宋朝"], ["Ruler", "Emperor", "Song Dynasty"],
  "宋朝第四位皇帝赵祯，在位四十余年，是北宋文化最繁荣的时期，包拯范仲淹欧阳修等名人辈出。",
  "Fourth Song emperor who reigned over 40 years; his era saw the peak of Northern Song culture, producing luminaries like Bao Zheng, Fan Zhongyan, and Ouyang Xiu.",
  "赵祯13岁即位，刘太后垂帘听政十余年，亲政后以仁厚著称——据说他批阅奏章到深夜想吃羊肉，怕扰民而忍住了。他在位期间名臣辈出：范仲淹推行庆历新政、包拯铁面无私、欧阳修领导古文运动、苏洵苏轼苏辙三父子崭露头角、司马光编纂《资治通鉴》。北宋最耀眼的文人集团几乎都集中在仁宗朝——这既是仁宗善于用人的证明，也是他过于宽厚的副产品：积贫积弱的问题也在这一时期加深。",
  "Zhao Zhen ascended at 13 under Empress Dowager Liu's regency. Known for benevolence — legend says he craved lamb at midnight while reviewing memorials but refrained from ordering it, not wanting to trouble palace staff. His era produced a constellation of talent: Fan Zhongyan's Qingli Reforms, the incorruptible judge Bao Zheng, Ouyang Xiu's classical prose movement, the three Su masters (Su Xun, Su Shi, Su Zhe), and Sima Guang's 'Zizhi Tongjian.' Nearly all of Northern Song's brightest literati flourished under Renzong — both a testament to his talent-spotting and a consequence of his excessive lenience: fiscal and military weakness deepened during his reign.",
  ["赵祯", "Zhao Zhen"], ["src-ss"], "", 0.85)

p("song-shenzong", "宋神宗", "Emperor Shenzong of Song", 1048, 1085, "song-dynasty",
  ["君主", "皇帝", "宋朝", "改革"], ["Ruler", "Emperor", "Song Dynasty", "Reform"],
  "宋朝第六位皇帝赵顼，支持王安石变法，试图通过一系列改革富国强兵。",
  "Sixth Song emperor who backed Wang Anshi's reforms in a sweeping attempt to enrich the state and strengthen the military.",
  "赵顼20岁即位，立志改变北宋积贫积弱的局面。他力排众议启用王安石推行新法——青苗法、免役法、市易法、保甲法等——目标是增加财政收入、加强军事力量。新法在短期内增加了国库收入，但也引发了激烈的党派斗争，朝臣分裂为新旧两党。军事上对西夏的战争有胜有败。1085年神宗在变法前途未卜中去世，此后新旧党争反复拉锯，消耗了北宋最后的气运。",
  "Zhao Xu ascended at 20, determined to reverse Song's fiscal and military decline. Overruling fierce opposition, he empowered Wang Anshi to implement the New Policies — Green Sprouts loans, labor exemption tax, market exchange bureaus, and community defense — aiming to boost revenue and military readiness. The reforms swelled state coffers but triggered ferocious factionalism, splitting court officials into reform and conservative camps. Military campaigns against Western Xia achieved mixed results. Shenzong died in 1085 with the reforms' future uncertain; the ensuing back-and-forth between factions would consume Northern Song's remaining vitality.",
  ["赵顼", "Zhao Xu"], ["src-ss"], "", 0.85)

p("song-huizong", "宋徽宗", "Emperor Huizong of Song", 1082, 1135, "song-dynasty",
  ["君主", "皇帝", "宋朝", "艺术"], ["Ruler", "Emperor", "Song Dynasty", "Art"],
  "宋朝第八位皇帝赵佶，艺术天才——独创瘦金体书法和院体画，但政治昏庸导致靖康之耻。",
  "Eighth Song emperor; an artistic genius who created the 'Slender Gold' calligraphy style, but whose political incompetence led to the Jingkang Humiliation.",
  "赵佶可能是中国历史上最不适合做皇帝的皇帝之一——他是卓越的艺术家。他的瘦金体书法独步天下、花鸟画精妙绝伦、还推动汝窑瓷器达到顶峰。但在政治上他重用蔡京、童贯等「六贼」，沉迷道教和园林（艮岳），搜刮花石纲使东南民不聊生。1126年金兵南下，他匆忙传位给儿子赵桓（钦宗），1127年靖康之变中父子双双被掳往金国，受尽屈辱后死于五国城。",
  "Zhao Ji may have been one of history's least-suited emperors — but a transcendent artist. His 'Slender Gold' calligraphy is unmatched, his bird-and-flower paintings exquisite, and he elevated Ru ware ceramics to their zenith. Politically, however, he entrusted the state to the 'Six Villains' — Cai Jing, Tong Guan, and others — while obsessing over Daoism and his Genyue pleasure garden, ruining southeast China with the 'Flower and Rock' requisitions. When Jurchen forces invaded in 1126, he hastily abdicated to his son Qinzong; in the 1127 Jingkang Incident, both were captured and died in humiliation in the Jin north.",
  ["赵佶", "Zhao Ji"], ["src-ss"], "", 0.85)

p("song-gaozong", "宋高宗", "Emperor Gaozong of Song", 1107, 1187, "song-dynasty",
  ["君主", "皇帝", "南宋"], ["Ruler", "Emperor", "Southern Song"],
  "南宋开国皇帝赵构，在金兵追击下渡江南逃，偏安临安，以莫须有罪名杀害岳飞。",
  "Founder of Southern Song who fled south across the Yangtze from Jurchen pursuers, settled in Lin'an, and executed the general Yue Fei on fabricated charges.",
  "赵构是徽宗第九子，靖康之变中侥幸未被掳走。他在应天府（商丘）即位后一路南逃——从扬州到镇江到杭州到明州甚至海上——直到金兵北撤。定都临安（杭州）后他始终主和，重用秦桧，在岳飞连战连捷时用十二道金牌将其召回，最终以「莫须有」罪名处死。他的偏安政策稳固了南宋政权，但也永远放弃了收复中原的希望。",
  "Zhao Gou, Huizong's ninth son, was the only prince to escape the Jingkang capture. Proclaimed emperor at Shangqiu, he fled south — from Yangzhou to Zhenjiang to Hangzhou to Mingzhou and even to sea — until the Jurchens retreated. After settling at Lin'an (Hangzhou), he consistently prioritized peace, employing Qin Hui and recalling Yue Fei with twelve gold medallions just as the general was on the verge of victory, ultimately executing him on 'dubious' charges. His policy of accommodation preserved the Southern Song state but forever abandoned hope of reclaiming the north.",
  ["赵构", "Zhao Gou"], ["src-ss"], "", 0.85)

# ============ YUAN (4 new, 1 existing Kublai) ============
p("yuan-chengzong", "元成宗", "Temür Khan", 1265, 1307, "yuan-dynasty",
  ["君主", "皇帝", "元朝", "蒙古"], ["Ruler", "Emperor", "Yuan Dynasty", "Mongol"],
  "元朝第二位皇帝铁穆耳，忽必烈之孙，延续了祖父的统治政策。",
  "Second Yuan emperor, grandson of Kublai Khan, who largely preserved his grandfather's policies.",
  "铁穆耳是忽必烈的孙子，因其父真金太子早逝而继承皇位。他在位期间基本维持忽必烈的制度框架，停止了对日本和东南亚的远征，缓和了对外关系。对内继续扶持藏传佛教，但在财政管理上日趋混乱——滥发纸币导致通货膨胀。他缺乏继承人也是元朝中期政治动荡的远因之一。",
  "Temür, grandson of Kublai Khan, succeeded due to his father Crown Prince Zhenjin's early death. His reign largely preserved Kublai's institutional framework while halting expeditions against Japan and Southeast Asia, easing foreign relations. Domestically, he continued patronage of Tibetan Buddhism, though fiscal management grew chaotic — overprinting of paper currency triggered inflation. His lack of an heir was a distant cause of the mid-Yuan political instability.",
  ["铁穆耳", "Temür Öljeytü"], ["src-yuanshi"], "", 0.7)

p("yuan-huizong", "元惠宗", "Toghon Temür", 1320, 1370, "yuan-dynasty",
  ["君主", "皇帝", "元朝", "蒙古"], ["Ruler", "Emperor", "Yuan Dynasty", "Mongol"],
  "元朝末代皇帝妥懽帖睦尔，面对全国性的农民起义无力回天，被朱元璋驱逐回漠北。",
  "Last Yuan emperor who proved powerless against nationwide peasant rebellions and was driven back to the steppe by Zhu Yuanzhang.",
  "妥懽帖睦尔年少即位，初期在权臣伯颜的控制下做傀儡。亲政后一度励精图治，但很快沉迷于密宗享乐。14世纪中叶黄河改道引发大规模灾荒，红巾军起义席卷全国——这是压垮元朝的最后一根稻草。1368年徐达攻入大都，他率残余势力逃往上都，元朝在中原的统治终结。他在漠北又维持了两年，最终病死于应昌。",
  "Toghon Temür ascended as a boy under the regency of the powerful minister Bayan. After assuming personal rule, he briefly tried to govern well but soon succumbed to tantric pleasures. Mid-14th-century Yellow River floods triggered massive famine and the Red Turban Rebellion swept the land — the final straw for the dynasty. When Xu Da captured Dadu (Beijing) in 1368, Toghon Temür fled to Shangdu with remnants, ending Mongol rule over China. He survived two more years on the steppe before dying at Yingchang.",
  ["妥懽帖睦尔", "Toghan Temur"], ["src-yuanshi"], "", 0.75)

# ============ MING (6 new, 2 existing) ============
p("ming-yongle", "明成祖", "Yongle Emperor", 1360, 1424, "ming-dynasty",
  ["君主", "皇帝", "明朝"], ["Ruler", "Emperor", "Ming Dynasty"],
  "明朝第三位皇帝朱棣，迁都北京、派郑和下西洋、编纂《永乐大典》。",
  "Third Ming emperor who moved the capital to Beijing, dispatched Zheng He's treasure fleets, and commissioned the Yongle Encyclopedia.",
  "朱棣是朱元璋第四子，封燕王镇守北平。建文帝削藩时他以「清君侧」为名发动靖难之役，四年后攻入南京夺取皇位。他的在位是明朝最具扩张性的时期——迁都北京、五次亲征漠北、派郑和七下西洋远达非洲东岸、编纂规模空前的《永乐大典》、修筑紫禁城。但他设立东厂开启了明代特务政治的先河，且靖难之役中屠杀建文旧臣的手段极为残酷。",
  "Zhu Di, fourth son of Zhu Yuanzhang, served as Prince of Yan at Beiping. When the Jianwen Emperor began stripping princely powers, Zhu Di launched the Jingnan ('pacification') Campaign and seized the throne after four years of civil war. His reign was Ming's most expansionist — moving the capital to Beijing, leading five personal campaigns into the steppe, dispatching Zheng He's seven voyages to East Africa, compiling the monumental Yongle Encyclopedia, and building the Forbidden City. But he also established the Eastern Depot secret police and massacred Jianwen loyalists with exceptional cruelty.",
  ["朱棣", "Zhu Di"], ["src-mingshi"], "", 0.9)

p("ming-xuande", "明宣宗", "Xuande Emperor", 1399, 1435, "ming-dynasty",
  ["君主", "皇帝", "明朝", "艺术"], ["Ruler", "Emperor", "Ming Dynasty", "Art"],
  "明朝第五位皇帝朱瞻基，「仁宣之治」的缔造者之一，宣德炉和宣德瓷为传世国宝。",
  "Fifth Ming emperor, co-architect of the 'Ren-Xuan Restoration'; his reign's bronzes and porcelains are national treasures.",
  "朱瞻基继承父亲明仁宗的仁政，与祖父永乐帝形成鲜明对比。他裁撤冗员、减轻赋税、撤回交趾驻军（承认越南独立），使明朝进入一个相对和平的阶段。他本人是出色的画家——其花鸟走兽画颇具水准——宫廷艺术在他推动下达到高峰，宣德炉和宣德青花瓷至今仍是中国工艺美术的极致代表。但他开创了宦官读书的制度，为后来王振等宦官专权埋下伏笔。",
  "Zhu Zhanji continued his father's benevolent governance, contrasting sharply with his grandfather Yongle. He cut bureaucracy, reduced taxes, and withdrew from Jiaozhi (accepting Vietnamese independence), ushering in a relatively peaceful era. An accomplished painter himself — his animal and bird paintings show real skill — court arts flourished under his patronage; Xuande bronzes and blue-and-white porcelains remain pinnacles of Chinese decorative arts. But he introduced palace education for eunuchs, sowing seeds for later eunuch dominance under figures like Wang Zhen.",
  ["朱瞻基", "Zhu Zhanji"], ["src-mingshi"], "", 0.85)

p("ming-wanli", "明神宗", "Wanli Emperor", 1563, 1620, "ming-dynasty",
  ["君主", "皇帝", "明朝"], ["Ruler", "Emperor", "Ming Dynasty"],
  "明朝第十三位皇帝朱翊钧，在位时间最长，前期张居正改革成效显著，后期长期怠政。",
  "Thirteenth Ming emperor, the longest-reigning; Zhang Juzheng's early reforms achieved notable success, but decades of imperial neglect followed.",
  "朱翊钧10岁即位，首辅张居正辅政十年推行「一条鞭法」等改革，国库充盈。但张居正去世后他展开疯狂清算，此后近三十年不上朝——不见大臣、不批奏章、不补空缺——朝政全赖内阁勉强维持。然而商品经济却在「无为」中蓬勃发展，晚明市民文化繁荣，《金瓶梅》《三言二拍》等文学作品涌现。他的怠政被认为是明朝走向灭亡的开始——「明之亡，实亡于神宗」。",
  "Zhu Yijun ascended at 10, with Grand Secretary Zhang Juzheng governing ably for a decade — implementing the 'Single Whip' tax reform and filling state coffers. But after Zhang's death, he launched a vindictive purge, then withdrew from governance for nearly three decades — refusing audiences, leaving memorials unanswered, declining to fill vacancies — leaving the state on bureaucratic autopilot. Paradoxically, the commercial economy boomed during this imperial 'non-action,' with late-Ming urban culture and literature like 'Jin Ping Mei' flourishing. Historians often mark his neglect as the beginning of Ming's end: 'The Ming perished, in truth, under Shenzong.'",
  ["朱翊钧", "Zhu Yijun"], ["src-mingshi"], "", 0.85)

p("ming-chongzhen", "明思宗", "Chongzhen Emperor", 1611, 1644, "ming-dynasty",
  ["君主", "皇帝", "明朝"], ["Ruler", "Emperor", "Ming Dynasty"],
  "明朝末代皇帝朱由检，勤政却无力回天，李自成攻破北京后在煤山上吊自尽。",
  "Last Ming emperor who worked tirelessly but could not save the dynasty; he hanged himself on Coal Hill when Li Zicheng took Beijing.",
  "朱由检是明朝最勤政的皇帝之一——据说每天只睡两个时辰，衣服打补丁以示节俭。他铲除了魏忠贤阉党，但面对内忧外患已回天乏术：关外满清虎视眈眈、关内农民起义如火如荼。他猜忌多疑的性格使他17年间更换了50位内阁大学士、诛杀了七位兵部尚书。1644年李自成攻入北京，崇祯在煤山自缢——临终前在衣襟上血书「朕死，无面目见祖宗于地下，自去冠冕，以发覆面。任贼分裂朕尸，勿伤百姓一人。」",
  "Zhu Youjian was among Ming's most diligent emperors — reportedly sleeping only four hours nightly and wearing patched robes to show frugality. He eliminated Wei Zhongxian's eunuch clique but faced insurmountable crises: the Manchus pressing from beyond the pass and peasant rebellions raging within. His paranoia led him to cycle through 50 grand secretaries and execute seven war ministers in 17 years. When Li Zicheng took Beijing in 1644, Chongzhen hanged himself on Coal Hill — his bloody final message on his robe read: 'I die ashamed to face my ancestors; I remove my crown and cover my face with my hair. Let the rebels dismember my corpse, but harm not a single commoner.'",
  ["朱由检", "Zhu Youjian"], ["src-mingshi"], "", 0.85)

# ============ QING (5 new, 3 existing) ============
p("qing-huangtaiji", "皇太极", "Hong Taiji", 1592, 1643, "qing-dynasty",
  ["君主", "皇帝", "清朝"], ["Ruler", "Emperor", "Qing Dynasty"],
  "清朝开国皇帝，改国号「后金」为「大清」，改族名「女真」为「满洲」，为入关奠定基础。",
  "Founding emperor of Qing who renamed the state from 'Later Jin' to 'Great Qing' and the people from 'Jurchen' to 'Manchu,' laying the groundwork for the conquest of China.",
  "皇太极是努尔哈赤第八子，1626年继承汗位。他通过一系列精明的军事和外交手段稳固了后金的地位——征服朝鲜、击败林丹汗获得传国玉玺、多次突破长城骚扰明朝腹地。政治上他改革八旗制度、重用汉人降将（范文程、洪承畴等）、仿照明制建立六部。1636年他在盛京正式称帝，改国号为「大清」——这个新名字以水克明之火。他去世时清军已做好了入主中原的一切准备。",
  "Hong Taiji, eighth son of Nurhaci, inherited the khanate in 1626. Through shrewd military and diplomatic maneuvers, he consolidated Later Jin — conquering Korea, defeating Ligdan Khan to obtain the imperial seal, and repeatedly breaching the Great Wall to raid Ming territory. Politically, he reformed the Banner system, employed surrendered Ming officials (Fan Wencheng, Hong Chengchou), and established ministries on the Ming model. In 1636 he proclaimed himself emperor at Mukden, renaming the state 'Great Qing' — the water radical of 'Qing' intended to extinguish Ming's fire. At his death, the Qing were fully prepared to conquer China.",
  [], ["src-qingshigao"], "", 0.85)

p("qing-shunzhi", "顺治帝", "Shunzhi Emperor", 1638, 1661, "qing-dynasty",
  ["君主", "皇帝", "清朝"], ["Ruler", "Emperor", "Qing Dynasty"],
  "清朝入关第一位皇帝福临，在位期间清军击败南明和农民军，统一全国。",
  "First Qing emperor to rule from Beijing; his reign saw the Qing defeat the Southern Ming and peasant armies to unify China.",
  "福临6岁即位，由叔父多尔衮摄政。1644年吴三桂引清兵入关，清军迅速占领北京并迁都。随后的十几年间清军南下消灭李自成、张献忠和南明诸政权，完成统一。顺治亲政后显示出对汉文化的浓厚兴趣，但也推行了「剃发易服」等高压政策。1661年他因天花去世（或传说出家为僧），年仅24岁。",
  "Fulin ascended at 6 under his uncle Dorgon's regency. When Wu Sangui opened Shanhai Pass in 1644, Qing forces quickly took Beijing and moved the capital. Over the next decade-plus, Qing armies destroyed Li Zicheng, Zhang Xianzhong, and the Southern Ming regimes, completing unification. After assuming personal rule, Shunzhi showed genuine interest in Han culture while also enforcing harsh policies like the queue-and-robe edict. He died of smallpox in 1661 at only 24 — or, as legend has it, became a Buddhist monk.",
  ["福临", "Fulin"], ["src-qingshigao"], "", 0.8)

p("qing-yongzheng", "雍正帝", "Yongzheng Emperor", 1678, 1735, "qing-dynasty",
  ["君主", "皇帝", "清朝", "改革"], ["Ruler", "Emperor", "Qing Dynasty", "Reform"],
  "清朝第五位皇帝胤禛，以铁腕著称，整顿吏治、改革财政，为乾隆盛世奠定基础。",
  "Fifth Qing emperor known for iron-fisted rule; he reformed governance and state finances, laying the foundation for the Qianlong era.",
  "胤禛在残酷的储位之争中胜出——「九子夺嫡」是清朝最激烈的皇位争夺。他以勤政著称——据说每天批阅奏章至深夜，朱批字数常常超过奏章本身。他推行了摊丁入亩、耗羡归公、改土归流等重大改革，设立军机处强化皇权，清查贪腐毫不手软。他的13年统治以其严格和不妥协著称——他不是最讨人喜欢的皇帝，但很可能是清朝最有效率的皇帝。",
  "Yinzhen prevailed in the brutal succession struggle — the 'Nine Princes' Contest' was Qing's most intense power battle. He was legendary for diligence, reportedly reviewing memorials into the night and writing vermilion rescripts longer than the original submissions. His major reforms — amalgamating the head tax into land tax, returning surcharges to the state treasury, and replacing native chieftains with imperial officials — together with creating the Grand Council to strengthen imperial authority and relentlessly pursuing corruption. His 13-year reign was defined by rigor and uncompromise — not the most likable emperor, but arguably Qing's most effective one.",
  ["胤禛", "Yinzhen"], ["src-qingshigao"], "", 0.9)

p("qing-guangxu", "光绪帝", "Guangxu Emperor", 1871, 1908, "qing-dynasty",
  ["君主", "皇帝", "清朝", "改革"], ["Ruler", "Emperor", "Qing Dynasty", "Reform"],
  "清朝第十一位皇帝载湉，试图通过戊戌变法改革自强，但被慈禧太后软禁至死。",
  "Eleventh Qing emperor who attempted modernization through the Hundred Days' Reform but was imprisoned by Empress Dowager Cixi until his death.",
  "载湉4岁即位，一生都在慈禧太后的阴影下。1898年他目睹甲午战败的屈辱后决心变法——百日维新期间连续发布上百道改革诏令，涵盖教育、军事、经济、政治各方面。但变法触动了保守派利益，慈禧发动戊戌政变将他软禁于瀛台，六君子血洒菜市口。此后十年他在囚禁中度过，1908年在慈禧去世前一天离奇死亡——2008年科学检测确认他是砒霜中毒。",
  "Zaitian ascended at 4 and lived his entire life under Empress Dowager Cixi's shadow. Stung by the 1895 defeat by Japan, he launched the Hundred Days' Reform in 1898 — issuing over a hundred reform edicts spanning education, military, economy, and governance. But the reforms threatened conservative interests; Cixi's coup confined him to Yingtai Pavilion and the Six Gentlemen were executed. He spent his last decade imprisoned, dying mysteriously one day before Cixi in 1908 — forensic tests in 2008 confirmed he died of arsenic poisoning.",
  ["载湉", "Zaitian"], ["src-qingshigao"], "", 0.85)

p("qing-puyi", "溥仪", "Puyi", 1906, 1967, "qing-dynasty",
  ["君主", "皇帝", "清朝"], ["Ruler", "Emperor", "Qing Dynasty"],
  "清朝末代皇帝，中国两千年帝制的终结者，一生三次登基三次退位。",
  "Last emperor of Qing and the final monarch of China's two-millennium imperial system; he ascended and abdicated three times in his extraordinary life.",
  "溥仪3岁即位，6岁退位——这是清朝的终结，也是中国两千年帝制的终结。然而他的人生比任何小说都离奇——1917年张勋复辟他短暂「复辟」12天，1932年又被日本人扶植为伪满洲国皇帝。1945年日本战败后他被苏联红军俘虏，1950年引渡回国在抚顺战犯管理所改造十年。1959年特赦后他成为一名普通公民和文史馆员，1967年在北京病逝。他的自传《我的前半生》记录了这段独一无二的经历。",
  "Puyi ascended at 3 and abdicated at 6 — ending not just the Qing dynasty but two millennia of Chinese imperial rule. Yet his life proved stranger than any novel: a brief 12-day 'restoration' under the warlord Zhang Xun in 1917, then installation as puppet emperor of Manchukuo by Japan in 1932. After Japan's defeat in 1945, he was captured by the Soviets, extradited to China in 1950, and spent a decade in the Fushun War Criminals Management Centre. Pardoned in 1959, he became an ordinary citizen and literary researcher, dying in Beijing in 1967. His autobiography 'From Emperor to Citizen' records this singular journey.",
  [], ["src-qingshigao"], "", 0.85)

# ============ OUTPUT ============
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
    alt = ", ".join(f"'{a}'" for a in person.get("alternativeNames", []))
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
print(f"\n// Total: {len(people)} Chinese emperors")
