#!/usr/bin/env python3
"""Supplement: additional Chinese ministers, literati, scientists. ~22 figures."""
def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")

people = []

def p(id, name, nameEn, birth, death, region, tags, tagsEn, summary, summaryEn, desc, descEn,
      alt=None, srcs=None, wiki="", conf=0.85):
    people.append(dict(id=id, name=name, nameEn=nameEn, birthYear=birth, deathYear=death,
        regionId=region, tags=tags, tagsEn=tagsEn, occupations=["政治家"],
        summary=summary, summaryEn=summaryEn, description=desc, descriptionEn=descEn,
        alternativeNames=alt or [], sourceIds=srcs or [], wikidataQid=wiki,
        dataStatus="published", confidenceScore=conf, externalReferences=[]))

# ===== 名臣补 (4) =====
p("chen-ping", "陈平", "Chen Ping", -245, -178, "han-dynasty",
  ["名臣", "谋士", "汉朝"], ["Minister", "Strategist", "Han Dynasty"],
  "西汉开国谋臣，六出奇计为刘邦平定天下，吕后专政时期韬光养晦保全汉室。",
  "Western Han founding strategist whose six ingenious stratagems helped Liu Bang conquer the realm; preserved the Han during Empress Lü's reign through calculated reticence.",
  "陈平出身贫寒但才华出众——年轻时替乡里分肉公平得到赞誉，他感叹「使平得宰天下，亦如是肉矣！」楚汉相争中他为刘邦出了六条奇计——离间项羽范增、荥阳突围诈降、封韩信为齐王安抚军心等都出自他的手笔。刘邦去世后吕后专权，他表面顺从实则暗中保护刘氏宗室。吕后死后他与周勃联手铲除诸吕、迎立汉文帝——完成了对汉室最重要的一次拯救。",
  "Chen Ping was born poor but prodigiously talented — dividing sacrificial meat fairly as a youth, he remarked: 'If I could govern the realm, it would be like carving this meat!' During the Chu-Han contention, he devised six brilliant stratagems for Liu Bang — driving a wedge between Xiang Yu and Fan Zeng, breaking the Xingyang siege with a false surrender, calming Han Xin by recommending his enfeoffment. After Liu Bang's death, under Empress Lü's dominance, he feigned compliance while secretly protecting the Liu clan. When she died, he joined Zhou Bo in eliminating the Lü clan and enthroning Emperor Wen — the most critical rescue of the Han dynasty.",
  [], ["src-shiji", "src-hanshu"], "", 0.85)

p("du-ruhui", "杜如晦", "Du Ruhui", 585, 630, "tang-dynasty",
  ["名臣", "政治家", "唐朝"], ["Minister", "Statesman", "Tang Dynasty"],
  "唐初名相，「房谋杜断」之杜断，以善断著称，辅佐李世民开创贞观之治，英年早逝。",
  "Early Tang chancellor famed as the 'decider' half of 'Fang plans, Du decides'; helped Li Shimin establish the Zhenguan era before his premature death.",
  "杜如晦与房玄龄是李世民最倚重的左右手——房玄龄善于谋划，杜如晦长于决断，两人配合天衣无缝。玄武门之变前，在李建成建议将房杜外调的关键时刻，杜如晦力劝李世民立刻行动——历史证明这个判断是正确的。他在贞观年间任尚书右仆射，与房玄龄共同执掌朝政。唐太宗评价：「房知杜之能断大事，杜知房之善建嘉谋。」可惜他46岁便去世——太宗痛哭「朕失一臂矣」。",
  "Du Ruhui and Fang Xuanling were Li Shimin's indispensable left and right hands — Fang excelled at planning, Du at deciding, and their synergy was flawless. Before the Xuanwu Gate coup, when Li Jiancheng maneuvered to exile both from court, Du Ruhui urged Li Shimin to act immediately — a judgment history proved correct. During the Zhenguan era, he served as chancellor alongside Fang Xuanling. Emperor Taizong observed: 'Fang knew Du could decide the gravest matters; Du knew Fang could devise the finest plans.' Du died at only 46 — Taizong wept: 'I have lost an arm.'",
  ["杜克明", "Du Keming"], ["src-jiutangshu"], "", 0.85)

