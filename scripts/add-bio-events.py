#!/usr/bin/env python3
"""
Add detailed biographical events for major Tang-Song-Ming-Qing figures.
Each person gets 4-8 key life events with specific years and descriptions.
Events are inserted into the events array in mockData.ts.
"""
import re
from pathlib import Path

MOCKDATA = Path('src/data/mockData.ts')
content = MOCKDATA.read_text(encoding='utf-8')

# Mapping of person ID to their region
PERSON_REGIONS = {
    'li-bai': 'tang-dynasty',
    'du-fu': 'tang-dynasty',
    'emperor-taizong': 'tang-dynasty', 
    'wu-zetian': 'tang-dynasty',
    'wang-anshi': 'song-dynasty',
    'su-shi': 'song-dynasty',
    'sima-guang': 'song-dynasty',
    'ouyang-xiu': 'song-dynasty',
    'zhu-xi': 'song-dynasty',
    'zhu-yuanzhang': 'ming-dynasty',
    'zheng-he': 'ming-dynasty',
    'li-shizhen': 'ming-dynasty',
    'kangxi': 'qing-dynasty',
    'qianlong': 'qing-dynasty',
    'cao-xueqin': 'qing-dynasty',
}

def make_event(event_id, title, title_en, year, person_id, region, summary, description, importance=3, tags=None, tags_en=None):
    region_id = PERSON_REGIONS.get(person_id, region)
    tags_str = str(tags) if tags else "['人物', '生平']"
    tags_en_str = str(tags_en) if tags_en else "['Biography', 'Life']"
    
    # Escape single quotes in English strings for TypeScript
    title_en = title_en.replace("'", "\\'")
    summary = summary.replace("'", "\\'")
    description = description.replace("'", "\\'")
    
    return f"""  {{
    id: '{event_id}',
    title: '{title}',
    titleEn: '{title_en}',
    startYear: {year},
    endYear: {year},
    regionId: '{region_id}',
    coordinates: undefined,
    placeName: '',
    personIds: ['{person_id}'],
    tags: {tags_str},
    tagsEn: {tags_en_str},
    summary: '{summary}',
    summaryEn: '{title_en}',
    description: '{description}',
    descriptionEn: '{title_en}',
    sourceIds: [],
    importance: {importance},
    datePrecision: 'year' as const,
    isApproximate: false,
    relatedEventIds: [],
    dataStatus: 'published' as const,
    confidenceScore: 0.9,
    externalReferences: [],
  }},
"""

# ============ ALL NEW EVENTS ============
new_events = []

# --- 李白 (701-762) ---
new_events.append(make_event('evt-libai-leaves-shu', '李白辞亲远游', 'Li Bai leaves Shu to wander', 725, 'li-bai', 'tang-dynasty',
    '开元十三年（725年），二十五岁的李白辞亲远游，仗剑出蜀，沿长江东下，途经江陵、洞庭、庐山、金陵等地，一路结交名士饮酒赋诗，开始了其豪迈壮阔的漫游生涯。',
    '开元十三年（725年），二十五岁的李白"仗剑去国，辞亲远游"，离开故乡蜀中沿长江东下。他自幼博览群书又习剑术，出蜀后游历江陵、洞庭、庐山、金陵等地，一路赋诗交友。在江陵遇道教名士司马承祯得赞赏；在金陵挥金如土，一年散尽三十万钱。《渡荆门送别》中"山随平野尽，江入大荒流"正写于此次出蜀途中。',
    importance=4, tags=['人物', '生平', '漫游'], tags_en=['Biography', 'Life', 'Travel']))

new_events.append(make_event('evt-libai-enters-court', '李白入长安为翰林供奉', 'Li Bai enters the imperial court', 742, 'li-bai', 'tang-dynasty',
    '天宝元年（742年），四十二岁的李白受唐玄宗召见入长安，供奉翰林院。他因其卓绝的诗才受到玄宗礼遇，传说曾令高力士脱靴、杨贵妃捧砚，一时风光无两。',
    '天宝元年（742年），四十二岁的李白因玉真公主和贺知章推荐，受唐玄宗召见。玄宗亲降辇步迎，以七宝床赐食，并御手调羹以饭之。李白供奉翰林院，专为皇帝起草诏书和应制诗文。传说他曾使高力士脱靴、杨国忠磨墨。然而优厚的礼遇并不能掩盖李白政治抱负未展的苦闷——他不过充当御用文人点缀升平而已。',
    importance=5, tags=['人物', '生平', '仕途'], tags_en=['Biography', 'Life', 'Career']))

