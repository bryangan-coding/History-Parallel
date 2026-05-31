export interface CivilizationPeriod {
  id: string;
  name: string;
  nameEn: string;
  startYear: number;
  endYear: number;
  civilizationId: string;
}

export interface Civilization {
  id: string;
  name: string;
  nameEn: string;
  color: string;
  periods: CivilizationPeriod[];
  keyEvents: CivilizationEvent[];
}

export interface CivilizationEvent {
  year: number;
  title: string;
  titleEn: string;
  civilizationId: string;
}

export const civilizations: Civilization[] = [
  {
    id: 'china',
    name: '中国',
    nameEn: 'China',
    color: '#b91c1c',
    periods: [
      { id: 'china-shang', name: '商朝', nameEn: 'Shang Dynasty', startYear: -1600, endYear: -1046, civilizationId: 'china' },
      { id: 'china-zhou', name: '周朝', nameEn: 'Zhou Dynasty', startYear: -1046, endYear: -256, civilizationId: 'china' },
      { id: 'china-qin', name: '秦朝', nameEn: 'Qin Dynasty', startYear: -221, endYear: -207, civilizationId: 'china' },
      { id: 'china-han', name: '汉朝', nameEn: 'Han Dynasty', startYear: -206, endYear: 220, civilizationId: 'china' },
      { id: 'china-sanguo', name: '三国', nameEn: 'Three Kingdoms', startYear: 220, endYear: 280, civilizationId: 'china' },
      { id: 'china-jin', name: '晋/南北朝', nameEn: 'Jin & S. Dynasties', startYear: 265, endYear: 589, civilizationId: 'china' },
      { id: 'china-sui-tang', name: '隋唐', nameEn: 'Sui & Tang', startYear: 581, endYear: 907, civilizationId: 'china' },
      { id: 'china-song', name: '宋/辽/金/西夏', nameEn: 'Song, Liao, Jin, Xixia', startYear: 960, endYear: 1279, civilizationId: 'china' },
      { id: 'china-yuan', name: '元朝', nameEn: 'Yuan Dynasty', startYear: 1271, endYear: 1368, civilizationId: 'china' },
      { id: 'china-ming', name: '明朝', nameEn: 'Ming Dynasty', startYear: 1368, endYear: 1644, civilizationId: 'china' },
      { id: 'china-qing', name: '清朝', nameEn: 'Qing Dynasty', startYear: 1644, endYear: 1912, civilizationId: 'china' },
    ],
    keyEvents: [
      { year: -221, title: '秦统一六国', titleEn: 'Qin Unification', civilizationId: 'china' },
      { year: -139, title: '张骞出使西域', titleEn: 'Zhang Qian to the West', civilizationId: 'china' },
      { year: 105, title: '蔡伦改进造纸术', titleEn: 'Cai Lun Improves Paper', civilizationId: 'china' },
      { year: 618, title: '唐朝建立', titleEn: 'Tang Dynasty Founded', civilizationId: 'china' },
      { year: 755, title: '安史之乱', titleEn: 'An Lushan Rebellion', civilizationId: 'china' },
      { year: 960, title: '北宋建立', titleEn: 'Northern Song Founded', civilizationId: 'china' },
      { year: 1069, title: '王安石变法', titleEn: 'Wang Anshi Reforms', civilizationId: 'china' },
      { year: 1206, title: '蒙古统一', titleEn: 'Mongol Unification', civilizationId: 'china' },
      { year: 1405, title: '郑和下西洋', titleEn: 'Zheng He Voyages', civilizationId: 'china' },
      { year: 1644, title: '明朝灭亡', titleEn: 'Fall of Ming', civilizationId: 'china' },
    ],
  },
  {
    id: 'europe',
    name: '欧洲',
    nameEn: 'Europe',
    color: '#1e40af',
    periods: [
      { id: 'europe-greece', name: '古希腊', nameEn: 'Ancient Greece', startYear: -800, endYear: -146, civilizationId: 'europe' },
      { id: 'europe-rome', name: '罗马共和国/帝国', nameEn: 'Roman Rep./Empire', startYear: -509, endYear: 476, civilizationId: 'europe' },
      { id: 'europe-byzantine', name: '拜占庭帝国', nameEn: 'Byzantine Empire', startYear: 330, endYear: 1453, civilizationId: 'europe' },
      { id: 'europe-frankish', name: '法兰克王国', nameEn: 'Frankish Kingdom', startYear: 481, endYear: 843, civilizationId: 'europe' },
      { id: 'europe-hre', name: '神圣罗马帝国', nameEn: 'Holy Roman Empire', startYear: 800, endYear: 1806, civilizationId: 'europe' },
      { id: 'europe-england', name: '英格兰/英国', nameEn: 'England/Britain', startYear: 927, endYear: 1901, civilizationId: 'europe' },
      { id: 'europe-renaissance', name: '文艺复兴', nameEn: 'Renaissance', startYear: 1300, endYear: 1600, civilizationId: 'europe' },
      { id: 'europe-modern', name: '近代欧洲', nameEn: 'Modern Europe', startYear: 1500, endYear: 1900, civilizationId: 'europe' },
    ],
    keyEvents: [
      { year: -431, title: '伯罗奔尼撒战争', titleEn: 'Peloponnesian War', civilizationId: 'europe' },
      { year: -44, title: '凯撒遇刺', titleEn: 'Caesar Assassinated', civilizationId: 'europe' },
      { year: 476, title: '西罗马灭亡', titleEn: 'Fall of Western Rome', civilizationId: 'europe' },
      { year: 800, title: '查理曼加冕', titleEn: 'Charlemagne Crowned', civilizationId: 'europe' },
      { year: 1066, title: '诺曼征服', titleEn: 'Norman Conquest', civilizationId: 'europe' },
      { year: 1215, title: '大宪章', titleEn: 'Magna Carta', civilizationId: 'europe' },
      { year: 1453, title: '君士坦丁堡陷落', titleEn: 'Fall of Constantinople', civilizationId: 'europe' },
      { year: 1492, title: '哥伦布到达美洲', titleEn: 'Columbus in Americas', civilizationId: 'europe' },
      { year: 1517, title: '宗教改革', titleEn: 'Reformation', civilizationId: 'europe' },
      { year: 1789, title: '法国大革命', titleEn: 'French Revolution', civilizationId: 'europe' },
    ],
  },
  {
    id: 'middle-east',
    name: '中东',
    nameEn: 'Middle East',
    color: '#b45309',
    periods: [
      { id: 'me-egypt', name: '古埃及', nameEn: 'Ancient Egypt', startYear: -3100, endYear: -30, civilizationId: 'middle-east' },
      { id: 'me-persia', name: '波斯帝国', nameEn: 'Persian Empire', startYear: -550, endYear: -330, civilizationId: 'middle-east' },
      { id: 'me-islamic', name: '伊斯兰哈里发', nameEn: 'Islamic Caliphates', startYear: 632, endYear: 1258, civilizationId: 'middle-east' },
      { id: 'me-seljuk', name: '塞尔柱帝国', nameEn: 'Seljuk Empire', startYear: 1037, endYear: 1194, civilizationId: 'middle-east' },
      { id: 'me-ottoman', name: '奥斯曼帝国', nameEn: 'Ottoman Empire', startYear: 1299, endYear: 1922, civilizationId: 'middle-east' },
      { id: 'me-safavid', name: '萨法维王朝', nameEn: 'Safavid Dynasty', startYear: 1501, endYear: 1736, civilizationId: 'middle-east' },
    ],
    keyEvents: [
      { year: -1750, title: '汉谟拉比法典', titleEn: 'Code of Hammurabi', civilizationId: 'middle-east' },
      { year: -539, title: '居鲁士解放巴比伦', titleEn: 'Cyrus Frees Babylon', civilizationId: 'middle-east' },
      { year: 622, title: '希吉拉（伊斯兰纪元）', titleEn: 'Hijra (Islamic Era)', civilizationId: 'middle-east' },
      { year: 762, title: '巴格达建都', titleEn: 'Baghdad Founded', civilizationId: 'middle-east' },
      { year: 1055, title: '塞尔柱入主巴格达', titleEn: 'Seljuks Enter Baghdad', civilizationId: 'middle-east' },
      { year: 1099, title: '第一次十字军占耶路撒冷', titleEn: '1st Crusade Takes Jerusalem', civilizationId: 'middle-east' },
      { year: 1187, title: '萨拉丁收复耶路撒冷', titleEn: 'Saladin Retakes Jerusalem', civilizationId: 'middle-east' },
      { year: 1258, title: '蒙古灭巴格达', titleEn: 'Mongols Sack Baghdad', civilizationId: 'middle-east' },
      { year: 1453, title: '奥斯曼占君士坦丁堡', titleEn: 'Ottomans Take Constantinople', civilizationId: 'middle-east' },
    ],
  },
  {
    id: 'india',
    name: '印度',
    nameEn: 'India',
    color: '#d97706',
    periods: [
      { id: 'india-indus', name: '印度河文明', nameEn: 'Indus Valley', startYear: -2600, endYear: -1500, civilizationId: 'india' },
      { id: 'india-vedic', name: '吠陀时代', nameEn: 'Vedic Period', startYear: -1500, endYear: -600, civilizationId: 'india' },
      { id: 'india-maurya', name: '孔雀王朝', nameEn: 'Maurya Empire', startYear: -322, endYear: -185, civilizationId: 'india' },
      { id: 'india-gupta', name: '笈多王朝', nameEn: 'Gupta Empire', startYear: 320, endYear: 550, civilizationId: 'india' },
      { id: 'india-chola', name: '朱罗王朝', nameEn: 'Chola Dynasty', startYear: 850, endYear: 1279, civilizationId: 'india' },
      { id: 'india-delhi', name: '德里苏丹国', nameEn: 'Delhi Sultanate', startYear: 1206, endYear: 1526, civilizationId: 'india' },
      { id: 'india-mughal', name: '莫卧儿帝国', nameEn: 'Mughal Empire', startYear: 1526, endYear: 1857, civilizationId: 'india' },
    ],
    keyEvents: [
      { year: -261, title: '阿育王皈依佛教', titleEn: 'Ashoka Embraces Buddhism', civilizationId: 'india' },
      { year: 320, title: '笈多王朝建立', titleEn: 'Gupta Empire Founded', civilizationId: 'india' },
      { year: 1025, title: '朱罗海军远征', titleEn: 'Chola Naval Expedition', civilizationId: 'india' },
      { year: 1192, title: '穆斯林征服北印度', titleEn: 'Muslim Conquest of N. India', civilizationId: 'india' },
      { year: 1526, title: '莫卧儿帝国建立', titleEn: 'Mughal Empire Founded', civilizationId: 'india' },
      { year: 1556, title: '阿克巴大帝登基', titleEn: 'Akbar the Great Crowned', civilizationId: 'india' },
    ],
  },
  {
    id: 'japan',
    name: '日本',
    nameEn: 'Japan',
    color: '#0d9488',
    periods: [
      { id: 'japan-yayoi', name: '弥生/古坟', nameEn: 'Yayoi & Kofun', startYear: -300, endYear: 538, civilizationId: 'japan' },
      { id: 'japan-asuka', name: '飞鸟/奈良', nameEn: 'Asuka & Nara', startYear: 538, endYear: 794, civilizationId: 'japan' },
      { id: 'japan-heian', name: '平安时代', nameEn: 'Heian Period', startYear: 794, endYear: 1185, civilizationId: 'japan' },
      { id: 'japan-kamakura', name: '镰仓幕府', nameEn: 'Kamakura Shogunate', startYear: 1185, endYear: 1333, civilizationId: 'japan' },
      { id: 'japan-muromachi', name: '室町/战国', nameEn: 'Muromachi & Sengoku', startYear: 1336, endYear: 1600, civilizationId: 'japan' },
      { id: 'japan-edo', name: '江户幕府', nameEn: 'Edo Shogunate', startYear: 1603, endYear: 1868, civilizationId: 'japan' },
    ],
    keyEvents: [
      { year: 794, title: '迁都平安京（京都）', titleEn: 'Capital Moves to Heian-kyo', civilizationId: 'japan' },
      { year: 1008, title: '源氏物语完成', titleEn: 'Tale of Genji Completed', civilizationId: 'japan' },
      { year: 1192, title: '镰仓幕府建立', titleEn: 'Kamakura Shogunate Founded', civilizationId: 'japan' },
      { year: 1603, title: '江户幕府建立', titleEn: 'Edo Shogunate Founded', civilizationId: 'japan' },
      { year: 1868, title: '明治维新', titleEn: 'Meiji Restoration', civilizationId: 'japan' },
    ],
  },
  {
    id: 'americas',
    name: '美洲',
    nameEn: 'Americas',
    color: '#7c3aed',
    periods: [
      { id: 'americas-olmec', name: '奥尔梅克', nameEn: 'Olmec', startYear: -1200, endYear: -400, civilizationId: 'americas' },
      { id: 'americas-maya', name: '玛雅文明', nameEn: 'Maya', startYear: -2000, endYear: 1500, civilizationId: 'americas' },
      { id: 'americas-teotihuacan', name: '特奥蒂瓦坎', nameEn: 'Teotihuacan', startYear: -100, endYear: 650, civilizationId: 'americas' },
      { id: 'americas-aztec', name: '阿兹特克', nameEn: 'Aztec Empire', startYear: 1325, endYear: 1521, civilizationId: 'americas' },
      { id: 'americas-inca', name: '印加帝国', nameEn: 'Inca Empire', startYear: 1438, endYear: 1533, civilizationId: 'americas' },
    ],
    keyEvents: [
      { year: 1325, title: '特诺奇蒂特兰建城', titleEn: 'Tenochtitlan Founded', civilizationId: 'americas' },
      { year: 1438, title: '印加帝国兴起', titleEn: 'Inca Empire Rises', civilizationId: 'americas' },
      { year: 1492, title: '哥伦布到达美洲', titleEn: 'Columbus Arrives', civilizationId: 'americas' },
      { year: 1519, title: '科尔特斯征服阿兹特克', titleEn: 'Cortés Conquers Aztecs', civilizationId: 'americas' },
      { year: 1533, title: '皮萨罗征服印加', titleEn: 'Pizarro Conquers Inca', civilizationId: 'americas' },
    ],
  },
  {
    id: 'mongol',
    name: '蒙古帝国',
    nameEn: 'Mongol Empire',
    color: '#047857',
    periods: [
      { id: 'mongol-empire', name: '蒙古帝国', nameEn: 'Mongol Empire', startYear: 1206, endYear: 1368, civilizationId: 'mongol' },
      { id: 'mongol-yuan', name: '元朝', nameEn: 'Yuan Dynasty', startYear: 1271, endYear: 1368, civilizationId: 'mongol' },
      { id: 'mongol-khans', name: '四大汗国', nameEn: 'Four Khanates', startYear: 1260, endYear: 1502, civilizationId: 'mongol' },
    ],
    keyEvents: [
      { year: 1206, title: '成吉思汗建蒙古帝国', titleEn: 'Genghis Khan Unites Mongols', civilizationId: 'mongol' },
      { year: 1215, title: '蒙古攻占金中都', titleEn: 'Mongols Take Jin Capital', civilizationId: 'mongol' },
      { year: 1258, title: '蒙古灭巴格达', titleEn: 'Mongols Sack Baghdad', civilizationId: 'mongol' },
      { year: 1271, title: '忽必烈建元', titleEn: 'Khubilai Establishes Yuan', civilizationId: 'mongol' },
      { year: 1279, title: '南宋灭亡', titleEn: 'Southern Song Falls', civilizationId: 'mongol' },
    ],
  },
];

export function getCivilizationById(id: string): Civilization | undefined {
  return civilizations.find((c) => c.id === id);
}
