import {
  parseWikidataTimeValue,
  normalizeHistoricalYear,
  formatApproximateDate,
  getYearDistance,
  doesEventOverlapRange,
} from '../datePrecision';
import type { HistoricalEvent } from '../types';

function makeEvent(overrides: Partial<HistoricalEvent> = {}): HistoricalEvent {
  return {
    id: 'test-event',
    title: 'Test Event',
    startYear: 1080,
    datePrecision: 'year',
    isApproximate: false,
    personIds: [],
    tags: [],
    importance: 3,
    sourceIds: [],
    relatedEventIds: [],
    dataStatus: 'published',
    confidenceScore: 0.8,
    externalReferences: [],
    ...overrides,
  };
}

describe('parseWikidataTimeValue', () => {
  test('parses a standard Wikidata year value', () => {
    const result = parseWikidataTimeValue('+1080-00-00T00:00:00Z/9');
    expect(result.year).toBe(1080);
    expect(result.precision).toBe('year');
    expect(result.isApproximate).toBe(false);
  });

  test('returns unknown for empty input', () => {
    const result = parseWikidataTimeValue('');
    expect(result.precision).toBe('unknown');
    expect(result.isApproximate).toBe(true);
    expect(result.displayText).toBe('时间不详');
  });

  test('returns unknown for non-string input', () => {
    const result = parseWikidataTimeValue('not-a-wikidata-value');
    expect(result.precision).toBe('unknown');
  });

  test('handles BC dates', () => {
    const result = parseWikidataTimeValue('-0221-00-00T00:00:00Z/9');
    expect(result.year).toBe(-221);
  });
});

describe('normalizeHistoricalYear', () => {
  test('returns number as-is', () => {
    expect(normalizeHistoricalYear(1080)).toBe(1080);
  });

  test('parses numeric string', () => {
    expect(normalizeHistoricalYear('1080')).toBe(1080);
  });

  test('parses Chinese year format', () => {
    expect(normalizeHistoricalYear('约1048年')).toBe(1048);
  });

  test('parses BC years', () => {
    const result = normalizeHistoricalYear('公元前221年');
    expect(result).toBe(-221);
  });

  test('parses century format', () => {
    const result = normalizeHistoricalYear('11世纪');
    expect(result).toBe(1001);
  });

  test('returns undefined for unparseable input', () => {
    expect(normalizeHistoricalYear('未知')).toBeUndefined();
    expect(normalizeHistoricalYear(undefined)).toBeUndefined();
  });
});

describe('formatApproximateDate', () => {
  test('formats a precise year', () => {
    const result = formatApproximateDate({ startYear: 1080, precision: 'year' });
    expect(result).toBe('1080 年');
  });

  test('formats an approximate year', () => {
    const result = formatApproximateDate({ startYear: 1080, precision: 'year', isApproximate: true });
    expect(result).toBe('约 1080 年');
  });

  test('formats a century', () => {
    const result = formatApproximateDate({ startYear: 1001, precision: 'century' });
    expect(result).toBe('11 世纪');
  });

  test('formats a year range', () => {
    const result = formatApproximateDate({ startYear: 1069, endYear: 1085, precision: 'range' });
    expect(result).toBe('1069 年–1085 年');
  });

  test('returns fallback text for unknown dates', () => {
    const result = formatApproximateDate({ precision: 'unknown' });
    expect(result).toBe('时间不详');
  });

  test('returns custom fallback text', () => {
    const result = formatApproximateDate({ precision: 'unknown', fallbackText: 'N/A' });
    expect(result).toBe('N/A');
  });
});

describe('getYearDistance', () => {
  test('returns 0 for event spanning target year', () => {
    const event = makeEvent({ startYear: 1069, endYear: 1085 });
    expect(getYearDistance(1080, event)).toBe(0);
  });

  test('returns distance when event is before target year', () => {
    const event = makeEvent({ startYear: 1000, endYear: 1010 });
    expect(getYearDistance(1080, event)).toBe(70);
  });

  test('returns distance when event is after target year', () => {
    const event = makeEvent({ startYear: 1100, endYear: 1110 });
    expect(getYearDistance(1080, event)).toBe(20);
  });

  test('uses startYear when endYear is undefined', () => {
    const event = makeEvent({ startYear: 1075, endYear: undefined });
    expect(getYearDistance(1080, event)).toBe(5);
  });
});

describe('doesEventOverlapRange', () => {
  test('event fully inside range returns true', () => {
    const event = makeEvent({ startYear: 1070, endYear: 1080 });
    expect(doesEventOverlapRange(event, 1060, 1090)).toBe(true);
  });

  test('event spanning range returns true', () => {
    const event = makeEvent({ startYear: 1060, endYear: 1100 });
    expect(doesEventOverlapRange(event, 1070, 1080)).toBe(true);
  });

  test('event outside range returns false', () => {
    const event = makeEvent({ startYear: 1000, endYear: 1010 });
    expect(doesEventOverlapRange(event, 1070, 1080)).toBe(false);
  });
});
