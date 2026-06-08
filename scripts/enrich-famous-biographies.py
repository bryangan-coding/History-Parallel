#!/usr/bin/env python3
"""
Fix biographical events by replacing entire event blocks.
Uses bracket-matching to find block boundaries safely.
"""
import re
from pathlib import Path

MOCKDATA = Path('src/data/mockData.ts')
lines = MOCKDATA.read_text(encoding='utf-8').split('\n')

def find_event_block(event_id):
    """Find start and end line of an event block by ID."""
    start = None
    for i, line in enumerate(lines):
        if f"id: '{event_id}'" in line or f'id: "{event_id}"' in line:
            start = i
            break
    if start is None:
        return None, None
    
    # Go up to find the opening brace of the event object
    while start > 0 and not lines[start].strip().startswith('{'):
        start -= 1
    
    # Find matching closing brace
    depth = 0
    end = start
    for i in range(start, len(lines)):
        line = lines[i]
        depth += line.count('{') - line.count('}')
        if depth == 0:
            end = i
            break
    
    return start, end

def replace_event_block(event_id, new_block_lines):
    """Replace an entire event block."""
    start, end = find_event_block(event_id)
    if start is None:
        print(f"  WARNING: Could not find event {event_id}")
        return False
    
    lines[start:end+1] = new_block_lines
    print(f"  Fixed: {event_id} (lines {start+1}-{end+1})")
    return True

def build_event_block(title, title_en, start_year, end_year, summary, summary_en, description, description_en, person_id, region='song-dynasty', importance=4, tags=['人物', '成就'], tags_en=['Biography', 'Achievement']):
    """Build a TypeScript event block."""
    # Escape single quotes in strings
    s_title = title.replace("'", "\\'")
    se_title = title_en.replace("'", "\\'").replace('"', '\\"')
    s_sum = summary.replace("'", "\\'").replace('"', '\\"')
    se_sum = summary_en.replace("'", "\\'").replace('"', '\\"')
    s_desc = description.replace("'", "\\'").replace('"', '\\"')
    se_desc = description_en.replace("'", "\\'").replace('"', '\\"')
    
    block = f"""  {{
    title: '{s_title}',
    titleEn: '{se_title}',
    startYear: {start_year},
    endYear: {end_year},
    regionId: '{region}',
    coordinates: undefined,
    placeName: '',
    personIds: ['{person_id}'],
    tags: {tags},
    tagsEn: {tags_en},
    summary: '{s_sum}',
    summaryEn: '{se_sum}',
    description: '{s_desc}',
    descriptionEn: '{se_desc}',
    sourceIds: [],
    importance: {importance},
    datePrecision: 'year' as const,
    isApproximate: false,
    relatedEventIds: [],
    dataStatus: 'published' as const,
    confidenceScore: 0.9,
    externalReferences: [],
  }}"""
    return block.split('\n')

# ============ Define fixes ============

