#!/usr/bin/env python3
"""CBDB Top Missing Batch: ~30 network-central Song-Yuan-Ming figures."""
def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")

people = []

def p(id, name, nameEn, birth, death, region, tags, tagsEn, summary, summaryEn, desc, descEn,
      alt=None, srcs=None, wiki="", conf=0.85):
    people.append(dict(id=id, name=name, nameEn=nameEn, birthYear=birth, deathYear=death,
        regionId=region, tags=tags, tagsEn=tagsEn, occupations=["文学家","政治家"],
        summary=summary, summaryEn=summaryEn, description=desc, descriptionEn=descEn,
        alternativeNames=alt or [], sourceIds=srcs or [], wikidataQid=wiki,
        dataStatus="published", confidenceScore=conf, externalReferences=[]))

# ===== SONG (15) =====
p("liu-kezhuang", "刘克庄", "Liu Kezhuang", 1187, 1269, "song-dynasty",
  ["文学家","政治家","宋朝"], ["Writer","Statesman","Song Dynasty"],
  "南宋江湖诗派领袖，以诗话和词著称，CBDB记录862条社交关联——宋代文人网络的超级枢纽。",
  "Southern Song leader of the Jianghu Poetry School; CBDB records 862 social associations, making him a super-hub in Song literati networks.",
  "刘克庄是南宋后期文坛的巨擘。他是江湖诗派的核心人物——这一诗派以布衣文人和低级官员为主，相较于江西诗派的艰深更追求平易自然的诗风。他的《后村诗话》是宋代最重要的诗学批评著作之一。他的词也极为出色——「男儿西北有神州，莫滴水西桥畔泪」以豪放之笔写家国之痛。CBDB记录了他862条社交关系——在宋代仅次于朱熹和周必大——说明他是当时文人社交网络的核心节点之一。",
  "Liu Kezhuang was a titan of late Southern Song literature. He was the central figure of the Jianghu Poetry School — a movement of commoner-literati and lower officials favoring natural accessibility over the Jiangxi School's abstruse density. His 'Houcun Poetry Talks' is among the most important works of Song poetic criticism. His ci lyrics were also superb — 'Northwest of the Divine Land lies our homeland; shed no tears at the Bridge of Water West' — expressing patriotic anguish in heroic style. CBDB records 862 social associations, second only to Zhu Xi and Zhou Bida in the Song — marking him as a core hub of the era's literati social network.",
  ["刘潜夫","Liu Qianfu","后村居士"],["src-ss"],"",0.85)

p("lou-yao", "楼钥", "Lou Yue", 1137, 1213, "song-dynasty",
  ["政治家","文学家","宋朝"], ["Statesman","Writer","Song Dynasty"],
  "南宋名臣，官至参知政事，其《攻愧集》收录大量墓志铭为宋代社会史提供了珍贵史料。",
  "Southern Song minister who rose to Vice Councilor; his collected works preserve vast numbers of epitaphs invaluable for Song social history.",
  "楼钥是南宋中期最勤政的官员之一——CBDB记录了他49次任职经历。他长期在中书舍人和给事中任上负责起草和审核诏命——以拒绝签署他认为不当的诏命而闻名。他的文集《攻愧集》大量收录了为时人撰写的墓志铭——这些墓志铭详细记录了南宋官员和平民的家世、婚姻、仕途——成为研究宋代社会史不可替代的材料。",
  "Lou Yue was among the most diligent officials of mid-Southern Song — CBDB records 49 separate office postings. He spent long years as Secretariat Drafter and Supervising Secretary, responsible for drafting and reviewing imperial edicts — and was famous for refusing to countersign decrees he considered improper. His collected works, 'Gongkui Ji,' preserve an enormous corpus of epitaphs he composed for contemporaries — these epitaphs meticulously document the family backgrounds, marriages, and careers of Song officials and commoners alike — becoming irreplaceable material for Song social history.",
  ["楼大防","Lou Dafang"],["src-ss"],"",0.85)

