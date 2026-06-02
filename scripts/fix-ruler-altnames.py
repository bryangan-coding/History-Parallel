#!/usr/bin/env python3
"""Add missing alternativeNames to all newly added rulers in mockData.ts."""
import re

TARGET = 'src/data/mockData.ts'

with open(TARGET) as f:
    content = f.read()

# Define fix data: id -> list of additional alternativeNames to ADD
fixes = {
    # ===== CHINESE EMPERORS =====
    'qin-er-shi': ['胡亥', 'Hu Hai'],
    'han-yuandi': ['刘奭', 'Liu Shi'],
    'cao-pi': ['曹丕', 'Cao Pi', '魏文帝'],
    'liu-bei': ['刘备', 'Liu Bei', '蜀汉昭烈帝'],
    'sun-quan': ['孙权', 'Sun Quan', '吴大帝'],
    'sima-yan': ['司马炎', 'Emperor Wu of Jin', '晋武帝'],
    'tang-xuanzong': ['唐明皇', '李隆基', 'Li Longji'],
    'yuan-huizong': ['元顺帝', '妥懽帖睦尔', 'Toghon Temür'],
    # Ming: add era names (年号)
    'ming-yongle': ['永乐帝', '永乐', '朱棣', 'Zhu Di', '明太宗'],
    'ming-xuande': ['宣德帝', '宣德', '朱瞻基', 'Zhu Zhanji'],
    'ming-wanli': ['万历帝', '万历', '朱翊钧', 'Zhu Yijun'],
    'ming-chongzhen': ['崇祯帝', '崇祯', '朱由检', 'Zhu Youjian'],
    # Qing: add era names (年号) & Manchu names
    'qing-huangtaiji': ['爱新觉罗·皇太极', 'Hong Taiji', '清太宗'],
    'qing-shunzhi': ['顺治', '爱新觉罗·福临', 'Fulin', '清世祖'],
    'qing-yongzheng': ['雍正', '爱新觉罗·胤禛', 'Yinzhen', '清世宗'],
    'qing-guangxu': ['光绪', '爱新觉罗·载湉', 'Zaitian', '清德宗'],
    'qing-puyi': ['爱新觉罗·溥仪', '宣统帝', '宣统', 'Puyi', 'Henry Puyi'],

    # ===== GLOBAL RULERS =====
    # Rome
    'tiberius': ['Tiberius Caesar Augustus', 'Tiberius Claudius Nero'],
    'caligula': ['Gaius Caesar Germanicus', 'Caligula'],
    'claudius': ['Tiberius Claudius Caesar Augustus Germanicus', 'Claudius'],
    'nero': ['Nero Claudius Caesar Augustus Germanicus', 'Nero'],
    'vespasian': ['Titus Flavius Vespasianus', 'Vespasian'],
    'trajan': ['Marcus Ulpius Traianus', 'Trajan', 'Optimus Princeps'],
    'hadrian': ['Publius Aelius Hadrianus', 'Hadrian'],
    'marcus-aurelius': ['Marcus Aurelius Antoninus', '哲人王', 'Philosopher King'],
    'diocletian': ['Gaius Aurelius Valerius Diocletianus', 'Diocletian'],
    'theodosius-i': ['Theodosius the Great', '狄奥多西大帝'],
    # Byzantium
    'heraclius': ['Heraclius', 'Flavius Heraclius Augustus'],
    'basil-ii': ['Basil II Porphyrogenitus', 'Bulgar-Slayer', '保加利亚屠夫'],
    'alexios-i': ['Alexius I Comnenus', 'Alexios I Komnenos'],
    'constantine-xi': ['Constantine XI Dragases Palaiologos', '君士坦丁·帕里奥洛格斯', 'Marble Emperor'],
    # England
    'henry-ii': ['Henry II Plantagenet', 'Henry Curtmantle'],
    'richard-i': ['Richard the Lionheart', 'Richard Coeur de Lion', 'Ricardus Rex'],
    'king-john': ['John Lackland', 'John of England', '无地王约翰'],
    'edward-i': ['Edward Longshanks', 'Hammer of the Scots', '长腿爱德华'],
    'henry-viii': ['Henry VIII Tudor', 'Defender of the Faith'],
    'charles-i': ['Charles Stuart', 'Charles I of England'],
    'victoria': ['Alexandrina Victoria', 'Empress of India', '欧洲祖母'],
    # France
    'louis-ix': ['Saint Louis', 'Louis IX of France', '圣路易'],
    'philip-ii-augustus': ['Philip II of France', 'Philippe Auguste'],
    'philip-iv': ['Philip the Fair', 'Philippe le Bel', '美男子腓力'],
    'francis-i': ['Francis I of France', 'Francois Ier'],
    'henry-iv-france': ['Henry IV of France', 'Henri IV', 'Good King Henry', 'Henri le Grand'],
    'louis-xvi': ['Louis XVI of France', 'Citizen Louis Capet', '路易·卡佩'],
    'napoleon-iii': ['Louis-Napoleon Bonaparte', 'Charles-Louis Napoleon Bonaparte'],
    # HRE
    'otto-i': ['Otto the Great', 'Otto I of Germany'],
    'frederick-barbarossa': ['Frederick I Barbarossa', 'Friedrich Barbarossa', '巴巴罗萨'],
    'frederick-ii': ['Frederick II of Hohenstaufen', 'Stupor Mundi', '世界惊奇'],
    'charles-v': ['Charles V of Habsburg', 'Carlos I of Spain', 'Karl V'],
    'maria-theresa': ['Maria Theresia', 'Maria Theresa of Austria'],
    # Russia
    'ivan-iii': ['Ivan the Great', 'Ivan III of Russia', 'Gatherer of the Russian Lands'],
    'catherine-the-great': ['Catherine II of Russia', 'Sophie Friederike Auguste', '叶卡捷琳娜二世'],
    'alexander-i': ['Alexander I of Russia', 'Alexander Pavlovich'],
    'alexander-ii': ['Alexander II of Russia', 'Alexander the Liberator', '解放者沙皇'],
    'nicholas-ii': ['Nicholas II of Russia', 'Nikolai Alexandrovich Romanov', '末代沙皇'],
    # Ottomans
    'osman-i': ['Osman Gazi', 'Osman Bey'],
    'selim-i': ['Selim the Grim', 'Yavuz Sultan Selim', '冷酷者塞利姆'],
    'selim-ii': ['Selim the Sot', 'Selim the Blond', '醉鬼塞利姆'],
    'murad-iv': ['Murad the Cruel', 'Murad IV of Turkey'],
    # Persia
    'darius-i': ['Darius the Great', 'Darayavaush', '大流士'],
    'xerxes-i': ['Xerxes the Great', 'Khshayarsha', '薛西斯', 'Ahasuerus'],
    'shapur-i': ['Shapur I of Persia', 'King of Kings'],
    'khosrow-i': ['Khosrow Anushirvan', 'Chosroes I', '不朽的灵魂'],
    'abbas-i': ['Shah Abbas the Great', '阿巴斯大帝'],
    # Egypt
    'hatshepsut': ['Hatshepsut', 'Maatkare'],
    'akhenaten': ['Amenhotep IV', 'Akhenaton', '阿蒙霍特普四世'],
    'tutankhamun': ['Tutankhamen', 'King Tut', 'Tutankhaten', '图坦卡门'],
    # Japan
    'empress-suiko': ['Suiko-tenno', '推古'],
    'emperor-kammu': ['Kammu-tenno', '桓武'],
    'oda-nobunaga': ['Oda Nobunaga', 'Demon King', '第六天魔王', 'Nobunaga'],
    'toyotomi-hideyoshi': ['Toyotomi Hideyoshi', 'Hideyoshi', 'Taiko', '太阁'],
    'emperor-go-daigo': ['Go-Daigo-tenno', '后醍醐'],
    # India
    'chandragupta-maurya': ['Chandragupta', 'Sandrocottus', '孔雀王朝开创者'],
    'chandragupta-ii': ['Chandragupta Vikramaditya', '超日王', 'Vikramaditya'],
    # Korea
    'gwanggaeto': ['Gwanggaeto', '广开土王', '好太王', 'King Gwanggaeto'],
    'taejo-goryeo': ['王建', 'Wang Geon', 'Taejo Wang Geon'],
    'sejong': ['Sejong the Great', '李祹', 'Yi Do', 'King Sejong'],
    'yeongjo': ['King Yeongjo', '李昑', 'Yi Geum', '英祖大王'],
    # Americas
    'montezuma-ii': ['Moctezuma II', 'Motecuhzoma Xocoyotzin', '蒙特苏马二世'],
    'pachacuti': ['Pachacuti Inca Yupanqui', '帕查库特克·印卡·尤潘基'],
    'simon-bolivar': ['El Libertador', 'Bolivar', 'Simon Jose Antonio de la Santisima Trinidad Bolivar'],
}

count = 0
for rid, new_alt_names in fixes.items():
    # Find the entry in mockData.ts
    pattern = rf"(  id: '{re.escape(rid)}',.*?alternativeNames: )\[(.*?)\]"
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"  NOT FOUND: {rid}")
        continue

    old_alts = match.group(2).strip()
    # Parse existing alt names
    if old_alts:
        # Split by ' and remove empty
        existing = [x.strip().strip("'\"") for x in old_alts.split(',') if x.strip().strip("'\"")]
    else:
        existing = []

    # Add only names not already present
    for name in new_alt_names:
        if name not in existing:
            existing.append(name)

    # Build new alternativeNames string
    new_alt_str = ', '.join(f"'{a}'" for a in existing)

    # Replace in content
    old_str = match.group(0)
    new_str = match.group(1) + '[' + new_alt_str + ']'
    content = content.replace(old_str, new_str, 1)
    count += 1

with open(TARGET, 'w') as f:
    f.write(content)

print(f"Fixed {count} entries")
print("Run 'tsc --noEmit' to verify")
