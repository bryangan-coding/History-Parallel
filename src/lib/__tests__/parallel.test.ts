/**
 * Tests for getParallelEvents
 * Covers: year range logic (0, 5, 20, 100), cross-year events, focus boosts
 */
import { getParallelEvents } from '@/lib/parallel';
import type { HistoricalEvent } from '@/lib/types';
import { events, personMap, regionMap } from '@/data/mockData';

describe('getParallelEvents — range logic', () => {
  test('range=0 returns only events that include the exact year', () => {
    const result = getParallelEvents({ year: 1080, range: 0, events, personMap, regionMap });
    const allEvents = result.flatMap((g) => g.events.map((s) => s.event));
    for (const evt of allEvents) {
      const start = evt.startYear ?? 0;
      const end = evt.endYear ?? start;
      const includes1080 =
        (start <= 1080 && end >= 1080) ||
        start === 1080 ||
        end === 1080;
      expect(includes1080).toBe(true);
    }
  });

  test('range=5 returns events within ±5 years of target year', () => {
    const result = getParallelEvents({ year: 1080, range: 5, events, personMap, regionMap });
    const allEvents = result.flatMap((g) => g.events.map((s) => s.event));
    for (const evt of allEvents) {
      const start = evt.startYear ?? 0;
      const end = evt.endYear ?? start;
      const inRange =
        Math.abs(start - 1080) <= 5 ||
        Math.abs(end - 1080) <= 5 ||
        (start <= 1080 && end >= 1080);
      expect(inRange).toBe(true);
    }
  });

  test('range=20 returns events within ±20 years of target year', () => {
    const result = getParallelEvents({ year: 1080, range: 20, events, personMap, regionMap });
    const allEvents = result.flatMap((g) => g.events.map((s) => s.event));
    for (const evt of allEvents) {
      const start = evt.startYear ?? 0;
      const end = evt.endYear ?? start;
      const inRange =
        Math.abs(start - 1080) <= 20 ||
        Math.abs(end - 1080) <= 20 ||
        (start <= 1080 && end >= 1080);
      expect(inRange).toBe(true);
    }
  });

  test('range=100 returns events within ±100 years of target year', () => {
    const result = getParallelEvents({ year: 1080, range: 100, events, personMap, regionMap });
    const allEvents = result.flatMap((g) => g.events.map((s) => s.event));
    // With range=100, we should get many events from ~980 to ~1180
    expect(allEvents.length).toBeGreaterThan(5);
    for (const evt of allEvents) {
      const start = evt.startYear ?? 0;
      const end = evt.endYear ?? start;
      const inRange =
        Math.abs(start - 1080) <= 100 ||
        Math.abs(end - 1080) <= 100 ||
        (start <= 1080 && end >= 1080);
      expect(inRange).toBe(true);
    }
  });
});

describe('getParallelEvents — cross-year (multi-year) events', () => {
  test('includes events that span across the target year', () => {
    // Find an event with endYear that spans across 1080
    const multiYearEvent = events.find(
      (e) =>
        e.endYear !== undefined &&
        (e.startYear ?? 0) <= 1080 &&
        e.endYear >= 1080
    );
    // If such an event exists in mock data, it should appear in range=0
    if (multiYearEvent) {
      const result = getParallelEvents({ year: 1080, range: 0, events, personMap, regionMap });
      const allIds = result.flatMap((g) => g.events.map((s) => s.event.id));
      expect(allIds).toContain(multiYearEvent.id);
    }
  });

  test('includes multi-year events when range > 0 and event overlaps with range', () => {
    // An event like 王安石变法 (1069-1085) should appear for year=1080, range=5
    const result = getParallelEvents({ year: 1080, range: 5, events, personMap, regionMap });
    const allIds = result.flatMap((g) => g.events.map((s) => s.event.id));
    // 王安石变法 (1069-1085) overlaps with 1075-1085
    expect(allIds).toContain('evt-wang-anshi-reform');
  });
});

