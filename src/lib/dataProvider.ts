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
// ============================================================

import {
  regions as mockRegions,
  people as mockPeople,
  events as mockEvents,
  sources as mockSources,
  personMap as mockPersonMap,
  regionMap as mockRegionMap,
  getRegionById as mockGetRegionById,
  getPersonById as mockGetPersonById,
  getEventById as mockGetEventById,
  getPersonsForEvent as mockGetPersonsForEvent,
  getEventsForPerson as mockGetEventsForPerson,
  getSourcesForEvent as mockGetSourcesForEvent,
} from '@/data/mockData';
import { search as mockSearch } from '@/lib/search';
import { getParallelEvents as mockGetParallelEvents } from '@/lib/parallel';

class MockDataProvider implements DataProvider {
  async getRegions(): Promise<Region[]> {
    return mockRegions;
  }

  async getRegionById(id: string): Promise<Region | undefined> {
    return mockGetRegionById(id);
  }

  async getPersons(): Promise<Person[]> {
    return mockPeople;
  }

  async getPersonById(id: string): Promise<Person | undefined> {
    return mockGetPersonById(id);
  }

  async getPersonsForEvent(eventId: string): Promise<Person[]> {
    return mockGetPersonsForEvent(eventId);
  }

  async getEvents(): Promise<HistoricalEvent[]> {
    return mockEvents;
  }

  async getEventById(id: string): Promise<HistoricalEvent | undefined> {
    return mockGetEventById(id);
  }

  async getEventsForPerson(personId: string): Promise<HistoricalEvent[]> {
    return mockGetEventsForPerson(personId);
  }

  async getEventsByYearRange(startYear: number, endYear: number): Promise<HistoricalEvent[]> {
    return mockEvents.filter((e) => {
      if (e.dataStatus !== 'published') return false;
      const s = e.startYear ?? 0;
      const en = e.endYear ?? s;
      return (s >= startYear && s <= endYear) || (en >= startYear && en <= endYear) || (s <= startYear && en >= endYear);
    });
  }

  async getSources(): Promise<Source[]> {
    return mockSources;
  }

  async getSourceById(id: string): Promise<Source | undefined> {
    return mockSources.find((s) => s.id === id);
  }

  async getSourcesForEvent(eventId: string): Promise<Source[]> {
    return mockGetSourcesForEvent(eventId);
  }

  async search(query: string) {
    return mockSearch(query, mockPeople, mockEvents, mockRegions);
  }

  async getParallelEvents(opts: {
    year: number;
    range?: TimeRange;
    focusEventId?: string;
    focusPersonId?: string;
  }): Promise<ParallelRegionGroup[]> {
    return mockGetParallelEvents({
      ...opts,
      events: mockEvents,
      personMap: mockPersonMap,
      regionMap: mockRegionMap,
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
