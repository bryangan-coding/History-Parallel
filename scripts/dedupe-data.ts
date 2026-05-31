#!/usr/bin/env tsx
/**
 * Deduplication detection script.
 * Reads all data and detects potential duplicate persons and events.
 * Outputs report to src/data/review/duplicate-report-[timestamp].json
 *
 * Usage: npm run dedupe:data
 */

import * as fs from 'fs';
import * as path from 'path';
import {
  findPotentialDuplicatePersons,
  findPotentialDuplicateEvents,
} from '../src/lib/dedupe';
import type { DuplicateCandidate } from '../src/lib/dedupe';
import type { Person, HistoricalEvent } from '../src/lib/types';
import { people, events } from '../src/data/mockData';

interface DedupeReport {
  timestamp: string;
  summary: { personDuplicates: number; eventDuplicates: number };
  personDuplicates: { personId: string; personName: string; candidates: { id: string; name: string; score: number; reasons: string[] }[] }[];
  eventDuplicates: { eventId: string; eventTitle: string; candidates: { id: string; title: string; score: number; reasons: string[] }[] }[];
}

function main(): void {
  const personResults: DedupeReport['personDuplicates'] = [];
  const eventResults: DedupeReport['eventDuplicates'] = [];

  // Check persons
  for (const person of people) {
    const candidates = findPotentialDuplicatePersons(person, people);
    if (candidates.length > 0) {
      personResults.push({
        personId: person.id,
        personName: person.name,
        candidates: candidates.map((c) => ({
          id: c.item.id,
          name: c.item.name,
          score: Math.round(c.score * 100) / 100,
          reasons: c.reasons,
        })),
      });
    }
  }

  // Check events
  for (const event of events) {
    const candidates = findPotentialDuplicateEvents(event, events);
    if (candidates.length > 0) {
      eventResults.push({
        eventId: event.id,
        eventTitle: event.title,
        candidates: candidates.map((c) => ({
          id: c.item.id,
          title: c.item.title,
          score: Math.round(c.score * 100) / 100,
          reasons: c.reasons,
        })),
      });
    }
  }

  const report: DedupeReport = {
    timestamp: new Date().toISOString(),
    summary: {
      personDuplicates: personResults.length,
      eventDuplicates: eventResults.length,
    },
    personDuplicates: personResults,
    eventDuplicates: eventResults,
  };

  // Write report
  const reviewDir = path.join(__dirname, '..', 'src', 'data', 'review');
  if (!fs.existsSync(reviewDir)) {
    fs.mkdirSync(reviewDir, { recursive: true });
  }

  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const reportPath = path.join(reviewDir, `duplicate-report-${timestamp}.json`);
  fs.writeFileSync(reportPath, JSON.stringify(report, null, 2), 'utf-8');

  console.log(`\n=== Deduplication Report ===`);
  console.log(`Person duplicates found: ${report.summary.personDuplicates}`);
  console.log(`Event duplicates found: ${report.summary.eventDuplicates}`);
  console.log(`Report saved to: ${reportPath}`);

  // Print top candidates
  if (personResults.length > 0) {
    console.log('\n--- Top Person Duplicate Candidates ---');
    for (const r of personResults.slice(0, 10)) {
      console.log(`\n  ${r.personName} (${r.personId}):`);
      for (const c of r.candidates.slice(0, 3)) {
        console.log(`    → ${c.name} (score: ${c.score}) [${c.reasons.join(', ')}]`);
      }
    }
  }

  if (eventResults.length > 0) {
    console.log('\n--- Top Event Duplicate Candidates ---');
    for (const r of eventResults.slice(0, 10)) {
      console.log(`\n  ${r.eventTitle} (${r.eventId}):`);
      for (const c of r.candidates.slice(0, 3)) {
        console.log(`    → ${c.title} (score: ${c.score}) [${c.reasons.join(', ')}]`);
      }
    }
  }

  process.exit(0);
}

main();
