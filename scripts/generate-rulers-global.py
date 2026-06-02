#!/usr/bin/env python3
"""Generate global rulers data for History Parallel.
Outputs TypeScript Person[] entries to stdout.
Existing rulers (already in mockData.ts): Augustus, Alexander, Charlemagne, Napoleon,
Cyrus, Hammurabi, Ramesses II, Ashoka, Henry V, Elizabeth I, Louis XIV, Peter the Great,
George Washington, Lincoln, Meiji, Akbar, Tokugawa Ieyasu, Ivan the Terrible,
Suleiman, Cleopatra, Justinian I, Ataturk, Constantine, Shah Jahan, Aurangzeb,
Mehmed II, William the Conqueror
"""
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

# ============ ROME (12 new) ============
p("tiberius", "提比略", "Tiberius", -42, 37, "roman-empire",
  ["君主", "皇帝", "罗马"], ["Ruler", "Emperor", "Rome"],
  "罗马帝国第二任皇帝，奥古斯都的养子和继承人，能干的军事统帅却是不情愿的统治者。",
  "Second Roman emperor, adopted son and heir of Augustus; a capable military commander but reluctant ruler.",
  "提比略是奥古斯都之妻莉维娅与前夫所生的儿子，在奥古斯都所有直系继承人都去世后被收养为继承人。他是一位出色的将军——在日耳曼和潘诺尼亚的战功卓著。继位后他最初治理审慎，但性格日益阴郁多疑，晚年退隐至卡普里岛，将朝政交给近卫军长官塞雅努斯。他最终在塞雅努斯权力膨胀后将其处死，但自己也在疑忌中去世。塔西佗在《编年史》中描绘了一个由明君逐渐蜕变为暴君的悲剧形象。",
  "Tiberius, son of Livia by her first husband, was adopted by Augustus after all direct heirs perished. An excellent general — his campaigns in Germania and Pannonia were exemplary. As emperor he initially governed prudently, but grew increasingly morose and paranoid, eventually retreating to Capri and leaving governance to Praetorian Prefect Sejanus. After Sejanus grew too powerful, Tiberius had him executed, but died himself in suspicion and isolation. Tacitus's 'Annals' portrays a tragic arc from capable ruler to tyrant.",
  [], ["src-tacitus", "src-suetonius"], "", 0.85)

p("caligula", "卡利古拉", "Caligula", 12, 41, "roman-empire",
  ["君主", "皇帝", "罗马"], ["Ruler", "Emperor", "Rome"],
  "罗马帝国第三任皇帝，以残忍和荒诞著称，在位仅四年即被禁卫军刺杀。",
  "Third Roman emperor, infamous for cruelty and eccentricity; assassinated by his Praetorian Guard after only four years.",
  "盖乌斯·凯撒——因其幼年在军营中穿的迷你军靴而被昵称为「卡利古拉」（小靴子）——即位之初颇得民心。但一场重病后他的行为变得荒唐暴虐：据说他打算任命自己的马为执政官、建造横跨那不勒斯湾的浮桥、自封为神。他奢靡无度迅速耗尽国库，肆意处决元老贵族。41年他被心怀不满的近卫军军官刺杀，成为第一个被杀的罗马皇帝。",
  "Gaius Caesar — nicknamed 'Caligula' (little boot) from the miniature military boots he wore as a child in camp — was initially popular. But after a severe illness, his behavior turned bizarre and tyrannical: he reportedly planned to make his horse a consul, built a pontoon bridge across the Bay of Naples, and declared himself a god. His extravagance rapidly emptied the treasury while he executed senators at whim. In 41 CE, he was assassinated by disgruntled Praetorian Guards — the first murdered Roman emperor.",
  [], ["src-suetonius"], "", 0.8)

p("claudius", "克劳狄乌斯", "Claudius", -10, 54, "roman-empire",
  ["君主", "皇帝", "罗马"], ["Ruler", "Emperor", "Rome"],
  "罗马帝国第四任皇帝，因身体残疾被家族忽视，却在学术和治国方面表现出色，征服不列颠。",
  "Fourth Roman emperor, dismissed by his family for physical disabilities, yet proved a capable scholar-ruler who conquered Britain.",
  "克劳狄乌斯因跛足和口吃被家族视为耻辱——他的母亲称他为「未完成的怪物」。卡利古拉被杀后，近卫军在宫中发现躲藏的他并拥立为帝。出乎所有人意料，他成为一位有效率的统治者：征服不列颠南部、扩建奥斯提亚港口、改革司法和官僚体系。但他在婚姻上极度不幸——第三任妻子梅萨利娜以淫乱闻名，第四任妻子小阿格里皮娜最终用毒蘑菇将他毒死，以便让儿子尼禄继位。",
  "Claudius, with his limp and stammer, was considered an embarrassment by his family — his mother called him 'a monster, unfinished by nature.' After Caligula's murder, the Praetorians found him hiding in the palace and proclaimed him emperor. To everyone's surprise, he proved effective: conquering southern Britain, expanding Ostia's port, and reforming the judiciary and bureaucracy. But his marriages were disastrous — his third wife Messalina was notorious for debauchery, and his fourth, Agrippina the Younger, ultimately poisoned him with mushrooms to secure the succession for her son Nero.",
  [], ["src-tacitus", "src-suetonius"], "", 0.85)

p("nero", "尼禄", "Nero", 37, 68, "roman-empire",
  ["君主", "皇帝", "罗马"], ["Ruler", "Emperor", "Rome"],
  "罗马帝国第五任皇帝，以暴政和纵情声色著称，罗马大火和迫害基督徒均发生在其在位期间。",
  "Fifth Roman emperor notorious for tyranny and debauchery; the Great Fire of Rome and persecution of Christians occurred under his rule.",
  "尼禄17岁即位，前期在哲学家塞内加的辅佐下尚能正常治国。但他逐渐沉溺于艺术表演和感官享乐——自认为是伟大的歌手和赛车手。64年罗马大火燃烧六天七夜，传说尼禄在城楼上弹琴吟唱（然而这一说法可能不实），事后他将责任推给基督徒展开残酷迫害。68年高卢和西班牙军团叛乱，元老院宣布他为人民公敌，尼禄在逃亡途中自杀——临死前哀叹「一个多么伟大的艺术家正在死去」。",
  "Nero ascended at 17 and, under the philosopher Seneca's guidance, governed reasonably at first. But he increasingly indulged in artistic performance and sensual pleasure — believing himself a great singer and chariot racer. When the Great Fire of 64 CE raged for nine days, rumor held that Nero 'fiddled while Rome burned' (likely apocryphal); he blamed the Christians and launched brutal persecutions. When the Gallic and Spanish legions revolted in 68, the Senate declared him a public enemy, and Nero committed suicide — lamenting, 'What an artist dies in me!'",
  [], ["src-tacitus", "src-suetonius"], "", 0.85)

p("vespasian", "韦斯帕芗", "Vespasian", 9, 79, "roman-empire",
  ["君主", "皇帝", "罗马"], ["Ruler", "Emperor", "Rome"],
  "弗拉维王朝开创者，结束四帝内乱之年，建造罗马斗兽场，以务实和幽默感著称。",
  "Founder of the Flavian dynasty who ended the Year of the Four Emperors; builder of the Colosseum, known for pragmatism and wry humor.",
  "韦斯帕芗出身平民骑士阶层——这在罗马皇帝中非常罕见。尼禄死后罗马陷入「四帝之年」的混乱，他率领东部军团杀回罗马夺取政权。他以务实著称——开征公共厕所税（催生了「金钱不臭」的名言）、开始建造罗马斗兽场、平定犹太起义（其子提图斯摧毁了耶路撒冷圣殿）。他恢复了被尼禄耗尽的国家财政，临终还不忘调侃自己被神化的命运：「天哪，我想我正在变成神。」",
  "Vespasian came from the equestrian order — rare among emperors. During the 'Year of the Four Emperors' after Nero's death, he marched his eastern legions on Rome and seized power. Notoriously practical, he taxed public toilets (giving us the phrase 'money doesn't stink'), began the Colosseum, and crushed the Jewish Revolt (his son Titus destroyed the Jerusalem Temple). He restored the state finances Nero had drained, and on his deathbed, with characteristic wit, quipped: 'Dear me, I think I'm becoming a god.'",
  [], ["src-tacitus", "src-suetonius"], "", 0.85)

p("trajan", "图拉真", "Trajan", 53, 117, "roman-empire",
  ["君主", "皇帝", "罗马", "军事"], ["Ruler", "Emperor", "Rome", "Military"],
  "罗马帝国第十三位皇帝，征服达契亚和帕提亚，罗马疆域在他的治下达到极盛。",
  "Thirteenth Roman emperor who conquered Dacia and Parthia, bringing the empire to its greatest territorial extent.",
  "图拉真出生于西班牙——是第一位行省出身的罗马皇帝。他是一位卓越的军事统帅：两次达契亚战争将多瑙河以北的金矿区纳入版图（图拉真记功柱至今矗立在罗马）；帕提亚战争占领了亚美尼亚和美索不达米亚，罗马帝国疆域达到前所未有的广度。但他也是一位仁慈的统治者——大规模公共建设（图拉真广场、图拉真市场）、设立救济贫困儿童的项目、与元老院保持良好关系。后世元老祈祷新皇帝时都会说「愿你比奥古斯都更幸运，比图拉真更好」。",
  "Born in Spain — the first provincial to become emperor — Trajan was a supreme military commander. Two Dacian wars annexed the gold-rich region north of the Danube (Trajan's Column still stands in Rome); the Parthian campaign seized Armenia and Mesopotamia. The empire reached its greatest expanse. Yet he was also a humane ruler — vast public works (Trajan's Forum and Market), programs to support poor children, and excellent senatorial relations. Later senators would inaugurate emperors with the prayer: 'Be luckier than Augustus and better than Trajan.'",
  [], ["src-tacitus"], "", 0.9)

p("hadrian", "哈德良", "Hadrian", 76, 138, "roman-empire",
  ["君主", "皇帝", "罗马", "建筑"], ["Ruler", "Emperor", "Rome", "Architecture"],
  "罗马帝国第十四任皇帝，建造哈德良长城，热爱希腊文化，以旅行和建筑著称。",
  "Fourteenth Roman emperor who built Hadrian's Wall, passionately loved Greek culture, and was renowned for travel and architecture.",
  "哈德良是图拉真的远房堂侄和养子。他做出了一项重大战略调整——放弃图拉真在东方征服的部分领土，改为防御性边界政策。他亲自巡视了帝国的每一个行省，在不列颠北部修建了著名的哈德良长城。他是一位狂热的希腊文化爱好者——蓄须（除尼禄外第一个蓄须的皇帝）、重建万神殿、在蒂沃利建造了规模宏大的别墅。他与美少年安提诺乌斯的关系及其早逝后的哀悼也是著名的历史典故。",
  "Hadrian, Trajan's distant cousin and adopted son, made a dramatic strategic shift — abandoning some of Trajan's eastern conquests in favor of defensive frontiers. He personally toured every province of the empire and built the famous Hadrian's Wall across northern Britain. A passionate Hellenophile, he was the first emperor after Nero to wear a beard, rebuilt the Pantheon, and constructed an enormous villa at Tivoli. His relationship with the youth Antinous and his extravagant mourning after the boy's death are also famous historical episodes.",
  [], ["src-tacitus"], "", 0.85)

p("marcus-aurelius", "马可·奥勒留", "Marcus Aurelius", 121, 180, "roman-empire",
  ["君主", "皇帝", "罗马", "哲学"], ["Ruler", "Emperor", "Rome", "Philosophy"],
  "罗马帝国第十六任皇帝，斯多葛派哲学家，《沉思录》的作者，五贤帝的最后一位。",
  "Sixteenth Roman emperor, Stoic philosopher and author of 'Meditations,' the last of the Five Good Emperors.",
  "马可·奥勒留被称为「哲人王」——他在戎马倥偬的军帐中写下的《沉思录》是斯多葛哲学的巅峰之作。但他一生的绝大部分时间都在边境战争中度过——抗击沿多瑙河入侵的日耳曼部落和东方的帕提亚帝国。他面临瘟疫（安东尼大瘟疫）和叛乱，却始终以斯多葛的冷静和坚韧面对一切。他的悲剧在于将帝位传给了儿子康茂德——这个暴虐的继承人打破了将近一个世纪的养子继承传统，开启了罗马帝国的衰落。",
  "Marcus Aurelius is known as the 'Philosopher King' — his 'Meditations,' written in military tents between campaigns, is the pinnacle of Stoic philosophy. Yet he spent most of his reign fighting frontier wars against Germanic tribes along the Danube and the Parthian Empire in the east. He faced plague (the Antonine Plague) and rebellion, meeting everything with Stoic composure and resilience. His tragedy was passing the throne to his son Commodus — this tyrannical heir broke nearly a century of adoptive succession and began Rome's decline.",
  [], ["src-tacitus"], "", 0.9)

