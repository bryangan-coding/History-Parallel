#!/usr/bin/env python3
"""Chinese Generals, Thinkers, and Religious figures. ~22 figures."""
def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")

people = []

def p(id, name, nameEn, birth, death, region, tags, tagsEn, summary, summaryEn, desc, descEn,
      alt=None, srcs=None, wiki="", conf=0.85, occ=None):
    people.append(dict(id=id, name=name, nameEn=nameEn, birthYear=birth, deathYear=death,
        regionId=region, tags=tags, tagsEn=tagsEn, occupations=occ or ["军事家"],
        summary=summary, summaryEn=summaryEn, description=desc, descriptionEn=descEn,
        alternativeNames=alt or [], sourceIds=srcs or [], wikidataQid=wiki,
        dataStatus="published", confidenceScore=conf, externalReferences=[]))

# ===== 军事将领 (13) =====
p("bai-qi", "白起", "Bai Qi", -332, -257, "china",
  ["军事家", "将领", "秦国"], ["Commander", "General", "Warring States"],
  "战国时期秦国名将，被称为「人屠」，一生攻城70余座，长平之战坑杀赵军40万。",
  "Warring States Qin general called 'the Butcher'; captured over 70 cities and buried 400,000 Zhao soldiers alive at Changping.",
  "白起是战国四大名将之首（白起、王翦、廉颇、李斯——另有说法含李牧）。他效力秦昭襄王三十余年，从一名普通士兵升至武安君，攻无不克战无不胜。长平之战他诱使赵国以赵括取代廉颇，一举歼灭赵军主力。此后他主张一鼓作气灭赵，但范雎嫉妒其功百般阻挠。后来秦攻赵不利重新起用白起，他托病不去——秦昭襄王大怒先是贬为士卒后又赐剑令其自刎。白起临死前说：「我固当死，长平之战，赵卒降者数十万，我诈而尽坑之，是足以死。」",
  "Bai Qi was the foremost of the Warring States' four great generals. He served King Zhaoxiang of Qin for over thirty years, rising from common soldier to Lord Wu'an, never losing a single battle. At Changping, he lured Zhao into replacing the veteran Lian Po with the book-theorist Zhao Kuo, then annihilated their main force. He urged pressing the advantage to destroy Zhao entirely, but the chancellor Fan Ju, jealous of his achievements, blocked every attempt. When Qin later needed him again, Bai Qi pleaded illness and refused — the furious king demoted him to common soldier, then sent a sword ordering his suicide. Dying, Bai Qi said: 'I deserve death — at Changping, when hundreds of thousands of Zhao soldiers surrendered, I deceived and buried them all alive. That alone merits death.'",
  [], ["src-shiji"], "", 0.85)

p("wang-jian", "王翦", "Wang Jian", -304, -214, "china",
  ["军事家", "将领", "秦国"], ["Commander", "General", "Warring States"],
  "战国末期秦国名将，统兵灭楚，六国中五国为其与子王贲所灭，功成身退安然善终。",
  "Late Warring States Qin general who conquered Chu; five of the six states fell to him and his son Wang Ben; retired successfully and died in peace.",
  "王翦是秦始皇统一六国的头号军事功臣。他最大的手笔是灭楚之战——当秦王问需要多少兵力时，年轻将领李信说20万，王翦坚持要60万。秦王嘲笑王翦年老胆怯，派李信出征——结果大败。秦王亲自登门道歉，王翦率60万大军用一年多时间稳扎稳打灭了楚国。他极为精通政治生存——出征前多次向秦王索要良田美宅以示无野心，出征途中也不断派人回来「催赏」——始终消解秦王的猜忌。他灭楚后立即交出兵权告老还乡，最终善终。",
  "Wang Jian was Qin Shi Huang's foremost military contributor to unification. His magnum opus was the conquest of Chu — when the king asked how many troops were needed, the young general Li Xin said 200,000; Wang Jian insisted on 600,000. The king mocked Wang Jian for senile timidity and sent Li Xin — who was catastrophically defeated. The king apologized in person; Wang Jian took 600,000 troops and methodically destroyed Chu over a year. He was a master of political survival — before campaigning, he repeatedly requested land grants and mansions to dispel suspicion of ambition, and during the campaign kept sending messengers back to 'remind' the king about promised rewards. After Chu fell, he immediately surrendered command and retired — and died peacefully.",
  ["王翦"], ["src-shiji"], "", 0.85)

