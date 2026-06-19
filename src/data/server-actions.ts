'use server';

import type { Person, HistoricalEvent, Region, Source, SearchResult } from '@/lib/types';
import { search } from '@/lib/search';
import { getParallelEvents } from '@/lib/parallel';
import {
  listPeople,
  findPersonById,
  findPeopleByIds,
  listEvents,
  listAllEvents,
  findEventById,
  findEventsForPerson,
  findEventsByRegion,
  findEventsByYearRange,
  findPersonsForEvent,
  listRegions,
  findRegionById,
  findSubRegions,
  listSources,
  findAllTags,
  listEventsBySearch,
} from '@/server/db/queries';

// ==================== Data fetchers ====================

export async function getPublishedPeople(): Promise<Person[]> {
  const { items } = await listPeople({ publishedOnly: true });
  return items;
}

export async function getAllPeople(): Promise<Person[]> {
  const { items } = await listPeople();
  return items;
}

export async function getAllEvents(): Promise<HistoricalEvent[]> {
  return listEvents({ publishedOnly: true });
}

export async function getAllRegions(): Promise<Region[]> {
  return listRegions();
}

export async function getAllSources(): Promise<Source[]> {
  return listSources();
}

// ==================== Single entity lookups ====================

export async function fetchPerson(id: string): Promise<Person | undefined> {
  return findPersonById(id);
}

export async function fetchEvent(id: string): Promise<HistoricalEvent | undefined> {
  return findEventById(id);
}

export async function fetchRegion(id: string): Promise<Region | undefined> {
  return findRegionById(id);
}

// ==================== Search ====================
// Uses DB-side queries instead of loading all data into memory.

export async function searchData(query: string): Promise<SearchResult> {
  const q = query.trim();
  if (!q) return { people: [], events: [], regions: [], yearMatches: [] };

  // Search people via SQL LIKE (limited to 100)
  const { items: people } = await listPeople({ publishedOnly: true, query: q, limit: 100 });

  // Search events via SQL (title/summary LIKE, limited to 50)
  const events = await listEventsBySearch(q, 50);

  // Region search
  const regions = await listRegions();
  const lowerQ = q.toLowerCase();
  const filteredRegions = regions.filter(r =>
    r.name?.toLowerCase().includes(lowerQ) || r.nameEn?.toLowerCase().includes(lowerQ)
  ).slice(0, 20);

  // Year search via time-range query
  const yearNum = parseInt(q, 10);
  let yearMatches: { year: number; nearEvents: HistoricalEvent[]; label: string }[] = [];
  if (!isNaN(yearNum)) {
    const nearEvents = await findEventsByYearRange(yearNum - 20, yearNum + 20);
    if (nearEvents.length > 0) {
      yearMatches = [{ year: yearNum, nearEvents: nearEvents.slice(0, 30), label: `${yearNum}年前后的事件` }];
    }
  }

  return { people, events, regions: filteredRegions, yearMatches };
}

// ==================== Parallel events ====================
// Fetches only events within the time window via SQL, not the full table.

export async function fetchParallelEvents(opts: {
  year: number;
  range?: number;
  focusEventId?: string;
  focusPersonId?: string;
}) {
  const { year, range = 20 } = opts;
  const minYear = year - range;
  const maxYear = year + range;

  // SQL-side time-filtered event fetch
  const events = await findEventsByYearRange(minYear, maxYear);

  const regions = await listRegions();
  const regionMap = new Map(regions.map((r) => [r.id, r]));

  // Only fetch persons referenced by the filtered events
  const personIds = [...new Set(events.flatMap(e => e.personIds))];
  const people = personIds.length > 0 ? await findPeopleByIds(personIds) : [];
  const personMap = new Map(people.map((p) => [p.id, p]));

  return getParallelEvents({
    ...opts,
    range: opts.range as import('@/lib/types').TimeRange | undefined,
    events,
    personMap,
    regionMap,
  });
}

// ==================== Relationship data ====================

export async function fetchEventsByRegion(regionId: string): Promise<HistoricalEvent[]> {
  return findEventsByRegion(regionId);
}

export async function fetchEventsForPerson(personId: string): Promise<HistoricalEvent[]> {
  return findEventsForPerson(personId);
}

export async function fetchPersonsForEvent(eventId: string): Promise<Person[]> {
  return findPersonsForEvent(eventId);
}

export async function fetchSubRegions(regionId: string): Promise<Region[]> {
  return findSubRegions(regionId);
}

export async function fetchAllTags(): Promise<string[]> {
  return findAllTags();
}
