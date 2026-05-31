import {
  normalizePersonName,
  normalizeEventTitle,
  normalizeRegionName,
  normalizeTags,
  createSlug,
} from '../normalization';
import type { ExternalReference } from '../types';

describe('normalizePersonName', () => {
  test('trims whitespace', () => {
    expect(normalizePersonName('  苏轼  ')).toBe('苏轼');
  });

  test('normalizes multiple spaces to single space', () => {
    expect(normalizePersonName('William   the   Conqueror')).toBe('William the Conqueror');
  });

  test('returns empty string for empty input', () => {
    expect(normalizePersonName('')).toBe('');
  });
});

describe('normalizeEventTitle', () => {
  test('trims whitespace', () => {
    expect(normalizeEventTitle('  诺曼征服英格兰  ')).toBe('诺曼征服英格兰');
  });

  test('normalizes spaces', () => {
    expect(normalizeEventTitle('Battle  of   Hastings')).toBe('Battle of Hastings');
  });
});

describe('normalizeRegionName', () => {
  test('trims whitespace', () => {
    expect(normalizeRegionName('  北宋  ')).toBe('北宋');
  });
});

describe('normalizeTags', () => {
  test('deduplicates tags', () => {
    expect(normalizeTags(['文学', '文学', '北宋'])).toEqual(['北宋', '文学']);
  });

  test('filters empty tags', () => {
    expect(normalizeTags(['文学', '', '  ', '北宋'])).toEqual(['北宋', '文学']);
  });

  test('returns empty array for empty input', () => {
    expect(normalizeTags([])).toEqual([]);
  });

  test('sorts alphabetically', () => {
    expect(normalizeTags(['C', 'A', 'B'])).toEqual(['A', 'B', 'C']);
  });
});

describe('createSlug', () => {
  test('creates slug from English', () => {
    expect(createSlug('History Parallel')).toBe('history-parallel');
  });

  test('creates slug from Chinese', () => {
    expect(createSlug('历史平行线')).toBe('历史平行线');
  });

  test('handles mixed content', () => {
    const slug = createSlug('Song Dynasty 北宋');
    expect(slug).toContain('song');
    expect(slug).toContain('dynasty');
  });

  test('truncates long slugs', () => {
    const long = 'a'.repeat(100);
    const slug = createSlug(long);
    expect(slug.length).toBeLessThanOrEqual(80);
  });
});
