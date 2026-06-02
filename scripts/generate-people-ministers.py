#!/usr/bin/env python3
"""Generate Chinese historical figures: ministers, literati, scientists, strategists.
Outputs TypeScript Person[] entries to stdout.
Already in mockData.ts: 苏轼/王安石/欧阳修/李白/司马迁/杜甫/李时珍/李鸿章/
孙子/李斯/商鞅/白居易/王维/鲁迅/李清照/张衡/沈括/徐光启/韩愈/诸葛亮/魏征/
郑和/玄奘/岳飞/王阳明/罗贯中/顾恺之"""
def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")

people = []

def p(id, name, nameEn, birth, death, region, tags, tagsEn, summary, summaryEn, desc, descEn,
      alt=None, srcs=None, wiki="", conf=0.85):
    people.append({
        "id": id, "name": name, "nameEn": nameEn, "birthYear": birth, "deathYear": death,
        "regionId": region, "tags": tags, "tagsEn": tagsEn, "occupations": ["政治家"],
        "summary": summary, "summaryEn": summaryEn,
        "description": desc, "descriptionEn": descEn,
        "alternativeNames": alt or [],
        "sourceIds": srcs or [],
        "wikidataQid": wiki,
        "dataStatus": "published",
        "confidenceScore": conf,
        "externalReferences": []
    })

# ===== 名臣 (17) =====
p("xiao-he", "萧何", "Xiao He", -257, -193, "han-dynasty",
  ["名臣", "政治家", "汉朝"], ["Minister", "Statesman", "Han Dynasty"],
  "西汉开国第一功臣，汉初三杰之一，月下追韩信，制定汉律，为汉朝四百年基业奠定制度基础。",
  "The foremost founding minister of Western Han, one of the Three Heroes. He pursued Han Xin under moonlight and established Han laws that underpinned four centuries of dynasty.",
  "萧何是刘邦的沛县同乡，秦末时任沛县主吏掾。刘邦起义后他始终掌管后勤和行政——秦朝灭亡时他不收金银而收取秦朝的律令图书，为汉朝的制度建设提供了关键基础。他月下追回韩信的典故展现了识人之明。汉朝建立后他制定《九章律》，构建了汉初的法律和赋税体系，是汉帝国行政机器的总设计师。司马迁评价他「位冠群臣，声施后世」。",
  "Xiao He, a fellow townsman of Liu Bang from Pei county, managed logistics and administration throughout Liu Bang's rise. When Qin fell, he famously seized its legal codes and archives rather than treasure, providing the blueprint for Han's institutional foundation. His legendary midnight pursuit of Han Xin demonstrated his eye for talent. After Han's establishment, he compiled the 'Nine Chapters Law,' constructing the legal and tax framework of early Han. Sima Qian praised him: 'Foremost among ministers, his reputation endures through the ages.'",
  ["萧相国", "Xiao He"], ["src-shiji", "src-hanshu"], "", 0.9)

p("zhang-liang", "张良", "Zhang Liang", -250, -186, "han-dynasty",
  ["名臣", "谋士", "战略家", "汉朝"], ["Minister", "Strategist", "Han Dynasty"],
  "汉初三杰之一，运筹帷幄之中决胜千里之外，博浪沙刺秦、圯桥进履的故事广为人知。",
  "One of the Three Heroes of early Han, master strategist who 'devised strategies within a tent to decide victory a thousand miles away.'",
  "张良出身韩国贵族世家，五代为韩相。秦灭韩后他散尽家财在博浪沙刺杀秦始皇未果，逃亡中得到黄石公传授《太公兵法》。他辅佐刘邦后在鸿门宴上巧妙斡旋、劝刘邦烧毁栈道取信项羽、建议封韩信为齐王以稳定军心。刘邦评价他「运筹帷幄之中，决胜千里之外，吾不如子房」。汉朝建立后，他急流勇退——自请食邑仅留县而非万户，并逐步隐退修仙——成为智慧和功成身退的象征。",
  "Zhang Liang came from a family that served five generations as Han state chancellors. After Qin destroyed Han, he bankrupted himself attempting to assassinate Qin Shi Huang at Bolangsha. In hiding, he received the 'Grand Duke's Art of War' from the mysterious Master Yellow Rock. Serving Liu Bang, he defused the crisis at Hongmen, advised burning the plank roads to win Xiang Yu's trust, and recommended enfeoffing Han Xin. Liu Bang said: 'Devising strategies in camp to decide victory a thousand li away — I cannot match Zifang.' After Han's founding, he withdrew from power — requesting only the smallest fief and retiring to pursue Daoist immortality — becoming a symbol of wisdom and timely withdrawal.",
  ["张子房", "Zhang Zifang", "留侯"], ["src-shiji", "src-hanshu"], "", 0.9)

p("huo-guang", "霍光", "Huo Guang", -120, -68, "han-dynasty",
  ["名臣", "政治家", "汉朝", "权臣"], ["Minister", "Statesman", "Han Dynasty"],
  "西汉权臣，霍去病异母弟，以大司马大将军身份辅政三朝，废黜昌邑王扶立汉宣帝。",
  "Western Han statesman and half-brother of Huo Qubing who, as Regent Marshal, governed three reigns and deposed one emperor to enthrone another.",
  "霍光是霍去病的异母弟弟，被武帝托孤为辅政大臣之首。他辅佐8岁的汉昭帝，挫败了上官桀等人的政变，独掌大权二十年。昭帝去世后他立昌邑王刘贺为帝——但刘贺在位仅27天就因荒淫被霍光废黜。霍光随后从民间迎立了武帝的曾孙刘病已（汉宣帝）。宣帝形容与霍光同车「如芒在背」——霍氏的权势已令皇帝恐惧。霍光去世后两年，宣帝即铲除了整个霍氏家族。",
  "Huo Guang, half-brother of the great general Huo Qubing, was appointed chief regent by the dying Emperor Wu. He governed on behalf of the 8-year-old Emperor Zhao, suppressing a coup by Shangguan Jie and dominating the state for two decades. After Emperor Zhao's death, he installed Prince Liu He of Changyi — but deposed him after just 27 days for debauchery. He then found Emperor Wu's great-grandson Liu Bingyi living among commoners and enthroned him as Emperor Xuan. Xuan later described riding with Huo Guang 'like having a thorn in my back' — such was the terror of the Huo clan's power. Two years after Huo Guang's death, Xuan exterminated the entire family.",
  ["霍子孟", "Huo Zimeng"], ["src-hanshu"], "", 0.85)

p("fang-xuanling", "房玄龄", "Fang Xuanling", 579, 648, "tang-dynasty",
  ["名臣", "政治家", "唐朝"], ["Minister", "Statesman", "Tang Dynasty"],
  "唐初名相，「房谋杜断」之房谋，辅佐李世民策划玄武门之变，任宰相二十余年。",
  "Early Tang chancellor, the 'strategist' half of 'Fang plans, Du decides,' mastermind of the Xuanwu Gate coup who served as chancellor for over twenty years.",
  "房玄龄早年为隋朝官员时便识破隋朝将亡，投奔李世民后成为秦王府首席谋士。玄武门之变的核心策划出自他之手。太宗即位后他任中书令、尚书左仆射——相当于宰相——长达二十余年。他最大的贡献在于制度建设：裁汰冗员、完善三省六部制度的运作、主持修订律令。他以超人的勤奋著称——据说每天处理政务要到深夜。他和杜如晦被称为「房谋杜断」——他善于谋划，杜善于决断。",
  "Fang Xuanling, recognizing the Sui dynasty was doomed, joined Li Shimin's staff and became the Prince of Qin's chief strategist. The Xuanwu Gate coup was largely his design. After Taizong's accession, he served effectively as chancellor for over twenty years. His greatest contribution lay in institution-building: streamlining the bureaucracy, perfecting the three-department system, and compiling legal codes. Legendarily hardworking — reportedly handling state business deep into every night. With Du Ruhui they formed 'Fang plans, Du decides' — Fang was the master strategist, Du the decisive executor.",
  ["房乔", "Fang Qiao"], ["src-jiutangshu"], "", 0.85)

p("di-renjie", "狄仁杰", "Di Renjie", 630, 700, "tang-dynasty",
  ["名臣", "政治家", "唐朝"], ["Minister", "Statesman", "Tang Dynasty"],
  "唐朝名相，武则天时期的栋梁之臣，以断案如神和举贤任能著称，至今仍是大理寺和神探的文化符号。",
  "Tang chancellor and pillar of Wu Zetian's reign, famed for brilliant adjudication and talent-spotting, remaining a cultural icon of justice.",
  "狄仁杰历任大理寺丞——据说他一年内判决积压案件一万七千余件，无一人喊冤。他在地方任职期间深受百姓爱戴，为他树立生祠。武周时期他出任宰相，是武则天最倚重的大臣之一。他最大的政治贡献是在不正面挑战武则天的前提下，为李唐复辟铺路——他力荐张柬之等人，最终这些人在武则天晚年发动政变恢复李唐。他的事迹被后世演绎为《狄公案》系列小说和影视作品——荷兰汉学家高罗佩甚至用英文创作了《大唐狄公案》。",
  "Di Renjie served as Chief Judge of the Supreme Court — reportedly clearing a backlog of 17,000 cases in a single year without a single appeal of injustice. As a local official, he was so beloved that people erected shrines in his honor during his lifetime. Under Wu Zetian's Zhou dynasty, he served as chancellor and was among her most trusted ministers. His greatest political achievement was paving the way for Tang restoration without directly challenging Wu Zetian — he recommended Zhang Jianzhi and others who eventually launched the coup restoring the Tang. His exploits inspired the 'Judge Dee' mystery novels, adapted even by Dutch sinologist Robert van Gulik in English as 'Celebrated Cases of Judge Dee.'",
  ["狄怀英", "Di Huaiying", "狄公"], ["src-jiutangshu"], "", 0.85)