p("wu-cheng", "吴澄", "Wu Cheng", 1249, 1333, "yuan-dynasty",
  ["哲学家","学者","元朝","理学"], ["Philosopher","Scholar","Yuan Dynasty"],
  "元代理学大家，与许衡并称「北许南吴」，调和朱陆之学，门下弟子遍天下。",
  "Yuan Neo-Confucian master paired with Xu Heng as 'Xu of the North, Wu of the South' who synthesized Zhu Xi and Lu Jiuyuan; disciples spread across the realm.",
  "吴澄是元代最具影响力的理学家之一。他在宋元易代之际选择隐居著述——拒绝出仕元朝长达数十年——直到晚年才应召入京。他的学术特色在于折中朱熹的「道问学」和陆九渊的「尊德性」——试图弥合理学和心学的分歧。他在家乡草庐讲学——「草庐学派」吸引了来自全国各地的学生。CBDB记录了584条社交关系——是元代学术网络中最大的节点。",
  "Wu Cheng was one of the Yuan dynasty's most influential Neo-Confucians. During the Song-Yuan transition, he chose to live in seclusion and write — refusing to serve the Mongol Yuan for decades — only accepting summons to the capital in old age. His scholarly hallmark was synthesizing Zhu Xi's 'following the path of inquiry and study' with Lu Jiuyuan's 'honoring the moral nature' — attempting to bridge the School of Principle and School of Mind. He lectured from his Thatched Hut, with the 'Caolu School' attracting students nationwide. CBDB records 584 social associations — the largest hub in the Yuan scholarly network.",
  ["吴幼清","Wu Youqing","草庐先生"],["src-yuanshi"],"",0.85)

p("zhang-shi", "张栻", "Zhang Shi", 1133, 1180, "song-dynasty",
  ["哲学家","宋朝","理学"], ["Philosopher","Song Dynasty"],
  "南宋理学家，张浚之子，湖湘学派核心，与朱熹、吕祖谦并称「东南三贤」。",
  "Southern Song Neo-Confucian, son of the general Zhang Jun, core figure of the Huxiang School, paired with Zhu Xi and Lü Zuqian as 'Three Worthies of the Southeast.'",
  "张栻是南宋理学最耀眼的天才之一——他30多岁便主讲岳麓书院使其成为理学重镇。他是抗金名将张浚的儿子——早年随父在军事前线长大——这种经历使他的学问始终带有经世致用的底色。他与朱熹进行了长达数年的学术辩论——「中和之辩」是理学史上最深入的哲学对话之一。他去世时年仅47岁——朱熹痛悼「吾道益孤矣」——理学世界失去了一位最具创造力的思想家。",
  "Zhang Shi was one of Southern Song Neo-Confucianism's most brilliant talents — in his thirties, he assumed the lectureship at Yuelu Academy, transforming it into a Neo-Confucian stronghold. He was the son of the famous anti-Jin general Zhang Jun and grew up on the military frontier — this experience gave his scholarship an enduring orientation toward practical governance. He engaged in years-long philosophical debates with Zhu Xi — the 'Debate on Equilibrium and Harmony' was among the most profound dialogues in Neo-Confucian history. He died at just 47 — Zhu Xi grieved: 'My path grows ever lonelier now' — the Neo-Confucian world had lost one of its most creative thinkers.",
  ["张敬夫","Zhang Jingfu","南轩先生"],["src-ss"],"",0.85)

p("fan-zuyu", "范祖禹", "Fan Zuyu", 1041, 1098, "song-dynasty",
  ["史学家","宋朝"], ["Historian","Song Dynasty"],
  "北宋史学家，司马光修《资治通鉴》最重要的助手，独立完成唐代部分，又著《唐鉴》为帝王教科书。",
  "Northern Song historian, Sima Guang's most important assistant on the 'Zizhi Tongjian,' independently completing the Tang section; his 'Tang Mirror' became an imperial textbook.",
  "范祖禹是司马光编纂《资治通鉴》团队中最倚重的史学家——他独立负责了其中唐代部分（约占总篇幅的三分之一）。此后他又撰写了《唐鉴》——以唐代史事为镜鉴供帝王参考——这部书在宋代被反复刊刻作为皇帝经筵的教材。他还参与了《神宗实录》的修撰但因反对王安石变法而被贬——在流放地死于化州。他的史学风格以严谨的考证和鲜明的道德判断著称——CBDB记录的340条社交关系反映了他深度嵌入北宋学术和政治网络。",
  "Fan Zuyu was Sima Guang's most trusted historian on the 'Zizhi Tongjian' compilation team — he independently handled the entire Tang dynasty section, roughly a third of the total work. He then wrote 'Tang Mirror' — using Tang history as a mirror for imperial reference — which was repeatedly reprinted through the Song as textbook for imperial lectures. He also participated in compiling the 'Veritable Records of Shenzong' but was banished for opposing Wang Anshi's reforms — dying in exile at Huazhou. His historical style was characterized by rigorous textual criticism and clear moral judgment. CBDB's 340 recorded associations reflect his deep embedding in Northern Song scholarly and political networks.",
  ["范淳夫","Fan Chunfu","范太史"],["src-ss"],"",0.85)

