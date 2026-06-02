#!/usr/bin/env python3
"""CBDB-inspired batch: Song/Tang literati, Neo-Confucians, women, Six Dynasties poets. ~35 figures."""
def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")

people = []

def p(id, name, nameEn, birth, death, region, tags, tagsEn, summary, summaryEn, desc, descEn,
      alt=None, srcs=None, wiki="", conf=0.85, occ=None):
    people.append(dict(id=id, name=name, nameEn=nameEn, birthYear=birth, deathYear=death,
        regionId=region, tags=tags, tagsEn=tagsEn, occupations=occ or ["文学家"],
        summary=summary, summaryEn=summaryEn, description=desc, descriptionEn=descEn,
        alternativeNames=alt or [], sourceIds=srcs or [], wikidataQid=wiki,
        dataStatus="published", confidenceScore=conf, externalReferences=[]))

# ===== Song Literati (10) =====
p("liu-yong", "柳永", "Liu Yong", 984, 1053, "song-dynasty",
  ["文学家", "词人", "宋朝"], ["Writer", "Ci Poet", "Song Dynasty"],
  "北宋第一个专业词人，慢词的开创者，「凡有井水处即能歌柳词」，其词流传之广在古代堪称奇迹。",
  "Northern Song's first professional ci poet and pioneer of the slow-ci form; 'wherever there is a well, they sing Liu's lyrics' — his popularity was unprecedented.",
  "柳永屡试不第后自称「奉旨填词柳三变」——这是对科举制度的最潇洒反抗。他混迹于青楼歌馆之间为歌女写词——这些词被广为传唱。「杨柳岸晓风残月」「衣带渐宽终不悔，为伊消得人憔悴」至今仍是中国人表达离愁别绪最常用的语言。他将词从小令扩展为长调慢词——拓宽了词的表现力——被公认为宋词发展史上从唐五代小令到苏辛豪放词之间的关键桥梁。他去世时据说是歌女们凑钱为他安葬。",
  "After repeatedly failing the imperial examinations, Liu Yong declared himself 'composing lyrics by imperial decree' — the most stylish rebellion against the examination system. He immersed himself in the entertainment quarters writing for singing girls — these lyrics were sung everywhere. 'Willow banks, dawn breeze, waning moon' and 'My robe grows looser, yet I never regret — for her I am wasting away' remain among the most-used Chinese expressions for parting sorrow. He expanded the ci form from short xiaoling to long slow-ci, broadening its expressive range — universally recognized as the critical bridge between Tang-Five-Dynasties xiaoling and the heroic ci of Su Shi and Xin Qiji. Legend says the singing girls pooled their money for his funeral.",
  ["柳三变", "Liu Sanbian", "柳耆卿", "Liu Qiqing", "柳七"], ["src-ss"], "", 0.85)

p("huang-tingjian", "黄庭坚", "Huang Tingjian", 1045, 1105, "song-dynasty",
  ["文学家", "书法家", "宋朝"], ["Writer", "Calligrapher", "Song Dynasty"],
  "苏门四学士之首，江西诗派开创者，其书法与苏轼、米芾、蔡襄并称「宋四家」。",
  "Foremost of Su Shi's four disciples, founder of the Jiangxi Poetry School; his calligraphy with Su Shi, Mi Fu, and Cai Xiang forms the 'Four Masters of Song.'",
  "黄庭坚是苏轼最得意的学生——但他在诗歌上走出了完全不同于苏轼的道路。他提出「点铁成金」「夺胎换骨」的创作理论——主张从前人作品中化出新意——开创了影响深远的江西诗派。他的书法以行书和草书最为出色——《松风阁诗帖》是其代表作，笔画如长枪大戟纵横开张。他一生因新旧党争数度被贬——最后一次死在贬所宜州（今广西）——但他在任何困境中都保持了文人的尊严和创造力。",
  "Huang Tingjian was Su Shi's most accomplished disciple — yet in poetry he forged a path completely different from his master. He proposed the theory of 'turning iron into gold' and 'transforming the embryo' — deriving fresh meaning from earlier works — founding the profoundly influential Jiangxi Poetry School. His running and cursive scripts represent the pinnacle of his calligraphy — 'Poem on the Pine Wind Pavilion' is his masterpiece, with brushstrokes like spears and halberds sweeping across the field. His life was marked by repeated banishment through the factional struggles of the New and Old Policies — he died at his place of exile in Yizhou (modern Guangxi) — yet in every adversity he maintained the dignity and creativity of the literatus.",
  ["黄鲁直", "Huang Luzhi", "山谷道人", "涪翁"], ["src-ss"], "", 0.85)

p("li-yu", "李煜", "Li Yu", 937, 978, "china",
  ["文学家", "词人", "南唐", "君主"], ["Writer", "Ci Poet", "Southern Tang", "Monarch"],
  "南唐后主，亡国之君却是不世出的词人，「问君能有几多愁，恰似一江春水向东流」将个人悲剧升华为永恒的人间感慨。",
  "Last ruler of Southern Tang — a failed monarch but transcendent ci poet whose 'How much sorrow can one bear? Like a river of spring water flowing east' elevated personal tragedy into universal lament.",
  "李煜本名李从嘉，是南唐中主李璟的第六子——一个本该与皇位无缘的文艺青年。命运将他推上王位时南唐已向宋朝称臣。他在位的十五年是不断退让和屈辱的过程——最终在975年宋军攻破金陵时被俘。他在汴京度过了最后的三年——以俘虏身份写下了中国词史上最沉痛的作品。《虞美人》「春花秋月何时了」和《浪淘沙》「帘外雨潺潺」中的每一个字都是血泪凝成。978年宋太宗赐牵机药——他在42岁生日那天痛苦地死去。王国维评价：「词至李后主而眼界始大，感慨遂深。」",
  "Li Yu, originally named Li Congjia, was the sixth son of the Southern Tang ruler Li Jing — a literary youth who should never have become king. Fate thrust the throne upon him when Southern Tang had already become a Song vassal. His fifteen-year reign was a procession of concessions and humiliations — ending when Song troops stormed Jinling in 975. He spent his final three years as a captive in Bianjing — composing the most harrowing lyrics in Chinese ci history. Every word of 'Beautiful Lady Yu' ('When will spring flowers and autumn moon end?') and 'Waves Scouring Sand' ('Outside the curtain, rain patters') is wrung from blood and tears. In 978, Emperor Taizong of Song sent the 'stride-haltering poison' — Li Yu died in agony on his 42nd birthday. Wang Guowei judged: 'Only with the Last Ruler did the ci form attain breadth of vision and depth of feeling.'",
  ["李后主", "南唐后主", "李从嘉", "Li Congjia"], ["src-ss"], "", 0.85)