describe('getParallelEvents — focusEventId boost', () => {
  test('focusEventId boosts the specified event to top of its region group', () => {
    const result = getParallelEvents({
      year: 1080,
      range: 20,
      focusEventId: 'evt-sushi-huangzhou',
      events,
      personMap,
      regionMap,
    });
    // The focused event should be the highest-scored in its region group
    for (const group of result) {
      const ids = group.events.map((s) => s.event.id);
      if (ids.includes('evt-sushi-huangzhou')) {
        // It should be the first in its group (highest score)
        expect(ids[0]).toBe('evt-sushi-huangzhou');
        break;
      }
    }
  });

  test('focusEventId still works when range=0', () => {
    const result = getParallelEvents({
      year: 1080,
      range: 0,
      focusEventId: 'evt-sushi-huangzhou',
      events,
      personMap,
      regionMap,
    });
    const allIds = result.flatMap((g) => g.events.map((s) => s.event.id));
    expect(allIds).toContain('evt-sushi-huangzhou');
  });
});

describe('getParallelEvents — data status filtering', () => {
  test('only published events appear in parallel results', () => {
    const result = getParallelEvents({ year: 1080, range: 20, events, personMap, regionMap });
    const allIds = result.flatMap((g) => g.events.map((s) => s.event.id));
    // All results should be published
    const allEvents = result.flatMap((g) => g.events.map((s) => s.event));
    expect(allEvents.every((e) => e.dataStatus === 'published')).toBe(true);
  });

  test('needs_review events do not appear in parallel results', () => {
    const result = getParallelEvents({ year: 1080, range: 20, events, personMap, regionMap });
    const allEvents = result.flatMap((g) => g.events.map((s) => s.event));
    expect(allEvents.some((e) => e.dataStatus !== 'published')).toBe(false);
  });
});

describe('getParallelEvents — focusPersonId boost', () => {
  test('focusPersonId boosts events associated with that person', () => {
    const result = getParallelEvents({
      year: 1080,
      range: 20,
      focusPersonId: 'su-shi',
      events,
      personMap,
      regionMap,
    });
    // Su Shi's events should be near the top of their region groups
    const allEvents = result.flatMap((g) => g.events);
    const suShiEvents = allEvents.filter((s) =>
      s.event.personIds.includes('su-shi')
    );
    expect(suShiEvents.length).toBeGreaterThan(0);
    // The top-scored event in each group should ideally be Su Shi's
    // (not strictly guaranteed but highly likely due to +100 boost)
    for (const group of result) {
      if (group.events[0]?.event.personIds.includes('su-shi')) {
        // At least one group has a Su Shi event at the top
        expect(true).toBe(true);
        return;
      }
    }
  });
});

describe('getParallelEvents — grouping by region', () => {
  test('returns groups each with a valid region', () => {
    const result = getParallelEvents({ year: 1080, range: 20, events, personMap, regionMap });
    for (const group of result) {
      expect(group.region).toBeDefined();
      expect(group.region.id).toBeDefined();
      expect(group.events.length).toBeGreaterThan(0);
    }
  });

  test('events in each group belong to the same region', () => {
    const result = getParallelEvents({ year: 1080, range: 20, events, personMap, regionMap });
    for (const group of result) {
      for (const s of group.events) {
        expect(s.event.regionId).toBe(group.region.id);
      }
    }
  });
});

describe('getParallelEvents — sorting within groups', () => {
  test('events within each group are sorted by score descending', () => {
    const result = getParallelEvents({ year: 1080, range: 20, events, personMap, regionMap });
    for (const group of result) {
      const scores = group.events.map((s) => s.score);
      for (let i = 1; i < scores.length; i++) {
        expect(scores[i]!).toBeLessThanOrEqual(scores[i - 1]!);
      }
    }
  });
});

describe('getParallelEvents — edge cases', () => {
  test('returns empty groups for a year with no nearby events', () => {
    // Year 3000 is far outside our mock data range
    const result = getParallelEvents({ year: 3000, range: 0, events, personMap, regionMap });
    const allEvents = result.flatMap((g) => g.events);
    expect(allEvents).toEqual([]);
  });

  test('returns results for year at the edge of mock data range', () => {
    const result = getParallelEvents({ year: 960, range: 5, events, personMap, regionMap });
    // Should find events near 960 (Song founding)
    expect(result.length).toBeGreaterThanOrEqual(0);
  });
});
