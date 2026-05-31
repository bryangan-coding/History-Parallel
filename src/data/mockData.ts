import type { Region, Person, HistoricalEvent, Source } from '@/lib/types';

// ==================== REGIONS ====================

export const regions: Region[] = [
  {
    id: 'china',
    name: '中国',
    nameEn: 'China',
    slug: 'china',
    description: '涵盖历史上中国各朝代疆域，包括中原王朝与周边政权。',
    descriptionEn: 'Historical Chinese territories across dynasties, including the Central Plains and surrounding polities.',
  },
  {
    id: 'song-dynasty',
    name: '北宋',
    nameEn: 'Northern Song',
    slug: 'song-dynasty',
    parentRegionId: 'china',
    description: '960年—1127年，赵匡胤建立，都城开封。经济文化高度繁荣的时期。',
    descriptionEn: '960–1127. Founded by Zhao Kuangyin, capital at Kaifeng. An era of great economic and cultural prosperity.',
  },
  {
    id: 'europe',
    name: '欧洲',
    nameEn: 'Europe',
    slug: 'europe',
    description: '中世纪欧洲，包括英格兰、法兰西、神圣罗马帝国、拜占庭等。',
    descriptionEn: 'Medieval Europe, including England, France, the Holy Roman Empire, Byzantium, and others.',
  },
  {
    id: 'england',
    name: '英格兰',
    nameEn: 'England',
    slug: 'england',
    parentRegionId: 'europe',
    description: '诺曼征服后的盎格鲁-诺曼王国。',
    descriptionEn: 'The Anglo-Norman kingdom after the Norman Conquest.',
  },
  {
    id: 'byzantine',
    name: '拜占庭帝国',
    nameEn: 'Byzantine Empire',
    slug: 'byzantine',
    parentRegionId: 'europe',
    description: '东罗马帝国，首都君士坦丁堡。11世纪经历了马其顿王朝末期与科穆宁王朝的崛起。',
    descriptionEn: 'The Eastern Roman Empire, capital Constantinople. The 11th century saw the end of the Macedonian dynasty and the rise of the Komnenoi.',
  },
  {
    id: 'middle-east',
    name: '中东 / 伊斯兰世界',
    nameEn: 'Middle East / Islamic World',
    slug: 'middle-east',
    description: '包括阿拔斯哈里发、塞尔柱帝国、法蒂玛王朝等伊斯兰政权。',
    descriptionEn: 'Including the Abbasid Caliphate, Seljuk Empire, Fatimid Caliphate, and other Islamic polities.',
  },
  {
    id: 'seljuk',
    name: '塞尔柱帝国',
    nameEn: 'Seljuk Empire',
    slug: 'seljuk',
    parentRegionId: 'middle-east',
    description: '1037年—1194年，突厥人建立的帝国，控制了从安纳托利亚到中亚的广大地区。',
    descriptionEn: '1037–1194. A Turkic empire that controlled vast territories from Anatolia to Central Asia.',
  },
  {
    id: 'japan',
    name: '日本',
    nameEn: 'Japan',
    slug: 'japan',
    description: '平安时代中后期，贵族政治与摄关政治的鼎盛时期。',
    descriptionEn: 'Mid-to-late Heian period, the zenith of aristocratic rule and regency politics.',
  },
  {
    id: 'india',
    name: '印度',
    nameEn: 'India',
    slug: 'india',
    description: '中世纪印度，包括朱罗王朝、波罗王朝等。',
    descriptionEn: 'Medieval India, including the Chola dynasty, Pala Empire, and others.',
  },
];

// ==================== SOURCES ====================

export const sources: Source[] = [
  {
    id: 'src-ztzy',
    title: '《资治通鉴》',
    titleEn: 'Zizhi Tongjian (Comprehensive Mirror for Aid in Government)',
    author: '司马光等',
    year: 1084,
    note: '编年体通史，涵盖战国至五代的历史。',
    license: 'Public Domain',
  },
  {
    id: 'src-ss',
    title: '《宋史》',
    titleEn: 'History of Song (Song Shi)',
    author: '脱脱等',
    publisher: '元朝官修',
    year: 1345,
    note: '二十四史之一，记录宋代历史的正史。',
    license: 'Public Domain',
  },
  {
    id: 'src-xzsl',
    title: '《续资治通鉴长编》',
    titleEn: 'Xu Zizhi Tongjian Changbian (Extended Continuation to Zizhi Tongjian)',
    author: '李焘',
    year: 1183,
    publisher: '南宋',
    note: '记载北宋九朝历史的编年体史书。',
    license: 'Public Domain',
  },
  {
    id: 'src-domesday',
    title: 'Domesday Book',
    titleEn: 'Domesday Book',
    author: 'William I Commissioners',
    year: 1086,
    publisher: 'Norman England',
    note: '英格兰土地清查记录，诺曼统治的重要文献。',
    license: 'Public Domain',
  },
  {
    id: 'src-asc',
    title: 'Anglo-Saxon Chronicle',
    titleEn: 'Anglo-Saxon Chronicle',
    author: '多位修道院编年史家',
    publisher: '英格兰各修道院',
    note: '英格兰历史的重要原始文献。',
    license: 'Public Domain',
  },
  {
    id: 'src-alexiad',
    title: 'The Alexiad',
    titleEn: 'The Alexiad',
    author: 'Anna Komnene',
    year: 1148,
    publisher: 'Byzantine Empire',
    note: '拜占庭公主安娜·科穆宁娜撰写的历史著作，记录其父阿历克塞一世时期的历史。',
    license: 'Public Domain',
  },
  {
    id: 'src-papal',
    title: 'Papal Registers of Gregory VII',
    titleEn: 'Papal Registers of Gregory VII',
    author: '教皇格里高利七世教廷',
    publisher: 'Rome',
    note: '记录格里高利七世教皇期间的法令和通信。',
    license: 'Public Domain',
  },
  {
    id: 'src-eiga',
    title: '《荣花物语》',
    titleEn: 'Eiga Monogatari (A Tale of Flowering Fortunes)',
    author: '赤染卫门（推定）',
    year: 1028,
    publisher: '平安日本',
    note: '记载藤原道长全盛期的历史物语。',
    license: 'Public Domain',
  },
  {
    id: 'src-seljuk',
    title: 'Cambridge History of Iran, Vol. 5',
    titleEn: 'Cambridge History of Iran, Vol. 5',
    author: 'J.A. Boyle (ed.)',
    publisher: 'Cambridge University Press',
    year: 1968,
    note: '关于塞尔柱时期伊朗和中东历史的学术著作。',
    license: 'Copyright',
    url: 'https://www.cambridge.org/',
  },
  {
    id: 'src-byz-empire',
    title: 'A History of the Byzantine State and Society',
    titleEn: 'A History of the Byzantine State and Society',
    author: 'Warren Treadgold',
    publisher: 'Stanford University Press',
    year: 1997,
    note: '综合性的拜占庭帝国通史。',
    license: 'Copyright',
  },
  {
    id: 'src-chola',
    title: 'The Cholas',
    titleEn: 'The Cholas',
    author: 'K.A. Nilakanta Sastri',
    publisher: 'University of Madras',
    year: 1955,
    note: '南印度朱罗王朝的经典研究著作。',
    license: 'Copyright',
  },
  {
    id: 'src-prosop',
    title: 'Prosopography of the Later Roman Empire',
    titleEn: 'Prosopography of the Later Roman Empire',
    publisher: 'Cambridge University Press',
    year: 1980,
    note: '晚期罗马帝国和拜占庭人物志。',
    license: 'Copyright',
  },
];

// ==================== PEOPLE ====================