new_events.append(make_event('evt-libai-departs-court', '李白赐金放还离开长安', 'Li Bai leaves Chang\'an', 744, 'li-bai', 'tang-dynasty',
    '天宝三载（744年），李白因遭权贵谗毁，被玄宗赐金放还，离开长安。同年他与另一位大诗人杜甫在洛阳相遇，二人结为至交，同游梁宋，成为文学史上的一段佳话。',
    '天宝三载（744年），李白因在朝中恃才傲物得罪权贵，被唐玄宗"赐金放还"，实际上是被排挤出京。他离开长安继续漫游，同年春夏之际在洛阳与三十三岁的杜甫相遇。这是中国文学史上最伟大的会面之一——"诗仙"与"诗圣"结为生死之交，同游梁宋（今河南商丘），一起登吹台、游梁园。惜别后二人再未相见，但杜甫终生怀念李白，写下了"故人入我梦，明我长相忆"的诗句。',
    importance=5, tags=['人物', '生平', '交友'], tags_en=['Biography', 'Life', 'Friendship']))

new_events.append(make_event('evt-libai-exiled-yelang', '李白流放夜郎', 'Li Bai exiled to Yelang', 757, 'li-bai', 'tang-dynasty',
    '至德二载（757年），李白因参与永王李璘幕府而获罪，被判流放夜郎（今贵州桐梓）。后行至巫山时遇朝廷大赦，他在白帝城写下千古名篇《早发白帝城》。',
    '至德二载（757年），安史之乱爆发后，唐玄宗第十六子永王李璘在江陵起兵，李白应邀入其幕府。不料李璘被肃宗定为叛逆，李白受牵连入狱，被判流放夜郎。五十八岁的李白在流放途中行至白帝城时，恰逢朝廷因关中大旱而大赦天下。重获自由后他写下《早发白帝城》："朝辞白帝彩云间，千里江陵一日还。两岸猿声啼不住，轻舟已过万重山。"诗中满溢的欢欣与重获新生的畅快，成为千古绝唱。',
    importance=5, tags=['人物', '生平', '流放'], tags_en=['Biography', 'Life', 'Exile']))

# --- 杜甫 (712-770) ---
new_events.append(make_event('evt-dufu-travels-wuyue', '杜甫漫游吴越', 'Du Fu travels through Wu and Yue', 735, 'du-fu', 'tang-dynasty',
    '开元二十三年（735年），二十四岁的杜甫首次远游江南，在吴越漫游了三四年。他徜徉于苏州、杭州、绍兴等名城，登临名胜古迹，开阔了视野。',
    '开元二十三年（735年），二十四岁的杜甫结束洛阳书斋生活，首次远游江南，在吴越一带漫游了三四年。他徜徉于苏州、杭州、绍兴等历史文化名城，登金陵凤凰台，访姑苏台旧址，泛舟太湖和鉴湖。与后来颠沛流离的岁月相比，这是杜甫一生中最自由奔放的青年时代。',
    importance=4, tags=['人物', '生平', '漫游'], tags_en=['Biography', 'Life', 'Travel']))

new_events.append(make_event('evt-dufu-meets-libai', '杜甫与李白相遇', 'Du Fu meets Li Bai in Luoyang', 744, 'du-fu', 'tang-dynasty',
    '天宝三载（744年），三十三岁的杜甫在洛阳与刚从长安失意而出的李白相遇，二人结为至交，同游梁宋，成为文学史上最伟大的友谊之一。',
    '天宝三载（744年），中国文学史上最伟大的会面在洛阳上演——三十三岁的杜甫与四十四岁的李白相遇。二人一见如故，同游梁宋（今河南商丘），登吹台游梁园，后又同游齐鲁。杜甫后来在《与李十二白同寻范十隐居》中写道："醉眠秋共被，携手日同行。"此后二人再未相见，但杜甫一生怀念李白，写下了二十余首怀念诗作。',
    importance=5, tags=['人物', '生平', '交友'], tags_en=['Biography', 'Life', 'Friendship']))

new_events.append(make_event('evt-dufu-trapped-anlushan', '杜甫身陷安史之乱', 'Du Fu trapped during An Lushan Rebellion', 756, 'du-fu', 'tang-dynasty',
    '至德元载（756年），安史叛军攻陷长安，杜甫举家逃亡。在投奔唐肃宗的路上被叛军俘虏并押回长安，亲眼目睹了国破家亡的惨状，创作了《春望》等不朽诗篇。',
    '至德元载（756年），安史之乱爆发后，杜甫安顿家小于鄜州，只身投奔在灵武即位的唐肃宗。不料途中被叛军俘虏押回长安。被困长安期间，他目睹曾经繁华的都城沦为废墟，写下了《春望》："国破山河在，城春草木深。感时花溅泪，恨别鸟惊心。"更为震撼的是他后来写下的《三吏》《三别》，用诗歌记录了战乱中普通百姓的深重苦难，因而后世称其诗为"诗史"。',
    importance=5, tags=['人物', '生平', '战争'], tags_en=['Biography', 'Life', 'War']))