p("diocletian", "戴克里先", "Diocletian", 244, 311, "roman-empire",
  ["君主", "皇帝", "罗马", "改革"], ["Ruler", "Emperor", "Rome", "Reform"],
  "罗马帝国第五十一任皇帝，建立四帝共治制，发动最后一次大规模迫害基督徒，主动退位。",
  "Roman emperor who established the Tetrarchy, launched the last great persecution of Christians, and voluntarily abdicated.",
  "戴克里先在经历了三世纪危机——50年内26位皇帝被杀——之后上台。他推行了彻底的改革：将帝国分为东西两部各设正副皇帝（四帝共治）；重整行省和军队；实施价格管制法令。他发起了最后一次、也是最残酷的基督徒迫害。305年他成为极少数自愿退位的罗马皇帝，回到达尔马提亚的宫殿种菜——当后来有人请求他复出时，他回答说：「如果你看到我在花园里种的卷心菜，你就不会再要求我回去。」",
  "Diocletian rose amid the Crisis of the Third Century — 26 emperors killed in 50 years. His reforms were sweeping: dividing the empire into East and West each with senior and junior emperors (the Tetrarchy); reorganizing provinces and the military; and issuing price-control edicts. He launched the last and most brutal persecution of Christians. In 305, he became one of the few Roman emperors to voluntarily abdicate, retiring to his palace in Dalmatia to grow cabbages — when later asked to return to power, he replied: 'If you could see the cabbages I have grown in my garden, you would not ask me to go back.'",
  [], ["src-tacitus"], "", 0.85)

p("theodosius-i", "狄奥多西一世", "Theodosius I", 347, 395, "roman-empire",
  ["君主", "皇帝", "罗马"], ["Ruler", "Emperor", "Rome"],
  "罗马帝国最后一位统一皇帝，宣布基督教为国教，死后帝国永久分裂为东西两部分。",
  "The last emperor of a unified Rome; he made Christianity the state religion, and the empire permanently split upon his death.",
  "狄奥多西一世面临哥特人入侵和宗教分裂的双重挑战。他于380年颁布《帖撒罗尼迦敕令》，使尼西亚基督教成为罗马帝国唯一的合法宗教——这是基督教历史上的一个转折点。394年他暂时统一了帝国东西两部，但这是最后的统一——395年他去世时将帝国分给两个儿子：阿卡狄乌斯统治东部（延续为拜占庭帝国），霍诺留统治西部。他因帖撒罗尼迦屠杀事件被米兰主教安布罗斯要求忏悔，展现了教会对皇权日益增长的影响力。",
  "Theodosius I faced both Gothic invasions and religious schism. His Edict of Thessalonica in 380 made Nicene Christianity the sole legal religion of the empire — a turning point in Christian history. In 394 he briefly reunified East and West, but this was the last unification — at his death in 395 he divided the empire between his sons: Arcadius ruling East (continuing as Byzantium) and Honorius the West. His forced penance by Bishop Ambrose of Milan after the Thessalonica massacre demonstrated the growing power of the Church over the throne.",
  [], [], "", 0.85)

# ============ BYZANTINE (5 new) ============
p("heraclius", "希拉克略", "Heraclius", 575, 641, "byzantine",
  ["君主", "皇帝", "拜占庭"], ["Ruler", "Emperor", "Byzantium"],
  "拜占庭帝国皇帝，击败萨珊波斯收复真十字架，但无法阻止阿拉伯帝国的崛起。",
  "Byzantine emperor who defeated Sassanid Persia and recovered the True Cross, but could not stop the Arab conquests.",
  "希拉克略在帝国最危急的时刻夺取政权——萨珊波斯已经占领了叙利亚、巴勒斯坦和埃及，兵临君士坦丁堡城下。他发动了一系列大胆的反攻深入波斯腹地，627年在尼尼微战役中大败波斯，收复了耶路撒冷和被掳走的真十字架。但正当帝国精疲力竭之时，新兴的阿拉伯穆斯林军队发动了闪电般的征服——叙利亚、巴勒斯坦、埃及在短短几年内全部丧失。希拉克略赢了一场伟大的战争，却输掉了中东的千年格局。",
  "Heraclius seized power at the empire's darkest hour — Sassanid Persia had taken Syria, Palestine, and Egypt, threatening Constantinople itself. He launched daring counter-offensives deep into Persia, decisively defeating them at Nineveh in 627 and recovering Jerusalem and the captured True Cross. But as both empires lay exhausted, the newly energized Arab Muslim armies launched lightning conquests — Syria, Palestine, and Egypt fell within years. Heraclius won a great war but lost the millennium-long Near Eastern order.",
  [], ["src-procopius"], "", 0.8)

p("basil-ii", "巴西尔二世", "Basil II", 958, 1025, "byzantine",
  ["君主", "皇帝", "拜占庭", "军事"], ["Ruler", "Emperor", "Byzantium", "Military"],
  "拜占庭马其顿王朝皇帝，「保加利亚屠夫」，将帝国疆域扩展至自查士丁尼以来的最大范围。",
  "Macedonian-dynasty emperor known as the 'Bulgar-Slayer,' who expanded the empire to its greatest extent since Justinian.",
  "巴西尔二世是拜占庭最能干的军事皇帝之一。他一生未娶、生活简朴，全身心投入战争和治理。他对保加利亚进行了长达数十年的残酷战争——1014年克雷迪昂战役后他将15,000名保加利亚战俘每百人留一人单眼带路回国，保加利亚沙皇据说被活活吓死。他征服了保加利亚、亚美尼亚和格鲁吉亚部分地区，使拜占庭帝国版图达到自查士丁尼以来最大。他临终时帝国空前强大，但继承人的无能很快将这一切葬送。",
  "Basil II was among Byzantium's most capable soldier-emperors. Never marrying and living spartanly, he devoted himself entirely to war and governance. He waged decades of brutal warfare against Bulgaria — after the Battle of Kleidion in 1014, he blinded 15,000 prisoners, leaving every hundredth man one eye to guide them home; the Bulgarian tsar reportedly died of shock. He conquered Bulgaria, parts of Armenia and Georgia, extending the empire to its largest since Justinian. He died with the empire at unprecedented strength, only for incompetent successors to squander it.",
  [], [], "", 0.8)

p("alexios-i", "阿莱克修斯一世", "Alexios I Komnenos", 1048, 1118, "byzantine",
  ["君主", "皇帝", "拜占庭", "十字军"], ["Ruler", "Emperor", "Byzantium", "Crusades"],
  "拜占庭科穆宁王朝开创者，请求西方援助对抗塞尔柱突厥，间接引发第一次十字军东征。",
  "Founder of the Komnenian dynasty whose appeal for Western aid against the Seljuk Turks inadvertently triggered the First Crusade.",
  "阿莱克修斯在拜占庭内外交困——塞尔柱突厥占领了安纳托利亚大部、诺曼人从西面入侵——时夺取皇位。他以高超的政治手腕周旋于多重威胁之间。1095年他向教皇乌尔班二世派遣使者请求雇佣兵援助，结果出乎意料——教皇在克莱蒙会议上号召了第一次十字军东征，数万西欧骑士涌入帝国领土。他在利用十字军收复失地的同时巧妙控制他们不威胁帝国安全。他的女儿安娜·科穆宁在《阿莱克修斯传》中留下了珍贵的记录。",
  "Alexios seized power when Byzantium was besieged on all fronts — Seljuk Turks held most of Anatolia, Normans attacked from the west. He navigated multiple threats with consummate political skill. In 1095, he sent envoys to Pope Urban II requesting mercenary aid, but the result was unexpected — the Pope's call at Clermont launched the First Crusade, and tens of thousands of Western knights flooded into imperial territory. He used the Crusaders to reclaim lost lands while skillfully preventing them from threatening the empire. His daughter Anna Komnene left an invaluable record in 'The Alexiad.'",
  [], ["src-alexiad"], "", 0.85)

p("constantine-xi", "君士坦丁十一世", "Constantine XI Palaiologos", 1405, 1453, "byzantine",
  ["君主", "皇帝", "拜占庭"], ["Ruler", "Emperor", "Byzantium"],
  "拜占庭帝国末代皇帝，1453年君士坦丁堡陷落时战死在城墙上，以一千年帝国的悲壮尾声载入史册。",
  "The last Byzantine emperor who died fighting on the walls as Constantinople fell in 1453 — the tragic finale of a millennium-old empire.",
  "君士坦丁十一世接手的拜占庭帝国已萎缩为君士坦丁堡及周边几个零碎领地。1453年奥斯曼苏丹穆罕默德二世率领大军包围了这座城市。君士坦丁率领约7,000守军（包括热那亚雇佣兵）抵抗了将近两个月。5月29日凌晨总攻发动后城墙被突破，他脱下皇袍冲入混战——此后再无人见到他的遗体。他的英勇战死为已持续1,123年的罗马帝国（及其继承者拜占庭）画上了句号。他的传奇在希腊民间演化为「大理石皇帝」的传说——人们相信他并未真正死去，终有一日将归来。",
  "Constantine XI inherited a Byzantium reduced to little more than Constantinople and scattered fragments. In 1453, Ottoman Sultan Mehmed II besieged the city with overwhelming force. Constantine led about 7,000 defenders (including Genoese mercenaries) in resisting for nearly two months. When the walls were breached in the final assault before dawn on May 29, he tore off his imperial insignia and charged into the melee — his body was never found. His heroic death marked the end of the Roman Empire (and its Byzantine continuation) after 1,123 years. His legend lives on in Greek folklore as the 'Marble Emperor' — believed not truly dead, destined one day to return.",
  [], [], "", 0.85)

# ============ ENGLAND / UK (10 new) ============
p("henry-ii", "亨利二世", "Henry II", 1133, 1189, "england",
  ["君主", "国王", "英格兰", "金雀花王朝"], ["Ruler", "King", "England", "Plantagenet"],
  "英格兰金雀花王朝首位国王，建立普通法体系，但其统治因与坎特伯雷大主教的冲突而蒙上阴影。",
  "First Plantagenet king who established the common law system, though his reign was overshadowed by conflict with the Archbishop of Canterbury.",
  "亨利二世通过母亲玛蒂尔达继承了英格兰王位，通过父亲继承了安茹和诺曼底，通过婚姻获得了阿基坦——他的「安茹帝国」横跨英吉利海峡两岸。他对英国法律体系的贡献是奠基性的：巡回法庭、陪审团制度和普通法的雏形均在他的治下成形。但他与挚友转敌人——坎特伯雷大主教托马斯·贝克特——的冲突以贝克特在坎特伯雷大教堂被刺杀达到顶峰，亨利被迫赤脚走到教堂前接受鞭笞忏悔。他的晚年被儿子们的叛乱所困扰。",
  "Henry II inherited England through his mother Matilda, Anjou and Normandy through his father, and Aquitaine through marriage — his 'Angevin Empire' straddled the Channel. His contribution to English law was foundational: circuit courts, jury trials, and the common law took shape under his rule. But his conflict with friend-turned-foe Thomas Becket, Archbishop of Canterbury, climaxed in Becket's murder in Canterbury Cathedral; Henry was forced to walk barefoot to the cathedral and be flogged in penance. His final years were troubled by his sons' rebellions.",
  [], [], "", 0.85)

p("richard-i", "理查一世（狮心王）", "Richard I (the Lionheart)", 1157, 1199, "england",
  ["君主", "国王", "英格兰", "十字军", "军事"], ["Ruler", "King", "England", "Crusades", "Military"],
  "英格兰国王，第三次十字军东征的传奇英雄，以卓越的军事才能而非治国能力著称。",
  "King of England and legendary hero of the Third Crusade, celebrated for military prowess rather than governance.",
  "理查一世在英格兰统治的十年中只有大约六个月待在英格兰——其余时间在十字军东征、战场上或被囚禁。他是他那个时代最卓越的战士——在阿苏夫战役中击败了萨拉丁的大军。他在归途中被奥地利公爵利奥波德俘虏并被神圣罗马帝国皇帝亨利六世关押，英格兰人民缴纳了相当于数年财政收入的巨额赎金才将他赎回。他最后在围攻法国一座不起眼城堡时中箭身亡。他是一位伟大的战士国王，但作为统治者却并不出色——他的名言是「如果能找到买家，我会把伦敦也卖掉」。",
  "Richard spent only about six months of his ten-year reign in England — the rest was consumed by crusading, campaigning, or captivity. He was the greatest warrior of his age, defeating Saladin's army at the Battle of Arsuf. Captured by Duke Leopold of Austria and imprisoned by Emperor Henry VI on his return journey, he was ransomed by England for a sum equivalent to several years' royal revenue. He died from a crossbow bolt while besieging an insignificant French castle. A great warrior-king but a mediocre ruler — he famously declared he would sell London if he could find a buyer.",
  ["Richard Coeur de Lion"], [], "", 0.85)