p("kou-zhun", "寇准", "Kou Zhun", 961, 1023, "song-dynasty",
  ["名臣", "政治家", "宋朝"], ["Minister", "Statesman", "Song Dynasty"],
  "北宋名相，澶渊之盟的关键推动者，以刚直敢谏著称，与包拯并称宋朝两大直臣。",
  "Northern Song chancellor who engineered the Chanyuan Treaty; famed for uncompromising candor alongside Bao Zheng as Song's two most outspoken ministers.",
  "1004年辽国大举南侵，朝中大臣纷纷主张迁都南逃。寇准力排众议坚持真宗皇帝御驾亲征——当皇帝到来时宋军士气大振。最终两国达成澶渊之盟：宋每年向辽输送岁币，但避免了战争并维持了百余年和平。寇准性格刚烈——曾拉住皇帝的衣襟不让他退朝直到把话说完。但他也因锋芒太露被政敌陷害，最终被贬到雷州（今广东雷州半岛），客死异乡。",
  "When the Liao launched a massive invasion in 1004, courtiers urged abandoning the capital. Kou Zhun overruled them all, insisting Emperor Zhenzong personally lead the defense — troop morale soared when the emperor appeared at the front. The resulting Chanyuan Treaty required annual payments to Liao but averted war and maintained peace for over a century. Kou Zhun's personality was volcanic — he once grabbed the emperor's robe to prevent him from leaving until he finished speaking. But his uncompromising edge made enemies; framed by rivals, he was exiled to Leizhou in the far south, where he died far from home.",
  ["寇平仲", "Kou Pingzhong"], ["src-ss"], "", 0.85)

p("zhao-pu", "赵普", "Zhao Pu", 922, 992, "song-dynasty",
  ["名臣", "政治家", "宋朝"], ["Minister", "Statesman", "Song Dynasty"],
  "北宋开国宰相，辅佐宋太祖赵匡胤制定「先南后北」统一方略，「半部论语治天下」的典故即源于他。",
  "Founding chancellor of Song who helped Zhao Kuangyin formulate the 'south first, north later' unification strategy; associated with the adage 'governing the realm with half the Analects.'",
  "赵普是赵匡胤最信任的谋臣。陈桥兵变、杯酒释兵权等重大决策背后都有他的身影。他提出了「先南后北」的统一方略——先消灭南方各割据政权再对付北方的辽国——这个策略基本上被成功执行。他在家中备有一个大瓦壶，将各地呈报的奏章看过后投入壶中，每隔一段时间集中焚烧——这种早期的保密和文档管理意识在当时非常先进。虽然他读书不多，但据说每遇大事就会从书箱中取出《论语》查阅——后人演绎为「半部论语治天下」。",
  "Zhao Pu was Zhao Kuangyin's most trusted strategist, instrumental in the Chen Bridge Mutiny and the 'dismissal of generals over wine.' He formulated the 'south first, north later' strategy — eliminate the southern kingdoms before confronting the northern Liao — which was largely executed successfully. He kept a large crock at home into which he dropped memorials after reading, periodically burning them — an early form of document security remarkable for the era. Though not widely read, legend says he consulted the Analects from his book chest whenever facing major decisions — embellished into the saying 'governing the realm with half the Analects.'",
  ["赵则平", "Zhao Zeping"], ["src-ss"], "", 0.8)

# ===== 文人补 (8) =====
p("luo-binwang", "骆宾王", "Luo Binwang", 640, 684, "tang-dynasty",
  ["文学家", "诗人", "唐朝", "初唐四杰"], ["Writer", "Poet", "Tang Dynasty"],
  "初唐四杰之一，七岁写出《咏鹅》，后为徐敬业撰写讨伐武则天的檄文，连武则天读后都感叹「宰相安得失此人」。",
  "One of the Four Paragons of Early Tang who wrote 'Ode to the Goose' at age seven; his denunciation of Wu Zetian was so brilliant that even she lamented losing such talent.",
  "骆宾王七岁那年在池塘边随口吟出「鹅鹅鹅，曲项向天歌。白毛浮绿水，红掌拨清波」——这可能是中国文学史上最著名的儿童诗。成年后他参加了徐敬业讨伐武则天的起兵，并撰写了《为徐敬业讨武曌檄》——这篇檄文以排山倒海的排比和典故罗列了武则天的「罪行」。传说武则天读到「一抔之土未干，六尺之孤何托」时震惊不已，责备宰相没有网罗这样的人才。起兵失败后骆宾王下落不明——有说被杀、有说出家为僧。",
  "At age seven, standing by a pond, Luo Binwang spontaneously composed 'Goose, goose, goose, curving neck sings to the sky. White feathers float on green water, red webs paddle the clear ripples' — possibly Chinese literature's most famous children's poem. As an adult, he joined Xu Jingye's rebellion against Wu Zetian and penned the 'Denunciation of Wu Zhao' — a thunderous parallel-prose indictment of her 'crimes.' Legend says Wu Zetian, reading the lines 'The grave-soil not yet dry, whom does the orphaned child depend on?', was stunned and berated her chancellor for failing to recruit such talent. After the rebellion's defeat, Luo disappeared — some say killed, others say he became a Buddhist monk.",
  ["骆观光", "Luo Guanguang"], ["src-jiutangshu"], "", 0.8)