p("bao-zheng", "包拯", "Bao Zheng", 999, 1062, "song-dynasty",
  ["名臣", "清官", "宋朝"], ["Minister", "Incorruptible Official", "Song Dynasty"],
  "北宋名臣，以铁面无私、执法如山著称，「包青天」成为中国文化中正义与清廉的化身。",
  "Northern Song minister renowned for absolute incorruptibility and impartial justice; 'Bao Qingtian' became the cultural embodiment of righteousness.",
  "包拯出身进士，历任知县、知府、御史中丞、三司使直至枢密副使。他铁面无私——弹劾过宰相、皇亲国戚甚至自己的举荐人。他最著名的是建议设立「登闻鼓」让平民直接申冤于御前。他断案公正、不畏权贵的故事通过元杂剧《包待制》和明清小说广为流传，后世「包青天」的月牙形印记和「龙头铡虎头铡狗头铡」等元素虽然多属虚构，却深刻塑造了中国民间对司法正义的想象。他的家训要求子孙如有贪赃枉法者「生不得归本家，死不得葬祖茔」。",
  "Bao Zheng rose from county magistrate to Vice Commissioner of Military Affairs. He was utterly incorruptible — impeaching chancellors, imperial relatives, and even his own patrons without hesitation. He famously advocated the 'Dengwen Drum' system allowing commoners to appeal directly to the throne. His tales of fearless justice — vastly embellished by Yuan-dynasty zaju drama and Ming-Qing fiction — with moon-shaped birthmarks and dragon/tiger/dog-head guillotines (mostly fictional) profoundly shaped the Chinese popular imagination of judicial justice. His family precepts warned that any descendant convicted of corruption would be 'denied return to the ancestral home in life and burial in the ancestral cemetery in death.'",
  ["包希仁", "Bao Xiren", "包青天", "包龙图"], ["src-ss"], "", 0.9)

p("fan-zhongyan", "范仲淹", "Fan Zhongyan", 989, 1052, "song-dynasty",
  ["名臣", "文学家", "改革家", "宋朝"], ["Minister", "Writer", "Reformer", "Song Dynasty"],
  "北宋名臣和文学家，「先天下之忧而忧，后天下之乐而乐」的名句流传千古，推动庆历新政。",
  "Northern Song minister and literary figure whose immortal line 'Be the first to bear the world's troubles, the last to enjoy its pleasures' embodies Confucian idealism.",
  "范仲淹两岁丧父，母亲改嫁，他在醴泉寺刻苦读书——据说每天只煮一锅粥划为四块早晚各吃两块。中进士后他为官清廉刚正，多次因直言被贬，友人梅尧臣劝他少说话，他回答「宁鸣而死，不默而生」。1043年他在仁宗支持下推行庆历新政——改革科举、整顿吏治、减轻徭役——但触动了官僚集团利益而失败。被贬后他在《岳阳楼记》中写下「先天下之忧而忧，后天下之乐而乐」——这十个字定义了中国士大夫两千年的精神追求。",
  "Fan Zhongyan lost his father at two; his mother remarried and he studied in bitter poverty at Liquan Temple — reportedly dividing one daily pot of congee into four portions. After earning the jinshi degree, he served with uncompromising integrity, repeatedly demoted for blunt remonstrance. When poet Mei Yaochen urged him to hold his tongue, he replied: 'Better to die speaking out than live in silence.' In 1043, with Emperor Renzong's backing, he launched the Qingli Reforms — restructuring examinations, purging corrupt officials, and reducing corvée — but vested bureaucratic interests crushed the effort. In exile, writing 'On Yueyang Tower,' he penned the line that defined two millennia of Chinese literati idealism: 'Be first to bear the world's troubles; be last to enjoy its pleasures.'",
  ["范希文", "Fan Xiwen"], ["src-ss"], "", 0.9)

p("wen-tianxiang", "文天祥", "Wen Tianxiang", 1236, 1283, "song-dynasty",
  ["名臣", "民族英雄", "南宋", "诗人"], ["Minister", "National Hero", "Southern Song", "Poet"],
  "南宋末代丞相，被元朝俘虏后宁死不降，「人生自古谁无死，留取丹心照汗青」成为千古绝唱。",
  "Last chancellor of Southern Song who chose death over surrender to the Mongols; his verses 'Who since time began has escaped death? Let my loyal heart illuminate the annals' are immortal.",
  "文天祥20岁中状元。元军南下时他散尽家财组织义军勤王。他奉命出使元营谈判被扣押，在押送途中逃脱后继续组织抵抗，最终兵败被俘。元朝以高官厚禄诱降，元世祖忽必烈甚至亲自劝降，他始终不为所动。在燕京牢狱中他写下了《正气歌》和《过零丁洋》——「人生自古谁无死，留取丹心照汗青」成为此后数百年中国文人殉节的精神坐标。1283年他在燕京柴市从容就义，年仅47岁。",
  "Wen Tianxiang earned the highest imperial examination rank at 20. When the Mongols swept south, he liquidated his family fortune to raise a loyalist army. Sent to negotiate with the Mongol camp, he was seized but escaped en route and continued resisting until final capture. The Yuan court offered him high office; Kublai Khan personally tried to persuade him — Wen remained unmoved. In a Yanjing prison, he wrote 'Song of Righteousness' and 'Crossing Lingdingyang' — 'Who since time began has escaped death? Let my loyal heart illuminate the annals' became the spiritual lodestar for Chinese scholar-martyrs for centuries. He was executed at Yanjing's Chai Market in 1283, aged 47.",
  ["文宋瑞", "Wen Songrui"], ["src-ss"], "", 0.9)

p("yu-qian", "于谦", "Yu Qian", 1398, 1457, "ming-dynasty",
  ["名臣", "军事家", "明朝", "民族英雄"], ["Minister", "Military Commander", "Ming Dynasty", "National Hero"],
  "明朝名臣，土木堡之变后力排南迁之议，领导北京保卫战击退瓦剌大军，挽救了明朝。",
  "Ming minister who, after the Tumu Crisis, vetoed the proposal to abandon the north, led the defense of Beijing, and saved the dynasty from collapse.",
  "于谦在土木堡之变——明英宗被俘、精锐全军覆没——后的关键时刻挺身而出。朝中大部分大臣主张迁都南京，于谦厉声驳斥：「言南迁者可斩也！」他拥立景泰帝、迅速调集京畿兵力、在北京城外修筑工事。瓦剌大军兵临城下时他亲自督战，最终击退敌军。他清廉到被抄家时家中除了皇帝赏赐的袍服外空无一物。英宗复辟后他因「谋立外藩」的莫须有罪名被杀——与岳飞一样，成为忠臣遭冤的悲剧象征。",
  "Yu Qian stepped forward at the decisive moment after the Tumu Crisis — when Emperor Yingzong was captured and the Ming's elite army annihilated. Most courtiers urged abandoning Beijing for Nanjing; Yu Qian thundered: 'Those who speak of retreating south should be beheaded!' He enthroned a new emperor, mustered garrison forces, and fortified Beijing. When the Mongol army reached the walls, he personally directed the defense and repelled the invaders. He was so incorruptible that when his house was searched after his arrest, nothing of value was found except robes gifted by the emperor. After Yingzong's restoration, Yu Qian was executed on fabricated charges — joining Yue Fei as a tragic symbol of loyal ministers destroyed by the states they saved.",
  ["于廷益", "Yu Tingyi"], ["src-mingshi"], "", 0.9)

p("zhang-juzheng", "张居正", "Zhang Juzheng", 1525, 1582, "ming-dynasty",
  ["名臣", "改革家", "明朝"], ["Minister", "Reformer", "Ming Dynasty"],
  "明朝最有权势的首辅，推行「一条鞭法」等改革，以一己之力为明朝延续了半个世纪的寿命。",
  "Ming dynasty's most powerful Grand Secretary whose 'Single Whip' tax reform single-handedly extended the dynasty's life by half a century.",
  "张居正以万历皇帝老师的身份掌握大权十年。他是实干派——面对国库空虚、吏治腐败、边患不断的烂摊子，他推行了一系列雷厉风行的改革：考成法整顿官吏考核、一条鞭法将复杂的赋税劳役合并为统一货币税、重新丈量全国土地。他的铁腕手段激怒了既得利益集团，但改革成效显著：国库从亏空转为盈余数百万两。他去世后万历皇帝展开了疯狂的清算——削去一切官职、抄家、长子自尽。但明朝此后数十年一直在吃他改革的老本。",
  "Zhang Juzheng wielded supreme power for a decade as the Wanli Emperor's tutor. A ruthless pragmatist confronting an empty treasury, endemic corruption, and constant border threats, he enacted sweeping reforms: the 'Performance Evaluation Law' to hold officials accountable, the 'Single Whip Reform' consolidating complex taxes and corvée into a single silver payment, and a nationwide land survey. His iron hand angered vested interests, but the results were dramatic — the treasury swung from deficit to millions of taels in surplus. After his death, the Wanli Emperor launched a vindictive purge — stripping all ranks, confiscating property, and driving Zhang's eldest son to suicide. Yet Ming survived for decades thereafter consuming the reserves his reforms had built.",
  ["张叔大", "Zhang Shuda", "张江陵"], ["src-mingshi"], "", 0.9)

p("hai-rui", "海瑞", "Hai Rui", 1514, 1587, "ming-dynasty",
  ["名臣", "清官", "明朝"], ["Minister", "Incorruptible Official", "Ming Dynasty"],
  "明朝清官典范，以抬棺上疏骂皇帝闻名，一生清廉到买不起肉为母亲祝寿的地步。",
  "Paragon of incorruptibility in Ming China, famous for submitting a memorial denouncing the emperor while carrying his own coffin; so poor he couldn't afford meat for his mother's birthday.",
  "海瑞可能是中国历史上最极端的清官。1566年他给嘉靖皇帝上了一道《治安疏》——直斥皇帝沉迷道教、不理朝政——他在上疏前已经买好了棺材。嘉靖虽然大怒但没有杀他，只是关入大牢——皇帝死后他才获释。他在地方任职时自种蔬菜、为母亲祝寿只买了两斤肉居然成了轰动消息。他的极端廉洁使他在官场中格格不入，但也使他成为民间传说中正义的化身——「海青天」在百姓心中的地位不亚于包拯。",
  "Hai Rui may be Chinese history's most extreme example of official incorruptibility. In 1566, he submitted the 'Memorial on State Security' to the Jiajing Emperor — directly denouncing the emperor's Daoist obsessions and neglect of governance — having already bought his own coffin in anticipation of execution. Jiajing was enraged but spared his life, merely imprisoning him; he was released upon the emperor's death. As a local official, he grew his own vegetables; his purchase of two jin of meat for his mother's birthday became a sensational news item. His radical asceticism made him an awkward fit in officialdom but cemented his status as a folk hero of justice — 'Hai Qingtian' rivaling Bao Zheng in the popular imagination.",
  ["海刚峰", "Hai Gangfeng", "海青天"], ["src-mingshi"], "", 0.85)

