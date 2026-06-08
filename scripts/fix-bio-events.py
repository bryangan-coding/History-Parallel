#!/usr/bin/env python3
"""
Fix biographical events by replacing specific fields within event blocks.
Safe approach: finds event by ID, replaces fields using regex.
"""
import re

MOCKDATA = 'src/data/mockData.ts'
with open(MOCKDATA) as f:
    content = f.read()

def add_fix(event_id, title, title_en, start_year, summary, summary_en, description, description_en, importance=4):
    """Replace specific fields within an event block."""
    global content
    # Find the event block by its id
    pattern = re.compile(rf"(id: '{event_id}',\n.*?)(?=\n  \}},\n  \{{\n    id: '|$)", re.DOTALL)
    match = pattern.search(content)
    if not match:
        print(f"  WARNING: Could not find {event_id}")
        return
    
    block = match.group(0)
    old_block = block
    
    # Replace fields
    block = re.sub(r"title: '[^']*'", f"title: '{title}'", block)
    title_en_esc = title_en.replace("'", "\\'")
    block = re.sub(r"titleEn: '[^']*'", f"titleEn: '{title_en_esc}'", block)
    block = re.sub(r"startYear: -?\d+", f"startYear: {start_year}", block)
    block = re.sub(r"endYear: -?\d+", f"endYear: {start_year}", block)
    
    def esc(s):
        return s.replace("'", "\\'")
    
    block = re.sub(r"summary: '[^']*'", f"summary: '{esc(summary)}'", block)
    block = re.sub(r"summaryEn: '[^']*'", f"summaryEn: '{esc(summary_en)}'", block)
    block = re.sub(r"description: '[^']*'", f"description: '{esc(description)}'", block)
    block = re.sub(r"descriptionEn: '[^']*'", f"descriptionEn: '{esc(description_en)}'", block)
    block = re.sub(r"importance: \d+", f"importance: {importance}", block)
    
    content = content.replace(old_block, block)
    print(f"  Fixed: {event_id} -> {title} ({start_year})")

# ========= Apply fixes =========
print("=== Fixing biographical events ===\n")

add_fix('evt-li-bai-major', '李白辞亲远游', 'Li Bai leaves home to wander the realm', 725,
    '开元十三年（725年），二十五岁的李白辞亲远游，仗剑出蜀，沿长江而下，途经江陵、洞庭、庐山等地，一路结交名士饮酒赋诗。这是他人生最重要的转折点，豪放不羁的游历为他浪漫壮丽的"诗仙"风格奠定了基础。',
    'In 725 at age 25, Li Bai departed Shu with his sword, sailing down the Yangtze. Visiting Jiangling, Lake Dongting, and Mount Lu, he befriended scholars and composed poetry, beginning the journey that would define his legendary poetic persona.',
    '开元十三年（725年），二十五岁的李白"仗剑去国，辞亲远游"，离开故乡蜀中，沿长江东下。这是他人生最重要的转折点。李白自幼博览群书又习剑术，出蜀后游历江陵、洞庭、庐山、金陵等地，一路赋诗交友。在江陵遇道教名士司马承祯得其赞赏；在金陵挥金如土，不到一年散尽三十万钱。《渡荆门送别》中"山随平野尽，江入大荒流"的诗句正写于此次出蜀途中。这种任侠豪放的生活方式，与他浪漫壮丽的"诗仙"风格相得益彰。',
    'In 725 at age 25, Li Bai departed his Shu homeland, sailing east along the Yangtze. Well-versed in classics and swordsmanship, he traveled through Jiangling, Lake Dongting, Mount Lu, and Jinling, befriending scholars. In Jiangling, Taoist master Sima Chengzhen praised him; in Jinling, he spent 300,000 cash within a year. His poem "Farewell at Jingmen" captures this journey: "Mountains give way to vast plains, the great river flows into the wilderness." This chivalrous lifestyle perfectly matched his bold, romantic poetic persona.',
    importance=4)

