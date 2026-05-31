/**
 * Data validation utilities.
 * Validates Person and HistoricalEvent entities against quality rules.
 */

import type { Person, HistoricalEvent, DataStatus } from './types';

export interface ValidationIssue {
  level: 'error' | 'warning';
  field?: string;
  message: string;
}

/**
 * Validate a Person entity.
 * Returns a list of issues. Warnings don't block publishing;
 * errors must be resolved before publishing.
 */
export function validatePerson(person: Person): ValidationIssue[] {
  const issues: ValidationIssue[] = [];

  // name must not be empty
  if (!person.name || person.name.trim().length === 0) {
    issues.push({ level: 'error', field: 'name', message: 'Name cannot be empty' });
  }

  // birthYear should not be later than deathYear
  if (
    person.birthYear !== undefined &&
    person.deathYear !== undefined &&
    person.birthYear > person.deathYear
  ) {
    issues.push({
      level: 'error',
      field: 'birthYear',
      message: `Birth year (${person.birthYear}) is later than death year (${person.deathYear})`,
    });
  }

  // published status requires summary
  if (person.dataStatus === 'published' && (!person.summary || person.summary.trim().length === 0)) {
    issues.push({
      level: 'error',
      field: 'summary',
      message: 'Published persons must have a summary',
    });
  }

  // published status requires at least one source
  if (
    person.dataStatus === 'published' &&
    person.sourceIds.length === 0 &&
    person.externalReferences.length === 0
  ) {
    issues.push({
      level: 'error',
      field: 'sourceIds',
      message: 'Published persons must have at least one source or external reference',
    });
  }

  // published status requires confidence >= 0.7
  if (person.dataStatus === 'published' && person.confidenceScore < 0.7) {
    issues.push({
      level: 'error',
      field: 'confidenceScore',
      message: `Published persons require confidenceScore >= 0.7 (current: ${person.confidenceScore.toFixed(2)})`,
    });
  }

  // Warnings for imported/review data
  if (!person.summary || person.summary.trim().length === 0) {
    issues.push({
      level: 'warning',
      field: 'summary',
      message: 'Person has no summary',
    });
  }

  if (person.sourceIds.length === 0 && person.externalReferences.length === 0) {
    issues.push({
      level: 'warning',
      field: 'sourceIds',
      message: 'Person has no sources or external references',
    });
  }

  if (person.birthYear === undefined && person.deathYear === undefined) {
    issues.push({
      level: 'warning',
      field: 'birthYear',
      message: 'Person has no birth or death year',
    });
  }

  if (!person.regionId) {
    issues.push({
      level: 'warning',
      field: 'regionId',
      message: 'Person has no region',
    });
  }

  return issues;
}

/**
 * Validate a HistoricalEvent entity.
 */
export function validateHistoricalEvent(
  event: HistoricalEvent,
  persons?: Person[],
): ValidationIssue[] {
  const issues: ValidationIssue[] = [];

  // title must not be empty
  if (!event.title || event.title.trim().length === 0) {
    issues.push({ level: 'error', field: 'title', message: 'Title cannot be empty' });
  }

  // startYear should not be later than endYear
  if (
    event.startYear !== undefined &&
    event.endYear !== undefined &&
    event.startYear > event.endYear
  ) {
    issues.push({
      level: 'error',
      field: 'startYear',
      message: `Start year (${event.startYear}) is later than end year (${event.endYear})`,
    });
  }

  // Event must have at least regionId or placeName
  if (!event.regionId && !event.placeName) {
    issues.push({
      level: 'warning',
      field: 'regionId',
      message: 'Event has no region or place name',
    });
  }

  // published status requires summary
  if (event.dataStatus === 'published' && (!event.summary || event.summary.trim().length === 0)) {
    issues.push({
      level: 'error',
      field: 'summary',
      message: 'Published events must have a summary',
    });
  }

  // published status requires at least one source
  if (
    event.dataStatus === 'published' &&
    event.sourceIds.length === 0 &&
    event.externalReferences.length === 0
  ) {
    issues.push({
      level: 'error',
      field: 'sourceIds',
      message: 'Published events must have at least one source or external reference',
    });
  }

  // published status requires confidence >= 0.7
  if (event.dataStatus === 'published' && event.confidenceScore < 0.7) {
    issues.push({
      level: 'error',
      field: 'confidenceScore',
      message: `Published events require confidenceScore >= 0.7 (current: ${event.confidenceScore.toFixed(2)})`,
    });
  }

  // Warning: event year outside related persons' lifespan
  if (persons && persons.length > 0 && event.startYear !== undefined) {
    for (const p of persons) {
      if (
        p.birthYear !== undefined &&
        p.deathYear !== undefined &&
        (event.startYear < p.birthYear - 5 || event.startYear > p.deathYear + 5)
      ) {
        issues.push({
          level: 'warning',
          field: 'startYear',
          message: `Event year (${event.startYear}) is outside lifespan of related person "${p.name}" (${p.birthYear}–${p.deathYear})`,
        });
      }
    }
  }

  // Warnings
  if (!event.summary || event.summary.trim().length === 0) {
    issues.push({
      level: 'warning',
      field: 'summary',
      message: 'Event has no summary',
    });
  }

  if (event.datePrecision === 'unknown') {
    issues.push({
      level: 'warning',
      field: 'datePrecision',
      message: 'Event date precision is unknown',
    });
  }

  return issues;
}

/**
 * Check if a Person can be published.
 * Returns ok: true only if there are no error-level issues.
 */
export function canPublishPerson(person: Person): {
  ok: boolean;
  issues: ValidationIssue[];
} {
  const issues = validatePerson(person);
  const errors = issues.filter((i) => i.level === 'error');
  return { ok: errors.length === 0, issues };
}

/**
 * Check if a HistoricalEvent can be published.
 */
export function canPublishEvent(
  event: HistoricalEvent,
  persons?: Person[],
): {
  ok: boolean;
  issues: ValidationIssue[];
} {
  const issues = validateHistoricalEvent(event, persons);
  const errors = issues.filter((i) => i.level === 'error');
  return { ok: errors.length === 0, issues };
}
