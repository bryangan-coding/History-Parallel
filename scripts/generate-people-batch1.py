"""
生成新批次历史人物 - 批次1
包含：战国诸子、历代名医、世界古代史、欧洲中世纪、近现代科学家、文学家
"""
import json
import re

# 读取现有ID
with open('src/data/mockData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

existing_ids = set(re.findall(r"id: '(.+?)'", content))
existing_names = set(re.findall(r"name: '(.+?)'", content))

print(f"已收录人数: {len(existing_ids)}")

# ========== 1. 战国诸子百家 ==========
zhanguo_thinkers = [
    {
        'id': 'xunzi',
        'name': '荀子',
        'nameEn': 'Xunzi',
        'birthYear': -313,
        'deathYear': -238,
        'regionId': 'china',
        'tags': ['哲学', '儒家'],
        'tagsEn': ['philosophy', 'confucian'],
        'summary': '战国末期儒家代表人物，融合儒法思想，弟子有韩非、李斯。',
        'summaryEn': 'Late Warring States period Confucian philosopher who synthesized Confucian and Legalist thought. His disciples included Han Fei and Li Si.',
        'dynasty': '战国',
    },
    {
        'id': 'mozi',
        'name': '墨子',
        'nameEn': 'Mozi',
        'birthYear': -468,
        'deathYear': -376,
        'regionId': 'china',
        'tags': ['哲学', '墨家'],
        'tagsEn': ['philosophy', 'mohism'],
        'summary': '墨家学派创始人，主张兼爱非攻，在逻辑学、光学、力学方面有贡献。',
        'summaryEn': 'Founder of Mohism, advocated universal love and anti-war. Contributed to logic, optics, and mechanics.',
        'dynasty': '战国',
    },
    {
        'id': 'sunzi',
        'name': '孙武',
        'nameEn': 'Sunzi',
        'birthYear': -544,
        'deathYear': -496,
        'regionId': 'china',
        'tags': ['军事', '兵法'],
        'tagsEn': ['military', 'strategy'],
        'summary': '《孙子兵法》作者，被尊为兵圣，其军事思想影响深远。',
        'summaryEn': 'Author of The Art of War, revered as the Sage of War. His military thought has profound influence.',
        'dynasty': '春秋',
    },
    {
        'id': 'sunbin',
        'name': '孙膑',
        'nameEn': 'Sun Bin',
        'birthYear': -380,
        'deathYear': -316,
        'regionId': 'china',
        'tags': ['军事', '兵法'],
        'tagsEn': ['military', 'strategy'],
        'summary': '孙武后代，战国军事家，《孙膑兵法》作者，桂陵、马陵之战获胜。',
        'summaryEn': 'Descendant of Sunzi, Warring States military strategist. Author of Sun Bin\'s Art of War.',
        'dynasty': '战国',
    },
    {
        'id': 'yangzhu',
        'name': '杨朱',
        'nameEn': 'Yang Zhu',
        'birthYear': -440,
        'deathYear': -360,
        'regionId': 'china',
        'tags': ['哲学', '杨朱学派'],
        'tagsEn': ['philosophy', 'yangzhu'],
        'summary': '战国时期道家学派代表，主张"贵己""重生"，强调个人价值。',
        'summaryEn': 'Warring States period Daoist philosopher, advocated valuing the self and preserving life.',
        'dynasty': '战国',
    },
    {
        'id': 'huishi',
        'name': '惠施',
        'nameEn': 'Hui Shi',
        'birthYear': -370,
        'deathYear': -310,
        'regionId': 'china',
        'tags': ['哲学', '名家'],
        'tagsEn': ['philosophy', 'sophist'],
        'summary': '战国时期名家代表人物，庄子好友，以"历物十事"闻名。',
        'summaryEn': 'Warring States period Sophist philosopher, friend of Zhuangzi, known for "Ten Theses on Things".',
        'dynasty': '战国',
    },
    {
        'id': 'gongsunlong',
        'name': '公孙龙',
        'nameEn': 'Gongsun Long',
        'birthYear': -325,
        'deathYear': -250,
        'regionId': 'china',
        'tags': ['哲学', '名家'],
        'tagsEn': ['philosophy', 'sophist'],
        'summary': '战国时期名家代表，"白马非马"论的代表人物。',
        'summaryEn': 'Warring States period Sophist, famous for the "White Horse is Not a Horse" paradox.',
        'dynasty': '战国',
    },
]

# ========== 2. 历代名医 ==========
famous_doctors = [
    {
        'id': 'zhangzhongjing',
        'name': '张仲景',
        'nameEn': 'Zhang Zhongjing',
        'birthYear': 150,
        'deathYear': 219,
        'regionId': 'china',
        'tags': ['医学', '中医'],
        'tagsEn': ['medicine', 'traditional-chinese-medicine'],
        'summary': '东汉医学家，被尊为"医圣"，《伤寒杂病论》作者，确立了辨证论治原则。',
        'summaryEn': 'Eastern Han physician, revered as the "Sage of Medicine". Author of Treatise on Cold Damage Diseases.',
        'dynasty': '东汉',
    },
    {
        'id': 'huatuo',
        'name': '华佗',
        'nameEn': 'Hua Tuo',
        'birthYear': 145,
        'deathYear': 208,
        'regionId': 'china',
        'tags': ['医学', '外科'],
        'tagsEn': ['medicine', 'surgery'],
        'summary': '东汉末年医学家，精通外科，发明"麻沸散"（麻醉剂），创编五禽戏。',
        'summaryEn': 'Late Eastern Han physician, master of surgery. Invented anesthetic "Mafeisan" and created the Five-Animal Exercises.',
        'dynasty': '东汉',
    },
    {
        'id': 'huangfumi',
        'name': '皇甫谧',
        'nameEn': 'Huangfu Mi',
        'birthYear': 215,
        'deathYear': 282,
        'regionId': 'china',
        'tags': ['医学', '针灸'],
        'tagsEn': ['medicine', 'acupuncture'],
        'summary': '魏晋医学家，著有《针灸甲乙经》，是现存最早的针灸学专著。',
        'summaryEn': 'Wei-Jin period physician, author of the earliest extant acupuncture treatise.',
        'dynasty': '魏晋',
    },
    {
        'id': 'sun-simiao',
        'name': '孙思邈',
        'nameEn': 'Sun Simiao',
        'birthYear': 581,
        'deathYear': 682,
        'regionId': 'china',
        'tags': ['医学', '中医'],
        'tagsEn': ['medicine', 'traditional-chinese-medicine'],
        'summary': '唐代医学家，被尊为"药王"，著有《千金要方》《千金翼方》。',
        'summaryEn': 'Tang dynasty physician, revered as the "King of Medicine". Author of Essential Prescriptions Worth a Thousand Gold.',
        'dynasty': '唐朝',
    },
    {
        'id': 'li-shizhen',
        'name': '李时珍',
        'nameEn': 'Li Shizhen',
        'birthYear': 1518,
        'deathYear': 1593,
        'regionId': 'china',
        'tags': ['医学', '药学'],
        'tagsEn': ['medicine', 'pharmacology'],
        'summary': '明代医学家，著有《本草纲目》，是中国古代药物学的集大成之作。',
        'summaryEn': 'Ming dynasty physician, author of Compendium of Materia Medica, the monumental work of Chinese pharmacology.',
        'dynasty': '明朝',
    },
]

# ========== 3. 世界古代史重要人物 ==========
ancient_world = [
    {
        'id': 'gilgamesh',
        'name': '吉尔伽美什',
        'nameEn': 'Gilgamesh',
        'birthYear': -2600,
        'deathYear': -2500,
        'regionId': 'middle-east',
        'tags': ['传说', '苏美尔'],
        'tagsEn': ['legend', 'sumerian'],
        'summary': '乌鲁克国王，史诗《吉尔伽美什史诗》主人公，被誉为最早的文学英雄。',
        'summaryEn': 'King of Uruk, hero of the Epic of Gilgamesh, considered the earliest literary hero.',
    },
    {
        'id': 'hammurabi',
        'name': '汉谟拉比',
        'nameEn': 'Hammurabi',
        'birthYear': -1810,
        'deathYear': -1750,
        'regionId': 'middle-east',
        'tags': ['法律', '巴比伦'],
        'tagsEn': ['law', 'babylonian'],
        'summary': '古巴比伦国王，颁布《汉谟拉比法典》，是现存最完整的早期法典。',
        'summaryEn': 'King of Babylon, promulgated the Code of Hammurabi, the most complete early law code.',
    },
    {
        'id': 'thutmose-iii',
        'name': '图特摩斯三世',
        'nameEn': 'Thutmose III',
        'birthYear': -1481,
        'deathYear': -1425,
        'regionId': 'egypt',
        'tags': ['法老', '新王国'],
        'tagsEn': ['pharaoh', 'new-kingdom'],
        'summary': '古埃及新王国时期法老，在位期间埃及版图达到最大。',
        'summaryEn': 'New Kingdom pharaoh of Egypt, expanded Egypt to its greatest territorial extent.',
    },
    {
        'id': 'akhenaten',
        'name': '阿肯那顿',
        'nameEn': 'Akhenaten',
        'birthYear': -1353,
        'deathYear': -1336,
        'regionId': 'egypt',
        'tags': ['法老', '宗教改革'],
        'tagsEn': ['pharaoh', 'religious-reform'],
        'summary': '古埃及法老，推行一神教改革，崇拜阿顿神。',
        'summaryEn': 'Egyptian pharaoh who attempted religious reform, promoting worship of the Aten.',
    },
    {
        'id': 'tutankhamun',
        'name': '图坦卡蒙',
        'nameEn': 'Tutankhamun',
        'birthYear': -1341,
        'deathYear': -1323,
        'regionId': 'egypt',
        'tags': ['法老', '新王国'],
        'tagsEn': ['pharaoh', 'new-kingdom'],
        'summary': '古埃及法老，其陵墓保存完好，1922年发现后震惊世界。',
        'summaryEn': 'Egyptian pharaoh whose nearly intact tomb was discovered in 1922, causing a sensation.',
    },
    {
        'id': 'cyrus',
        'name': '居鲁士大帝',
        'nameEn': 'Cyrus the Great',
        'birthYear': -600,
        'deathYear': -530,
        'regionId': 'persia',
        'tags': ['皇帝', '波斯'],
        'tagsEn': ['emperor', 'persian'],
        'summary': '波斯帝国创建者，宽容的统治者，释放巴比伦之囚。',
        'summaryEn': 'Founder of the Persian Empire, known for his tolerance and liberating the Babylonian captivity.',
    },
    {
        'id': 'leonidas',
        'name': '列奥尼达',
        'nameEn': 'Leonidas',
        'birthYear': -540,
        'deathYear': -480,
        'regionId': 'greece',
        'tags': ['国王', '斯巴达'],
        'tagsEn': ['king', 'sparta'],
        'summary': '斯巴达国王，温泉关战役中率领300勇士抵抗波斯大军。',
        'summaryEn': 'King of Sparta who led 300 Spartans at the Battle of Thermopylae against Persia.',
    },
    {
        'id': 'pericles',
        'name': '伯里克利',
        'nameEn': 'Pericles',
        'birthYear': -495,
        'deathYear': -429,
        'regionId': 'greece',
        'tags': ['政治家', '雅典'],
        'tagsEn': ['politician', 'athens'],
        'summary': '雅典政治家，伯里克利时代是雅典民主政治和文化的黄金时期。',
        'summaryEn': 'Athenian statesman, under whom Athens reached the height of democracy and culture.',
    },
]

# ========== 4. 欧洲中世纪重要人物 ==========
medieval_europe = [
    {
        'id': 'benedict-nursia',
        'name': '努西亚的本笃',
        'nameEn': 'Benedict of Nursia',
        'birthYear': 480,
        'deathYear': 547,
        'regionId': 'byzantine',
        'tags': ['修士', '本笃会'],
        'tagsEn': ['monk', 'benedictine'],
        'summary': '西方修道院制度创始人，本笃会创立者，被尊为欧洲主保圣人。',
        'summaryEn': 'Founder of Western monasticism and the Benedictine Order, patron saint of Europe.',
    },
    {
        'id': 'boethius',
        'name': '波爱修斯',
        'nameEn': 'Boethius',
        'birthYear': 480,
        'deathYear': 524,
        'regionId': 'byzantine',
        'tags': ['哲学家', '政治家'],
        'tagsEn': ['philosopher', 'politician'],
        'summary': '罗马哲学家，著有《哲学的慰藉》，是中世纪早期最重要的思想家之一。',
        'summaryEn': 'Roman philosopher, author of The Consolation of Philosophy, one of the most important early medieval thinkers.',
    },
    {
        'id': 'bede',
        'name': '比德',
        'nameEn': 'Bede',
        'birthYear': 673,
        'deathYear': 735,
        'regionId': 'england',
        'tags': ['修士', '历史学家'],
        'tagsEn': ['monk', 'historian'],
        'summary': '英国历史学家，著有《英吉利教会史》，被尊为"英国历史之父"。',
        'summaryEn': 'English historian, author of Ecclesiastical History of the English People, "Father of English History".',
    },
    {
        'id': 'charlemagne',
        'name': '查理大帝',
        'nameEn': 'Charlemagne',
        'birthYear': 742,
        'deathYear': 814,
        'regionId': 'france',
        'tags': ['皇帝', '法兰克'],
        'tagsEn': ['emperor', 'frankish'],
        'summary': '法兰克国王，加洛林王朝最著名的君主，建立了加洛林帝国。',
        'summaryEn': 'King of the Franks, most famous Carolingian ruler, established the Carolingian Empire.',
    },
    {
        'id': 'alcuin',
        'name': '阿尔昆',
        'nameEn': 'Alcuin',
        'birthYear': 735,
        'deathYear': 804,
        'regionId': 'england',
        'tags': ['学者', '教育家'],
        'tagsEn': ['scholar', 'educator'],
        'summary': '英国学者，查理曼宫廷学校的领导人，加洛林文艺复兴的关键人物。',
        'summaryEn': 'English scholar, head of Charlemagne\'s palace school, key figure in the Carolingian Renaissance.',
    },
    {
        'id': 'anselm',
        'name': '安瑟伦',
        'nameEn': 'Anselm',
        'birthYear': 1033,
        'deathYear': 1109,
        'regionId': 'holy-roman-empire',
        'tags': ['哲学家', '坎特伯雷大主教'],
        'tagsEn': ['philosopher', 'archbishop-of-canterbury'],
        'summary': '坎特伯雷大主教，经院哲学创始人，提出"本体论论证"。',
        'summaryEn': 'Archbishop of Canterbury, founder of Scholasticism, proposed the ontological argument.',
    },
    {
        'id': 'abelard',
        'name': '阿伯拉尔',
        'nameEn': 'Peter Abelard',
        'birthYear': 1079,
        'deathYear': 1142,
        'regionId': 'france',
        'tags': ['哲学家', '神学家'],
        'tagsEn': ['philosopher', 'theologian'],
        'summary': '法国哲学家，与埃洛伊丝的爱情故事闻名，著有《我的苦难史》。',
        'summaryEn': 'French philosopher, famous for his love story with Heloise. Author of Historia Calamitatum.',
    },
    {
        'id': 'hildegard-bingen',
        'name': '宾根的希尔德加德',
        'nameEn': 'Hildegard of Bingen',
        'birthYear': 1098,
        'deathYear': 1179,
        'regionId': 'holy-roman-empire',
        'tags': ['修女', '神秘主义者'],
        'tagsEn': ['nun', 'mystic'],
        'summary': '德国修女，神秘主义者，在音乐、医学、神学方面都有贡献。',
        'summaryEn': 'German abbess, mystic, who made contributions to music, medicine, and theology.',
    },
]

# ========== 5. 近现代重要科学家 ==========
modern_scientists = [
    {
        'id': 'copernicus',
        'name': '哥白尼',
        'nameEn': 'Nicolaus Copernicus',
        'birthYear': 1473,
        'deathYear': 1543,
        'regionId': 'holy-roman-empire',
        'tags': ['天文学', '日心说'],
        'tagsEn': ['astronomy', 'heliocentrism'],
        'summary': '波兰天文学家，提出日心说，著有《天体运行论》，引发天文学革命。',
        'summaryEn': 'Polish astronomer who proposed heliocentrism. Author of On the Revolutions of the Celestial Spheres.',
    },
    {
        'id': 'kepler',
        'name': '开普勒',
        'nameEn': 'Johannes Kepler',
        'birthYear': 1571,
        'deathYear': 1630,
        'regionId': 'holy-roman-empire',
        'tags': ['天文学', '行星运动定律'],
        'tagsEn': ['astronomy', 'planetary-motion'],
        'summary': '德国天文学家，发现行星运动三大定律，为牛顿力学奠定基础。',
        'summaryEn': 'German astronomer who discovered the three laws of planetary motion, foundational for Newtonian mechanics.',
    },
    {
        'id': 'galileo',
        'name': '伽利略',
        'nameEn': 'Galileo Galilei',
        'birthYear': 1564,
        'deathYear': 1642,
        'regionId': 'italy',
        'tags': ['物理学', '天文学'],
        'tagsEn': ['physics', 'astronomy'],
        'summary': '意大利科学家，现代观测天文学之父，支持哥白尼的日心说。',
        'summaryEn': 'Italian scientist, father of modern observational astronomy. Supported Copernican heliocentrism.',
    },
    {
        'id': 'newton',
        'name': '牛顿',
        'nameEn': 'Isaac Newton',
        'birthYear': 1643,
        'deathYear': 1727,
        'regionId': 'england',
        'tags': ['物理学', '微积分'],
        'tagsEn': ['physics', 'calculus'],
        'summary': '英国物理学家、数学家，提出万有引力定律和三大运动定律，发明微积分。',
        'summaryEn': 'English physicist and mathematician, formulated laws of motion and universal gravitation, invented calculus.',
    },
    {
        'id': 'darwin',
        'name': '达尔文',
        'nameEn': 'Charles Darwin',
        'birthYear': 1809,
        'deathYear': 1882,
        'regionId': 'england',
        'tags': ['生物学', '进化论'],
        'tagsEn': ['biology', 'evolution'],
        'summary': '英国生物学家，提出进化论，著有《物种起源》，改变了人类对生命的理解。',
        'summaryEn': 'English biologist who proposed the theory of evolution. Author of On the Origin of Species.',
    },
    {
        'id': 'mendel',
        'name': '孟德尔',
        'nameEn': 'Gregor Mendel',
        'birthYear': 1822,
        'deathYear': 1884,
        'regionId': 'austria',
        'tags': ['生物学', '遗传学'],
        'tagsEn': ['biology', 'genetics'],
        'summary': '奥地利修士，遗传学之父，通过豌豆实验发现遗传定律。',
        'summaryEn': 'Austrian monk, father of genetics, discovered laws of inheritance through pea experiments.',
    },
    {
        'id': 'pasteur',
        'name': '巴斯德',
        'nameEn': 'Louis Pasteur',
        'birthYear': 1822,
        'deathYear': 1895,
        'regionId': 'france',
        'tags': ['微生物学', '疫苗'],
        'tagsEn': ['microbiology', 'vaccine'],
        'summary': '法国微生物学家，巴氏杀菌法发明者，狂犬病疫苗开发者。',
        'summaryEn': 'French microbiologist, invented pasteurization and developed the rabies vaccine.',
    },
    {
        'id': 'tesla',
        'name': '特斯拉',
        'nameEn': 'Nikola Tesla',
        'birthYear': 1856,
        'deathYear': 1943,
        'regionId': 'united-states',
        'tags': ['物理学', '电气工程'],
        'tagsEn': ['physics', 'electrical-engineering'],
        'summary': '美籍塞尔维亚发明家，交流电系统、无线电、特斯拉线圈的发明者。',
        'summaryEn': 'Serbian-American inventor, developed AC power system, radio, and the Tesla coil.',
    },
    {
        'id': 'curie-marie',
        'name': '玛丽·居里',
        'nameEn': 'Marie Curie',
        'birthYear': 1867,
        'deathYear': 1934,
        'regionId': 'france',
        'tags': ['物理学', '化学'],
        'tagsEn': ['physics', 'chemistry'],
        'summary': '波兰裔法国科学家，研究放射性，是首位获得两次诺贝尔奖的人。',
        'summaryEn': 'Polish-French scientist who conducted pioneering research on radioactivity. First person to win two Nobel Prizes.',
    },
    {
        'id': 'einstein',
        'name': '爱因斯坦',
        'nameEn': 'Albert Einstein',
        'birthYear': 1879,
        'deathYear': 1955,
        'regionId': 'united-states',
        'tags': ['物理学', '相对论'],
        'tagsEn': ['physics', 'relativity'],
        'summary': '德裔美国物理学家，提出狭义相对论和广义相对论，质能方程E=mc²。',
        'summaryEn': 'German-American physicist who developed special and general relativity. Famous for E=mc².',
    },
    {
        'id': 'rutherford',
        'name': '卢瑟福',
        'nameEn': 'Ernest Rutherford',
        'birthYear': 1871,
        'deathYear': 1937,
        'regionId': 'united-kingdom',
        'tags': ['物理学', '原子核'],
        'tagsEn': ['physics', 'atomic-nucleus'],
        'summary': '新西兰裔英国物理学家，原子核物理学之父，提出原子行星模型。',
        'summaryEn': 'New Zealand-born British physicist, father of nuclear physics, proposed the planetary model of the atom.',
    },
    {
        'id': 'planck',
        'name': '普朗克',
        'nameEn': 'Max Planck',
        'birthYear': 1858,
        'deathYear': 1947,
        'regionId': 'germany',
        'tags': ['物理学', '量子力学'],
        'tagsEn': ['physics', 'quantum-mechanics'],
        'summary': '德国物理学家，量子力学创始人，提出量子假说，获1918年诺贝尔物理学奖。',
        'summaryEn': 'German physicist, founder of quantum mechanics, proposed the quantum hypothesis.',
    },
    {
        'id': 'bohr',
        'name': '玻尔',
        'nameEn': 'Niels Bohr',
        'birthYear': 1885,
        'deathYear': 1962,
        'regionId': 'denmark',
        'tags': ['物理学', '量子力学'],
        'tagsEn': ['physics', 'quantum-mechanics'],
        'summary': '丹麦物理学家，原子结构量子理论创始人，玻尔模型提出者。',
        'summaryEn': 'Danish physicist, founder of quantum theory of atomic structure. Proposed the Bohr model.',
    },
    {
        'id': 'heisenberg',
        'name': '海森堡',
        'nameEn': 'Werner Heisenberg',
        'birthYear': 1901,
        'deathYear': 1976,
        'regionId': 'germany',
        'tags': ['物理学', '量子力学'],
        'tagsEn': ['physics', 'quantum-mechanics'],
        'summary': '德国物理学家，量子力学矩阵形式创始人，提出不确定性原理。',
        'summaryEn': 'German physicist, founder of matrix mechanics, proposed the uncertainty principle.',
    },
    {
        'id': 'schrodinger',
        'name': '薛定谔',
        'nameEn': 'Erwin Schrödinger',
        'birthYear': 1887,
        'deathYear': 1961,
        'regionId': 'austria',
        'tags': ['物理学', '量子力学'],
        'tagsEn': ['physics', 'quantum-mechanics'],
        'summary': '奥地利物理学家，量子波动力学创始人，以"薛定谔的猫"思想实验闻名。',
        'summaryEn': 'Austrian physicist, founder of wave mechanics, famous for Schrödinger\'s cat thought experiment.',
    },
    {
        'id': 'dirac',
        'name': '狄拉克',
        'nameEn': 'Paul Dirac',
        'birthYear': 1902,
        'deathYear': 1984,
        'regionId': 'united-kingdom',
        'tags': ['物理学', '量子力学'],
        'tagsEn': ['physics', 'quantum-mechanics'],
        'summary': '英国物理学家，量子电动力学创始人之一，狄拉克方程提出者。',
        'summaryEn': 'British physicist, co-founder of quantum electrodynamics, proposed the Dirac equation.',
    },
    {
        'id': 'turing',
        'name': '图灵',
        'nameEn': 'Alan Turing',
        'birthYear': 1912,
        'deathYear': 1954,
        'regionId': 'united-kingdom',
        'tags': ['计算机科学', '人工智能'],
        'tagsEn': ['computer-science', 'artificial-intelligence'],
        'summary': '英国数学家，计算机科学之父，人工智能先驱，图灵机提出者。',
        'summaryEn': 'British mathematician, father of computer science and pioneer of artificial intelligence. Proposed the Turing machine.',
    },
    {
        'id': 'von-neumann',
        'name': '冯·诺依曼',
        'nameEn': 'John von Neumann',
        'birthYear': 1903,
        'deathYear': 1957,
        'regionId': 'united-states',
        'tags': ['数学', '计算机科学'],
        'tagsEn': ['mathematics', 'computer-science'],
        'summary': '匈裔美国数学家，现代计算机架构（冯·诺依曼架构）设计者。',
        'summaryEn': 'Hungarian-American mathematician, designer of the modern computer architecture (von Neumann architecture).',
    },
]

# ========== 6. 近现代重要文学家、艺术家 ==========
modern_writers_artists = [
    {
        'id': 'dante',
        'name': '但丁',
        'nameEn': 'Dante Alighieri',
        'birthYear': 1265,
        'deathYear': 1321,
        'regionId': 'italy',
        'tags': ['文学', '诗歌'],
        'tagsEn': ['literature', 'poetry'],
        'summary': '意大利诗人，著有三部曲《神曲》，是意大利语之父和文艺复兴先驱。',
        'summaryEn': 'Italian poet, author of the Divine Comedy trilogy. Father of the Italian language and precursor to the Renaissance.',
    },
    {
        'id': 'petrarch',
        'name': '彼特拉克',
        'nameEn': 'Francesco Petrarca',
        'birthYear': 1304,
        'deathYear': 1374,
        'regionId': 'italy',
        'tags': ['文学', '人文主义'],
        'tagsEn': ['literature', 'humanism'],
        'summary': '意大利诗人，文艺复兴人文主义之父，十四行诗大师。',
        'summaryEn': 'Italian poet, father of Renaissance humanism, master of the sonnet.',
    },
    {
        'id': 'boccaccio',
        'name': '薄伽丘',
        'nameEn': 'Giovanni Boccaccio',
        'birthYear': 1313,
        'deathYear': 1375,
        'regionId': 'italy',
        'tags': ['文学', '短篇小说'],
        'tagsEn': ['literature', 'short-fiction'],
        'summary': '意大利作家，《十日谈》作者，文艺复兴时期重要文学家。',
        'summaryEn': 'Italian writer, author of the Decameron, important Renaissance literatus.',
    },
    {
        'id': 'shakespeare',
        'name': '莎士比亚',
        'nameEn': 'William Shakespeare',
        'birthYear': 1564,
        'deathYear': 1616,
        'regionId': 'england',
        'tags': ['文学', '戏剧'],
        'tagsEn': ['literature', 'drama'],
        'summary': '英国剧作家、诗人，被认为是英语文学最杰出的作家，《哈姆雷特》等作者。',
        'summaryEn': 'English playwright and poet, regarded as the greatest writer in English literature. Author of Hamlet, etc.',
    },
    {
        'id': 'cervantes',
        'name': '塞万提斯',
        'nameEn': 'Miguel de Cervantes',
        'birthYear': 1547,
        'deathYear': 1616,
        'regionId': 'spain',
        'tags': ['文学', '小说'],
        'tagsEn': ['literature', 'novel'],
        'summary': '西班牙作家，《堂吉诃德》作者，被誉为西方现代小说之父。',
        'summaryEn': 'Spanish writer, author of Don Quixote, regarded as the father of the modern Western novel.',
    },
    {
        'id': 'milton',
        'name': '弥尔顿',
        'nameEn': 'John Milton',
        'birthYear': 1608,
        'deathYear': 1674,
        'regionId': 'england',
        'tags': ['文学', '诗歌'],
        'tagsEn': ['literature', 'poetry'],
        'summary': '英国诗人，《失乐园》作者，英国文学史上最重要的诗人之一。',
        'summaryEn': 'English poet, author of Paradise Lost, one of the most important poets in English literary history.',
    },
    {
        'id': 'moliere',
        'name': '莫里哀',
        'nameEn': 'Molière',
        'birthYear': 1622,
        'deathYear': 1673,
        'regionId': 'france',
        'tags': ['戏剧', '喜剧'],
        'tagsEn': ['drama', 'comedy'],
        'summary': '法国剧作家，法国喜剧之父，《伪君子》《吝啬鬼》等作品至今上演。',
        'summaryEn': 'French playwright, father of French comedy. Works like Tartuffe and The Miser are still performed today.',
    },
    {
        'id': 'swift',
        'name': '斯威夫特',
        'nameEn': 'Jonathan Swift',
        'birthYear': 1667,
        'deathYear': 1745,
        'regionId': 'ireland',
        'tags': ['文学', '讽刺文学'],
        'tagsEn': ['literature', 'satire'],
        'summary': '爱尔兰作家，《格列佛游记》作者，英语文学最杰出的讽刺作家之一。',
        'summaryEn': 'Irish writer, author of Gulliver\'s Travels, one of the finest satirists in English literature.',
    },
    {
        'id': 'goethe',
        'name': '歌德',
        'nameEn': 'Johann Wolfgang von Goethe',
        'birthYear': 1749,
        'deathYear': 1832,
        'regionId': 'germany',
        'tags': ['文学', '哲学'],
        'tagsEn': ['literature', 'philosophy'],
        'summary': '德国作家、诗人、哲学家，《浮士德》作者，德国文学史上最伟大的人物。',
        'summaryEn': 'German writer, poet, and philosopher. Author of Faust, the greatest figure in German literary history.',
    },
    {
        'id': 'schiller',
        'name': '席勒',
        'nameEn': 'Friedrich Schiller',
        'birthYear': 1759,
        'deathYear': 1805,
        'regionId': 'germany',
        'tags': ['文学', '戏剧'],
        'tagsEn': ['literature', 'drama'],
        'summary': '德国诗人、剧作家、哲学家，《欢乐颂》（贝多芬第九交响曲歌词）作者。',
        'summaryEn': 'German poet, playwright, and philosopher. Author of Ode to Joy (set to music in Beethoven\'s 9th).',
    },
    {
        'id': 'austen',
        'name': '简·奥斯汀',
        'nameEn': 'Jane Austen',
        'birthYear': 1775,
        'deathYear': 1817,
        'regionId': 'england',
        'tags': ['文学', '小说'],
        'tagsEn': ['literature', 'novel'],
        'summary': '英国小说家，《傲慢与偏见》作者，以社会风俗小说闻名。',
        'summaryEn': 'English novelist, author of Pride and Prejudice, famous for her social commentary novels.',
    },
    {
        'id': 'dickens',
        'name': '狄更斯',
        'nameEn': 'Charles Dickens',
        'birthYear': 1812,
        'deathYear': 1870,
        'regionId': 'england',
        'tags': ['文学', '小说'],
        'tagsEn': ['literature', 'novel'],
        'summary': '英国小说家，《双城记》《雾都孤儿》作者，维多利亚时代最杰出的作家。',
        'summaryEn': 'English novelist, author of A Tale of Two Cities and Oliver Twist, the foremost Victorian novelist.',
    },
    {
        'id': 'dostoevsky',
        'name': '陀思妥耶夫斯基',
        'nameEn': 'Fyodor Dostoevsky',
        'birthYear': 1821,
        'deathYear': 1881,
        'regionId': 'russia',
        'tags': ['文学', '小说'],
        'tagsEn': ['literature', 'novel'],
        'summary': '俄国小说家，《罪与罚》《卡拉马佐夫兄弟》作者，心理现实主义大师。',
        'summaryEn': 'Russian novelist, author of Crime and Punishment and The Brothers Karamazov. Master of psychological realism.',
    },
    {
        'id': 'tolstoy',
        'name': '托尔斯泰',
        'nameEn': 'Leo Tolstoy',
        'birthYear': 1828,
        'deathYear': 1910,
        'regionId': 'russia',
        'tags': ['文学', '小说'],
        'tagsEn': ['literature', 'novel'],
        'summary': '俄国小说家，《战争与和平》《安娜·卡列尼娜》作者，现实主义文学高峰。',
        'summaryEn': 'Russian novelist, author of War and Peace and Anna Karenina. Peak of realist literature.',
    },
    {
        'id': 'hugo',
        'name': '雨果',
        'nameEn': 'Victor Hugo',
        'birthYear': 1802,
        'deathYear': 1885,
        'regionId': 'france',
        'tags': ['文学', '诗歌'],
        'tagsEn': ['literature', 'poetry'],
        'summary': '法国作家、诗人，《巴黎圣母院》《悲惨世界》作者，法国浪漫主义领袖。',
        'summaryEn': 'French writer and poet, author of The Hunchback of Notre-Dame and Les Misérables. Leader of French Romanticism.',
    },
    {
        'id': 'balzac',
        'name': '巴尔扎克',
        'nameEn': 'Honoré de Balzac',
        'birthYear': 1799,
        'deathYear': 1850,
        'regionId': 'france',
        'tags': ['文学', '小说'],
        'tagsEn': ['literature', 'novel'],
        'summary': '法国小说家，《人间喜剧》系列作者，现实主义文学巨匠。',
        'summaryEn': 'French novelist, author of the La Comédie humaine series. Master of realist literature.',
    },
    {
        'id': 'flaubert',
        'name': '福楼拜',
        'nameEn': 'Gustave Flaubert',
        'birthYear': 1821,
        'deathYear': 1880,
        'regionId': 'france',
        'tags': ['文学', '小说'],
        'tagsEn': ['literature', 'novel'],
        'summary': '法国小说家，《包法利夫人》作者，以完美的文体著称。',
        'summaryEn': 'French novelist, author of Madame Bovary, renowned for his perfect prose style.',
    },
    {
        'id': 'proust',
        'name': '普鲁斯特',
        'nameEn': 'Marcel Proust',
        'birthYear': 1871,
        'deathYear': 1922,
        'regionId': 'france',
        'tags': ['文学', '小说'],
        'tagsEn': ['literature', 'novel'],
        'summary': '法国小说家，《追忆似水年华》作者，意识流文学先驱。',
        'summaryEn': 'French novelist, author of In Search of Lost Time. Pioneer of stream-of-consciousness literature.',
    },
    {
        'id': 'woolf',
        'name': '弗吉尼亚·伍尔夫',
        'nameEn': 'Virginia Woolf',
        'birthYear': 1882,
        'deathYear': 1941,
        'regionId': 'england',
        'tags': ['文学', '小说'],
        'tagsEn': ['literature', 'novel'],
        'summary': '英国小说家，意识流文学代表人物，《达洛维夫人》《到灯塔去》作者。',
        'summaryEn': 'English novelist, leading figure of stream-of-consciousness literature. Author of Mrs Dalloway and To the Lighthouse.',
    },
    {
        'id': 'hemingway',
        'name': '海明威',
        'nameEn': 'Ernest Hemingway',
        'birthYear': 1899,
        'deathYear': 1961,
        'regionId': 'united-states',
        'tags': ['文学', '小说'],
        'tagsEn': ['literature', 'novel'],
        'summary': '美国小说家，《老人与海》作者，诺贝尔文学奖得主，以简洁风格著称。',
        'summaryEn': 'American novelist, author of The Old Man and the Sea. Nobel laureate known for his concise style.',
    },
    {
        'id': 'faulkner',
        'name': '福克纳',
        'nameEn': 'William Faulkner',
        'birthYear': 1897,
        'deathYear': 1962,
        'regionId': 'united-states',
        'tags': ['文学', '小说'],
        'tagsEn': ['literature', 'novel'],
        'summary': '美国小说家，意识流文学大师，《喧哗与骚动》作者，诺贝尔文学奖得主。',
        'summaryEn': 'American novelist, master of stream-of-consciousness. Author of The Sound and the Fury. Nobel laureate.',
    },
]

# 合并所有新人物
all_new = (zhanguo_thinkers + famous_doctors + ancient_world + 
           medieval_europe + modern_scientists + modern_writers_artists)

print(f"\n待添加人数: {len(all_new)}")

# 去重并生成TypeScript
added = 0
skipped = 0
output_lines = []

for p in all_new:
    pid = p['id']
    name = p['name']
    
    if pid in existing_ids or name in existing_names:
        skipped += 1
        continue
    
    # 构建人物对象
    person_lines = [
        '  {',
        f"    id: '{pid}',",
        f"    name: '{name}',",
        f"    nameEn: '{p['nameEn']}',",
        f"    birthYear: {p['birthYear']},",
        f"    deathYear: {p['deathYear']},",
        f"    regionId: '{p['regionId']}',",
        f"    tags: {json.dumps(p['tags'], ensure_ascii=False)},",
        f"    tagsEn: {json.dumps(p['tagsEn'], ensure_ascii=False)},",
        f"    summary: '{p['summary']}',",
        f"    summaryEn: '{p['summaryEn']}',",
        f"    description: '{p['summary']}',",
        f"    descriptionEn: '{p['summaryEn']}',",
        f"    alternativeNames: ['{name}'],",
        f"    sourceIds: ['src-cbdb'],",
    ]
    
    if p.get('dynasty'):
        person_lines.append(f"    dynasty: '{p['dynasty']}',")
    
    person_lines.append("    dataStatus: 'published',")
    person_lines.append("    featured: false,")
    person_lines.append('  },')
    
    output_lines.extend(person_lines)
    added += 1
    existing_ids.add(pid)
    existing_names.add(name)

print(f"新增人数: {added}")
print(f"跳过人数: {skipped}")

# 写入文件
output_path = 'scripts/generated-people-batch1.ts'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('// 新增历史人物批次1\n')
    f.write(f'// 新增 {added} 位人物\n')
    f.write('// 生成时间: 2026-06-02\n')
    f.write('// 数据来源: 人工整理\n\n')
    f.write('export const newPeople = [\n')
    f.write('\n'.join(output_lines))
    f.write('\n];\n')

print(f"\n数据已写入: {output_path}")

# 生成合并脚本
merge_script = """#!/usr/bin/env python3
'''
将生成的人物数据合并到 mockData.ts
'''
import re

# 读取生成的数据
with open('scripts/generated-people-batch1.ts', 'r', encoding='utf-8') as f:
    gen_content = f.read()

# 提取人物对象
people_match = re.search(r'export const newPeople = \\[(.*?)\\];', gen_content, re.DOTALL)
if not people_match:
    print("未找到生成的数据")
    exit(1)

new_people_str = people_match.group(1).strip()
# 去掉末尾的逗号
if new_people_str.endswith(','):
    new_people_str = new_people_str[:-1]

# 读取mockData.ts
with open('src/data/mockData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到people数组的结尾
people_end = content.rfind('  },\n];', content.find('export const people'))
if people_end == -1:
    print("未找到people数组结尾")
    exit(1)

# 插入新数据（在 ];\n 之前）
insert_pos = people_end + 4  # 跳过 '  },'
before = content[:insert_pos]
after = content[insert_pos:]

new_content = before + ',\\n' + new_people_str + after

# 写回
with open('src/data/mockData.ts', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"成功添加 {new_people_str.count('id:')} 位新人物到 mockData.ts")
"""

with open('scripts/merge-people-batch1.py', 'w', encoding='utf-8') as f:
    f.write(merge_script)

print("合并脚本已生成: scripts/merge-people-batch1.py")
