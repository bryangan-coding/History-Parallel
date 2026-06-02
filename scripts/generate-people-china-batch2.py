#!/usr/bin/env python3
"""Chinese Artists, Modern Figures, and Famous Women. ~18 figures."""
def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")

people = []

def p(id, name, nameEn, birth, death, region, tags, tagsEn, summary, summaryEn, desc, descEn,
      alt=None, srcs=None, wiki="", conf=0.85, occ=None):
    people.append(dict(id=id, name=name, nameEn=nameEn, birthYear=birth, deathYear=death,
        regionId=region, tags=tags, tagsEn=tagsEn, occupations=occ or ["艺术家"],
        summary=summary, summaryEn=summaryEn, description=desc, descriptionEn=descEn,
        alternativeNames=alt or [], sourceIds=srcs or [], wikidataQid=wiki,
        dataStatus="published", confidenceScore=conf, externalReferences=[]))

# ===== 艺术家/画家 (6) =====
p("wu-daozi", "吴道子", "Wu Daozi", 685, 758, "tang-dynasty",
  ["画家", "艺术家", "唐朝"], ["Painter", "Artist", "Tang Dynasty"],
  "唐代「画圣」，被民间画工尊为祖师，据说其壁画生动到「天衣飞扬满壁风动」。",
  "Tang 'Sage of Painting,' worshipped as the patron deity of Chinese painters; his murals were said to be so vivid that 'celestial robes flew, the whole wall stirred by wind.'",
  "吴道子是中国绘画史上传说最多的人物——他一生创作了超过三百面壁画的记录本身就近乎神话。据说他在长安兴善寺画佛像时观者如堵——当画到佛像头顶的光环时他不用圆规一笔挥就——被惊叹为神技。唐玄宗命他在大同殿画三百里嘉陵江——他一日而毕，李思训则用了数月，玄宗评价道：「李思训数月之功，吴道子一日之迹，皆极其妙也。」他创造的「吴带当风」人物画风格——衣纹线条如被风吹拂——影响了此后一千年的中国人物画。",
  "Wu Daozi is the most legendary figure in Chinese painting history — the very claim that he created over three hundred murals in his lifetime is almost mythical. When painting Buddhist figures at Xing Shan Temple in Chang'an, legend says crowds packed around — and when he came to the halo, he drew it freehand in one continuous stroke without compass, leaving onlookers in awe. Emperor Xuanzong tasked him with depicting the three-hundred-li Jialing River — he finished in a single day while Li Sixun took months; Xuanzong observed: 'Li Sixun's months of labor and Wu Daozi's single day's work — both are supreme.' He created the 'Wu's Sash Blown by Wind' figure-painting style — drapery lines as though wind-stirred — which influenced Chinese figure painting for the next millennium.",
  ["吴道玄", "Wu Daoxuan", "画圣"], ["src-jiutangshu"], "", 0.8)

p("zhang-zeduan", "张择端", "Zhang Zeduan", 1085, 1145, "song-dynasty",
  ["画家", "艺术家", "宋朝"], ["Painter", "Artist", "Song Dynasty"],
  "北宋画家，《清明上河图》的作者，以百科全书式的精度记录了12世纪开封的城市生活。",
  "Northern Song painter, creator of 'Along the River During the Qingming Festival,' which records 12th-century Kaifeng's urban life with encyclopedic precision.",
  "关于张择端生平我们所知甚少——几乎所有关于他的信息都来自《清明上河图》卷末的一行题跋。但这并不妨碍这幅画成为中国乃至世界艺术史上最著名的作品之一。画卷宽24.8厘米长528.7厘米——描绘了824个人物、60余匹牲畜、28艘船、20辆车——以散点透视的方式从郊外到城内全景式记录了北宋都城的繁华景象。这幅作品不仅是艺术杰作，更是研究宋代城市经济、建筑、服饰、交通和日常生活的无可替代的视觉文献。",
  "We know almost nothing of Zhang Zeduan's life — virtually all information about him comes from a single line of colophon at the end of his scroll. Yet this does nothing to diminish the painting's status as one of the most famous works in Chinese and world art history. The scroll, 24.8 cm wide and 528.7 cm long, depicts 824 human figures, over 60 animals, 28 boats, and 20 vehicles — a panoramic record of the Northern Song capital's prosperity, moving from countryside to city center through shifting perspective. The work is not only an artistic masterpiece but also an irreplaceable visual document for studying Song dynasty urban economy, architecture, fashion, transport, and daily life.",
  ["张正道", "Zhang Zhengdao"], ["src-ss"], "", 0.8)