p("qin-guan", "秦观", "Qin Guan", 1049, 1100, "song-dynasty",
  ["文学家", "词人", "宋朝"], ["Writer", "Ci Poet", "Song Dynasty"],
  "苏门四学士之一，婉约词派的杰出代表，其词情深婉丽「自在飞花轻似梦，无边丝雨细如愁」。",
  "One of Su Shi's four disciples, an outstanding representative of the delicate-and-restrained ci school; his lyrics are exquisitely tender.",
  "秦观是苏轼最钟爱的学生——苏轼听说他去世后在扇子上写下「少游已矣，虽万人何赎」的痛语。他的词以深情婉约著称——将男女之情写得细腻入微又哀婉欲绝。《鹊桥仙》「两情若是久长时，又岂在朝朝暮暮」至今被有情人反复吟诵。《踏莎行》「郴江幸自绕郴山，为谁流下潇湘去」则是他屡遭贬谪命运的写照。他的词风对后来的周邦彦和李清照影响深远。",
  "Qin Guan was Su Shi's most beloved disciple — upon hearing of his death, Su Shi wrote on his fan: 'Shaoyou is gone — even ten thousand men could not redeem him.' His lyrics are celebrated for their profound tenderness, depicting love with exquisite delicacy and heartrending pathos. 'Immortal at Magpie Bridge' — 'If love between two hearts can last forever, why must they be together day and night?' — is endlessly recited by lovers. 'Treading on Grass' — 'The Chen River faithfully winds around Chen Mountain, for whom does it flow down to the Xiao-Xiang?' — reflects his own fate of repeated banishment. His style profoundly influenced the later Zhou Bangyan and Li Qingzhao.",
  ["秦少游", "Qin Shaoyou", "淮海居士"], ["src-ss"], "", 0.85)

p("zhou-bangyan", "周邦彦", "Zhou Bangyan", 1056, 1121, "song-dynasty",
  ["文学家", "词人", "音乐家", "宋朝"], ["Writer", "Ci Poet", "Musician", "Song Dynasty"],
  "北宋末期最杰出的词人和音乐家，被尊为「词中老杜」，其词格律精严对南宋词坛影响深远。",
  "The finest ci poet and musician of late Northern Song, revered as 'the Du Fu of ci'; his metrical precision profoundly shaped Southern Song ci.",
  "周邦彦是北宋词坛的集大成者——他在大晟府担任音乐官员期间将词的音律推到前所未有的精严程度。他擅长以华丽的词藻和精巧的结构铺叙——《兰陵王·柳》是送别词的绝唱——「登临望故国，谁识京华倦客」。他的词「富艳精工」被南宋词人奉为圭臬——姜夔、吴文英、张炎等人都深受其影响。王国维在《人间词话》中给了他最高的评价——将他和杜甫相提并论。",
  "Zhou Bangyan was the great synthesizer of Northern Song ci — during his tenure at the Imperial Music Bureau, he pushed ci metrics to an unprecedented level of refinement. He excelled at ornate diction and intricate structural elaboration — 'Prince of Lanling: The Willow' is the supreme farewell ci — 'Climbing high, I gaze toward my homeland; who recognizes this weary sojourner in the capital?' His lyrics, 'richly ornate and exquisitely crafted,' were canonized by Southern Song ci poets — Jiang Kui, Wu Wenying, Zhang Yan, and others were profoundly influenced. Wang Guowei in 'Poetic Remarks in the Human World' gave him the highest praise, likening him to Du Fu.",
  ["周美成", "Zhou Meicheng", "清真居士"], ["src-ss"], "", 0.85)

p("jiang-kui", "姜夔", "Jiang Kui", 1155, 1221, "song-dynasty",
  ["文学家", "词人", "音乐家", "南宋"], ["Writer", "Ci Poet", "Musician", "Southern Song"],
  "南宋格律词派宗师，终生布衣以卖字为生，其词清空骚雅自成一派，并自创了十七首词调曲谱。",
  "Southern Song master of the regulated ci school who lived as a commoner selling calligraphy; his 'pure and void' style created its own school, and he composed 17 original ci melodies with musical notation.",
  "姜夔可能是中国文学史上最纯粹的艺术家之一——他终生未仕，浪迹江湖，靠朋友接济和卖字为生。但他却是词学史上罕见的打通文学和音乐的大师——他不仅写词还自度曲——《扬州慢》《暗香》《疏影》等自创词牌曲谱至今保存完好，是研究宋代音乐的珍贵资料。他的词风「清空骚雅」——不追求秾丽而追求意境的高远——被张炎在《词源》中推崇备至。他一生漂泊却从未真正潦倒——在范成大、张鉴等名公巨卿的庇护下保持了艺术家的尊严。",
  "Jiang Kui may be one of Chinese literary history's purest artists — never holding office, wandering the rivers and lakes, surviving on patronage and selling calligraphy. Yet he was a rare master who unified literature and music in ci history — he not only wrote lyrics but composed his own melodies. 'Slow Song of Yangzhou,' 'Fragrance in the Dark,' 'Dappled Shadows' — his self-composed ci melodies have been preserved with their original musical notation, providing precious material for Song music research. His style — 'pure and void, elegantly restrained' — pursuing transcendent artistic conception over ornate surface — was praised to the skies by Zhang Yan in 'Origins of Ci.' He drifted through life but never truly fell into destitution — sheltered by patrons like Fan Chengda and Zhang Jian, he maintained the dignity of the artist.",
  ["姜尧章", "Jiang Yaozhang", "白石道人"], ["src-ss"], "", 0.85)

p("yang-wanli", "杨万里", "Yang Wanli", 1127, 1206, "song-dynasty",
  ["文学家", "诗人", "南宋"], ["Writer", "Poet", "Southern Song"],
  "南宋中兴四大诗人之一，独创「诚斋体」，以清新活泼的口语化笔法写自然景物和生活小事。",
  "One of the Four Great Poets of Southern Song's restoration, creator of the 'Chengzhai Style' — fresh, lively, colloquial poems on nature and everyday life.",
  "杨万里与陆游、范成大、尤袤并称「南宋四大家」。他早年学江西诗派但中年觉悟将之前的诗稿全部焚毁——自创「诚斋体」。他的诗有「活法」——「小荷才露尖尖角，早有蜻蜓立上头」「接天莲叶无穷碧，映日荷花别样红」以寻常景物出奇妙的诗意。他写了两万多首诗留存四千余首——在南宋只有陆游在他之上。他还是一位刚正不阿的官员——因反对韩侂胄的权奸被罢官，忧愤而死。",
  "Yang Wanli stands with Lu You, Fan Chengda, and You Mao as one of the Four Great Poets of the Southern Song restoration. In youth he followed the Jiangxi School, but in middle age experienced an awakening — burning all his earlier poems and creating his own 'Chengzhai Style.' His poetry has a 'living method' — 'A tiny lotus bud just shows its pointed tip, already a dragonfly alights upon it' and 'Lotus leaves stretch to the horizon, boundless green; lotus blossoms catch the sun, a special red' — transforming ordinary scenes into miraculous poetry. He wrote over 20,000 poems with 4,000 surviving — second only to Lu You in the Southern Song. He was also an uncompromisingly upright official — dismissed for opposing the powerful minister Han Tuozhou, he died of indignation.",
  ["杨廷秀", "Yang Tingxiu", "诚斋"], ["src-ss"], "", 0.85)

