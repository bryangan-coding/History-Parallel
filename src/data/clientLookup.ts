/**
 * Client-safe data utilities — NO large data arrays are imported.
 *
 * This module provides lightweight lookup helpers that accept pre-built
 * Map indexes as parameters. Use these in 'use client' components instead
 * of importing from '@/data/mockData'.
 *
 * The Map indexes are created on the server and passed down as props.
 */

import type { Person, HistoricalEvent, Region, Source } from '@/lib/types';

/** Look up a region by ID from a pre-built Map */
export function lookupRegion(regionMap: Map<string, Region>, id: string): Region | undefined {
  return regionMap.get(id);
}

/** Look up a person by ID from a pre-built Map */
export function lookupPerson(personMap: Map<string, Person>, id: string): Person | undefined {
  return personMap.get(id);
}

/** Look up an event by ID from a pre-built Map */
export function lookupEvent(eventMap: Map<string, HistoricalEvent>, id: string): HistoricalEvent | undefined {
  return eventMap.get(id);
}

/** Get persons for a given event using pre-built maps */
export function lookupPersonsForEvent(
  personMap: Map<string, Person>,
  eventMap: Map<string, HistoricalEvent>,
  eventId: string,
): Person[] {
  const event = eventMap.get(eventId);
  if (!event) return [];
  return event.personIds
    .map((pid) => personMap.get(pid))
    .filter((p): p is Person => p !== undefined);
}

/** Get events for a given person */
export function lookupEventsForPerson(
  events: HistoricalEvent[],
  personId: string,
): HistoricalEvent[] {
  return events.filter((e) => e.personIds.includes(personId) && e.dataStatus === 'published');
}

/** Build a region map from a regions array */
export function buildRegionMap(regions: Region[]): Map<string, Region> {
  return new Map(regions.map((r) => [r.id, r]));
}

/** Build a person map from a people array */
export function buildPersonMap(people: Person[]): Map<string, Person> {
  return new Map(people.map((p) => [p.id, p]));
}

/** Build an event map from an events array */
export function buildEventMap(events: HistoricalEvent[]): Map<string, HistoricalEvent> {
  return new Map(events.map((e) => [e.id, e]));
}