p("han-xin", "韩信", "Han Xin", -231, -196, "han-dynasty",
  ["军事家", "将领", "汉朝"], ["Commander", "General", "Han Dynasty"],
  "汉初三杰之一，「兵仙」神帅，暗度陈仓、背水一战、十面埋伏均出自其手，被吕后诱杀于长乐宫。",
  "One of the Three Heroes of early Han, hailed as the 'Immortal of Military Strategy' whose brilliant tactics included crossing Chencang in secret and the ambush at Gaixia; executed by Empress Lü.",
  "韩信可能是中国历史上最杰出的战术天才。他年轻时曾受胯下之辱——从屠夫胯下钻过——表现出了超人的隐忍。投奔刘邦后他被萧何追回拜为大将军。暗度陈仓（明修栈道暗中出陈仓）、背水一战（在井陉口背水列阵激发出士卒的死战决心）、十面埋伏（在垓下四面楚歌围困项羽）这些战术创造中的每一项都堪称战争艺术史上的教科书案例。但他政治上的天真导致了他的悲剧——犹豫不决是否背叛刘邦，最终被吕后和萧何设计诱杀于长乐宫钟室。「成也萧何，败也萧何」的成语即由此而来。",
  "Han Xin may be Chinese history's most brilliant tactical genius. As a youth, he crawled through a butcher's legs — enduring ultimate humiliation with superhuman patience. After joining Liu Bang, Xiao He pursued him and had him appointed Commander-in-Chief. His tactical creations — secretly crossing Chencang while publicly repairing plank roads, fighting with a river at his back at Jingxing to force his soldiers into desperate valor, the ten-sided ambush at Gaixia with Chu songs on all sides — each is a textbook case in the art of war. But his political naivety sealed his tragedy — wavering on whether to betray Liu Bang, he was finally lured by Empress Lü and Xiao He to Changle Palace and executed in the Bell Chamber. The idiom 'Xiao He made him, Xiao He destroyed him' originates here.",
  ["韩重言", "Han Chongyan", "淮阴侯", "兵仙"], ["src-shiji", "src-hanshu"], "", 0.9)

p("xiang-yu", "项羽", "Xiang Yu", -232, -202, "china",
  ["军事家", "将领", "楚汉"], ["Commander", "Warlord", "Chu-Han"],
  "西楚霸王，力能扛鼎的绝世猛将，巨鹿之战破釜沉舟大破秦军，最终在垓下四面楚歌乌江自刎。",
  "Hegemon-King of Western Chu, a warrior of peerless might who shattered the Qin army at Julu by burning his own boats, only to fall at Gaixia surrounded by Chu songs.",
  "项羽是中国历史上最具悲剧英雄色彩的人物。他是楚国贵族后代，「力能扛鼎，才气过人」。巨鹿之战他破釜沉舟——渡过漳河后沉船砸锅每人只带三日粮——以不足五万人击溃秦军主力三十万，威震天下。但他犯了一系列战略错误：坑杀秦降卒二十万失去民心、放弃关中回彭城使刘邦得以壮大、鸿门宴上犹豫不杀刘邦。四年楚汉战争最终在垓下终结——四面楚歌声中爱妾虞姬自刎，他率八百骑突围后在乌江边拒绝渡江回乡：「无颜见江东父老」——自刎而死，年仅31岁。",
  "Xiang Yu is Chinese history's ultimate tragic hero. A Chu noble descendant of prodigious strength and talent. At the Battle of Julu, he burned his boats, smashed his cooking pots, and took only three days' rations — then routed the main Qin army of 300,000 with under 50,000 men, stunning the realm. But he committed a cascade of strategic blunders: burying 200,000 Qin prisoners alive lost popular support; abandoning the Guanzhong heartland for Pengcheng allowed Liu Bang to grow; hesitating to kill Liu Bang at the Hongmen Banquet. Four years of Chu-Han warfare ended at Gaixia — surrounded by Chu songs, his beloved concubine Yu Ji took her own life, and he broke out with 800 cavalry only to refuse a boat across the Wu River: 'I cannot face the elders of Jiangdong' — he slit his own throat at 31.",
  ["项籍", "Xiang Ji", "西楚霸王"], ["src-shiji"], "", 0.9)

