/** All UI text keys used in the application */
export interface Dictionary {
  // App shell
  app: {
    title: string;
    subtitle: string;
    footer: string;
  };

  // Navigation
  nav: {
    home: string;
    aboutData: string;
    backToHome: string;
    relationships: string;
    civilizations: string;
  };

  // Home page
  home: {
    heroTitle: string;
    heroSubtitle: string;
    searchPlaceholder: string;
    exampleTitle: string;
    exploreByPerson: string;
    exploreByPersonDesc: string;
    exploreByYear: string;
    exploreByYearDesc: string;
    exploreByRegion: string;
    exploreByRegionDesc: string;
    exploreRelationships: string;
    exploreRelationshipsDesc: string;
    exploreCivilizations: string;
    exploreCivilizationsDesc: string;
  };

  // Search page
  search: {
    title: string;
    subtitle: string;
    subtitleWithQuery: string;
    noQueryTitle: string;
    noQueryDesc: string;
    noResults: string;
    noResultsDesc: string;
    sectionPeople: string;
    sectionEvents: string;
    sectionRegions: string;
    sectionYears: string;
    viewParallel: string;
    moreEvents: string;
    searchPlaceholder: string;
  };

  // Person page
  person: {
    timeline: string;
    noEvents: string;
    noEventsDesc: string;
    viewParallel: string;
  };

  // Event page
  event: {
    eventInfo: string;
    time: string;
    location: string;
    region: string;
    importance: string;
    relatedPeople: string;
    viewParallel: string;
    relatedEventsTitle: string;
  };

  // Parallel page
  parallel: {
    timeRange: string;
    eventsCount: string;
    noData: string;
    noDataDesc: string;
    viewModeCard: string;
    viewModeTimeline: string;
  };

  // About page
  about: {
    title: string;
    subtitle: string;
    dataSources: string;
    dataSourcesText: string;
    dataSourcesText2: string;
    dataStructure: string;
    itemRegion: string;
    itemPerson: string;
    itemEvent: string;
    itemSource: string;
    license: string;
    licenseCode: string;
    licenseCodeDesc: string;
    licenseData: string;
    licenseDataDesc: string;
    licenseBrand: string;
    licenseBrandDesc: string;
    coverage: string;
    coverageDesc: string;
    coverageItems: string[];
    roadmap: string;
    roadmapItems: string[];
  };

  // Common
  common: {
    notFound: string;
    notFoundDesc: string;
    backToHome: string;
    loading: string;
    source: string;
    yearsAround: string;
  };
}