p("zhao-mengfu", "赵孟頫", "Zhao Mengfu", 1254, 1322, "china",
  ["画家", "书法家", "元朝"], ["Painter", "Calligrapher", "Yuan Dynasty"],
  "元代书画大家，赵宋宗室后裔，提倡复古以开创新风，其书画理论和实践影响了此后六百年。",
  "Yuan dynasty painter-calligrapher of Song imperial descent who advocated archaism as innovation; his theory and practice shaped the next six centuries.",
  "赵孟頫的身份本身就充满张力——他是宋太祖赵匡胤的第十一世孙，却在元朝做了高官。传统文人因此对他颇有微词，但他的艺术成就无人能够否认。他提出了「书画同源」的理论——以书法笔法入画——这一思想深刻影响了此后中国文人画的方向。他的书法被后世称为「赵体」——与欧阳询、颜真卿、柳公权并称楷书四大家。他的妻子管道升也是出色的画家和书法家。在绘画上他擅长山水、人物、鞍马——《鹊华秋色图》是他最著名的作品。",
  "Zhao Mengfu's identity was itself charged with tension — he was the eleventh-generation descendant of Song founder Zhao Kuangyin, yet served as a high official under the Mongol Yuan. Traditional literati faulted him for this, but his artistic achievement is undeniable. He proposed the theory that 'calligraphy and painting share the same source' — infusing painting with calligraphic brushwork — a concept that profoundly shaped the direction of Chinese literati painting thereafter. His calligraphy, known as 'Zhao Style,' is ranked alongside Ouyang Xun, Yan Zhenqing, and Liu Gongquan as one of the Four Masters of Regular Script. His wife Guan Daosheng was also an accomplished painter and calligrapher. In painting he excelled in landscapes, figures, and horses — 'Autumn Colors on the Qiao and Hua Mountains' is his most celebrated work.",
  ["赵子昂", "Zhao Zi'ang", "松雪道人", "赵吴兴"], [], "", 0.85)

p("tang-yin", "唐寅", "Tang Yin (Tang Bohu)", 1470, 1524, "ming-dynasty",
  ["画家", "诗人", "明朝"], ["Painter", "Poet", "Ming Dynasty"],
  "明代「江南四大才子」之首，其画作和风流轶事在民间传说中被反复演绎至今。",
  "The foremost of Ming's 'Four Talents of Jiangnan'; his paintings and romantic legend have been endlessly retold through popular culture.",
  "唐寅（伯虎）的人生是一部天才陨落的悲剧。他在南京乡试中考取第一名（解元）后风光无限——但接下来在北京会试中卷入科场舞弊案被终身剥夺考试资格。他从一个前程似锦的士子变成了靠卖画为生的落魄才子。但也正是政治上的绝路使他把全部才华倾注于艺术——他的仕女画尤为精妙，《秋风纨扇图》中女子手持纨扇的落寞神情被视为画家自身心境的写照。后世将他的故事不断浪漫化——《唐伯虎点秋香》等戏曲影视使他成为中国文化中最具辨识度的风流才子形象，与真实历史已有相当距离。",
  "Tang Yin (courtesy name Bohu) lived the tragedy of fallen genius. After winning first place in the Nanjing provincial examinations, he seemed destined for glory — then became entangled in a Beijing metropolitan exam cheating scandal and was permanently barred from office. He fell from a scholar of boundless promise to a destitute talent selling paintings for survival. Yet this political dead end channeled his brilliance entirely into art — his paintings of court ladies are exquisitely delicate; the melancholy figure clutching a silk fan in 'Autumn Wind and Silk Fan' is read as a self-portrait of the artist's mood. Later generations romanticized his story endlessly — the opera 'Tang Bohu Courts Qiuxiang' and its countless film and TV adaptations have made him Chinese culture's most recognizable romantic genius figure, now considerably removed from the historical reality.",
  ["唐伯虎", "Tang Bohu", "六如居士", "桃花庵主"], ["src-mingshi"], "", 0.8)