p("wei-qing", "卫青", "Wei Qing", -140, -106, "han-dynasty",
  ["军事家", "将领", "汉朝"], ["Commander", "General", "Han Dynasty"],
  "西汉名将，七次出击匈奴无一败绩，收复河套地区，从奴隶出身升至大将军。",
  "Western Han general who led seven campaigns against the Xiongnu without a single defeat, reclaiming the Ordos region; rose from slavery to Commander-in-Chief.",
  "卫青出身极为卑微——其母是平阳侯府的女奴，他本人也是骑奴出身。他同母异父的姐姐卫子夫被汉武帝立为皇后后，他才获得机会。但他用一连串辉煌的胜利证明了自己并非靠裙带关系——七次大规模出击匈奴无一败绩。他收复了河套地区设立朔方郡、夺取了河西走廊的控制权。他以谦和低调著称——即使位极人臣对待士大夫和士兵都极为尊重。他的外甥霍去病青出于蓝——但卫青开创的骑兵大兵团运动战体系才是汉匈战争转折的关键。",
  "Wei Qing's origins were abjectly humble — his mother was a slave at the household of the Marquis of Pingyang, and he himself was a mounted slave. Only when his half-sister Wei Zifu became Empress to Emperor Wu did opportunity knock. But he proved his merit through a string of brilliant victories — seven major campaigns against the Xiongnu without a single defeat. He reclaimed the Ordos region, established Shuofang Commandery, and seized control of the Hexi Corridor. Known for his humility — even at the pinnacle of power, he treated scholars and soldiers alike with deep respect. His nephew Huo Qubing surpassed him in speed and aggression, but it was Wei Qing who pioneered the large-scale cavalry maneuver warfare that was the turning point in the Han-Xiongnu conflict.",
  ["卫仲卿", "Wei Zhongqing"], ["src-shiji", "src-hanshu"], "", 0.9)

p("huo-qubing", "霍去病", "Huo Qubing", -140, -117, "han-dynasty",
  ["军事家", "将领", "汉朝"], ["Commander", "General", "Han Dynasty"],
  "西汉天才将领，18岁出征天下，「匈奴未灭何以家为」，封狼居胥成为历代武将的最高理想。",
  "Western Han prodigy general who first campaigned at 18; 'While the Xiongnu remain undestroyed, what home can I have?' — his sacrifice at Wolf Mountain became every later general's ideal.",
  "霍去病是中国军事史上最耀眼的天才——17岁随卫青出征，率八百骑兵深入大漠斩首两千余级俘获匈奴单于的祖父和叔父，被封冠军侯。此后他如旋风般扫荡河西走廊——同一年春、夏两次大出击，歼敌四万余人，迫使匈奴浑邪王率四万人投降。公元前119年漠北大战中他率五万骑兵北进两千余里、封狼居胥祭天——「封狼居胥」从此成为中国武将的最高荣誉代称。但他年仅24岁便暴病身亡——汉武帝痛失爱将在其墓前设计了祁连山形状的封土。",
  "Huo Qubing is Chinese military history's brightest shooting star. At 17, riding with his uncle Wei Qing, he led 800 cavalry deep into the desert, decapitating over 2,000 and capturing the Xiongnu chanyu's grandfather and uncle — earning the title Marquis of Champion at 18. He then swept through the Hexi Corridor like a whirlwind — two campaigns that same year killed over 40,000 and forced the Xiongnu Hunye King to surrender with 40,000 followers. In the 119 BCE Mobei campaign, he led 50,000 cavalry over 1,000 km north, reaching Wolf Mountain to sacrifice to heaven — 'sealing Wolf Mountain' became the ultimate accolade every later Chinese general aspired to. But he died suddenly at 24 — the grieving Emperor Wu designed his tomb mound in the shape of the Qilian Mountains.",
  ["霍冠军", "Huo Guanjun", "冠军侯"], ["src-shiji", "src-hanshu"], "", 0.9)

p("guan-yu", "关羽", "Guan Yu", 160, 219, "three-kingdoms",
  ["军事家", "将领", "三国", "蜀汉"], ["Commander", "General", "Three Kingdoms", "Shu Han"],
  "三国蜀汉名将，「美髯公」，以忠义著称，被民间尊为「关圣帝君」，成为中国武神和财神的完美合一。",
  "Shu Han general famed for his magnificent beard and peerless loyalty; deified as 'Guan Sheng Dijun' (Holy Emperor Guan), uniquely combining the Chinese god of war and god of wealth.",
  "关羽在正史中是「万人敌」的猛将——白马之战中于万军之中刺死袁绍大将颜良。但民间信仰将他提升到了无与伦比的高度。他「身在曹营心在汉」千里走单骑寻找刘备的故事是中国忠义的终极象征。他水淹七军威震华夏是军事生涯的巅峰——但随后吕蒙白衣渡江偷袭荆州，关羽败走麦城与其子关平一同被东吴擒杀。死后他在民间信仰中地位一路攀升——从关公到关帝，从武圣到财神——全国各地有数以万计的关帝庙。在海外华人社区中，关公是分布最广的神祇之一。",
  "In official history, Guan Yu was a warrior 'worthy of ten thousand' — at the Battle of Boma, he charged into the enemy host and killed Yuan Shao's prized general Yan Liang. But folk religion elevated him to unrivalled heights. His 'body in Cao's camp, heart with Han' — traveling a thousand li alone to rejoin Liu Bei — is the ultimate symbol of Chinese loyalty. His flooding of seven armies was his military peak — but then Lü Meng's White-Robed Crossing took Jingzhou by stealth, and Guan Yu fled to Mai City where Eastern Wu forces caught and executed him alongside his son Guan Ping. After death, his status climbed: from Guan Gong to Guan Di, from Martial Sage to God of Wealth — tens of thousands of Guan Di temples dot China. Among overseas Chinese, Guan Gong is one of the most widely distributed deities.",
  ["关云长", "Guan Yunchang", "关公", "美髯公", "关圣帝君"], ["src-sanguozhi"], "", 0.85)