add_fix('evt-du-fu-major', '杜甫漫游吴越', 'Du Fu travels through Jiangnan', 735,
    '开元二十三年（735年），二十四岁的杜甫首次远游江南，在吴越一带漫游了三四年之久。他徜徉于苏州、杭州等名城，登临名胜古迹，开阔了视野，为其沉郁顿挫的诗风奠定了基础。',
    'In 735, the 24-year-old Du Fu left his study for his first great journey, spending three to four years traveling through the historic cities and landscapes of the Wu and Yue regions in Jiangnan.',
    '开元二十三年（735年），二十四岁的杜甫结束洛阳书斋生活，首次远游江南，在吴越一带漫游了三四年。他徜徉于苏州、杭州、绍兴等历史文化名城，登金陵凤凰台，访姑苏台旧址，泛舟太湖和鉴湖。这段经历让他见识了盛唐江南的富庶繁华，也接触了大量古代文化遗迹。后来他在诗中回忆："放荡齐赵间，裘马颇清狂。"与后来颠沛流离的生活相比，这是杜甫一生中最自由奔放的青年时代。',
    'In 735, the 24-year-old Du Fu left Luoyang for his first great journey, spending years exploring Suzhou, Hangzhou, and Shaoxing. He climbed historic terraces, visited ancient ruins, and boated on Taihu Lake, experiencing the prosperity of High Tang Jiangnan. Compared to his later displacement, this was his freest and most exuberant period.',
    importance=4)

add_fix('evt-emperor-taizong-major', '李世民劝父起兵', 'Li Shimin persuades his father to revolt', 617,
    '大业十三年（617年），李世民审时度势，联合裴寂、刘文静力劝其父太原留守李渊起兵反隋。七月李渊在太原誓师，李世民率军攻入长安，开启了唐朝建立的序幕。',
    'In 617, Li Shimin assessed the collapsing Sui dynasty and urged his father Li Yuan, governor of Taiyuan, to rebel. Li Yuan raised his army in July, with Li Shimin leading the charge to capture Chang\'an.',
    '大业十三年（617年），隋朝天下大乱。太原留守李渊卷入政治危机，其子李世民联合晋阳宫副监裴寂、晋阳县令刘文静，力劝父亲起兵。李渊起初犹豫，李世民与裴寂设计迫使其下定决心。七月李渊在太原誓师，李世民与兄长李建成分率左右两军直指长安。十一月攻克长安，李渊自任大丞相。次年五月李渊正式称帝建立唐朝。年仅二十岁的李世民展现出了卓越的军事谋略和组织才能。',
    'In 617, amid the Sui dynasty\'s collapse, Li Shimin joined forces with Pei Ji and Liu Wenjing to urge his father Li Yuan to revolt. After initial hesitation, Li Yuan raised his army at Taiyuan, with Li Shimin and his elder brother commanding two flanks toward Chang\'an. They captured the capital by November. The following year, Li Yuan founded the Tang dynasty. Though only twenty, Li Shimin demonstrated extraordinary strategic acumen.',
    importance=5)

add_fix('evt-wu-zetian-major', '武则天立为皇后', 'Wu Zetian is installed as Empress', 655,
    '永徽六年（655年），唐高宗力排众议废王皇后，立武则天为皇后。武则天由此掌握后宫与朝政实权，与高宗并称"二圣"，为其日后成为中国历史上唯一的女皇帝铺平了道路。',
    'In 655, Emperor Gaozong overrode objections to depose Empress Wang and install Wu Zetian. Wu seized power in the inner court and government, ruling jointly as the Two Sages, paving her path to becoming China\'s only female emperor.',
    '永徽六年（655年），唐高宗李治力排众议，废王皇后立武则天为皇后。武则天14岁入宫为太宗才人，太宗驾崩后入感业寺为尼，高宗即位后召回封为昭仪。在"废王立武"的政治斗争中，她争取到重臣李勣"此陛下家事"的支持。立为皇后后因高宗体弱多病，武则天得以批阅奏章处理政务，实际上与高宗并称"二圣"。这为她后来代唐建周、成为中国历史上唯一女皇帝奠定了基础。',
    'In 655, Emperor Gaozong deposed Empress Wang and installed Wu Zetian. Wu had entered the palace at 14, was sent to a convent after Taizong\'s death, then recalled by Gaozong. In the political struggle, she secured Chancellor Li Ji\'s crucial support. Once empress, Wu assumed governance due to Gaozong\'s poor health, ruling jointly as the Two Sages and paving her path to becoming China\'s only female emperor.',
    importance=5)