p("king-john", "约翰王", "King John", 1166, 1216, "england",
  ["君主", "国王", "英格兰"], ["Ruler", "King", "England"],
  "英格兰国王，因其失败统治被迫签署《大宪章》，为英国宪政传统奠基了基础。",
  "King of England whose failed rule forced him to sign the Magna Carta, laying the foundation for English constitutional tradition.",
  "约翰是亨利二世最小的儿子，因早年在爱尔兰的失败被称为「无地王」。他即位后几乎每件事都在出错——与教皇英诺森三世发生冲突导致英格兰被禁教令制裁、丢失诺曼底等大陆领地、滥征重税激怒贵族。1215年反叛的贵族在兰尼米德草原上迫使他签署了《大宪章》——一份限制王权的里程碑式文件，确立了「国王在法律之下」的原则。虽然约翰当时就想推翻它，但大宪章的精神在随后的世纪中生根发芽，成为英国乃至世界宪政主义的基石。",
  "John, Henry II's youngest son, was nicknamed 'Lackland' after his early failures in Ireland. As king, almost everything went wrong: conflict with Pope Innocent III brought England under interdict, he lost Normandy and other continental possessions, and his heavy taxation enraged the barons. In 1215, rebel barons forced him to sign the Magna Carta at Runnymede — a landmark document limiting royal power and establishing the principle that the king is under law. Though John immediately sought to overturn it, Magna Carta's spirit took root over subsequent centuries, becoming a cornerstone of English and global constitutionalism.",
  [], [], "", 0.85)

p("edward-i", "爱德华一世", "Edward I", 1239, 1307, "england",
  ["君主", "国王", "英格兰", "军事"], ["Ruler", "King", "England", "Military"],
  "英格兰国王，「苏格兰之锤」，征服威尔士，强化议会制度，以铁腕和法律著称。",
  "King of England known as the 'Hammer of the Scots,' conqueror of Wales, and strengthener of Parliament.",
  "爱德华一世身材高大——被称为「长腿爱德华」——是英格兰最令人敬畏的中世纪国王。他征服了威尔士并在当地修建了一系列宏伟城堡（至今仍矗立）；他试图征服苏格兰，虽然击败了威廉·华莱士，但苏格兰的抵抗在罗伯特·布鲁斯的领导下持续不断。他开创了「模范议会」模式——吸收各阶层代表参与决策——奠定了英国议会制度的基础。他的法律制度也经过重大改革，许多法规沿用数百年。",
  "Edward I, towering in stature and nicknamed 'Longshanks,' was England's most formidable medieval king. He conquered Wales and built a chain of magnificent castles that still stand; he campaigned to subjugate Scotland, defeating William Wallace, though Scottish resistance continued under Robert the Bruce. He pioneered the 'Model Parliament' — bringing representatives from all estates into governance — laying foundations for the British parliamentary system. His legal reforms produced statutes that endured for centuries.",
  [], [], "", 0.85)

p("henry-viii", "亨利八世", "Henry VIII", 1491, 1547, "england",
  ["君主", "国王", "英格兰", "宗教改革"], ["Ruler", "King", "England", "Reformation"],
  "英格兰都铎王朝第二位国王，以六次婚姻和发动英国宗教改革脱离罗马教廷而闻名。",
  "Second Tudor monarch, famous for his six marriages and for breaking with Rome to launch the English Reformation.",
  "亨利八世年轻时是英俊的「文艺复兴君主」——会多国语言、擅长音乐和运动。但他对男性继承人的执念彻底改变了英国历史。教皇拒绝批准他与凯瑟琳王后的离婚后，他于1534年通过《至尊法案》宣布自己为英格兰教会最高领袖，与罗马教廷决裂。他解散修道院、将教会财富收归王室，但也处决了任何反对者——包括他的首席大臣托马斯·莫尔。他的六位王后以悲惨命运著称：离婚、斩首、死亡、离婚、斩首、存活。",
  "Young Henry VIII was the handsome 'Renaissance prince' — multilingual, musical, and athletic. But his obsession with producing a male heir transformed English history. When the Pope refused his divorce from Catherine of Aragon, Henry broke with Rome through the 1534 Act of Supremacy, making himself Supreme Head of the Church of England. He dissolved monasteries, seized Church wealth, and executed dissenters — including his former chancellor Thomas More. His six wives are remembered by their tragic fates: divorced, beheaded, died, divorced, beheaded, survived.",
  [], [], "", 0.9)

p("charles-i", "查理一世", "Charles I", 1600, 1649, "england",
  ["君主", "国王", "英格兰", "内战"], ["Ruler", "King", "England", "Civil War"],
  "英格兰斯图亚特王朝国王，因与议会的冲突引发英国内战，最终被审判处决——欧洲第一个被公开处决的君主。",
  "Stuart king whose conflict with Parliament sparked the English Civil War, leading to his trial and execution — the first European monarch publicly executed.",
  "查理一世坚信「君权神授」——国王只对上帝负责。这种信念导致他与议会持续冲突：他解散了三次议会，曾实行十一年的「个人统治」不经议会征税。1642年内战爆发，奥利弗·克伦威尔领导的新模范军最终击败了保王党。1649年查理被审判并定罪——他的最后演说中仍坚持「君主和臣民的自由在于法律的统治」——然后在白厅的断头台上被斩首。他的处决震撼了整个欧洲，也标志着英格兰共和制的短暂实验。",
  "Charles I was convinced of the 'Divine Right of Kings' — that he answered only to God. This conviction led to relentless conflict with Parliament: he dissolved three Parliaments and ruled for eleven years of 'Personal Rule' without parliamentary taxation. Civil war erupted in 1642, and Oliver Cromwell's New Model Army ultimately defeated the Royalists. Charles was tried and convicted in 1649 — his final speech still insisted 'the liberty of the subject consists in the government of laws' — then beheaded on a scaffold at Whitehall. His execution shocked Europe and inaugurated England's brief experiment with republicanism.",
  [], [], "", 0.9)

p("victoria", "维多利亚女王", "Queen Victoria", 1819, 1901, "england",
  ["君主", "女王", "大英帝国"], ["Ruler", "Queen", "British Empire"],
  "大不列颠及爱尔兰联合王国女王兼印度女皇，维多利亚时代是英国工业革命和帝国扩张的鼎盛期。",
  "Queen of the United Kingdom and Empress of India; the Victorian era was the zenith of British industrialization and imperial expansion.",
  "维多利亚18岁即位，在位63年——是英国历史上最长的统治之一。她统治的时期被称为「维多利亚时代」：工业革命加速发展、铁路网覆盖全国、大英帝国扩张至全球四分之一陆地（「日不落帝国」）、伦敦成为世界金融中心。她与阿尔伯特亲王的婚姻是英国王室罕见的爱情故事——阿尔伯特去世后她穿黑衣哀悼40年。她的九个子女与欧洲各国王室联姻，使她成为「欧洲的祖母」。",
  "Victoria ascended at 18 and reigned for 63 years — among the longest in British history. Her era, the 'Victorian Age,' saw the Industrial Revolution accelerate, railways network the nation, the British Empire expand to cover a quarter of the globe ('the empire on which the sun never sets'), and London become the world's financial center. Her marriage to Prince Albert was a rare royal love story — she wore black in mourning for 40 years after his death. Her nine children married into royal houses across Europe, earning her the title 'Grandmother of Europe.'",
  [], [], "", 0.9)

p("louis-ix", "路易九世（圣路易）", "Louis IX (Saint Louis)", 1214, 1270, "france",
  ["君主", "国王", "法兰西", "十字军", "圣徒"], ["Ruler", "King", "France", "Crusades", "Saint"],
  "法兰西卡佩王朝国王，唯一被封圣的法国国王，以公正和虔诚著称。",
  "Capetian king of France, the only French monarch to be canonized, renowned for justice and piety.",
  "路易九世是他那个时代基督教世界的道德楷模。他在巴黎修建了圣礼拜堂来珍藏耶稣的荆冠；他创立了法国最高法院雏形——国王亲自在万塞纳的橡树下为臣民主持公道；他领导了第七次和第八次十字军东征——第一次虽然失败被俘但以身赎之，第二次在突尼斯死于瘟疫。他对穷人慷慨、对司法严格、对信仰虔诚——1297年被教皇卜尼法斯八世封圣。但他的统治也伴随着对犹太人的迫害——强制佩戴标记、焚烧《塔木德》。",
  "Louis IX was the moral exemplar of Christendom. He built Sainte-Chapelle in Paris to house the Crown of Thorns; established the precursor of France's supreme court, personally dispensing justice under an oak at Vincennes; and led the Seventh and Eighth Crusades — captured in the first but ransoming himself, dying of plague in the second at Tunis. Generous to the poor, strict in justice, devout in faith — he was canonized in 1297. Yet his reign also saw persecution of Jews — compulsory badges and Talmud burnings.",
  [], [], "", 0.85)

# ============ FRANCE (7 new) ============
p("philip-ii-augustus", "腓力二世·奥古斯都", "Philip II Augustus", 1165, 1223, "france",
  ["君主", "国王", "法兰西", "军事"], ["Ruler", "King", "France", "Military"],
  "法兰西卡佩王朝国王，将法兰西从一个小王国转变为欧洲最强大的君主国之一。",
  "Capetian king who transformed France from a small kingdom into one of Europe's most powerful monarchies.",
  "腓力二世是卡佩王朝最伟大的国王之一。他巧妙地利用了英格兰金雀花王朝的内部矛盾——特别是约翰王与理查一世的冲突。他与狮心王理查一同参加第三次十字军东征，但提前返回法国并趁理查不在时蚕食其领地。在布汶战役中他取得了决定性胜利——击败了神圣罗马帝国皇帝奥托四世和英格兰的联军——这场战役被视为法兰西民族意识觉醒的标志性时刻。他还修建了巴黎城墙、卢浮宫要塞、铺设了巴黎最早的街道。",
  "Philip II was among the greatest Capetian kings. He skillfully exploited the internal conflicts of the Angevin empire — especially between King John and Richard I. He joined Richard on the Third Crusade but returned early to nibble at Angevin territories. At the Battle of Bouvines, he won a decisive victory against the combined forces of Emperor Otto IV and England — a battle seen as a defining moment in the emergence of French national consciousness. He also built Paris's walls and the Louvre fortress, and paved the city's first streets.",
  [], [], "", 0.85)

p("philip-iv", "腓力四世（美男子）", "Philip IV (the Fair)", 1268, 1314, "france",
  ["君主", "国王", "法兰西"], ["Ruler", "King", "France"],
  "法兰西卡佩王朝国王，摧毁圣殿骑士团，将教廷迁至阿维尼翁。",
  "Capetian king who destroyed the Knights Templar and moved the Papacy to Avignon.",
  "腓力四世面貌英俊但冷酷无情。他为了筹措战争经费而不断扩展王权——向教会征税、驱逐犹太人和伦巴第银行家以没收财产、操纵货币贬值。他最大的成就是摧毁了圣殿骑士团——以异端和亵渎罪名逮捕并审判骑士团成员，最终在教皇默许下将最后一任大团长雅克·德·莫莱火刑处死。他还强迫教皇克雷芒五世将教廷从罗马迁至阿维尼翁——开启了教皇的「巴比伦之囚」时期。传说莫莱在火刑柱上诅咒腓力和教皇一年内受审——两人确实在同一年去世。",
  "Philip IV was handsome in face but ruthless in action. To finance his wars, he relentlessly extended royal power — taxing the Church, expelling Jews and Lombard bankers to seize their assets, and manipulating currency. His greatest stroke was destroying the Knights Templar — arresting and trying them on heresy and blasphemy charges, and with papal acquiescence burning Grand Master Jacques de Molay at the stake. He also forced Pope Clement V to move the Papacy from Rome to Avignon — the 'Babylonian Captivity' of the Papacy. Legend says Molay cursed both Philip and the Pope from the pyre to face judgment within a year — both did die that same year.",
  [], [], "", 0.85)

p("francis-i", "弗朗索瓦一世", "Francis I", 1494, 1547, "france",
  ["君主", "国王", "法兰西", "文艺复兴"], ["Ruler", "King", "France", "Renaissance"],
  "法兰西瓦卢瓦王朝国王，法国文艺复兴的赞助人，将达芬奇带到法国。",
  "Valois king and great patron of the French Renaissance who brought Leonardo da Vinci to France.",
  "弗朗索瓦一世是典型的文艺复兴君主——热爱艺术、文学和建筑。他将达芬奇请到法国安度晚年（据说达芬奇在他怀中去世）；他大规模扩建枫丹白露宫和卢浮宫，创建了法兰西公学院；他确立法语为官方语言（维莱科特雷法令）。但他一生与神圣罗马帝国皇帝查理五世交战——1525年在帕维亚战役中被俘，在马德里被囚禁一年，付出了两个儿子作为人质的代价才获释。他的统治标志着法国从晚期中世纪走向文艺复兴鼎盛阶段。",
  "Francis I was the quintessential Renaissance monarch — passionate about art, literature, and architecture. He brought Leonardo da Vinci to spend his final years in France (legend holds the master died in his arms); expanded Fontainebleau and the Louvre; founded the Collège de France; and established French as the official language (Ordinance of Villers-Cotterêts). Yet he spent his life at war with Holy Roman Emperor Charles V — captured at Pavia in 1525, imprisoned in Madrid for a year, and released only after his two sons served as hostages. His reign marked France's transition from late medieval to high Renaissance.",
  [], [], "", 0.85)

