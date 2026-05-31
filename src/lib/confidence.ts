/**
 * Confidence scoring utilities.
 * Calculates data quality scores (0–1) for persons and events
 * based on completeness and source quality.
 */

import type { Person, HistoricalEvent } from './types';

/**
 * Calculate confidence score for a Person (0–1, rounded to 2 decimals).
 */
export function calculatePersonConfidenceScore(person: Person): number {
  let score = 0.3; // Base score

  // Bonus factors
  if (person.wikidataQid) score += 0.15;
  if (person.externalReferences.length > 0) {
    score += 0.05 * Math.min(person.externalReferences.length, 3);
  }
  if (person.birthYear !== undefined && person.deathYear !== undefined) {
    score += 0.1;
  } else if (person.birthYear !== undefined || person.deathYear !== undefined) {
    score += 0.05;
  }
  if (person.regionId) score += 0.05;
  if (person.occupations.length > 0) score += 0.05;
  if (person.summary && person.summary.trim().length > 20) score += 0.1;
  if (person.sourceIds.length > 0) score += 0.1;

  // Penalty factors
  if (person.sourceIds.length === 0 && person.externalReferences.length === 0) score -= 0.2;
  if (person.birthYear === undefined && person.deathYear === undefined) score -= 0.1;
  if (!person.summary || person.summary.trim().length === 0) score -= 0.15;
  if (person.sourceIds.length === 1 && person.externalReferences.length === 0) score -= 0.05;
  if (
    person.birthDatePrecision === 'century' ||
    person.birthDatePrecision === 'unknown' ||
    person.deathDatePrecision === 'century' ||
    person.deathDatePrecision === 'unknown'
  ) {
    score -= 0.05;
  }

  return clampScore(score);
}

/**
 * Calculate confidence score for a HistoricalEvent (0–1, rounded to 2 decimals).
 */
export function calculateEventConfidenceScore(event: HistoricalEvent): number {
  let score = 0.3; // Base score

  // Bonus factors
  if (event.wikidataQid) score += 0.15;
  if (event.externalReferences.length > 0) {
    score += 0.05 * Math.min(event.externalReferences.length, 3);
  }
  if (event.startYear !== undefined) {
    score += 0.1;
    if (event.datePrecision === 'day' || event.datePrecision === 'month') {
      score += 0.05;
    }
  }
  if (event.regionId || event.placeName) score += 0.05;
  if (event.personIds.length > 0) score += 0.05;
  if (event.summary && event.summary.trim().length > 20) score += 0.1;
  if (event.sourceIds.length > 0) score += 0.1;
  if (event.importance >= 4) score += 0.05;

  // Penalty factors
  if (event.sourceIds.length === 0 && event.externalReferences.length === 0) score -= 0.2;
  if (event.startYear === undefined) score -= 0.15;
  if (!event.regionId && !event.placeName) score -= 0.1;
  if (!event.summary || event.summary.trim().length === 0) score -= 0.15;
  if (event.personIds.length === 0 && event.importance < 4) score -= 0.05;

  return clampScore(score);
}

function clampScore(score: number): number {
  return Math.round(Math.max(0, Math.min(1, score)) * 100) / 100;
}
