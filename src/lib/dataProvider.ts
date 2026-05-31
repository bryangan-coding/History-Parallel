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
      const s = e.startYear;
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
    return mockSearch(query);
  }

  async getParallelEvents(opts: {
    year: number;
    range?: TimeRange;
    focusEventId?: string;
    focusPersonId?: string;
  }): Promise<ParallelRegionGroup[]> {
    return mockGetParallelEvents(opts);
  }
}

// ============================================================
// SupabaseDataProvider — 骨架（准备好接入时实现）
// ============================================================
//
// 接入步骤：
// 1. npm install @supabase/supabase-js
// 2. 复制 .env.example → .env.local，填入你的 Supabase 凭证
// 3. 在下方每个方法中实现 Supabase 查询
// 4. 翻转 NEXT_PUBLIC_DATA_PROVIDER=supabase
//
// Supabase 表/列名与本文件中的 TypeScript 类型对应，
// 参见 supabase/migrations/00001_initial_schema.sql。
//
// 注意：所有方法必须返回与 MockDataProvider 相同的类型。
// 页面/组件层永远不会直接导入 @supabase/supabase-js。

class SupabaseDataProvider implements DataProvider {
  // TODO: 在此初始化 Supabase client
  // import { createClient } from '@supabase/supabase-js'
  // private client = createClient(
  //   process.env.NEXT_PUBLIC_SUPABASE_URL!,
  //   process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
  // );

  async getRegions(): Promise<Region[]> {
    // TODO: this.client.from('regions').select('*').then(...)
    console.warn('[SupabaseDataProvider] getRegions not yet implemented');
    return [];
  }

  async getRegionById(id: string): Promise<Region | undefined> {
    // TODO: .from('regions').select('*').eq('id', id).single()
    console.warn('[SupabaseDataProvider] getRegionById not yet implemented');
    return undefined;
  }

  async getPersons(): Promise<Person[]> {
    // TODO: .from('persons').select('*')
    console.warn('[SupabaseDataProvider] getPersons not yet implemented');
    return [];
  }

  async getPersonById(id: string): Promise<Person | undefined> {
    // TODO: .from('persons').select('*').eq('id', id).single()
    console.warn('[SupabaseDataProvider] getPersonById not yet implemented');
    return undefined;
  }

  async getPersonsForEvent(eventId: string): Promise<Person[]> {
    // TODO: select from event_persons join persons on person_id = persons.id
    //       where event_id = eventId
    console.warn('[SupabaseDataProvider] getPersonsForEvent not yet implemented');
    return [];
  }

  async getEvents(): Promise<HistoricalEvent[]> {
    // TODO: .from('historical_events').select('*')
    console.warn('[SupabaseDataProvider] getEvents not yet implemented');
    return [];
  }

  async getEventById(id: string): Promise<HistoricalEvent | undefined> {
    // TODO: .from('historical_events').select('*').eq('id', id).single()
    console.warn('[SupabaseDataProvider] getEventById not yet implemented');
    return undefined;
  }

  async getEventsForPerson(personId: string): Promise<HistoricalEvent[]> {
    // TODO: select from event_persons join historical_events on event_id = historical_events.id
    //       where person_id = personId
    console.warn('[SupabaseDataProvider] getEventsForPerson not yet implemented');
    return [];
  }

  async getEventsByYearRange(startYear: number, endYear: number): Promise<HistoricalEvent[]> {
    // TODO: .from('historical_events')
    //       .gte('start_year', startYear)
    //       .lte('start_year', endYear)
    console.warn('[SupabaseDataProvider] getEventsByYearRange not yet implemented');
    return [];
  }

  async getSources(): Promise<Source[]> {
    // TODO: .from('sources').select('*')
    console.warn('[SupabaseDataProvider] getSources not yet implemented');
    return [];
  }

  async getSourceById(id: string): Promise<Source | undefined> {
    // TODO: .from('sources').select('*').eq('id', id).single()
    console.warn('[SupabaseDataProvider] getSourceById not yet implemented');
    return undefined;
  }

  async getSourcesForEvent(eventId: string): Promise<Source[]> {
    // TODO: select from event_sources join sources on source_id = sources.id
    //       where event_id = eventId
    console.warn('[SupabaseDataProvider] getSourcesForEvent not yet implemented');
    return [];
  }

  async search(query: string) {
    // TODO: 使用 Supabase 全文搜索 (tsvector) 或 edge function
    // 目前回退到 mock search 作为参考实现：
    // import { search as mockSearch } from './search';
    // return mockSearch(query);
    console.warn('[SupabaseDataProvider] search not yet implemented');
    return { people: [], events: [], regions: [], yearMatches: [] };
  }

  async getParallelEvents(opts: {
    year: number;
    range?: TimeRange;
    focusEventId?: string;
    focusPersonId?: string;
  }): Promise<ParallelRegionGroup[]> {
    // TODO: 通过 Supabase 查询实现平行事件算法
    // 1. 计算 minYear = year - range, maxYear = year + range
    // 2. 选择 start_year 在 min/max 之间或 end_year 在 min/max 之间的事件
    // 3. 通过 event_persons join 获取相关人物
    // 4. 在 JS 中按区域分组并评分（或通过 Supabase RPC 提升性能）
    console.warn('[SupabaseDataProvider] getParallelEvents not yet implemented');
    return [];
  }
}

// ============================================================
// 根据环境变量导出活跃的 provider
// ============================================================

const providerType = (process.env.NEXT_PUBLIC_DATA_PROVIDER ?? 'mock').toLowerCase();

let activeProvider: DataProvider;

if (providerType === 'supabase') {
  console.info('[dataProvider] 使用 SupabaseDataProvider');
  activeProvider = new SupabaseDataProvider();
} else {
  console.info('[dataProvider] 使用 MockDataProvider');
  activeProvider = new MockDataProvider();
}

export default activeProvider;