p("wang-zhihuan", "王之涣", "Wang Zhihuan", 688, 742, "tang-dynasty",
  ["文学家", "诗人", "唐朝"], ["Writer", "Poet", "Tang Dynasty"],
  "盛唐边塞诗人，「欲穷千里目，更上一层楼」流传千年，其诗传世仅六首却首首经典。",
  "High Tang frontier poet whose 'to see a thousand li further, climb one more story' has echoed for a millennium; only six of his poems survive, yet each is a classic.",
  "王之涣存世仅有六首诗——但这六首诗中的两首（《登鹳雀楼》和《凉州词》）成为了中国诗歌中最家喻户晓的篇目。「白日依山尽，黄河入海流。欲穷千里目，更上一层楼」是每个中国孩子最早接触的唐诗之一——短短二十个字包含了宇宙视野和人生哲理。「羌笛何须怨杨柳，春风不度玉门关」以边塞的荒凉衬托戍卒的乡愁——苍凉中见悲悯。据传他和王昌龄、高适在旗亭赌唱的故事——「旗亭画壁」——是唐诗传播史上最风雅的轶事。",
  "Only six of Wang Zhihuan's poems survive — yet two of them ('Climbing Stork Tower' and 'Beyond the Border') rank among the most universally recognized in Chinese poetry. 'The white sun sets behind the mountains; the Yellow River flows to the sea. To see a thousand li further, climb one more story' is among the first Tang poems every Chinese child encounters — twenty characters encompassing cosmic vision and life philosophy. 'Why should the Qiang flute blame the willows? The spring wind never reaches Jade Gate Pass' — frontier desolation framing a soldier's homesickness, desolation shot through with compassion. Legend says he wagered with Wang Changling and Gao Shi at a tavern, with singers performing their verses to determine superiority — the 'Flag Pavilion Wall-Carving' anecdote is Tang poetry's most elegant tale of literary rivalry.",
  [], ["src-jiutangshu"], "", 0.8)

p("yan-zhenqing", "颜真卿", "Yan Zhenqing", 709, 785, "tang-dynasty",
  ["书法家", "名臣", "唐朝"], ["Calligrapher", "Minister", "Tang Dynasty"],
  "唐代最伟大的书法家之一，与柳公权并称「颜筋柳骨」，其楷书雄浑端庄，也是为国捐躯的忠烈之臣。",
  "One of Tang's greatest calligraphers, paired with Liu Gongquan as 'Yan's sinews, Liu's bones'; his regular script is majestic and dignified; he also died a loyal martyr.",
  "颜真卿的书法被后世尊为「颜体」——以雄强圆厚、端庄雄伟的风格与王羲之的秀美飘逸形成双峰并峙。他的《多宝塔碑》《颜勤礼碑》《祭侄文稿》是中国书法的巅峰之作——后者被称为「天下第二行书」。但在政治生涯中他同样可歌可泣：在李希烈叛乱时他受命前去劝降——明知此行必死仍毅然前往——最终被叛军缢杀。他的书法和人格都体现了「字如其人」——雄浑中见风骨。",
  "Yan Zhenqing's calligraphy, revered as 'Yan Style,' stands as a majestic counterpoint to Wang Xizhi's elegance — powerful, round, dignified regular script. His 'Duobao Pagoda Stele,' 'Yan Qinli Stele,' and 'Draft Eulogy for My Nephew' are pinnacles of Chinese calligraphy — the latter acclaimed as the 'second greatest running-script work under heaven.' His political life was equally heroic: when the rebel Li Xilie rose, Yan was dispatched on what everyone knew was a suicide mission to negotiate — he went unflinchingly and was strangled by the rebels. Both his calligraphy and his character embody the Chinese ideal that 'the writing reveals the person' — majesty infused with moral backbone.",
  ["颜清臣", "Yan Qingchen", "颜鲁公"], ["src-jiutangshu"], "", 0.85)

p("zhang-xu", "张旭", "Zhang Xu", 658, 747, "tang-dynasty",
  ["书法家", "诗人", "唐朝"], ["Calligrapher", "Poet", "Tang Dynasty"],
  "唐代「草圣」，以狂草闻名天下，醉酒后挥毫泼墨的狂态成为中国文化中艺术天才的经典形象。",
  "Tang dynasty 'Sage of Cursive Script,' renowned for wild cursive; his drunken, ecstatic brushwork became the archetypal image of artistic genius in Chinese culture.",
  "张旭的狂草达到了书法从实用走向纯粹艺术表达的极致——他的字常常难以辨认，但线条中蕴含的情绪和力量令人震撼。他醉酒后常披头散发、以头发蘸墨挥洒——这种表演性的创作方式使他成为「饮中八仙」之一。杜甫在《饮中八仙歌》中写道：「张旭三杯草圣传，脱帽露顶王公前，挥毫落纸如云烟。」他的草书与李白的诗歌、裴旻的剑舞被唐文宗下诏称为「三绝」。",
  "Zhang Xu's wild cursive pushed calligraphy beyond legibility into pure artistic expression — his characters were often unreadable, but the emotion and power in his lines were overwhelming. When drunk, he would let down his hair, dip it in ink, and fling it across the paper — this performative creativity earned him a place among the 'Eight Immortals of the Wine Cup.' Du Fu wrote: 'Three cups make Zhang Xu the cursive sage — he bares his head before lords and princes, brush falling on paper like clouds and mist.' His cursive, Li Bai's poetry, and Pei Min's sword dance were declared the 'Three Perfections' by imperial decree under Emperor Wenzong.",
  ["张伯高", "Zhang Bogao", "张颠", "草圣"], ["src-jiutangshu"], "", 0.8)