p("zhang-fei", "张飞", "Zhang Fei", 167, 221, "three-kingdoms",
  ["军事家", "将领", "三国", "蜀汉"], ["Commander", "General", "Three Kingdoms", "Shu Han"],
  "三国蜀汉猛将，长坂桥上一声吼退曹军，但暴躁酗酒最终被部下刺杀。",
  "Shu Han's fierce general who famously roared Cao Cao's army to a standstill at Changban Bridge; killed by his own men for his drunken brutality.",
  "张飞与关羽并称「万人敌」——长坂坡之战中他仅率二十余骑据守当阳桥，一声断喝竟使曹军无人敢近前——这虽然经过了《三国演义》的传奇化渲染，但他确实是公认的顶尖猛将。他粗中有细——义释严颜展现了他的胸襟，大破张郃证明了他并非只有勇猛。但他对士卒暴虐无恩——「爱敬君子而不恤小人」——刘备一再告诫他「卿刑杀既过差，又日鞭挝健儿」终将自取其祸。果然，221年为关羽报仇的东征前夕，他被部将张达、范强刺杀，首级被送往东吴。",
  "Zhang Fei was counted alongside Guan Yu as a 'match for ten thousand.' At Changban, he reportedly held the bridge with only twenty-odd riders and roared so ferociously that Cao Cao's entire army dared not advance — though Romance of the Three Kingdoms magnified this into legend, he was universally acknowledged as a top-tier warrior. He had unexpected subtlety — his generous treatment of the captured veteran Yan Liang showed magnanimity, and his crushing defeat of Zhang He proved he was more than brute force. But he brutalized his own soldiers — 'he respected gentlemen but had no pity for the rank and file' — and Liu Bei repeatedly warned him: 'Your punishments are excessive, and you flog your own men daily — this will bring disaster.' Indeed, on the eve of the 221 eastern campaign to avenge Guan Yu, his subordinates Zhang Da and Fan Qiang murdered him in his sleep and sent his head to Eastern Wu.",
  ["张翼德", "Zhang Yide"], ["src-sanguozhi"], "", 0.85)

p("li-jing", "李靖", "Li Jing", 571, 649, "tang-dynasty",
  ["军事家", "将领", "唐朝"], ["Commander", "General", "Tang Dynasty"],
  "唐初第一名将，灭萧铣、平辅公祏、破东突厥、征吐谷浑，被尊为托塔李天王的原型。",
  "Foremost Tang general who destroyed Xiao Xian, suppressed Fu Gongshi, shattered the Eastern Turks, and conquered Tuyuhun; mythologized as the Pagoda-Bearing Heavenly King Li.",
  "李靖是唐初最全能的统帅——无论水战、陆战还是沙漠远征都极为出色。他年轻时曾向李渊告发李渊将反——但李渊起兵后要杀他时被李世民救下，从此成为唐朝最倚重的战将。他的成就单令人目眩：水陆并进灭萧铣的梁国、平定辅公祏的江南叛乱、630年率三千骑兵冒着风雪夜袭阴山大破东突厥颉利可汗——后者被俘至长安跳舞谢罪。此后他远征吐谷浑跨越青海高原取得完胜。他的兵法总结在《李卫公问对》中——被列为《武经七书》之一。",
  "Li Jing was early Tang's most versatile commander — excelling in naval, land, and desert campaigns alike. As a young man, he had actually reported Li Yuan's impending rebellion to the Sui — when Li Yuan captured him and prepared execution, Li Shimin intervened, and Li Jing became the dynasty's most trusted general. His record is dizzying: destroying Xiao Xian's Liang kingdom through combined water-land assault; pacifying Fu Gongshi's Jiangnan rebellion; in 630, leading 3,000 cavalry through a blizzard to strike the Eastern Turkic Khaganate by night, routing and capturing Jieli Khan, who was brought to Chang'an to dance in submission. He then conquered Tuyuhun across the Qinghai plateau. His military principles are recorded in the 'Duke Li of Wei's Dialogues' — included among the 'Seven Military Classics.'",
  ["李药师", "Li Yaoshi", "卫国公"], ["src-jiutangshu"], "", 0.9)