p("xu-wei", "徐渭", "Xu Wei", 1521, 1593, "ming-dynasty",
  ["画家", "书法家", "文学家", "明朝"], ["Painter", "Calligrapher", "Writer", "Ming Dynasty"],
  "明代泼墨大写意花鸟画的开创者，「青藤画派」始祖，其艺术影响直达齐白石和八大山人。",
  "Ming pioneer of splash-ink expressive flower-and-bird painting, founder of the 'Green Vine School'; his influence extended directly to Qi Baishi and Bada Shanren.",
  "徐渭可能是中国艺术史上最不幸的天才——他出生百天丧父，成年后八次科举不第，一度精神失常九次自杀未遂（其中一次用铁钉钉入耳中），失手杀妻入狱七年。但他的艺术在这种极端的痛苦中爆发出了前所未有的创造力。他的泼墨大写意——以大笔饱蘸浓墨在纸上肆意挥洒——彻底打破了宋元以来工笔花鸟的精致传统。郑板桥刻了一方印「青藤门下走狗」表达对他的崇拜——齐白石更是说「恨不生前三百年，为青藤磨墨理纸」。",
  "Xu Wei may be the most unfortunate genius in Chinese art history — father dead before he was a hundred days old, failed the provincial exams eight times, suffered severe mental breakdowns with nine suicide attempts (once driving an iron nail into his ear), killed his wife in a fit and spent seven years in prison. Yet his art erupted with unprecedented creative force from this extreme suffering. His splash-ink expressive style — loading the brush with thick ink and sweeping it across the paper with abandon — utterly shattered the Song-Yuan tradition of meticulous gongbi flower-and-bird painting. Zheng Banqiao carved a seal reading 'Running Dog at the Green Vine Gate' to express his reverence; Qi Baishi went further: 'If only I had been born three hundred years earlier, I would grind ink and prepare paper for the Green Vine.'",
  ["徐文长", "Xu Wenchang", "青藤道士", "天池山人"], [], "", 0.8)

p("ba-da-shanren", "八大山人", "Bada Shanren (Zhu Da)", 1626, 1705, "qing-dynasty",
  ["画家", "书法家", "清朝"], ["Painter", "Calligrapher", "Qing Dynasty"],
  "清初四僧之一，明宗室后裔，以「白眼向人」的鱼鸟和极简水墨表达亡国之痛。",
  "One of the 'Four Monastic Masters' of early Qing, a Ming imperial descendant who expressed his dynasty's fall through contemptuous fish-birds and radical ink minimalism.",
  "八大山人原名朱耷——这是明太祖朱元璋第十七子宁王朱权的后裔。明朝灭亡时他才19岁。为了逃避迫害他出家为僧，后来精神间歇性失常——时而大笑时而痛哭。他将所有的悲痛和愤怒倾注于笔墨——他画的鱼和鸟全部翻着白眼——这是对征服者无声的蔑视。他的签名「八大山人」看上去既像「哭之」又像「笑之」——以字形本身传达哭笑皆非的情感。他的花鸟画以大面积的留白、极度简练的笔墨和变形的手法开创了水墨画的全新境界。",
  "Bada Shanren was born Zhu Da — a descendant of the Ming founder's son, Prince Ning. The dynasty fell when he was only 19. To escape persecution, he became a Buddhist monk, later suffering intermittent psychotic episodes — sometimes laughing hysterically, sometimes weeping uncontrollably. He channeled all his grief and rage into ink — his fish and birds all roll their eyes skyward in contemptuous white — silent scorn for the conquerors. His signature 'Bada Shanren' 八大山人 is graphically ambiguous — reading simultaneously as 'laughing it off' 笑之 and 'crying it over' 哭之 — expressing through the very form of the characters what words cannot. His flower-and-bird paintings, with vast areas of blank space, extreme brush economy, and deliberate distortion, opened an entirely new realm in ink-wash painting.",
  ["朱耷", "Zhu Da", "雪个", "驴屋"], [], "", 0.8)