p("shi-naian", "施耐庵", "Shi Nai'an", 1296, 1372, "china",
  ["文学家", "小说家", "元明"], ["Writer", "Novelist", "Yuan-Ming"],
  "元末明初小说家，《水浒传》的作者，塑造了以宋江为首的108位梁山好汉群像。",
  "Late Yuan novelist, author of 'Water Margin' (Outlaws of the Marsh), creating the epic ensemble of 108 Liangshan heroes led by Song Jiang.",
  "施耐庵的生平极少有可靠史料——甚至《水浒传》的作者是否为他也存在学术争议。但这部小说无疑是世界文学史上最伟大的群像作品之一。108位好汉被逼上梁山——每个人都有自己的入伙故事和独特个性——武松打虎、林冲风雪山神庙、鲁智深倒拔垂杨柳这些情节已深入中国人骨髓。小说以「官逼民反」为主题，但其结局——宋江接受招安后兄弟们一个个凋零——也深刻揭示了农民起义的悲剧宿命。《水浒传》被金圣叹评为「第五才子书」。",
  "Reliable biographical records of Shi Nai'an are extremely scarce — even his authorship of 'Water Margin' is debated. Yet this novel is indisputably one of world literature's greatest ensemble works. The 108 heroes, each driven to Liangshan by injustice, each with a distinctive origin story and personality — Wu Song killing the tiger, Lin Chong at the Mountain Spirit Temple in the blizzard, Lu Zhishen uprooting the willow tree — these episodes are woven into the Chinese cultural fabric. The novel's theme is 'oppression drives rebellion,' but its ending — Song Jiang accepting amnesty as his sworn brothers fall one by one — lays bare the tragic destiny of peasant uprisings. Jin Shengtan ranked it the 'Fifth Work of Genius.'",
  ["施彦端", "Shi Yanduan"], [], "", 0.7)

p("ma-zhiyuan", "马致远", "Ma Zhiyuan", 1250, 1321, "china",
  ["文学家", "戏剧家", "散曲家", "元朝"], ["Writer", "Playwright", "Yuan Dynasty"],
  "元曲四大家之一，《汉宫秋》和《天净沙·秋思》的作者，「枯藤老树昏鸦」千古传唱。",
  "One of the Four Masters of Yuan Drama, author of 'Autumn in the Han Palace' and 'Autumn Thoughts' with its immortal 'withered vines, old trees, crows at dusk.'",
  "马致远在元曲中的地位有些类似于唐诗中的王维——作品不多但件件精品。《天净沙·秋思》「枯藤老树昏鸦，小桥流水人家，古道西风瘦马。夕阳西下，断肠人在天涯」仅28个字便构造出一个完整的悲秋意境——被后人称为「秋思之祖」。他的杂剧《汉宫秋》改写王昭君故事——在元朝异族统治的背景下赋予了这个历史故事新的民族悲情。他年轻时热衷功名但仕途坎坷，晚年自号「东篱」——致敬陶渊明。",
  "Ma Zhiyuan occupies a position in Yuan drama somewhat akin to Wang Wei in Tang poetry — limited output but every piece a gem. His 'Autumn Thoughts' — 'Withered vines, old trees, crows at dusk; a little bridge, flowing water, a cottage; an ancient road, west wind, a gaunt horse. The sun sets in the west; a heartbroken man at the edge of the world' — uses just 28 characters to construct a complete autumnal landscape of melancholy, acclaimed as the 'ancestor of autumn meditations.' His zaju play 'Autumn in the Han Palace' reworks the Wang Zhaojun story, infusing it with the new ethnic pathos of Mongol-dominated Yuan. He pursued official advancement in youth but his career foundered; in old age he adopted the penname 'Eastern Hedge' — a salute to Tao Yuanming.",
  ["马千里", "Ma Qianli", "东篱"], [], "", 0.8)

p("pu-songling", "蒲松龄", "Pu Songling", 1640, 1715, "qing-dynasty",
  ["文学家", "小说家", "清朝"], ["Writer", "Novelist", "Qing Dynasty"],
  "清代小说家，《聊斋志异》的作者，以狐鬼花妖的故事构筑了中国文学中最奇丽的幻想世界。",
  "Qing novelist, author of 'Strange Tales from a Chinese Studio' (Liaozhai Zhiyi), constructing Chinese literature's most wondrous fantasy world of fox-spirits and flower-fairies.",
  "蒲松龄一生科场失意——从19岁参加科举直到71岁才获得岁贡生。他在淄川老家设帐教书，同时在路边摆茶摊收集民间奇闻异事。这些故事最终汇聚成《聊斋志异》——近500篇文言短篇小说。表面上写的是狐仙鬼怪，实际上充满了对人性的深刻洞察和对科举制度、社会不公的辛辣讽刺。《画皮》《聂小倩》《促织》等篇章至今被不断改编为影视作品。鲁迅评价其「用传奇法而以志怪」——在志怪的外壳下是人间的悲欢。",
  "Pu Songling's examination career was a lifelong failure — he began at 19 and did not attain even the lowest degree until 71. He taught at a private school in his hometown of Zichuan while collecting strange tales from passersby at a roadside tea stand. These stories coalesced into 'Strange Tales from a Chinese Studio' — nearly 500 classical-language short stories. On the surface, foxes and ghosts; beneath the surface, profound insights into human nature and biting satire of the examination system and social injustice. 'The Painted Skin,' 'Nie Xiaoqian,' 'The Cricket' continue to be adapted endlessly for film and television. Lu Xun praised the work as 'recording the strange in the manner of classical tales' — beneath the supernatural shell lies all the joy and sorrow of the human world.",
  ["蒲留仙", "Pu Liuxian", "柳泉居士"], ["src-qingshigao"], "", 0.85)