p("fan-chengda", "范成大", "Fan Chengda", 1126, 1193, "song-dynasty",
  ["文学家", "诗人", "外交家", "南宋"], ["Writer", "Poet", "Diplomat", "Southern Song"],
  "南宋四大家之一，出使金国不辱使命，其田园诗《四时田园杂兴》被誉为中国古代田园诗的集大成之作。",
  "One of Southern Song's Four Great Poets who fulfilled his diplomatic mission to the Jin with honor; his 'Four Seasons of Fields and Gardens' is acclaimed as the culmination of Chinese pastoral poetry.",
  "范成大是一位罕见地在外交和文学两个领域都达到顶尖的人物。1170年他出使金国——在几乎确定会被扣留的情况下提出了归还河南陵寝之地和更改受书礼仪的要求——金国君臣震惊于他的胆识。他的《揽辔录》记录了出使途中的见闻。文学上他以田园诗著称——《四时田园杂兴》六十首全面展现了江南农村的劳作和风俗——将陶渊明以来的田园诗从隐士的抒情推向了对农民生活的真实描摹。",
  "Fan Chengda is a rare figure who reached the summit in both diplomacy and literature. In 1170, he was dispatched to the Jin court — and despite near-certainty of detention, demanded the return of the Song imperial tombs in Henan and changes to humiliating reception protocols — the Jin court was stunned by his audacity. His 'Reins Held Tight: A Travel Record' documents his journey. In literature, he is celebrated for pastoral poetry — his sixty 'Four Seasons of Fields and Gardens' comprehensively depicts the labor and customs of Jiangnan rural life, pushing the pastoral tradition from the hermit's lyrical expression to realistic portrayal of peasant existence.",
  ["范致能", "Fan Zhineng", "石湖居士"], ["src-ss"], "", 0.85)

p("yan-shu", "晏殊", "Yan Shu", 991, 1055, "song-dynasty",
  ["文学家", "词人", "政治家", "宋朝"], ["Writer", "Ci Poet", "Statesman", "Song Dynasty"],
  "北宋宰相和词人，一生富贵优游却写出最深的闲愁，「无可奈何花落去，似曾相识燕归来」千古传诵。",
  "Northern Song chancellor and ci poet who lived in wealth and leisure yet wrote the most profound idle melancholy; 'Helpless, the flowers fall; as if familiar, the swallows return' is etched in memory.",
  "晏殊14岁以神童举荐入朝，一生仕途顺遂官至宰相——这在宋代文人中极为罕见。他的词没有苏轼的豪放也没有柳永的俚俗——而是富贵闲雅中的淡淡惆怅。「无可奈何花落去，似曾相识燕归来」「昨夜西风凋碧树，独上高楼，望尽天涯路」——这些词句写的不是具体的事件而是人生的普遍感受。他提拔了范仲淹、欧阳修等一大批人才——被称为「北宋第一伯乐」。他的儿子晏几道也是著名词人——父子并称「二晏」。",
  "Yan Shu was recommended to court as a child prodigy at 14 and rose smoothly to the rank of chancellor — exceptionally rare among Song literati. His ci lack Su Shi's heroic grandeur and Liu Yong's colloquial earthiness — instead capturing a faint melancholy within the elegance of wealth and leisure. 'Helpless, the flowers fall; as if familiar, the swallows return' and 'Last night the west wind withered the green trees; alone I climb the tall tower, gazing to the horizon's end' — these lines address not specific events but the universal condition of human existence. He promoted a galaxy of talent — Fan Zhongyan, Ouyang Xiu, and many others — earning the title 'Northern Song's greatest talent scout.' His son Yan Jidao was also a famous ci poet; together they are called the 'Two Yans.'",
  ["晏同叔", "Yan Tongshu", "晏元献"], ["src-ss"], "", 0.85)

# ===== Tang Poets (8) =====
p("chen-ziang", "陈子昂", "Chen Zi'ang", 659, 700, "tang-dynasty",
  ["文学家", "诗人", "唐朝"], ["Writer", "Poet", "Tang Dynasty"],
  "初唐诗歌革新者，一扫齐梁绮靡诗风，「前不见古人，后不见来者」为盛唐诗歌吹响了号角。",
  "Early Tang poetic reformer who swept away the ornate Southern-Dynasties style; his 'Before me, no ancients; behind me, none to come' sounded the bugle for High Tang poetry.",
  "陈子昂在初唐诗坛仍被齐梁浮靡诗风笼罩时振臂高呼——主张恢复建安风骨——诗歌要有现实内容和慷慨之气。他的《登幽州台歌》「前不见古人，后不见来者。念天地之悠悠，独怆然而涕下」仅二十二个字便写出宇宙之浩渺与个体之孤独——被公认为唐诗从初唐走向盛唐的标志性作品。他后来被武三思陷害死于狱中——年仅42岁——但他的诗歌革命为李白和杜甫开辟了道路。",
  "At a time when early Tang poetry remained trapped in the ornate Southern-Dynasties manner, Chen Zi'ang raised a banner — calling for the restoration of the 'Jian'an vigor' — poetry must have substantive content and impassioned spirit. His 'Song on Climbing Youzhou Terrace' — 'Before me, no ancients; behind me, none to come. Thinking of heaven and earth, boundless and eternal, alone I weep in sorrow' — uses just 22 characters to capture cosmic vastness and individual loneliness, universally recognized as the landmark signaling the transition from Early to High Tang poetry. He was later framed by Wu Sansi and died in prison at 42 — but his poetic revolution had already cleared the path for Li Bai and Du Fu.",
  ["陈伯玉", "Chen Boyu"], ["src-jiutangshu"], "", 0.85)