p("lin-zexu", "林则徐", "Lin Zexu", 1785, 1850, "qing-dynasty",
  ["名臣", "民族英雄", "清朝"], ["Minister", "National Hero", "Qing Dynasty"],
  "清朝名臣，虎门销烟的指挥者，中国近代「开眼看世界的第一人」。",
  "Qing minister who directed the destruction of opium at Humen; the 'first Chinese to open his eyes to the world' in the modern era.",
  "林则徐被道光皇帝任命为钦差大臣前往广州禁烟。他抵达后迅速行动——收缴英国商人的鸦片两万余箱，在虎门海滩全部销毁（历时23天）。这一壮举使他成为中华民族抵抗外侮的象征——但也成为英国发动鸦片战争的借口。战争失败后他被贬新疆，在伊犁他兴修水利、推广坎儿井——至今新疆仍有「林公渠」。他在广州期间组织翻译西方报刊和书籍——《四洲志》——使他成为近代中国系统了解西方的第一人。",
  "Lin Zexu was appointed Imperial Commissioner and dispatched to Guangzhou to suppress the opium trade. He acted with startling speed — confiscating over 20,000 chests of opium from British merchants and destroying them all on Humen Beach over 23 days. This heroic act made him a national symbol of resistance — and also Britain's casus belli for the Opium War. After China's defeat, he was exiled to Xinjiang, where he built irrigation works and promoted karez wells — 'Lin's Canal' persists to this day. In Guangzhou, he had organized the translation of Western newspapers and books — notably 'A Gazetteer of Four Continents' — making him modern China's first systematic student of the West.",
  ["林元抚", "Lin Yuanfu", "林文忠公"], ["src-qingshigao"], "", 0.9)

p("zeng-guofan", "曾国藩", "Zeng Guofan", 1811, 1872, "qing-dynasty",
  ["名臣", "军事家", "理学家", "清朝"], ["Minister", "Military Leader", "Confucian Scholar", "Qing Dynasty"],
  "清朝中兴名臣，组建湘军平定太平天国，开创洋务运动，其家书影响了数代中国人。",
  "Qing restoration minister who raised the Hunan Army to crush the Taiping Rebellion and launched the Self-Strengthening Movement; his family letters influenced generations.",
  "曾国藩是近代中国最有影响力的人物之一。太平天国运动席卷半壁江山时，他以在籍侍郎身份组建了湘军——一支以乡村儒生为军官、以宗族乡谊为纽带的私人武装——经过十余年血战最终攻克天京。战后他推动洋务运动——设立安庆军械所和江南制造总局、派遣第一批留美幼童。毛泽东和蒋介石都曾深入研究他的著作。他的《曾国藩家书》成为中国家庭教育和个人修养的经典——体现了他「修身齐家治国平天下」的一生。",
  "Zeng Guofan was one of modern China's most influential figures. When the Taiping Rebellion engulfed half the empire, he raised the Hunan Army — a private force officered by rural Confucian scholars and bonded by clan ties — and after over a decade of bloody campaigning, finally captured the Taiping capital at Nanjing. Post-war, he launched the Self-Strengthening Movement — establishing the Anqing Arsenal and Jiangnan Arsenal and dispatching the first cohort of Chinese students to study in America. Both Mao Zedong and Chiang Kai-shek studied his writings deeply. His 'Family Letters of Zeng Guofan' became a classic of Chinese family education and self-cultivation — embodying his lifelong pursuit of 'cultivate the self, regulate the family, govern the state, and bring peace to the world.'",
  ["曾伯涵", "Zeng Bohan", "曾文正公"], ["src-qingshigao"], "", 0.9)

p("zuo-zongtang", "左宗棠", "Zuo Zongtang", 1812, 1885, "qing-dynasty",
  ["名臣", "军事家", "清朝"], ["Minister", "Military Leader", "Qing Dynasty"],
  "清朝中兴名臣，率军收复新疆，与曾国藩、李鸿章、张之洞并称晚清四大名臣。",
  "Qing restoration minister who led the military reconquest of Xinjiang; counted among the 'Four Famous Ministers of the Late Qing.'",
  "左宗棠早年科举不顺，仅中举人，但在太平天国战争中展现出卓越的军事才能。他的最大功绩在年近七旬时完成——当时新疆已被阿古柏侵占十余年，朝廷中李鸿章等人主张放弃，左宗棠力排众议自筹军饷、抬棺出征，率军收复了新疆全境。他还在沿途种植柳树改善生态——被后人称为「左公柳」。他是晚清洋务运动的重要推动者——创办福州船政局和兰州织呢局。",
  "Zuo Zongtang struggled with the imperial examinations, only achieving the provincial juren degree, but displayed exceptional military talent during the Taiping wars. His greatest achievement came near age 70 — Xinjiang had been under Yaqub Beg's occupation for over a decade, and Li Hongzhang and others urged abandonment. Zuo defied them all, raised his own funds, and marched west carrying his coffin — reconquering the entirety of Xinjiang. He planted willows along the route to improve the ecology — 'Zuo's Willows' are remembered to this day. He was a key driver of the Self-Strengthening Movement, founding the Fuzhou Naval Yard and the Lanzhou Woolen Mill.",
  ["左季高", "Zuo Jigao", "左文襄公"], ["src-qingshigao"], "", 0.9)

# ===== 文人 (16) =====
p("qu-yuan", "屈原", "Qu Yuan", -340, -278, "china",
  ["文学家", "诗人", "楚国"], ["Writer", "Poet", "Chu"],
  "中国第一位伟大的诗人，《离骚》的作者，楚国贵族，投汨罗江自尽，端午节即源于对他的纪念。",
  "China's first great poet, author of 'Li Sao' (Encountering Sorrow), a Chu aristocrat who drowned himself; the Dragon Boat Festival commemorates him.",
  "屈原出身楚国贵族，曾任左徒和三闾大夫。他主张联齐抗秦、改革内政，但遭到贵族排挤被流放。在流放中他写下了《离骚》——中国文学史上第一首个人抒情长诗，以香草美人比兴开创了中国诗歌的浪漫主义传统。公元前278年秦将白起攻破楚国都城郢，屈原在绝望中怀抱石头投入汨罗江自尽。百姓划船投粽子以免鱼虾伤害他的遗体——这演变成今天赛龙舟和吃粽子的端午节习俗。",
  "Qu Yuan was a Chu royal clan member who served as Left Minister. He advocated an alliance with Qi against Qin and domestic reform, but was slandered by rivals and exiled. In exile, he composed 'Li Sao' (Encountering Sorrow) — Chinese literature's first long personal lyric poem, inaugurating the romantic tradition with its fragrant-herb-and-beauty allegories. When Qin general Bai Qi captured the Chu capital Ying in 278 BCE, Qu Yuan clasped a stone and drowned himself in the Miluo River. Locals raced boats and threw rice dumplings to keep fish from his body — evolving into today's Dragon Boat Festival customs of racing and eating zongzi.",
  ["屈平", "Qu Ping"], ["src-shiji"], "", 0.85)

p("cao-zhi", "曹植", "Cao Zhi", 192, 232, "three-kingdoms",
  ["文学家", "诗人", "三国"], ["Writer", "Poet", "Three Kingdoms"],
  "三国时期曹魏文学家，曹操之子，「才高八斗」的典故即出自对他的赞誉，七步成诗的故事广为流传。",
  "Cao Wei literary genius and son of Cao Cao; the idiom 'eight dou of talent' originated from praise of him, and the 'seven-step poem' legend endures.",
  "曹植是曹操最宠爱的儿子——他才华横溢，十岁便能诵读诗论辞赋数十万言。在继承权之争中他败给了兄长曹丕，此后备受猜忌和打压。传说曹丕命他在七步内作诗否则处死，他应声吟出「煮豆燃豆萁，豆在釜中泣。本是同根生，相煎何太急」——成为中国文学中最著名的即兴诗篇。他的《洛神赋》以与神女的邂逅表达政治失意和对理想的追求，文辞华丽精美。谢灵运评价「天下才有一石，曹子建独占八斗」——「才高八斗」的成语由此而来。",
  "Cao Zhi was Cao Cao's favorite son — a prodigy who could recite hundreds of thousands of words of poetry and prose by age ten. He lost the succession struggle to his elder brother Cao Pi and spent the rest of his life under suspicion and persecution. Legend says Cao Pi ordered him to compose a poem within seven paces or face execution — he instantly delivered the 'Seven-Step Poem' about burning beanstalks and crying beans: 'Born of the same root, why the rush to burn each other?' — Chinese literature's most famous impromptu verse. His 'Rhapsody of the Luo River Goddess' uses a divine encounter to express political frustration and idealist longing in sumptuous prose. Xie Lingyun praised: 'Of all the world's talent, one dan (ten dou), Cao Zijian alone commands eight dou' — giving us the idiom 'talent of eight dou.'",
  ["曹子建", "Cao Zijian", "陈思王"], ["src-sanguozhi"], "", 0.85)