add_fix('evt-wang-anshi-major', '王安石进士及第', 'Wang Anshi passes the imperial examination', 1042,
    '庆历二年（1042年），22岁的王安石考中进士，名列第四名，授签书淮南判官。自此步入仕途，在地方任职中积累了丰富的治理经验，为其后来推行熙宁变法奠定了实践基础。',
    'In 1042, the 22-year-old Wang Anshi passed the imperial examination ranked fourth and was appointed Assistant Magistrate of Huainan, beginning a career of local governance that informed his later Xining Reforms.',
    '庆历二年（1042年），22岁的王安石进士及第，以第四名的成绩脱颖而出，授签书淮南判官。王安石自幼随父宦游各地，遍览民间疾苦。进士及第后他主动选择到地方任职，在鄞县（今浙江宁波）知县任上兴修水利、贷谷于民、改革学校，政绩为"江东第一"。十余年的基层经历让他深刻认识了北宋积贫积弱的症结。他后来向宋神宗提出的"变风俗，立法度"主张和"天变不足畏，祖宗不足法，人言不足恤"的改革精神，正是在此期间逐步形成的。',
    'In 1042, the 22-year-old Wang Anshi passed the examination ranked fourth. After traveling widely with his official father and witnessing common hardships, he voluntarily chose local postings. As magistrate of Yin County, he built waterworks, provided grain loans, and reformed schools. His reform philosophy—"Heavenly changes need not be feared, ancestral laws need not be followed, human criticism need not be heeded"—crystallized during these grassroots years.',
    importance=4)

add_fix('evt-su-shi-major', '苏轼进士及第', 'Su Shi and Su Zhe pass the imperial examination', 1057,
    '嘉祐二年（1057年），21岁的苏轼与19岁的弟弟苏辙同榜进士及第，轰动京师。主考官欧阳修读到苏轼文章时误以为是弟子曾巩所作，为避嫌将之列为第二，赞叹道："老夫当避路，放他出一头地也。"',
    'In 1057, the 21-year-old Su Shi and his 19-year-old brother Su Zhe both passed the examination. Chief examiner Ouyang Xiu, mistaking Su Shi\'s essay for his disciple\'s work, ranked it second and declared: "I must step aside and let this young man soar."',
    '嘉祐二年（1057年）是中国科举史上最光辉的一届。年仅21岁的苏轼与19岁的弟弟苏辙同榜进士及第，轰动京师。主考官欧阳修读到苏轼的《刑赏忠厚之至论》时拍案叫绝，误以为此文出自弟子曾巩之手，为避嫌忍痛将其列为第二名。欧阳修感慨："读轼书，不觉汗出，快哉快哉！老夫当避路，放他出一头地也。"苏轼自此名震天下。同榜还有曾巩、张载、程颢等日后的大儒名臣，堪称"千古第一榜"。',
    'In 1057, the most illustrious examination class in Chinese history, the 21-year-old Su Shi and 19-year-old Su Zhe both passed. Chief examiner Ouyang Xiu was overwhelmed by Su Shi\'s essay but mistook it for his disciple Zeng Gong\'s work and ranked it second, declaring: "I must step aside and let this young man soar." Fellow graduates included Zeng Gong, Zhang Zai, and Cheng Hao—truly an unprecedented gathering of talent.',
    importance=5)