# ===== 现代人物 (8) =====
p("liang-qichao", "梁启超", "Liang Qichao", 1873, 1929, "china",
  ["思想家", "学者", "政治家", "清朝", "民国"], ["Thinker", "Scholar", "Statesman", "Modern"],
  "中国近代史上最重要的启蒙思想家之一，戊戌变法领袖，「少年中国」的呐喊者。",
  "One of modern China's most important enlightenment thinkers, leader of the Hundred Days' Reform, and herald of 'Young China.'",
  "梁启超23岁时便与老师康有为一同领导了戊戌变法——失败后流亡日本十四年。在海外他创办《清议报》和《新民丛报》——以笔为武器向国内输送新思想。他的文章气势磅礴——「少年智则国智，少年富则国富，少年强则国强」至今仍被每一个中国学生朗读。他涉猎了政治学、历史学、哲学、文学、经济学等几乎所有人文社科领域——著作达一千四百万字。他的子女个个成才：长子梁思成是建筑学家（参与了国徽设计），次子梁思永是考古学家，三子梁思礼是火箭专家。",
  "At just 23, Liang Qichao led the Hundred Days' Reform alongside his teacher Kang Youwei — after its failure, he spent fourteen years exiled in Japan. From abroad, he founded journals like 'The China Discussion' and 'New Citizen' — wielding his pen as a weapon to inject new ideas into China. His prose thunders with power — 'When the youth are wise, the nation is wise; when the youth are wealthy, the nation is wealthy; when the youth are strong, the nation is strong' — still recited by every Chinese student today. He ventured into virtually every field of the humanities and social sciences — political science, history, philosophy, literature, economics — leaving a corpus of fourteen million characters. His children all achieved eminence: the eldest, Liang Sicheng, was an architectural historian who helped design China's national emblem; the second, Liang Siyong, was an archaeologist; the third, Liang Sili, was a rocket scientist.",
  ["梁任公", "Liang Rengong", "饮冰室主人"], [], "", 0.9)

p("cai-yuanpei", "蔡元培", "Cai Yuanpei", 1868, 1940, "china",
  ["教育家", "思想家", "民国"], ["Educator", "Thinker", "Republic of China"],
  "中国近代最伟大的教育家，北京大学校长，「思想自由兼容并包」的办学方针奠定了中国现代大学精神。",
  "Modern China's greatest educator who, as president of Peking University, established 'freedom of thought, inclusiveness' as the cornerstone of the modern Chinese university spirit.",
  "蔡元培最为人铭记的身份是北京大学校长——但他同时也是清廷翰林、光复会创始人、教育总长。1917年就任北大校长时这所学校还以官僚的衙门习气闻名——他把李大钊、陈独秀、胡适、鲁迅、钱玄同等一批新文化运动的旗手全部聘入北大——同时也留用了辜鸿铭、刘师培等旧派学者——真正践行了「思想自由兼容并包」。他支持学生的五四爱国运动却反对学生过度参与政治活动。他的教育理念——德智体美劳全面发展——至今仍是中国的教育宗旨。",
  "Cai Yuanpei is best remembered as president of Peking University — but he was also a Qing Hanlin Academy scholar, co-founder of the Restoration Society, and Minister of Education. When he assumed the PKU presidency in 1917, the institution was notorious as a bureaucratic sinecure mill. He recruited the entire vanguard of the New Culture Movement — Li Dazhao, Chen Duxiu, Hu Shi, Lu Xun, Qian Xuantong — while also retaining conservative scholars like Gu Hongming and Liu Shipei — truly practicing 'freedom of thought and inclusiveness.' He supported the students' May Fourth patriotic movement while opposing excessive student involvement in politics. His educational philosophy — the all-round development of morality, intellect, physique, aesthetics, and labor — remains China's educational objective to this day.",
  ["蔡孑民", "Cai Jiemin", "蔡鹤卿"], [], "", 0.9)

