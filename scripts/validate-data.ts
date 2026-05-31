#!/usr/bin/env tsx
/**
 * Data validation script.
 * Reads all data from imported/, review/, published/ directories,
 * runs validation rules, and outputs a report.
 *
 * Usage: npm run validate:data
 */

import {
  validatePerson,
  validateHistoricalEvent,
  canPublishPerson,
  canPublishEvent,
} from '../src/lib/validation';
import type { Person, HistoricalEvent } from '../src/lib/types';
import { people, events } from '../src/data/mockData';

interface ValidationReport {
  timestamp: string;
  summary: { total: number; errors: number; warnings: number; ok: number };
  personResults: { id: string; name: string; status: string; issues: string[] }[];
  eventResults: { id: string; title: string; status: string; issues: string[] }[];
}

function main(): void {
  const personResults: ValidationReport['personResults'] = [];
  const eventResults: ValidationReport['eventResults'] = [];

  // Validate persons
  for (const person of people) {
    const issues = validatePerson(person);
    const publishCheck = canPublishPerson(person);
    personResults.push({
      id: person.id,
      name: person.name,
      status: publishCheck.ok ? 'OK' : 'HAS_ERRORS',
      issues: issues.map((i) => `[${i.level.toUpperCase()}] ${i.field ?? ''}: ${i.message}`),
    });
  }

  // Validate events
  for (const event of events) {
    const issues = validateHistoricalEvent(event);
    const publishCheck = canPublishEvent(event);
    eventResults.push({
      id: event.id,
      title: event.title,
      status: publishCheck.ok ? 'OK' : 'HAS_ERRORS',
      issues: issues.map((i) => `[${i.level.toUpperCase()}] ${i.field ?? ''}: ${i.message}`),
    });
  }

  const totalErrors = [...personResults, ...eventResults].filter(
    (r) => r.status === 'HAS_ERRORS',
  ).length;
  const totalWarnings = [...personResults, ...eventResults].reduce(
    (sum, r) => sum + r.issues.filter((i) => i.startsWith('[WARNING]')).length, 0,
  );

  const report: ValidationReport = {
    timestamp: new Date().toISOString(),
    summary: {
      total: personResults.length + eventResults.length,
      errors: totalErrors,
      warnings: totalWarnings,
      ok: personResults.length + eventResults.length - totalErrors,
    },
    personResults,
    eventResults,
  };

  console.log('\n=== Validation Report ===');
  console.log(`Timestamp: ${report.timestamp}`);
  console.log(`Total entities: ${report.summary.total}`);
  console.log(`  OK: ${report.summary.ok}`);
  console.log(`  Errors: ${report.summary.errors}`);
  console.log(`  Warnings: ${report.summary.warnings}`);

  if (totalErrors > 0) {
    console.log('\n--- ERRORS ---');
    for (const r of [...personResults, ...eventResults]) {
      if (r.status === 'HAS_ERRORS') {
        const name = 'name' in r ? r.name : (r as typeof eventResults[0]).title;
        console.log(`\n  ${name}:`);
        for (const issue of r.issues) {
          console.log(`    ${issue}`);
        }
      }
    }
  }

  // Exit with non-zero if errors exist
  process.exit(totalErrors > 0 ? 1 : 0);
}

main();