p("henry-iv-france", "亨利四世", "Henry IV of France", 1553, 1610, "france",
  ["君主", "国王", "法兰西"], ["Ruler", "King", "France"],
  "法兰西波旁王朝首位国王，颁布《南特敕令》结束宗教战争，「想让每个农民锅里都有一只鸡」。",
  "First Bourbon king who ended the Wars of Religion with the Edict of Nantes and famously wished 'every peasant a chicken in his pot.'",
  "亨利四世原是胡格诺派（新教）领袖，经历了血腥的宗教战争后为继承王位改宗天主教——他的名言「巴黎值得一场弥撒」。1598年他颁布《南特敕令》赋予新教徒宗教自由，结束了撕裂法国三十余年的宗教内战。此后他全力重建被战争摧毁的国家——兴修水利和道路、鼓励农业和贸易，他的大臣苏利公爵说「耕牧是法国的两个乳房」。他的平民关怀使他成为法国最受爱戴的国王之一。1610年被狂热的天主教徒刺杀。",
  "Originally a Huguenot (Protestant) leader, Henry converted to Catholicism to inherit the throne after decades of religious war — quipping 'Paris is worth a Mass.' His 1598 Edict of Nantes granted Protestants religious freedom, ending over thirty years of civil war. He then devoted himself to rebuilding the devastated nation — constructing waterways and roads, encouraging agriculture and trade; his minister Sully declared 'ploughing and pasturage are the two breasts of France.' His populist touch made him one of France's best-loved monarchs. He was assassinated by a Catholic fanatic in 1610.",
  [], [], "", 0.85)

p("louis-xvi", "路易十六", "Louis XVI", 1754, 1793, "france",
  ["君主", "国王", "法兰西", "法国大革命"], ["Ruler", "King", "France", "French Revolution"],
  "法兰西波旁王朝末代国王，法国大革命中被推翻并送上断头台。",
  "Last Bourbon king of France, overthrown by the French Revolution and executed by guillotine.",
  "路易十六本质上是个好人——热爱制锁工艺远胜于治国。他即位时的法国已深陷债务危机，三级会议的召开本为解决问题，却点燃了革命的火焰。他试图逃跑（瓦伦逃亡事件）被捕后彻底失去了信用。1793年1月21日他在革命广场的断头台上被处决——他最后的遗言是「我清白地死去，原谅我的敌人，希望我的血能巩固法兰西的幸福。」他的王后玛丽·安托瓦内特也在同年被处决。他的死标志着法国千年君主制的终结。",
  "Louis XVI was fundamentally a decent man who loved lock-making far more than governing. France was already deep in debt when he inherited the throne; the convening of the Estates-General, intended to address the crisis, instead ignited revolution. His attempted escape (the Flight to Varennes) and subsequent capture destroyed his remaining credibility. On January 21, 1793, he was executed by guillotine in the Place de la Révolution — his last words: 'I die innocent; I forgive my enemies; I hope my blood may cement the happiness of France.' His queen Marie Antoinette met the same fate that year. His death ended a millennium of French monarchy.",
  [], [], "", 0.9)

p("napoleon-iii", "拿破仑三世", "Napoleon III", 1808, 1873, "france",
  ["君主", "皇帝", "法兰西", "现代化"], ["Ruler", "Emperor", "France", "Modernization"],
  "法兰西第二帝国皇帝，拿破仑一世的侄子，推动巴黎现代化改造和工业革命。",
  "Emperor of the Second French Empire, nephew of Napoleon I, who drove the modernization of Paris and industrial revolution.",
  "路易·拿破仑·波拿巴先是当选法兰西第二共和国总统，随后发动政变建立第二帝国自称拿破仑三世。他的统治是法国现代化的关键时期——他委托奥斯曼男爵进行巴黎大改造（现代巴黎的宽阔林荫道和下水道系统都是这一时期的产物）、推动铁路网络建设、与英国签订自由贸易协定。但在外交上他连连失误——墨西哥冒险失败，最终在普法战争中被俾斯麦击败在色当被俘。战后他流亡英国并在那里去世——他是马克思《路易·波拿巴的雾月十八日》的讽刺对象。",
  "Louis-Napoleon Bonaparte was first elected President of the Second Republic, then staged a coup to establish the Second Empire as Napoleon III. His reign was pivotal for French modernization — commissioning Baron Haussmann's transformation of Paris (the wide boulevards and sewer systems of modern Paris date from this era), expanding the railway network, and signing free-trade agreements with Britain. But his foreign policy was marked by failures — the Mexican adventure collapsed, and he was ultimately defeated by Bismarck in the Franco-Prussian War and captured at Sedan. He died in exile in England — the target of Marx's scathing 'The Eighteenth Brumaire of Louis Bonaparte.'",
  [], [], "", 0.85)

# ============ HOLY ROMAN EMPIRE (5) ============
p("otto-i", "奥托一世", "Otto I (the Great)", 912, 973, "holy-roman-empire",
  ["君主", "皇帝", "神圣罗马帝国"], ["Ruler", "Emperor", "Holy Roman Empire"],
  "神圣罗马帝国开创者，在莱希菲尔德战役中击败马扎尔人，962年由教皇加冕为皇帝。",
  "Founder of the Holy Roman Empire who defeated the Magyars at the Battle of Lechfeld and was crowned emperor by the Pope in 962.",
  "奥托一世继承父亲「捕鸟者」亨利的东法兰克王国王位。他首先镇压了国内公爵们的叛乱，然后在955年的莱希菲尔德战役中决定性地击败了威胁欧洲长达一个世纪的马扎尔骑兵——这场胜利标志着马扎尔人定居匈牙利并皈依基督教的开始。962年教皇约翰十二世在罗马为他加冕，标志着神圣罗马帝国的正式成立。此后他将教会纳入皇权管理体系，「奥托体系」——皇帝任命主教——成为此后帝国政治的核心特征。",
  "Otto I inherited the East Frankish kingdom from his father Henry the Fowler. He first crushed rebellious dukes, then at the Battle of Lechfeld in 955 decisively defeated the Magyar cavalry that had terrorized Europe for a century — this victory marked the beginning of Magyar settlement in Hungary and their conversion to Christianity. In 962, Pope John XII crowned him emperor in Rome, formally establishing the Holy Roman Empire. He then incorporated the Church into imperial governance — the 'Ottonian system' of emperor-appointed bishops became a core feature of imperial politics.",
  [], [], "", 0.85)

p("frederick-barbarossa", "腓特烈一世（巴巴罗萨）", "Frederick I (Barbarossa)", 1122, 1190, "holy-roman-empire",
  ["君主", "皇帝", "神圣罗马帝国", "十字军"], ["Ruler", "Emperor", "Holy Roman Empire", "Crusades"],
  "神圣罗马帝国霍亨斯陶芬王朝皇帝，长期与教皇和意大利城邦斗争，第三次十字军中溺水身亡。",
  "Hohenstaufen emperor who waged prolonged struggles against the Papacy and Italian cities; drowned during the Third Crusade.",
  "腓特烈一世因其红胡子而被称为「巴巴罗萨」。他试图恢复查理大帝时代的帝国权威——六次远征意大利与伦巴第联盟和教皇作战，虽在莱尼亚诺战役中被步兵击败，但通过外交手段达成了有利于帝国的和平。他在帝国内部重建了秩序和法律。1189年他响应第三次十字军东征的号召，率领大军跨越安纳托利亚，但1190年在渡河时溺水身亡——这一天降横祸导致德国十字军群龙无首。在中世纪德国传说中，巴巴罗萨并未真正死去，而是沉睡在图林根的基夫豪瑟山，等待德国需要他时醒来。",
  "Frederick I was called 'Barbarossa' for his red beard. He sought to restore the imperial authority of Charlemagne's era — six Italian expeditions against the Lombard League and Papacy, and though defeated by infantry at Legnano, he achieved favorable peace through diplomacy. Within the empire, he re-established order and law. In 1189, he answered the call of the Third Crusade and led a massive army across Anatolia, but drowned crossing a river in 1190 — this calamity left the German crusaders leaderless. In medieval German legend, Barbarossa never truly died but sleeps beneath the Kyffhäuser mountain, awaiting Germany's hour of need.",
  [], [], "", 0.85)

p("frederick-ii", "腓特烈二世", "Frederick II", 1194, 1250, "holy-roman-empire",
  ["君主", "皇帝", "神圣罗马帝国", "科学"], ["Ruler", "Emperor", "Holy Roman Empire", "Science"],
  "神圣罗马帝国皇帝兼西西里国王，「世界惊奇」，精通多门语言和科学，与教皇长期冲突。",
  "Holy Roman Emperor and King of Sicily called 'Stupor Mundi' (Wonder of the World), multilingual polymath who clashed bitterly with the Papacy.",
  "腓特烈二世是那个时代最非凡的人物——在西西里巴勒莫这个基督教、伊斯兰和犹太文化的交汇处长大。他通晓六种语言、撰写猎鹰训练专著、赞助科学实验和诗歌创作、建立那不勒斯大学。他通过外交而非战争从苏丹手中获得耶路撒冷（六次被教皇绝罚仍安然无恙），但这更加深了他与教廷的冲突——教皇称他为「启示录中的兽」。他的宫廷是欧洲最早的文艺复兴式文化中心。他去世后霍亨斯陶芬王朝迅速衰落——教皇成功地摧毁了他的一切。",
  "Frederick II was the most extraordinary figure of his age — raised in Palermo, Sicily, at the crossroads of Christian, Islamic, and Jewish cultures. He spoke six languages, wrote a treatise on falconry, sponsored scientific experiments and poetry, and founded the University of Naples. He obtained Jerusalem from the Sultan through diplomacy rather than war (unscathed despite six papal excommunications), though this only deepened his conflict with the Papacy — the Pope called him 'the Beast of the Apocalypse.' His court was Europe's earliest Renaissance cultural center. After his death, the Hohenstaufen dynasty crumbled — the Pope had successfully destroyed everything he built.",
  [], [], "", 0.85)

p("charles-v", "查理五世", "Charles V", 1500, 1558, "holy-roman-empire",
  ["君主", "皇帝", "神圣罗马帝国", "西班牙"], ["Ruler", "Emperor", "Holy Roman Empire", "Spain"],
  "神圣罗马帝国皇帝兼西班牙国王，统治着日不落帝国，与宗教改革和新教势力斗争。",
  "Holy Roman Emperor and King of Spain who ruled an empire on which the sun never set, grappling with the Reformation.",
  "查理五世通过继承获得了空前庞大的领土——哈布斯堡的奥地利、勃艮第、西班牙及其美洲帝国。他的帝国确实是「日不落」的。但他一生面临三大挑战：与法国弗朗索瓦一世的意大利战争、奥斯曼帝国在匈牙利的推进以及最重要的——马丁·路德的宗教改革。他亲自在沃尔姆斯会议上审问路德，但未能阻止新教的蔓延。1555年《奥格斯堡和约》确立了「教随国定」原则。心力交瘁的查理于1556年退位——将西班牙和尼德兰给儿子腓力二世，帝国给弟弟斐迪南一世——退居西班牙的修道院。",
  "Charles V inherited an unprecedentedly vast realm through dynastic marriage — Habsburg Austria, Burgundy, Spain, and its American empire. His dominions truly spanned the globe. Yet his reign faced three monumental challenges: the Italian Wars against Francis I of France, Ottoman advances in Hungary, and above all, Martin Luther's Reformation. He personally interrogated Luther at the Diet of Worms but could not stop Protestantism's spread. The 1555 Peace of Augsburg established 'cuius regio, eius religio' (whose realm, his religion). Exhausted, Charles abdicated in 1556 — giving Spain and the Netherlands to his son Philip II and the Empire to his brother Ferdinand I — retiring to a Spanish monastery.",
  [], [], "", 0.9)

p("maria-theresa", "玛丽亚·特蕾莎", "Maria Theresa", 1717, 1780, "holy-roman-empire",
  ["君主", "女皇", "神圣罗马帝国", "奥地利", "改革"], ["Ruler", "Empress", "Holy Roman Empire", "Austria", "Reform"],
  "哈布斯堡王朝唯一的女统治者，奥地利女大公、匈牙利和波希米亚女王，推行开明专制改革，生下16个子女其中包括玛丽·安托瓦内特。",
  "The only female Habsburg ruler, Archduchess of Austria and Queen of Hungary and Bohemia, who enacted enlightened absolutist reforms and gave birth to 16 children including Marie Antoinette.",
  "玛丽亚·特蕾莎23岁即位时立即遭到普鲁士腓特烈大帝的入侵——奥地利王位继承战争爆发。虽然被迫割让西里西亚，她成功保住了其余领土并使丈夫弗朗茨·斯蒂芬当选神圣罗马帝国皇帝。此后她推行了全面的现代化改革：统一行政和司法体系、削弱贵族特权、推行义务教育（特蕾莎学校改革）、促进工商业。她是一位虔诚的天主教徒但限制教会在世俗事务中的权力。她的16个子女通过婚姻使哈布斯堡家族的王室联姻网络达到顶峰——最著名也最不幸的是嫁到法国的小女儿玛丽·安托瓦内特。",
  "Maria Theresa inherited the throne at 23 and was immediately invaded by Frederick the Great of Prussia — triggering the War of the Austrian Succession. Though forced to cede Silesia, she preserved the rest and secured her husband Francis Stephen's election as Holy Roman Emperor. She then enacted comprehensive modernization: unifying administration and judiciary, curtailing noble privileges, mandating primary education (the Theresian school reform), and promoting commerce and industry. A devout Catholic, she nonetheless restricted Church power in secular affairs. Her 16 children took Habsburg marriage diplomacy to its peak — most famously and tragically her youngest daughter Marie Antoinette, married into France.",
  [], [], "", 0.85)