p("tao-yuanming", "陶渊明", "Tao Yuanming", 365, 427, "china",
  ["文学家", "诗人", "隐士", "东晋"], ["Writer", "Poet", "Recluse", "Eastern Jin"],
  "东晋田园诗人，「不为五斗米折腰」而辞官归隐，《桃花源记》创造了中国文化中永恒的乌托邦。",
  "Eastern Jin pastoral poet who resigned rather than 'bow for five dou of rice'; his 'Peach Blossom Spring' created Chinese culture's eternal utopia.",
  "陶渊明担任彭泽县令仅八十余天——督邮来视察要他束带迎接，他叹道「吾不能为五斗米折腰」，随即辞官归乡。此后二十余年他亲自耕田种菊，写下了中国文学史上最纯粹的田园诗——《归园田居》和《饮酒》二十首——其中的「采菊东篱下，悠然见南山」成为隐逸文化的最高境界。他的散文《桃花源记》描绘了一个躲避战乱的世外桃源——这个意象在此后一千六百年中不断被重述，成为中国人心灵中永远的乌托邦。他的生活态度定义了中国文人的另一条道路——不为仕途所困，在自然中寻找自由。",
  "Tao Yuanming served as magistrate of Pengze county for barely eighty days. When a regional inspector's visit required him to dress formally and kowtow, he sighed 'I cannot bow for five dou of rice' and resigned on the spot. For the next twenty-plus years, he personally farmed and planted chrysanthemums, writing Chinese literature's purest pastoral poetry — 'Returning to Fields and Gardens' and twenty 'Drinking Wine' poems — with lines like 'Plucking chrysanthemums by the eastern hedge, I gaze distantly at the southern mountains' becoming the apogee of reclusive culture. His prose piece 'Peach Blossom Spring,' depicting a hidden utopia of refugees from war, has been retold for 1,600 years as the eternal utopia of the Chinese soul. His life defined an alternative path for Chinese literati — freedom in nature over the shackles of officialdom.",
  ["陶潜", "Tao Qian", "五柳先生"], [], "", 0.85)

p("wang-bo", "王勃", "Wang Bo", 650, 676, "tang-dynasty",
  ["文学家", "诗人", "唐朝"], ["Writer", "Poet", "Tang Dynasty"],
  "初唐四杰之首，《滕王阁序》的作者，「落霞与孤鹜齐飞，秋水共长天一色」为千古名句。",
  "Leader of the Four Paragons of Early Tang, author of 'Preface to the Prince of Teng's Pavilion' with its immortal couplet about sunset clouds and autumn waters.",
  "王勃六岁能文，被誉为神童。他最著名的作品《滕王阁序》是在一次宴会上的即兴创作——主办者本来安排自己的女婿来展示才华，但王勃毫不推辞当众挥毫写下了这篇千古名文。当他写到「落霞与孤鹜齐飞，秋水共长天一色」时，满座惊叹——这两句将黄昏、飞鸟、秋水、长天四种意象融为一幅绝美画面。可惜他年仅26岁就在前往交趾（今越南）探望父亲的途中溺水身亡——留下了文学史上最早的青春陨落传奇之一。",
  "Wang Bo could compose essays at age six, hailed as a child prodigy. His most famous work, 'Preface to the Prince of Teng's Pavilion,' was an impromptu composition at a banquet — the host had planned for his son-in-law to display his talent, but Wang Bo unhesitatingly picked up the brush and delivered this immortal masterpiece on the spot. When he wrote 'Sunset clouds and the solitary duck fly together; autumn waters merge with the vast sky in one hue,' the entire hall gasped — fusing twilight, birds, autumn waters, and sky into a single breathtaking vision. Tragically, he drowned at just 26 while traveling to Jiaozhi (modern Vietnam) to visit his father — one of literary history's earliest legends of youthful genius cut short.",
  ["王子安", "Wang Zian"], ["src-jiutangshu"], "", 0.85)

p("meng-haoran", "孟浩然", "Meng Haoran", 689, 740, "tang-dynasty",
  ["文学家", "诗人", "唐朝", "山水田园"], ["Writer", "Poet", "Tang Dynasty", "Pastoral"],
  "盛唐山水田园诗派代表，与王维并称「王孟」，其清淡自然的诗风影响了后代诗人。",
  "Representative of High Tang's landscape-pastoral poetry, paired with Wang Wei as 'Wang-Meng'; his limpid, natural style influenced generations.",
  "孟浩然终身未仕——这在盛唐诗人中极为罕见。他曾应试不第、在张九龄幕府短暂任职——但他似乎更享受襄阳的田园生活。他结交了当时几乎所有重要诗人——王维、李白（曾写下「吾爱孟夫子，风流天下闻」）、王昌龄。他的《春晓》「春眠不觉晓，处处闻啼鸟」成为每个中国人最早背诵的唐诗之一。但他也有壮志未酬的一面——「欲济无舟楫，端居耻圣明」——只是命运的偶然使他更多地被记住为隐居诗人。",
  "Meng Haoran never held office — exceptionally rare among High Tang poets. He failed the examinations and briefly served on Zhang Jiuling's staff, but seemed to prefer the pastoral life of Xiangyang. He befriended virtually every important poet of the age — Wang Wei, Li Bai (who wrote 'I love Master Meng, his free spirit known throughout the world'), Wang Changling. His 'Spring Dawn' — 'Spring sleep unaware of dawn, everywhere I hear birds singing' — is among the first Tang poems every Chinese child memorizes. Yet he also harbored unfulfilled ambition — 'I long to cross but have no boat; in times of sagely peace I am ashamed to idle' — but circumstance remembered him more as the hermit-poet.",
  ["孟山人", "Meng Haoran"], ["src-jiutangshu"], "", 0.85)

p("du-mu", "杜牧", "Du Mu", 803, 852, "tang-dynasty",
  ["文学家", "诗人", "唐朝", "晚唐"], ["Writer", "Poet", "Tang Dynasty", "Late Tang"],
  "晚唐杰出诗人，与李商隐并称「小李杜」，其咏史怀古诗深沉蕴藉，七绝精妙绝伦。",
  "Outstanding late Tang poet paired with Li Shangyin as 'Little Li-Du'; his historical meditations are profound and his jueju quatrains exquisitely crafted.",
  "杜牧出身名门——祖父杜佑是三朝宰相和《通典》作者。他注《孙子》是影响深远的军事学著作。但诗歌才是他不朽的遗产——《清明》「清明时节雨纷纷，路上行人欲断魂」、《泊秦淮》「商女不知亡国恨，隔江犹唱后庭花」、《阿房宫赋》的华美铺陈——这些作品将历史沉思、现实关怀和个人感伤完美融合。他的七言绝句在唐诗中仅次于李白和王昌龄。樊川别墅是他的隐居之所，后人称他为「杜樊川」。",
  "Du Mu came from an eminent family — his grandfather Du You was a three-reign chancellor and author of the encyclopedic 'Tongdian.' His commentary on Sun Tzu's 'Art of War' is an influential work of military scholarship. But poetry is his immortal legacy — 'Qingming Festival' ('Drizzling rain at Qingming, the traveler's soul near breaking'), 'Moored on the Qinhuai River' ('The singing girl knows not the grief of a fallen kingdom; across the river she still sings the rear-court flower'), the sumptuous 'Rhapsody of Epang Palace' — these works fuse historical meditation, contemporary concern, and personal melancholy with perfect artistry. His seven-character quatrains rank only below Li Bai and Wang Changling in Tang poetry. His retirement villa at Fanchuan gave him the posthumous name 'Du Fanchuan.'",
  ["杜牧之", "Du Muzhi", "杜樊川"], ["src-jiutangshu"], "", 0.85)

p("li-shangyin", "李商隐", "Li Shangyin", 813, 858, "tang-dynasty",
  ["文学家", "诗人", "唐朝", "晚唐"], ["Writer", "Poet", "Tang Dynasty", "Late Tang"],
  "晚唐最杰出的诗人之一，与杜牧并称「小李杜」，其无题诗以朦胧晦涩之美开创了中国诗歌的新境界。",
  "One of the finest late Tang poets, paired with Du Mu as 'Little Li-Du'; his untitled poems with their ambiguous beauty opened new dimensions in Chinese poetry.",
  "李商隐的诗以隐晦朦胧著称——「此情可待成追忆，只是当时已惘然」「春蚕到死丝方尽，蜡炬成灰泪始干」「身无彩凤双飞翼，心有灵犀一点通」这些名句已是中国人情感表达的共同语汇。他一生卷入了牛李党争的政治漩涡——娶了李党要员的女儿却受知于牛党，这种政治上的两难处境使他的一生都在漂泊失意中度过。他的诗大量使用典故和隐喻，将自己的爱情和身世之痛隐藏在层层文字的背后——这种「无题诗」的创造是中国诗歌史上独特的贡献。",
  "Li Shangyin's poetry is celebrated for its ambiguous beauty — lines like 'This feeling could become a memory to cherish, but at the time I was already lost,' 'Spring silkworms spin silk until death; candles weep tears until they turn to ash,' and 'Without the colorful phoenix's paired wings, our hearts communicate through the magic rhino horn' have become part of the shared emotional vocabulary of Chinese speakers. His life was caught in the Niu-Li factional struggle — he married a Li-faction daughter but received patronage from the Niu faction — this political predicament condemned him to a life of wandering disappointment. His poetry employs dense allusions and metaphors, burying personal pain beneath layers of text — his creation of the 'untitled poem' form is a unique contribution to Chinese poetry.",
  ["李义山", "Li Yishan", "玉谿生"], ["src-jiutangshu"], "", 0.85)