new_events.append(make_event('evt-dufu-chengdu-cottage', '杜甫栖居成都草堂', 'Du Fu dwells in Chengdu Thatched Cottage', 760, 'du-fu', 'tang-dynasty',
    '上元元年（760年），杜甫在朋友帮助下于成都浣花溪畔建成草堂，度过了相对安定的四年。他在这里写下了《春夜喜雨》《茅屋为秋风所破歌》等名篇。',
    '上元元年（760年），杜甫在好友严武等人的帮助下，在成都浣花溪畔建成了草堂。这是一段相对安定的日子——他种菜养鸡，写诗会友。然而《茅屋为秋风所破歌》中"安得广厦千万间，大庇天下寒士俱欢颜"的呐喊，表明即使在个人困境稍缓之时，他始终心怀天下苍生。成都的四年是杜甫诗歌创作的高峰期之一。',
    importance=4, tags=['人物', '生平'], tags_en=['Biography', 'Life']))

# --- 唐太宗 (598-649) ---
new_events.append(make_event('evt-taizong-taiyuan-uprising', '李世民劝父起兵', 'Li Shimin persuades father to revolt', 617, 'emperor-taizong', 'tang-dynasty',
    '大业十三年（617年），李世民审时度势，联合裴寂、刘文静力劝其父太原留守李渊起兵反隋。七月李渊在太原誓师，李世民率军攻入长安，开启唐朝建立的序幕。',
    '大业十三年（617年），隋朝天下大乱。太原留守李渊卷入政治危机，其子李世民联合裴寂和刘文静力劝父亲起兵。七月李渊在太原誓师，李世民与兄长李建成分率左右两军直指长安。十一月攻克长安后李渊自任大丞相，次年五月正式称帝建立唐朝。年仅二十岁的李世民展现出了卓越的军事谋略。',
    importance=5, tags=['人物', '生平', '战争'], tags_en=['Biography', 'Life', 'War']))

new_events.append(make_event('evt-taizong-xuanwu-gate', '玄武门之变', 'Xuanwu Gate Incident', 626, 'emperor-taizong', 'tang-dynasty',
    '武德九年（626年），李世民在长安宫城玄武门设伏射杀兄长太子李建成和弟李元吉，迫使李渊立其为太子并退位，是为"玄武门之变"，由此开启了贞观之治。',
    '武德九年六月初四（626年7月2日），李世民经过精心策划，在玄武门设下伏兵，亲手射杀了前来上朝的太子李建成，部将尉迟恭则射死了齐王李元吉。三天后李渊立李世民为太子，两个月后正式退位称太上皇。李世民即位后次年改元贞观，开启了历史上著名的"贞观之治"。玄武门之变虽是血腥的宫廷政变，但李世民的治国能力确实证明了他是一个优秀的皇帝。',
    importance=5, tags=['人物', '生平', '政变'], tags_en=['Biography', 'Life', 'Coup']))

new_events.append(make_event('evt-taizong-zhenguan-governance', '贞观之治', 'The Zhenguan Reign', 630, 'emperor-taizong', 'tang-dynasty',
    '贞观四年（630年），唐太宗治下的唐朝呈现出政治清明、经济发展、文化繁荣的局面。他任用贤相房玄龄和杜如晦（房谋杜断），虚心纳谏，以魏徵为"镜"，开创了中国历史上著名的"贞观之治"。',
    '贞观年间（627-649），唐太宗李世民展现出卓越的治国才能。他知人善任——房玄龄善谋、杜如晦能断，世称"房谋杜断"；他广开言路——以魏徵为镜，魏徵敢于犯颜直谏，留下了"以铜为镜可以正衣冠，以古为镜可以知兴替，以人为镜可以明得失"的名言；他轻徭薄赋，与民休息；他平定突厥被尊为"天可汗"。贞观之治成为中国封建社会的治理典范。',
    importance=5, tags=['人物', '生平', '政治'], tags_en=['Biography', 'Life', 'Politics']))

# --- 武则天 (624-705) ---
new_events.append(make_event('evt-wuzetian-enter-palace', '武则天入宫为才人', 'Wu Zetian enters the palace', 638, 'wu-zetian', 'tang-dynasty',
    '贞观十二年（638年），十四岁的武则天因美貌被唐太宗选入宫中，封为才人，赐号"武媚"。唐太宗驾崩后她入感业寺为尼，后被高宗召回宫中。',
    '贞观十二年（638年），十四岁的武则天因"美容止"被唐太宗召入宫中封为才人，赐号"武媚"。太宗驾崩后她依例入感业寺削发为尼。永徽二年（651年），唐高宗在寺中见到武则天后旧情复燃，将她召回宫中封为昭仪。这段从才人到尼姑再到昭仪的经历，锻炼了武则天在复杂宫廷政治中生存和发展的能力。',
    importance=4, tags=['人物', '生平', '宫廷'], tags_en=['Biography', 'Life', 'Court']))

