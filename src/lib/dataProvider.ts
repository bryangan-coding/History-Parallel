/**
 * Data Provider — 历史平行线 (History Parallel) 数据访问抽象层
 *
 * 架构：页面/组件 → dataProvider（本文件）→ mockData.ts | Supabase client
 *
 * 切换方式：在 .env.local 中设置 NEXT_PUBLIC_DATA_PROVIDER=mock 或 supabase
 * 默认值：mock（无需 Supabase 即可运行）
 *
 * 当接入 Supabase 时：实现 SupabaseDataProvider 中的每个方法，
 * 然后翻转环境变量。页面/组件层无需任何改动。
 */

import type {
  Region,
  Person,
  HistoricalEvent,
  Source,
  Locale,
  ParallelRegionGroup,
  ScoredEvent,
  TimeRange,
} from './types';

// ============================================================
// DataProvider 接口 — 应用所需的所有数据访问方法
// ============================================================

export interface DataProvider {
  // ---- Regions ----
  getRegions(): Promise<Region[]>;
  getRegionById(id: string): Promise<Region | undefined>;

  // ---- Persons ----
  getPersons(): Promise<Person[]>;
  getPersonById(id: string): Promise<Person | undefined>;
  getPersonsForEvent(eventId: string): Promise<Person[]>;

  // ---- Events ----
  getEvents(): Promise<HistoricalEvent[]>;
  getEventById(id: string): Promise<HistoricalEvent | undefined>;
  getEventsForPerson(personId: string): Promise<HistoricalEvent[]>;
  getEventsByYearRange(startYear: number, endYear: number): Promise<HistoricalEvent[]>;

  // ---- Sources ----
  getSources(): Promise<Source[]>;
  getSourceById(id: string): Promise<Source | undefined>;
  getSourcesForEvent(eventId: string): Promise<Source[]>;

  // ---- Search ----
  search(query: string): Promise<{
    people: Person[];
    events: HistoricalEvent[];
    regions: Region[];
    yearMatches: { year: number; nearEvents: HistoricalEvent[]; label: string }[];
  }>;

  // ---- Parallel events ----
  getParallelEvents(opts: {
    year: number;
    range?: TimeRange;
    focusEventId?: string;
    focusPersonId?: string;
  }): Promise<ParallelRegionGroup[]>;
}

// ============================================================
// MockDataProvider — 基于现有 mockData.ts（同步数据）
//
// IMPORTANT: mockData.ts 导入约 170 个大型 JSON 文件（~140MB+）。
// 使用动态 import() 延迟加载，仅在实际使用 mock provider 时才加载。
// 当前默认 provider 为 MySQL，因此 mockData 不会被加载到内存中。
// ============================================================

class MockDataProvider implements DataProvider {
  private _loaded = false;
  // Use any type to avoid TypeScript compiler resolving mockData.ts's 170+ JSON imports
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  private _mockData: any = null;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  private _mockSearch: any = null;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  private _mockGetParallelEvents: any = null;

  private async _load() {
    if (this._loaded) return;
    const [mockData, searchMod, parallelMod] = await Promise.all([
      import('@/data/mockData'),
      import('@/lib/search'),
      import('@/lib/parallel'),
    ]);
    this._mockData = mockData;
    this._mockSearch = searchMod.search;
    this._mockGetParallelEvents = parallelMod.getParallelEvents;
    this._loaded = true;
  }

  async getRegions(): Promise<Region[]> {
    await this._load();
    return this._mockData!.regions;
  }

  async getRegionById(id: string): Promise<Region | undefined> {
    await this._load();
    return this._mockData!.getRegionById(id);
  }

  async getPersons(): Promise<Person[]> {
    await this._load();
    return this._mockData!.people;
  }

  async getPersonById(id: string): Promise<Person | undefined> {
    await this._load();
    return this._mockData!.getPersonById(id);
  }

  async getPersonsForEvent(eventId: string): Promise<Person[]> {
    await this._load();
    return this._mockData!.getPersonsForEvent(eventId);
  }

  async getEvents(): Promise<HistoricalEvent[]> {
    await this._load();
    return this._mockData!.events;
  }

  async getEventById(id: string): Promise<HistoricalEvent | undefined> {
    await this._load();
    return this._mockData!.getEventById(id);
  }