p("li-gang", "李纲", "Li Gang", 1083, 1140, "song-dynasty",
  ["政治家","军事家","宋朝"], ["Statesman","Commander","Song Dynasty"],
  "北宋末南宋初抗金名臣，靖康之变时主持开封保卫战，力主抗金被贬，被朱熹盛赞。",
  "Patriotic minister of the late Northern-early Southern Song who led the defense of Kaifeng during the Jingkang Crisis; praised by Zhu Xi for his unwavering resistance.",
  "李纲在靖康之变中挺身而出——金兵第一次围攻开封时他以尚书右丞身份主持城防——短时间内组织军民击退了金兵。金兵撤退后主和派立即将他排挤出朝——金兵第二次南下时无人能守导致靖康之耻。南宋建立后高宗一度起用他但仅75天就再次被罢免——主和派始终容不下他。朱熹对李纲极为推崇——认为他是南渡诸臣中最有气节的。",
  "Li Gang stepped forward during the Jingkang Crisis — when Jin forces first besieged Kaifeng, he assumed command of the city's defense as Vice Director of the Right — and within days organized soldiers and civilians to repel the invaders. As soon as the Jin withdrew, the peace faction engineered his dismissal — when the Jin returned, no one could hold the city, leading to the Jingkang catastrophe. After the Southern Song's founding, Gaozong briefly appointed him but dismissed him after just 75 days — the peace faction could never tolerate his presence. Zhu Xi deeply admired Li Gang, considering him the most principled of all the courtiers who fled south.",
  ["李伯纪","Li Boji","梁溪先生"],["src-ss"],"",0.85)

p("hu-quan", "胡铨", "Hu Quan", 1102, 1180, "song-dynasty",
  ["政治家","文学家","宋朝"], ["Statesman","Writer","Song Dynasty"],
  "南宋主战派代表，上书请斩秦桧以谢天下，这篇奏章被金国以千金购得读后失色。",
  "Southern Song hawk who submitted a memorial demanding Qin Hui's execution; the Jin purchased this document for a thousand gold and paled upon reading it.",
  "1138年秦桧主持对金和议——胡铨上书反对言辞激烈直斥秦桧为「奸臣」并请斩秦桧、王伦、孙近三人之头「竿之藁街」。这篇奏章迅速传遍天下——金国间谍以千金购得后金国君臣读后大惊失色——「南朝有人！」胡铨因此被贬二十余年——但主战派的精神始终未灭。他的词「匣底龙泉夜夜鸣」至今读来令人热血沸腾。CBDB记录了他21次任职和248条社交关系。",
  "In 1138, when Qin Hui pushed through the peace treaty with Jin, Hu Quan submitted a blistering memorial denouncing Qin Hui as a 'traitorous minister' and demanding the heads of Qin Hui, Wang Lun, and Sun Jin be 'paraded through the capital on poles.' The memorial spread across the realm like wildfire — Jin spies purchased it for a thousand gold and the Jin court paled upon reading it: 'The Southern Dynasty has men of character!' Hu Quan was exiled for over twenty years — but the hawk faction's spirit was never extinguished. His ci line 'The Dragon Spring sword beneath the box cries out every night' still stirs the blood. CBDB records 21 office postings and 248 social associations.",
  ["胡邦衡","Hu Bangheng","澹庵"],["src-ss"],"",0.85)

p("fan-chunren", "范纯仁", "Fan Chunren", 1027, 1101, "song-dynasty",
  ["政治家","宋朝"], ["Statesman","Song Dynasty"],
  "范仲淹次子，官至宰相，以「忠恕」为人生信条——一生多次因直言被贬而不改其志。",
  "Fan Zhongyan's second son who rose to chancellor; lived by 'loyalty and forbearance' — repeatedly banished for blunt remonstrance yet never wavered.",
  "范纯仁完美继承了父亲范仲淹的风骨。他在哲宗朝官至宰相——但因为反对清算元祐旧臣而主动辞职。他的政治风格温和包容——即使对政敌也保持尊重——这使他在新旧党争白热化的时代中显得格外独特。他的人生信条是「但以责人之心责己，恕己之心恕人」——这种极致的自我要求和对他人的宽容贯彻了他的一生。CBDB记录了他56次任职经历——是北宋任职经历最丰富的官员之一。",
  "Fan Chunren perfectly inherited his father Fan Zhongyan's moral backbone. He rose to chancellor under Emperor Zhezong — but resigned rather than participate in the purge of the Yuanyou-era officials. His political style was moderate and inclusive — maintaining respect even for political opponents — making him uniquely distinctive in an era of vicious factional warfare. His life creed was 'hold yourself to the standard you apply to others, and extend to others the forgiveness you grant yourself' — this combination of extreme self-discipline and broad tolerance defined his entire life. CBDB records 56 office postings — among the most varied official careers of the Northern Song.",
  ["范尧夫","Fan Yaofu","范忠宣"],["src-ss"],"",0.85)