p("liu-yuxi", "刘禹锡", "Liu Yuxi", 772, 842, "tang-dynasty",
  ["文学家", "诗人", "哲学家", "唐朝"], ["Writer", "Poet", "Philosopher", "Tang Dynasty"],
  "中唐诗豪，被贬二十三年不改其志，「沉舟侧畔千帆过，病树前头万木春」以豁达昂扬的姿态面对逆境。",
  "Mid-Tang 'poetic hero' who endured 23 years of exile without wavering; 'Beside the sunken boat, a thousand sails pass; before the withered tree, ten thousand trees bloom in spring' — facing adversity with magnanimous optimism.",
  "刘禹锡因参与永贞革新被贬——一贬就是二十三年。但他可能是中国古代最乐观的诗人——在贬所他写下了「自古逢秋悲寂寥，我言秋日胜春朝」的宣言。他最著名的《陋室铭》「山不在高有仙则名，水不在深有龙则灵。斯是陋室，惟吾德馨」以极度的自信将贬谪的困窘转化为精神的胜利。「沉舟侧畔千帆过，病树前头万木春」同样表达了一种面对衰败而相信新生的乐观——这与白居易晚年的消沉形成了鲜明对比。他晚年回到洛阳后与白居易唱和——被称为「刘白」。",
  "Liu Yuxi was banished for participating in the Yongzhen Reform — for 23 years. But he may be ancient China's most optimistic poet — from exile, he declared: 'Since ancient times, autumn has been lamented in solitude; I say autumn surpasses the spring morning.' His most famous 'Inscription for My Humble Dwelling' — 'A mountain need not be tall to be famed if immortals dwell there; water need not be deep to be spirit-filled if dragons inhabit it. This is a humble room, but my virtue makes it fragrant' — transforms the humiliation of banishment into spiritual triumph through sheer confidence. 'Beside the sunken boat, a thousand sails pass; before the withered tree, ten thousand trees bloom in spring' similarly expresses an optimism that sees renewal amid decay — in sharp contrast to the late-life despondency of his friend Bai Juyi. Returning to Luoyang in old age, he exchanged poems with Bai Juyi — together they were called 'Liu-Bai.'",
  ["刘梦得", "Liu Mengde", "刘宾客"], ["src-jiutangshu"], "", 0.85)

p("li-he", "李贺", "Li He", 790, 816, "tang-dynasty",
  ["文学家", "诗人", "唐朝"], ["Writer", "Poet", "Tang Dynasty"],
  "中唐「诗鬼」，以瑰丽奇幻的想象著称，「大漠沙如雪，燕山月似钩」年仅27岁便病死。",
  "Mid-Tang 'Ghost of Poetry,' celebrated for his gorgeous, fantastical imagination; died of illness at just 27.",
  "李贺是中国诗歌史上最奇诡的天才。他体弱多病、因父亲名「晋肃」与「进士」谐音被剥夺了参加科举的资格——这个荒诞的理由断送了他的仕途。他将所有的痛苦和奇思异想倾注于诗歌——骑驴出游时命书童背负锦囊——想到好句子便写下来投入囊中。「黑云压城城欲摧」「石破天惊逗秋雨」「大漠沙如雪，燕山月似钩」——他的想象力和语言创造力在唐诗中独树一帜。他去世时年仅27岁——传说天帝新修白玉楼召他去撰写记文——这个传说是对他才华的最高致敬。",
  "Li He is Chinese poetry's most bizarre and brilliant genius. Frail and sickly, he was barred from the imperial examinations because his father's name 'Jinsu' was homophonous with 'jinshi' (the exam degree) — an absurd taboo that destroyed his official career. He poured all his suffering and wild imagination into poetry — riding a donkey on excursions with a servant boy carrying a brocade pouch for jotting down inspired lines. 'Black clouds press the city, the city nearly shatters,' 'Rocks crack, heaven startles, teasing autumn rain,' 'The vast desert sand like snow, the Yan Mountain moon like a hook' — his imagination and linguistic creativity stand uniquely apart in Tang poetry. He died at 27. Legend says the Jade Emperor had just completed a new white-jade palace and summoned him to compose the commemorative inscription — the highest tribute to his genius.",
  ["李长吉", "Li Changji", "诗鬼", "昌谷"], ["src-jiutangshu"], "", 0.85)

p("yu-xuanji", "鱼玄机", "Yu Xuanji", 844, 871, "tang-dynasty",
  ["文学家", "诗人", "女性", "唐朝"], ["Writer", "Poet", "Women", "Tang Dynasty"],
  "唐代最著名的女诗人之一，早年入道观为女冠，以大胆的情诗挑战了传统女性的书写边界。",
  "One of Tang's most famous female poets who became a Daoist priestess in youth and challenged traditional boundaries of women's writing with bold love poems.",
  "鱼玄机原名鱼幼薇，曾为李亿的妾室——被正妻不容后入咸宜观为女道士。她在道观中展开了与多位文人的交往——她的诗歌直白地表达了女性的情欲和孤寂——「易求无价宝，难得有心郎」「自能窥宋玉，何必恨王昌」等诗句大胆突破了闺怨诗的含蓄传统。她因涉嫌打死婢女被处死——年仅27岁——这个案件至今仍有争议。她在短暂的一生中以女性身份发出的声音在千年以来持续回响。",
  "Born Yu Youwei, Yu Xuanji became the concubine of Li Yi — driven out by the principal wife, she entered Xianyi Abbey and became a Daoist priestess. Within the abbey, she engaged with numerous literati — and her poetry openly expressed female desire and loneliness. 'A priceless treasure is easy to find, a devoted heart is hard to come by' and 'Since I can gaze upon Song Yu myself, why resent Wang Chang?' — such lines boldly shattered the restrained tradition of boudoir-plaint poetry. She was executed for allegedly beating a maidservant to death — at just 27 — the case remains disputed today. The voice she raised as a woman in her brief life has echoed through the millennium.",
  ["鱼幼薇", "Yu Youwei", "蕙兰"], ["src-jiutangshu"], "", 0.75)

p("shangguan-waner", "上官婉儿", "Shangguan Wan'er", 664, 710, "tang-dynasty",
  ["政治家", "诗人", "女性", "唐朝"], ["Stateswoman", "Poet", "Women", "Tang Dynasty"],
  "唐代女政治家，被武则天重用掌管诏命，被称为「巾帼宰相」——中国历史上级别最高的女性文官。",
  "Tang stateswoman trusted by Wu Zetian to draft imperial edicts, called the 'Female Chancellor' — the highest-ranking female civil official in Chinese history.",
  "上官婉儿是唐初诗人上官仪的孙女——上官仪因反对武则天被处死时她尚在襁褓中，随母亲被没入掖庭为奴。但她在宫中受到教育展现出惊人的文才——被武则天赏识提拔掌管诏命。她娴熟政务——在武则天晚年和唐中宗时期实际上起着首席秘书甚至宰相的作用——草拟诏命、品评诗文。她的诗歌留存不多但清丽典雅——在初唐诗坛占有一席之地。710年李隆基发动唐隆政变时她与韦后集团一同被杀——政治舞台上的女性命运往往更为残酷。",
  "Shangguan Wan'er was the granddaughter of early Tang poet Shangguan Yi — who was executed for opposing Wu Zetian while Wan'er was still an infant. Consigned with her mother to the palace slave quarters, she received education and displayed astonishing literary talent — Wu Zetian recognized her and elevated her to draft imperial edicts. She became intimately versed in governance — effectively serving as chief secretary and de facto chancellor during Wu Zetian's final years and Emperor Zhongzong's reign — drafting decrees and adjudicating literary competitions. Her surviving poems are few but exquisitely refined — earning her a place in early Tang literary circles. In 710, when Li Longji launched his coup, she was executed alongside Empress Wei's faction — the fates of women on the political stage were often the cruelest.",
  ["上官昭容", "Shangguan Zhaorong"], ["src-jiutangshu"], "", 0.8)