# ============ RUSSIA (5 new) ============
p("ivan-iii", "伊凡三世", "Ivan III (the Great)", 1440, 1505, "russia",
  ["君主", "大公", "俄罗斯"], ["Ruler", "Grand Prince", "Russia"],
  "莫斯科大公，摆脱金帐汗国统治，统一俄罗斯各公国，奠定沙皇俄国的基础。",
  "Grand Prince of Moscow who threw off the Golden Horde's yoke, unified Russian principalities, and laid the foundations of Tsarist Russia.",
  "伊凡三世在位期间将莫斯科大公国的领土扩大了三倍——通过征服、购买和联姻吞并了雅罗斯拉夫尔、诺夫哥罗德和特维尔等公国。他的标志性成就是1480年在乌格拉河对峙中不战而屈金帐汗国之兵——从此俄罗斯正式摆脱了蒙古统治。他迎娶了拜占庭末代皇帝的侄女索菲亚·帕列奥洛格，将拜占庭的双头鹰徽引入俄罗斯国徽，宣称莫斯科是「第三罗马」。他重建了克里姆林宫（意大利建筑师设计），颁布了第一部全国法典《伊凡三世法典》。",
  "Ivan III tripled the territory of the Grand Duchy of Moscow during his reign — conquering, purchasing, or marrying into principalities like Yaroslavl, Novgorod, and Tver. His signature achievement was the Great Stand on the Ugra River in 1480, where the Golden Horde withdrew without battle, ending Mongol suzerainty over Russia. He married Sophia Palaiologina, niece of the last Byzantine emperor, adopting the double-headed eagle and proclaiming Moscow the 'Third Rome.' He rebuilt the Kremlin (with Italian architects) and issued Russia's first national law code, the Sudebnik of 1497.",
  [], [], "", 0.85)

p("catherine-the-great", "叶卡捷琳娜大帝", "Catherine the Great", 1729, 1796, "russia",
  ["君主", "女皇", "俄罗斯", "启蒙运动"], ["Ruler", "Empress", "Russia", "Enlightenment"],
  "俄罗斯帝国女皇，发动政变夺取政权，推行开明专制，将俄罗斯打造为欧洲一流强国。",
  "Empress of Russia who seized power through a coup, enacted enlightened absolutism, and established Russia as a premier European power.",
  "叶卡捷琳娜原为德国小公国的公主，嫁给彼得三世后在一场政变中废黜丈夫夺取皇位。她与伏尔泰和狄德罗通信讨论启蒙思想，但俄罗斯的现实使她的改革有限度。她在位期间俄罗斯领土大幅扩张——吞并克里米亚、瓜分波兰（三次瓜分后波兰从地图上消失）、在黑海取得出海口。她大力赞助艺术和教育——建立斯莫尔尼女子学院和艾尔米塔什博物馆。她的统治被认为是俄罗斯的黄金时代之一——尽管农奴制在这一时期反而更加固化。",
  "Catherine was a minor German princess who, after marrying Peter III, deposed her husband in a coup and seized the throne. She corresponded with Voltaire and Diderot on Enlightenment ideas, though Russian realities limited her reforms. Her reign saw dramatic territorial expansion — annexing Crimea, partitioning Poland (which disappeared from the map after three partitions), and gaining access to the Black Sea. She was a great patron of arts and education — founding the Smolny Institute for noble girls and the Hermitage Museum. Her reign is regarded as a golden age of Russia — despite the paradox that serfdom actually tightened during her rule.",
  [], [], "", 0.9)

p("alexander-i", "亚历山大一世", "Alexander I", 1777, 1825, "russia",
  ["君主", "沙皇", "俄罗斯", "拿破仑战争"], ["Ruler", "Tsar", "Russia", "Napoleonic Wars"],
  "俄罗斯帝国沙皇，领导俄罗斯击败拿破仑入侵，维也纳会议的主导者之一。",
  "Tsar of Russia who led the nation's defeat of Napoleon's invasion and was a principal architect of the Congress of Vienna.",
  "亚历山大一世在位的早期以自由主义改革著称——他与友人组成「秘密委员会」讨论废除农奴制和宪法改革。但拿破仑的入侵——1812年六十万大军进犯——改变了一切。俄军实行焦土政策并不断后撤，而法军在被烧毁的莫斯科城中陷入绝境，最终从六十万人锐减至不足三万残兵撤退。亚历山大随后领导反法同盟追至巴黎，成为维也纳会议上的「欧洲救世主」。战后他越来越转向宗教神秘主义——他的突然去世催生了关于他假死隐居成为西伯利亚修士的传说。",
  "Alexander I's early reign was marked by liberal reform — his 'Secret Committee' of friends discussed abolishing serfdom and constitutional reform. But Napoleon's invasion — 600,000 troops in 1812 — changed everything. The Russian army employed scorched-earth tactics and kept retreating, while the French, trapped in burned Moscow, were reduced from 600,000 to fewer than 30,000 survivors on the retreat. Alexander then led the coalition to Paris and became the 'Savior of Europe' at the Congress of Vienna. He grew increasingly mystical and religious afterward — his sudden death spawned legends that he faked his death and became a Siberian hermit.",
  [], [], "", 0.85)

p("alexander-ii", "亚历山大二世", "Alexander II", 1818, 1881, "russia",
  ["君主", "沙皇", "俄罗斯", "改革"], ["Ruler", "Tsar", "Russia", "Reform"],
  "俄罗斯帝国沙皇，「解放者」，废除农奴制并推行一系列大改革，最终被民意党人刺杀。",
  "Tsar known as 'the Liberator' who abolished serfdom and enacted the Great Reforms, ultimately assassinated by revolutionaries.",
  "亚历山大二世在克里米亚战争失败后深刻认识到俄罗斯的落后。1861年他颁布了解放宣言废除了农奴制——解放了约2,300万农奴——这是俄罗斯历史上最重大的社会改革。此后他推行了一系列「大改革」：建立地方自治机构、改革司法系统（引入陪审团制度）、军队现代化。但他拒绝建立全国性议会，激进分子日渐不满。他在经历了多次暗杀未遂后——包括冬宫的炸弹爆炸——最终在1881年3月13日被民意党人投掷的炸弹炸成重伤身亡。讽刺的是，他当天原本要去签署一项建立有限代议制的法令。他的遇刺使俄罗斯走向了更加保守和反动的方向。",
  "Alexander II, humiliated by defeat in the Crimean War, recognized Russia's backwardness. In 1861, his Emancipation Manifesto abolished serfdom — freeing some 23 million serfs — the most momentous social reform in Russian history. He followed with the 'Great Reforms': local self-government (zemstvos), judicial reform (introducing jury trials), and military modernization. But his refusal to create a national assembly bred radical discontent. After surviving multiple assassination attempts — including a Palace bombing — he was mortally wounded by a revolutionary's bomb on March 13, 1881. Tragically, he had been on his way to sign a decree establishing limited representative government. His assassination pushed Russia toward greater conservatism and reaction.",
  [], [], "", 0.9)

p("nicholas-ii", "尼古拉二世", "Nicholas II", 1868, 1918, "russia",
  ["君主", "沙皇", "俄罗斯"], ["Ruler", "Tsar", "Russia"],
  "俄罗斯帝国末代沙皇，统治期间经历了一战和两次革命，最终全家被布尔什维克处决。",
  "The last Tsar of Russia, whose reign saw World War I and two revolutions, ending with his family's execution by the Bolsheviks.",
  "尼古拉二世是一个好人但却是糟糕的统治者——他对家庭充满爱心但缺乏治理庞大帝国的能力和意志。他的统治是一场接一场的灾难：加冕典礼上的霍登卡踩踏事件、对日战争失败、血腥星期日（和平请愿者遭枪杀）、1905年革命。建立杜马（议会）的让步总是很快收回。一战中他亲自担任最高统帅离开首都——将朝政留给皇后亚历山德拉和备受争议的「圣人」拉斯普京。1917年二月革命迫使他退位。他和家人被羁押一年后于1918年7月17日凌晨在叶卡捷琳堡的地下室被枪决——罗曼诺夫王朝三百余年的统治以一种残酷的方式终结。",
  "Nicholas II was a good man but a terrible ruler — devoted to his family but lacking the capacity and will to govern a vast empire. His reign was a procession of disasters: the Khodynka stampede at his coronation, defeat by Japan, Bloody Sunday (the shooting of peaceful petitioners), and the 1905 Revolution. His concessions — creating the Duma (parliament) — were invariably clawed back. In World War I, he took personal command of the army and left the capital, abandoning governance to Empress Alexandra and the controversial 'holy man' Rasputin. The February Revolution of 1917 forced his abdication. After a year of captivity, he and his family were shot in a Yekaterinburg basement in the early hours of July 17, 1918 — the brutal end of 300 years of Romanov rule.",
  [], [], "", 0.9)

# ============ OTTOMANS (4 new) ============
p("osman-i", "奥斯曼一世", "Osman I", 1258, 1326, "ottoman-empire",
  ["君主", "苏丹", "奥斯曼帝国"], ["Ruler", "Sultan", "Ottoman Empire"],
  "奥斯曼帝国创始人，以他的名字命名的帝国将延续六个多世纪。",
  "Founder of the Ottoman Empire, which would bear his name and endure for over six centuries.",
  "奥斯曼一世最初是安纳托利亚西北部一个不起眼的突厥部落首领。他利用拜占庭帝国衰落的时机不断扩张领土——他的「加齐」战士以圣战的名义进攻拜占庭边境。传说他曾梦见一棵大树从肚脐长出遮天蔽日——解释为他的王朝将统治世界。他去世时领土仍然不大，但已奠定了此后伟大帝国的基础。奥斯曼这个名字本身——在阿拉伯语中是「奥斯曼」——就是帝国最持久的遗产。",
  "Osman I began as the leader of an obscure Turkic tribe in northwestern Anatolia. Exploiting Byzantine decline, he steadily expanded — his 'ghazi' warriors raided the frontier in the name of holy war. A famous dream foretold a great tree growing from his navel to shade the world — interpreted as his dynasty's future dominion. At his death, his territory remained modest, but he had laid the foundation for what would become a great empire. The name 'Osman' — 'Uthman' in Arabic — is the empire's most enduring legacy.",
  [], [], "", 0.75)

p("selim-i", "塞利姆一世", "Selim I", 1470, 1520, "ottoman-empire",
  ["君主", "苏丹", "奥斯曼帝国", "军事"], ["Ruler", "Sultan", "Ottoman Empire", "Military"],
  "奥斯曼帝国苏丹，绰号「冷酷者」，征服埃及马穆鲁克王朝，将哈里发头衔带到伊斯坦布尔。",
  "Ottoman sultan known as 'the Grim' who conquered Mamluk Egypt and brought the Caliphate to Istanbul.",
  "塞利姆一世可能是奥斯曼王朝中最令人恐惧的苏丹——他首先在内战中击败并杀死了自己的兄弟，然后将矛头指向外部。他先后击败波斯萨法维帝国的伊斯玛仪一世——在查尔迪兰战役中——然后转向南方征服了整个马穆鲁克苏丹国（叙利亚、巴勒斯坦和埃及）。他将麦加和麦地那纳入奥斯曼保护之下，并将阿拔斯王朝末代哈里发带到伊斯坦布尔，使奥斯曼苏丹成为伊斯兰世界的最高宗教领袖。他仅在位8年却将奥斯曼领土扩大了一倍多——一个高效而无情的帝国建设者。",
  "Selim I may have been the most fearsome of the Ottoman sultans — he first defeated and killed his own brothers in a civil war, then turned outward. He defeated Shah Ismail I of Safavid Persia at Chaldiran, then swept south to conquer the entire Mamluk Sultanate — Syria, Palestine, and Egypt. He brought Mecca and Medina under Ottoman protection and transferred the last Abbasid caliph to Istanbul, making the Ottoman sultan the supreme religious leader of the Islamic world. He reigned only 8 years but more than doubled Ottoman territory — an efficient and ruthless empire-builder.",
  [], [], "", 0.85)