export const zh: Dictionary = {
  app: {
    title: '历史平行线',
    subtitle: '在同一时间，看见世界不同角落的历史现场',
    footer: '历史平行线 · 代码 Apache-2.0 许可 · 历史数据 CC BY-SA 4.0',
  },
  nav: {
    home: '历史平行线',
    aboutData: '数据说明',
    backToHome: '首页',
    relationships: '人物关系',
    civilizations: '文明时间轴',
  },
  home: {
    heroTitle: '历史平行线',
    heroSubtitle: '在同一时间，看见世界不同角落的历史现场',
    searchPlaceholder: '搜索人物、事件、地点、年份…',
    exampleTitle: '示例探索',
    exploreByPerson: '按人物探索',
    exploreByPersonDesc: '从历史人物的视角看世界',
    exploreByYear: '按年份探索',
    exploreByYearDesc: '选择一个时间点看世界',
    exploreByRegion: '按地区探索',
    exploreByRegionDesc: '浏览全球各文明的时间线',
    exploreRelationships: '人物关系图',
    exploreRelationshipsDesc: '探索历史人物之间的关联',
    exploreCivilizations: '文明时间轴',
    exploreCivilizationsDesc: '各大文明的横向时间对比',
  },
  search: {
    title: '搜索',
    subtitle: '请输入关键词搜索历史人物、事件、地点或年份',
    subtitleWithQuery: '"{query}" 的搜索结果',
    noQueryTitle: '输入关键词开始探索',
    noQueryDesc: '支持搜索人物名、事件名、地名或年份',
    noResults: '未找到与 "{query}" 相关的结果',
    noResultsDesc: '请尝试其他关键词，或检查拼写',
    sectionPeople: '人物',
    sectionEvents: '历史事件',
    sectionRegions: '地区/文明',
    sectionYears: '年份',
    viewParallel: '查看平行时间 →',
    moreEvents: '还有 {count} 个相关事件……',
    searchPlaceholder: '搜索人物、事件、地点、年份…',
  },
  person: {
    timeline: '生命时间轴',
    noEvents: '暂无时间线事件',
    noEventsDesc: '该人物的历史事件正在整理中',
    viewParallel: '同时期世界 →',
  },
  event: {
    eventInfo: '事件信息',
    time: '时间',
    location: '地点',
    region: '地区/文明',
    importance: '重要性',
    relatedPeople: '相关人物',
    viewParallel: '查看同一时期的世界 →',
    relatedEventsTitle: '同一地区同时期事件',
  },
  parallel: {
    timeRange: '时间范围',
    eventsCount: '共匹配 {events} 个历史事件，覆盖 {regions} 个地区',
    noData: '该时间范围内暂无数据',
    noDataDesc: '请调整时间范围或选择其他年份',
    viewModeCard: '卡片视图',
    viewModeTimeline: '时间带视图',
  },
  about: {
    title: '数据说明',
    subtitle: '关于历史平行线项目的数据结构、来源原则与授权方式',
    dataSources: '数据来源原则',
    dataSourcesText: '本项目的 mock 数据目前基于公开的历史文献和现代学术研究整理而成。每个事件和人物都标注了来源引用，方便用户追溯原始资料。',
    dataSourcesText2: '未来接入真实数据库后，每条数据将包含更完整的元数据，包括：引用出处、出处页码、可靠度评级、贡献者信息等。',
    dataStructure: '数据结构',
    itemRegion: 'Region（地区/文明）：包含名称、描述、层级关系（父-子地区）。',
    itemPerson: 'Person（人物）：包含姓名、别名、生卒年、所属地区、标签、简介和来源。',
    itemEvent: 'HistoricalEvent（历史事件）：包含标题、起止年份、地区、地点、相关人物、重要性（1-5级）、简介、详细描述、来源和关联事件。',
    itemSource: 'Source（来源）：包含标题、作者、出版信息、年份、许可方式。',
    license: '授权方式',
    licenseCode: '代码',
    licenseCodeDesc: 'Apache License 2.0 — 自由使用、修改和分发，需保留版权声明。',
    licenseData: '历史数据、时间线与事件描述',
    licenseDataDesc: 'CC BY-SA 4.0（署名-相同方式共享）— 可以自由分享和改编，但需署名原作者并以相同方式共享。',
    licenseBrand: '项目名称、Logo 和品牌视觉',
    licenseBrandDesc: '不包含在开源授权中。未经许可不得将项目名称「历史平行线」及其品牌视觉资产用于衍生项目。',
    coverage: '当前 Mock 数据覆盖',
    coverageDesc: 'MVP 阶段的 mock 数据主要覆盖 11 世纪（约公元 960-1127 年），聚焦北宋时期的中国与同时代的世界：',
    coverageItems: [
      '北宋中国：苏轼、王安石、司马光、欧阳修等人物及相关事件',
      '欧洲：诺曼征服、卡诺莎之辱、教会改革、英格兰《末日审判书》',
      '拜占庭帝国：曼齐刻尔特战役、科穆宁王朝崛起',
      '中东/伊斯兰世界：塞尔柱帝国崛起、尼扎米亚经学院建立',
      '日本：平安时代、紫式部《源氏物语》、藤原道长摄关政治',
      '印度：朱罗王朝海上扩张、加兹尼王朝入侵',
    ],
    roadmap: '未来路线图',
    roadmapItems: [
      '接入 Supabase / PostgreSQL 数据库，支持数据增删改查。',
      '扩展时间覆盖：从 11 世纪扩展到更多历史时期。',
      '增加更多地区：非洲、美洲、东南亚等。',
      '添加可视化时间轴和地图视图。',
      '支持用户贡献和社区维护历史数据。',
      '实现多语言支持（中/英/日等）。',
    ],
  },
  common: {
    notFound: '页面不存在',
    notFoundDesc: '你访问的页面可能已被移动、删除，或从未存在过。',
    backToHome: '返回首页',
    loading: '加载中…',
    source: '来源',
    yearsAround: '{year}年前后的事件',
  },
};