add_fix('evt-sima-guang-major', '司马光进士及第', 'Sima Guang passes the imperial examination', 1038,
    '宝元元年（1038年），年仅20岁的司马光进士及第。他七岁便晓《左传》大义，"砸缸救友"的故事家喻户晓。后以刚正敢言著称，最终以编纂《资治通鉴》闻名于世。',
    'In 1038, the 20-year-old Sima Guang passed the imperial examination. A prodigy who grasped the Zuo Zhuan at seven and famously rescued a friend by smashing a water jar, he later compiled the monumental Zizhi Tongjian.',
    '宝元元年（1038年），年仅20岁的司马光以甲科进士及第。他七岁时听人讲《左传》便能领悟大意，"砸缸救友"的故事更是世代传诵。进士及第后历任华州判官、苏州判官等职，以刚正敢言著称。但司马光最大的贡献是耗费19年心血编纂的《资治通鉴》——一部涵盖战国至五代1362年历史的编年体巨著。宋神宗亲自赐名，意为"鉴于往事，有资于治道"。司马光与王安石虽在新法问题上势同水火，但二人在学术和私德上相互敬重，"君子之争"成为古代政治史的佳话。',
    'In 1038, the 20-year-old Sima Guang passed the examination with honors. A prodigy who grasped the Zuo Zhuan at seven and rescued a drowning friend, he served in various posts known for his courage. His greatest legacy was the Zizhi Tongjian—a 294-volume chronicle covering 1,362 years, compiled over 19 years. Emperor Shenzong bestowed the title meaning "a mirror for governance from past events." Though opposed to Wang Anshi\'s reforms, their "contest of gentlemen" remains a model of principled opposition.',
    importance=4)

add_fix('evt-ouyang-xiu-major', '欧阳修进士及第', 'Ouyang Xiu passes the imperial examination', 1030,
    '天圣八年（1030年），欧阳修以第一名通过省试后进士及第。他四岁丧父，母亲以荻草画沙教其识字——"画荻教子"千古流传。后成为北宋文坛领袖，位列"唐宋八大家"。',
    'In 1030, Ouyang Xiu passed the imperial examination with top provincial honors. Orphaned at four, his mother taught him to write with reed stalks on sand—the legendary "reed-painting" story. He became the Northern Song\'s leading literary figure.',
    '天圣八年（1030年），欧阳修以第一名通过省试后进士及第。他四岁丧父，家贫无纸笔，母亲郑氏以荻草画沙教他识字——"画荻教子"千古流传。进士及第后历任馆阁校勘、参知政事等职，因支持范仲淹改革屡遭贬谪。在文学上他领导了古文运动，力矫浮靡文风。《醉翁亭记》中"醉翁之意不在酒，在乎山水之间也"成为千古名句。他奖掖后进，苏轼、苏辙、曾巩皆受其提携，被誉为"一代文宗"。',
    'In 1030, Ouyang Xiu achieved first place in the provincial examination. Orphaned at four, too poor for brush and paper, his mother taught him to write with reed stalks on sand. After entering officialdom, he was repeatedly exiled for supporting Fan Zhongyan\'s reforms. In literature, he led the Classical Prose Movement; his masterpiece "The Old Drunkard\'s Pavilion" contains the immortal line about finding joy in nature rather than wine. He mentored Su Shi and others, earning the title of literary patriarch.',
    importance=5)

add_fix('evt-zhu-xi-major', '朱熹进士及第', 'Zhu Xi passes the imperial examination', 1148,
    '绍兴十八年（1148年），年仅19岁的朱熹进士及第。他自幼聪颖好学，后继承和发展二程理学，构建了庞大的哲学体系，成为程朱理学的集大成者，其思想影响了中国此后数百年。',
    'In 1148, the 19-year-old Zhu Xi passed the imperial examination. A brilliant scholar, he later synthesized the Cheng brothers\' Neo-Confucian philosophy into a comprehensive system that shaped Chinese thought for centuries.',
    '绍兴十八年（1148年），年仅19岁的朱熹以第五甲第九十名进士及第。他自幼聪颖，五岁能诵《孝经》，十四岁丧父后受父友教诲。进士及第后历任同安主簿、知南康军等地方职，但更重要的贡献在学术领域。他继承和发展了二程（程颢、程颐）的理学思想，在白鹿洞书院、岳麓书院讲学，编纂《四书章句集注》，将四书确立为儒家核心经典。朱熹的思想后来成为元明清三代科举考试的标准，影响东亚数百年。',
    'In 1148, the 19-year-old Zhu Xi passed the imperial examination. A prodigy who could recite the Classic of Filial Piety at five, he studied under his father\'s friends after being orphaned at fourteen. Though he served in local posts, his greatest contribution was academic—synthesizing the Cheng brothers\' Neo-Confucianism. Teaching at the White Deer Grotto and Yuelu Academies, he compiled the "Collected Commentaries on the Four Books," which became the standard for civil service examinations for centuries.',
    importance=4)