p("liu-zongyuan", "柳宗元", "Liu Zongyuan", 773, 819, "tang-dynasty",
  ["文学家", "哲学家", "唐朝", "古文运动"], ["Writer", "Philosopher", "Tang Dynasty", "Classical Prose"],
  "唐代古文运动领袖之一，与韩愈并称「韩柳」，《永州八记》开创了中国山水散文的传统。",
  "Co-leader of the Tang Classical Prose Movement with Han Yu; his 'Eight Records of Yongzhou' pioneered the Chinese landscape essay tradition.",
  "柳宗元少年成名，21岁中进士。参与「永贞革新」失败后被贬永州十年、再贬柳州四年，最终病死于柳州任上——年仅47岁。政治上的失意反而成就了他的文学——在永州的山水间他写下了《永州八记》，以精炼优雅的散文将个人心境融于自然景观的描写之中，开创了中国山水游记的传统。他还撰写了《捕蛇者说》《三戒》等寓言名篇，《封建论》则是中国政治思想史上的重要著作。贬谪之苦贯穿了他的人生——但他的文字从未被苦难压垮。",
  "Liu Zongyuan earned the jinshi degree at 21. After the failed Yongzhen Reform, he was banished to Yongzhou for ten years, then to Liuzhou for four — dying at his post at just 47. Political failure paradoxically birthed his literary legacy — in Yongzhou's landscapes he wrote the 'Eight Records of Yongzhou,' fusing personal sentiment with natural description in crystalline prose, pioneering the Chinese landscape essay. He also wrote famous allegories like 'The Snake Catcher' and 'Three Precepts,' while his 'On Feudalism' is an important text in Chinese political thought. Exile defined his life — but his writing was never crushed by suffering.",
  ["柳子厚", "Liu Zihou", "柳河东", "柳柳州"], ["src-jiutangshu"], "", 0.85)

p("lu-you", "陆游", "Lu You", 1125, 1210, "song-dynasty",
  ["文学家", "诗人", "南宋", "爱国"], ["Writer", "Poet", "Southern Song", "Patriot"],
  "中国文学史上留存诗作最多的诗人，一生9000余首诗，以收复中原的爱国情怀贯穿始终。",
  "The most prolific poet in Chinese literary history with over 9,000 surviving poems, his lifelong theme was the patriotic dream of recovering the lost north.",
  "陆游活了85岁写了超过九千首诗——在古代世界这几乎是不可想象的数字。他与表妹唐婉的爱情悲剧——被迫休妻后在沈园重逢时写下《钗头凤》——是宋词中最令人心碎的爱情词。但占据他诗歌绝大部分的是对收复中原的渴望——「王师北定中原日，家祭无忘告乃翁」是他临终前的绝笔。他年轻时曾在抗金前线军中任职，这段经历成为他一生反复吟咏的素材——至死他都相信自己曾见到的北伐终将实现。",
  "Lu You lived 85 years and wrote over 9,000 poems — an almost unimaginable corpus in the pre-modern world. His tragic love for his cousin Tang Wan — forced to divorce her, then encountering her years later at Shen Garden and writing 'Phoenix Hairpin' — produced some of the most heartbreaking love lyrics in the Song ci tradition. But the overwhelming theme of his poetry was the dream of recovering the lost north from the Jurchen — his deathbed poem reads: 'When the royal armies finally reclaim the Central Plains, do not forget to tell your father at the family rites.' As a young man he served at the anti-Jurchen front — this experience became the inexhaustible wellspring of his lifelong verse — he died believing the northern expedition he had witnessed would one day succeed.",
  ["陆务观", "Lu Wuguan", "放翁"], ["src-ss"], "", 0.9)

p("xin-qiji", "辛弃疾", "Xin Qiji", 1140, 1207, "song-dynasty",
  ["文学家", "词人", "南宋", "军事", "爱国"], ["Writer", "Ci Poet", "Southern Song", "Military", "Patriot"],
  "南宋最伟大的豪放派词人，也是能带兵打仗的将军，其词雄浑豪迈被誉为「词中之龙」。",
  "Southern Song's greatest heroic-style ci poet who was also a battle-hardened general; his powerful lyrics earned him the epithet 'Dragon among Ci Poets.'",
  "辛弃疾可能是中国文学史上最独特的诗人——他不仅写诗词，还亲率五十骑冲入五万人的金军大营生擒叛徒全身而退。他出生于金国统治下的山东，22岁起义南归宋朝。但南宋朝廷主和派当权，他的北伐主张始终不被采纳——他在江西上饶的带湖隐居了二十余年。在「却将万字平戎策，换得东家种树书」的无奈中，他将满腔壮志化为雄浑悲壮的词章——《永遇乐·京口北固亭怀古》被后世评为辛词第一。他与苏轼并称「苏辛」——但苏轼从未上过战场，而辛弃疾的豪放是刀头舐血的真豪放。",
  "Xin Qiji may be the most unique poet in Chinese literary history — he not only wrote lyrics but personally led fifty riders into a Jurchen camp of fifty thousand to capture a traitor and escape unscathed. Born in Shandong under Jurchen rule, he rebelled at 22 and fled south to Song. But the peace faction dominated the Southern Song court, and his advocacy for northern campaigns was never heeded — he spent over twenty years in forced retirement at Daihu in Jiangxi. In the frustration of 'exchanging ten thousand words of war strategy for the neighbor's tree-planting manual,' he channeled his thwarted ambition into heroic, tragic verse — his 'Joy of Eternal Union: Thoughts on the Past at Beigu Pavilion' is ranked his greatest work. He and Su Shi are coupled as 'Su-Xin' — but Su Shi never saw a battlefield; Xin Qiji's heroism was forged in real blood and steel.",
  ["辛幼安", "Xin You'an", "稼轩"], ["src-ss"], "", 0.9)

p("guan-hanqing", "关汉卿", "Guan Hanqing", 1234, 1300, "china",
  ["文学家", "戏剧家", "元朝"], ["Writer", "Playwright", "Yuan Dynasty"],
  "元曲四大家之首，《窦娥冤》的作者，中国戏剧史上最伟大的剧作家，比莎士比亚早三个世纪。",
  "The foremost of the Four Masters of Yuan Drama, author of 'The Injustice to Dou E,' China's greatest playwright, predating Shakespeare by three centuries.",
  "关汉卿在元朝——一个对汉族文人极不友好的时代——选择了一条独特的道路：他混迹于勾栏瓦舍，与艺人和妓女为友，自称「普天下郎君领袖，盖世界浪子班头」。他以惊人的多产——创作了六十余部杂剧——成为中国戏剧的奠基人。他最著名的作品《窦娥冤》讲述一个善良女子被冤杀的故事——窦娥临刑前发下的三桩誓愿（血溅白练、六月飞雪、大旱三年）成为世界戏剧史上最震撼人心的抗议之一。他的戏剧创作比莎士比亚早了三百年——两人在人文关怀和对社会不公的批判上惊人地相似。",
  "Guan Hanqing, in the Yuan dynasty — an era deeply hostile to Han literati — chose a unique path: he immersed himself in the entertainment quarters, befriending performers and courtesans, calling himself 'the leader of all the realm's gallants, the chief of the world's libertines.' With astonishing productivity — over sixty zaju plays — he became the founder of Chinese drama. His most famous work, 'The Injustice to Dou E,' tells of an innocent woman wrongly executed — her three dying curses (blood spraying onto white silk, snow falling in June, three years of drought) are among the most powerful protests in world drama. He wrote three centuries before Shakespeare — yet the two share a remarkable affinity in their humanism and critiques of social injustice.",
  ["已斋叟", "Guan Yizhai"], [], "", 0.8)

p("wang-xizhi", "王羲之", "Wang Xizhi", 303, 361, "china",
  ["书法家", "文学家", "东晋"], ["Calligrapher", "Writer", "Eastern Jin"],
  "中国历史上最伟大的书法家，被尊为「书圣」，《兰亭序》被誉为天下第一行书。",
  "The greatest calligrapher in Chinese history, revered as the 'Sage of Calligraphy'; his 'Preface to the Orchid Pavilion' is acclaimed as the finest running-script work ever.",
  "王羲之出身东晋的顶级门阀——琅琊王氏。他师从卫夫人学习书法，但最终超越了所有前人——他兼善隶、草、楷、行各体，尤其以行书和草书冠绝古今。353年上巳节，他与谢安、孙绰等41位名士在会稽山阴的兰亭曲水流觞、饮酒赋诗，微醺中他用蚕茧纸和鼠须笔写下了《兰亭集序》——这篇28行324字的作品不仅是文学名篇，更是中国书法史上无可争议的最高峰。后世唐太宗对它痴迷到死后将其陪葬——我们今天看到的都是摹本。他的第七子王献之也是杰出的书法家，与其父并称「二王」。",
  "Wang Xizhi was born into the Eastern Jin's top aristocratic clan — the Langya Wangs. He studied calligraphy under Lady Wei but ultimately surpassed all predecessors, mastering clerical, cursive, regular, and running scripts — his running and cursive scripts are considered unsurpassable. On the Spring Purification Festival of 353, he and 41 luminaries including Xie An and Sun Chuo gathered at the Orchid Pavilion for a poetry-and-wine gathering beside a winding stream. Slightly tipsy, using silkworm-cocoon paper and a rat-whisker brush, he wrote the 'Preface to the Orchid Pavilion Collection' — 324 characters in 28 lines that is not only a literary masterpiece but also the undisputed pinnacle of Chinese calligraphy. Emperor Taizong of Tang was so obsessed with it that he had it buried in his tomb — what we see today are all copies. Wang's seventh son, Wang Xianzhi, was also an outstanding calligrapher; together they are known as the 'Two Wangs.'",
  ["王逸少", "Wang Yishao", "王右军"], [], "", 0.85)