export const people: Person[] = [
  {
    id: 'su-shi',
    name: '苏轼',
    nameEn: 'Su Shi (Su Dongpo)',
    alternativeNames: ['苏东坡', '子瞻', '和仲', 'Su Shi', 'Su Dongpo'],
    birthYear: 1037,
    deathYear: 1101,
    regionId: 'song-dynasty',
    tags: ['文学家', '书画家', '政治人物', '北宋', '唐宋八大家'],
    tagsEn: ['Writer', 'Calligrapher', 'Statesman', 'Northern Song'],
    summary: '北宋中期文坛领袖，诗词文书画俱绝。一生历经仁宗、英宗、神宗、哲宗、徽宗五朝，仕途坎坷。',
    summaryEn: 'Literary giant of the Northern Song, excelling in poetry, prose, calligraphy, and painting. His career spanned five reigns and was marked by repeated political exile.',
    sourceIds: ['src-ss'],
  },
  {
    id: 'wang-anshi',
    name: '王安石',
    nameEn: 'Wang Anshi',
    alternativeNames: ['王介甫', '半山', 'Wang Anshi'],
    birthYear: 1021,
    deathYear: 1086,
    regionId: 'song-dynasty',
    tags: ['政治人物', '文学家', '改革家', '北宋', '唐宋八大家'],
    tagsEn: ['Statesman', 'Writer', 'Reformer', 'Northern Song'],
    summary: '北宋著名改革家，神宗时期主持熙宁变法，力图富国强兵。',
    summaryEn: 'Renowned Northern Song reformer who led the Xining Reforms under Emperor Shenzong to strengthen the state and military.',
    sourceIds: ['src-ss', 'src-xzsl'],
  },
  {
    id: 'sima-guang',
    name: '司马光',
    nameEn: 'Sima Guang',
    alternativeNames: ['司马君实', 'Sima Guang'],
    birthYear: 1019,
    deathYear: 1086,
    regionId: 'song-dynasty',
    tags: ['政治人物', '史学家', '保守派', '北宋'],
    tagsEn: ['Statesman', 'Historian', 'Conservative', 'Northern Song'],
    summary: '北宋政治家、史学家，主持编纂编年体通史《资治通鉴》，政治上反对王安石变法。',
    summaryEn: 'Northern Song statesman and historian who compiled "Zizhi Tongjian" and opposed Wang Anshi\'s reforms.',
    sourceIds: ['src-ss', 'src-ztzy'],
  },
  {
    id: 'ouyang-xiu',
    name: '欧阳修',
    nameEn: 'Ouyang Xiu',
    alternativeNames: ['欧阳永叔', '醉翁', '六一居士', 'Ouyang Xiu'],
    birthYear: 1007,
    deathYear: 1072,
    regionId: 'song-dynasty',
    tags: ['文学家', '史学家', '政治人物', '北宋', '唐宋八大家'],
    tagsEn: ['Writer', 'Historian', 'Statesman', 'Northern Song'],
    summary: '北宋文学革新运动领袖，唐宋八大家之一。文学上推行古文运动，史学上参与编纂《新唐书》。',
    summaryEn: 'Leader of the Northern Song literary reform movement. Promoted the Classical Prose Movement and co-edited the "New Book of Tang."',
    sourceIds: ['src-ss'],
  },
  {
    id: 'william-conqueror',
    name: '威廉一世（征服者）',
    nameEn: 'William I (the Conqueror)',
    alternativeNames: ['William the Conqueror', 'William I of England', '诺曼底公爵威廉', 'William of Normandy'],
    birthYear: 1028,
    deathYear: 1087,
    regionId: 'england',
    tags: ['君主', '军事家', '诺曼征服', '欧洲'],
    tagsEn: ['Monarch', 'Military Leader', 'Norman Conquest', 'Europe'],
    summary: '诺曼底公爵，1066年征服英格兰，建立诺曼王朝，彻底改变英格兰的政治和社会结构。',
    summaryEn: 'Duke of Normandy who conquered England in 1066, established the Norman dynasty, and fundamentally transformed English politics and society.',
    sourceIds: ['src-asc', 'src-domesday'],
  },
  {
    id: 'gregory-vii',
    name: '格里高利七世',
    nameEn: 'Pope Gregory VII',
    alternativeNames: ['Pope Gregory VII', 'Hildebrand of Sovana', '格列高利七世'],
    birthYear: 1015,
    deathYear: 1085,
    regionId: 'europe',
    tags: ['宗教人物', '教皇', '教会改革', '欧洲'],
    tagsEn: ['Religious Figure', 'Pope', 'Church Reform', 'Europe'],
    summary: '罗马教皇，推行格列高利改革，与神圣罗马帝国皇帝亨利四世发生"叙任权斗争"，引发卡诺莎之辱事件。',
    summaryEn: 'Pope who launched the Gregorian Reform and clashed with Holy Roman Emperor Henry IV over investiture, leading to the dramatic encounter at Canossa.',
    sourceIds: ['src-papal'],
  },
  {
    id: 'anselm',
    name: '安瑟伦',
    nameEn: 'Anselm of Canterbury',
    alternativeNames: ['Anselm of Canterbury', '圣安瑟伦', 'Anselm of Aosta'],
    birthYear: 1033,
    deathYear: 1109,
    regionId: 'europe',
    tags: ['宗教人物', '哲学家', '神学家', '经院哲学', '欧洲'],
    tagsEn: ['Religious Figure', 'Philosopher', 'Theologian', 'Scholasticism', 'Europe'],
    summary: '坎特伯雷大主教，经院哲学奠基人，提出"信仰寻求理解"和上帝存在的本体论证明。',
    summaryEn: 'Archbishop of Canterbury and father of Scholasticism, known for "faith seeking understanding" and the ontological argument for God\'s existence.',
    sourceIds: ['src-papal'],
  },
  {
    id: 'murasaki-shikibu',
    name: '紫式部',
    nameEn: 'Murasaki Shikibu',
    alternativeNames: ['Murasaki Shikibu', '藤原香子'],
    birthYear: 973,
    deathYear: 1014,
    regionId: 'japan',
    tags: ['文学家', '平安时代', '日本'],
    tagsEn: ['Writer', 'Heian Period', 'Japan'],
    summary: '平安时代中期女作家，《源氏物语》作者。作品被认为是世界最早的长篇小说之一。',
    summaryEn: 'Lady-in-waiting and writer of mid-Heian Japan, author of "The Tale of Genji," widely considered to be the world\'s first novel.',
    sourceIds: ['src-eiga'],
  },
  {
    id: 'fujiwara-michinaga',
    name: '藤原道长',
    nameEn: 'Fujiwara no Michinaga',
    alternativeNames: ['Fujiwara no Michinaga', '御堂关白'],
    birthYear: 966,
    deathYear: 1028,
    regionId: 'japan',
    tags: ['政治人物', '贵族', '摄关政治', '平安时代', '日本'],
    tagsEn: ['Statesman', 'Aristocrat', 'Regency Politics', 'Heian Period', 'Japan'],
    summary: '平安时代中期最有权势的贵族，摄关政治的巅峰人物。其三个女儿分别成为三位天皇的皇后。',
    summaryEn: 'The most powerful aristocrat of mid-Heian Japan and the pinnacle of regency rule. Three of his daughters became empresses to three successive emperors.',
    sourceIds: ['src-eiga'],
  },
  {
    id: 'alexios-komnenos',
    name: '阿历克塞一世',
    nameEn: 'Alexios I Komnenos',
    alternativeNames: ['Alexios I Komnenos', 'Alexius Comnenus'],
    birthYear: 1048,
    deathYear: 1118,
    regionId: 'byzantine',
    tags: ['君主', '军事家', '科穆宁王朝', '拜占庭', '十字军'],
    tagsEn: ['Emperor', 'Military Leader', 'Komnenos Dynasty', 'Byzantium', 'Crusades'],
    summary: '拜占庭帝国科穆宁王朝开国皇帝，面对塞尔柱入侵和诺曼威胁，请求西方援助，间接促成第一次十字军东征。',
    summaryEn: 'Founder of the Komnenian dynasty, who faced Seljuk and Norman threats and appealed for Western aid—a request that helped trigger the First Crusade.',
    sourceIds: ['src-alexiad', 'src-byz-empire'],
  },
];

