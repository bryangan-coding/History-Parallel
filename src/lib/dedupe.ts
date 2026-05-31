/**
 * Data deduplication utilities.
 * Detects potential duplicate persons and events for human review.
 * Never auto-merges or deletes — only flags candidates.
 */

import type { Person, HistoricalEvent } from './types';

export interface DuplicateCandidate<T> {
  item: T;
  score: number;
  reasons: string[];
}

/**
 * Calculate string similarity using Dice coefficient.
 * Returns 0–1, where 1 means identical.
 */
export function calculateNameSimilarity(a: string, b: string): number {
  if (a === b) return 1;
  if (!a || !b) return 0;

  const normalize = (s: string) =>
    s
      .toLowerCase()
      .trim()
      .replace(/\s+/g, ' ')
      .replace(/[^\w\u4e00-\u9fff ]/g, '');

  const na = normalize(a);
  const nb = normalize(b);

  // Exact match after normalization
  if (na === nb) return 0.95;

  // Token overlap
  const tokensA = new Set(na.split(' ').filter(Boolean));
  const tokensB = new Set(nb.split(' ').filter(Boolean));

  if (tokensA.size === 0 || tokensB.size === 0) {
    // For CJK names, use character overlap
    if (na === nb) return 1;
    const charsA = new Set(na.split(''));
    const charsB = new Set(nb.split(''));
    if (charsA.size === 0 || charsB.size === 0) return 0;
    const intersection = new Set([...charsA].filter((c) => charsB.has(c)));
    const union = new Set([...charsA, ...charsB]);
    return intersection.size / union.size;
  }

  const intersection = new Set([...tokensA].filter((t) => tokensB.has(t)));
  const union = new Set([...tokensA, ...tokensB]);
  return intersection.size / union.size;
}

/**
 * Calculate event title similarity using the same approach.
 */
export function calculateEventTitleSimilarity(a: string, b: string): number {
  return calculateNameSimilarity(a, b);
}

/**
 * Find potential duplicate persons from an existing list.
 * Weights multiple signals to compute a similarity score.
 */
export function findPotentialDuplicatePersons(
  person: Person,
  existingPersons: Person[],
): DuplicateCandidate<Person>[] {
  const candidates: DuplicateCandidate<Person>[] = [];

  for (const existing of existingPersons) {
    if (existing.id === person.id) continue;

    let score = 0;
    const reasons: string[] = [];

    // 1. Same Wikidata QID (strongest signal)
    if (person.wikidataQid && existing.wikidataQid && person.wikidataQid === existing.wikidataQid) {
      score += 1.0;
      reasons.push('Same Wikidata QID');
    }

    // 2. Name similarity
    const nameSim = calculateNameSimilarity(person.name, existing.name);
    if (nameSim > 0.9) {
      score += 0.5;
      reasons.push('Nearly identical names');
    } else if (nameSim > 0.7) {
      score += 0.3;
      reasons.push('Similar names');
    }

    // 3. Alternative names overlap
    const altOverlap = person.alternativeNames.filter((a) =>
      existing.alternativeNames.some(
        (b) => calculateNameSimilarity(a, b) > 0.8
      ),
    );
    if (altOverlap.length > 0) {
      score += 0.2 * altOverlap.length;
      reasons.push('Overlapping alternative names');
    }

    // 4. Birth/death years close
    if (
      person.birthYear !== undefined &&
      existing.birthYear !== undefined
    ) {
      const birthDiff = Math.abs(person.birthYear - existing.birthYear);
      if (birthDiff <= 2) {
        score += 0.2;
        reasons.push('Birth years within 2 years');
      } else if (birthDiff <= 10) {
        score += 0.1;
        reasons.push('Birth years within 10 years');
      }
    }

    if (
      person.deathYear !== undefined &&
      existing.deathYear !== undefined
    ) {
      const deathDiff = Math.abs(person.deathYear - existing.deathYear);
      if (deathDiff <= 2) {
        score += 0.2;
        reasons.push('Death years within 2 years');
      } else if (deathDiff <= 10) {
        score += 0.1;
        reasons.push('Death years within 10 years');
      }
    }

    // 5. Same region
    if (person.regionId && existing.regionId && person.regionId === existing.regionId) {
      score += 0.15;
      reasons.push('Same region');
    }

    // 6. Overlapping occupations
    const occOverlap = person.occupations.filter((o) =>
      existing.occupations.includes(o),
    );
    if (occOverlap.length > 0) {
      score += 0.1 * Math.min(occOverlap.length, 3);
      reasons.push('Overlapping occupations');
    }

    // Only add if score threshold met
    if (score >= 0.3) {
      candidates.push({ item: existing, score: Math.min(score, 1), reasons });
    }
  }

  return candidates.sort((a, b) => b.score - a.score);
}

/**
 * Find potential duplicate events from an existing list.
 */
export function findPotentialDuplicateEvents(
  event: HistoricalEvent,
  existingEvents: HistoricalEvent[],
): DuplicateCandidate<HistoricalEvent>[] {
  const candidates: DuplicateCandidate<HistoricalEvent>[] = [];

  for (const existing of existingEvents) {
    if (existing.id === event.id) continue;

    let score = 0;
    const reasons: string[] = [];

    // 1. Same Wikidata QID
    if (event.wikidataQid && existing.wikidataQid && event.wikidataQid === existing.wikidataQid) {
      score += 1.0;
      reasons.push('Same Wikidata QID');
    }

    // 2. Title similarity
    const titleSim = calculateEventTitleSimilarity(event.title, existing.title);
    if (titleSim > 0.9) {
      score += 0.4;
      reasons.push('Nearly identical titles');
    } else if (titleSim > 0.7) {
      score += 0.25;
      reasons.push('Similar titles');
    }

    // 3. Start year close
    if (
      event.startYear !== undefined &&
      existing.startYear !== undefined
    ) {
      const yearDiff = Math.abs(event.startYear - existing.startYear);
      if (yearDiff <= 2) {
        score += 0.25;
        reasons.push('Start years within 2 years');
      } else if (yearDiff <= 10) {
        score += 0.15;
        reasons.push('Start years within 10 years');
      }
    }

    // 4. End year close
    if (
      event.endYear !== undefined &&
      existing.endYear !== undefined
    ) {
      const yearDiff = Math.abs(event.endYear - existing.endYear);
      if (yearDiff <= 2) {
        score += 0.15;
        reasons.push('End years within 2 years');
      }
    }

    // 5. Same region
    if (event.regionId && existing.regionId && event.regionId === existing.regionId) {
      score += 0.15;
      reasons.push('Same region');
    }

    // 6. Similar place names
    if (
      event.placeName &&
      existing.placeName &&
      calculateNameSimilarity(event.placeName, existing.placeName) > 0.7
    ) {
      score += 0.15;
      reasons.push('Similar place names');
    }

    // 7. Overlapping person IDs
    const personOverlap = event.personIds.filter((pid) =>
      existing.personIds.includes(pid),
    );
    if (personOverlap.length > 0) {
      score += 0.1 * personOverlap.length;
      reasons.push('Shared related persons');
    }

    // 8. Overlapping tags
    const tagOverlap = event.tags.filter((t) => existing.tags.includes(t));
    if (tagOverlap.length > 0) {
      score += 0.05 * Math.min(tagOverlap.length, 4);
      reasons.push('Shared tags');
    }

    if (score >= 0.3) {
      candidates.push({ item: existing, score: Math.min(score, 1), reasons });
    }
  }

  return candidates.sort((a, b) => b.score - a.score);
}