p("guo-ziyi", "郭子仪", "Guo Ziyi", 697, 781, "tang-dynasty",
  ["军事家", "将领", "唐朝"], ["Commander", "General", "Tang Dynasty"],
  "唐朝中兴名将，平定安史之乱的大功臣，一生功高盖主却能善终，享年85岁。",
  "Tang restoration general who played the decisive role in crushing the An Lushan Rebellion; achieved the near-impossible feat of dying peacefully at 85 despite unparalleled military prestige.",
  "郭子仪在安史之乱爆发时已年届花甲——但他承担起了挽救唐王朝的使命。他与李光弼联手收复长安和洛阳，然后在仆固怀恩叛乱、吐蕃入侵时再次力挽狂澜。他在军队和民间享有极高的威望——这在一个猜忌心极重的时代本是最危险的。但郭子仪以极致的谦逊和坦荡化解了皇帝的疑虑——他将大门敞开任人进出以示毫无隐私、甚至在代宗面前为陷害过他的人求情。他八子七婿均在朝廷担任高官——家族兴旺空前绝后。唐德宗尊他为「尚父」——他的人生堪称中国历史上功高震主而能善终的最完美范例。",
  "Guo Ziyi was already in his sixties when the An Lushan Rebellion erupted — but he shouldered the mission of saving the Tang. He and Li Guangbi jointly recaptured Chang'an and Luoyang, then saved the dynasty again during Pugu Huai'en's rebellion and the Tibetan invasion. His prestige with the army and populace was immense — in a paranoid era, the most dangerous thing imaginable. Yet Guo Ziyi neutralized imperial suspicion through extreme humility and transparency — he kept his mansion gates perpetually open so anyone could see he had nothing to hide, and even interceded with Emperor Daizong for those who had slandered him. His eight sons and seven sons-in-law all held high office — a family prosperity unmatched in Chinese history. Emperor Dezong honored him as 'Shangfu' (Venerable Father). His life is arguably the most perfect example in Chinese history of transcending the deadly 'merit that overshadows the lord' with serene longevity.",
  ["郭令公", "Guo Linggong"], ["src-jiutangshu"], "", 0.9)

p("qi-jiguang", "戚继光", "Qi Jiguang", 1528, 1588, "ming-dynasty",
  ["军事家", "将领", "明朝"], ["Commander", "General", "Ming Dynasty"],
  "明朝抗倭名将，创建戚家军以鸳鸯阵大破倭寇，著有《纪效新书》和《练兵实纪》。",
  "Ming general who formed the Qi Army and crushed the Japanese pirates with the revolutionary Mandarin Duck formation; author of military science classics.",
  "戚继光面对的不是传统意义上的敌国军队——而是流窜在东南沿海、刀法精熟的倭寇。他创造性地将步兵小队编成「鸳鸯阵」——藤牌掩护、狼筅阻敌、长枪刺杀、短刀近战——11人一个战术单元完美克制倭寇的单兵战斗力。他招募义乌矿工和农民组建戚家军——纪律严明到令人发指的程度（他当众处决了自己的亲舅舅以正军法）。台州九战九捷基本肃清了东南倭患。随后他调任蓟镇镇守北疆十六年——修筑长城敌台、训练火器部队——著有中国军事科学史上的不朽之作《纪效新书》和《练兵实纪》。",
  "Qi Jiguang faced not a conventional enemy army but Japanese pirates — master swordsmen — ravaging the southeastern coast. He creatively organized infantry squads into the 'Mandarin Duck Formation': rattan shields for cover, wolf-brush spears to entangle, long pikes to thrust, short swords for close combat — eleven men as a tactical unit perfectly countering individual Japanese swordsmanship. He recruited miners and peasants from Yiwu to form the Qi Army — disciplined to extremes (he had his own uncle publicly executed for violating military law). Nine battles, nine victories around Taizhou essentially eradicated the pirate scourge. Then reassigned to Ji Garrison, he defended the northern frontier for 16 years — building watchtowers on the Great Wall, training firearms units — and authored the immortal classics of Chinese military science, 'New Book of Effective Discipline' and 'Record of Military Training.'",
  ["戚元敬", "Qi Yuanjing", "戚南塘"], ["src-mingshi"], "", 0.9)

