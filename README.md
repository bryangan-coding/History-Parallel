# History Parallel

> See what was happening around the world at the same moment in history.

**History Parallel** is a web app for comparing historical timelines across civilizations. Pick a point in time, a historical figure, a region, or an event — and see what was unfolding simultaneously across different parts of the globe.

## Quick Start

```bash
npm install
npm run dev
# Open http://localhost:3000
```

## Tech Stack

| Layer | Choice |
|-------|--------|
| Framework | Next.js (App Router) |
| Language | TypeScript |
| Styling | Tailwind CSS v4 |
| Icons | lucide-react |
| State | React state (MVP) |
| Database | Mock data → Supabase (planned) |

## Project Structure

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

## Core Features

- **Home**: Search entry + example prompts + browse by person / year / region
- **Search**: Find people, events, regions, and years with grouped results
- **Person Page**: Bio + life timeline + "explore the world at this time" link
- **Parallel Timeline** (core): Side-by-side comparison of events across regions, with card view and horizontal timeline view
- **Event Detail**: Event description + source citations + related people
- **Data Notes**: Data structure, sourcing principles, licensing
- **i18n**: Full Chinese / English language switch, with manually verified translations for all historical names and facts

## Data Coverage

MVP covers the **11th century** (~960–1127 CE), including:

| Region | Content |
|--------|---------|
| Northern Song China | Su Shi, Wang Anshi, Sima Guang, Ouyang Xiu; Crow Terrace Poetry Trial, Xining Reforms |
| Europe | Norman Conquest, Road to Canossa, Gregorian Reform, Domesday Book |
| Byzantium | Battle of Manzikert, Komnenos Dynasty |
| Middle East | Seljuk Empire rise, Nizamiyya Madrasa |
| Japan | Murasaki Shikibu, Fujiwara no Michinaga, The Tale of Genji |
| India | Chola Dynasty, Ghaznavid invasions |

## License

| Type | License |
|------|---------|
| Source Code | [Apache License 2.0](LICENSE) |
| Historical data, timelines & event descriptions | [CC BY-SA 4.0](LICENSE-CONTENT.md) |
| Project name, logo & brand identity | All rights reserved |

See [NOTICE](NOTICE.md) for details.

## Roadmap

1. Supabase / PostgreSQL backend
2. Expanded time coverage (more historical periods)
3. Expanded region coverage (Africa, Americas, Southeast Asia, etc.)
4. Map-based and visual timeline views
5. Community contribution and curation tools
6. Additional language support

## Development

```bash
npm run dev          # Start dev server
npm run build        # Production build
npx tsc --noEmit     # Type check
npm run lint         # Lint
npm test             # Run tests (63 unit tests)
npm run test:coverage # Test coverage report
```

## Contributing

Issues and pull requests are welcome. Before submitting a PR:

- Ensure typecheck and lint pass
- Include source citations for new data
- Follow existing code style