p("selim-ii", "塞利姆二世", "Selim II", 1524, 1574, "ottoman-empire",
  ["君主", "苏丹", "奥斯曼帝国"], ["Ruler", "Sultan", "Ottoman Empire"],
  "奥斯曼帝国苏丹，绰号「醉鬼」，勒班陀海战失败标志着奥斯曼海上霸权的衰落。",
  "Ottoman sultan known as 'the Sot'; the defeat at Lepanto marked the decline of Ottoman naval supremacy.",
  "塞利姆二世是苏莱曼大帝唯一存活的儿子，但与父亲截然相反——他沉溺于酒色，将朝政交给大维齐尔索库鲁·穆罕默德帕夏。在他的统治下奥斯曼征服了塞浦路斯，但1571年的勒班陀海战中神圣同盟摧毁了奥斯曼舰队——这是奥斯曼海军第一次遭受决定性失败。尽管舰队迅速重建，但经验丰富的水手和军官的损失无法弥补。勒班陀常被视为奥斯曼帝国长期衰落的起点——即使这种衰落要到几个世纪后才变得明显。",
  "Selim II was Suleiman the Magnificent's sole surviving son but his complete opposite — given to drink and pleasure, he left governance to Grand Vizier Sokollu Mehmed Pasha. Under his reign, the Ottomans conquered Cyprus, but in 1571 the Holy League destroyed the Ottoman fleet at the Battle of Lepanto — the first decisive Ottoman naval defeat. Though ships were rapidly rebuilt, the loss of experienced sailors and officers was irreplaceable. Lepanto is often seen as the beginning of the long Ottoman decline — even if that decline would take centuries to become evident.",
  [], [], "", 0.8)

p("murad-iv", "穆拉德四世", "Murad IV", 1612, 1640, "ottoman-empire",
  ["君主", "苏丹", "奥斯曼帝国"], ["Ruler", "Sultan", "Ottoman Empire"],
  "奥斯曼帝国苏丹，以铁腕恢复秩序，禁止咖啡酒精和烟草，亲自率军收复巴格达。",
  "Ottoman sultan who restored order with an iron fist, banned coffee, alcohol, and tobacco, and personally led the reconquest of Baghdad.",
  "穆拉德四世11岁即位，早期在母亲和后宫干政下长大。成年亲政后他以极端的手段恢复帝国秩序——禁止咖啡、酒精和烟草、晚上亲自微服巡逻并处决违法者。他是自苏莱曼大帝以来第一个亲自统兵作战的苏丹——1638年他徒步走在军队最前面穿越安纳托利亚收复了巴格达。他以残忍著称但也以重新确立了苏丹权威而闻名。他去世时仅27岁，死前下令处死自己的弟弟易卜拉欣——这道命令幸运地未被执行（否则奥斯曼王朝将没有继承人）。",
  "Murad IV ascended at 11, spending his early reign under his mother and harem influence. Once in personal control, he restored order through extreme measures — banning coffee, alcohol, and tobacco, personally patrolling the streets at night in disguise and executing violators. He was the first sultan since Suleiman to personally lead his troops into battle — in 1638, he marched at the head of his army on foot across Anatolia to recapture Baghdad. He was notorious for cruelty but also for reasserting sultanic authority. He died at 27, having ordered his brother Ibrahim's execution — mercifully, the order was not carried out (the Ottoman dynasty would otherwise have no heir).",
  [], [], "", 0.8)

# ============ PERSIA (5 new) ============
p("darius-i", "大流士一世", "Darius I", -550, -486, "persia",
  ["君主", "国王", "波斯", "阿契美尼德"], ["Ruler", "King", "Persia", "Achaemenid"],
  "波斯阿契美尼德王朝国王，将帝国治理推向顶峰，建立行省制和皇家大道。",
  "Achaemenid king who brought the Persian Empire to its administrative peak, establishing satrapies and the Royal Road.",
  "大流士一世在平定一场篡位危机后夺取了波斯王位。他的主要贡献不在于征服而在于治理——他将帝国划分为20个行省、修建了连接苏萨和萨迪斯的皇家大道（全长2,700公里）、引入统一的货币（大流克金币）、开创性地修建了苏伊士运河前身。他在贝希斯敦山崖上以三种楔形文字刻下了自己的功绩——这成为解读楔形文字的关键。但他发动了入侵希腊的远征，于公元前490年在马拉松战役中遭到失败——这只是一场更大规模入侵的序曲。",
  "Darius I seized power after quelling a usurpation crisis. His genius lay not in conquest but in administration — he divided the empire into 20 satrapies, built the Royal Road from Susa to Sardis (2,700 km), introduced a unified currency (the gold daric), and pioneered a precursor to the Suez Canal. He carved his achievements in three cuneiform scripts on the Behistun cliff — which became the key to deciphering cuneiform. But he also launched an invasion of Greece, defeated at Marathon in 490 BCE — merely the prelude to an even greater invasion.",
  [], [], "", 0.85)

p("xerxes-i", "薛西斯一世", "Xerxes I", -519, -465, "persia",
  ["君主", "国王", "波斯", "阿契美尼德"], ["Ruler", "King", "Persia", "Achaemenid"],
  "波斯阿契美尼德王朝国王，大流士之子，发动第二次希波战争——温泉关和萨拉米斯的传奇由此而来。",
  "Achaemenid king, son of Darius, who launched the second Persian invasion of Greece — giving rise to the legends of Thermopylae and Salamis.",
  "薛西斯一世继承父亲对希腊的复仇使命。他动员了古代世界最大规模的军队——据希罗多德记载超过百万（现代估计可能约20-30万）——跨越赫勒斯滂海峡搭建浮桥。他在温泉关击败了斯巴达国王列奥尼达和他那300勇士，焚毁了雅典，但随后在萨拉米斯海战中被雅典海军统帅地米斯托克利智取——狭窄的海峡使波斯舰队的数量优势变为劣势。他返回波斯后再也没有发动对希腊的远征。据希罗多德记载，当他眺望自己庞大的军队时曾落泪——因为百年之后这些人将无一在世。",
  "Xerxes inherited his father's mission of revenge against Greece. He mobilized the largest army the ancient world had seen — Herodotus claims over a million (modern estimates suggest perhaps 200,000-300,000) — crossing the Hellespont on pontoon bridges. He defeated Leonidas and his 300 Spartans at Thermopylae and burned Athens, but was then outmaneuvered by the Athenian admiral Themistocles at the naval Battle of Salamis, where the narrow straits neutralized Persian numerical superiority. He returned to Persia and never launched another Greek campaign. Herodotus records that while reviewing his vast army, Xerxes wept — because in a hundred years, not one of them would be alive.",
  [], [], "", 0.85)

p("shapur-i", "沙普尔一世", "Shapur I", 215, 270, "persia",
  ["君主", "国王", "波斯", "萨珊"], ["Ruler", "King", "Persia", "Sassanid"],
  "萨珊波斯第二位国王，在三次战役中击败罗马帝国，甚至俘虏了罗马皇帝瓦勒良。",
  "Second Sassanid king who defeated the Roman Empire in three campaigns, even capturing the Roman emperor Valerian.",
  "沙普尔一世继承父亲阿尔达希尔一世建立的萨珊王朝后展现了惊人的军事才能。他对罗马发动了一系列毁灭性战役——击败了三位罗马皇帝：戈尔迪安三世战死、阿拉伯人菲利普被迫求和、而瓦勒良皇帝被他俘虏（这是罗马历史上唯一一次在任皇帝被外敌俘虏）。他在纳克什·鲁斯塔姆的巨型岩壁上雕刻了瓦勒良跪在他面前的场景。他不仅是一位征服者——还赞助城市建设、促进贸易、对宗教持宽容态度（包括保护摩尼教的创始人摩尼）。",
  "Shapur I, inheriting the newly-founded Sassanid Empire from his father Ardashir I, displayed stunning military prowess. He waged a series of devastating campaigns against Rome, defeating three emperors: Gordian III was killed, Philip the Arab was forced to sue for peace, and Emperor Valerian was captured alive — the only time a Roman emperor was taken captive by a foreign enemy. Shapur commemorated this with colossal rock reliefs at Naqsh-e Rostam showing Valerian kneeling before him. He was not only a conqueror — he also sponsored city-building, promoted trade, and tolerated religious diversity, including protecting Mani, founder of Manichaeism.",
  [], [], "", 0.8)

p("khosrow-i", "库思老一世", "Khosrow I (Anushirvan)", 501, 579, "persia",
  ["君主", "国王", "波斯", "萨珊", "改革"], ["Ruler", "King", "Persia", "Sassanid", "Reform"],
  "萨珊波斯最伟大的国王之一，绰号「不朽的灵魂」，推行全面的行政改革并赞助学术。",
  "One of the greatest Sassanid kings, called 'Anushirvan' (Immortal Soul), who enacted comprehensive reforms and patronized scholarship.",
  "库思老一世的统治被视为萨珊波斯的黄金时代。他推行了全面的税务和行政改革——将土地税固定化、重整军队——使帝国恢复了财政稳定和军事实力。他赞助哲学和科学——在朱迪沙普尔建立了著名的学院，收留了因查士丁尼关闭雅典学院而流亡的希腊哲学家。他本人对印度象棋的引入起到了重要作用——《卡里来和笛木乃》寓言集也在他的赞助下从梵文翻译为波斯语。他在与拜占庭的战争中总体上占据上风，602-628年的毁灭性战争后萨珊波斯的衰落更反衬出他时代的辉煌。",
  "Khosrow I's reign is considered the golden age of Sassanid Persia. He enacted sweeping tax and administrative reforms — fixing land taxes and reorganizing the military — restoring fiscal stability and martial strength. He patronized philosophy and science, establishing the famous academy at Gundeshapur and offering refuge to Greek philosophers exiled by Justinian's closure of the Athenian Academy. He was instrumental in introducing Indian chess to Persia, and the fable collection 'Kalila wa Dimna' was translated from Sanskrit under his patronage. His general success against Byzantium stood in sharp contrast to the devastating war of 602-628 that would later bring Sassanid collapse.",
  [], [], "", 0.8)

p("abbas-i", "阿巴斯一世", "Abbas I (the Great)", 1571, 1629, "safavid-persia",
  ["君主", "沙阿", "波斯", "萨法维", "军事"], ["Ruler", "Shah", "Persia", "Safavid", "Military"],
  "萨法维波斯最伟大的沙阿，将帝国带入黄金时代，迁都伊斯法罕使其成为世界最美城市之一。",
  "Safavid Persia's greatest shah who brought the empire to its golden age, transforming Isfahan into one of the world's most beautiful cities.",
  "阿巴斯一世16岁即位时萨法维帝国正被内外敌人撕裂。成年后他展现了惊人的治国才能——改革军队（建立了火枪和炮兵部队）、从奥斯曼帝国收复失地、将葡萄牙人驱逐出霍尔木兹海峡。但最持久的遗产是他将首都从加兹温迁至伊斯法罕——他将这座城市建成了当时的建筑奇迹：伊玛目广场、阿里·卡普宫、谢赫·洛特福拉清真寺。他对欧洲外交开放，欢迎英国和荷兰商人。他的统治是波斯在伊斯兰时代最辉煌的时期之一——被后世称为「阿巴斯大帝」。",
  "Abbas I inherited a Safavid empire torn apart by enemies at 16. Reaching maturity, he displayed astonishing statecraft — reforming the army (creating musket and artillery corps), reconquering territory from the Ottomans, and expelling the Portuguese from the Strait of Hormuz. But his most enduring legacy was moving the capital from Qazvin to Isfahan, which he transformed into an architectural wonder: the Naqsh-e Jahan Square, Ali Qapu Palace, and Sheikh Lotfollah Mosque. He opened diplomacy with Europe, welcoming English and Dutch merchants. His reign was one of the most glorious periods of Islamic Persia — he is remembered as 'Abbas the Great.'",
  [], [], "", 0.85)

# ============ ANCIENT EGYPT (3 new) ============
p("hatshepsut", "哈特谢普苏特", "Hatshepsut", -1507, -1458, "egypt",
  ["君主", "法老", "古埃及", "女性"], ["Ruler", "Pharaoh", "Ancient Egypt", "Women"],
  "古埃及第十八王朝女法老，以男性形象统治，大力发展贸易和建筑。",
  "Female pharaoh of Egypt's Eighteenth Dynasty who ruled in male guise, vigorously promoting trade and monumental construction.",
  "哈特谢普苏特是古埃及最成功的女性统治者。她作为年幼的图特摩斯三世的摄政王开始掌权，但不久后便自称法老——穿戴全套法老服饰包括假胡须。她的统治以繁荣和和平为特征——她派遣大规模贸易远征队前往蓬特（可能是今天的索马里），带回了没药树、象牙、黄金和异国动物。她在代尔·埃尔-巴哈里建造了宏伟的神庙建筑群，被认为是古埃及建筑的最精美典范之一。她死后图特摩斯三世发动了有组织的记忆抹除行动——凿掉她的名字和雕像。",
  "Hatshepsut was ancient Egypt's most successful female ruler. She began as regent for the young Thutmose III but soon proclaimed herself pharaoh — wearing full regalia including the ceremonial false beard. Her reign was characterized by prosperity and peace — she sent a great trading expedition to Punt (likely modern Somalia), returning with myrrh trees, ivory, gold, and exotic animals. She built a magnificent temple complex at Deir el-Bahari, considered among the finest examples of ancient Egyptian architecture. After her death, Thutmose III launched a systematic campaign of erasure, chiseling out her names and images.",
  [], [], "", 0.8)

