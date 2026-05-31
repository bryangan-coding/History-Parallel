/**
 * Tests for date utilities (formatYear, formatYearRange, formatLifespan, ageAt)
 */
import {
  formatYear,
  formatYearRange,
  formatLifespan,
  ageAt,
} from '@/lib/date';

describe('formatYear', () => {
  test('formats positive year with "年" suffix', () => {
    expect(formatYear(1080)).toBe('1080年');
    expect(formatYear(2024)).toBe('2024年');
    expect(formatYear(1)).toBe('1年');
  });

  test('formats negative year as BC with "公元前" prefix', () => {
    expect(formatYear(-551)).toBe('公元前551年'); // Confucius
    expect(formatYear(-1)).toBe('公元前1年');
  });

  test('handles year 0 if needed', () => {
    // Year 0 is not historically used; our function treats it as positive
    expect(formatYear(0)).toBe('0年');
  });
});

describe('formatYearRange', () => {
  test('returns single year when endYear is omitted', () => {
    expect(formatYearRange(1080)).toBe('1080年');
  });

  test('returns year range when startYear equals endYear', () => {
    expect(formatYearRange(1080, 1080)).toBe('1080年');
  });

  test('returns formatted range when startYear != endYear', () => {
    expect(formatYearRange(1069, 1085)).toBe('1069年 — 1085年');
    expect(formatYearRange(-551, -479)).toBe('公元前551年 — 公元前479年');
  });

  test('handles BC to AD transition', () => {
    expect(formatYearRange(-1, 1)).toBe('公元前1年 — 1年');
  });
});

describe('formatLifespan', () => {
  test('formats birth and death years', () => {
    expect(formatLifespan(1037, 1101)).toBe('1037年 — 1101年');
    expect(formatLifespan(-551, -479)).toBe('公元前551年 — 公元前479年');
  });
});

describe('ageAt', () => {
  test('calculates age correctly when year is within lifespan', () => {
    expect(ageAt(1037, 1101, 1080)).toBe(43); // Su Shi at Huangzhou
    expect(ageAt(1037, 1101, 1037)).toBe(0);  // birth year
    expect(ageAt(1037, 1101, 1101)).toBe(64); // death year
  });

  test('returns undefined when year is before birth', () => {
    expect(ageAt(1037, 1101, 1000)).toBeUndefined();
  });

  test('returns undefined when year is after death', () => {
    expect(ageAt(1037, 1101, 1200)).toBeUndefined();
  });

  test('handles BC lifespans', () => {
    expect(ageAt(-551, -479, -500)).toBe(51);
    expect(ageAt(-551, -479, -551)).toBe(0);
    expect(ageAt(-551, -479, -600)).toBeUndefined();
    expect(ageAt(-551, -479, -400)).toBeUndefined();
  });
});