p("wu-chengen", "吴承恩", "Wu Cheng'en", 1506, 1582, "ming-dynasty",
  ["文学家", "小说家", "明朝"], ["Writer", "Novelist", "Ming Dynasty"],
  "明代小说家，《西游记》的作者，创造了中国文化中最家喻户晓的神魔世界。",
  "Ming novelist, author of 'Journey to the West,' creating the most universally recognized mythological world in Chinese culture.",
  "吴承恩一生科场蹭蹬——直到中年才考取岁贡生，晚年做过几年小官便辞官归乡。但他的《西游记》已经成为中国文化最重要的支柱之一——孙悟空、猪八戒、沙僧和白龙马保护唐僧西天取经的故事融入了每个中国人的童年记忆。这部百回神魔小说将佛教朝圣、道教仙术和民间传说编织成一个精彩绝伦的冒险故事——而孙悟空反抗天庭大闹天宫的章节更是中国文化中对权威最淋漓尽致的嘲讽。吴承恩在一个政治上倍感压抑的时代，通过想象力的极致张扬达到了超越。",
  "Wu Cheng'en's examination career was a string of failures — he only obtained the lowest degree in middle age, holding minor posts briefly before retiring in frustration. Yet his 'Journey to the West' became one of the foundational pillars of Chinese culture — the story of Sun Wukong, Zhu Bajie, Sha Seng, and the White Dragon Horse escorting the monk Xuanzang to fetch Buddhist scriptures has entered every Chinese child's memory. This hundred-chapter mythological novel weaves Buddhist pilgrimage, Daoist sorcery, and folk legend into a dazzling adventure — and Sun Wukong's rampage against Heaven's celestial bureaucracy remains Chinese culture's most exuberant mockery of authority. In a politically stifling era, Wu Cheng'en achieved transcendence through the ultimate liberation of imagination.",
  ["吴汝忠", "Wu Ruzhong"], ["src-mingshi"], "", 0.8)

# ===== 科学家 (10) =====
p("cai-lun", "蔡伦", "Cai Lun", 61, 121, "han-dynasty",
  ["科学家", "发明家", "汉朝"], ["Scientist", "Inventor", "Han Dynasty"],
  "东汉宦官，105年改进了造纸术并使其实用化，这项发明彻底改变了人类文明的进程。",
  "Eastern Han eunuch who refined papermaking into a practical technology in 105 CE, an invention that fundamentally altered the course of human civilization.",
  "蔡伦是汉和帝时期的宦官，官至尚方令——掌管宫廷器物制作。在他之前中国已有原始纸张（以麻纤维制造），但粗糙、昂贵、不宜书写。蔡伦于105年改进了造纸工艺——使用树皮、麻头、破布和旧渔网等廉价材料，通过打浆、抄纸、晾干等工序制造出轻薄、平滑、适于书写的纸张。他的造纸术在几百年间从中国传到阿拉伯世界再到欧洲——古登堡印刷术的出现正是建立在纸的普遍可得之上。造纸术被列为中国古代四大发明之一。",
  "Cai Lun was a eunuch serving Emperor He of Han, rising to Director of Imperial Workshops. Before him, rudimentary paper existed in China (made from hemp), but it was coarse, expensive, and unsuitable for writing. In 105 CE, Cai Lun refined the process — using tree bark, hemp waste, rags, and old fishing nets as cheap raw materials, pulping, sheet-forming, and drying to produce thin, smooth, writable paper. His papermaking technology spread over centuries from China to the Islamic world and then to Europe — Gutenberg's printing press was built on the widespread availability of paper. Papermaking is counted among China's Four Great Inventions.",
  ["蔡敬仲", "Cai Jingzhong"], ["src-hanshu"], "", 0.85)

p("zhang-zhongjing", "张仲景", "Zhang Zhongjing", 150, 219, "han-dynasty",
  ["医学家", "科学家", "汉朝"], ["Physician", "Scientist", "Han Dynasty"],
  "东汉医学家，被尊为「医圣」，《伤寒杂病论》奠定了中医临床诊疗体系的基础。",
  "Eastern Han physician honored as the 'Sage of Medicine'; his 'Treatise on Cold-Damage Disorders' established the foundation of clinical Chinese medicine.",
  "张仲景生活在东汉末年——瘟疫频发，他的家族二百余人不到十年死了三分之二，其中七成死于伤寒。这促使他毕生钻研医学、勤求古训、博采众方，最终写出《伤寒杂病论》——这是中国医学史上第一部理法方药兼备的临床专著。他首创了六经辨证体系——将外感热病的发展按照太阳、少阳、阳明、太阴、少阴、厥阴六个阶段进行辨证论治。他书中的方剂至今仍广泛应用于临床——被称为「经方」。他的医学贡献在中国医学史上的地位可以比肩希波克拉底在西方医学中的地位。",
  "Zhang Zhongjing lived in the late Eastern Han era of rampant epidemics. Of his clan of over 200, two-thirds died within a decade, seven in ten from cold-damage fevers. This drove his lifelong dedication to medicine, and after exhaustive study of ancient texts and collection of diverse prescriptions, he completed the 'Treatise on Cold-Damage and Miscellaneous Disorders' — China's first clinical text with complete theory, methodology, formulas, and pharmacology. He pioneered the Six-Channel Pattern Identification system, classifying febrile disease progression through six stages. His formulas remain in widespread clinical use today, known as 'classical prescriptions.' His stature in Chinese medicine parallels Hippocrates in Western medicine.",
  ["张机", "Zhang Ji", "医圣"], [], "", 0.85)

p("hua-tuo", "华佗", "Hua Tuo", 145, 208, "han-dynasty",
  ["医学家", "科学家", "汉朝"], ["Physician", "Scientist", "Han Dynasty"],
  "东汉神医，发明麻沸散——世界最早的麻醉药，创立五禽戏养生功法，被曹操处死。",
  "Eastern Han divine physician who invented mafeisan, the world's earliest anesthetic, and created the Five Animal Frolics; executed by Cao Cao.",
  "华佗是中国古代最著名的外科医师——他发明了麻沸散（以曼陀罗花等药物制成的麻醉剂），比西方最早的麻醉术早了约1600年。他在麻醉下进行腹部手术的记载令后世惊叹。他还创立了五禽戏——模仿虎、鹿、熊、猿、鸟五种动物的动作来强身健体——这是中国最早的健身体系之一。当曹操的头风病发作时召华佗诊治，华佗建议开颅手术——曹操认为这是谋害的借口将他处死。传说华佗在狱中将毕生医术写成《青囊书》交予狱卒，但狱卒不敢收——华佗将其付之一炬，中国医学史上的巨大损失。",
  "Hua Tuo was ancient China's most famous surgeon. He invented mafeisan — an anesthetic made from datura and other herbs — predating Western anesthesia by roughly 1,600 years. Records of his abdominal surgeries performed under anesthesia have astonished later generations. He also created the Five Animal Frolics — mimicking the movements of tiger, deer, bear, monkey, and crane for health and longevity — one of China's earliest exercise systems. When Cao Cao's chronic headaches flared, he summoned Hua Tuo, who proposed trepanation — Cao Cao suspected assassination and executed him. Legend says in prison Hua Tuo wrote his life's medical knowledge into the 'Green Satchel Classic' and offered it to the jailer, who dared not accept it — whereupon Hua Tuo burned it, an incalculable loss to Chinese medicine.",
  ["华元化", "Hua Yuanhua", "神医华佗"], ["src-sanguozhi"], "", 0.75)

p("zu-chongzhi", "祖冲之", "Zu Chongzhi", 429, 500, "china",
  ["科学家", "数学家", "天文学家", "南北朝"], ["Scientist", "Mathematician", "Astronomer", "Southern Dynasties"],
  "南北朝时期数学家，将圆周率精确到小数点后第七位——这一记录保持了近千年。",
  "Southern Dynasties mathematician who calculated pi to seven decimal places — a record that stood for nearly a millennium.",
  "祖冲之生活的南北朝是中国历史上政治最动荡的时期之一——但他献身于科学与数学。他最大的成就是将圆周率计算到了3.1415926到3.1415927之间——这一精度直到近一千年后才被阿拉伯数学家打破。他还给出了两个分数近似值：密率355/113和约率22/7。在他的《大明历》中，他精确计算了回归年长度为365.2428天——与现代值仅差约50秒。他的儿子祖暅之也是数学家，父子二人在球体体积计算上的贡献（祖暅原理）比意大利数学家卡瓦列里的类似发现早了一千多年。",
  "Zu Chongzhi lived during one of China's most politically turbulent eras, the Southern and Northern Dynasties — but he devoted himself to science and mathematics. His greatest achievement was calculating pi to between 3.1415926 and 3.1415927 — a precision not surpassed until Arab mathematicians achieved it nearly a thousand years later. He also provided two fractional approximations: the precise 355/113 and the rough 22/7. In his 'Da Ming Calendar,' he calculated the tropical year as 365.2428 days — only about 50 seconds off the modern value. His son Zu Gengzhi was also a mathematician; their work on sphere volume (Zu Gengzhi's Principle) predated Cavalieri's similar discovery by over a millennium.",
  ["祖文远", "Zu Wenyuan"], [], "", 0.85)

p("bi-sheng", "毕昇", "Bi Sheng", 972, 1051, "song-dynasty",
  ["科学家", "发明家", "宋朝"], ["Scientist", "Inventor", "Song Dynasty"],
  "北宋发明家，发明了活字印刷术——比古登堡早了约四百年，是印刷史上的革命性突破。",
  "Northern Song inventor who created movable-type printing roughly four centuries before Gutenberg — a revolutionary breakthrough in printing history.",
  "关于毕昇的生平我们知之甚少——沈括在《梦溪笔谈》中的一段记载是几乎唯一的资料来源。毕昇以胶泥制作单个字模，用火烧硬后按韵排列在木格中。排版时在铁板上敷以松脂蜡和纸灰，将字模排列其上后用火烘烤使蜡稍融，再用平板压平字面——冷却后字模便牢固地固定住。印完后加热取下字模可重复使用。这一发明的天才之处在于将整版雕刻变为单个活字的循环使用——大幅降低了印刷成本。虽然由于汉字数量庞大活字印刷在中国未全面取代雕版印刷，但这一思想传到欧洲后与字母文字完美结合，引发了传播革命。",
  "We know almost nothing of Bi Sheng's life — Shen Kuo's brief account in 'Dream Pool Essays' is virtually our only source. Bi Sheng carved individual characters in clay, fired them hard, and arranged them by rhyme in wooden cases. To print, he spread pine resin, wax, and paper ash on an iron plate, arranged the type, heated the plate to soften the wax, and pressed with a flat board — when cool, the type was firmly fixed. After printing, heating released the type for reuse. The genius was transforming block-carving into reusable individual characters — dramatically reducing printing costs. Though the vast number of Chinese characters prevented movable type from fully replacing block printing in China, the idea transmitted to Europe and, combined with alphabetic scripts, sparked a communications revolution.",
  ["毕升", "Bi Sheng"], ["src-ss"], "", 0.8)

