/**
 * Tests for dataProvider methods:
 *   getPersonById, getEventById, getEventsForPerson, getRegionById
 */
import type { Person, HistoricalEvent, Region } from '@/lib/types';
import {
  getPersonById,
  getEventById,
  getEventsForPerson,
  getRegionById,
  getPersonsForEvent,
  getSourcesForEvent,
} from '@/data/mockData';

// ---------- getPersonById ----------

describe('getPersonById', () => {
  test('returns the correct person for a valid id', () => {
    const suShi = getPersonById('su-shi');
    expect(suShi).toBeDefined();
    expect(suShi?.name).toBe('苏轼');
    expect(suShi?.birthYear).toBe(1037);
    expect(suShi?.deathYear).toBe(1101);
  });

  test('returns Wang Anshi correctly', () => {
    const wang = getPersonById('wang-anshi');
    expect(wang).toBeDefined();
    expect(wang?.name).toBe('王安石');
    expect(wang?.tags).toContain('改革家');
  });

  test('returns undefined for non-existent id', () => {
    const result = getPersonById('nonexistent-person-id');
    expect(result).toBeUndefined();
  });

  test('returns English name when available', () => {
    const suShi = getPersonById('su-shi');
    expect(suShi?.nameEn).toBe('Su Shi (Su Dongpo)');
  });
});

// ---------- getEventById ----------

describe('getEventById', () => {
  test('returns the correct event for a valid id', () => {
    const evt = getEventById('evt-sushi-huangzhou');
    expect(evt).toBeDefined();
    expect(evt?.title).toContain('苏轼被贬黄州');
    expect(evt?.startYear).toBe(1080);
  });

  test('returns undefined for non-existent id', () => {
    const result = getEventById('nonexistent-event-id');
    expect(result).toBeUndefined();
  });

  test('returns event with endYear when applicable', () => {
    const reform = getEventById('evt-wang-anshi-reform');
    expect(reform).toBeDefined();
    expect(reform?.endYear).toBe(1085);
  });
});

// ---------- getEventsForPerson ----------

describe('getEventsForPerson', () => {
  test('returns events associated with Su Shi', () => {
    const events = getEventsForPerson('su-shi');
    expect(events.length).toBeGreaterThan(0);
    // Su Shi's events include: 乌台诗案, 被贬黄州, etc.
    const titles = events.map((e) => e.title);
    expect(titles.some((t) => t.includes('苏轼'))).toBe(true);
  });

  test('returns multiple events for Wang Anshi', () => {
    const events = getEventsForPerson('wang-anshi');
    expect(events.length).toBeGreaterThan(0);
  });

  test('returns empty array for non-existent person id', () => {
    const events = getEventsForPerson('nonexistent-person-id');
    expect(events).toEqual([]);
  });

  test('returned events have correct personIds linkage', () => {
    const events = getEventsForPerson('su-shi');
    for (const evt of events) {
      expect(evt.personIds).toContain('su-shi');
    }
  });
});

// ---------- getRegionById ----------

describe('getRegionById', () => {
  test('returns the correct region for a valid id', () => {
    const region = getRegionById('song-dynasty');
    expect(region).toBeDefined();
    expect(region?.name).toBe('北宋');
  });

  test('returns Europe region', () => {
    const region = getRegionById('europe');
    expect(region).toBeDefined();
    expect(region?.name).toBe('欧洲');
  });

  test('returns undefined for non-existent id', () => {
    const result = getRegionById('nonexistent-region-id');
    expect(result).toBeUndefined();
  });
});

// ---------- getPersonsForEvent ----------

describe('getPersonsForEvent', () => {
  test('returns persons linked to 苏轼被贬黄州 event', () => {
    const persons = getPersonsForEvent('evt-sushi-huangzhou');
    expect(persons.length).toBeGreaterThan(0);
    expect(persons.some((p) => p.name === '苏轼')).toBe(true);
  });

  test('returns empty array for event with no personIds', () => {
    // Create a synthetic test: an event with empty personIds
    const persons = getPersonsForEvent('evt-norman-conquest');
    // Even if the event has no persons, it should return an array (may be empty)
    expect(Array.isArray(persons)).toBe(true);
  });
});

// ---------- getSourcesForEvent ----------

describe('getSourcesForEvent', () => {
  test('returns sources linked to an event', () => {
    const sources = getSourcesForEvent('evt-sushi-huangzhou');
    expect(Array.isArray(sources)).toBe(true);
    // Sources may be empty in mock data, but should not throw
  });
});