p("xue-tao", "薛涛", "Xue Tao", 768, 832, "tang-dynasty",
  ["文学家", "诗人", "女性", "唐朝"], ["Writer", "Poet", "Women", "Tang Dynasty"],
  "唐代著名女诗人，创制「薛涛笺」，与元稹、白居易等大诗人往来唱和。",
  "Famous Tang female poet who created 'Xue Tao Paper' and exchanged poems with major poets like Yuan Zhen and Bai Juyi.",
  "薛涛是唐代身世最富传奇色彩的女诗人——她幼年随父入蜀，父死后流落为乐籍——但她以文才自立，被剑南西川节度使韦皋赏识聘为「校书郎」——虽然由于性别未获正式任命，但「女校书」之名不胫而走。她与元稹有过一段著名的恋情——元稹离开后她自制深红色小笺写诗寄情——被称为「薛涛笺」——成为后世文人雅士追捧的文具。她晚年隐居成都浣花溪畔——穿女冠服——她的诗至今存留九十余首，是唐代存诗最多的女诗人之一。",
  "Xue Tao's life story is the most romantic among Tang female poets. She accompanied her father to Shu as a child; after his death, she drifted into the entertainment registry — but she asserted her independence through literary talent, catching the eye of Wei Gao, Military Governor of Jiannan-Xichuan, who appointed her 'Editorial Clerk.' Though gender prevented formal appointment, the name 'Female Editor' spread far and wide. She had a famous romance with the poet Yuan Zhen — after he left, she made small sheets of deep-red paper to write poems expressing her feelings — 'Xue Tao Paper' became a coveted stationery item among later literati connoisseurs. In her final years, she lived in reclusion along Chengdu's Flower-Rinsing Creek, wearing Daoist robes. Over ninety of her poems survive — among the most of any Tang female poet.",
  ["薛洪度", "Xue Hongdu", "女校书"], ["src-jiutangshu"], "", 0.8)

# ===== Neo-Confucians (6) =====
p("zhou-dunyi", "周敦颐", "Zhou Dunyi", 1017, 1073, "song-dynasty",
  ["哲学家", "儒家", "宋朝", "理学"], ["Philosopher", "Confucian", "Song Dynasty", "Neo-Confucianism"],
  "宋明理学的开山鼻祖，《爱莲说》「出淤泥而不染」和《太极图说》影响了此后八百年的中国思想。",
  "Founding father of Neo-Confucianism; his 'On Loving the Lotus' ('emerging from mud yet unstained') and 'Explanation of the Diagram of the Supreme Ultimate' shaped eight centuries of Chinese thought.",
  "周敦颐虽然生前官位不高——只做到知县和州通判——但他对中国思想的贡献是开创性的。他的《太极图说》以最精炼的语言构建了一个从无极到太极、阴阳五行到万物化生的宇宙论体系——成为宋明理学的哲学基石。而《爱莲说》「予独爱莲之出淤泥而不染，濯清涟而不妖」则以文学的方式表达了儒家理想人格——在俗世中保持高洁。他的两个学生程颢程颐将他的思想发展为完整的理学体系——但源头在他这里。他被称为「濂溪先生」——濂溪之学开启了此后八百年的中国哲学主流。",
  "Though Zhou Dunyi held only modest official posts — county magistrate and prefectural vice-governor — his contribution to Chinese thought is foundational. His 'Explanation of the Diagram of the Supreme Ultimate' constructed, in the most concentrated language, a cosmological system from the Non-Ultimate through the Supreme Ultimate to yin-yang, the five phases, and the generation of all things — becoming the philosophical cornerstone of Neo-Confucianism. And 'On Loving the Lotus' — 'I love only the lotus, emerging from mud yet unstained, washed by clear ripples yet not seductive' — expressed the Confucian ideal personality through literature: maintaining purity amid the mundane world. His two students, the Cheng brothers, developed his ideas into a complete system — but the source was here. He is called 'Master Lianxi' — Lianxi learning inaugurated the mainstream of Chinese philosophy for the next eight centuries.",
  ["周茂叔", "Zhou Maoshu", "濂溪先生"], ["src-ss"], "", 0.85)

p("cheng-hao", "程颢", "Cheng Hao", 1032, 1085, "song-dynasty",
  ["哲学家", "儒家", "宋朝", "理学"], ["Philosopher", "Confucian", "Song Dynasty", "Neo-Confucianism"],
  "北宋理学家，与弟程颐并称「二程」，提出「天理」概念，其「仁者浑然与物同体」开启心学一脉。",
  "Northern Song Neo-Confucian who, with his brother Cheng Yi as the 'Two Chengs,' proposed the concept of 'Heavenly Principle'; his 'the humane person is one body with all things' opened the School of Mind.",
  "程颢与其弟程颐共同师从周敦颐——但两兄弟的哲学气质截然不同。程颢温和圆融——「如坐春风」的典故即源于听他的讲学。他提出「天者理也」——将宇宙法则化为道德原理——「仁者浑然与物同体」的境界打通了自我与天地万物的隔阂。他的学说经过谢良佐等人的传播为后来的陆九渊和王阳明的心学奠定了基础。程颢去世后他的弟弟程颐继续发展了理学——但「二程」之学从来是两股不同的哲学潮流。",
  "Cheng Hao and his younger brother Cheng Yi both studied under Zhou Dunyi — but their philosophical temperaments were starkly different. Cheng Hao was gentle and harmonious — the idiom 'as if bathed in spring breeze' originated from descriptions of attending his lectures. He proposed 'Heaven is Principle' — transmuting cosmic law into moral principle — and the realm where 'the humane person is one body with all things' dissolved the barrier between self and the cosmos. His teachings, transmitted through Xie Liangzuo and others, laid the foundation for the later School of Mind of Lu Jiuyuan and Wang Yangming. After his death, his brother Cheng Yi further developed Neo-Confucianism — but the 'Two Chengs' teachings were always two distinct philosophical currents.",
  ["程伯淳", "Cheng Bochun", "明道先生"], ["src-ss"], "", 0.85)