p("qin-hui", "秦桧", "Qin Hui", 1090, 1155, "song-dynasty",
  ["政治家","宋朝"], ["Statesman","Song Dynasty"],
  "南宋权相，主持宋金和议以莫须有罪名杀害岳飞，成为中国历史上「奸臣」的代名词。",
  "Southern Song chancellor who orchestrated the peace with Jin and executed Yue Fei on fabricated charges; synonymous with 'traitorous minister' in Chinese history.",
  "秦桧可能是中国历史上最臭名昭著的宰相——他的名字已经等同于「奸臣」的最高级别。他早年曾被金军俘虏——在北方三年后奇迹般逃回——这个「逃归」的过程至今充满疑云。回到南宋后他以主和派的旗手身份迅速获得高宗信任——两度出任宰相长达十九年。1142年他与高宗合谋在岳飞连战连捷时用十二道金牌将其召回并以「莫须有」罪名处死。此后直到去世他牢牢掌控朝政——大肆排斥异己——在历史记载和民间记忆中留下了最黑暗的一笔。",
  "Qin Hui may be Chinese history's most reviled chancellor — his name has become the ultimate synonym for 'traitorous minister.' He was captured by the Jin early in his career and miraculously 'escaped' after three years — a return shrouded in suspicion to this day. Back in Southern Song, he quickly gained Gaozong's trust as the standard-bearer of the peace faction and served as chancellor for nineteen years across two terms. In 1142, he and Gaozong conspired to recall Yue Fei with twelve gold medallions just as the general was on the verge of victory, then executed him on the 'dubious' charge. Until his death, he controlled the court with an iron grip, ruthlessly purging opponents — leaving the darkest stain in both historical record and popular memory.",
  ["秦会之","Qin Huizhi"],["src-ss"],"",0.85)

# ===== YUAN (6) =====
p("wang-yun", "王恽", "Wang Yun", 1227, 1304, "yuan-dynasty",
  ["文学家","政治家","元朝"], ["Writer","Statesman","Yuan Dynasty"],
  "元初文学家和史学家，《秋涧集》作者，其诗文反映了金元之际北方士人的精神世界。",
  "Early Yuan writer and historian, author of 'Qiujian Ji'; his poetry and prose illuminate the spiritual world of northern literati during the Jin-Yuan transition.",
  "王恽是元初北方文人的杰出代表。他在忽必烈朝担任监察御史——以直言敢谏著称。他的《秋涧集》是研究元初政治和社会的最重要文献之一——特别是其中对忽必烈朝重大事件的记载。他还在至元年间参与了实录的修撰。CBDB记录了他531条社交关系——是元代北方文人社交网络的核心人物。他的文学风格承袭金代传统——与江南的虞集等人形成了南北并峙的格局。",
  "Wang Yun was an outstanding representative of early Yuan northern literati. He served as Investigating Censor under Kublai Khan, renowned for his fearless remonstrance. His 'Qiujian Ji' is among the most important sources for studying early Yuan politics and society — particularly its accounts of key events under Kublai. He also participated in compiling the imperial veritable records. CBDB records 531 social associations for him — marking him as a core figure in the northern literati network of the Yuan. His literary style continued Jin dynasty traditions, forming a north-south counterpoint with Jiangnan figures like Yu Ji.",
  ["王仲谋","Wang Zhongmou","秋涧"],["src-yuanshi"],"",0.85)