p("hu-shi", "胡适", "Hu Shi", 1891, 1962, "china",
  ["思想家", "文学家", "学者", "民国"], ["Thinker", "Writer", "Scholar", "Republic of China"],
  "新文化运动领袖，白话文运动的主要推动者，哥伦比亚大学哲学博士，一生倡导自由主义。",
  "Leader of the New Culture Movement and principal driver of vernacular Chinese; Columbia PhD who championed liberalism throughout his life.",
  "胡适26岁从哥伦比亚大学博士毕业回国——一到上海码头就宣布中国需要「文学革命」——用活的白话文取代死的文言文。他的《文学改良刍议》提出了八项主张——「不用典」「不避俗字俗语」等。他自己身体力行写了中国第一部白话诗集《尝试集》和第一部白话话剧《终身大事》。他在学术上的成就同样惊人——《中国哲学史大纲》以现代学术方法重新审视先秦诸子、《红楼梦考证》开创了新红学。他的墓志铭只有五个字——「这是胡适的墓」——是他一生所倡导的朴素白话最好的注脚。",
  "Hu Shi returned from Columbia University with his PhD at 26 — the moment he disembarked at Shanghai, he announced China needed a 'literary revolution' — replacing dead classical Chinese with living vernacular. His 'Tentative Proposals for Literary Reform' set forth eight principles — 'avoid classical allusions,' 'do not shun colloquial expressions.' He led by example, writing China's first vernacular poetry collection 'Experiments' and first vernacular play 'The Greatest Event in Life.' His scholarly achievements were equally staggering — 'An Outline History of Chinese Philosophy' re-examined pre-Qin thinkers through modern methodology; his 'Textual Research on Dream of the Red Chamber' founded the New Redology. His epitaph reads simply: 'This is Hu Shi's tomb' — the perfect testament to the plain vernacular he championed all his life.",
  ["胡适之", "Hu Shizhi"], [], "", 0.9)

p("qian-xuesen", "钱学森", "Qian Xuesen", 1911, 2009, "china",
  ["科学家", "航天", "现代"], ["Scientist", "Aerospace", "Modern China"],
  "中国航天之父和导弹之父，参与创建美国喷气推进实验室，历经五年软禁后回国开创了中国航天事业。",
  "Father of China's space and missile programs; co-founder of JPL, endured five years of US house arrest before returning to China to found its aerospace enterprise.",
  "钱学森的故事是中美冷战史最戏剧性的篇章之一。他1935年赴美留学，成为空气动力学宗师冯·卡门的得意门生——后来参与创建了喷气推进实验室（JPL）——他的安全许可等级高到能接触美国所有军事机密。1950年麦卡锡时代他被指控为共产党员被软禁五年——无法进行任何研究工作。1955年经过周恩来政府的艰难谈判以朝鲜战争中的美军战俘换回了他。回国后他白手起家创建了中国导弹和航天体系——从东风导弹到长征火箭到神舟飞船——他的足迹贯穿了中国航天发展的全部历程。",
  "Qian Xuesen's story is one of the Cold War's most dramatic chapters. He went to America in 1935, becoming the star student of aerodynamics master Theodore von Kármán, and co-founded the Jet Propulsion Laboratory — his security clearance gave him access to virtually all US military secrets. In 1950, the McCarthy era saw him accused of Communist Party membership and confined under house arrest for five years, barred from all research. In 1955, painstaking negotiations by the Zhou Enlai government exchanged American POWs from the Korean War for his return. Back in China, he built the missile and space program from nothing — from Dongfeng missiles to Long March rockets to Shenzhou spacecraft — his career tracing the entire arc of China's aerospace development.",
  ["Tsien Hsue-shen"], [], "", 0.9)

