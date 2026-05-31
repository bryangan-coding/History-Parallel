/**
 * Tests for search function (searchEntities equivalent)
 * Covers: Chinese name, English alias, event title, year, non-existent query
 */
import { search } from '@/lib/search';
import { people, events } from '@/data/mockData';

describe('search — Chinese person name', () => {
  test('finds 苏轼 by full name', () => {
    const result = search('苏轼');
    expect(result.people.length).toBeGreaterThan(0);
    expect(result.people[0]?.name).toBe('苏轼');
  });

  test('finds 王安石 by full name', () => {
    const result = search('王安石');
    expect(result.people.length).toBeGreaterThan(0);
    expect(result.people[0]?.name).toBe('王安石');
  });

  test('returns 苏轼 first for higher relevance score', () => {
    const result = search('苏轼');
    const names = result.people.map((p) => p.name);
    expect(names[0]).toBe('苏轼');
  });
});

describe('search — English alias / alternative name', () => {
  test('finds 苏轼 by English name "Su Shi"', () => {
    const result = search('Su Shi');
    expect(result.people.some((p) => p.name === '苏轼')).toBe(true);
  });

  test('finds 欧阳修 by English name "Ouyang Xiu"', () => {
    const result = search('Ouyang Xiu');
    expect(result.people.some((p) => p.name === '欧阳修')).toBe(true);
  });

  test('finds William I by English name "William the Conqueror"', () => {
    const result = search('William the Conqueror');
    expect(result.people.some((p) => p.nameEn === 'William I (the Conqueror)')).toBe(true);
  });
});

describe('search — event title', () => {
  test('finds 乌台诗案 by title', () => {
    const result = search('乌台诗案');
    expect(result.events.length).toBeGreaterThan(0);
    expect(result.events[0]?.title).toContain('乌台诗案');
  });

  test('finds 诺曼征服 by title', () => {
    const result = search('诺曼征服');
    expect(result.events.length).toBeGreaterThan(0);
  });

  test('finds event by English title', () => {
    const result = search('Crow Terrace Poetry Trial');
    expect(result.events.some((e) => e.titleEn === 'The Crow Terrace Poetry Trial')).toBe(true);
  });
});

describe('search — year number', () => {
  test('returns year match for 1080', () => {
    const result = search('1080');
    expect(result.yearMatches.length).toBeGreaterThan(0);
    expect(result.yearMatches[0]?.year).toBe(1080);
  });

  test('returns year match for 1066 (Norman Conquest)', () => {
    const result = search('1066');
    expect(result.yearMatches.length).toBeGreaterThan(0);
    expect(result.yearMatches[0]?.year).toBe(1066);
  });

  test('returns empty yearMatches for out-of-range year', () => {
    const result = search('3000');
    expect(result.yearMatches).toEqual([]);
  });

  test('returns events within ±20 years of the query year', () => {
    const result = search('1080');
    const near = result.yearMatches[0]?.nearEvents ?? [];
    // All returned events should be within ±20 years of 1080
    for (const evt of near) {
      const start = evt.startYear;
      const end = evt.endYear ?? start;
      const overlaps =
        Math.abs(start - 1080) <= 20 ||
        Math.abs(end - 1080) <= 20 ||
        (start <= 1080 && end >= 1080);
      expect(overlaps).toBe(true);
    }
  });
});

describe('search — non-existent query', () => {
  test('returns empty arrays for gibberish query', () => {
    const result = search('xyznonexistent123');
    expect(result.people).toEqual([]);
    expect(result.events).toEqual([]);
    expect(result.regions).toEqual([]);
    expect(result.yearMatches).toEqual([]);
  });

  test('returns empty arrays for empty string', () => {
    const result = search('');
    expect(result.people).toEqual([]);
    expect(result.events).toEqual([]);
    expect(result.regions).toEqual([]);
    expect(result.yearMatches).toEqual([]);
  });

  test('returns empty arrays for whitespace-only string', () => {
    const result = search('   ');
    expect(result.people).toEqual([]);
    expect(result.events).toEqual([]);
  });
});

describe('search — region name', () => {
  test('finds 中国 by name', () => {
    const result = search('中国');
    expect(result.regions.length).toBeGreaterThan(0);
  });

  test('finds Europe by English name', () => {
    const result = search('Europe');
    expect(result.regions.length).toBeGreaterThan(0);
  });
});

describe('search — tag matching', () => {
  test('finds 苏轼 by tag "文学家"', () => {
    const result = search('文学家');
    expect(result.people.some((p) => p.name === '苏轼')).toBe(true);
  });

  test('finds 王安石 by tag "改革家"', () => {
    const result = search('改革家');
    expect(result.people.some((p) => p.name === '王安石')).toBe(true);
  });
});