p("cheng-yi", "程颐", "Cheng Yi", 1033, 1107, "song-dynasty",
  ["哲学家", "儒家", "宋朝", "理学"], ["Philosopher", "Confucian", "Song Dynasty", "Neo-Confucianism"],
  "北宋理学家，与兄程颢并称「二程」，其「存天理灭人欲」和「饿死事小失节事大」对中国社会产生了深远影响。",
  "Northern Song Neo-Confucian, with his brother Cheng Hao as the 'Two Chengs'; his 'preserve Heavenly Principle, extinguish human desire' profoundly shaped Chinese society.",
  "程颐与他哥哥程颢性格截然相反——他严肃刚正不苟言笑。一次皇帝在春天折了一枝柳条——他当面批评「方春发生，不可无故摧折」——这种不近人情的严格贯穿了他的一生。他的哲学体系以「理」为核心——认为宇宙万物背后都有其理——人的使命是通过格物穷理来认识天理并以此规范自身。他的名言「饿死事极小，失节事极大」在历史上被用于压迫女性——虽然他原本指的是士大夫的政治气节。他的思想由朱熹集大成——成为此后中国正统的官方哲学。",
  "Cheng Yi's personality was the polar opposite of his brother's — he was stern, upright, and humorless. Once the young emperor broke off a willow branch in spring — Cheng Yi rebuked him to his face: 'In spring, when all things are growing, one must not causelessly break them' — this unbending rigor defined his entire life. His philosophical system centered on 'Principle' (li) — believing that behind all phenomena lies an underlying principle, and humanity's mission is to comprehend this Heavenly Principle through the investigation of things and regulate oneself accordingly. His famous maxim 'starving to death is a very small matter, but losing one's integrity is extremely grave' was historically weaponized to oppress women — though he originally meant the political integrity of scholar-officials. His thought was synthesized by Zhu Xi into the orthodox philosophy that dominated China thereafter.",
  ["程正叔", "Cheng Zhengshu", "伊川先生"], ["src-ss"], "", 0.85)

p("zhang-zai", "张载", "Zhang Zai", 1020, 1077, "song-dynasty",
  ["哲学家", "儒家", "宋朝", "理学"], ["Philosopher", "Confucian", "Song Dynasty", "Neo-Confucianism"],
  "北宋理学家，「为天地立心，为生民立命，为往圣继绝学，为万世开太平」的「横渠四句」至今激励着中国知识分子。",
  "Northern Song Neo-Confucian whose 'Four Sentences of Hengqu' — 'establish heart for heaven and earth, secure destiny for the people, continue the interrupted learning of past sages, open peace for ten thousand generations' — still inspires Chinese intellectuals.",
  "张载年轻时曾热衷于兵学——21岁上书范仲淹请求组建民兵收复失地。范仲淹看出他的潜质对他说「儒者自有名教可乐，何事于兵」——并赠他一本《中庸》。张载从此转向哲学。他出身关中——他的学派被称为「关学」——与二程的「洛学」并立。他的四句教言「为天地立心，为生民立命，为往圣继绝学，为万世开太平」以最短的文字概括了中国知识分子最大的理想——被当代哲学家冯友兰称为「横渠四句」。",
  "In youth, Zhang Zai was passionate about military affairs — at 21, he petitioned Fan Zhongyan to form a militia and recover lost territory. Fan Zhongyan perceived his deeper potential and told him: 'The Confucian way itself offers its own delights — why pursue the military?' — gifting him a copy of 'The Doctrine of the Mean.' Zhang Zai turned to philosophy. From his base in the Guanzhong region, his school became known as 'Guan Learning' — standing alongside the Cheng brothers' 'Luo Learning.' His four-sentence teaching — 'Establish heart for heaven and earth, secure destiny for the people, continue the interrupted learning of past sages, open peace for ten thousand generations' — encapsulates the ultimate ideal of the Chinese intellectual in the briefest possible form, acclaimed by philosopher Feng Youlan as the 'Four Sentences of Hengqu.'",
  ["张子厚", "Zhang Zihou", "横渠先生"], ["src-ss"], "", 0.85)

p("lu-jiuyuan", "陆九渊", "Lu Jiuyuan", 1139, 1193, "song-dynasty",
  ["哲学家", "儒家", "宋朝", "心学"], ["Philosopher", "Confucian", "Song Dynasty", "School of Mind"],
  "南宋心学开创者，提出「宇宙便是吾心，吾心即是宇宙」，1175年与朱熹鹅湖之辩成为中国哲学史上最著名的辩论。",
  "Southern Song founder of the School of Mind who declared 'the universe is my mind, my mind is the universe'; his 1175 Goose Lake debate with Zhu Xi is Chinese philosophy's most famous disputation.",
  "陆九渊四五岁时就问父亲「天地何所穷际」——父亲笑而不答——他为此深思到废寝忘食。他成年后发展出一套与朱熹截然不同的哲学——朱熹主张「格物穷理」向外探求，陆九渊主张「发明本心」向内自省。1175年吕祖谦安排两人在鹅湖寺会面辩论——这就是中国哲学史上最著名的「鹅湖之会」。两人辩论三日最终谁也无法说服谁——但这场辩论将中国哲学分为「理学」和「心学」两大流派。他的思想经过王阳明的发扬成为明清时期最有影响力的哲学思潮之一。",
  "At age four or five, Lu Jiuyuan asked his father 'Where does heaven and earth end?' — his father smiled without answering — the boy pondered this so deeply he forgot to eat and sleep. As an adult, he developed a philosophy radically different from Zhu Xi's — while Zhu Xi advocated 'investigating things to exhaust principle' through outward inquiry, Lu Jiuyuan advocated 'illuminating the original mind' through inward reflection. In 1175, Lü Zuqian arranged for the two to meet and debate at Goose Lake Monastery — Chinese philosophy's most famous 'Goose Lake Debate.' After three days of argument, neither could convince the other — but this debate bifurcated Chinese philosophy into the 'School of Principle' and 'School of Mind.' His thought, expanded by Wang Yangming, became one of the most influential philosophical currents of the Ming-Qing period.",
  ["陆子静", "Lu Zijing", "象山先生"], ["src-ss"], "", 0.85)