p("guo-shoujing", "郭守敬", "Guo Shoujing", 1231, 1316, "yuan-dynasty",
  ["科学家", "天文学家", "水利学家", "元朝"], ["Scientist", "Astronomer", "Hydraulic Engineer", "Yuan Dynasty"],
  "元朝天文学家和水利学家，《授时历》的主要编制者，其天文观测精度达到了古代世界的巅峰。",
  "Yuan dynasty astronomer and hydraulic engineer, principal author of the Shoushi Calendar, whose astronomical observations achieved ancient world's peak precision.",
  "郭守敬是古代中国最伟大的实测天文学家。忽必烈任命他主持历法改革后，他在全国范围内设立了27个观测站——东至高丽西至云南南至南海北至铁勒。他设计制造了多种精密的天文仪器——简仪、高表、候极仪——用以测量天体位置和影长。他编制的《授时历》以365.2425天为一年——与现行格里高利历完全相同但早了三个世纪。他还是一位卓越的水利工程师——主持修建了通惠河，使京杭大运河全线贯通直达大都（北京）城内的积水潭。",
  "Guo Shoujing was ancient China's greatest observational astronomer. When Kublai Khan appointed him to reform the calendar, he established 27 observation stations across the empire — from Korea in the east to Yunnan in the west, from the South China Sea to the Tiele tribes in the north. He designed and built precision astronomical instruments — the simplified armillary sphere, the gnomon, and the polar-height instrument. His 'Shoushi Calendar' computed the year as 365.2425 days — identical to the modern Gregorian calendar but three centuries earlier. He was also a distinguished hydraulic engineer, supervising the Tonghui River project that completed the Grand Canal's direct access into Dadu (Beijing), reaching all the way to the Jishuitan lake within the capital.",
  ["郭若思", "Guo Ruosi"], ["src-yuanshi"], "", 0.85)

p("song-yingxing", "宋应星", "Song Yingxing", 1587, 1666, "ming-dynasty",
  ["科学家", "百科全书家", "明朝"], ["Scientist", "Encyclopedist", "Ming Dynasty"],
  "明末科学家，《天工开物》的作者——中国第一部综合性工业技术百科全书，被誉为十七世纪的工艺百科全书。",
  "Late Ming scientist, author of 'Tiangong Kaiwu' — China's first comprehensive encyclopedia of industrial technology, hailed as the 'technological encyclopedia of the 17th century.'",
  "宋应星在明朝灭亡的动荡中度过了一生。他五次会试不第之后放弃了科举仕途，转而投身于对生产技术的系统记录。1637年他完成了《天工开物》——一部涵盖了农业、纺织、陶瓷、冶金、造纸、造船、兵器制造等三十多个工业门类的百科全书。书中有123幅精美插图详细展示了各种生产设备和工艺流程——这是中国科技史上独一无二的视觉技术文献。他坚持「此书于功名进取毫不相关也」——在一个以科举为正途的时代，他将自己的才智献给了被士大夫视为「奇技淫巧」的实用技术。",
  "Song Yingxing lived through the collapse of the Ming dynasty. After failing the metropolitan examination five times, he abandoned the path of official advancement and devoted himself to systematically documenting productive technologies. In 1637, he completed 'Tiangong Kaiwu' (The Exploitation of the Works of Nature) — an encyclopedia covering over thirty industrial categories including agriculture, textiles, ceramics, metallurgy, papermaking, shipbuilding, and weapons manufacturing. The book features 123 exquisite illustrations detailing equipment and processes — a unique visual technological document in Chinese history. He insisted that 'this book has nothing to do with official advancement' — in an era when the examination ladder was the only respectable path, he devoted his intellect to practical technologies that scholar-officials dismissed as 'trifling tricks.'",
  ["宋长庚", "Song Changgeng"], [], "", 0.85)

# ===== 谋士/战略家 (8) =====
p("jiang-ziya", "姜子牙", "Jiang Ziya (Jiang Taigong)", -1128, -1015, "china",
  ["谋士", "战略家", "政治家", "周朝"], ["Strategist", "Statesman", "Zhou Dynasty"],
  "周朝开国元勋，辅佐周文王和周武王灭商，「太公钓鱼愿者上钩」是中国文化中最经典的求贤典故。",
  "Founding strategist of Zhou who aided Kings Wen and Wu in overthrowing Shang; the 'Grand Duke fishing with a straight hook' is Chinese culture's enduring emblem of waiting for the right lord.",
  "姜子牙的早年充满传奇——据说他曾在商朝做小官、卖过面粉、屠过牛，但直到72岁在渭水边用直钩钓鱼时才被周文王发现。「太公钓鱼愿者上钩」的故事成为此后三千年中国文化中贤臣待明主的永恒象征。他被尊为「太公望」——文王祖父太公所盼望的贤人。他辅佐武王伐纣——在牧野之战中以少胜多灭亡了商朝。他被封于齐国，是齐国的开国君主。《六韬》这部兵书以他为名——虽然实际成书于战国时代——被后人列入《武经七书》。",
  "Jiang Ziya's early life is shrouded in legend — he supposedly served as a minor Shang official, sold flour, butchered oxen — and was not discovered until age 72, when King Wen of Zhou found him fishing at the Wei River with a straight hook. The tale of 'Grand Duke fishing — those who wish take the bait' became the eternal symbol of the worthy minister awaiting his destined lord. He was honored as 'Tai Gong Wang' — the worthy man longed for by King Wen's grandfather. He helped King Wu overthrow the Shang, achieving victory against superior numbers at the Battle of Muye. Enfeoffed in Qi, he became its founding ruler. The military treatise 'Six Secret Teachings' bears his name — though actually compiled in the Warring States period — and was later included in the 'Seven Military Classics.'",
  ["姜尚", "吕尚", "太公望", "Jiang Shang", "Lu Shang", "Tai Gong Wang"], [], "", 0.7)

p("sima-yi", "司马懿", "Sima Yi", 179, 251, "three-kingdoms",
  ["谋士", "战略家", "三国", "军事家"], ["Strategist", "Commander", "Three Kingdoms"],
  "三国时期曹魏权臣和军事家，以超乎常人的隐忍和谋略著称，终其一生为司马氏篡魏奠定基础。",
  "Cao Wei statesman and military strategist famed for superhuman patience and cunning; his lifetime of maneuvering laid the groundwork for the Sima clan's usurpation.",
  "司马懿可能是三国最被低估的战略家。他辅佐曹魏四代——曹操、曹丕、曹叡、曹芳。在与诸葛亮的五次北伐对阵中他以坚守不战的策略拖垮了对手——即使诸葛亮送来女人衣服羞辱他也依然按兵不动。他的政治手腕比军事才能更为可怕——他隐藏野心数十年，甚至在曹爽派人探查时假装中风流涎——然后在249年发动高平陵之变一举铲除曹爽集团。此后曹魏政权名存实亡。他的隐忍和权谋深刻地塑造了中国政治文化——「司马懿之心」已成为深不可测的代名词。",
  "Sima Yi may be the Three Kingdoms' most underrated strategist. He served four generations of Cao Wei — Cao Cao, Cao Pi, Cao Rui, and Cao Fang. Against Zhuge Liang's five northern campaigns, his strategy of refusing battle exhausted his opponent — even when Zhuge sent him women's clothing as an insult, he stayed within his fortifications. His political cunning surpassed even his military skill — he concealed his ambition for decades, even faking a stroke and drooling when Cao Shuang sent an agent to check on him — then struck in the 249 Gaoping Tombs coup, eliminating the Cao Shuang faction in one stroke. Thereafter Cao Wei was an empty shell. His patience and craft fundamentally shaped Chinese political culture — 'Sima Yi's true intentions' is a byword for unfathomable calculation.",
  ["司马仲达", "Sima Zhongda"], ["src-sanguozhi"], "", 0.85)

p("zhou-yu", "周瑜", "Zhou Yu", 175, 210, "three-kingdoms",
  ["谋士", "军事家", "三国", "东吴"], ["Strategist", "Commander", "Three Kingdoms", "Eastern Wu"],
  "东吴名将，赤壁之战中联合刘备大破曹操，风姿卓越「曲有误周郎顾」，但英年早逝于36岁。",
  "Eastern Wu's celebrated commander who defeated Cao Cao at Red Cliffs; famed for elegance — 'if a note was wrong, Zhou Yu would glance back' — but died young at 36.",
  "周瑜是三国时代最具魅力的将领之一——他精通音律（据说宴会上有人故意弹错曲子让他回头）、姿貌俊美、与孙策为至交好友一同娶了大小乔姐妹。208年曹操率大军南下时他力排朝中投降之议，与诸葛亮联手在赤壁以火攻大败曹军——这场战役奠定了三分天下的格局。但他在准备进攻益州时在巴丘病逝，年仅36岁。《三国演义》将他改写为嫉恨诸葛亮、最终被气死的形象——这个虚构极大地扭曲了历史中这位才华横溢而豁达大度的儒将。",
  "Zhou Yu was among the Three Kingdoms' most charismatic commanders — a connoisseur of music (legend says guests at banquets would deliberately play wrong notes to catch his glance), strikingly handsome, and sworn brother to Sun Ce, the two marrying the Qiao sisters together. In 208, when Cao Cao's armada descended, Zhou Yu overrode the court's capitulation faction and, with Zhuge Liang, annihilated Cao's forces with fire at Red Cliffs — the battle that cemented the tripartite balance. But before he could launch his planned conquest of Yi Province, he fell ill and died at Baqiu, at just 36. 'Romance of the Three Kingdoms' recast him as consumed by jealousy of Zhuge Liang and literally angered to death — a fabrication that grotesquely distorts the historical Zhou Yu, who was brilliant and magnanimous.",
  ["周郎", "Zhou Lang", "周公瑾", "Zhou Gongjin"], ["src-sanguozhi"], "", 0.85)