p("akhenaten", "阿肯那顿", "Akhenaten", -1380, -1334, "egypt",
  ["君主", "法老", "古埃及", "宗教改革"], ["Ruler", "Pharaoh", "Ancient Egypt", "Religious Reform"],
  "古埃及第十八王朝法老，推行一神教改革，崇拜唯一的太阳神阿顿，彻底颠覆了埃及宗教传统。",
  "Eighteenth Dynasty pharaoh who introduced monotheistic worship of the sun-disk Aten, radically upending Egyptian religious tradition.",
  "阿肯那顿原名阿蒙霍特普四世，在位的第五年他做出了一项惊人举措——废除埃及万神殿中的一切神祇，只崇拜太阳圆盘神阿顿，并将自己的名字改为阿肯那顿（「阿顿的仆人」）。他还在沙漠中建造了新首都阿克塔顿（今阿玛纳）。「阿玛纳时期」的艺术也发生了革命性变化——法老本人和他的家庭以更为自然主义甚至怪诞的形式被描绘。他的改革在他死后被迅速废除——他的儿子图坦卡蒙原名图坦卡顿——传统宗教全面恢复，阿肯那顿的名字被从法老名单上抹去。",
  "Originally named Amenhotep IV, Akhenaten in his fifth regnal year did something astonishing — he abolished all gods of the Egyptian pantheon, worshipping only the sun-disk Aten, and changed his name to Akhenaten ('Servant of Aten'). He built a new capital, Akhetaten (modern Amarna), in the desert. The art of the 'Amarna Period' also underwent a revolution — the pharaoh and his family were depicted in a startlingly naturalistic, even grotesque, style. His revolution was swiftly reversed after his death — his son Tutankhamun was originally named Tutankhaten — and traditional religion was fully restored, Akhenaten's name expunged from the king lists.",
  [], [], "", 0.8)

p("tutankhamun", "图坦卡蒙", "Tutankhamun", -1341, -1323, "egypt",
  ["君主", "法老", "古埃及"], ["Ruler", "Pharaoh", "Ancient Egypt"],
  "古埃及第十八王朝法老，少年早逝，因其陵墓在1922年被完好发现而闻名于世。",
  "Eighteenth Dynasty pharaoh who died young, world-famous for the intact discovery of his tomb in 1922.",
  "图坦卡蒙9岁即位，在位约十年——他执政期间最重要的事可能是将国教从阿肯那顿的一神教恢复为传统的多神教。但他真正举世闻名的原因是在1922年——霍华德·卡特在帝王谷发现了几乎完好无损的图坦卡蒙陵墓。墓中出土了超过5,000件珍宝——最著名的是11公斤的纯金面具——是埃及学史上最轰动的考古发现。卡特打开墓室时那句「我看到了奇妙的东西」已成为名言。他的早逝原因长期成谜——最近的CT扫描显示他可能有骨骼疾病且腿骨折可能是致命因素。",
  "Tutankhamun ascended at around 9 and reigned for roughly a decade — the most significant act of his reign was probably restoring traditional polytheism after Akhenaten's monotheism. But his true world fame came in 1922, when Howard Carter discovered his nearly intact tomb in the Valley of the Kings. Over 5,000 treasures were recovered — most famously the 11-kilogram solid gold death mask — the most sensational archaeological find in Egyptology. Carter's words upon first peering into the chamber — 'I see wonderful things' — have become legendary. The cause of his early death was long mysterious; recent CT scans suggest bone disease and a leg fracture may have been fatal factors.",
  ["图坦卡门", "King Tut"], [], "", 0.85)

# ============ JAPAN (5 new) ============
p("empress-suiko", "推古天皇", "Empress Suiko", 554, 628, "japan",
  ["君主", "天皇", "日本", "女性"], ["Ruler", "Emperor", "Japan", "Women"],
  "日本第一位女性天皇，圣德太子摄政期间推行大化改新前的一系列改革。",
  "Japan's first reigning empress; during her reign, Prince Shotoku served as regent and enacted reforms preceding the Taika era.",
  "推古天皇是日本第33代天皇，也是第一位有明确史料记载的女性天皇。她在位期间由侄子圣德太子担任摄政——这是日本历史上最具创造力的政治和文化时期之一。圣德太子制定了《十七条宪法》、建立了冠位十二阶的官僚等级制、派遣遣隋使向中国学习、大力推广佛教。推古天皇本人也以坚定支持这些改革而著称。她的统治标志着日本从部落氏族联盟向中央集权律令国家的重大转变。",
  "Empress Suiko was Japan's 33rd sovereign and the first female emperor with clear historical documentation. Her reign was guided by her nephew Prince Shotoku as regent — one of the most creative political and cultural periods in Japanese history. Prince Shotoku drafted the Seventeen-Article Constitution, established a twelve-level cap-rank bureaucracy, sent envoys to Sui China, and vigorously promoted Buddhism. Empress Suiko herself was a steadfast supporter of these reforms. Her reign marked Japan's major transition from tribal-clan confederation toward centralized bureaucratic state.",
  ["Suiko-tenno"], [], "", 0.75)

p("emperor-kammu", "桓武天皇", "Emperor Kammu", 737, 806, "japan",
  ["君主", "天皇", "日本"], ["Ruler", "Emperor", "Japan"],
  "日本第50代天皇，迁都平安京（京都），开启了辉煌的平安时代。",
  "Japan's 50th emperor who moved the capital to Heian-kyo (Kyoto), inaugurating the brilliant Heian Period.",
  "桓武天皇在位期间做出了一项影响日本千年历史的决定——将都城从奈良迁往平安京（即京都）。迁都的原因包括摆脱奈良佛教寺院的强大政治影响力。新都的规划以唐代长安为蓝本，街道呈棋盘状布局。平安京作为日本首都超过一千年——直到1868年迁都东京——平安时代成为日本古典文化最辉煌的时期，《源氏物语》和《枕草子》等世界文学瑰宝诞生于此。",
  "Emperor Kammu made a decision during his reign that would shape Japan for a millennium — moving the capital from Nara to Heian-kyo (Kyoto). The move was partly motivated by the desire to escape the powerful political influence of Nara's Buddhist temples. The new city was laid out in a grid pattern modeled on Tang-dynasty Chang'an. Heian-kyo remained Japan's capital for over a thousand years — until the move to Tokyo in 1868 — and the Heian Period became the zenith of classical Japanese culture, producing world literary treasures like 'The Tale of Genji' and 'The Pillow Book.'",
  ["Kammu-tenno"], [], "", 0.8)

p("oda-nobunaga", "织田信长", "Oda Nobunaga", 1534, 1582, "japan",
  ["君主", "大名", "日本", "战国", "军事"], ["Ruler", "Daimyo", "Japan", "Sengoku", "Military"],
  "日本战国时代大名，以「天下布武」为口号，率先使用火枪改变了日本战争方式。",
  "Sengoku-period daimyo who, under the slogan 'Rule the Realm by Force,' pioneered the use of firearms in Japanese warfare.",
  "织田信长是日本统一事业的第一位伟大推动者。他以尾张国为据点，先后击败今川义元（桶狭间之战）、浅井朝仓联盟、武田胜赖（长篠之战——火枪的三段击战术在此战中达到顶峰）。他残酷镇压佛教一向一揆起义，火烧比叡山延历寺。他是一位彻底的现实主义者——拥抱基督教传教士和西方火器技术——同时也是一个暴君。1582年他在京都本能寺被部下明智光秀背叛——「敌人就在本能寺」——被迫自杀。他的统一事业由丰臣秀吉完成。",
  "Oda Nobunaga was the first great unifier of Japan. From his base in Owari Province, he successively defeated Imagawa Yoshimoto (Battle of Okehazama), the Azai-Asakura alliance, and Takeda Katsuyori (Battle of Nagashino, where rotating volley fire with arquebuses reached its apogee). He brutally suppressed Ikko-ikki Buddhist uprisings and burned the temple complex of Mount Hiei. A thorough realist who welcomed Jesuit missionaries and Western firearms, he was also a tyrant. In 1582, betrayed by his general Akechi Mitsuhide at Honno-ji temple in Kyoto — 'the enemy is at Honno-ji' — he was forced to commit suicide. His unification mission was completed by Toyotomi Hideyoshi.",
  [], [], "", 0.85)

p("toyotomi-hideyoshi", "丰臣秀吉", "Toyotomi Hideyoshi", 1537, 1598, "japan",
  ["君主", "关白", "日本", "战国", "军事"], ["Ruler", "Kampaku", "Japan", "Sengoku", "Military"],
  "日本战国时代统一者，从农民出身升至最高权力，两次入侵朝鲜，奠定了德川幕府的基础。",
  "Unifier of Japan during the Sengoku period who rose from peasant origins to supreme power, invaded Korea twice, and laid the groundwork for the Tokugawa shogunate.",
  "丰臣秀吉的人生是日本历史上最惊人的上升故事——从织田信长的草鞋仆人到统一日本的统治者。他在信长死后迅速消灭了明智光秀，然后逐一降伏或消灭了其他战国大名。他进行了著名的「太阁检地」——全国范围的土地调查——并推行刀狩令收缴农民武器。1592年和1597年他发动了两次入侵朝鲜的战争——最初势如破竹但最终被朝鲜海军（李舜臣的龟船）和明朝援军所阻。他去世时留下年幼的儿子丰臣秀赖，最终被德川家康消灭。",
  "Toyotomi Hideyoshi's life is the most astonishing rise in Japanese history — from sandal-bearer to Oda Nobunaga to ruler of unified Japan. After Nobunaga's death, he swiftly eliminated Akechi Mitsuhide and then subdued or destroyed the other daimyo one by one. He conducted the famous 'Taiko Land Survey' — a nationwide cadastral survey — and enforced the Sword Hunt to disarm the peasantry. In 1592 and 1597, he launched two invasions of Korea — initially devastating but ultimately checked by the Korean navy (Admiral Yi Sun-sin's turtle ships) and Ming Chinese reinforcements. He died leaving an infant son, Toyotomi Hideyori, who would ultimately be destroyed by Tokugawa Ieyasu.",
  [], [], "", 0.85)

p("emperor-go-daigo", "后醍醐天皇", "Emperor Go-Daigo", 1288, 1339, "japan",
  ["君主", "天皇", "日本", "建武新政"], ["Ruler", "Emperor", "Japan", "Kenmu Restoration"],
  "日本第96代天皇，试图恢复天皇亲政（建武新政），失败后建立南朝，开启了南北朝时代。",
  "Japan's 96th emperor who attempted to restore direct imperial rule (Kenmu Restoration), and after failure established the Southern Court.",
  "后醍醐天皇是日本历史上少数试图恢复天皇实权的君主。1333年他联合不满镰仓幕府的武士推翻幕府，开始了「建武新政」——试图建立以天皇为中心的中国式官僚体制。但新政脱离实际，武士们的不满迅速蔓延——足利尊氏反叛并建立了新的军事政权（室町幕府）。后醍醐逃往吉野建立南朝，与足利支持的京都北朝对峙，开启了长达56年的南北朝时代。他的不屈与失败成为日本文学（尤其是《太平记》）的经典主题。",
  "Emperor Go-Daigo was one of the few Japanese monarchs to attempt reclaiming real imperial power. In 1333, he allied with disaffected warriors to overthrow the Kamakura Shogunate and began the 'Kenmu Restoration' — an attempt to establish Chinese-style bureaucratic governance centered on the emperor. But the Restoration was impractical, and warrior discontent quickly spread — Ashikaga Takauji rebelled and established a new military regime (the Muromachi Shogunate). Go-Daigo fled to Yoshino, establishing the Southern Court against the Kyoto-based Northern Court supported by the Ashikaga, inaugurating 56 years of divided courts. His indomitable yet doomed struggle became a classic theme in Japanese literature, especially the 'Taiheiki.'",
  ["Go-Daigo-tenno"], [], "", 0.75)

# ============ INDIA (2 new, many existing) ============
p("chandragupta-maurya", "旃陀罗笈多·孔雀", "Chandragupta Maurya", -340, -297, "india",
  ["君主", "皇帝", "印度", "孔雀王朝"], ["Ruler", "Emperor", "India", "Maurya"],
  "印度孔雀王朝开创者，驱逐亚历山大大帝的残余势力，统一北印度大部。",
  "Founder of the Maurya Empire who expelled the remnants of Alexander's forces and unified most of northern India.",
  "旃陀罗笈多的早年充满传奇——据说他年轻时见过亚历山大大帝。在亚历山大的将领离开印度后，旃陀罗笈多迅速崛起：他先在老师的帮助下推翻了难陀王朝，然后击败了亚历山大在印度留下的总督塞琉古一世——双方最终达成和平协议，塞琉古将大片领土割让并嫁女给旃陀罗笈多。他在位期间建立了高效的中亚帝国管理体系——他的首席大臣考底利耶撰写的《政事论》是古代政治学的杰作。根据耆那教传统，他晚年放弃了王位成为耆那教僧人。",
  "Chandragupta's early life is shrouded in legend — he reportedly met Alexander the Great as a youth. After Alexander's generals departed India, Chandragupta rose rapidly: first overthrowing the Nanda dynasty with his mentor's help, then defeating Seleucus I, Alexander's successor in the east — the peace treaty ceded vast territories to Chandragupta and included a marriage alliance. He established efficient imperial administration — his chief minister Kautilya's 'Arthashastra' is a masterpiece of ancient political science. According to Jain tradition, he abdicated in old age and became a Jain monk.",
  [], [], "", 0.8)

