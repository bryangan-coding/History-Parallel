/**
 * Lightweight helper functions for client-side use.
 * These functions are tree-shakeable and do NOT pull in the full data arrays.
 * Import from here instead of '@/data/mockData' in client components.
 */

import type { Person, HistoricalEvent, Region, Source } from '@/lib/types';

// These are set lazily from the server-side data
let _people: Person[] = [];
let _events: HistoricalEvent[] = [];
let _regions: Region[] = [];
let _sources: Source[] = [];

/** Initialize helpers with data (called by server components) */
export function initData(people: Person[], events: HistoricalEvent[], regions: Region[], sources: Source[]) {
  _people = people;
  _events = events;
  _regions = regions;
  _sources = sources;
}

export function getPersonById(id: string): Person | undefined {
  return _people.find((p) => p.id === id);
}

export function getRegionById(id: string): Region | undefined {
  return _regions.find((r) => r.id === id);
}

export function getEventById(id: string): HistoricalEvent | undefined {
  return _events.find((e) => e.id === id);
}

export function getSourceById(id: string): Source | undefined {
  return _sources.find((s) => s.id === id);
}

export function getSubRegions(regionId: string): Region[] {
  return _regions.filter((r) => r.parentRegionId === regionId);
}

export function getEventsForPerson(personId: string): HistoricalEvent[] {
  return _events.filter((e) => e.personIds.includes(personId) && e.dataStatus === 'published');
}

export function getPersonsForEvent(eventId: string): Person[] {
  const event = _events.find((e) => e.id === eventId);
  if (!event) return [];
  return event.personIds.map((pid) => _people.find((p) => p.id === pid)!).filter(Boolean);
}

export function getEventsByRegion(regionId: string): HistoricalEvent[] {
  return _events.filter((e) => e.regionId === regionId && e.dataStatus === 'published');
}

export function getAllTags(): string[] {
  const tagSet = new Set<string>();
  _people.forEach((p) => p.tags.forEach((t) => tagSet.add(t)));
  _events.forEach((e) => e.tags.forEach((t) => tagSet.add(t)));
  return Array.from(tagSet).sort();
}

export function getSourcesForEvent(eventId: string): Source[] {
  const event = _events.find((e) => e.id === eventId);
  if (!event) return [];
  return event.sourceIds.map((sid) => _sources.find((s) => s.id === sid)!).filter(Boolean);
}