p("yuan-longping", "袁隆平", "Yuan Longping", 1930, 2021, "china",
  ["科学家", "农学家", "现代"], ["Scientist", "Agronomist", "Modern China"],
  "中国杂交水稻之父，其研究成果解决了数亿人的温饱问题，获国家最高科学技术奖和共和国勋章。",
  "Father of hybrid rice whose research has fed hundreds of millions; recipient of China's highest science award and the Medal of the Republic.",
  "袁隆平的故事始于1960年代——他目睹了大饥荒中饿死的人，下决心用科学技术消灭饥饿。1973年他领导的团队成功培育出世界上第一株杂交水稻——将水稻亩产从约300公斤提升到500公斤以上。此后他从未停止——超级稻计划将亩产推到700公斤、800公斤、900公斤、1000公斤——不断刷新世界纪录。他的杂交水稻技术被推广到印度、越南、菲律宾、巴基斯坦、非洲各国——在全球范围内养活了难以计数的人口。他九十岁高龄时仍几乎每天都下田——「我毕生的追求就是让所有人远离饥饿。」",
  "Yuan Longping's story begins in the 1960s — witnessing people starve to death during the great famine, he resolved to use science and technology to eliminate hunger. In 1973, his team successfully bred the world's first hybrid rice plant — raising per-mu yields from roughly 300 kg to over 500 kg. He never stopped — the Super Rice program pushed yields to 700, 800, 900, 1,000 kg per mu — repeatedly shattering world records. His hybrid rice technology has been transferred to India, Vietnam, the Philippines, Pakistan, and across Africa — feeding uncountable populations worldwide. At ninety, he still went to the paddies nearly every day — 'My life's pursuit is to keep everyone away from hunger.'",
  [], [], "", 0.95)

p("zhan-tianyou", "詹天佑", "Zhan Tianyou", 1861, 1919, "china",
  ["工程师", "科学家", "清朝", "民国"], ["Engineer", "Scientist", "Modern China"],
  "中国铁路之父，京张铁路的总工程师，以「之」字形爬坡方案让中国人自己设计建造了第一条铁路。",
  "Father of China's railways and chief engineer of the Beijing-Zhangjiakou line, who devised the zigzag climbing solution for China's first self-designed railway.",
  "詹天佑是中国第一批赴美留学的幼童之一——12岁到美国，从耶鲁大学土木工程系毕业。回国后他一度被安排去学海军驾驶——人才被极度浪费。他主持修建京张铁路时面临西方工程师认为不可能完成的挑战——穿越八达岭的陡峭山坡。他创造性地设计了「之」字形路线——火车先向前开到岔道再倒退继续爬升——以有限的经费和技术条件完成了这条铁路。他还创立了中华工程师学会——培养了中国第一代本土工程技术人员。",
  "Zhan Tianyou was among the first cohort of Chinese children sent to study in America — arriving at 12 and graduating from Yale's civil engineering program. Returning to China, he was absurdly assigned to study naval navigation — a colossal waste of talent. When tasked with building the Beijing-Zhangjiakou railway, he faced what Western engineers had declared impossible — the precipitous slopes through Badaling. He creatively devised the 'switchback' (zigzag) route — the train would advance to a siding, then reverse to continue climbing — completing the railway with limited budget and technology. He also founded the Chinese Institute of Engineers, training China's first generation of indigenous engineering talent.",
  ["詹眷诚", "Zhan Juancheng"], [], "", 0.85)