p("shao-yong", "邵雍", "Shao Yong", 1011, 1077, "song-dynasty",
  ["哲学家", "数学家", "宋朝", "理学"], ["Philosopher", "Mathematician", "Song Dynasty", "Neo-Confucianism"],
  "北宋理学家和象数易学大师，以数学方法构建了一套宏大的宇宙历史哲学体系，是宋代最有原创性的思想家之一。",
  "Northern Song Neo-Confucian and master of image-number Yijing studies who constructed a grand cosmohistorical philosophical system through mathematical methods.",
  "邵雍可能是宋代最独特的哲学家——他拒绝出仕，在洛阳过着清贫的自耕自读生活——但他的小园子却是当时最重要的学术沙龙。他创造了一套以《易经》六十四卦为基础的宇宙历史周期论——将中国从尧到宋的历史按「元会运世」的时间单位进行数学推演——这套体系虽然今天看来神秘色彩浓重但其内在的逻辑严密性和数学素养令二程和朱熹都不得不敬重。他的《皇极经世书》是宋代理学中最具原创性的著作之一。程颢评价他：「尧夫之学，内圣外王之学也。」",
  "Shao Yong was arguably Song's most unique philosopher — he refused office and lived a life of austere self-sufficiency in his Luoyang garden — yet that garden was the era's most important intellectual salon. He created a cosmological-historical cycle theory based on the Yijing's 64 hexagrams, mathematically charting Chinese history from Yao to Song through units of 'epoch, cycle, era, generation.' Though today this system appears heavily mystical, its internal logical rigor and mathematical sophistication commanded the respect of even the Cheng brothers and Zhu Xi. His 'Supreme Principles Governing the World' is one of the most original works in Song Neo-Confucianism. Cheng Hao assessed: 'Yaofu's learning is the learning of inner sagehood and outer kingship.'",
  ["邵康节", "Shao Kangjie", "尧夫", "安乐先生"], ["src-ss"], "", 0.8)

# ===== Other Important (6) =====
p("xie-lingyun", "谢灵运", "Xie Lingyun", 385, 433, "china",
  ["文学家", "诗人", "南北朝"], ["Writer", "Poet", "Southern Dynasties"],
  "中国山水诗的开创者，出身顶级门阀陈郡谢氏，其「池塘生春草」开创了以自然抒写心灵的传统。",
  "Founder of Chinese landscape poetry from the top-tier Xie clan of Chen Commandery; his 'spring grass grows by the pond' inaugurated the tradition of expressing the soul through nature.",
  "谢灵运是中国历史上最傲慢的诗人之一——他公开宣称「天下才共一石，曹子建独占八斗，我得一斗，天下共分一斗」。他出身东晋最显赫的谢氏家族——谢安、谢玄的后人——但政治上的失意使他将激情倾注于山水之间。他穿着特制的登山木屐（谢公屐）漫游于会稽的山水之间——用精雕细琢的语言描绘自然景色开创了中国山水诗派。《登池上楼》「池塘生春草，园柳变鸣禽」以最简单的意象传达了季节转换的微妙感受。他最终因卷入政治谋反被处死——年仅49岁。",
  "Xie Lingyun was one of Chinese history's most arrogant poets — he publicly declared: 'Of all the world's talent, one dan (ten dou), Cao Zijian alone commands eight dou, I get one dou, and the rest of the world shares the remaining one.' He descended from the Eastern Jin's most illustrious Xie clan — grandson of Xie Xuan — but political frustration channeled his passion into mountains and rivers. Wearing specially designed climbing clogs ('Xie's Clogs'), he roamed the landscapes of Kuaiji, depicting natural scenery in exquisitely sculpted language, founding the Chinese landscape poetry school. 'Climbing the Pool Tower' — 'Spring grass grows by the pond, garden willows change to singing birds' — captures the subtle sensation of seasonal transition through the simplest images. He was eventually executed for involvement in political rebellion — at 49.",
  ["谢康乐", "Xie Kangle", "谢客"], [], "", 0.8)

p("ji-kang", "嵇康", "Ji Kang", 223, 262, "china",
  ["文学家", "音乐家", "哲学家", "魏晋"], ["Writer", "Musician", "Philosopher", "Wei-Jin"],
  "竹林七贤的精神领袖，打铁为生拒不出仕，临刑前弹奏《广陵散》成为中国文人风骨的最高象征。",
  "Spiritual leader of the Seven Sages of the Bamboo Grove who lived as a blacksmith and refused office; playing 'Guangling San' before his execution became the supreme symbol of literati integrity.",
  "嵇康身高七尺八寸「龙章凤姿」是魏晋名士中最有魅力的人物。他在洛阳城外的大树下打铁为生——司马氏的心腹钟会带了大批随从前来拜访——他头也不抬继续打铁——钟会尴尬离去时他冷冷问道：「何所闻而来，何所见而去？」钟会答：「闻所闻而来，见所见而去」——这是中国文化史上最著名的傲岸对话。后来钟会报复进谗——司马昭以不孝的罪名将他处死。刑场上三千太学生请求以他为师——嵇康从容弹完《广陵散》叹道「《广陵散》于今绝矣」——然后从容赴死。",
  "Ji Kang, standing over six feet tall with 'dragon bearing and phoenix elegance,' was the most charismatic of the Wei-Jin celebrity-intellectuals. He lived as a blacksmith under a great tree outside Luoyang. When Zhong Hui — the Sima clan's henchman — came to visit with a large retinue, Ji Kang kept hammering without looking up. As Zhong Hui awkwardly turned to leave, Ji Kang coldly asked: 'What did you hear that made you come? What did you see that makes you leave?' Zhong Hui replied: 'I heard what I heard and came; I see what I see and leave' — these are the most famously proud lines in Chinese cultural history. Later, Zhong Hui's slander led Sima Zhao to execute Ji Kang on charges of unfilial conduct. At the execution ground, three thousand Imperial Academy students petitioned to make him their teacher. Ji Kang calmly played 'Guangling San' to its end, sighed 'Guangling San is now lost forever' — and faced death with perfect composure.",
  ["嵇叔夜", "Ji Shuye", "嵇中散"], [], "", 0.85)

p("ruan-ji", "阮籍", "Ruan Ji", 210, 263, "china",
  ["文学家", "诗人", "哲学家", "魏晋"], ["Writer", "Poet", "Philosopher", "Wei-Jin"],
  "竹林七贤之首，82首《咏怀诗》开创了中国五言咏怀诗的传统，以醉酒和穷途之哭宣泄对黑暗政治的无声抗议。",
  "Foremost of the Seven Sages, whose 82 'Poems of My Heart' founded the pentasyllabic meditation tradition; his drunkenness and 'crying at the road's end' were silent protests against political darkness.",
  "阮籍可能是中国历史上最痛苦的诗人之一——生活在魏晋易代的血腥时代却无法直抒胸臆。他创造了用醉酒逃避政治的生存方式——司马昭想与他联姻——他连醉六十天使对方无从开口。他驾着马车没有目的地前行——「走到路的尽头便痛哭而返」——「穷途之哭」成为中国文化中精神困顿的永恒隐喻。他的八十二首《咏怀诗》以隐晦的象征、深沉的孤独感和对自由的渴望开启了五言诗表现内心世界的新维度。他是嵇康最亲近的朋友但以更曲折的方式应对暴政——活了下来，但付出了巨大的精神代价。",
  "Ruan Ji was perhaps Chinese history's most tormented poet — living through the bloody Wei-Jin transition yet unable to express himself directly. He created drunkenness as a survival strategy against politics — when Sima Zhao sought a marriage alliance, Ruan Ji stayed drunk for sixty consecutive days, making the proposal impossible to convey. He drove his carriage aimlessly — 'when the road ended, he would weep and turn back' — 'crying at the road's end' became Chinese culture's eternal metaphor for spiritual impasse. His 82 'Poems of My Heart,' with their oblique symbolism, profound loneliness, and yearning for freedom, opened new dimensions for pentasyllabic verse in expressing interiority. He was Ji Kang's closest friend but navigated tyranny through more circuitous means — he survived, at enormous spiritual cost.",
  ["阮嗣宗", "Ruan Sizong", "阮步兵"], [], "", 0.85)