// ==================== EVENTS ====================

export const events: HistoricalEvent[] = [
  // --- Chinese events (Song Dynasty) ---
  {
    id: 'evt-wutai',
    title: '乌台诗案',
    titleEn: 'The Crow Terrace Poetry Trial',
    startYear: 1079,
    regionId: 'song-dynasty',
    personIds: ['su-shi'],
    tags: ['政治事件', '北宋', '文字狱'],
    tagsEn: ['Political Event', 'Northern Song', 'Literary Inquisition'],
    importance: 5,
    summary: '苏轼因诗文被弹劾讥讽朝政，入御史台狱（乌台）百余日，震惊朝野。',
    summaryEn: 'Su Shi was impeached for allegedly mocking the government in his poetry and imprisoned in the Censorate jail (Crow Terrace) for over a hundred days.',
    description:
      '元丰二年（1079年），御史李定、舒亶等人指控苏轼在诗文中讥讽新法、影射朝廷。苏轼被捕入御史台监狱，被关押审讯一百余日。最终在多方营救之下，苏轼被贬为黄州团练副使，不得签署公事。此案是北宋最著名的文字狱，也标志着苏轼人生的重要转折。',
    descriptionEn:
      'In 1079, censors Li Ding and Shu Dan accused Su Shi of satirizing the New Policies and criticizing the court in his poems. He was imprisoned and interrogated for over a hundred days. After intervention by allies, he was demoted to Deputy Militia Commander of Huangzhou, with no authority to sign official documents—a turning point in his life.',
    sourceIds: ['src-ss', 'src-xzsl'],
    relatedEventIds: ['evt-sushi-huangzhou'],
  },
  {
    id: 'evt-sushi-huangzhou',
    title: '苏轼被贬黄州',
    titleEn: 'Su Shi Exiled to Huangzhou',
    startYear: 1080,
    endYear: 1084,
    regionId: 'song-dynasty',
    placeName: '黄州（今湖北黄冈）',
    placeNameEn: 'Huangzhou (present-day Huanggang, Hubei)',
    personIds: ['su-shi'],
    tags: ['政治事件', '贬谪', '北宋', '文学'],
    tagsEn: ['Political Event', 'Exile', 'Northern Song', 'Literature'],
    importance: 5,
    summary: '乌台诗案后，苏轼被贬黄州，在困顿中创作了大量传世名作，包括前后《赤壁赋》、《念奴娇·赤壁怀古》。',
    summaryEn: 'After the Crow Terrace Trial, Su Shi was exiled to Huangzhou, where in hardship he produced some of his greatest works, including the "Red Cliff Rhapsodies."',
    description:
      '1080年至1084年，苏轼谪居黄州。他自号"东坡居士"，在城东开荒种地，写下了中国文学史上最辉煌的篇章之一。《念奴娇·赤壁怀古》、前后《赤壁赋》、《定风波》等千古名篇均创作于此期。黄州时期是苏轼从仕途人物转变为伟大文学家的关键转折。',
    descriptionEn:
      'From 1080 to 1084, Su Shi lived in exile in Huangzhou. Adopting the name "Dongpo Jushi" (Resident of the Eastern Slope), he farmed and wrote some of the most celebrated works in Chinese literary history. The Huangzhou period marks his transformation from a political figure into a transcendent literary artist.',
    sourceIds: ['src-ss'],
    relatedEventIds: ['evt-wutai'],
  },
  {
    id: 'evt-wang-anshi-reform',
    title: '王安石变法（熙宁变法）',
    titleEn: 'Wang Anshi\'s Reforms (Xining Reforms)',
    startYear: 1069,
    endYear: 1085,
    regionId: 'song-dynasty',
    personIds: ['wang-anshi', 'sima-guang', 'su-shi'],
    tags: ['政治事件', '改革', '北宋'],
    tagsEn: ['Political Event', 'Reform', 'Northern Song'],
    importance: 5,
    summary: '宋神宗任用王安石推行大规模改革，包括青苗法、免役法、市易法等，引发激烈党争。',
    summaryEn: 'Emperor Shenzong empowered Wang Anshi to launch sweeping reforms—including the Green Sprouts Law and the Hired Service System—igniting fierce factional conflict.',
    description:
      '宋神宗熙宁年间，王安石出任参知政事并拜相，推行以富国强兵为目标的大规模改革。新法包括经济、军事、教育等多个领域：青苗法给农民低息贷款；免役法以钱代役；市易法平抑物价。改革遭到以司马光、苏轼等人为首的保守派强烈反对，形成了持续数十年的新旧党争。',
    descriptionEn:
      'During the Xining era, Wang Anshi became Chancellor and implemented reforms aimed at enriching the state and strengthening the military. Key measures included the Green Sprouts Law (low-interest agricultural loans), the Hired Service System (commuting labor duties with cash payments), and the Market Exchange Law. The reforms were fiercely opposed by conservatives led by Sima Guang and Su Shi, sparking decades of factional strife.',
    sourceIds: ['src-ss', 'src-xzsl'],
    relatedEventIds: ['evt-sima-zztj'],
  },
  {
    id: 'evt-sima-zztj',
    title: '司马光编纂《资治通鉴》',
    titleEn: 'Sima Guang Compiles "Zizhi Tongjian"',
    startYear: 1066,
    endYear: 1084,
    regionId: 'song-dynasty',
    personIds: ['sima-guang'],
    tags: ['著作', '史学', '北宋'],
    tagsEn: ['Scholarship', 'Historiography', 'Northern Song'],
    importance: 5,
    summary: '司马光历时19年编纂完成中国最重要的编年体通史之一，涵盖1362年历史。',
    summaryEn: 'Sima Guang spent 19 years compiling one of the most important Chinese historical chronicles, covering 1,362 years of history.',
    description:
      '治平三年（1066年），司马光开始编纂《资治通鉴》，得到了宋英宗和宋神宗的支持。历时十九年，于元丰七年（1084年）完成，共294卷，记录从周威烈王二十三年（公元前403年）到五代后周世宗显德六年（959年）共1362年的历史。这部著作成为中国史学史上最重要的著作之一。',
    descriptionEn:
      'Beginning in 1066 with imperial support, Sima Guang completed "Zizhi Tongjian" in 1084—294 volumes spanning 1,362 years from 403 BCE to 959 CE. It remains one of the monumental achievements of Chinese historiography.',
    sourceIds: ['src-ztzy'],
    relatedEventIds: ['evt-wang-anshi-reform'],
  },
  {
    id: 'evt-ouyang-xiu-xintangshu',
    title: '欧阳修主持编修《新唐书》',
    titleEn: 'Ouyang Xiu Edits "New Book of Tang"',
    startYear: 1044,
    endYear: 1060,
    regionId: 'song-dynasty',
    personIds: ['ouyang-xiu'],
    tags: ['著作', '史学', '北宋'],
    tagsEn: ['Scholarship', 'Historiography', 'Northern Song'],
    importance: 4,
    summary: '欧阳修与宋祁等人奉敕编修《新唐书》，对唐代历史进行了重新整理。',
    summaryEn: 'Ouyang Xiu and Song Qi led a commission to compile a revised history of the Tang dynasty.',
    description:
      '庆历四年，宋仁宗下诏重修《唐书》。欧阳修主持编修工作，与宋祁等人历时17年完成。新唐书对旧唐书进行了大量补充和修订，成为后世研究唐代历史的重要依据。',
    descriptionEn:
      'Emperor Renzong ordered a revision of the "Old Book of Tang" in 1044. Ouyang Xiu led the 17-year project, producing a significantly expanded and revised edition that became a cornerstone of Tang dynasty studies.',
    sourceIds: ['src-ss'],
    relatedEventIds: [],
  },
  {
    id: 'evt-song-liao-xixia',
    title: '北宋与辽、西夏三方对峙',
    titleEn: 'Northern Song\'s Three-Way Standoff with Liao and Western Xia',
    startYear: 1004,
    endYear: 1127,
    regionId: 'song-dynasty',
    personIds: [],
    tags: ['军事', '外交', '北宋'],
    tagsEn: ['Military', 'Diplomacy', 'Northern Song'],
    importance: 4,
    summary: '11世纪，北宋与北方辽朝、西北西夏形成长期对峙格局，通过岁币维持和平。',
    summaryEn: 'Throughout the 11th century, the Northern Song maintained a delicate balance of power with the Liao dynasty to the north and the Western Xia to the northwest, using annual tribute payments to secure peace.',
    description:
      '自澶渊之盟（1004年）起，北宋与辽朝达成和平协议，宋每年向辽输送岁币。同时，西夏在西北崛起，与宋之间战事不断。三方在11世纪的大部分时间里保持着微妙的平衡关系。',
    descriptionEn:
      'Following the Treaty of Chanyuan (1004), the Song paid annual tribute to the Liao in exchange for peace. Meanwhile, the Western Xia emerged as a military power in the northwest, leading to recurring conflicts. The three powers maintained a tense equilibrium throughout much of the 11th century.',
    sourceIds: ['src-ss'],
    relatedEventIds: [],
  },
  {
    id: 'evt-sushi-lingnan',
    title: '苏轼被贬岭南',
    titleEn: 'Su Shi Exiled to Lingnan',
    startYear: 1094,
    endYear: 1100,
    regionId: 'song-dynasty',
    placeName: '惠州、儋州（今海南）',
    placeNameEn: 'Huizhou and Danzhou (present-day Hainan)',
    personIds: ['su-shi'],
    tags: ['政治事件', '贬谪', '北宋'],
    tagsEn: ['Political Event', 'Exile', 'Northern Song'],
    importance: 3,
    summary: '哲宗亲政后，新党重新上台，苏轼被贬至惠州，后又至海南儋州，在最南端的流放中度过晚年。',
    summaryEn: 'After Emperor Zhezong took personal rule, the reform faction returned to power and exiled Su Shi to Huizhou and then Hainan—the southernmost reaches of the empire.',
    description:
      '绍圣元年（1094年），新党再度执政，已经年近六旬的苏轼被贬到更偏远的惠州（今广东），随后又被贬至海南儋州——当时被视为中原文明的最南端。在海南期间，苏轼办学教书，传播中原文化，为海南的文化发展做出了重要贡献。',
    descriptionEn:
      'In 1094, the reform faction returned to power and banished the nearly 60-year-old Su Shi first to Huizhou (Guangdong) and then to Danzhou on Hainan—the southernmost outpost of Chinese civilization at the time. On Hainan, Su Shi established schools and introduced mainland culture, making a lasting contribution to the island\'s cultural development.',
    sourceIds: ['src-ss'],
    relatedEventIds: ['evt-wutai', 'evt-sushi-huangzhou'],
  },

  // --- European events ---
  {
    id: 'evt-norman-conquest',
    title: '诺曼征服英格兰',
    titleEn: 'Norman Conquest of England',
    startYear: 1066,
    regionId: 'england',
    placeName: '黑斯廷斯（Hastings）',
    placeNameEn: 'Hastings',
    personIds: ['william-conqueror'],
    tags: ['战争', '诺曼征服', '欧洲'],
    tagsEn: ['War', 'Norman Conquest', 'Europe'],
    importance: 5,
    summary: '诺曼底公爵威廉在黑斯廷斯战役中击败英王哈罗德，征服英格兰，建立诺曼王朝。',
    summaryEn: 'Duke William of Normandy defeated King Harold at the Battle of Hastings, conquered England, and established the Norman dynasty.',
    description:
      '1066年，英格兰国王忏悔者爱德华去世，诺曼底公爵威廉声称拥有王位继承权。他率军渡过英吉利海峡，在10月14日的黑斯廷斯战役中击败并杀死英王哈罗德·戈德温森。威廉随后在圣诞节加冕为英格兰国王，开始诺曼征服，将法语和诺曼封建制度引入英格兰。',
    descriptionEn:
      'Following the death of Edward the Confessor in 1066, William of Normandy claimed the English throne. He crossed the Channel and defeated King Harold Godwinson at the Battle of Hastings on October 14. Crowned on Christmas Day, William introduced Norman feudalism and the French language to England.',
    sourceIds: ['src-asc', 'src-domesday'],
    relatedEventIds: ['evt-harrying-north', 'evt-domesday-book'],
  },
  {
    id: 'evt-harrying-north',
    title: '北方劫掠（Harrying of the North）',
    titleEn: 'Harrying of the North',
    startYear: 1069,
    endYear: 1070,
    regionId: 'england',
    personIds: ['william-conqueror'],
    tags: ['战争', '英格兰', '军事'],
    tagsEn: ['War', 'England', 'Military'],
    importance: 4,
    summary: '威廉一世对英格兰北部叛乱进行残酷镇压，大规模毁坏农田和城镇。',
    summaryEn: 'William I brutally suppressed rebellions in northern England, devastating farmland and settlements across Yorkshire and beyond.',
    description:
      '诺曼征服后，英格兰北部爆发多次叛乱。1069至1070年冬季，威廉一世对约克郡及以北地区进行了残酷的军事行动，大规模毁坏农田、牲畜和财产，造成了严重的人道主义灾难。此后英格兰北部长期未能恢复元气。',
    descriptionEn:
      'After the Norman Conquest, northern England rose in repeated rebellion. During the winter of 1069–1070, William I conducted a scorched-earth campaign across Yorkshire and the North, destroying crops, livestock, and property—a humanitarian catastrophe from which the region took decades to recover.',
    sourceIds: ['src-asc', 'src-domesday'],
    relatedEventIds: ['evt-norman-conquest'],
  },
  {
    id: 'evt-domesday-book',
    title: '编撰《末日审判书》',
    titleEn: 'Compilation of the Domesday Book',
    startYear: 1085,
    endYear: 1086,
    regionId: 'england',
    personIds: ['william-conqueror'],
    tags: ['行政', '英格兰', '法律'],
    tagsEn: ['Administration', 'England', 'Law'],
    importance: 4,
    summary: '威廉一世下令全面普查英格兰土地和财产，编成《末日审判书》，是欧洲中世纪最重要的行政记录之一。',
    summaryEn: 'William I ordered a comprehensive survey of English land and property, producing the Domesday Book—one of the most important administrative records of medieval Europe.',
    description:
      '1085年圣诞节，威廉一世下令对英格兰全境进行土地和财产普查。普查官员详细记录了每个庄园的土地、人口、牲畜和价值。这些记录于1086年汇编完成，因其精细程度犹如末日审判一般不可更改，故称《末日审判书》。这是了解中世纪英格兰社会的最重要文献。',
    descriptionEn:
      'At Christmas 1085, William I ordered a nationwide survey. Commissioners recorded every manor\'s land, population, livestock, and value with such detail that the resulting record was called the Domesday Book—so comprehensive it was likened to the Last Judgment, from which no appeal was possible.',
    sourceIds: ['src-domesday'],
    relatedEventIds: ['evt-norman-conquest'],
  },
  {
    id: 'evt-canossa',
    title: '卡诺莎之辱',
    titleEn: 'The Humiliation at Canossa',
    startYear: 1077,
    regionId: 'europe',
    placeName: '卡诺莎城堡（意大利）',
    placeNameEn: 'Canossa Castle, Italy',
    personIds: ['gregory-vii'],
    tags: ['宗教', '政治', '教权与王权', '欧洲'],
    tagsEn: ['Religion', 'Politics', 'Papacy vs Empire', 'Europe'],
    importance: 5,
    summary: '神圣罗马帝国皇帝亨利四世在雪中站立三日，向教皇格里高利七世忏悔，成为教权与王权斗争的象征性事件。',
    summaryEn: 'Holy Roman Emperor Henry IV stood barefoot in the snow for three days, begging Pope Gregory VII for forgiveness—a defining moment in the struggle between papal and imperial authority.',
    description:
      '1076年，教皇格里高利七世因叙任权争议，对神圣罗马帝国皇帝亨利四世宣布绝罚。亨利四世面临国内诸侯的叛变威胁，被迫于1077年1月前往意大利北部的卡诺莎城堡，在雪中赤足站立三日，恳请教皇宽恕。教皇最终撤销了绝罚，这一事件成为中世纪教权凌驾于王权之上的标志性时刻。',
    descriptionEn:
      'In 1076, Pope Gregory VII excommunicated Emperor Henry IV over the investiture controversy. Facing rebellion from his nobles, Henry traveled to Canossa in January 1077 and stood barefoot in the snow for three days, begging absolution. The Pope eventually lifted the excommunication—a moment that came to symbolize papal supremacy over secular rulers.',
    sourceIds: ['src-papal'],
    relatedEventIds: [],
  },
  {
    id: 'evt-anselm-canterbury',
    title: '安瑟伦出任坎特伯雷大主教',
    titleEn: 'Anselm Becomes Archbishop of Canterbury',
    startYear: 1093,
    regionId: 'england',
    personIds: ['anselm'],
    tags: ['宗教', '哲学', '欧洲'],
    tagsEn: ['Religion', 'Philosophy', 'Europe'],
    importance: 4,
    summary: '经院哲学先驱安瑟伦被任命为坎特伯雷大主教，后在叙任权斗争中与英王发生冲突。',
    summaryEn: 'The pioneering Scholastic philosopher Anselm was appointed Archbishop of Canterbury and later clashed with the English king over investiture rights.',
    description:
      '1093年，安瑟伦被任命为坎特伯雷大主教。他坚持教皇对教会事务的最高权威，与英王威廉二世在叙任权问题上发生争执，被迫两次流亡。在此期间，他撰写了《上帝为何化为人》等重要神学著作，奠定了经院哲学的基础。',
    descriptionEn:
      'Appointed Archbishop of Canterbury in 1093, Anselm insisted on papal primacy over church affairs and clashed with King William II over investiture, enduring two periods of exile. During these years he wrote seminal works including "Cur Deus Homo" (Why God Became Man), laying the foundations of Scholastic theology.',
    sourceIds: ['src-papal'],
    relatedEventIds: [],
  },
  {
    id: 'evt-manzikert',
    title: '曼齐刻尔特战役',
    titleEn: 'Battle of Manzikert',
    startYear: 1071,
    regionId: 'byzantine',
    placeName: '曼齐刻尔特（今土耳其东部）',
    placeNameEn: 'Manzikert (present-day eastern Turkey)',
    personIds: ['alexios-komnenos'],
    tags: ['战争', '拜占庭', '塞尔柱', '军事'],
    tagsEn: ['War', 'Byzantium', 'Seljuk', 'Military'],
    importance: 5,
    summary: '拜占庭军队在曼齐刻尔特惨败于塞尔柱突厥人，皇帝罗曼努斯四世被俘，安纳托利亚门户洞开。',
    summaryEn: 'The Byzantine army suffered a catastrophic defeat against the Seljuk Turks at Manzikert; Emperor Romanos IV was captured, opening Anatolia to Turkish settlement.',
    description:
      '1071年8月26日，拜占庭皇帝罗曼努斯四世率领大军与塞尔柱苏丹阿尔普·阿尔斯兰在曼齐刻尔特交战。由于拜占庭军队内部不和及战术失误，拜军惨败，皇帝被俘。此战之后，突厥人大量涌入安纳托利亚，拜占庭永久失去了最主要的兵源地，帝国的衰落不可逆转。',
    descriptionEn:
      'On August 26, 1071, Emperor Romanos IV Diogenes led the Byzantine army against Sultan Alp Arslan near Manzikert. Internal dissension and tactical errors led to a devastating Byzantine defeat and the Emperor\'s capture. Turkish migration into Anatolia followed, and Byzantium permanently lost its main recruiting ground—a turning point in the Empire\'s decline.',
    sourceIds: ['src-alexiad', 'src-byz-empire', 'src-seljuk'],
    relatedEventIds: ['evt-alexios-coronation'],
  },
  {
    id: 'evt-alexios-coronation',
    title: '阿历克塞一世登基与拜占庭中兴',
    titleEn: 'Alexios I\'s Accession and Byzantine Revival',
    startYear: 1081,
    regionId: 'byzantine',
    personIds: ['alexios-komnenos'],
    tags: ['政治', '拜占庭', '科穆宁'],
    tagsEn: ['Politics', 'Byzantium', 'Komnenoi'],
    importance: 4,
    summary: '阿历克塞一世·科穆宁夺取皇位，开启科穆宁王朝，试图挽救衰落的帝国。',
    summaryEn: 'Alexios I Komnenos seized the throne in 1081, founding the Komnenian dynasty and launching an effort to restore the declining Empire.',
    description:
      '1081年4月1日，年轻的将军阿历克塞·科穆宁发动政变，进入君士坦丁堡，推翻尼基弗鲁斯三世。他面临塞尔柱突厥在东方的扩张和诺曼人在西方的入侵。经过二十年的努力，阿历克塞一世稳定了帝国局势。1095年他向教皇乌尔班二世求援，间接引发了第一次十字军东征。',
    descriptionEn:
      'On April 1, 1081, the young general Alexios Komnenos staged a coup, entering Constantinople and overthrowing Nikephoros III. Facing Seljuk expansion in the east and Norman invasions in the west, Alexios spent two decades stabilizing the Empire. His appeal to Pope Urban II in 1095 for military aid helped trigger the First Crusade.',
    sourceIds: ['src-alexiad', 'src-byz-empire'],
    relatedEventIds: ['evt-manzikert'],
  },
  {
    id: 'evt-gregorian-reform',
    title: '格列高利教会改革',
    titleEn: 'Gregorian Reform',
    startYear: 1073,
    endYear: 1085,
    regionId: 'europe',
    personIds: ['gregory-vii'],
    tags: ['宗教', '改革', '欧洲'],
    tagsEn: ['Religion', 'Reform', 'Europe'],
    importance: 4,
    summary: '格里高利七世推行全面教会改革，反对世俗势力干预教会事务，禁止神职人员结婚和买卖圣职。',
    summaryEn: 'Pope Gregory VII launched sweeping Church reforms, opposing lay interference in church affairs, prohibiting clerical marriage, and banning simony.',
    description:
      '1073年希尔德布兰德当选教皇（格里高利七世）后，大力推行教会改革。他发布《教皇训令》，宣称教皇拥有至高无上的权威，有权废黜皇帝。改革包括禁止圣职买卖（辛摩尼）、强制神职人员独身，以及与世俗君主争夺主教任命权。这些改革深刻改变了中世纪欧洲的政教关系。',
    descriptionEn:
      'Elected pope in 1073, Hildebrand—as Gregory VII—promulgated the Dictatus Papae, asserting papal supremacy and the right to depose emperors. His reforms targeted simony, mandated clerical celibacy, and challenged lay rulers over bishop appointments, reshaping medieval church-state relations.',
    sourceIds: ['src-papal'],
    relatedEventIds: ['evt-canossa'],
  },

  // --- Middle East events ---
  {
    id: 'evt-seljuk-rise',
    title: '塞尔柱帝国崛起',
    titleEn: 'Rise of the Seljuk Empire',
    startYear: 1037,
    endYear: 1092,
    regionId: 'seljuk',
    personIds: [],
    tags: ['政治', '军事', '伊斯兰'],
    tagsEn: ['Politics', 'Military', 'Islam'],
    importance: 5,
    summary: '塞尔柱突厥人从草原崛起，建立横跨中亚至安纳托利亚的大帝国。',
    summaryEn: 'The Seljuk Turks rose from the steppes to build a vast empire stretching from Central Asia to Anatolia.',
    description:
      '塞尔柱帝国在首领图格里勒·贝格率领下于1037年建立，1055年进入巴格达，被阿拔斯哈里发授予"苏丹"称号。在阿尔普·阿尔斯兰（1063-1072年在位）和马利克沙（1072-1092年在位）时期达到鼎盛，领土从河中地区延伸到地中海东岸。',
    descriptionEn:
      'Founded in 1037 under Tughril Beg, the Seljuk Empire entered Baghdad in 1055 and received the title of "Sultan" from the Abbasid Caliph. Under Alp Arslan (1063–1072) and Malik Shah (1072–1092), the empire reached its peak, extending from Transoxiana to the eastern Mediterranean coast.',
    sourceIds: ['src-seljuk'],
    relatedEventIds: ['evt-manzikert'],
  },
  {
    id: 'evt-baghdad-1055',
    title: '塞尔柱人进入巴格达',
    titleEn: 'Seljuks Enter Baghdad',
    startYear: 1055,
    regionId: 'seljuk',
    placeName: '巴格达',
    placeNameEn: 'Baghdad',
    personIds: [],
    tags: ['政治', '伊斯兰', '塞尔柱'],
    tagsEn: ['Politics', 'Islam', 'Seljuk'],
    importance: 4,
    summary: '图格里勒·贝格率塞尔柱军队进入巴格达，阿拔斯哈里发被迫授予其"苏丹"称号。',
    summaryEn: 'Tughril Beg led the Seljuk army into Baghdad; the Abbasid Caliph was compelled to grant him the title of "Sultan."',
    description:
      '1055年，塞尔柱首领图格里勒·贝格受阿拔斯哈里发请求，率军进入巴格达，驱逐了什叶派的布韦希王朝势力。哈里发卡伊姆正式授予图格里勒"苏丹"（东、西方之王）称号，塞尔柱人由此成为伊斯兰世界的实际统治者。',
    descriptionEn:
      'In 1055, Tughril Beg entered Baghdad at the request of the Abbasid Caliph and expelled the Shi\'a Buyid dynasty. Caliph al-Qa\'im formally granted him the title of "Sultan" (Sultan of East and West), making the Seljuks the de facto rulers of the Islamic world.',
    sourceIds: ['src-seljuk'],
    relatedEventIds: ['evt-seljuk-rise'],
  },
  {
    id: 'evt-nizamiyya',
    title: '建立尼扎米亚经学院',
    titleEn: 'Founding of the Nizamiyya Madrasa',
    startYear: 1065,
    endYear: 1067,
    regionId: 'seljuk',
    placeName: '巴格达',
    placeNameEn: 'Baghdad',
    personIds: [],
    tags: ['教育', '伊斯兰', '文化'],
    tagsEn: ['Education', 'Islam', 'Culture'],
    importance: 4,
    summary: '塞尔柱名相尼扎姆·穆尔克在巴格达创立尼扎米亚经学院，成为伊斯兰世界最重要的学术机构之一。',
    summaryEn: 'The Seljuk vizier Nizam al-Mulk founded the Nizamiyya Madrasa in Baghdad, which became one of the most important scholarly institutions in the Islamic world.',
    description:
      '尼扎姆·穆尔克是塞尔柱帝国的著名宰相，他于1065至1067年在巴格达建立了尼扎米亚经学院。学院教授伊斯兰法学、神学、哲学和科学，成为后来欧洲大学的范本之一。著名学者安萨里曾在此讲学。',
    descriptionEn:
      'Nizam al-Mulk, the celebrated Seljuk vizier, established the Nizamiyya Madrasa in Baghdad between 1065 and 1067. Teaching Islamic jurisprudence, theology, philosophy, and science, it served as a model for later European universities. The renowned scholar Al-Ghazali lectured here.',
    sourceIds: ['src-seljuk'],
    relatedEventIds: ['evt-seljuk-rise'],
  },
  {
    id: 'evt-fatimid-decline',
    title: '法蒂玛王朝衰落与十字军前夜的近东',
    titleEn: 'Decline of the Fatimid Caliphate and the Near East on the Eve of the Crusades',
    startYear: 1073,
    endYear: 1099,
    regionId: 'middle-east',
    personIds: [],
    tags: ['政治', '伊斯兰', '法蒂玛'],
    tagsEn: ['Politics', 'Islam', 'Fatimid'],
    importance: 3,
    summary: '埃及法蒂玛王朝在内乱和塞尔柱人的威胁下持续衰落，近东政治格局剧烈变动。',
    summaryEn: 'The Fatimid Caliphate in Egypt steadily declined amid internal strife and Seljuk pressure, reshaping the political landscape of the Near East.',
    description:
      '11世纪后期，什叶派的法蒂玛王朝在埃及的统治日趋衰弱。塞尔柱帝国从东方不断施压，从法蒂玛手中夺取了叙利亚和巴勒斯坦的大部分地区。这种权力真空为后来十字军的到来创造了条件。',
    descriptionEn:
      'In the late 11th century, the Shi\'a Fatimid Caliphate in Egypt weakened considerably. The Seljuk Empire pressed from the east, seizing most of Syria and Palestine. The resulting power vacuum created the conditions for the Crusaders\' arrival.',
    sourceIds: ['src-seljuk'],
    relatedEventIds: ['evt-seljuk-rise'],
  },

  // --- Japanese events ---
  {
    id: 'evt-genji-monogatari',
    title: '《源氏物语》问世',
    titleEn: '"The Tale of Genji" is Written',
    startYear: 1008,
    endYear: 1010,
    regionId: 'japan',
    personIds: ['murasaki-shikibu'],
    tags: ['文学', '平安时代', '日本'],
    tagsEn: ['Literature', 'Heian Period', 'Japan'],
    importance: 5,
    summary: '紫式部创作《源氏物语》，被广泛认为是世界上最早的长篇小说之一。',
    summaryEn: 'Murasaki Shikibu wrote "The Tale of Genji," widely regarded as one of the world\'s earliest novels.',
    description:
      '平安时代中期，女作家紫式部创作了《源氏物语》，共54帖，以光源氏的爱情和生活为主线，描绘了平安贵族社会的全貌。这部作品以其深刻的心理描写和精致的文学技巧，被认为是日本文学的巅峰之作，也是世界文学史上最早的长篇小说。',
    descriptionEn:
      'Lady Murasaki Shikibu, a Heian court lady, wrote "The Tale of Genji" in 54 chapters, following the life and loves of the shining Prince Genji. With its psychological depth and literary sophistication, it is considered both the pinnacle of Japanese literature and one of the world\'s earliest novels.',
    sourceIds: ['src-eiga'],
    relatedEventIds: [],
  },
  {
    id: 'evt-michinaga-peak',
    title: '藤原道长全盛期',
    titleEn: 'Fujiwara no Michinaga\'s Zenith',
    startYear: 996,
    endYear: 1028,
    regionId: 'japan',
    personIds: ['fujiwara-michinaga'],
    tags: ['政治', '贵族', '平安时代'],
    tagsEn: ['Politics', 'Aristocracy', 'Heian Period'],
    importance: 5,
    summary: '藤原道长作为摄关政治的代表人物达到权力巅峰，三个女儿先后成为皇后。',
    summaryEn: 'Fujiwara no Michinaga, the supreme figure of regency politics, reached the pinnacle of power; three of his daughters became empresses.',
    description:
      '藤原道长是平安时代摄关政治的顶峰。他通过将自己的女儿们嫁入皇室，使得三个女儿彰子、妍子、威子分别成为一条天皇、三条天皇后和后来天皇的皇后。他的时代被称为"藤原氏最盛期"，他本人也留下了"此世即吾世，如月满无缺"的著名和歌。',
    descriptionEn:
      'Fujiwara no Michinaga represented the apex of Heian regency rule. By marrying his daughters Shoshi, Kenshi, and Ishi into the imperial family, each became empress to successive emperors. This era was called the Fujiwara zenith, and he famously composed the verse: "This world is my world; like the full moon, I lack nothing."',
    sourceIds: ['src-eiga'],
    relatedEventIds: [],
  },
  {
    id: 'evt-tale-of-flourishing-fortune',
    title: '《荣花物语》编纂',
    titleEn: 'Compilation of "Eiga Monogatari"',
    startYear: 1028,
    endYear: 1030,
    regionId: 'japan',
    personIds: ['fujiwara-michinaga'],
    tags: ['文学', '历史', '平安时代'],
    tagsEn: ['Literature', 'History', 'Heian Period'],
    importance: 3,
    summary: '《荣花物语》开始编纂，记录藤原道长时代的繁荣景象。',
    summaryEn: '"A Tale of Flowering Fortunes" (Eiga Monogatari) was compiled, recording the glory of Fujiwara no Michinaga\'s era.',
    description:
      '《荣花物语》是一部记录平安时代历史的物语文学作品，主要描写了从宇多天皇到堀河天皇约200年的历史，尤其以藤原道长的全盛时代为重点。作品以华丽的笔触赞美了藤原氏的荣华，为后世留下了珍贵的平安时代社会记录。',
    descriptionEn:
      '"Eiga Monogatari" is a historical tale covering roughly 200 years of Heian history, from Emperor Uda to Emperor Horikawa, with special focus on Fujiwara no Michinaga\'s zenith. Its vivid prose celebrates Fujiwara splendor and preserves a valuable record of Heian court society.',
    sourceIds: ['src-eiga'],
    relatedEventIds: ['evt-michinaga-peak'],
  },

  // --- Indian events ---
  {
    id: 'evt-chola-expedition',
    title: '朱罗王朝海上远征',
    titleEn: 'Chola Naval Expedition',
    startYear: 1025,
    regionId: 'india',
    personIds: [],
    tags: ['军事', '贸易', '南印度'],
    tagsEn: ['Military', 'Trade', 'South India'],
    importance: 4,
    summary: '朱罗王朝国王拉金德拉一世发动大规模海上远征，征服三佛齐（今印尼苏门答腊），控制印度洋贸易。',
    summaryEn: 'King Rajendra I of the Chola dynasty launched a major naval expedition, conquering Srivijaya (present-day Sumatra) and asserting control over Indian Ocean trade.',
    description:
      '1025年，南印度朱罗王朝的拉金德拉一世（Rajendra I）发动了大规模的海上远征，跨越孟加拉湾，征服了东南亚的三佛齐王国（Srivijaya，位于今苏门答腊）。此举使朱罗王朝成为印度洋上的海上霸权，控制了中国与中东之间的重要贸易路线。',
    descriptionEn:
      'In 1025, Rajendra I of the Chola dynasty launched a massive naval expedition across the Bay of Bengal, conquering the Srivijaya kingdom in Sumatra. This established Chola naval supremacy in the Indian Ocean and control over the vital trade routes between China and the Middle East.',
    sourceIds: ['src-chola'],
    relatedEventIds: [],
  },
  {
    id: 'evt-chola-temple',
    title: '朱罗王朝大庙建造',
    titleEn: 'Construction of Chola Great Temple',
    startYear: 1010,
    endYear: 1030,
    regionId: 'india',
    personIds: [],
    tags: ['建筑', '宗教', '艺术', '南印度'],
    tagsEn: ['Architecture', 'Religion', 'Art', 'South India'],
    importance: 4,
    summary: '朱罗王朝修建宏伟的布里哈迪希瓦拉神庙，体现南印度达罗毗荼建筑艺术的巅峰。',
    summaryEn: 'The Chola dynasty built the magnificent Brihadeeswarar Temple, representing the apex of Dravidian architecture.',
    description:
      '拉贾拉贾一世于1010年在坦贾武尔（Thanjavur）建成布里哈迪希瓦拉神庙（Brihadeeswarar Temple），其高耸的维马纳塔楼高达66米，是当时世界上最高的建筑之一。这座印度教湿婆神庙是朱罗王朝建筑艺术的巅峰之作，于1987年被列为世界文化遗产。',
    descriptionEn:
      'Rajaraja I completed the Brihadeeswarar Temple in Thanjavur in 1010. Its soaring vimana tower reaches 66 meters, making it one of the tallest structures of its time. This Hindu Shiva temple, the crowning achievement of Chola architecture, was designated a UNESCO World Heritage site in 1987.',
    sourceIds: ['src-chola'],
    relatedEventIds: ['evt-chola-expedition'],
  },
  {
    id: 'evt-pala-university',
    title: '波罗王朝佛教大学繁荣',
    titleEn: 'Pala Dynasty Buddhist Universities Flourish',
    startYear: 1000,
    endYear: 1100,
    regionId: 'india',
    personIds: [],
    tags: ['教育', '宗教', '佛教', '文化'],
    tagsEn: ['Education', 'Religion', 'Buddhism', 'Culture'],
    importance: 3,
    summary: '东印度波罗王朝的佛教大学（如超戒寺、那烂陀寺）在11世纪继续繁荣，吸引来自亚洲各地的学者。',
    summaryEn: 'The Buddhist universities of the Pala dynasty in eastern India (Vikramashila, Nalanda) flourished in the 11th century, attracting scholars from across Asia.',
    description:
      '11世纪，帕拉王朝（波罗王朝）统治下的东印度佛教大学，如超戒寺（Vikramashila）和那烂陀寺（Nalanda），仍然是亚洲最重要的学术中心。来自中国（包括西藏）、东南亚和中亚的僧侣和学者在此研习佛学、哲学、逻辑学和医学。',
    descriptionEn:
      'In the 11th century, the Buddhist universities of eastern India under Pala patronage—Vikramashila and Nalanda foremost among them—remained Asia\'s premier centers of learning. Monks and scholars from China (including Tibet), Southeast Asia, and Central Asia gathered here to study Buddhism, philosophy, logic, and medicine.',
    sourceIds: ['src-chola'],
    relatedEventIds: [],
  },
  {
    id: 'evt-ghaznavid-invasion',
    title: '加兹尼王朝入侵北印度',
    titleEn: 'Ghaznavid Invasions of Northern India',
    startYear: 1001,
    endYear: 1030,
    regionId: 'india',
    personIds: [],
    tags: ['战争', '伊斯兰', '北印度'],
    tagsEn: ['War', 'Islam', 'North India'],
    importance: 4,
    summary: '突厥将领马哈茂德·加兹尼多次入侵北印度，掠夺索姆纳特神庙，伊斯兰势力首次深入印度腹地。',
    summaryEn: 'The Turkic general Mahmud of Ghazni repeatedly invaded northern India, sacking the Somnath temple—the first deep Islamic incursion into the Indian heartland.',
    description:
      '公元1001年至1030年间，阿富汗加兹尼王朝的统治者马哈茂德（Mahmud of Ghazni）对北印度发动了多达17次入侵。1026年，他洗劫了古吉拉特的印度教圣地索姆纳特神庙。这些入侵虽然主要是掠夺性的，但为后来穆斯林势力在印度建立持久统治铺平了道路。',
    descriptionEn:
      'Between 1001 and 1030, Mahmud of Ghazni launched 17 invasions of northern India. In 1026, he sacked the Somnath temple in Gujarat, a revered Hindu pilgrimage site. Although primarily plundering expeditions, these campaigns paved the way for lasting Muslim rule in India.',
    sourceIds: ['src-seljuk'],
    relatedEventIds: [],
  },

  // --- Additional events ---
  {
    id: 'evt-venice-rise',
    title: '威尼斯共和国崛起',
    titleEn: 'Rise of the Venetian Republic',
    startYear: 1082,
    regionId: 'europe',
    placeName: '威尼斯',
    placeNameEn: 'Venice',
    personIds: [],
    tags: ['贸易', '政治', '欧洲'],
    tagsEn: ['Trade', 'Politics', 'Europe'],
    importance: 3,
    summary: '拜占庭皇帝阿历克塞一世授予威尼斯广泛贸易特权，威尼斯开始成为地中海的商业霸主。',
    summaryEn: 'Emperor Alexios I granted extensive trade privileges to Venice, launching the city\'s rise as the commercial powerhouse of the Mediterranean.',
    description:
      '1082年，为换取威尼斯的海军支持以对抗诺曼人，阿历克塞一世授予威尼斯商人在拜占庭帝国境内免关税的贸易特权。这一金玺诏书成为威尼斯海上商业帝国的起点，威尼斯逐渐控制了东地中海的贸易。',
    descriptionEn:
      'In 1082, in exchange for naval support against the Normans, Alexios I issued a Golden Bull granting Venetian merchants duty-free trade throughout the Byzantine Empire. This charter became the foundation of Venice\'s maritime commercial empire and its eventual domination of eastern Mediterranean trade.',
    sourceIds: ['src-alexiad', 'src-byz-empire'],
    relatedEventIds: ['evt-alexios-coronation'],
  },
  {
    id: 'evt-first-crusade-call',
    title: '克莱芒会议——第一次十字军东征的号召',
    titleEn: 'Council of Clermont — Call for the First Crusade',
    startYear: 1095,
    regionId: 'europe',
    placeName: '克莱芒（法国）',
    placeNameEn: 'Clermont, France',
    personIds: [],
    tags: ['宗教', '战争', '十字军'],
    tagsEn: ['Religion', 'War', 'Crusades'],
    importance: 5,
    summary: '教皇乌尔班二世在克莱芒会议上号召基督徒夺回圣地，引发第一次十字军东征。',
    summaryEn: 'Pope Urban II at the Council of Clermont called on Christians to reclaim the Holy Land, launching the First Crusade.',
    description:
      '1095年11月，教皇乌尔班二世在法国克莱芒召开宗教会议，回应拜占庭皇帝阿历克塞一世对抗塞尔柱突厥的求援。他以夺回耶路撒冷圣墓为号召，发表激昂演说，呼吁西欧基督徒组织十字军前往东方。这一号召引发了持续近两百年的十字军运动。',
    descriptionEn:
      'In November 1095, Pope Urban II convened a council at Clermont. Responding to Emperor Alexios I\'s appeal for aid against the Seljuks, he delivered a rousing sermon calling for Western Christians to liberate Jerusalem. The response launched the crusading movement that would convulse the Mediterranean world for nearly two centuries.',
    sourceIds: ['src-papal', 'src-byz-empire'],
    relatedEventIds: ['evt-alexios-coronation', 'evt-manzikert'],
  },
  {
    id: 'evt-song-science',
    title: '北宋科技发明高峰',
    titleEn: 'Northern Song Technological Peak',
    startYear: 1041,
    endYear: 1088,
    regionId: 'song-dynasty',
    personIds: [],
    tags: ['科技', '文化', '北宋', '发明'],
    tagsEn: ['Technology', 'Culture', 'Northern Song', 'Invention'],
    importance: 3,
    summary: '11世纪北宋在科技上取得重大突破，毕昇发明活字印刷，沈括著《梦溪笔谈》。',
    summaryEn: 'The 11th century saw major technological breakthroughs in the Northern Song, including Bi Sheng\'s movable-type printing and Shen Kuo\'s "Dream Pool Essays."',
    description:
      '1041至1048年间，毕昇发明了活字印刷术，被视为世界印刷技术史上的重大突破。沈括（1031-1095）的《梦溪笔谈》记录了大量科学技术知识，包括首次记载磁偏角现象。这反映了北宋高度发达的科技文明。',
    descriptionEn:
      'Between 1041 and 1048, Bi Sheng invented movable-type printing, a landmark in the history of communications. Shen Kuo (1031–1095) wrote "Dream Pool Essays" (Mengxi Bitan), compiling extensive scientific and technical knowledge—including the first recorded observation of magnetic declination.',
    sourceIds: ['src-ss'],
    relatedEventIds: [],
  },
];

