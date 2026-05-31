'use server';

import type { Person, HistoricalEvent, Region, Source, SearchResult } from '@/lib/types';
import { people, events, regions, sources, getPersonById, getEventById, getRegionById, getSubRegions, getEventsByRegion, getSourcesForEvent, getAllTags } from '@/data/mockData';
import { search } from '@/lib/search';
import { getParallelEvents } from '@/lib/parallel';

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

export async function fetchPerson(id: string): Promise<Person | undefined> {
  return getPersonById(id);
}

export async function fetchEvent(id: string): Promise<HistoricalEvent | undefined> {
  return getEventById(id);
}

export async function fetchRegion(id: string): Promise<Region | undefined> {
  return getRegionById(id);
}

export async function searchData(query: string): Promise<SearchResult> {
  return search(query);
}

export async function fetchEventsByRegion(regionId: string): Promise<HistoricalEvent[]> {
  return getEventsByRegion(regionId);
}