p("yuan-chonghuan", "袁崇焕", "Yuan Chonghuan", 1584, 1630, "ming-dynasty",
  ["军事家", "将领", "明朝"], ["Commander", "General", "Ming Dynasty"],
  "明末抗清名将，宁远之战炮伤努尔哈赤，因反间计被崇祯帝凌迟处死，死时百姓争食其肉。",
  "Late Ming general who mortally wounded Nurhaci at the Battle of Ningyuan; executed by lingering death on false charges, with the Beijing populace fighting over his flesh.",
  "袁崇焕是明末最杰出的将领——也是一出最惨烈的悲剧。1626年宁远之战中他以红夷大炮命中努尔哈赤——后者不久后伤重而死——这是明军对后金取得的第一次重大胜利。1629年皇太极绕道蒙古突破长城兵临北京城下，袁崇焕率九千骑兵昼夜兼程赶到北京勤王。但皇太极利用俘获的明朝太监散布袁崇焕通敌的谣言——多疑的崇祯皇帝竟信以为真，将袁崇焕凌迟处死。北京百姓——相信了处决布告中的叛国罪名——在刑场争购其肉。直到清朝编修明史时才公布真相——但这段冤案已成了中国历史上最黑暗的忠臣悲剧之一。",
  "Yuan Chonghuan was late Ming's most brilliant general — and its starkest tragedy. At the 1626 Battle of Ningyuan, his Portuguese-style cannon fatally wounded Nurhaci — the first major Ming victory over the Later Jin. In 1629, Hong Taiji bypassed the Great Wall through Mongolia and reached Beijing's gates; Yuan Chonghuan raced his 9,000 cavalry day and night to defend the capital. But Hong Taiji used captured Ming eunuchs to spread the rumor that Yuan was collaborating with the enemy — and the paranoid Chongzhen Emperor believed it, sentencing him to death by slow slicing. The Beijing populace — convinced by the execution notice's treason charges — fought to buy and eat his flesh. Only when the Qing compiled the official Ming history was the truth revealed — but by then this had become one of Chinese history's darkest sagas of a loyal minister destroyed.",
  ["袁元素", "Yuan Yuansu"], ["src-mingshi"], "", 0.85)

# ===== 思想家 (4) =====
p("dong-zhongshu", "董仲舒", "Dong Zhongshu", -179, -104, "han-dynasty",
  ["哲学家", "儒家", "汉朝"], ["Philosopher", "Confucian", "Han Dynasty"],
  "西汉大儒，「罢黜百家独尊儒术」的倡议者，将儒学与阴阳五行结合，使儒家成为两千年中国的正统思想。",
  "Western Han Confucian who proposed 'dismiss the hundred schools and revere only Confucianism'; fused Confucianism with yin-yang cosmology, making it China's orthodoxy for two millennia.",
  "董仲舒在汉武帝策问天下贤良时提出了改变中国历史的建议：「诸不在六艺之科、孔子之术者，皆绝其道，勿使并进」——即罢黜百家、独尊儒术。他的「天人感应」理论将皇帝的行为与自然灾异联系起来——为皇权提供了神学基础，但也给予了儒臣以灾异批评皇帝的武器。他在《春秋繁露》中系统地融合了儒家伦理和阴阳五行宇宙观——这种综合性使得儒学从一种学说上升为一种涵盖天地人的完整世界观。",
  "Dong Zhongshu, responding to Emperor Wu's call for worthy scholars, made the proposal that changed Chinese history: 'All teachings not within the Six Arts and the way of Confucius should be suppressed, not permitted to flourish alongside it' — dismiss the hundred schools and revere only Confucianism. His 'Heaven-Human Resonance' theory linked the emperor's conduct to natural disasters — providing divine sanction for imperial power while giving Confucian officials a weapon to criticize misrule through portents. His 'Luxuriant Dew of the Spring and Autumn Annals' systematically fused Confucian ethics with yin-yang and five-phase cosmology — elevating Confucianism from a school of thought into a comprehensive worldview encompassing heaven, earth, and humanity.",
  [], ["src-shiji", "src-hanshu"], "", 0.85)