p("guo-jia", "郭嘉", "Guo Jia", 170, 207, "three-kingdoms",
  ["谋士", "战略家", "三国"], ["Strategist", "Three Kingdoms"],
  "曹操最倚重的谋士之一，以精准的预判著称——官渡之战前预言袁绍必败，其早逝令曹操痛惜「哀哉奉孝」。",
  "One of Cao Cao's most trusted strategists, famed for devastatingly accurate predictions — foretold Yuan Shao's defeat before Guandu; his early death left Cao Cao grieving 'Alas, Fengxiao!'",
  "郭嘉在荀彧的推荐下加入曹操阵营，很快成为最受信任的谋士。官渡之战前他提出著名的「十胜十败论」从十个方面分析曹操必能战胜兵力远胜于己的袁绍——后来的战局完全印证了他的预判。他建议曹操远征乌桓消除北方边患——曹操采纳后在白狼山大胜，但郭嘉在这次远征中染病去世，年仅38岁。赤壁之战大败后曹操痛哭：「郭奉孝在，不使孤至此」——这可能是曹操一生中最高的赞誉。",
  "Guo Jia joined Cao Cao on Xun Yu's recommendation and quickly became the most trusted advisor. Before the Guandu campaign, he presented the famous 'Ten Advantages and Ten Weaknesses' analysis, arguing from every dimension why Cao Cao would defeat the numerically superior Yuan Shao — subsequent events vindicated every point. He advised Cao Cao's expedition against the Wuhuan tribes to secure the northern frontier — Cao Cao won decisively at White Wolf Mountain, but Guo Jia fell ill on the campaign and died at 38. After the catastrophic defeat at Red Cliffs, Cao Cao wept: 'Had Guo Fengxiao been alive, I would not have come to this' — possibly the highest praise of his life.",
  ["郭奉孝", "Guo Fengxiao"], ["src-sanguozhi"], "", 0.8)

p("pang-tong", "庞统", "Pang Tong", 179, 214, "three-kingdoms",
  ["谋士", "战略家", "三国", "蜀汉"], ["Strategist", "Three Kingdoms", "Shu Han"],
  "与诸葛亮并称「卧龙凤雏」的谋士，为刘备献上取益州的上中下三计，攻雒城时中箭身亡年仅36岁。",
  "Strategist paired with Zhuge Liang as 'Crouching Dragon and Fledgling Phoenix,' who offered Liu Bei three strategies for conquering Yi Province; died from an arrow at Luo at 36.",
  "庞统貌不惊人——孙权最初因为他长相而轻视他——但他的战略头脑与诸葛亮齐名。鲁肃评价他「非百里之才」。投奔刘备后他随军入蜀，在涪城向刘备提出了夺取益州的上中下三策——刘备采取了中策回师攻取成都。但在围攻雒城的战斗中庞统被流矢射死——「凤雏」陨落于落凤坡，名字与命运的巧合令时人唏嘘。他的早逝和诸葛亮的早逝一样——是蜀汉无法弥补的损失。",
  "Pang Tong was unprepossessing in appearance — Sun Quan initially dismissed him for his looks — but his strategic mind rivaled Zhuge Liang. Lu Su assessed he was 'no talent for a mere hundred-li district.' After joining Liu Bei, he accompanied the invasion of Yi Province and presented three strategies — upper, middle, lower — for seizing Chengdu; Liu Bei chose the middle path and succeeded. But during the siege of Luo, Pang Tong was shot by an arrow — the 'Fledgling Phoenix' fell at Fallen Phoenix Slope, a haunting coincidence of name and fate. Like Zhuge Liang's premature death, Pang Tong's loss was irreplaceable for Shu Han.",
  ["庞士元", "Pang Shiyuan", "凤雏"], ["src-sanguozhi"], "", 0.8)

p("xun-yu", "荀彧", "Xun Yu", 163, 212, "three-kingdoms",
  ["谋士", "战略家", "三国", "政治家"], ["Strategist", "Statesman", "Three Kingdoms"],
  "曹操的首席谋臣，被称为「吾之子房」，为曹操推荐了郭嘉、司马懿等大批人才，因反对称帝被赐死。",
  "Cao Cao's chief strategist, called 'my Zifang (Zhang Liang),' who recruited Guo Jia, Sima Yi, and many others; forced to suicide for opposing Cao Cao's imperial ambitions.",
  "荀彧是颍川荀氏的杰出代表——这是东汉三国时期最负盛名的士族之一。他29岁投奔曹操后迅速成为其最重要的战略顾问——曹操称赞他为「吾之子房」（把荀彧比作刘邦的张良）。官渡之战期间他在后方稳定局势、保障后勤补给。他最大的贡献是为曹操推荐了庞大的谋士团队——郭嘉、司马懿、钟繇、陈群等都出自他的举荐。但当曹操日益显露称帝野心时，荀彧——内心仍忠于汉室——坚决反对。212年曹操派人送给他一个空食盒——这是一道无声的死亡命令——荀彧服毒自尽。",
  "Xun Yu was the preeminent scion of the Yingchuan Xun clan — one of the most prestigious aristocratic families of the late Han. Joining Cao Cao at 29, he quickly became the paramount strategic advisor — Cao Cao praised him as 'my Zifang' (likening him to Liu Bang's Zhang Liang). During the Guandu campaign, he stabilized the rear and secured logistics. His greatest contribution was recruiting an extraordinary team of advisors for Cao Cao — Guo Jia, Sima Yi, Zhong Yao, Chen Qun, and others all entered service through his recommendation. But as Cao Cao's imperial ambitions grew unmistakable, Xun Yu — still loyal to the Han in his heart — stood in opposition. In 212, Cao Cao sent him an empty food container — a silent death order — and Xun Yu drank poison.",
  ["荀文若", "Xun Wenruo"], ["src-sanguozhi"], "", 0.85)

p("jia-xu", "贾诩", "Jia Xu", 147, 223, "three-kingdoms",
  ["谋士", "战略家", "三国"], ["Strategist", "Three Kingdoms"],
  "三国时期最精准的战略预言者——被称为「毒士」，数次改换门庭却总能全身而退并活到77岁善终。",
  "The Three Kingdoms' most devastatingly accurate strategic prophet — called 'the Venomous Adviser' — repeatedly changed masters yet always extricated himself, living to 77.",
  "贾诩可能是三国时期生存智慧最高的人。他最早建议李傕郭汜反攻长安导致天下大乱——有人说「文和乱武」是他的罪。但他随后离开李傕投靠段煨和张绣——在张绣帐下他两次献策大败曹操，让曹操失去了长子曹昂和爱将典韦。当曹操势力日盛时他又建议张绣投降曹操——并预测曹操不会计较前仇——再次应验。在曹魏朝廷中他从不站队、极少发言——但每次建议都精准得可怕。他活到77岁在乱世中善终——对比其他三国谋士几乎全部非正常死亡的命运，贾诩的生存智慧令人叹服。",
  "Jia Xu may have been the Three Kingdoms' survival genius. His earliest advice — urging Li Jue and Guo Si to counterattack Chang'an — plunged the realm into chaos; some say 'Wenhe threw the world into disorder.' But he left Li Jue, serving Duan Wei and Zhang Xiu in turn — twice devising strategies under Zhang Xiu that dealt Cao Cao crushing defeats, costing him his eldest son Cao Ang and beloved bodyguard Dian Wei. When Cao Cao grew unstoppable, Jia Xu urged Zhang Xiu to surrender — predicting Cao Cao would overlook past grievances — again precisely correct. In the Wei court, he never took sides and rarely spoke — but every suggestion was chillingly accurate. He died peacefully at 77 amid chaos — contrasting with nearly every other Three Kingdoms strategist who met violent ends, Jia Xu's art of survival is breathtaking.",
  ["贾文和", "Jia Wenhe", "毒士"], ["src-sanguozhi"], "", 0.8)

p("liu-bowen", "刘伯温", "Liu Bowen", 1311, 1375, "ming-dynasty",
  ["谋士", "战略家", "明朝", "预言家"], ["Strategist", "Ming Dynasty", "Prophet"],
  "明朝开国第一谋臣，辅佐朱元璋统一天下，民间传说中他的预言能力被神化为《烧饼歌》。",
  "Ming dynasty's foremost founding strategist who helped Zhu Yuanzhang unite the realm; folk legend deified his prophetic powers in the 'Shaobing Song' (Pancake Prophecies).",
  "刘基（字伯温）在元朝中过进士但仕途坎坷，49岁时投奔朱元璋。他迅速成为朱元璋的首席谋士——制定了「先灭陈友谅、再灭张士诚、然后北伐中原」的统一方略。明朝建立后他参与制定了多项重要制度。但他深知「兔死狗烹」的规律——洪武四年便告老还乡。然而政敌的陷害使他被朱元璋猜忌，被迫回到南京在软禁中——传说被政敌下毒致死。民间传说中刘伯温的形象远超史实——《烧饼歌》假托他之名预言了明清两代六百年的大事——在民间信仰中他几乎成了能掐会算的半仙之体。",
  "Liu Ji (courtesy name Bowen) earned the jinshi degree under the Yuan but endured a frustrating official career before joining Zhu Yuanzhang at 49. He quickly became the paramount strategist, devising the unified strategy: 'First destroy Chen Youliang, then Zhang Shicheng, then march north to the Central Plains.' After Ming's founding, he helped design key institutions. But he understood keenly the law of 'the hounds are cooked when the rabbits are gone' — he retired in just the fourth year of Hongwu. Yet political enemies' slander drew Zhu Yuanzhang's suspicion; forced back to Nanjing under house arrest, he allegedly died from poisoning by a rival. Folk legend inflated Liu Bowen far beyond the historical record — the 'Shaobing Song' (Pancake Prophecies), spuriously attributed to him, predicted six centuries of Ming-Qing events — and popular belief has practically elevated him to a Daoist immortal with prophetic powers.",
  ["刘基", "Liu Ji", "刘青田"], ["src-mingshi"], "", 0.85)

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
print(f"\n// Total: {len(people)} Chinese historical figures (ministers, literati, scientists, strategists)")
