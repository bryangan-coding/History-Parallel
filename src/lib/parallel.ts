import type {
  ParallelRegionGroup,
  ScoredEvent,
  TimeRange,
} from '@/lib/types';
import { events, getPersonById, getRegionById } from '@/data/mockData';
import type { Person } from '@/lib/types';

interface GetParallelEventsOptions {
  year: number;
  range?: TimeRange;
  focusEventId?: string;
  focusPersonId?: string;
}

/**
 * Get all events in parallel across regions for a given year and time range.
 * Returns events grouped by region, sorted by relevance.
 */
export function getParallelEvents({
  year,
  range = 20,
  focusEventId,
  focusPersonId,
}: GetParallelEventsOptions): ParallelRegionGroup[] {
  const minYear = year - range;
  const maxYear = year + range;

  // Find events within the time window
  const eventsInRange = events.filter((e) => {
    const eventStart = e.startYear;
    const eventEnd = e.endYear ?? e.startYear;
    return (
      (eventStart >= minYear && eventStart <= maxYear) ||
      (eventEnd >= minYear && eventEnd <= maxYear) ||
      (eventStart <= minYear && eventEnd >= maxYear)
    );
  });

  // Score each event
  const scored: ScoredEvent[] = eventsInRange.map((event) => {
    let score = 100;
    let distanceFromFocus = 0;

    // Distance from focus year
    const eventMid = event.endYear
      ? (event.startYear + event.endYear) / 2
      : event.startYear;
    distanceFromFocus = Math.abs(eventMid - year);
    score -= distanceFromFocus * 3;

    // Importance boost
    score += event.importance * 10;

    // Focus event/person boost
    if (focusEventId && event.id === focusEventId) {
      score += 200;
    }
    if (
      focusPersonId &&
      event.personIds.includes(focusPersonId)
    ) {
      score += 100;
    }

    // Resolve persons
    const persons: Person[] = event.personIds
      .map((pid) => getPersonById(pid))
      .filter((p): p is Person => p !== undefined);

    return { event, persons, score, distanceFromFocus };
  });

  // Group by region
  const grouped = new Map<string, ScoredEvent[]>();

  for (const s of scored) {
    const regionId = s.event.regionId;
    if (!grouped.has(regionId)) {
      grouped.set(regionId, []);
    }
    grouped.get(regionId)!.push(s);
  }

  // Sort events within each group
  for (const [, evts] of grouped) {
    evts.sort((a, b) => b.score - a.score);
  }

  // Build result, only include regions with events
  const result: ParallelRegionGroup[] = [];
  for (const [regionId, evts] of grouped) {
    const region = getRegionById(regionId);
    if (!region) continue;
    result.push({ region, events: evts });
  }

  // Sort regions: China first if focus is Chinese, then by event count
  result.sort((a, b) => {
    // Prioritize regions that have highest-scored events
    const aTop = a.events[0]?.score ?? 0;
    const bTop = b.events[0]?.score ?? 0;
    return bTop - aTop;
  });

  return result;
}