p("zheng-banqiao", "郑板桥", "Zheng Banqiao", 1693, 1766, "qing-dynasty",
  ["画家", "书法家", "文学家", "清朝"], ["Painter", "Calligrapher", "Writer", "Qing Dynasty"],
  "清代「扬州八怪」之首，以画竹和「难得糊涂」的人生哲学闻名，独创六分半书。",
  "Leading figure of the Qing's 'Eight Eccentrics of Yangzhou,' famous for bamboo paintings, his 'rarely feign ignorance' philosophy, and his unique 'six-and-a-half' calligraphy style.",
  "郑板桥的一生是文人做官的典型案例——他在山东范县和潍县做了十二年知县，清廉爱民，但因为开仓赈济灾民触怒上司被罢官。于是他回到扬州卖画为生——并公然贴出润格（价目表）：「大幅六两，中幅四两，小幅二两」——这在当时被视为惊世骇俗的商人行为。「难得糊涂」四个字是他最著名的人生格言——题跋解释「聪明难，糊涂尤难，由聪明而转入糊涂更难」——体现了一种在浊世中主动选择「糊涂」的生存智慧。他的竹石图以寥寥数笔传达出坚韧不屈的精神。",
  "Zheng Banqiao's life is a classic case study of the scholar-official. He served twelve years as magistrate of Fanxian and Weixian in Shandong — honest, beloved by the people — but was dismissed for opening granaries to feed famine victims without authorization. Returning to Yangzhou, he sold paintings for a living — and publicly posted a price list: 'Large scrolls six taels, medium four, small two' — scandalous merchant behavior for a literatus. His motto 'Rarely feign ignorance' — with his annotation: 'To be clever is hard, to play the fool is harder, to transition from cleverness to playing the fool is hardest of all' — embodies a survival philosophy of willed 'foolishness' in a corrupt world. His bamboo-and-rock paintings convey indomitable spirit with the fewest possible strokes.",
  ["郑燮", "Zheng Xie", "板桥道人"], [], "", 0.85)

# ===== 科学家补 (6) =====
p("sun-simiao", "孙思邈", "Sun Simiao", 541, 682, "tang-dynasty",
  ["医学家", "科学家", "唐朝"], ["Physician", "Scientist", "Tang Dynasty"],
  "唐代「药王」，著有《千金要方》和《千金翼方》，系统总结了唐以前的医学成就，活到141岁。",
  "Tang 'King of Medicine,' author of 'Essential Formulas Worth a Thousand Gold' and its supplement; systematically compiled pre-Tang medical knowledge and reportedly lived to 141.",
  "孙思邈可能是中国历史上最长寿的名医——据说他活了141岁。他拒绝隋唐两代皇帝的征召，终身在民间行医采药。他以「人命至重，有贵千金」的理念命名自己的著作为《千金要方》和《千金翼方》——这两部书合计60卷，涵盖了内科、外科、妇科、儿科、针灸、养生等几乎所有医学分支，收集了五千多个药方。他提出的医德规范——《大医精诚》——至今仍是中国医生的入行必读。他提倡食疗先于药疗、注重预防和养生的理念在现代看来极具前瞻性。",
  "Sun Simiao may be Chinese history's longest-lived famous physician — reportedly reaching 141. He refused summons from both Sui and Tang emperors, choosing to practice medicine and collect herbs among the common people his entire life. Believing 'human life is supremely precious, worth a thousand pieces of gold,' he named his works 'Essential Formulas Worth a Thousand Gold' and its supplement — 60 volumes covering internal medicine, surgery, gynecology, pediatrics, acupuncture, and health cultivation, collecting over 5,000 prescriptions. His code of medical ethics — 'On the Absolute Sincerity of Great Physicians' — remains required reading for Chinese doctors today. His advocacy of dietary therapy before medication and emphasis on prevention now seem remarkably prescient.",
  ["孙真人", "药王"], [], "", 0.8)