new_events.append(make_event('evt-wuzetian-zhou-dynasty', '武则天改唐为周称帝', 'Wu Zetian proclaims the Zhou dynasty', 690, 'wu-zetian', 'tang-dynasty',
    '载初元年（690年），六十七岁的武则天废黜唐睿宗，正式称帝，改国号为周，定都洛阳。她成为中国历史上唯一的女皇帝。',
    '载初元年九月九日（690年10月16日），六十七岁的武则天登上则天门楼，宣布改唐为周，改元天授，正式称"圣神皇帝"。她以洛阳为神都，大封武氏宗族，同时继续任用狄仁杰、张柬之等贤臣治国。武则天在位十五年，首创殿试和武举制度，打破士族门阀对官僚体系的垄断。705年"神龙政变"后被迫退位，恢复唐朝，同年十二月病逝于洛阳。',
    importance=5, tags=['人物', '生平', '称帝'], tags_en=['Biography', 'Life', 'Coronation']))

# --- 王安石 (1021-1086) ---
new_events.append(make_event('evt-wanganshi-wanyanshu', '王安石上万言书', 'Wang Anshi submits the Ten-Thousand Word Memorial', 1058, 'wang-anshi', 'song-dynasty',
    '嘉祐三年（1058年），王安石向宋仁宗上《万言书》（《上仁宗皇帝言事书》），系统阐述其变法主张，但未被采纳。这篇奏章为他后来的熙宁变法奠定了理论基础。',
    '嘉祐三年（1058年），时任三司度支判官的王安石向宋仁宗呈递了长达万言的奏章，直指北宋积贫积弱的根源在于"方今之法度多不合于先王之政"。他提出"改易更革"的主张，建议从理财、整军、富国、强兵等方面进行系统改革。虽然仁宗未予重视，但这篇《万言书》成为了十五年后熙宁变法的理论纲领。',
    importance=5, tags=['人物', '生平', '变法'], tags_en=['Biography', 'Life', 'Reform']))

new_events.append(make_event('evt-wanganshi-xining-reforms', '王安石推行熙宁变法', 'Wang Anshi launches the Xining Reforms', 1069, 'wang-anshi', 'song-dynasty',
    '熙宁二年（1069年），宋神宗任命四十九岁的王安石为参知政事，次年拜相，全面推行青苗法、免役法、市易法、保甲法等新法，"熙宁变法"正式拉开序幕。',
    '熙宁二年（1069年），宋神宗任命王安石为参知政事，次年拜同中书门下平章事（宰相）。王安石以"天变不足畏，祖宗不足法，人言不足恤"的勇气，开始推行一系列旨在富国强兵的新法：青苗法——政府低息贷款给农民；免役法——以钱代役；市易法——平抑物价；保甲法——兵民合一。新法轰动朝野，遭到司马光、苏轼等人的激烈反对，朝中形成"新旧党争"。变法的成败至今仍是史学界争论的话题。',
    importance=5, tags=['人物', '生平', '变法', '政治'], tags_en=['Biography', 'Life', 'Reform', 'Politics']))

new_events.append(make_event('evt-wanganshi-resigns', '王安石罢相退居金陵', 'Wang Anshi resigns and retires to Jinling', 1076, 'wang-anshi', 'song-dynasty',
    '熙宁九年（1076年），五十六岁的王安石在变法接连受挫、爱子王雱病逝的双重打击下，辞去宰相之职，退居金陵（今南京）钟山，寄情山水诗文度余生。',
    '熙宁九年（1076年），王安石心爱的长子王雱病逝，变法派内部也出现分裂。五十六岁的他身心俱疲，辞去宰相之职退居金陵钟山。晚年的王安石住在钟山半山园，自号"半山"，骑驴游山玩水，与苏轼等昔日政敌在文学上惺惺相惜。元祐元年（1086年），保守派上台废除新法，王安石在钟山闻讯后悲愤而卒，享年六十六岁。',
    importance=4, tags=['人物', '生平', '归隐'], tags_en=['Biography', 'Life', 'Retirement']))

# --- 苏轼 (1037-1101) ---
new_events.append(make_event('evt-sushi-wutai-poetry-trial', '苏轼乌台诗案被贬黄州', 'Su Shi exiled to Huangzhou after the Crow Terrace Poetry Trial', 1079, 'su-shi', 'song-dynasty',
    '元丰二年（1079年），苏轼因诗文被指控讽刺新法，被捕入御史台狱（因院中遍植柏树栖乌鸦故称乌台），历经四月审讯后被贬为黄州团练副使。在黄州他自号东坡居士，创作了《赤壁赋》等千古名篇。',
    '元丰二年（1079年），监察御史弹劾苏轼的诗文"讥讪朝政"，四十三岁的苏轼被捕入御史台狱——这就是著名的"乌台诗案"。在狱中他一度以为自己必死无疑，连绝命诗都已写好。经多方营救——连王安石也上书"安有圣世而杀才士乎"——苏轼被从轻发落，贬为黄州团练副使。在黄州期间他自耕东坡，自号"东坡居士"，泛舟赤壁之下写下了前、后《赤壁赋》和《念奴娇·赤壁怀古》。这段贬谪岁月反而催生了他文学创作的巅峰。',
    importance=5, tags=['人物', '生平', '贬谪', '文学'], tags_en=['Biography', 'Life', 'Exile', 'Literature']))