FIXES = [
    # Tang Dynasty
    ('evt-li-bai-major', 
     '李白辞亲远游', 'Li Bai leaves home to wander as a wandering knight',
     725, 725,
     '开元十三年（725年），二十五岁的李白辞亲远游，仗剑出蜀，开始了他豪迈壮阔的漫游生涯。他沿长江而下，途经江陵、洞庭、庐山等地，一路结交名士，饮酒赋诗。《渡荆门送别》中的"山随平野尽，江入大荒流"正写于此次出蜀途中。',
     'In 725 at age 25, Li Bai departed his Shu homeland, sword at his side, sailing down the Yangtze. He visited Jiangling, Lake Dongting, and Mount Lu, befriending scholars and composing poetry. "Mountains give way to vast plains, the great river flows into the wilderness" was written during this journey.',
     '开元十三年（725年），年方二十五岁的李白"仗剑去国，辞亲远游"，离开故乡蜀中，沿长江东下。这是他人生最重要的转折点。李白自幼博览群书又习剑术，出蜀后游历江陵、洞庭、庐山、金陵等地，一路赋诗交友。在江陵，他遇见了道教名士司马承祯，得其赞赏；在金陵，他饮酒赋诗、挥金如土，不到一年散尽三十万钱。《渡荆门送别》中"山随平野尽，江入大荒流"的诗句正写于此次出蜀途中。这种任侠豪放的生活方式与他浪漫壮丽的诗风相得益彰。',
     'In 725 at age 25, Li Bai "left home with his sword," sailing east along the Yangtze — his life most pivotal moment. Well-versed in classics and swordsmanship, he traveled through Jiangling, Lake Dongting, Mount Lu, and Jinling. In Jiangling, Taoist master Sima Chengzhen praised him. In Jinling, he spent 300,000 cash within a year. The poem "Farewell at Jingmen" captures the moment: "Mountains give way to vast plains, the great river flows into the wilderness.',
     'li-bai',4),
    
    ('evt-du-fu-major',
     '杜甫漫游吴越', 'Du Fu travels through the Wu and Yue regions',
     735, 735,
     '开元二十三年（735年），二十四岁的杜甫结束了书斋生活，首次远游江南，在吴越一带漫游了三四年之久。他徜徉于苏杭等历史文化名城，登临名胜古迹，开阔了视野，为其沉郁顿挫的诗风奠定了基础。',
     'In 735, the 24-year-old Du Fu left his study for his first great journey, spending three years exploring the historic cities and landscapes of the Wu and Yue regions, broadening his horizons and gathering material for his future poetry.',
     '开元二十三年（735年），二十四岁的杜甫结束洛阳书斋生活，首次远游江南，在吴越（今苏南、浙江）漫游了三四年。他徜徉于苏州、杭州、绍兴等历史文化名城，登金陵凤凰台，访姑苏台旧址，泛舟太湖和鉴湖。这段经历让他见识了盛唐江南的富庶繁华，也接触了大量古代文化遗迹。后来他在诗中回忆："放荡齐赵间，裘马颇清狂。"与后来颠沛流离的生活相比，这是杜甫一生中最自由奔放的青年时代。',
     'In 735, the 24-year-old Du Fu left Luoyang for a three-year journey through the Wu and Yue regions. He wandered through Suzhou, Hangzhou, and Shaoxing, climbed historic terraces, and boated on Taihu and Jianhu Lakes. The experience exposed him to the prosperity of High Tang Jiangnan and its ancient cultural relics. He later recalled: "Reckless and wild in the Qi and Zhao lands." Compared to his later displacement, this was Du Fu freest period.',
     'du-fu',4),
    
    ('evt-emperor-taizong-major',
     '李世民劝父起兵', 'Li Shimin persuades his father to rebel against the Sui',
     617, 617,
     '大业十三年（617年），李世民审时度势，联合裴寂、刘文静等人力劝其父太原留守李渊起兵反隋。七月李渊在太原誓师，李世民率军攻入长安，开启了唐朝建立的序幕。',
     'In 617, Li Shimin assessed the collapsing Sui and urged his father Li Yuan, governor of Taiyuan, to rebel. Li Yuan raised his army in July, with Shimin leading troops to capture Chang\'an — the prelude to founding the Tang dynasty.',
     '大业十三年（617年），隋朝天下大乱。太原留守李渊卷入宫廷政治危机，其子李世民联合晋阳宫副监裴寂、晋阳县令刘文静，力劝父亲起兵。李渊起初犹豫，李世民与裴寂设计迫使李渊下定决心。七月，李渊在太原誓师，李世民与兄长李建成分率左右两军直指长安。十一月攻克长安后立代王杨侑为帝，李渊自任大丞相。次年五月（618年）李渊正式称帝建立唐朝。年仅二十岁的李世民展现出了卓越的军事谋略和组织能力。',
     'In 617, amid the collapse of the Sui dynasty, Li Shimin joined forces with Pei Ji and Liu Wenjing to urge his father Li Yuan to revolt. After initial hesitation, Li Yuan raised his army at Taiyuan in July, with Shimin and his elder brother commanding two flanks toward Chang\'an. They captured the capital by November. The following year, Li Yuan founded the Tang dynasty. Though only twenty, Li Shimin demonstrated extraordinary strategic ability throughout the campaign.',
     'emperor-taizong',5),
    
    ('evt-wu-zetian-major',
     '武则天立为皇后', 'Wu Zetian is installed as Empress',
     655, 655,
     '永徽六年（655年），唐高宗力排众议废王皇后，立武则天为皇后。武则天由此掌握后宫与朝政实权，与高宗并称"二圣"，为其日后成为中国历史上唯一女皇帝铺平了道路。',
     'In 655, Emperor Gaozong overrode all objections to depose Empress Wang and install Wu Zetian. Wu seized power in both the inner court and government, ruling jointly with Gaozong as the "Two Sages," paving her path to becoming China\'s only female emperor.',
     '永徽六年（655年），唐高宗李治力排众议，废王皇后立武则天为皇后。武则天14岁入宫为太宗才人，太宗驾崩后入感业寺为尼。高宗即位后将其召回封为昭仪。在废王立武的政治斗争中，她争取到重臣李勣"此陛下家事"的支持。立为皇后后，因高宗体弱多病，武则天得以批阅奏章、处理政务，实际上与高宗并称"二圣"。这为其后来代唐建周、成为中国历史上唯一的女皇帝奠定了基础。',
     'In 655, Emperor Gaozong deposed Empress Wang and installed Wu Zetian. Wu had entered the palace at 14, was sent to a convent after Taizong\'s death, then recalled by Gaozong. In the political struggle, she secured the crucial support of Chancellor Li Ji. Once empress, Wu gradually assumed governance due to Gaozong\'s poor health, ruling jointly as the "Two Sages." This paved her path to founding the Zhou dynasty and becoming China\'s only female emperor.',
     'wu-zetian',5),
    
    # Song Dynasty
    ('evt-wang-anshi-major',
     '王安石进士及第', 'Wang Anshi passes the imperial examination',
     1042, 1042,
     '庆历二年（1042年），22岁的王安石考中进士，名列第四名，授签书淮南判官。自此步入仕途，在地方任上积累了丰富的治理经验，为其后来推行熙宁变法奠定了基础。',
     'In 1042, the 22-year-old Wang Anshi passed the imperial examination ranked fourth and was appointed Assistant Magistrate of Huainan, beginning a career of local governance that would inform his later Xining Reforms.',
     '庆历二年（1042年），22岁的王安石进士及第，以第四名的成绩脱颖而出，授签书淮南判官。王安石自幼随父宦游各地，遍览民间疾苦。进士及第后他主动选择到地方任职，在鄞县（今浙江宁波）知县任上兴修水利、贷谷于民、改革学校，政绩为"江东第一"。十余年的基层经历让他深刻认识了北宋积贫积弱的症结。他后来向宋神宗提出的"变风俗，立法度"主张，以及"天变不足畏，祖宗不足法，人言不足恤"的改革精神，正是在此期间逐步形成的。',
     'In 1042, the 22-year-old Wang Anshi passed the imperial examination with distinction, ranking fourth. Having traveled with his official father and witnessed common people\'s hardships, Wang voluntarily chose local postings. As magistrate of Yin County (modern Ningbo), he built water infrastructure, provided grain loans, and reformed schools — earning recognition as the best-governed region. His reform philosophy — "Heavenly portents need not be feared, ancestral laws need not be followed, human criticism need not be heeded" — crystallized during these grassroots years.',
     'wang-anshi',4),
    
    ('evt-su-shi-major',
     '苏轼进士及第', 'Su Shi and Su Zhe pass the imperial examination',
     1057, 1057,
     '嘉祐二年（1057年），21岁的苏轼与19岁的弟弟苏辙同榜进士及第。主考官欧阳修读到苏轼文章时误以为是弟子曾巩所作，为避嫌将之列为第二，并赞叹道："老夫当避路，放他出一头地也。"',
     'In 1057, the 21-year-old Su Shi and his 19-year-old brother Su Zhe both passed the examination. Chief examiner Ouyang Xiu mistook Su Shi\'s essay for his disciple\'s work and ranked it second, declaring: "I must step aside and let this young man soar."',
     '嘉祐二年（1057年）是中国科举史上最光辉的一届。21岁的苏轼与19岁的弟弟苏辙同榜进士及第，轰动京师。主考官欧阳修读到苏轼的《刑赏忠厚之至论》时拍案叫绝，误以为此文出自弟子曾巩之手，为避嫌忍痛将其列为第二名。欧阳修感叹："读轼书，不觉汗出，快哉快哉！老夫当避路，放他出一头地也。"苏轼自此名震天下。同榜还有曾巩、张载、程颢等日后的大儒名臣，堪称"千古第一榜"。',
     'In 1057, the most illustrious examination class in Chinese history, the 21-year-old Su Shi and 19-year-old Su Zhe both passed. Chief examiner Ouyang Xiu was overwhelmed by Su Shi\'s essay "On Generosity in Punishment and Reward" but mistook it for his disciple Zeng Gong\'s work and ranked it second, declaring: "I must step aside and let this young man soar." Fellow graduates included Zeng Gong, Zhang Zai, and Cheng Hao — truly an unprecedented gathering of talent.',
     'su-shi',5),
    
    ('evt-sima-guang-major',
     '司马光进士及第', 'Sima Guang passes the imperial examination',
     1038, 1038,
     '宝元元年（1038年），年仅20岁的司马光进士及第。他七岁便晓《左传》大义，"砸缸救友"的故事家喻户晓。及第后以刚正敢言著称，最终以编纂《资治通鉴》闻名于世。',
     'In 1038, the 20-year-old Sima Guang passed the imperial examination. A prodigy who grasped the Zuo Zhuan at seven and famously rescued a drowning friend, he was known for his integrity and later became famous for compiling the Zizhi Tongjian.',
     '宝元元年（1038年），年仅20岁的司马光以甲科进士及第。司马光七岁时听人讲《左传》便能领悟大意，"砸缸救友"的故事更是世代传诵。及第后他历任华州判官、苏州判官等地方职，以刚正敢言闻名。但司马光最大的贡献是耗费19年心血编纂的《资治通鉴》——一部涵盖战国至五代1362年历史的编年体巨著。宋神宗亲自赐名，意为"鉴于往事，有资于治道"。司马光与王安石虽在新法问题上势同水火，但二人在学术和私德上相互敬重，其"君子之争"成为古代政治史的佳话。',
     'In 1038, the 20-year-old Sima Guang passed the imperial examination with honors. A prodigy who grasped the Zuo Zhuan at seven and famously rescued a friend by smashing a water jar, Sima served in various posts known for his courage in remonstrating. His greatest legacy was the Zizhi Tongjian — a monumental 294-volume chronicle covering 1,362 years, compiled over 19 years. Emperor Shenzong bestowed the title, meaning "a mirror for governance from past events." Though fiercely opposed to Wang Anshi\'s reforms, their "contest of gentlemen" remains a model of principled political opposition.',
     'sima-guang',4),
    
    ('evt-ouyang-xiu-major',
     '欧阳修进士及第', 'Ouyang Xiu passes the imperial examination',
     1030, 1030,
     '天圣八年（1030年），欧阳修以第一名通过省试，随后进士及第。他四岁丧父，母亲以荻草画沙教其识字。后成为北宋文坛领袖，位列"唐宋八大家"。',
     'In 1030, Ouyang Xiu passed the imperial examination with top provincial honors. Orphaned at four, his mother taught him to write using reed stalks on sand. He became the Northern Song\'s leading literary figure.',
     '天圣八年（1030年），欧阳修以第一名通过省试后进士及第。欧阳修四岁丧父，家贫无纸笔，母亲郑氏以荻草画沙教他识字——"画荻教子"千古流传。进士及第后历任馆阁校勘、参知政事等职，因支持范仲淹改革屡遭贬谪。在文学上，他领导古文运动，力矫浮靡文风，提出"文以道俱"的主张。《醉翁亭记》"醉翁之意不在酒，在乎山水之间也"成为千古名句。他奖掖后进，苏轼、苏辙、曾巩皆受其提携，被誉为"一代文宗"。',
     'In 1030, Ouyang Xiu achieved first place in the provincial examination before becoming a jinshi. Orphaned at four and too poor for brush and paper, his mother taught him to write with reed stalks on sand — the immortal "reed-painting" story. After entering officialdom, he was repeatedly exiled for supporting Fan Zhongyan\'s reforms. In literature, he led the Classical Prose Movement, advocating that "writing should convey the Way." His masterpiece "The Old Drunkard\'s Pavilion" contains the immortal line about the drunkard\'s heart being in the scenery, not the wine. He mentored Su Shi, Su Zhe, and Zeng Gong, becoming the literary patriarch of his generation.',
     'ouyang-xiu',5),
    
    # Ming Dynasty
    ('evt-zhu-yuanzhang-major',
     '朱元璋投奔红巾军', 'Zhu Yuanzhang joins the Red Turban Rebellion',
     1352, 1352,
     '至正十二年（1352年），25岁的朱元璋投奔郭子兴的红巾军起义。他作战勇猛又识字能文，很快获得赏识被提拔为九夫长，郭子兴还将养女马氏许配给他，由此开启从乞丐到皇帝的传奇人生。',
     'In 1352, the 25-year-old Zhu Yuanzhang joined Guo Zixing\'s Red Turban rebellion. His bravery and literacy earned him rapid promotion, and Guo married his adopted daughter Lady Ma to him — beginning his legendary journey from beggar to emperor.',
     '至正十二年（1352年），元末天下大乱。朱元璋幼年家贫，父母兄长在灾荒和瘟疫中相继去世，他沦为乞丐后入皇觉寺为僧四处化缘。25岁那年，儿时玩伴汤和从濠州红巾军中来信劝他投军。朱元璋前往濠州投奔郭子兴，郭见其相貌奇伟收为亲兵。朱元璋作战骁勇又识字能文，很快被提拔为九夫长，郭子兴还将养女马氏许配给他——马氏即日后的马皇后。由此，朱元璋从游方僧一步步成长为红巾军重要将领，最终推翻元朝建立大明帝国。',
     'In 1352, with the Yuan dynasty collapsing, Zhu Yuanzhang — who had lost his family to famine, begged, and become a novice monk — received a letter from his childhood friend Tang He urging him to join the Red Turbans. Presenting himself to Guo Zixing, his striking appearance impressed the rebel leader, who took him as a personal guard. Zhu fought bravely and could read and write — rare among soldiers — earning rapid promotion. Guo married his adopted daughter Lady Ma (the future Empress Ma) to Zhu. From a homeless mendicant monk, Zhu rose to become a key Red Turban commander and ultimately founded the Ming dynasty in 1368.',
     'zhu-yuanzhang',5),
    
    ('evt-zheng-he-major',
     '郑和首次下西洋', 'Zheng He embarks on his first voyage to the Western Ocean',
     1405, 1405,
     '永乐三年（1405年），郑和奉明成祖之命率领庞大船队首次下西洋。舰队从苏州刘家港出发，拥有大小船只二百余艘、船员二万七千余人，先后访问了占城、爪哇、苏门答腊等地，最远到达印度古里，开启了人类航海史上的壮举。',
     'In 1405, Zheng He commanded a massive fleet of over 200 vessels with 27,000 crew on his first voyage to the Western Ocean by order of the Yongle Emperor. Visiting Champa, Java, Sumatra and reaching Calicut, India, this inaugurated one of history\'s greatest maritime enterprises.',
     '永乐三年（1405年）七月，明成祖命郑和为正使，率领当时世界上最大的船队从苏州刘家港启航，开始了规模空前的远洋航行。郑和本姓马，云南昆阳人，幼年被明军掳入宫中成为太监，后因战功赐姓郑。船队有大小船只二百余艘、船员二万七千八百余人，拥有当时世界上最大的宝船。船队先后到达占城（越南南部）、爪哇、旧港（巨港）、苏门答腊、满剌加（马六甲），最远抵达古里（印度卡利卡特）。郑和每到一处便宣读永乐帝诏书、赏赐当地国王、建立友好贸易关系。历时两年于1407年返航，标志着明朝海上丝绸之路的鼎盛时代。',
     'In July 1405, the Yongle Emperor appointed Zheng He as chief envoy to command the largest fleet in the world at the time — over 200 vessels with 27,800 crew. Originally surnamed Ma from Yunnan, Zheng He was captured as a child, castrated, and later given his imperial surname for military valor. His fleet visited Champa, Java, Sumatra, Malacca, and reached Calicut on India\'s Malabar Coast. At each port, Zheng He proclaimed the emperor\'s edicts, bestowed gifts, and established trade relations. The two-year voyage concluded in 1407, inaugurating the golden age of the Ming Maritime Silk Road.',
     'zheng-he',5),
    
    ('evt-li-shizhen-major',
     '李时珍开始编纂本草纲目', 'Li Shizhen begins compiling the Bencao Gangmu',
     1552, 1552,
     '嘉靖三十一年（1552年），李时珍鉴于历代本草多有谬误，决心编纂一部全面准确的药物学巨著。他辞去太医院职务，深入山林采集标本，向药农樵夫渔民请教，开启了历时27年的《本草纲目》编纂工作。',
     'In 1552, recognizing errors in earlier pharmacological texts, Li Shizhen resolved to compile a comprehensive materia medica. He resigned from the Imperial Medical Academy, ventured into the wilderness, and consulted herb gatherers and fishermen — beginning 27 years of work on the Bencao Gangmu.',
     '嘉靖三十一年（1552年），已是名医的李时珍在行医实践中发现历代本草书籍谬误甚多，立下宏愿编纂《本草纲目》。为此他辞去太医院院判之职，走出书斋，"远穷僻壤之产，险探仙麓之华"，足迹遍及湖北、江西、江苏、安徽等地名山大川。他亲自采集品尝药材，向药农樵夫渔民请教，收集了大量民间验方。历经27年三易其稿，完成52卷190多万字的《本草纲目》，收录药物1892种、附方11096首。这部著作被达尔文誉为"中国古代的百科全书"。',
     'In 1552, already a respected physician, Li Shizhen grew frustrated with traditional pharmacological texts riddled with errors. He resolved to compile the Bencao Gangmu, resigned from the Imperial Medical Academy, and ventured to remote regions across Hubei, Jiangxi, Jiangsu, and Anhui, personally collecting and tasting herbs and consulting local healers. After 27 years and three revisions, he completed 52 volumes cataloging 1,892 medicinal substances with 11,096 prescriptions — a work Darwin praised as "the ancient Chinese encyclopedia.',
     'li-shizhen',5),
    
    # Qing Dynasty
    ('evt-kangxi-major',
     '康熙智擒鳌拜', 'Kangxi Emperor outwits the regent Oboi',
     1669, 1669,
     '康熙八年（1669年），年仅16岁的康熙帝表面沉迷布库游戏，暗中训练满洲少年擒拿之术，在武英殿一举擒获专横跋扈的辅政大臣鳌拜，从此亲掌朝政，开启了中国历史上最长的帝王统治。',
     'In 1669, at age sixteen, the Kangxi Emperor — feigning an obsession with Manchu wrestling — secretly trained young warriors. Summoning the autocratic regent Oboi to the Hall of Martial Valor, his wrestlers captured him on the spot, allowing Kangxi to seize personal control and begin the longest imperial reign in Chinese history.',
     '康熙八年（1669年）五月，紫禁城内上演了一场精心策划的宫廷政变。康熙帝8岁即位时由四大臣辅政，但鳌拜专横跋扈不把少年天子放在眼里。康熙表面沉迷布库游戏，暗中挑选数十名满洲少年苦练擒拿之术。五月十六日，康熙召鳌拜入武英殿，一声令下，这群布库少年一拥而上将鳌拜当场擒获——这便是"智擒鳌拜"。16岁的康熙帝除掉心腹大患后正式亲政，不久后又平定三藩、收复台湾、驱逐沙俄、三征噶尔丹，开创了康乾盛世。',
     'In May 1669, a carefully orchestrated palace coup unfolded. The Kangxi Emperor, who had ascended at age eight under a regency, secretly trained Manchu youths in wrestling while appearing absorbed in the sport. On May 16, he summoned Oboi to the Hall of Martial Valor and ordered the wrestlers to seize him — the famous "outwitting of Oboi." At sixteen, having eliminated his greatest obstacle, Kangxi formally assumed rule and went on to suppress rebellions, conquer Taiwan, expel Russian incursions, and subdue Galdan Khan, inaugurating the High Qing era.',
     'kangxi',5),
    
    ('evt-qianlong-major',
     '乾隆平定准噶尔', 'Qianlong Emperor conquers the Dzungar Khanate',
     1755, 1755,
     '乾隆二十年（1755年），乾隆帝抓住准噶尔内乱之机，命班第、永常分两路远征伊犁，彻底消灭了困扰清朝近百年的准噶尔汗国，将天山南北正式纳入版图，奠定现代中国西北边疆的基础。',
     'In 1755, seizing on Dzungar internal strife, the Qianlong Emperor dispatched two armies to capture Ili, decisively destroying the khanate that had troubled the Qing for nearly a century and incorporating the region into the empire as Xinjiang.',
     '乾隆二十年（1755年）是清朝版图奠定的关键之年。自康熙年间噶尔丹崛起以来，准噶尔蒙古一直是清朝西北最大的威胁，战事绵延近百年。1755年准噶尔内部分裂，辉特部台吉阿睦尔撒纳投奔清朝提供重要情报。乾隆帝果断出兵，以班第、永常为将各率两万五千精兵分两路远征伊犁。五月清军会师博罗塔拉，准噶尔首领达瓦齐猝不及防被擒，汗国灭亡。此役使天山南北正式纳入清朝版图，随后的驻军屯田将这片土地定名为"新疆"——意为"故土新归"。',
     'In 1755, a pivotal year for Qing territorial expansion, internal Dzungar succession struggles presented an opportunity after nearly a century of conflict. When Amursana defected with crucial intelligence, the Qianlong Emperor dispatched two armies of 25,000 each under Bandi and Yongchang toward Ili. In May, the Qing forces converged at Bortala, capturing the Dzungar leader Dawachi and destroying the khanate. The region was formally incorporated into the empire and garrisoned, officially named "Xinjiang" — "the New Frontier.',
     'qianlong',5),
    
    ('evt-cao-xueqin-major',
     '曹雪芹开始创作红楼梦', 'Cao Xueqin begins writing Dream of the Red Chamber',
     1744, 1744,
     '约乾隆九年（1744年），家道中落的曹雪芹在北京西郊香山脚下的陋室中开始创作《红楼梦》。他以自身家族从繁华到衰败的经历为蓝本，"披阅十载，增删五次"，完成了这部中国古典小说的巅峰之作的前八十回。',
     'Around 1744, the impoverished Cao Xueqin began writing Dream of the Red Chamber in his humble dwelling at the foot of Fragrant Hills west of Beijing. Drawing on his own family\'s fall from wealth, he spent a decade revising, completing eighty chapters of China\'s greatest classical novel.',
     '约乾隆九年（1744年），曹雪芹在北京西郊香山脚下的陋室中开始提笔创作《红楼梦》。他出身江宁织造曹家，祖父曹寅是康熙帝宠臣，家族四次接驾南巡。雍正年间家族被抄，从金陵富贵之乡迁回北京沦为贫民。晚年移居香山"蓬牖茅椽、绳床瓦灶"，以卖画和亲友接济为生。"字字看来皆是血，十年辛苦不寻常"——他以血泪之笔描绘了四大家族兴衰的爱情悲剧与社会画卷，将亲身经历融入贾宝玉、林黛玉等人物命运之中。曹雪芹生前未能完成全部创作即去世，留下的前八十回最终成为世界文学史上不朽的经典。',
     'Around 1744, in a humble dwelling at Fragrant Hills west of Beijing, Cao Xueqin began writing Dream of the Red Chamber. Born into the illustrious Cao family of Jiangning textile commissioners who had hosted the Kangxi Emperor on four southern tours, Cao\'s world collapsed when the family was disgraced under Yongzheng. Reduced to poverty, he survived on friends\' charity and selling paintings. "Every word is written in blood, ten bitter years" — he poured his life\'s experience of the rise and fall of great families into the story of Jia Baoyu and Lin Daiyu. Cao died before completing the work, but the eighty finished chapters became an immortal classic of world literature.',
     'cao-xueqin',5),
    
    ('evt-zhu-xi-major',
     '朱熹进士及第', 'Zhu Xi passes the imperial examination',
     1148, 1148,
     '绍兴十八年（1148年），年仅19岁的朱熹进士及第。他自幼聪颖好学，后继承和发展二程理学，成为程朱理学的集大成者，其思想影响了中国此后数百年。',
     'In 1148, the 19-year-old Zhu Xi passed the imperial examination. A brilliant scholar from childhood, he later synthesized the Neo-Confucian philosophy of the Cheng brothers, becoming its greatest exponent and shaping Chinese thought for centuries.',
     '绍兴十八年（1148年），年仅19岁的朱熹以第五甲第九十名进士及第。朱熹自幼聪颖，五岁能诵《孝经》，十四岁丧父后受父友刘子翚等人教诲。进士及第后历任同安主簿、知南康军等地方官职，但更重要的贡献在学术领域。他继承并发展了二程（程颢、程颐）的理学思想，构建了庞大的哲学体系。他在白鹿洞书院、岳麓书院讲学，编纂《四书章句集注》，将《大学》《中庸》《论语》《孟子》确立为儒家核心经典。朱熹的思想后来成为元明清三代科举考试的标准，影响东亚数百年。',
     'In 1148, the 19-year-old Zhu Xi passed the imperial examination. A prodigy who could recite the Classic of Filial Piety at age five, he studied under his father\'s friends after being orphaned at fourteen. Though he served in various local posts, his greatest contribution was academic — synthesizing the Cheng brothers\' Neo-Confucianism into a comprehensive philosophical system. Teaching at the White Deer Grotto and Yuelu Academies, he compiled the "Collected Commentaries on the Four Books," establishing the Analects, Mencius, Great Learning, and Doctrine of the Mean as core Confucian texts. His interpretation became the standard for civil service examinations throughout the Yuan, Ming, and Qing dynasties.',
     'zhu-xi',4),
]

# Apply fixes
print("=== Fixing biographical events ===\n")
for fix in FIXES:
    evt_id = fix[0]
    # Unpack: evt_id, title, title_en, start_year, end_year, summary, summary_en, desc, desc_en, person_id, importance=4
    new_block = build_event_block(
        title=fix[1],
        title_en=fix[2],
        start_year=fix[3],
        end_year=fix[4],
        summary=fix[5],
        summary_en=fix[6],
        description=fix[7],
        description_en=fix[8],
        person_id=fix[9],
        importance=fix[10] if len(fix) > 10 else 4,
    )
    replace_event_block(evt_id, new_block)

# Write back
MOCKDATA.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(f"\nDone. Fixed {len(FIXES)} events.")