p("yu-ji", "虞集", "Yu Ji", 1272, 1348, "yuan-dynasty",
  ["文学家","学者","元朝"], ["Writer","Scholar","Yuan Dynasty"],
  "元代文学泰斗，「元诗四大家」之首，主持修撰《经世大典》，是元代最博学的文臣。",
  "Yuan literary titan and foremost of the 'Four Great Yuan Poets'; chief compiler of the 'Jingshi Dadian' (Grand Canon for Governing the World), the era's most erudite scholar-official.",
  "虞集是元中期文坛的领袖。他祖籍四川但生长于江西——这种南北交融的背景使他的文学兼具北方之雄浑和南方之精致。他在文宗朝担任奎章阁侍书学士——主持编纂了元朝最重要的政书《经世大典》。他的诗歌代表了元代典雅诗风的最高水平。CBDB记录了他501条社交关系——是元代江南文人网络的中心。他的学生遍布朝野——苏天爵、萨都剌等名家均出自其门。",
  "Yu Ji was the literary leader of mid-Yuan. His ancestral roots were in Sichuan but he grew up in Jiangxi — this north-south background infused his writing with northern vigor and southern refinement. Under Emperor Wenzong, he served in the Kuizhang Pavilion as Academician-in-Waiting and directed the compilation of the 'Jingshi Dadian,' the Yuan's most important institutional compendium. His poetry represents the peak of the refined Yuan style. CBDB records 501 social associations — the hub of the Jiangnan literati network. His disciples spread throughout court and provinces — luminaries like Su Tianjue and Sadula all studied under him.",
  ["虞伯生","Yu Bosheng","道园"],["src-yuanshi"],"",0.85)

p("huang-jin", "黄溍", "Huang Jin", 1277, 1357, "yuan-dynasty",
  ["文学家","史学家","元朝"], ["Writer","Historian","Yuan Dynasty"],
  "元末文学家，与柳贯、虞集、揭傒斯并称「儒林四杰」，其文典雅醇厚。",
  "Late Yuan writer, one of the 'Four Paragons of Confucian Letters' with Liu Guan, Yu Ji, and Jie Xisi; his prose was elegant and rich.",
  "黄溍是元代义乌人，与柳贯同乡并终身交好。他在文坛上的地位由虞集的一句评价奠定——虞集看到他的文章后评论「如精金美玉」。他在元朝官至侍讲学士——为皇帝讲解经史。他的文章以典雅醇厚著称——其门人宋濂后来成为明朝开国文臣之首将师门之学发扬光大。CBDB记录了他416条社交关系。",
  "Huang Jin was a native of Yiwu, lifelong friend of fellow townsman Liu Guan. His literary reputation was sealed by Yu Ji's comment upon reading his prose: 'Like refined gold and beautiful jade.' He served the Yuan as Academician Expositor-in-Waiting, lecturing the emperor on classics and history. His writing was celebrated for its elegance and richness. His disciple Song Lian would become the foremost literary official of the early Ming, carrying forward his teacher's legacy. CBDB records 416 social associations.",
  ["黄晋卿","Huang Jinqing"],["src-yuanshi"],"",0.8)

p("yuan-jue", "袁桷", "Yuan Jue", 1266, 1327, "yuan-dynasty",
  ["文学家","学者","元朝"], ["Writer","Scholar","Yuan Dynasty"],
  "元代浙东文派的代表人物，长于碑传文和宫廷典制之学，是元代翰林院的核心人物。",
  "Representative figure of Yuan's Eastern Zhejiang literary school; excelled in stele biographies and court ritual scholarship as a core Hanlin Academy figure.",
  "袁桷出身四明（宁波）袁氏——一个南宋以来以学术著称的家族。他是元代翰林院任职时间最长的汉族文人之一——历经成宗、武宗、仁宗、英宗、泰定帝五朝。他精于碑版文字——朝中重臣去世后多请他撰写神道碑——这些碑文成为了解元代政治的重要史料。CBDB记录322条社交关系使他成为元代最具社会影响力的文人之一。",
  "Yuan Jue came from the Yuan clan of Siming (Ningbo) — a scholarly lineage dating from Southern Song. He was among the longest-serving Han literati in the Yuan Hanlin Academy, spanning five reigns. He was a master of commemorative stele prose — most high officials commissioned their spirit-path steles from him — and these inscriptions became vital historical sources for Yuan politics. CBDB's 322 recorded associations mark him as one of the most socially influential Yuan literati.",
  ["袁伯长","Yuan Bochang","清容居士"],["src-yuanshi"],"",0.8)