p("wang-guowei", "王国维", "Wang Guowei", 1877, 1927, "china",
  ["学者", "史学家", "文学家", "清朝", "民国"], ["Scholar", "Historian", "Modern China"],
  "中国近代学术史上最博学的人物之一，以「二重证据法」开创了中国现代史学方法论。",
  "One of the most erudite figures in modern Chinese scholarship who pioneered modern historical methodology with the 'dual-evidence method.'",
  "王国维的学术视野之广令人叹为观止——他精通哲学（最早将叔本华和康德系统地介绍到中国）、文学（《人间词话》是中国词学批评的巅峰之作）、古文字学（最早系统研究甲骨文并取得了突破性成果）、历史学（开创了以地下出土文物印证传世文献的「二重证据法」）。他提出的「治学三境界」——「昨夜西风凋碧树，独上高楼，望尽天涯路」「衣带渐宽终不悔，为伊消得人憔悴」「众里寻他千百度，蓦然回首，那人却在灯火阑珊处」——已成为中国知识分子学术追求的精神格言。1927年他在颐和园昆明湖自沉——遗书只有十六个字：「五十之年，只欠一死。经此世变，义无再辱。」",
  "Wang Guowei's scholarly breadth is breathtaking — he was master of philosophy (first to systematically introduce Schopenhauer and Kant to China), literature (his 'Poetic Remarks in the Human World' is the summit of Chinese ci-poetry criticism), paleography (among the first to systematically study oracle bones, producing breakthrough results), and history (pioneering the 'dual-evidence method' of corroborating transmitted texts with excavated artifacts). His 'Three Realms of Scholarship' — borrowed from Song ci lyrics about solitary pursuit, relentless devotion, and sudden enlightenment — has become the spiritual motto of Chinese intellectual endeavor. In 1927, he drowned himself in Kunming Lake at the Summer Palace — his suicide note contained only sixteen characters: 'At fifty, I owe only death. After this epochal upheaval, righteousness forbids further humiliation.'",
  ["王静安", "Wang Jing'an", "观堂"], [], "", 0.85)

p("zhu-kezhen", "竺可桢", "Zhu Kezhen", 1890, 1974, "china",
  ["科学家", "气象学家", "地理学家", "教育家"], ["Scientist", "Meteorologist", "Geographer", "Educator"],
  "中国气象学和地理学奠基人，浙江大学校长，对中国五千年气候变化的重建工作在国际上影响深远。",
  "Founder of Chinese meteorology and geography, president of Zhejiang University; his reconstruction of China's 5,000-year climate history was internationally influential.",
  "竺可桢是哈佛大学气象学博士——中国第一位获得气象学博士学位的学者。他创建了中国第一个气象研究所，在全国范围内建立了气象观测网络。他最为人称道的学术成就是对中国历史时期气候变化的重建——从《诗经》《二十四史》等古籍中搜集了数千条物候记录——梅花开放的时间、降雪的日期、河流封冻的情况——通过这些碎片重建了中国近五千年的温度变化曲线。这一工作在世界气候变迁研究史上具有里程碑式的意义。他担任浙江大学校长期间提出的「求是」校训——至今仍是浙大的精神核心。",
  "Zhu Kezhen earned his PhD in meteorology from Harvard — the first Chinese scholar to achieve this. He founded China's first meteorological research institute and established a nationwide weather observation network. His most celebrated scholarly achievement is reconstructing China's historical climate change — mining thousands of phenological records from classical texts like the 'Book of Songs' and the 'Twenty-Four Histories' — plum blossom blooming dates, snowfall records, river freeze dates — from these fragments he reconstructed China's temperature curve over the past five millennia. This work holds landmark significance in global climate change research. As president of Zhejiang University, he articulated the motto 'Seek Truth' (Qiu Shi) — which remains the university's spiritual core.",
  [], [], "", 0.9)