p("jia-sixie", "贾思勰", "Jia Sixie", 480, 550, "china",
  ["科学家", "农学家", "南北朝"], ["Scientist", "Agronomist", "Northern Dynasties"],
  "北魏农学家，《齐民要术》的作者——中国现存最早最完整的农学百科全书，系统总结了北方的农业技术。",
  "Northern Wei agronomist, author of 'Qimin Yaoshu' (Essential Techniques for the Common People) — China's earliest complete agricultural encyclopedia.",
  "贾思勰曾任高阳太守，但他最伟大的贡献是《齐民要术》——「齐民」意为平民百姓，「要术」则是关键的技术。这部10卷92篇的巨著涵盖了谷物种植、蔬菜栽培、果树管理、畜牧养殖、食品加工（包括酿酒、制酱、腌菜）以及南方作物的北方引种方法。他收集整理了当时北方农业生产的全部知识——从选种到收割、从灌溉到施肥、从农具制作到家畜防疫。这部书不仅是技术手册，也是了解6世纪中国北方社会经济生活的珍贵文献。",
  "Jia Sixie served as governor of Gaoyang, but his greatest legacy is 'Qimin Yaoshu' — 'Qimin' meaning common people, 'Yaoshu' meaning essential techniques. This 10-volume, 92-section magnum opus covers grain cultivation, vegetable growing, orchard management, animal husbandry, food processing (brewing, sauce-making, pickling), and methods for introducing southern crops to the north. He systematically compiled the totality of then-known northern agricultural knowledge — from seed selection to harvesting, irrigation to fertilization, tool-making to livestock disease prevention. The book is not only a technical manual but also an invaluable window into 6th-century northern Chinese socioeconomic life.",
  [], [], "", 0.8)

p("li-daoyuan", "郦道元", "Li Daoyuan", 472, 527, "china",
  ["科学家", "地理学家", "南北朝"], ["Scientist", "Geographer", "Northern Dynasties"],
  "北魏地理学家，《水经注》的作者——一部集文学与地理学于一体的不朽杰作。",
  "Northern Wei geographer, author of 'Commentary on the Water Classic' — an immortal masterpiece fusing literature and geography.",
  "郦道元以《水经》为纲，将原本仅记载137条水道的简略文献扩展为一部长达40卷、记录1252条河流的巨著——《水经注》。他并非仅在地图上研究河流——他亲自考察了众多水道，详细记录了沿岸的地形、植被、物产、城邑、关隘、名胜和碑刻。他的文字具有极高的文学价值——最著名的是对三峡的描写：「重岩叠嶂，隐天蔽日。自非亭午夜分，不见曦月」——这段文字至今仍在语文课本中传诵。他的死充满悲剧——在出任关右大使的途中被叛军包围，断水而死。",
  "Taking the laconic 'Water Classic' — a text listing only 137 waterways — as his framework, Li Daoyuan expanded it into a 40-volume magnum opus documenting 1,252 rivers. He did not merely study rivers on maps — he personally surveyed countless waterways, meticulously recording topography, vegetation, products, towns, passes, scenic sites, and stone inscriptions along their banks. His prose achieves the highest literary quality — his description of the Three Gorges is the most famous: 'Layer upon layer of cliffs, peak upon peak, hiding the sky and blotting out the sun. Except at midday and midnight, neither sun nor moon can be seen' — still recited in Chinese textbooks today. His death was tragic: dispatched as imperial inspector, he was besieged by rebels and died of thirst.",
  ["郦善长", "Li Shanchang"], [], "", 0.8)

p("yi-xing", "僧一行", "Yi Xing (Monk Yixing)", 683, 727, "tang-dynasty",
  ["科学家", "天文学家", "数学家", "唐朝"], ["Scientist", "Astronomer", "Mathematician", "Tang Dynasty"],
  "唐代天文学家和高僧，实测地球子午线长度——世界上第一次科学测量，编制《大衍历》。",
  "Tang astronomer and Buddhist monk who conducted the world's first scientific measurement of a meridian arc and compiled the 'Dayan Calendar.'",
  "一行俗名张遂，年轻时因不愿与权臣武三思结交而出家为僧。但他并未因此放弃科学——唐玄宗征召他入宫主持历法改革。他在全国设立了12个观测点——最北在铁勒（今蒙古）、最南在林邑（今越南）——通过测量同一时间日影长度的差异计算出了子午线一度的弧长约131.3公里（现代值为111.2公里）——这是人类历史上第一次以科学方法测量地球的大小。他编制的《大衍历》在唐代使用了近百年。他还制造了黄道游仪和水运浑天仪等精密仪器。",
  "Born Zhang Sui, Yi Xing became a monk in his youth to avoid entanglement with the powerful minister Wu Sansi. But monasticism did not end his scientific pursuits — Emperor Xuanzong summoned him to lead calendar reform. He established 12 observation stations across the empire — as far north as the Tiele lands (modern Mongolia) and as far south as Linyi (modern Vietnam) — and by measuring shadow-length differences at the same moment, calculated a meridian arc of roughly 131.3 km per degree (modern value: 111.2 km) — the first scientific measurement of Earth's size in human history. His 'Dayan Calendar' served the Tang for nearly a century. He also built precision instruments including an ecliptic armillary sphere and a water-driven celestial globe.",
  ["张遂", "Zhang Sui", "大慧禅师"], [], "", 0.8)