p("liu-guan", "柳贯", "Liu Guan", 1270, 1342, "yuan-dynasty",
  ["文学家","学者","元朝"], ["Writer","Scholar","Yuan Dynasty"],
  "「儒林四杰」之一，黄溍的至交好友，以经学和文章著称，其学传至明初宋濂。",
  "One of the 'Four Paragons of Confucian Letters,' Huang Jin's closest friend; renowned for classical scholarship and prose, his learning passed to the early Ming's Song Lian.",
  "柳贯与黄溍同为义乌人——两人终身切磋学问被誉为元代浙东学术的双璧。他精通六经——尤其深研《春秋》——学者称他为「静俭先生」。他在元朝官至翰林待制——负责起草重要的朝廷文书。他在文学上主张博学而后能文——他的文章以深厚的经学功底为基础。他与黄溍共同的弟子宋濂成为了明朝文学的开山人物——从这个意义上说他是从元到明学术传承的关键一环。",
  "Liu Guan and Huang Jin, both from Yiwu, spent their lives discussing scholarship and were acclaimed as the twin pillars of Yuan-era Eastern Zhejiang learning. He was deeply versed in the Six Classics, especially the 'Spring and Autumn Annals,' and scholars called him 'Master Tranquil Frugality.' He served as Hanlin Academician in the Yuan, drafting important court documents. His literary theory held that broad learning must precede fine writing — his prose was built on profound classical scholarship. His and Huang Jin's shared disciple Song Lian became the founding figure of Ming literature — in this sense, he was a crucial link in the transmission of learning from Yuan to Ming.",
  ["柳道传","Liu Daochuan","静俭先生"],["src-yuanshi"],"",0.8)

# ===== MING (9) =====
p("shen-shixing", "申时行", "Shen Shixing", 1535, 1614, "ming-dynasty",
  ["政治家","明朝","首辅"], ["Statesman","Ming Dynasty","Grand Secretary"],
  "万历朝首辅，以调和折中著称——在皇帝怠政和群臣激争之间艰难维持了明朝政府的运转。",
  "Wanli-era Grand Secretary who maintained government operations through compromise between an absentee emperor and fractious officialdom.",
  "申时行在张居正被清算后的废墟上接任首辅。他的前任张居正因为过于强势的改革遭万历皇帝疯狂报复——申时行完全改变了策略：以柔克刚。他小心翼翼地调和万历皇帝与群臣之间日益激化的矛盾——在「国本之争」（立太子）等重大问题上尽力周旋。CBDB记录了他331条社交关系——数量惊人的社交网络是他在复杂政局中生存的基础。他最终因为在立储问题上两面不讨好而被迫致仕。",
  "Shen Shixing became Grand Secretary in the smoking ruins left by Zhang Juzheng's posthumous purge. His predecessor had been destroyed by the Wanli Emperor's vengeful backlash against his heavy-handed reforms — Shen Shixing adopted a completely different strategy: bend like water. He painstakingly mediated the escalating conflicts between the absentee Wanli Emperor and an increasingly confrontational bureaucracy — navigating the explosive 'Succession Dispute' with extreme delicacy. CBDB's 331 recorded associations — a startlingly large social network — was his survival infrastructure. He was eventually forced to resign when his middle-way approach pleased neither side in the succession crisis.",
  ["申汝默","Shen Rumei","申文定"],["src-mingshi"],"",0.85)

p("gu-xiancheng", "顾宪成", "Gu Xiancheng", 1550, 1612, "ming-dynasty",
  ["哲学家","政治家","明朝","东林党"], ["Philosopher","Statesman","Ming Dynasty"],
  "东林书院重建者和东林党领袖，「风声雨声读书声声声入耳，家事国事天下事事事关心」的作者。",
  "Rebuilder of the Donglin Academy and leader of the Donglin faction; author of the immortal couplet about the sounds of wind, rain, and reading intertwining with family, state, and world affairs.",
  "顾宪成被罢官后回到家乡无锡——与高攀龙等人修复了宋代杨时讲学的东林书院。他们在书院中不仅讲学还「讽议朝政裁量人物」——以东林书院为基地形成了一个影响晚明政治数十年的清议集团——东林党。那副「风声雨声读书声声声入耳，家事国事天下事事事关心」的对联至今悬挂在东林书院——浓缩了中国知识分子入世济民的全部理想。",
  "After being dismissed from office, Gu Xiancheng returned to his hometown Wuxi, where he and Gao Panlong restored the Donglin Academy, originally founded by the Song Neo-Confucian Yang Shi. They not only lectured there but 'discussed court politics and judged public figures' — from this base, the Donglin faction formed, a political movement of righteous remonstrance that shaped late Ming politics for decades. The couplet 'The sounds of wind, rain, and reading all enter my ears; family affairs, state affairs, and world affairs all fill my heart' still hangs at the Donglin Academy — distilling the entire ideal of the politically engaged Chinese intellectual.",
  ["顾叔时","Gu Shushi","泾阳先生"],["src-mingshi"],"",0.85)