p("wang-fuzhi", "王夫之", "Wang Fuzhi", 1619, 1692, "china",
  ["哲学家", "思想家", "明末清初"], ["Philosopher", "Late Ming-Early Qing"],
  "明末清初三大思想家之一，隐居船山著书立说四十年，批判专制、倡导经世致用之学。",
  "One of the three great thinkers of the Ming-Qing transition who lived as a hermit on Boat Mountain for forty years, criticizing despotism and championing practical scholarship.",
  "王夫之（船山先生）在清军南下时组织义军抵抗失败后，为躲避剃发令隐居湖南衡阳石船山——此后四十年未出。他在这漫长的隐居岁月中写下了一百余种著作，涵盖哲学、史学、政治、文学等——总量惊人地达到了八百余万字。他猛烈批判了历代专制制度——认为「天下非一姓之私」——成为近代中国民族主义和民主思想的重要源头。他对「理」与「气」的辩证讨论将宋明理学推向了一个新的高度。他是曾国藩极为推崇的思想家——《船山遗书》的刊刻正是在曾国藩的支持下完成的。",
  "After his loyalist army failed against the Qing advance and to avoid the forced queue-and-robe edict, Wang Fuzhi (Master Boat Mountain) retreated to Stone Boat Mountain in Hengyang, Hunan — where he remained for four decades. In this marathon of seclusion, he produced over one hundred works spanning philosophy, history, politics, and literature — an astounding total of over eight million characters. He fiercely criticized the despotic tradition — 'the realm is not the private possession of one surname' — becoming a crucial source for modern Chinese nationalism and democratic thought. His dialectical analysis of 'principle' (li) and 'material force' (qi) pushed Neo-Confucianism to new heights. He was deeply admired by Zeng Guofan, who personally supported the publication of his posthumous works.",
  ["王而农", "Wang Ernong", "船山先生", "王船山"], ["src-qingshigao"], "", 0.85)

p("huang-zongxi", "黄宗羲", "Huang Zongxi", 1610, 1695, "china",
  ["哲学家", "思想家", "史学家", "明末清初"], ["Philosopher", "Historian", "Late Ming-Early Qing"],
  "明末清初三大思想家之一，《明夷待访录》猛烈批判君主专制，其民主主义思想比卢梭早了一个世纪。",
  "One of the three great Ming-Qing transition thinkers; his 'Waiting for the Dawn' fiercely critiqued autocratic monarchy with democratic ideas predating Rousseau by a century.",
  "黄宗羲年轻时曾在朝堂上用铁锥刺伤陷害父亲致死的仇人——这种刚烈贯穿了他的一生。明朝灭亡后他拒绝出仕清朝，转而潜心学术。他最著名的政治著作《明夷待访录》系统地批判了中国君主专制制度——「为天下之大害者，君而已矣」这句话的激烈程度在中国古代政治思想中是空前绝后的。他提出了以学校议政、以法律限制君权等极具前瞻性的主张——比卢梭《社会契约论》早了近一个世纪。他还在学术史领域有杰出贡献——《明儒学案》是中国第一部系统的学术思想史。",
  "As a young man, Huang Zongxi attacked the man who had framed and killed his father, stabbing him with an iron awl in the courtroom — this fierce integrity defined his life. After the Ming fell, he refused to serve the Qing and devoted himself to scholarship. His most famous political work, 'Waiting for the Dawn' (Mingyi Daifang Lu), systematically critiques Chinese autocratic monarchy — the line 'the greatest harm to the realm is none other than the ruler' is unparalleled in its ferocity in pre-modern Chinese political thought. He proposed having schools deliberate on governance and using laws to constrain imperial power — prefiguring Rousseau's 'Social Contract' by nearly a century. His 'Case Studies of Ming Confucians' is China's first systematic history of scholarly thought.",
  ["黄太冲", "Huang Taichong", "梨洲先生", "南雷"], [], "", 0.85)

p("gu-yanwu", "顾炎武", "Gu Yanwu", 1613, 1682, "china",
  ["哲学家", "思想家", "学者", "明末清初"], ["Philosopher", "Scholar", "Late Ming-Early Qing"],
  "明末清初三大思想家之一，「天下兴亡匹夫有责」的提出者，开创了清代考据学先河。",
  "One of the three great Ming-Qing transition thinkers who coined 'every man bears responsibility for the fate of the realm'; pioneered Qing textual criticism.",
  "顾炎武在明朝灭亡后改名「炎武」以示心向炎黄——对清朝的剃发易服进行了最顽强的意志抵抗。他后半生以骡马驮着书籍游历北方各地——考察山川形胜、访问故老遗民、搜集地方文献。他提出的「天下兴亡匹夫有责」成为此后三百余年中国人爱国精神最响亮的表达。在学术上他是清代考据学的开山鼻祖——《日知录》和《天下郡国利病书》以实证方法研究经典和地理——影响了此后两百年的中国学术走向。他将学术与经世致用紧密结合——批判空谈性理的宋明理学末流。",
  "After the Ming fell, Gu Yanwu renamed himself 'Yanwu' (Flaming Martiality) signaling his loyalty to the Yan-Huang (mythic Chinese) ancestors — mounting the most determined spiritual resistance to Qing rule. He spent the second half of his life traveling North China with mules carrying his library — surveying terrain, interviewing surviving loyalists, collecting local documents. His formulation 'every common man bears responsibility for the rise and fall of the realm' became the most resonant expression of Chinese patriotism for the next three centuries. Academically, he is the founding father of Qing evidential scholarship — his 'Record of Daily Knowledge' and 'Merits and Drawbacks of the Realm's Prefectures' applied empirical methods to classics and geography, shaping Chinese scholarship for two centuries. He insisted scholarship must serve practical governance — fiercely attacking the empty metaphysical speculation of late Neo-Confucianism.",
  ["顾宁人", "Gu Ningren", "亭林先生"], [], "", 0.85)