p("su-song", "苏颂", "Su Song", 1020, 1101, "song-dynasty",
  ["科学家", "天文学家", "政治家", "宋朝"], ["Scientist", "Astronomer", "Statesman", "Song Dynasty"],
  "北宋科学家和政治家，主持制造了水运仪象台——世界上最古老的天文钟，集观测、演示和报时于一体。",
  "Northern Song scientist-statesman who directed the construction of the water-driven astronomical clock tower — the world's oldest known astronomical clock.",
  "苏颂在北宋政坛官至宰相，但他对后世最卓越的贡献是科技方面的。1088年他主持设计建造了水运仪象台——一座高达12米的巨型天文仪器，顶层为浑仪用于观测星象，中层为浑象演示天体运行，底层为报时装置，全部由水力驱动并以擒纵机构控制精确运转。这个擒纵机构是机械钟表的核心技术——比欧洲最早的机械钟早了约两个世纪。他还编写了《新仪象法要》详细记录了设计图纸和制作工艺——这是世界科技史上最珍贵的技术图纸文献之一。",
  "Su Song rose to the rank of chancellor in the Northern Song, but his most enduring contribution was technological. In 1088, he directed the construction of the water-driven astronomical clock tower — a massive 12-meter structure with an armillary sphere atop for observation, a celestial globe in the middle for demonstration, and a time-announcing mechanism below, all water-powered and regulated by an escapement mechanism. This escapement is the core technology of mechanical clocks — predating Europe's earliest mechanical clocks by roughly two centuries. He also compiled the 'New Design for an Armillary Clock,' meticulously documenting the blueprints and construction — among the most precious technical drawings in world history.",
  ["苏子容", "Su Zirong"], ["src-ss"], "", 0.85)

p("ge-hong", "葛洪", "Ge Hong", 283, 363, "china",
  ["科学家", "医学家", "道教", "东晋"], ["Scientist", "Physician", "Daoism", "Eastern Jin"],
  "东晋道教学者和医药学家，《肘后备急方》记载了世界最早的青蒿抗疟和天花症状描述。",
  "Eastern Jin Daoist scholar and pharmacologist whose 'Handbook of Prescriptions for Emergencies' contains the world's earliest records of artemisinin antimalarial use and smallpox description.",
  "葛洪是魏晋时期最博学的人物之一——集道家学者、炼丹家、医学家于一身。《抱朴子》内篇总结了他对金丹和长生术的研究——是早期化学史的重要文献。但他更实际的贡献是《肘后备急方》——一本便携急救手册。这本书中记载了用青蒿汁治疗疟疾的方法——1600多年后屠呦呦正是从中得到启发提取了青蒿素，获得了2015年诺贝尔医学奖。他还首次精确描述了天花的症状和流行特征。",
  "Ge Hong was among the most polymathic figures of the Wei-Jin era — Daoist scholar, alchemist, and physician in one. The 'Inner Chapters' of his 'Baopuzi' (Master Who Embraces Simplicity) summarizes his research into elixir-making and immortality — an important text in early chemistry. But his more practical contribution was the 'Handbook of Prescriptions for Emergencies' — a portable first-aid manual. It records using sweet wormwood (qinghao) juice to treat malaria — over 1,600 years later, Tu Youyou drew inspiration from this very passage to extract artemisinin, earning the 2015 Nobel Prize in Medicine. He also provided the first precise clinical description of smallpox symptoms and epidemiology.",
  ["葛稚川", "Ge Zhichuan", "抱朴子"], [], "", 0.8)

# ===== 谋士/其他补 (3) =====
p("fan-zeng", "范增", "Fan Zeng", -277, -204, "china",
  ["谋士", "战略家", "楚汉"], ["Strategist", "Chu-Han"],
  "项羽的首席谋士，被尊为「亚父」，多次劝项羽杀掉刘邦未果，最终被离间计气走。",
  "Xiang Yu's chief strategist, honored as 'Second Father,' who repeatedly urged killing Liu Bang in vain and was ultimately driven away by Chen Ping's stratagem.",
  "范增年逾七十时投奔项梁和项羽——成为项羽最倚重的谋士，被尊称为「亚父」。鸿门宴上他多次举玉玦示意项羽下令杀死刘邦，项羽犹豫不决。他派项庄舞剑意图在席间刺杀——但项伯以身遮蔽和张良的斡旋使刘邦得以逃脱。范增愤怒地将刘邦赠送的玉斗摔碎：「唉！竖子不足与谋！夺项王天下者必沛公也！」后来陈平用离间计使项羽怀疑范增——范增愤然告老还乡，途中背疽发作而死。他一生的悲剧在于遇到了一个勇冠天下却刚愎自用的主公。",
  "Fan Zeng joined Xiang Liang and Xiang Yu past age seventy, becoming the paramount strategist known as 'Second Father.' At the Hongmen Banquet, he repeatedly raised his jade ring signaling Xiang Yu to order Liu Bang's death — Xiang Yu hesitated. He dispatched Xiang Zhuang to 'perform a sword dance' and assassinate Liu Bang during the performance — but Xiang Bo shielded Liu and Zhang Liang's diplomacy enabled his escape. Enraged, Fan Zeng smashed the jade goblet Liu Bang had gifted: 'Alas! A worthless boy unworthy of counsel! The one who seizes Xiang Yu's realm shall be the Lord of Pei!' Later, Chen Ping's stratagem made Xiang Yu suspect Fan Zeng of disloyalty — the old strategist left in fury, dying of a carbuncle on his back en route home. His lifelong tragedy was serving a lord of peerless valor and fatal obstinacy.",
  ["范亚父", "Ya Fu"], ["src-shiji"], "", 0.8)