p("chandragupta-ii", "旃陀罗笈多二世", "Chandragupta II (Vikramaditya)", 375, 415, "india",
  ["君主", "皇帝", "印度", "笈多王朝"], ["Ruler", "Emperor", "India", "Gupta"],
  "印度笈多王朝皇帝，绰号「超日王」，笈多文化的黄金时代在其治下达到鼎盛。",
  "Gupta emperor known as 'Vikramaditya' (Sun of Valor); the golden age of Gupta culture reached its zenith under his rule.",
  "旃陀罗笈多二世以「超日王」之名流传后世——「超日」（Vikramaditya）成为理想君主的代名词。他通过婚姻联盟和军事征服将笈多帝国扩展到历史上最大范围。他的宫廷聚集了印度古典文化最璀璨的「九宝」——包括诗人迦梨陀娑（「印度的莎士比亚」）、天文学家伐罗诃密希罗等。中国僧人法显在他的统治时期访问印度，留下了珍贵的记载。笈多时期被认为是印度古典文明的巅峰——雕塑、壁画、文学和科学都取得了卓越成就。",
  "Chandragupta II is remembered by his epithet 'Vikramaditya' — the 'Sun of Valor' — which became synonymous with the ideal monarch. Through marital alliances and military conquest, he expanded the Gupta Empire to its greatest extent. His court hosted the 'Nine Jewels' (Navaratnas) — the brightest luminaries of classical Indian culture, including the poet Kalidasa ('the Shakespeare of India') and the astronomer Varahamihira. The Chinese monk Faxian visited India during his reign, leaving invaluable records. The Gupta period is considered the pinnacle of classical Indian civilization — with outstanding achievements in sculpture, painting, literature, and science.",
  ["超日王", "Vikramaditya"], [], "", 0.8)

# ============ KOREA (4) ============
p("gwanggaeto", "广开土大王", "Gwanggaeto the Great", 374, 413, "korea",
  ["君主", "国王", "朝鲜", "高句丽", "军事"], ["Ruler", "King", "Korea", "Goguryeo", "Military"],
  "高句丽第十九代国王，大幅扩张领土，其功业被刻于广开土大王碑上流传至今。",
  "Nineteenth king of Goguryeo who dramatically expanded the kingdom's territory; his achievements are recorded on the Gwanggaeto Stele.",
  "广开土大王的名字意为「广开土地」——这正是他一生的写照。他在位期间将高句丽的疆域向北扩展到辽东半岛、向西进入辽东、向南至汉江流域。他击败了倭国（日本）在朝鲜半岛的军事存在、征服了契丹部落、迫使百济和新罗臣服。他的功业被记录在巨大的石碑上——广开土大王碑至今矗立在中国吉林省集安市——是研究东北亚古代历史的最重要金石文献。他年仅39岁便去世，留下了一个空前强大的高句丽王国。",
  "Gwanggaeto's name literally means 'Great Expander of Territory' — the story of his life. During his reign, he pushed Goguryeo's borders north into the Liaodong Peninsula, west into Manchuria, and south to the Han River basin. He defeated Japanese military presence on the Korean peninsula, conquered Khitan tribes, and forced Baekje and Silla into submission. His achievements were recorded on a massive stele — the Gwanggaeto Stele, still standing in Ji'an, Jilin Province, China — one of the most important epigraphic sources for ancient Northeast Asian history. He died at just 39, leaving an unprecedentedly powerful Goguryeo.",
  [], [], "", 0.8)

p("taejo-goryeo", "高丽太祖", "Taejo of Goryeo", 877, 943, "korea",
  ["君主", "国王", "朝鲜", "高丽"], ["Ruler", "King", "Korea", "Goryeo"],
  "高丽王朝开国君主王建，统一后三国，奠定了高丽近五百年的统治基础。",
  "Founder of the Goryeo dynasty who unified the Later Three Kingdoms and laid the foundation for nearly five centuries of Goryeo rule.",
  "王建原为后高句丽王国（泰封）的将领。918年他推翻暴虐的君主弓裔，改国号为高丽（即「高句丽」的简称——Korea一名即源于此）。此后他通过军事征服和联盟策略先后消灭了后百济和新罗，于936年完成统一。他推行了务实的「北进政策」、通过联姻团结地方豪族、颁布《训要十条》作为后世君主的治国准则。高丽王朝延续了474年——比大多数中国王朝都要长久。",
  "Wang Geon began as a general of Later Goguryeo (Taebong). In 918, he overthrew the tyrannical ruler Gung Ye and renamed the kingdom Goryeo (a shortened form of Goguryeo — from which the name 'Korea' derives). He then eliminated Later Baekje and Silla through conquest and alliance, completing unification in 936. He pursued a pragmatic 'Northern Expansion Policy,' united regional elites through marriage alliances, and promulgated the 'Ten Injunctions' (Hunyo Sipjo) as a guide for future rulers. The Goryeo dynasty endured for 474 years — longer than most Chinese dynasties.",
  ["王建", "Wang Geon"], [], "", 0.8)

p("sejong", "世宗大王", "Sejong the Great", 1397, 1450, "korea",
  ["君主", "国王", "朝鲜", "科学", "文化"], ["Ruler", "King", "Korea", "Science", "Culture"],
  "朝鲜王朝第四代国王，创制训民正音（韩文），推动科学技术和文化全面发展。",
  "Fourth king of the Joseon dynasty who created Hangul (the Korean alphabet) and propelled scientific, technological, and cultural advancement.",
  "世宗大王被尊为韩国历史上最伟大的君主。他创制了韩文——一套基于发音器官形状的科学性字母系统——使普通百姓也能识字书写，这在当时是革命性的。他还建立了集贤殿（皇家研究院）、推动农业技术改良、发明了雨量计和水钟、编纂了《东国通鉴》和《农事直说》、派军讨伐对马岛倭寇。世宗时代被认为是朝鲜王朝文化的第一个黄金时代。他的肖像至今仍出现在韩国一万元纸币上。",
  "King Sejong is revered as Korea's greatest monarch. He created Hangul — a scientifically designed alphabet based on the shapes of speech organs — enabling common people to read and write, revolutionary for its time. He also established the Hall of Worthies (Jiphyeonjeon, a royal research institute), advanced agricultural techniques, invented the rain gauge and water clock, compiled historical and agricultural texts, and dispatched a military expedition to suppress Japanese pirates on Tsushima Island. The Sejong era is regarded as the first golden age of Joseon culture. His portrait still appears on South Korea's 10,000-won banknote.",
  ["李祹", "Yi Do"], [], "", 0.9)

p("yeongjo", "英祖", "Yeongjo of Joseon", 1694, 1776, "korea",
  ["君主", "国王", "朝鲜", "改革"], ["Ruler", "King", "Korea", "Reform"],
  "朝鲜王朝第21代国王，在位最久，推行荡平策和各项改革，其子思悼世子的悲剧令人扼腕。",
  "The 21st and longest-reigning Joseon king who enacted the Policy of Impartiality and reforms, overshadowed by the tragedy of his son Crown Prince Sado.",
  "英祖在位52年是朝鲜王朝统治时间最长的君主。他推行了「荡平策」——在东西两班党派之间保持平衡以减少党争——并实行了多项社会改革：禁止残酷刑罚、减轻赋税、限制官僚特权。但他一生最黑暗的阴影来自他的儿子——思悼世子。思悼因精神疾病和暴力行为日益不受控制，1762年在英祖的命令下被关入米柜中活活饿死。这成为了韩国历史上最悲惨的王室悲剧之一——也是韩国电影《思悼》的原型。",
  "Yeongjo reigned for 52 years, the longest of any Joseon monarch. He implemented the 'Policy of Impartiality' (Tangpyeongchaek) — balancing between the Eastern and Western political factions to reduce strife — and enacted social reforms: banning cruel punishments, reducing taxes, and limiting bureaucratic privileges. But the darkest shadow of his life was his son — Crown Prince Sado. Sado's mental illness and increasingly violent behavior led Yeongjo to order him confined in a rice chest in 1762, where he starved to death. This became one of Korean history's most tragic royal episodes — and the subject of the acclaimed film 'The Throne.'",
  [], [], "", 0.85)

# ============ AMERICAS (3 new) ============
p("montezuma-ii", "蒙特祖马二世", "Montezuma II", 1466, 1520, "aztec-empire",
  ["君主", "皇帝", "阿兹特克"], ["Ruler", "Emperor", "Aztec"],
  "阿兹特克帝国第九任皇帝，在西班牙征服者科尔特斯到来时统治帝国，最终死于西班牙人之手。",
  "Ninth Aztec emperor ruling when the conquistador Hernán Cortés arrived; he died at Spanish hands.",
  "蒙特祖马二世统治着当时中美洲最强大的帝国——拥有数百万人口和宏伟的特诺奇蒂特兰城（建立在湖上的奇观）。当科尔特斯率领不到600名西班牙人在1519年登陆时，蒙特祖马的犹豫和矛盾导致了灾难——他最初以礼相待迎接西班牙人进城，但很快成为人质。1520年当他试图向自己的人民讲话平息叛乱时，被石头击中身亡（死因究竟是西班牙人所为还是被自己的臣民所杀至今有争议）。他的死亡和阿兹特克的覆灭是美洲历史上最戏剧性的转折点之一。",
  "Montezuma II ruled the most powerful empire in Mesoamerica — millions of subjects and the magnificent lake-city of Tenochtitlan. When Cortés landed with fewer than 600 Spaniards in 1519, Montezuma's hesitation and ambivalence proved catastrophic — he initially welcomed the Spanish into the city with gifts but soon became their hostage. In 1520, when he tried to address his own people to calm a rebellion, he was struck by stones and died — whether killed by the Spanish or his own subjects remains disputed. His death and the Aztec collapse mark one of the most dramatic turning points in American history.",
  [], [], "", 0.8)

p("pachacuti", "帕查库特克", "Pachacuti", 1418, 1471, "inca-empire",
  ["君主", "萨帕·印卡", "印加帝国"], ["Ruler", "Sapa Inca", "Inca Empire"],
  "印加帝国第九代萨帕·印卡，将库斯科一个部落王国打造为庞大的安第斯帝国。",
  "Ninth Sapa Inca who transformed a tribal kingdom around Cusco into the vast Andean empire.",
  "帕查库特克的名字意为「改变世界的人」——名副其实。他在击退昌卡人的入侵后夺取权力，随后发动了一系列雷霆般的征服战争，将印加从一个库斯科山谷的小城邦扩展为纵贯安第斯山脉三千多公里的大帝国。他不仅是征服者也是建设者——重建了库斯科城规划为美洲豹形状、建造了马丘比丘、建立了遍布帝国的道路系统（总长近四万公里）和驿站体系。印加帝国卓越的行政和工程成就大多可以追溯到他的远见。",
  "Pachacuti's name means 'He Who Transforms the World' — and he did. After repelling the Chanka invasion, he seized power and launched lightning conquests, transforming the Inca from a small Cusco valley polity into an empire stretching over 3,000 kilometers along the Andes. He was not only a conqueror but a builder — redesigning Cusco in the shape of a puma, constructing Machu Picchu, and building the imperial road system (nearly 40,000 km total) with its relay-runner network. Much of the Inca's remarkable administrative and engineering achievements trace back to his vision.",
  [], [], "", 0.75)

p("simon-bolivar", "西蒙·玻利瓦尔", "Simón Bolívar", 1783, 1830, "americas",
  ["君主", "革命者", "拉丁美洲", "独立"], ["Ruler", "Revolutionary", "Latin America", "Independence"],
  "南美独立运动领袖，「解放者」，领导委内瑞拉、哥伦比亚、秘鲁和玻利维亚等国脱离西班牙统治。",
  "Leader of South American independence movements, 'El Libertador,' who liberated Venezuela, Colombia, Peru, and Bolivia from Spanish rule.",
  "西蒙·玻利瓦尔出身委内瑞拉富豪家庭，在目睹欧洲拿破仑时代的变革后决心解放自己的祖国。他领导的独立战争历经了最戏剧性的曲折——数次失败和流亡——但每次都卷土重来。他率军穿越安第斯山脉的壮举在军事史上堪称奇迹。他建立了大哥伦比亚共和国——涵盖今委内瑞拉、哥伦比亚、巴拿马和厄瓜多尔——并梦想建立统一的南美洲联邦。但他的晚年充满失望——各国相继分离、内斗不止，他在流亡途中去世，留下著名的遗言：「我在徒劳的海洋中耕耘。」玻利维亚的国名即是对他的致敬。",
  "Simón Bolívar was born to immense wealth in Venezuela; witnessing the Napoleonic transformation of Europe, he resolved to liberate his homeland. His independence campaigns featured the most dramatic reversals — repeated defeats and exiles — yet he returned each time. His crossing of the Andes with his army is a feat of military history. He established Gran Colombia — encompassing modern Venezuela, Colombia, Panama, and Ecuador — and dreamed of a unified South American federation. But his final years were marked by disappointment — nations seceded, infighting raged, and he died on the way to exile, lamenting 'I have plowed the sea.' Bolivia's name is his tribute.",
  [], [], "", 0.85)

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
print(f"\n// Total: {len(people)} global rulers")