p("gong-zizhen", "龚自珍", "Gong Zizhen", 1792, 1841, "qing-dynasty",
  ["文学家", "诗人", "思想家", "清朝"], ["Writer", "Poet", "Thinker", "Qing Dynasty"],
  "晚清启蒙思想家，「九州生气恃风雷，万马齐喑究可哀。我劝天公重抖擞，不拘一格降人才」呼唤变革的呐喊。",
  "Late Qing enlightenment thinker whose famous quatrain called for a thunderstorm to break the silence of a stagnant empire and bring forth talent unrestrained.",
  "龚自珍是晚清第一个敏锐感知到时代正在巨变的知识分子。他的外祖父是著名的文字学家段玉裁——早年的学术训练是乾嘉考据学——但他抛弃了考据书斋转向社会批判。「九州生气恃风雷」一诗是在1839年鸦片战争前夕写的——当时绝大多数中国人还浑然不觉——他已在诗文和政论中反复警告社会危机。他被视为从古代走向近代的过渡性人物——梁启超说「晚清思想之解放，自珍确与有功焉」——鲁迅、柳亚子等人都深受其影响。他于1841年暴病身亡——传说是被政敌毒死的——这一年正是鸦片战争爆发的年份。",
  "Gong Zizhen was the first late Qing intellectual to keenly perceive that the era was hurtling toward cataclysm. His maternal grandfather was the famous philologist Duan Yucai — his early scholarly training was in Qian-Jia evidential research — but he abandoned the study for social critique. His famous quatrain was written in 1839, on the eve of the Opium War — when virtually no one else sensed the coming storm — he had already been warning of social crisis in his poetry and political essays for years. He is seen as a transitional figure from the ancient to the modern — Liang Qichao wrote: 'In the liberation of late Qing thought, Zizhen genuinely contributed' — Lu Xun, Liu Yazi, and others were deeply influenced by him. He died suddenly in 1841 — allegedly poisoned by political enemies — the very year the Opium War erupted.",
  ["龚定庵", "Gong Ding'an", "龚璱人"], ["src-qingshigao"], "", 0.85)

p("li-zhi", "李贽", "Li Zhi", 1527, 1602, "ming-dynasty",
  ["思想家", "文学家", "明朝"], ["Thinker", "Writer", "Ming Dynasty"],
  "明代异端思想家，公开批判程朱理学和孔子权威，以剃发和自刎狱中的极端方式践行了精神独立。",
  "Ming heretic thinker who publicly criticized Neo-Confucianism and Confucian authority, practicing radical spiritual independence by tonsuring himself and cutting his throat in prison.",
  "李贽可能是中国帝制时代最激烈的反叛思想家。他50多岁辞官后剃发为僧但照常吃肉喝酒——以极端的方式表达对一切规范的蔑视。他在《焚书》中批判千百年来「以孔子之是非为是非」——呼吁每个人建立自己的判断标准。他在麻城讲学时男女听众混杂——这在当时是惊世骇俗的。1602年他被以「敢倡乱道，惑世诬民」的罪名逮捕——在狱中用剃刀割喉自尽，享年76岁。他的著作在明清两代多次被禁——但每一次禁毁都激起更多人对他的好奇。他的思想在五四时期被重新发现——成为反传统运动的先声。",
  "Li Zhi was arguably the most radical rebel-thinker of imperial China. After resigning from office in his fifties, he shaved his head as a monk while continuing to eat meat and drink wine — expressing contempt for all conventions through extremes. In 'A Book to Be Burned,' he attacked a millennium of 'taking Confucius's yes-and-no for one's own' — calling on each person to establish their own criteria of judgment. When he lectured in Macheng, his audience mixed men and women — scandalous for the era. In 1602, he was arrested on charges of 'daring to promote heterodox doctrines, deluding the age and deceiving the people' — in prison he cut his own throat with a razor, dying at 76. His works were repeatedly banned through the Ming and Qing — but each prohibition only stirred greater curiosity. His thought was rediscovered during the May Fourth era as a precursor to the anti-traditionalist movement.",
  ["李卓吾", "Li Zhuowu", "李宏甫"], ["src-mingshi"], "", 0.8)

p("yuan-mei", "袁枚", "Yuan Mei", 1716, 1797, "qing-dynasty",
  ["文学家", "诗人", "美食家", "清朝"], ["Writer", "Poet", "Gourmet", "Qing Dynasty"],
  "清代性灵派诗人，33岁辞官归隐随园，倡导诗歌抒写性灵，其《随园食单》是中国烹饪史上最重要的文献。",
  "Qing poet of the 'Native Sensibility' school who retired at 33 to Suiyuan Garden, championing poetry of authentic feeling; his 'Suiyuan Cookbook' is Chinese culinary history's most important text.",
  "袁枚可能是中国古代活得最潇洒的文人。他33岁辞官后用积蓄买下了南京一座破败的园林——随园——将其打造成江南最著名的文人雅集之所。他公开招收女弟子——这在当时被道学家视为洪水猛兽。他的诗歌理论「性灵说」——主张诗歌应该抒写个人真实的情感而不是堆砌典故——既反对格调派的复古也反对考据派以学问为诗。但普通中国人最熟悉的可能是他的《随园食单》——他一辈子追求美食并将其理论和实践写成了一本集大成的烹饪著作。",
  "Yuan Mei may be the Chinese literatus who lived most freely. At 33, he resigned from office and used his savings to purchase a dilapidated garden in Nanjing — Suiyuan — transforming it into Jiangnan's most celebrated gathering place for literati. He openly accepted female disciples — which the moralists of his time considered outrageous. His poetic theory of 'Native Sensibility' (Xingling Shuo) held that poetry should express genuine personal feeling rather than piling up allusions — opposing both the archaists of the Formalist school and the textual scholars who turned poetry into scholarship. But what ordinary Chinese know best is his 'Suiyuan Cookbook' — a lifelong pursuit of gastronomy systematized into the most comprehensive culinary text in Chinese history.",
  ["袁子才", "Yuan Zicai", "随园老人", "简斋"], ["src-qingshigao"], "", 0.85)

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
print(f"\n// Total: {len(people)} CBDB-inspired figures")