p("ji-xiaolan", "纪晓岚", "Ji Xiaolan", 1724, 1805, "qing-dynasty",
  ["文学家", "学者", "名臣", "清朝"], ["Writer", "Scholar", "Minister", "Qing Dynasty"],
  "清代大学士，《四库全书》总纂官，以博学和机智幽默著称，其逸事通过影视作品广为流传。",
  "Qing Grand Secretary and chief editor of the 'Complete Library of the Four Treasuries' (Siku Quanshu); famed for erudition and wit, his anecdotes circulate widely through film and TV.",
  "纪昀（晓岚）是乾隆时期最博学的官员。他一生中最大的成就是总纂《四库全书》——这是中国历史上规模最大的丛书，收录图书3500多种、近8万卷，动用了4000多名抄写员历时十年完成。他还主编了《四库全书总目提要》——中国古典目录学的巅峰之作。在民间传说和影视作品中他被塑造为与和珅斗智斗勇的才子形象——虽然历史中两人关系并非如此简单。他晚年写的《阅微草堂笔记》是继《聊斋志异》之后最重要的文言笔记小说。",
  "Ji Yun (courtesy name Xiaolan) was the most erudite official of the Qianlong era. His life's greatest achievement was serving as chief editor of the 'Siku Quanshu' (Complete Library of the Four Treasuries) — the largest book collection project in Chinese history, encompassing over 3,500 titles in nearly 80,000 volumes, employing over 4,000 scribes over a decade. He also compiled the 'Annotated Catalog of the Siku Quanshu' — the pinnacle of classical Chinese bibliography. In folklore and popular media, he is portrayed as a witty scholar constantly outsmarting the corrupt Heshen — though the historical relationship was more complex. His late-life 'Notes of the Thatched Abode of Close Observations' is the most important classical-language notebook fiction after 'Strange Tales from a Chinese Studio.'",
  ["纪昀", "Ji Yun", "纪文达公", "观弈道人"], ["src-qingshigao"], "", 0.85)

p("liu-yong", "刘墉", "Liu Yong", 1719, 1805, "qing-dynasty",
  ["名臣", "书法家", "清朝"], ["Minister", "Calligrapher", "Qing Dynasty"],
  "清代名臣和书法家，以清廉刚正著称，民间传说中与和珅斗智的「刘罗锅」形象深入人心。",
  "Qing minister and calligrapher famed for integrity; his folk image as 'Hunchback Liu' outwitting the corrupt Heshen is deeply embedded in popular culture.",
  "刘墉是乾隆朝名臣刘统勋之子，自己后来也官至体仁阁大学士。他以清廉著称——任地方官时平反了大量冤案。但他的书法才是真正不朽的——与翁方纲、梁同书、王文治并称「清四家」，其字貌丰骨劲、味厚神藏。与荧幕形象不同，真实的刘墉身材魁梧而非驼背——「刘罗锅」是民间文学的美化。电视剧《宰相刘罗锅》将他和和珅的对抗演绎得淋漓尽致——虽是虚构，却在民间塑造了一个正直智慧的清官典范。",
  "Liu Yong, son of the Qianlong-era grand secretary Liu Tongxun, himself rose to Grand Secretary of the Tiren Pavilion. He was famed for integrity — as a provincial official he righted countless wrongful convictions. But his calligraphy is the truly immortal legacy — together with Weng Fanggang, Liang Tongshu, and Wang Wenzhi, he is counted among the 'Four Masters of the Qing'; his characters are outwardly plump yet inwardly vigorous, richly flavored yet deeply reserved. Contrary to his screen image, the historical Liu Yong was tall and robust, not a hunchback — 'Hunchback Liu' is a folk-literary embellishment. The TV drama 'Hunchback Liu the Chancellor' dramatized his clashes with Heshen — entirely fictional yet for generations shaping the popular image of an upright, quick-witted incorruptible official.",
  ["刘崇如", "Liu Chongru", "石庵"], ["src-qingshigao"], "", 0.85)

# ===== OUTPUT =====
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
print(f"\n// Total: {len(people)} supplementary figures")