new_events.append(make_event('evt-sushi-hangzhou-governor', '苏轼知杭州筑苏堤', 'Su Shi governs Hangzhou and builds Su Causeway', 1089, 'su-shi', 'song-dynasty',
    '元祐四年（1089年），苏轼以龙图阁学士出知杭州。他疏浚西湖，利用挖出的淤泥葑草堆筑长堤，后人称为"苏堤"。苏堤春晓至今仍是西湖十景之首。',
    '元祐四年（1089年），苏轼以龙图阁学士出任杭州知州。面对西湖严重淤塞、水面萎缩的困境，他组织二十万民工大规模疏浚西湖，将挖出的淤泥与水草堆筑成一条贯穿南北的长堤，堤上遍植桃柳芙蓉，建六桥以通水流。杭州百姓感激苏轼，将这道长堤命名为"苏堤"。"苏堤春晓"至今仍是西湖十景之首。苏轼在杭州还建立了中国最早的公立医院之一"安乐坊"，救灾恤民，留下了不朽功绩。',
    importance=5, tags=['人物', '生平', '治水', '民生'], tags_en=['Biography', 'Life', 'Governance']))

new_events.append(make_event('evt-sushi-hainan-exile', '苏轼贬谪海南儋州', 'Su Shi exiled to Hainan', 1097, 'su-shi', 'song-dynasty',
    '绍圣四年（1097年），六十二岁的苏轼被贬到当时荒蛮的海南儋州。在极端艰苦的条件下，他办学授徒、传播文化，培养出了海南第一位举人。',
    '绍圣四年（1097年），六十二岁高龄的苏轼被贬谪到当时被视为天涯海角的海南儋州。他携幼子苏过渡海抵达荒岛，食无肉、病无药、居无室，但他以乐观豁达的态度在桄榔林中搭建草庐寓居。在儋州三年间，他办学堂、介学风，传播中原文化。当地人姜唐佐在他指导下成为海南历史上第一位举人。苏轼临别前赠姜诗"沧海何曾断地脉，白袍端合破天荒"——海南"破天荒"之典即源于此。',
    importance=4, tags=['人物', '生平', '贬谪', '教育'], tags_en=['Biography', 'Life', 'Exile', 'Education']))

# --- 司马光 (1019-1086) ---
new_events.append(make_event('evt-simaguang-zztj-start', '司马光开始编纂资治通鉴', 'Sima Guang begins compiling Zizhi Tongjian', 1064, 'sima-guang', 'song-dynasty',
    '治平元年（1064年），司马光将已完成的《历年图》呈送宋英宗。此后他前后耗时十九年，终于完成涵盖战国至五代1362年历史的编年体通史《资治通鉴》。',
    '治平元年（1064年），司马光向宋英宗进呈八卷《历年图》，将战国至五代一千多年的历史大事编成提要。此后他得到英宗和神宗两代皇帝的支持，设立书局专心编纂。在王安石变法期间，司马光退居洛阳十五载，团结刘恕、刘攽、范祖禹等一流史学家，翻阅了大量宫廷秘藏史料，十九年呕心沥血完成二百九十四卷的《资治通鉴》。神宗御笔亲题书名并作序："鉴于往事，有资于治道。"',
    importance=5, tags=['人物', '生平', '史学'], tags_en=['Biography', 'Life', 'History']))

new_events.append(make_event('evt-simaguang-opposes-reform', '司马光反对王安石变法', 'Sima Guang opposes Wang Anshi\'s reforms', 1069, 'sima-guang', 'song-dynasty',
    '熙宁二年（1069年），王安石推行新法，司马光作为保守派领袖上书激烈反对，认为变法扰民伤财。这场新旧党争深刻影响了北宋后期的政治格局。',
    '熙宁二年（1069年），宋神宗任用王安石变法，司马光以翰林学士的身份多次上书反对。他认为"祖宗之法不可变"，青苗法实为与民争利，免役法加重百姓负担。二人之间的论战不仅仅在政见层面——王安石主张积极有为，司马光主张稳健守成——更代表了两种不同的治国理念。尽管政治立场对立，司马光与王安石在个人品格上相互敬重，这场"君子之争"成为中国政治史上的典范。',
    importance=5, tags=['人物', '生平', '政治'], tags_en=['Biography', 'Life', 'Politics']))

