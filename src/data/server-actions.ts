'use server';

import type { Person, HistoricalEvent, Region, Source, SearchResult } from '@/lib/types';
import {
  people,
  events,
  regions,
  sources,
  personMap,
  regionMap,
  eventMap,
  getEventsForPerson as _getEventsForPerson,
  getSubRegions as _getSubRegions,
  getEventsByRegion as _getEventsByRegion,
  getAllTags as _getAllTags,
} from '@/data/mockData';
import { search } from '@/lib/search';
import { getParallelEvents } from '@/lib/parallel';

// ==================== Data fetchers ====================

export async function getPublishedPeople(): Promise<Person[]> {
  return people.filter((p) => p.dataStatus === 'published');
}

export async function getAllPeople(): Promise<Person[]> {
  return people;
}

export async function getAllEvents(): Promise<HistoricalEvent[]> {
  return events.filter((e) => e.dataStatus === 'published');
}

export async function getAllRegions(): Promise<Region[]> {
  return regions;
}

export async function getAllSources(): Promise<Source[]> {
  return sources;
}

// ==================== Single entity lookups ====================

export async function fetchPerson(id: string): Promise<Person | undefined> {
  return personMap.get(id);
}

export async function fetchEvent(id: string): Promise<HistoricalEvent | undefined> {
  return eventMap.get(id);
}

export async function fetchRegion(id: string): Promise<Region | undefined> {
  return regionMap.get(id);
}

// ==================== Search ====================

export async function searchData(query: string): Promise<SearchResult> {
  return search(query, people, events, regions);
}

// ==================== Parallel events ====================

export async function fetchParallelEvents(opts: {
  year: number;
  range?: number;
  focusEventId?: string;
  focusPersonId?: string;
}) {
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
  return _getEventsByRegion(regionId);
}

export async function fetchEventsForPerson(personId: string): Promise<HistoricalEvent[]> {
  return _getEventsForPerson(personId);
}

export async function fetchSubRegions(regionId: string): Promise<Region[]> {
  return _getSubRegions(regionId);
}

export async function fetchAllTags(): Promise<string[]> {
  return _getAllTags();
}