# ===== 宗教人物 (2) =====
p("huineng", "慧能", "Huineng", 638, 713, "tang-dynasty",
  ["佛教", "禅师", "唐朝", "禅宗六祖"], ["Buddhism", "Chan Master", "Tang Dynasty"],
  "禅宗六祖，将禅宗彻底中国化的关键人物，其《坛经》是中国佛教著作唯一被称为「经」的本土作品。",
  "The Sixth Patriarch of Chan Buddhism who thoroughly Sinicized Chan; his 'Platform Sutra' is the only Chinese Buddhist text elevated to 'sutra' status.",
  "慧能的故事是中国佛教史上最富戏剧性的——一个不识字的岭南樵夫，在寺院里舂米八个月，因一句「本来无一物，何处惹尘埃」的偈语被五祖弘忍秘密传授衣钵。他逃到南方隐居了十五年后才正式开坛说法。他倡导「直指人心，见性成佛」——不需要繁琐的经典研读和渐进的修行，人人皆可通过顿悟成佛。这种思想将深奥的佛教哲学转化为普通人可以直接体验的精神实践——使禅宗成为对中国文化影响最深远的佛教宗派。他的弟子将他的说法记录为《六祖坛经》——唯一一部非佛陀所说而被称为「经」的佛教典籍。",
  "Huineng's story is Zen Buddhism's most dramatic: an illiterate firewood-cutter from Lingnan who pounded rice for eight months in a monastery, then won the Fifth Patriarch's secret transmission of the robe and bowl with a single verse: 'Originally there is not a single thing — where could dust alight?' He fled south and lived in hiding for fifteen years before openly teaching. He advocated 'directly pointing to the mind, seeing one's nature and becoming Buddha' — no need for arcane textual study or gradual practice; anyone could achieve enlightenment through sudden insight. This democratized profound Buddhist philosophy into lived spiritual experience, making Chan (Zen) the most culturally influential Buddhist school in China. His disciples recorded his teachings as the 'Platform Sutra of the Sixth Patriarch' — the only non-Buddha-authored text ever elevated to 'sutra' status.",
  ["慧能禅师", "六祖惠能", "曹溪"], ["src-jiutangshu"], "", 0.8)

p("faxian", "法显", "Faxian", 337, 422, "china",
  ["佛教", "旅行家", "东晋"], ["Buddhism", "Traveler", "Eastern Jin"],
  "东晋高僧，60岁时西行求法，历经十四年三十余国，著有《佛国记》，比玄奘早230年。",
  "Eastern Jin monk who journeyed West for Buddhist scriptures at age 60, traversing thirty countries over fourteen years; his 'Record of Buddhist Kingdoms' predates Xuanzang by 230 years.",
  "法显是中国第一位从陆路前往印度并经由海路返回的求法高僧——而且他出发时已经六十岁了。他与几位同伴穿越塔克拉玛干沙漠（「上无飞鸟，下无走兽」）和帕米尔高原到达印度，在中天竺学习和抄写梵文佛经，然后从狮子国（斯里兰卡）搭乘商船经海路回国——途中遭遇风暴险些丧命。他在412年返回中国后翻译了大量佛经，并撰写了《佛国记》——这部游记至今仍是研究五世纪中亚和南亚历史地理的最重要文献之一。",
  "Faxian was the first Chinese monk to travel to India overland and return by sea — and he was sixty years old when he departed. With companions, he crossed the Taklamakan Desert (where 'above no bird flies, below no beast walks') and the Pamir Plateau to reach India, studied and copied Sanskrit scriptures, then took a merchant ship from Sri Lanka back via the sea route — surviving a storm that nearly killed him. Returning in 412, he translated numerous scriptures and wrote 'A Record of Buddhist Kingdoms' (Foguo Ji) — this travelogue remains one of the most important sources for the historical geography of 5th-century Central and South Asia.",
  ["法显法师", "Faxian Fashi"], [], "", 0.8)

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
print(f"\n// Total: {len(people)} figures (generals, thinkers, religious)")