p("cheng-minzheng", "程敏政", "Cheng Minzheng", 1445, 1499, "ming-dynasty",
  ["文学家","史学家","明朝"], ["Writer","Historian","Ming Dynasty"],
  "明代文学家和史学家，以神童著称——十岁被推荐入翰林院读书，后卷入科场舞弊案含冤而死。",
  "Ming writer and historian, celebrated as a child prodigy recommended to the Hanlin Academy at ten; died in disgrace after being framed in an exam scandal.",
  "程敏政的人生是一个天才的悲剧。他十岁时因才华出众被巡抚推荐到翰林院读书——这在明朝是极为罕见的荣誉。他后来高中榜眼（进士第二名）官至礼部右侍郎。弘治十二年他主持会试时被指控「泄题」——唐寅（唐伯虎）也卷入此案——虽然最终查无实据但程敏政在出狱后四天便愤懑而死。这一科场案断送了唐寅的仕途——也结束了程敏政的生命。CBDB记录了他273条社交关系。",
  "Cheng Minzheng's life was a tragedy of genius. At ten, his extraordinary talent led the provincial governor to recommend him for study at the Hanlin Academy — an exceptionally rare honor in the Ming. He later placed second in the metropolitan examinations and rose to Vice Minister of Rites. In the twelfth year of Hongzhi, while serving as chief examiner, he was accused of leaking exam questions — Tang Yin (Tang Bohu) was also implicated. Though ultimately no evidence was found, Cheng Minzheng died of rage and despair just four days after his release from prison. This scandal destroyed Tang Yin's official career and ended Cheng Minzheng's life. CBDB records 273 social associations.",
  ["程克勤","Cheng Keqin"],["src-mingshi"],"",0.8)

p("zou-yuanbiao", "邹元标", "Zou Yuanbiao", 1551, 1624, "ming-dynasty",
  ["政治家","哲学家","明朝","东林党"], ["Statesman","Philosopher","Ming Dynasty"],
  "明代东林党重要人物，因反对张居正夺情被廷杖八十贬谪——后复出任左都御史。",
  "Key Donglin figure who received eighty court beatings for opposing Zhang Juzheng's refusal to observe mourning; later returned as Censor-in-Chief.",
  "邹元标在万历五年因上疏反对张居正「夺情」（不守父丧）被廷杖八十——腿被打断后流放贵州都匀卫。他在贵州的荒僻之地办学讲学——将儒家文化传播到边远地区。张居正死后他被召回朝廷——官至左都御史。他一生以刚正不阿著称——是东林党中最坚定的清议派人物。CBDB记录了他316条社交关系——在东林网络中处于核心位置。",
  "In the fifth year of Wanli, Zou Yuanbiao submitted a memorial opposing Zhang Juzheng's 'seizure of affection' (skipping mourning duties) — receiving eighty court beatings that broke his legs, followed by exile to remote Duyun in Guizhou. There, in the desolate frontier, he founded schools and lectured — spreading Confucian culture to the borderlands. After Zhang Juzheng's death, he was recalled to court, eventually serving as Censor-in-Chief. He was known throughout his life for uncompromising integrity — among the most steadfast voices of righteous remonstrance in the Donglin faction. CBDB records 316 social associations, placing him at the core of the Donglin network.",
  ["邹尔瞻","Zou Erzhan","南皋"],["src-mingshi"],"",0.85)

p("li-weizhen", "李维桢", "Li Weizhen", 1547, 1626, "ming-dynasty",
  ["文学家","史学家","明朝"], ["Writer","Historian","Ming Dynasty"],
  "明末文坛领袖，主持文坛数十年，其文名与王世贞并称——CBDB记录375条社交关系。",
  "Late Ming literary leader who dominated letters for decades; his literary fame rivaled Wang Shizhen's — CBDB records 375 social associations.",
  "李维桢是晚明最长寿和最多产的文人之一——他活了80岁著述等身。他接续王世贞成为文坛的又一位盟主——为人撰写碑传墓志数以百计——几乎成了晚明社会的「官方写手」。CBDB记录了他375条社交关系——这个数字在晚明仅次于袁宏道和王世贞。他的文风典雅平和——不像前后七子那样激进地复古——而更接近台阁体的端庄稳重。",
  "Li Weizhen was among late Ming's longest-lived and most prolific literati — reaching 80 with a corpus to match. He succeeded Wang Shizhen as the literary world's arbiter, composing hundreds of stele biographies and epitaphs — effectively the 'official writer' of late Ming society. CBDB records 375 social associations, third only to Yuan Hongdao and Wang Shizhen in the late Ming. His literary style was elegantly moderate — neither as radically archaist as the Earlier and Later Seven Masters, closer to the dignified restraint of the Cabinet Style.",
  ["李本宁","Li Benning"],["src-mingshi"],"",0.8)