add_fix('evt-zhu-yuanzhang-major', '朱元璋投奔红巾军', 'Zhu Yuanzhang joins the Red Turban Rebellion', 1352,
    '至正十二年（1352年），25岁的朱元璋投奔郭子兴的红巾军起义。他作战勇猛又识字能文，很快获得赏识被提拔为九夫长，郭子兴还将养女马氏许配给他，由此开启从乞丐到皇帝的传奇人生。',
    'In 1352, the 25-year-old Zhu Yuanzhang joined Guo Zixing\'s Red Turban rebellion. His bravery and literacy earned rapid promotion, and Guo married his adopted daughter Lady Ma to him, beginning his legendary journey from beggar to emperor.',
    '至正十二年（1352年），元末天下大乱。朱元璋幼年家贫，父母兄长在灾荒和瘟疫中相继去世，他沦为乞丐后入皇觉寺为僧四处化缘。25岁那年，儿时玩伴汤和从濠州红巾军中来信劝他投军。朱元璋前往濠州投奔郭子兴，郭见其相貌奇伟收为亲兵。朱元璋作战骁勇又识字能文，很快被提拔为九夫长，郭子兴还将养女马氏许配给他——马氏即日后的马皇后。由此朱元璋从游方僧一步步成长为红巾军重要将领，最终推翻元朝建立大明帝国。',
    'In 1352, with the Yuan dynasty crumbling, Zhu Yuanzhang—who had lost his family to famine and become a mendicant monk—was urged by his childhood friend Tang He to join the Red Turban rebels. Presenting himself to Guo Zixing, his striking appearance impressed the rebel leader, who took him as a guard. Zhu fought bravely and could read and write, earning rapid promotion. Guo married his adopted daughter Lady Ma to Zhu. From a homeless monk, Zhu rose to become a key commander and ultimately founded the Ming dynasty in 1368.',
    importance=5)

add_fix('evt-zheng-he-major', '郑和首次下西洋', 'Zheng He embarks on his first voyage to the Western Ocean', 1405,
    '永乐三年（1405年），郑和奉明成祖之命，率领庞大船队首次下西洋。舰队拥有大小船只二百余艘、船员二万七千余人，先后访问占城、爪哇、苏门答腊等地，最远到达印度古里，开启了人类航海史上的壮举。',
    'In 1405, Zheng He commanded a massive fleet of over 200 vessels with 27,000 crew on his first voyage to the Western Ocean, visiting Champa, Java, Sumatra and reaching Calicut, India, inaugurating one of history\'s greatest maritime enterprises.',
    '永乐三年（1405年）七月，明成祖命郑和为正使，率领当时世界上最大的船队从苏州刘家港启航。郑和本姓马，云南昆阳人，幼年被明军掳入宫中成为太监，后因战功赐姓郑。船队拥有大小船只二百余艘、船员二万七千八百余人。先后到达占城（越南南部）、爪哇、旧港（巨港）、苏门答腊、满剌加（马六甲），最远抵达古里（印度卡利卡特）。郑和每到一处便宣读永乐帝诏书、赏赐当地国王、建立友好贸易关系。首次下西洋历时两年于1407年返航，标志着明朝海上丝绸之路的鼎盛时代。',
    'In July 1405, the Yongle Emperor appointed Zheng He as chief envoy to command the world\'s largest fleet at the time—over 200 vessels with 27,800 crew. Originally surnamed Ma from Yunnan, Zheng He was captured as a child, castrated, and later given his imperial surname for military valor. His fleet visited Champa, Java, Sumatra, Malacca, and reached Calicut on India\'s Malabar Coast. The two-year voyage concluded in 1407, inaugurating the golden age of the Ming Maritime Silk Road.',
    importance=5)

