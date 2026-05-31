/** Lightweight date utilities for handling historical dates */

const BC_PREFIX = '公元前';

/**
 * Format a year for display. Negative numbers are treated as BC.
 */
export function formatYear(year: number): string {
  if (year < 0) {
    return `${BC_PREFIX}${Math.abs(year)}年`;
  }
  return `${year}年`;
}

/**
 * Format a year range for display.
 */
export function formatYearRange(startYear: number | undefined, endYear?: number): string {
  const start = startYear ?? 0;
  if (!endYear || start === endYear) {
    return formatYear(start);
  }
  return `${formatYear(start)} — ${formatYear(endYear)}`;
}

/**
 * Format a person's birth/death years as a string like "1037年 — 1101年" or "1037年 — 1101年（北宋）"
 */
export function formatLifespan(
  birthYear: number | undefined,
  deathYear: number | undefined,
): string {
  const birth = birthYear ?? 0;
  const death = deathYear ?? 0;
  return `${formatYear(birth)} — ${formatYear(death)}`;
}

/**
 * Calculate age at a given year.
 * Returns undefined if the year is outside the person's lifespan.
 */
export function ageAt(personBirth: number, personDeath: number, year: number): number | undefined {
  if (year < personBirth || year > personDeath) return undefined;
  return year - personBirth;
}