p("lv-nan", "吕柟", "Lü Nan", 1479, 1542, "ming-dynasty",
  ["哲学家","教育家","明朝","理学"], ["Philosopher","Educator","Ming Dynasty"],
  "明代理学教育家，主讲南京国子监和各地书院——CBDB记录346条社交关系，门生遍布天下。",
  "Ming Neo-Confucian educator who lectured at the Nanjing Imperial Academy and academies nationwide; CBDB records 346 associations with disciples across the realm.",
  "吕柟是明代中期最重要的理学教育家之一。他师从薛敬之——属于程朱理学的正统传承——在王阳明心学风靡天下的时代始终坚持格物穷理的传统路径。他担任南京国子监祭酒期间推动了教育改革。他的讲学吸引了大量学生——CBDB记录346条社交关系——其中绝大多数是师生关系。他对理学的坚守和传播使他在心学大潮中保持了朱子学的阵地。",
  "Lü Nan was among the most important Neo-Confucian educators of mid-Ming. He had studied under Xue Jingzhi, belonging to the orthodox Cheng-Zhu transmission, and steadfastly maintained the traditional path of 'investigating things to exhaust principle' even as Wang Yangming's School of Mind swept the realm. As Chancellor of the Nanjing Imperial Academy, he promoted educational reform. His lectures attracted vast numbers of students — CBDB records 346 social associations, overwhelmingly teacher-student relationships. His faithful transmission of the Cheng-Zhu tradition preserved Zhu Xi's teachings as a living school through the tide of Wang Yangming's popularity.",
  ["吕仲木","Lü Zhongmu","泾野"],["src-mingshi"],"",0.8)

p("wang-daokun", "汪道昆", "Wang Daokun", 1525, 1593, "ming-dynasty",
  ["文学家","军事家","明朝"], ["Writer","Military Commander","Ming Dynasty"],
  "明后期文坛重镇，与王世贞并称「两司马」——因同官兵部侍郎而以「司马」相称。",
  "Late Ming literary heavyweight, paired with Wang Shizhen as the 'Two Simas' — both having served as Vice Minister of War, they called each other by this ancient title.",
  "汪道昆是明代少有的文武双全型人才——他与戚继光一同在福建抗倭前线合作——戚继光负责军事他负责后勤和战略。他的文学与王世贞并称——虽然他的作品传世不多但他的社交网络极为庞大——CBDB记录了261条社交关系。他在新安（徽州）组织了多次大规模的文学聚会——利用徽商的财力推动文化活动——是晚明文人社交的重要组织者。",
  "Wang Daokun was a rare Ming figure combining literary and military talent. He collaborated with Qi Jiguang on the Fujian front against the Japanese pirates — Qi handled military operations, Wang managed logistics and strategy. In literature, he was paired with Wang Shizhen as the 'Two Simas.' Though his surviving works are not voluminous, his social network was enormous — CBDB records 261 associations. He organized large-scale literary gatherings in Xin'an (Huizhou), leveraging the wealth of Huizhou merchants to drive cultural activities — he was a key organizer of late Ming literati sociability.",
  ["汪伯玉","Wang Boyu","太函"],["src-mingshi"],"",0.8)

# ===== OUTPUT =====
for person in people:
    p_id = person["id"]
    name = person["name"]
    name_en = person.get("nameEn", "")
    birth = person.get("birthYear", "undefined") if person.get("birthYear") is not None else "undefined"
    death = person.get("deathYear", "undefined") if person.get("deathYear") is not None else "undefined"
    region = person.get("regionId", "")
    tags_s = ", ".join(f"'{t}'" for t in person["tags"])
    tags_en_s = ", ".join(f"'{t}'" for t in person.get("tagsEn", []))
    occ_s = ", ".join(f"'{o}'" for o in person.get("occupations", []))
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
    occupations: [{occ_s}],
    tags: [{tags_s}],
    tagsEn: [{tags_en_s}],
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
print(f"\n// Total: {len(people)} CBDB network-central figures")