add_fix('evt-li-shizhen-major', '李时珍开始编纂本草纲目', 'Li Shizhen begins compiling the Bencao Gangmu', 1552,
    '嘉靖三十一年（1552年），李时珍鉴于历代本草著作多有谬误，决心编纂一部全面准确的药物学巨著。他辞去太医院职务，先后深入各地名山大川采集标本，历时27年完成《本草纲目》，被达尔文誉为"中国古代的百科全书"。',
    'In 1552, recognizing errors in earlier pharmacological texts, Li Shizhen resolved to compile a comprehensive materia medica. Over 27 years, he traveled extensively to collect specimens, producing the Bencao Gangmu, which Darwin praised as "the ancient Chinese encyclopedia."',
    '嘉靖三十一年（1552年），已是名医的李时珍在行医实践中发现历代本草书籍谬误甚多——如将毒物与良药混为一谈。他立下宏愿编纂《本草纲目》，为此辞去太医院院判之职，走出书斋，"远穷僻壤之产，险探仙麓之华"，足迹遍及湖北、江西、江苏、安徽等地名山大川。他亲自采集品尝药材，向药农樵夫渔民请教，收集了大量民间验方。历经27年三易其稿，完成52卷190多万字的巨著，收录药物1892种、附方11096首，这部著作被达尔文誉为"中国古代的百科全书"。',
    'In 1552, already a respected physician, Li Shizhen grew frustrated with errors in earlier pharmacological texts. He resolved to compile the Bencao Gangmu, resigned from the Imperial Medical Academy, and ventured to remote regions across Hubei, Jiangxi, Jiangsu, and Anhui, personally collecting and tasting herbs and consulting local healers. After 27 years and three revisions, he completed 52 volumes cataloging 1,892 medicinal substances with 11,096 prescriptions—a work Darwin praised as "the ancient Chinese encyclopedia.',
    importance=5)

add_fix('evt-kangxi-major', '康熙智擒鳌拜', 'Kangxi Emperor outwits the regent Oboi', 1669,
    '康熙八年（1669年），年仅16岁的康熙帝表面沉迷布库（满族摔跤）游戏，暗中训练满洲少年擒拿之术，在武英殿一举擒获专横跋扈的辅政大臣鳌拜，从此亲掌朝政，开启了中国历史上最长的帝王统治。',
    'In 1669, at age sixteen, the Kangxi Emperor feigned an obsession with Manchu wrestling while secretly training young warriors, then captured the autocratic regent Oboi in the Hall of Martial Valor, seizing personal control of the government.',
    '康熙八年（1669年）五月，紫禁城内上演了一场精心策划的政变。康熙帝8岁即位时由四大臣辅政，但鳌拜专横跋扈不把少年天子放在眼里。康熙表面沉迷布库（满族摔跤）游戏，暗中挑选数十名满洲少年苦练擒拿之术。五月十六日，康熙召鳌拜入武英殿，一声令下这群布库少年一拥而上将鳌拜当场擒获——"智擒鳌拜"成为千古传奇。16岁的康熙帝除掉心腹大患后正式亲政，不久后平定三藩之乱、收复台湾、驱逐沙俄、三征噶尔丹，开创了康乾盛世。',
    'In May 1669, a carefully orchestrated palace coup unfolded in the Forbidden City. Having ascended at age eight under a regency, the young Kangxi feigned an obsession with Manchu wrestling while secretly training youths. Summoning Oboi to the Hall of Martial Valor, he ordered the wrestlers to seize him on the spot—the famous "outwitting of Oboi." At sixteen, Kangxi formally assumed rule and went on to suppress rebellions, conquer Taiwan, expel Russian incursions, and subdue Galdan Khan, inaugurating the High Qing era.',
    importance=5)

