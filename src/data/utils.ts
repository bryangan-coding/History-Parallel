/**
 * Pure utility functions that accept data as parameters.
 * These are SAFE to import in client components — no data arrays are bundled.
 * Import from here instead of '@/data/mockData' in client components.
 */
import type { Person, HistoricalEvent, Region, Source } from '@/lib/types';

export function getRegionById(regions: Region[], id: string): Region | undefined {
  return regions.find((r) => r.id === id);
}

export function getPersonById(people: Person[], id: string): Person | undefined {
  return people.find((p) => p.id === id);
}

export function getEventById(events: HistoricalEvent[], id: string): HistoricalEvent | undefined {
  return events.find((e) => e.id === id);
}

export function getSourceById(sources: Source[], id: string): Source | undefined {
  return sources.find((s) => s.id === id);
}

export function getSubRegions(regions: Region[], regionId: string): Region[] {
  return regions.filter((r) => r.parentRegionId === regionId);
}

export function getEventsForPerson(events: HistoricalEvent[], personId: string): HistoricalEvent[] {
  return events.filter((e) => e.personIds.includes(personId) && e.dataStatus === 'published');
}

export function getPersonsForEvent(people: Person[], events: HistoricalEvent[], eventId: string): Person[] {
  const event = events.find((e) => e.id === eventId);
  if (!event) return [];
  return event.personIds.map((pid) => people.find((p) => p.id === pid)!).filter(Boolean);
}

export function getEventsByRegion(events: HistoricalEvent[], regionId: string): HistoricalEvent[] {
  return events.filter((e) => e.regionId === regionId && e.dataStatus === 'published');
}

export function getAllTags(people: Person[], events: HistoricalEvent[]): string[] {
  const tagSet = new Set<string>();
  people.forEach((p) => p.tags.forEach((t) => tagSet.add(t)));
  events.forEach((e) => e.tags.forEach((t) => tagSet.add(t)));
  return Array.from(tagSet).sort();
}

export function getSourcesForEvent(sources: Source[], events: HistoricalEvent[], eventId: string): Source[] {
  const event = events.find((e) => e.id === eventId);
  if (!event) return [];
  return event.sourceIds.map((sid) => sources.find((s) => s.id === sid)!).filter(Boolean);
}
