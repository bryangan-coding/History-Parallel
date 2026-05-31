# History Parallel &middot; 历史平行线

> See what was happening around the world at the same moment in history.
>
> 在同一时间，看见世界不同角落的历史现场。

**History Parallel** is a web app for comparing historical timelines across civilizations. Pick a point in time, a historical figure, a region, or an event — and see what was unfolding simultaneously across different parts of the globe.

---

**历史平行线** 是一个历史时空对照 WebApp。选择一个历史时间点、人物、地区或事件，即可看到同一时段内，全球不同文明、不同地区正在发生什么事。

---

## Quick Start / 快速开始

```bash
npm install
npm run dev
# Open http://localhost:3000
```

## Tech Stack / 技术栈

| Layer | Choice |
|-------|--------|
| Framework | Next.js (App Router) |
| Language | TypeScript |
| Styling | Tailwind CSS v4 |
| Icons | lucide-react |
| State | React state (MVP) |
| Database | Mock data → Supabase (planned) |

## Project Structure / 项目结构

```
src/
  app/                    # Pages
    page.tsx              # Home
    search/page.tsx       # Search
    people/[id]/page.tsx  # Person detail
    events/[id]/page.tsx  # Event detail
    parallel/page.tsx     # Parallel timeline (core)
    about-data/page.tsx   # Data notes
  components/
    common/               # SearchBox, Tag, EmptyState, PageHeader
    cards/                # PersonCard, EventCard, ExamplePromptCard, SourceList
    timeline/             # Timeline, TimelineItem
    parallel/             # ParallelTimelineView, TimelineTrack, EventPreviewPanel
  data/
    mockData.ts           # Mock data (MVP)
  lib/
    types.ts              # Type definitions
    date.ts               # Date utilities
    slug.ts               # Slug utilities
    search.ts             # Search algorithm
    parallel.ts           # Parallel event algorithm
    dataProvider.ts       # Data provider abstraction
  i18n/
    dictionaries/         # zh.ts, en.ts
    LocaleProvider.tsx    # i18n context
```

## Core Features / 核心功能

- **Home**: Search entry + example prompts + browse by person / year / region
- **Search**: Find people, events, regions, and years with grouped results
- **Person Page**: Bio + life timeline + "explore the world at this time" link
- **Parallel Timeline** (core): Side-by-side comparison of events across regions, with card view and horizontal timeline view
- **Event Detail**: Event description + source citations + related people
- **Data Notes**: Data structure, sourcing principles, licensing
- **i18n**: Full Chinese / English language switch, with manually verified translations for all historical names and facts

## Data Coverage / 当前数据覆盖

MVP covers the **11th century** (~960–1127 CE), including:

| Region / 地区 | Content / 内容 |
|---------------|----------------|
| Northern Song China | Su Shi, Wang Anshi, Sima Guang, Ouyang Xiu; Crow Terrace Poetry Trial, Xining Reforms |
| Europe | Norman Conquest, Road to Canossa, Gregorian Reform, Domesday Book |
| Byzantium | Battle of Manzikert, Komnenos Dynasty |
| Middle East | Seljuk Empire rise, Nizamiyya Madrasa |
| Japan | Murasaki Shikibu, Fujiwara no Michinaga, The Tale of Genji |
| India | Chola Dynasty, Ghaznavid invasions |

## License / 授权

| Type | License |
|------|---------|
| Source Code | [Apache License 2.0](LICENSE) |
| Historical data, timelines & event descriptions | [CC BY-SA 4.0](LICENSE-CONTENT.md) |
| Project name, logo & brand identity | All rights reserved |

See [NOTICE](NOTICE.md) for details.

## Roadmap / 路线图

1. Supabase / PostgreSQL backend
2. Expanded time coverage (more historical periods)
3. Expanded region coverage (Africa, Americas, Southeast Asia, etc.)
4. Map-based and visual timeline views
5. Community contribution and curation tools
6. Additional language support

## Development / 开发

```bash
npm run dev          # Start dev server
npm run build        # Production build
npx tsc --noEmit     # Type check
npm run lint         # Lint
npm test             # Run tests (63 unit tests)
npm run test:coverage # Test coverage report
```

## Contributing / 贡献

Issues and pull requests are welcome. Before submitting a PR:

- Ensure typecheck and lint pass
- Include source citations for new data
- Follow existing code style