add_fix('evt-qianlong-major', '乾隆平定准噶尔', 'Qianlong Emperor conquers the Dzungar Khanate', 1755,
    '乾隆二十年（1755年），乾隆帝抓住准噶尔内乱之机，命班第、永常分两路出兵远征伊犁，彻底消灭了困扰清朝近百年的准噶尔汗国，将天山南北正式纳入版图，奠定现代中国西北边疆。',
    'In 1755, seizing on Dzungar internal strife, the Qianlong Emperor dispatched two armies to capture Ili, decisively destroying the khanate that had troubled the Qing for nearly a century and incorporating the region as Xinjiang.',
    '乾隆二十年（1755年）是清朝版图奠定的关键之年。自康熙年间噶尔丹崛起以来，准噶尔蒙古一直是清朝西北最大威胁，战事绵延近百年。1755年准噶尔内部分裂，辉特部台吉阿睦尔撒纳投奔清朝提供重要情报。乾隆帝果断出兵，以班第、永常为将各率二万五千精兵分两路远征伊犁。五月清军会师博罗塔拉，准噶尔首领达瓦齐猝不及防被擒，汗国灭亡。此役使天山南北正式纳入清朝版图，随后的驻军屯田将这片土地定名为"新疆"——意为"故土新归"。',
    'In 1755, a pivotal year for Qing territorial expansion, internal Dzungar succession struggles presented opportunity after nearly a century of conflict. When Amursana defected with crucial intelligence, the Qianlong Emperor dispatched two armies of 25,000 each to capture Ili. In May, Qing forces converged at Bortala, capturing the Dzungar leader Dawachi and destroying the khanate. The region was formally incorporated and garrisoned, officially named "Xinjiang"—"the New Frontier.',
    importance=5)

add_fix('evt-cao-xueqin-major', '曹雪芹开始创作红楼梦', 'Cao Xueqin begins writing Dream of the Red Chamber', 1744,
    '约乾隆九年（1744年），家道中落的曹雪芹在北京西郊香山脚下的陋室中开始创作《红楼梦》。他以自身家族从繁华到衰败的经历为蓝本，"披阅十载，增删五次"，完成了这部中国古典小说巅峰之作的前八十回。',
    'Around 1744, the impoverished Cao Xueqin began writing Dream of the Red Chamber at the foot of Fragrant Hills west of Beijing. Drawing on his own family\'s fall from wealth, he spent a decade revising, completing eighty chapters of China\'s greatest classical novel.',
    '约乾隆九年（1744年），曹雪芹在北京西郊香山脚下的陋室中开始提笔创作《红楼梦》。他出身江宁织造曹家，祖父曹寅是康熙帝宠臣，家族四次接驾南巡。雍正年间家族被抄，从金陵富贵之乡沦为北京贫民。晚年移居香山"蓬牖茅椽、绳床瓦灶"，以卖画和亲友接济为生。"字字看来皆是血，十年辛苦不寻常"——他以血泪之笔描绘了四大家族兴衰的爱情悲剧与社会画卷。曹雪芹生前未能完成全部创作即去世，前八十回成为世界文学史上不朽的经典。',
    'Around 1744, in a humble dwelling at Fragrant Hills, Cao Xueqin began writing Dream of the Red Chamber. Born into the illustrious Cao family of imperial textile commissioners who had hosted the Kangxi Emperor, his family was disgraced and stripped of wealth under Yongzheng. Reduced to poverty, he survived on charity and selling paintings. "Every word is written in blood, ten bitter years of extraordinary labor"—he poured his experience of the rise and fall of great families into the story, completing eighty chapters before his death. The work became an immortal classic of world literature.',
    importance=5)

# Write back
with open(MOCKDATA, 'w') as f:
    f.write(content)
print(f"\nDone. Fixed events in {MOCKDATA}")