# --- 欧阳修 (1007-1072) ---
new_events.append(make_event('evt-ouyangxiu-leads-reform', '欧阳修支持范仲淹庆历新政', 'Ouyang Xiu supports the Qingli Reforms', 1043, 'ouyang-xiu', 'song-dynasty',
    '庆历三年（1043年），范仲淹推行庆历新政，欧阳修积极参与并撰写《朋党论》支持改革。新政失败后他被贬滁州，却在此写下了传世名篇《醉翁亭记》。',
    '庆历三年（1043年），宋仁宗任用范仲淹推行新政，欧阳修以谏官身份热情支持改革。他著名的《朋党论》提出君子有朋、小人无朋的议论，力辩君子之党有利于国。新政遭保守派反扑失败后，欧阳修被贬滁州知州。然而政治失意反而催生了文学杰作——在滁州他写下了《醉翁亭记》："醉翁之意不在酒，在乎山水之间也"。这篇文章以"也"字连缀全篇，意境深远，成为散文史上的千古绝唱。',
    importance=5, tags=['人物', '生平', '政治', '文学'], tags_en=['Biography', 'Life', 'Politics', 'Literature']))

# --- 朱元璋 (1328-1398) ---
new_events.append(make_event('evt-zhuyuanzhang-poyang-lake', '朱元璋鄱阳湖大捷', 'Zhu Yuanzhang wins Battle of Lake Poyang', 1363, 'zhu-yuanzhang', 'ming-dynasty',
    '至正二十三年（1363年），朱元璋与陈友谅在鄱阳湖展开决战，以二十万兵力击败陈友谅六十万水军。此役是中国古代规模最大的水战，奠定了朱元璋统一南方的基础。',
    '至正二十三年（1363年），朱元璋与陈友谅在鄱阳湖展开了中国古代规模最大的水战。陈友谅号称六十万大军，楼船高数丈联舟布阵；朱元璋以二十万兵力采取火攻战术，在康郎山水域大破陈友谅水寨。八月陈友谅在突围中中箭身亡，次年其子陈理投降。鄱阳湖大捷后朱元璋控制了长江中下游，为北伐元朝扫清了最大的障碍。',
    importance=5, tags=['人物', '生平', '战争'], tags_en=['Biography', 'Life', 'War']))

new_events.append(make_event('evt-zhuyuanzhang-founds-ming', '朱元璋称帝建立明朝', 'Zhu Yuanzhang founds the Ming dynasty', 1368, 'zhu-yuanzhang', 'ming-dynasty',
    '洪武元年正月（1368年1月），朱元璋在应天（南京）即皇帝位，国号大明，年号洪武。同年八月明军攻克元大都（北京），元朝灭亡。',
    '洪武元年正月初四（1368年1月23日），四十岁的朱元璋在应天府（南京）祭天即皇帝位，国号大明，年号洪武。这个曾经沿街乞讨的孤儿和游方僧，在十六年的浴血奋战后成为帝国的主人。同年八月，徐达、常遇春率明军攻克元大都（今北京），元顺帝北逃，元朝灭亡。朱元璋开创的明朝延续了二百七十六年，是中国历史上最后一个由汉族建立的大一统王朝。',
    importance=5, tags=['人物', '生平', '称帝'], tags_en=['Biography', 'Life', 'Coronation']))

new_events.append(make_event('evt-zhuyuanzhang-abolish-chancellor', '朱元璋废丞相权分六部', 'Zhu Yuanzhang abolishes the chancellor position', 1380, 'zhu-yuanzhang', 'ming-dynasty',
    '洪武十三年（1380年），朱元璋以胡惟庸谋反案为契机，废除延续千年的丞相制度，权分六部直属皇帝。此举极大加强了皇权，深刻影响了此后明清五百年的政治体制。',
    '洪武十三年（1380年），朱元璋以左丞相胡惟庸谋反为由将其诛杀，株连三万余人。随后宣布永远废除丞相制度，将中书省的权力分散到吏、户、礼、兵、刑、工六部，六部尚书直接对皇帝负责。这是中国古代政治制度的一次重大变革——自秦以降延续近一千六百年的宰相制度被彻底取消，皇权专制达到了前所未有的高度。这一制度框架贯穿明、清两朝，直到1906年清末新政才重新设立了内阁。',
    importance=5, tags=['人物', '生平', '政治', '制度'], tags_en=['Biography', 'Life', 'Politics']))

# --- 郑和 (1371-1433) ---
new_events.append(make_event('evt-zhenghe-seventh-voyage', '郑和第七次下西洋', 'Zheng He embarks on his seventh and final voyage', 1431, 'zheng-he', 'ming-dynasty',
    '宣德六年（1431年），年已六旬的郑和奉命第七次出使西洋。这是郑和最后一次远航，他于返航途中在古里（今印度卡利卡特）病逝，结束了他传奇的航海生涯。',
    '宣德六年（1431年），六十一岁的郑和奉明宣宗之命第七次出使西洋。这是郑和最远的一次航行——舰队穿过马六甲海峡、横渡印度洋、到达霍尔木兹海峡和东非海岸。然而在返航途中行至古里（今印度卡利卡特）时，这位伟大的航海家病逝于海上。根据伊斯兰教习俗他的遗体被葬于大海，明宣宗赐其衣冠冢于南京牛首山。郑和七下西洋历时二十八年，是中国航海史上的空前壮举。',
    importance=5, tags=['人物', '生平', '航海'], tags_en=['Biography', 'Life', 'Navigation']))

