/**
 * Historical date precision utilities.
 * Handles parsing, normalization, formatting, and comparisons
 * of dates with varying levels of precision.
 */

import type { DatePrecision, HistoricalEvent } from './types';

/** Parsed date components from a Wikidata-style time value */
interface ParsedTimeValue {
  year?: number;
  month?: number;
  day?: number;
  precision: DatePrecision;
  isApproximate: boolean;
  displayText: string;
}

/**
 * Parse a Wikidata-style time value string (e.g., "+1080-00-00T00:00:00Z/9").
 * Returns structured date components with precision level.
 */
export function parseWikidataTimeValue(input: string): ParsedTimeValue {
  if (!input || typeof input !== 'string') {
    return {
      precision: 'unknown',
      isApproximate: true,
      displayText: '时间不详',
    };
  }

  // Common Wikidata format: +YYYY-MM-DDT00:00:00Z/PRECISION
  const match = input.match(/^([+-]?\d{4,})-(\d{2})-(\d{2})T.*\/(\d+)$/);
  if (!match) {
    return {
      precision: 'unknown',
      isApproximate: true,
      displayText: input,
    };
  }

  const year = parseInt(match[1], 10);
  const month = parseInt(match[2], 10);
  const day = parseInt(match[3], 10);
  const precisionNum = parseInt(match[4], 10);

  let precision: DatePrecision;
  switch (precisionNum) {
    case 11: precision = 'day'; break;
    case 10: precision = 'month'; break;
    case 9: precision = 'year'; break;
    case 8: precision = 'decade'; break;
    case 7: precision = 'century'; break;
    case 6: precision = 'century'; break;
    default: precision = 'year'; break;
  }

  const isApproximate = precisionNum <= 8;

  let displayText: string;
  const absYear = Math.abs(year);
  const bc = year < 0 ? 'BC ' : '';
  switch (precision) {
    case 'day':
      displayText = `${bc}${absYear}-${month}-${day}`;
      break;
    case 'month':
      displayText = `${bc}${absYear}-${month}`;
      break;
    case 'year':
      displayText = `${bc}${absYear}`;
      break;
    case 'decade':
      displayText = `${bc}${absYear}s`;
      break;
    case 'century':
      displayText = `${bc}${Math.ceil(absYear / 100)}th century`;
      break;
    default:
      displayText = input;
  }

  return {
    year: month > 0 ? year : year,  // Only treat as known if month/day are non-zero
    month: month > 0 ? month : undefined,
    day: day > 0 ? day : undefined,
    precision,
    isApproximate,
    displayText,
  };
}

/**
 * Normalize a historical year from various input formats.
 * Returns undefined if input cannot be parsed.
 */
export function normalizeHistoricalYear(input: string | number | undefined): number | undefined {
  if (input === undefined || input === null) return undefined;
  if (typeof input === 'number') return input;

  const s = input.trim();

  // "11世纪" -> 1001 (century start) — check BEFORE plain parseInt
  const centuryMatch = s.match(/^[-]?\d+\s*世[纪紀]/);
  if (centuryMatch) {
    const century = parseInt(centuryMatch[0], 10);
    return century < 0 ? (century + 1) * 100 : (century - 1) * 100 + 1;
  }

  // Try direct number parse
  const n = parseInt(s, 10);
  if (!isNaN(n)) return n;

  // "约1048年" -> 1048 (approximate)
  const approxMatch = s.match(/约?\s*(公元前\s*)?\s*(-?\d+)/);
  if (approxMatch) {
    const num = parseInt(approxMatch[2] ?? approxMatch[1], 10);
    const isBC = (approxMatch[1] ?? '').includes('公元前');
    return isBC ? -num : num;
  }

  // BC years: "公元前221年" -> -221
  const bcMatch = s.match(/公元前\s*(\d+)/);
  if (bcMatch) return -parseInt(bcMatch[1], 10);

  return undefined;
}

/**
 * Format an approximate date range for display.
 * Examples:
 *   - "1080"
 *   - "约 1080 年"
 *   - "11 世纪"
 *   - "1080–1084"
 *   - "时间不详"
 */
export function formatApproximateDate(params: {
  startYear?: number;
  endYear?: number;
  precision: DatePrecision;
  isApproximate?: boolean;
  fallbackText?: string;
}): string {
  const { startYear, endYear, precision, isApproximate = false, fallbackText = '时间不详' } = params;

  if (startYear === undefined && endYear === undefined) {
    return fallbackText;
  }

  const prefix = isApproximate ? '约 ' : '';
  const suffix = ' 年';

  switch (precision) {
    case 'century':
      if (startYear !== undefined) {
        const century = Math.ceil(Math.abs(startYear) / 100);
        const bc = startYear < 0 ? '公元前' : '';
        return `${bc}${century} 世纪`;
      }
      return fallbackText;

    case 'decade':
      if (startYear !== undefined) {
        const decade = Math.floor(Math.abs(startYear) / 10) * 10;
        return `${prefix}${decade}${suffix}代`;
      }
      return fallbackText;

    case 'range':
      if (startYear !== undefined && endYear !== undefined && startYear !== endYear) {
        return `${startYear}${suffix}–${endYear}${suffix}`;
      }
      // Fall through to year format
      return startYear !== undefined ? `${startYear}${suffix}` : fallbackText;

    case 'year':
    case 'month':
    case 'day':
    default:
      return startYear !== undefined ? `${prefix}${startYear}${suffix}` : fallbackText;
  }
}

/**
 * Calculate the distance between a target year and an event's time range.
 * Returns the minimum distance from the target year to any point in the event's range.
 */
export function getYearDistance(targetYear: number, event: HistoricalEvent): number {
  const start = event.startYear ?? targetYear;
  const end = event.endYear ?? start;

  if (targetYear >= start && targetYear <= end) return 0;
  if (targetYear < start) return start - targetYear;
  return targetYear - end;
}

/**
 * Check if a historical event overlaps with a given year range.
 */
export function doesEventOverlapRange(
  event: HistoricalEvent,
  rangeStartYear: number,
  rangeEndYear: number,
): boolean {
  const eventStart = event.startYear ?? rangeStartYear;
  const eventEnd = event.endYear ?? eventStart;

  return (
    (eventStart >= rangeStartYear && eventStart <= rangeEndYear) ||
    (eventEnd >= rangeStartYear && eventEnd <= rangeEndYear) ||
    (eventStart <= rangeStartYear && eventEnd >= rangeEndYear)
  );
}