// ==================== HELPERS ====================

/** Get a person by ID */
export function getPersonById(id: string): Person | undefined {
  return people.find((p) => p.id === id);
}

/** Get a region by ID */
export function getRegionById(id: string): Region | undefined {
  return regions.find((r) => r.id === id);
}

/** Get an event by ID */
export function getEventById(id: string): HistoricalEvent | undefined {
  return events.find((e) => e.id === id);
}

/** Get a source by ID */
export function getSourceById(id: string): Source | undefined {
  return sources.find((s) => s.id === id);
}

/** Get sub-regions for a given region */
export function getSubRegions(regionId: string): Region[] {
  return regions.filter((r) => r.parentRegionId === regionId);
}

/** Get events for a person */
export function getEventsForPerson(personId: string): HistoricalEvent[] {
  return events.filter((e) => e.personIds.includes(personId));
}

/** Get persons for an event */
export function getPersonsForEvent(eventId: string): Person[] {
  const event = getEventById(eventId);
  if (!event) return [];
  return event.personIds
    .map((pid) => getPersonById(pid))
    .filter((p): p is Person => p !== undefined);
}

/** Get events by region */
export function getEventsByRegion(regionId: string): HistoricalEvent[] {
  return events.filter((e) => e.regionId === regionId);
}

/** Get all unique tags across people and events */
export function getAllTags(): string[] {
  const tagSet = new Set<string>();
  people.forEach((p) => p.tags.forEach((t) => tagSet.add(t)));
  events.forEach((e) => e.tags.forEach((t) => tagSet.add(t)));
  return Array.from(tagSet).sort();
}

/** Get sources linked to an event */
export function getSourcesForEvent(eventId: string): Source[] {
  const event = getEventById(eventId);
  if (!event) return [];
  return event.sourceIds
    .map((sid) => getSourceById(sid))
    .filter((s): s is Source => s !== undefined);
}