# --- 李时珍 (1518-1593) ---
new_events.append(make_event('evt-lishizhen-complete-bencao', '李时珍完成本草纲目初稿', 'Li Shizhen completes the first draft of Bencao Gangmu', 1578, 'li-shizhen', 'ming-dynasty',
    '万历六年（1578年），经过二十七年艰苦卓绝的努力，六十一岁的李时珍终于完成了《本草纲目》的初稿。这部巨著五十二卷，收录药物1892种。',
    '万历六年（1578年），六十一岁的李时珍终于完成了《本草纲目》的五十二卷初稿。从1552年立志编纂至今，他已付出了二十七年心血——亲登武当山采药，远赴岭南考察，遍访药农樵夫，对每种药材都详细考订其名称、产地、形态、栽培方法、采集季节、炮制过程和药理功效。这部一百九十余万字的巨著共收录药物1892种（其中新增374种）、药方11096首、插图1160幅。李时珍于1593年去世，《本草纲目》在他身后三年才得以刊行，随即震动了整个学术界。',
    importance=5, tags=['人物', '生平', '医学', '著作'], tags_en=['Biography', 'Life', 'Medicine']))

# --- 康熙 (1654-1722) ---
new_events.append(make_event('evt-kangxi-ascends-throne', '康熙八岁登基', 'Kangxi Emperor ascends the throne', 1661, 'kangxi', 'qing-dynasty',
    '顺治十八年（1661年），清世祖顺治帝驾崩，年仅八岁的玄烨即位，是为康熙帝，由索尼、鳌拜等四大臣辅政。',
    '顺治十八年正月初七（1661年2月5日），二十四岁的顺治帝因天花驾崩，遗诏立年仅八岁的皇三子玄烨为帝，以索尼、苏克萨哈、遏必隆、鳌拜四人为辅政大臣。这位八岁的小皇帝在祖母孝庄太皇太后的庇护下成长，虽然年幼但聪慧好学——他每天凌晨即起读经史，兼习骑射。康熙帝在成长中逐渐展现出非凡的政治天赋，为他日后长达六十一年的统治奠定了基础。',
    importance=4, tags=['人物', '生平', '登基'], tags_en=['Biography', 'Life', 'Coronation']))

new_events.append(make_event('evt-kangxi-three-feudatories', '康熙平定三藩之乱', 'Kangxi Emperor suppresses the Revolt of the Three Feudatories', 1681, 'kangxi', 'qing-dynasty',
    '康熙二十年（1681年），清朝平定三藩之乱。自1673年吴三桂起兵反清以来，这场持续八年的战争终于以清朝的胜利告终，西南地区从此纳入中央有效管辖。',
    '康熙十二年十一月（1673年），平西王吴三桂在云南发动叛乱，自称周王，靖南王耿精忠、平南王尚之信相继响应，史称"三藩之乱"。这场战争波及云南、贵州、湖南、四川、福建、广东、陕西等省，一度使清朝丧失半壁江山。年仅二十岁的康熙帝临危不惧，采取剿抚并用的策略，终于在康熙二十年（1681年）清军攻克昆明，三藩之乱彻底平定。这一胜利使清朝完成了对全国的统一。',
    importance=5, tags=['人物', '生平', '战争', '统一'], tags_en=['Biography', 'Life', 'War']))

new_events.append(make_event('evt-kangxi-conquer-taiwan', '康熙收复台湾', 'Kangxi Emperor conquers Taiwan', 1683, 'kangxi', 'qing-dynasty',
    '康熙二十二年（1683年），康熙帝派施琅率水师攻克澎湖，郑克塽降清，台湾正式纳入清朝版图。次年清政府在台湾设府，隶属福建省。',
    '康熙二十二年（1683年），施琅率领两万余清军从福建东山岛出发，在澎湖海域与郑军主帅刘国轩展开大海战。施琅巧妙利用风向变化发动火攻，大破郑军水师，七月郑克塽率台湾军民投降。次年清政府在台湾设立一府三县（台湾府及台湾、凤山、诸罗三县），隶属福建省。康熙帝的这一决策使台湾首次被纳入中央政府的行政管辖体系。',
    importance=5, tags=['人物', '生平', '战争', '统一'], tags_en=['Biography', 'Life', 'War']))