  async getEventsForPerson(personId: string): Promise<HistoricalEvent[]> {
    await this._load();
    return this._mockData!.getEventsForPerson(personId);
  }

  async getEventsByYearRange(startYear: number, endYear: number): Promise<HistoricalEvent[]> {
    await this._load();
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const mockEvents = this._mockData!.events as any[];
    return mockEvents.filter((e: any) => {
      if (e.dataStatus !== 'published') return false;
      const s = e.startYear ?? 0;
      const en = e.endYear ?? s;
      return (s >= startYear && s <= endYear) || (en >= startYear && en <= endYear) || (s <= startYear && en >= endYear);
    });
  }

  async getSources(): Promise<Source[]> {
    await this._load();
    return this._mockData!.sources;
  }

  async getSourceById(id: string): Promise<Source | undefined> {
    await this._load();
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    return this._mockData!.sources.find((s: any) => s.id === id);
  }

  async getSourcesForEvent(eventId: string): Promise<Source[]> {
    await this._load();
    return this._mockData!.getSourcesForEvent(eventId);
  }

  async search(query: string) {
    await this._load();
    return this._mockSearch!(query, this._mockData!.people, this._mockData!.events, this._mockData!.regions);
  }

  async getParallelEvents(opts: {
    year: number;
    range?: TimeRange;
    focusEventId?: string;
    focusPersonId?: string;
  }): Promise<ParallelRegionGroup[]> {
    await this._load();
    return this._mockGetParallelEvents!({
      ...opts,
      events: this._mockData!.events,
      personMap: this._mockData!.personMap,
      regionMap: this._mockData!.regionMap,
    });
  }
}

// ============================================================
// SupabaseDataProvider — 骨架
// ============================================================

class SupabaseDataProvider implements DataProvider {
  // ... (existing skeleton)
  async getRegions(): Promise<Region[]> { console.warn('[Supabase] not implemented'); return []; }
  async getRegionById(): Promise<Region | undefined> { return undefined; }
  async getPersons(): Promise<Person[]> { return []; }
  async getPersonById(): Promise<Person | undefined> { return undefined; }
  async getPersonsForEvent(): Promise<Person[]> { return []; }
  async getEvents(): Promise<HistoricalEvent[]> { return []; }
  async getEventById(): Promise<HistoricalEvent | undefined> { return undefined; }
  async getEventsForPerson(): Promise<HistoricalEvent[]> { return []; }
  async getEventsByYearRange(): Promise<HistoricalEvent[]> { return []; }
  async getSources(): Promise<Source[]> { return []; }
  async getSourceById(): Promise<Source | undefined> { return undefined; }
  async getSourcesForEvent(): Promise<Source[]> { return []; }
  async search() { return { people: [], events: [], regions: [], yearMatches: [] }; }
  async getParallelEvents(): Promise<ParallelRegionGroup[]> { return []; }
}

// ============================================================
// MySQLDataProvider — 懒加载，仅服务端，并发安全
// ============================================================

let mysqlProvider: DataProvider | null = null;
let mysqlProviderPromise: Promise<DataProvider> | null = null;

async function getMySQLProvider(): Promise<DataProvider> {
  if (mysqlProvider) return mysqlProvider;
  if (mysqlProviderPromise) return mysqlProviderPromise;
  
  mysqlProviderPromise = import('@/server/db/MySQLDataProvider').then(mod => {
    mysqlProvider = new mod.MySQLDataProvider();
    return mysqlProvider;
  });
  return mysqlProviderPromise;
}

// ============================================================
// 根据环境变量导出活跃的 provider
// ============================================================

const providerType = (process.env.NEXT_PUBLIC_DATA_PROVIDER ?? 'mysql').toLowerCase();

let activeProvider: DataProvider | Promise<DataProvider>;

if (providerType === 'mysql') {
  activeProvider = getMySQLProvider();
} else if (providerType === 'supabase') {
  activeProvider = new SupabaseDataProvider();
} else {
  activeProvider = new MockDataProvider();
}

// Helper: resolve the provider (handles async lazy-loading for MySQL)
export async function resolveProvider(): Promise<DataProvider> {
  return activeProvider instanceof Promise ? activeProvider : activeProvider;
}

export default activeProvider;