# ===== 著名女性 (3) =====
p("lü-zhi", "吕雉", "Empress Lü Zhi", -241, -180, "han-dynasty",
  ["政治家", "女性", "汉朝"], ["Stateswoman", "Female Ruler", "Han Dynasty"],
  "中国历史上第一位实际统治帝国的女性，刘邦之妻，临朝称制16年，将戚夫人做成「人彘」使她背上千古骂名。",
  "The first woman to actually rule imperial China; Liu Bang's wife ruled as Empress Dowager for 16 years; her transformation of Consort Qi into a 'human pig' earned her eternal infamy.",
  "吕雉是刘邦的糟糠之妻——在刘邦还只是一个亭长时嫁给了他。楚汉战争中她被项羽俘虏做了两年多人质。刘邦称帝后想改立宠妃戚夫人之子为太子——吕雉请出商山四皓保住了儿子刘盈的太子之位。刘邦死后她临朝称制——这是中国历史上第一次女性实际掌控最高权力。她对戚夫人的报复堪称中国历史上最残忍——砍去手足、挖眼熏耳、灌哑药、扔在厕所中称为「人彘」——甚至叫儿子刘盈去看——刘盈看后惊吓过度从此不理朝政纵酒而死。然而她在治国上却颇为能干——维持了汉初的休养生息政策。",
  "Lü Zhi was Liu Bang's wife from poverty — she married him when he was still just a village chief. During the Chu-Han War, Xiang Yu held her hostage for over two years. After Liu Bang became emperor, he wanted to replace her son, the crown prince, with the son of his favorite consort Qi — Lü Zhi summoned the Four Whiteheads of Mount Shang to secure her son Liu Ying's position. After Liu Bang's death, she ruled as Empress Dowager — the first woman to actually wield supreme power in Chinese history. Her revenge on Consort Qi is arguably the cruelest in Chinese history — she cut off her limbs, gouged out her eyes, burned out her ears, forced a silence-inducing drug, and threw her into a latrine, calling her a 'human pig' — then made her son Liu Ying go see. The traumatized emperor abandoned governance and drank himself to death. Yet in governance she was surprisingly capable, maintaining the early Han policy of recovery and rest.",
  ["吕太后", "Empress Lü", "汉高后"], ["src-shiji", "src-hanshu"], "", 0.85)

p("wang-zhaojun", "王昭君", "Wang Zhaojun", -50, -15, "han-dynasty",
  ["女性", "和亲", "汉朝"], ["Historical Woman", "Heqin", "Han Dynasty"],
  "中国古代四大美女之「落雁」，被选入宫后因不肯贿赂画师而被丑化，最终远嫁匈奴呼韩邪单于。",
  "One of the 'Four Great Beauties' of ancient China whose nickname 'Dropping Geese' came from her legendary appearance; refused to bribe the court painter and was sent to marry a Xiongnu chanyu.",
  "王昭君的故事充满了浪漫和悲剧色彩。她被选入汉元帝后宫，但当时宫廷画师毛延寿负责为宫女画像供皇帝挑选——其他宫女都贿赂画师将自己画得更美，唯独王昭君不肯。毛延寿便在她的画像上点了一颗丧夫痣。当匈奴呼韩邪单于来长安请求和亲时，元帝按图索骥选中了最丑的王昭君。临行告别时元帝第一次见到她的真容——惊为天人但为时已晚。她远嫁匈奴后先后嫁给了呼韩邪单于和他的儿子——在草原上生活了三十余年，死后葬于大青山南麓——她的坟墓被称为「青冢」——据说塞外草木皆白唯有此冢草色常青。",
  "Wang Zhaojun's story mingles romance and tragedy. Selected for Emperor Yuan's harem, she fell under the power of court painter Mao Yanshou, whose portraits determined which women the emperor would summon. All the other palace women bribed the painter to enhance their beauty — only Wang Zhaojun refused. Mao marked her portrait with a mole indicating widowhood. When the Xiongnu chanyu Huhanye came to Chang'an requesting a marriage alliance, Emperor Yuan picked the 'ugliest' based on the portraits — Wang Zhaojun. At the farewell ceremony, he saw her true beauty for the first time — and was thunderstruck, but it was too late to change. She married into the Xiongnu, first to Huhanye, then to his son, living over thirty years on the steppe. Her tomb south of the Daqing Mountains is called 'Green Mound' — legend says all vegetation beyond the Great Wall turns white, but the grass on her mound remains forever green.",
  ["王嫱", "Wang Qiang", "明妃", "落雁"], ["src-hanshu"], "", 0.75)

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
print(f"\n// Total: {len(people)} figures (artists, modern, women)")