# --- 乾隆 (1711-1799) ---
new_events.append(make_event('evt-qianlong-ascends', '乾隆登基', 'Qianlong Emperor ascends the throne', 1735, 'qianlong', 'qing-dynasty',
    '雍正十三年（1735年），清世宗雍正帝驾崩，二十五岁的弘历即位，是为乾隆帝。乾隆在位六十年，实际上掌权长达六十三年零四个月，是中国历史上实际掌权时间最长的皇帝。',
    '雍正十三年八月二十三日（1735年10月8日），雍正帝突然驾崩于圆明园。根据秘密立储制度，二十五岁的皇四子弘历顺利即位，次年改元乾隆。乾隆帝自幼受祖父康熙帝喜爱和亲自养育，即位后效法康熙励精图治，在其统治的前中期清朝国力达到了顶峰。他在位六十年后主动禅位给嘉庆帝，但仍以太上皇身份训政三年多，实际掌权长达六十三年零四个月。',
    importance=5, tags=['人物', '生平', '登基'], tags_en=['Biography', 'Life', 'Coronation']))

new_events.append(make_event('evt-qianlong-siku-quanshu', '乾隆编纂四库全书', 'Qianlong Emperor compiles the Siku Quanshu', 1772, 'qianlong', 'qing-dynasty',
    '乾隆三十七年（1772年），乾隆帝下诏征集天下图书，开始编纂中国古代规模最大的丛书——《四库全书》。全书抄录七部，历时十余年完成。',
    '乾隆三十七年（1772年），乾隆帝下诏征集天下图书，开始编纂中国古代规模最大的丛书。在总纂官纪昀（纪晓岚）主持下，三百六十多位学者历时十余年，将经、史、子、集四部共三千四百六十一种图书（七万九千三百三十七卷）抄录为七部四库全书，分藏于紫禁城文渊阁、沈阳文溯阁、圆明园文源阁、承德文津阁、扬州文汇阁、镇江文宗阁和杭州文澜阁。然而征书过程中也销毁了大量不利于清朝统治的著作，功过参半。',
    importance=5, tags=['人物', '生平', '文化', '典籍'], tags_en=['Biography', 'Life', 'Culture']))

new_events.append(make_event('evt-qianlong-abdicates', '乾隆禅位嘉庆', 'Qianlong Emperor abdicates to Emperor Jiaqing', 1796, 'qianlong', 'qing-dynasty',
    '嘉庆元年（1796年），八十六岁的乾隆帝在即位六十年后，遵守其即位初"不敢超过皇祖康熙帝在位六十一年"的誓言，禅位于第十五子嘉庆帝。',
    '嘉庆元年正月初一（1796年2月9日），八十六岁高龄的乾隆帝在太和殿举行了隆重的禅位大典，将皇帝玉玺传给三十七岁的第十五子永琰（嘉庆帝）。这是乾隆帝即位之初的誓言——如在位满六十年则主动退位，不超过祖父康熙帝的六十一年。然而乾隆并未真正放权，他以"太上皇"身份继续训政，嘉庆帝不过是一个"实习皇帝"。直到嘉庆四年（1799年）乾隆驾崩，嘉庆才真正亲政。',
    importance=5, tags=['人物', '生平', '禅位'], tags_en=['Biography', 'Life', 'Abdication']))

# --- 曹雪芹 (1715-1763) ---
new_events.append(make_event('evt-caoxueqin-family-falls', '曹雪芹家族被抄家', 'Cao Xueqin family is disgraced', 1727, 'cao-xueqin', 'qing-dynasty',
    '雍正五年（1727年），曹雪芹约十二岁时，其父曹頫因亏空库银被革职抄家，曹家从世代富贵的江宁织造府沦为北京贫民。这一从繁华到衰败的经历成为《红楼梦》的创作源泉。',
    '雍正五年（1727年），曹頫因骚扰驿站、亏空帑银等罪名被革职抄家，曹家百余年的荣华富贵一夜之间化为乌有。曹雪芹的祖父曹寅曾是康熙帝的宠臣和少年伴读，曹家三代四人历任江宁织造近六十年，四次接驾康熙南巡。然而一朝倾覆——曹雪芹从锦衣玉食的公子沦为北京崇文门外蒜市口的贫民。正是这刻骨铭心的家族兴衰体验，成为他日后创作《红楼梦》的灵魂所在。',
    importance=5, tags=['人物', '生平', '家族'], tags_en=['Biography', 'Life', 'Family']))

# Insert before the closing ]; of the events array
insert_point = content.rfind('];\n\n')
content = content[:insert_point] + '\n'.join(new_events) + '\n' + content[insert_point:]

MOCKDATA.write_text(content, encoding='utf-8')
print(f"Added {len(new_events)} new biographical events.")
print("Event IDs:")
for e in new_events:
    # Extract ID from first line
    id_match = re.search(r"id: '([^']+)'", e)
    if id_match:
        print(f"  - {id_match.group(1)}")
