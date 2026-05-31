# 历史平行线 (History Parallel)

> 在同一时间，看见世界不同角落的历史现场。

**历史平行线** 是一个历史时空对照 WebApp。用户可以选择历史上的某个时间点、历史人物、地区或事件，然后看到同一时间段内，全球不同地区、不同文明、不同历史人物身上正在发生什么事。

## 快速开始

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 打开浏览器
# http://localhost:3000
```

## 技术栈

- **Framework:** Next.js (App Router)
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **Icons:** lucide-react
- **State:** React state (MVP)

## 项目结构

```
src/
  app/                    # Next.js App Router 页面
    page.tsx              # 首页
    search/page.tsx       # 搜索页
    people/[id]/page.tsx  # 人物详情页
    events/[id]/page.tsx  # 事件详情页
    parallel/page.tsx     # 平行时间页（核心）
    about-data/page.tsx   # 数据说明页
  components/
    common/               # 通用组件（SearchBox, Tag, EmptyState 等）
    cards/                # 卡片组件（PersonCard, EventCard 等）
    timeline/             # 时间轴组件
    parallel/             # 平行视图组件
  data/
    mockData.ts           # Mock 数据（MVP 阶段）
  lib/
    types.ts              # 类型定义
    date.ts               # 日期工具
    slug.ts               # Slug 工具
    search.ts             # 搜索逻辑
    parallel.ts           # 平行事件算法
```

## 核心功能

- **首页**: 搜索入口 + 示例探索 + 按人物/年份/地区浏览
- **搜索**: 支持人物名、事件名、地区、年份搜索，结果分组展示
- **人物页**: 人物信息 + 生命时间轴 + 同时期世界跳转
- **平行时间页**: 核心页面，展示全球各地区同时期历史事件
- **事件详情页**: 事件详情 + 来源引用 + 相关人物
- **数据说明页**: 数据结构、来源原则、授权方式

## 当前数据覆盖

MVP 阶段 mock 数据主要覆盖 **11 世纪**（约 960-1127 年），包括：

| 地区 | 内容 |
|------|------|
| 北宋中国 | 苏轼、王安石、司马光、欧阳修；乌台诗案、熙宁变法等 |
| 欧洲 | 诺曼征服、卡诺莎之辱、教会改革、末日审判书 |
| 拜占庭 | 曼齐刻尔特战役、科穆宁王朝 |
| 中东 | 塞尔柱帝国崛起、尼扎米亚经学院 |
| 日本 | 紫式部、藤原道长、源氏物语 |
| 印度 | 朱罗王朝、加兹尼入侵 |

## 授权

| 类型 | 许可证 |
|------|--------|
| **代码** | [Apache License 2.0](LICENSE) |
| **历史数据、时间线与事件描述** | [CC BY-SA 4.0](LICENSE-CONTENT.md) |
| **项目名称、Logo 和品牌视觉** | 保留所有权利（不包含在开源授权中） |

详见 [NOTICE](NOTICE.md)。

## 下一步路线图

1. 接入 Supabase / PostgreSQL，支持数据增删改查
2. 扩展时间覆盖（更多历史时期）
3. 增加地区覆盖（非洲、美洲、东南亚等）
4. 可视化时间轴和地图视图
5. 用户贡献和社区维护机制
6. 多语言支持

## 开发

```bash
# 类型检查
npx tsc --noEmit

# Lint
npm run lint

# 构建
npm run build
```

## 贡献

欢迎提交 Issue 和 Pull Request。在提交 PR 前请确保：
- 代码通过 typecheck 和 lint
- 新增数据包含来源引用
- 遵循项目现有的代码风格
