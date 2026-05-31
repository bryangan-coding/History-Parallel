#!/usr/bin/env tsx
/**
 * Import historical persons from Wikidata.
 *
 * Usage:
 *   npm run import:wikidata:people -- --birthYearStart 960 --birthYearEnd 1279 --limit 50 --dry-run
 *
 * Options:
 *   --birthYearStart <year>    Filter by birth year range start
 *   --birthYearEnd <year>      Filter by birth year range end
 *   --region <region>          (Reserved for future use)
 *   --occupation <QID>         Filter by Wikidata occupation QID
 *   --limit <n>                Max results (default: 50)
 *   --dry-run                  Run without saving to disk
 */

import * as fs from 'fs';
import * as path from 'path';
import { runWikidataSparqlQuery } from './wikidata/client';
import { buildPersonQuery } from './wikidata/queries';
import { mapWikidataPerson } from './wikidata/mapper';
import type { Person } from '../src/lib/types';

interface ImportOptions {
  birthYearStart?: number;
  birthYearEnd?: number;
  region?: string;
  occupation?: string;
  limit?: number;
  dryRun?: boolean;
}

function parseArgs(): ImportOptions {
  const args = process.argv.slice(2);
  const opts: ImportOptions = {};

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case '--birthYearStart': opts.birthYearStart = parseInt(args[++i], 10); break;
      case '--birthYearEnd': opts.birthYearEnd = parseInt(args[++i], 10); break;
      case '--region': opts.region = args[++i]; break;
      case '--occupation': opts.occupation = args[++i]; break;
      case '--limit': opts.limit = parseInt(args[++i], 10); break;
      case '--dry-run': opts.dryRun = true; break;
    }
  }
  return opts;
}

async function main(): Promise<void> {
  const opts = parseArgs();

  console.log('=== Wikidata Person Import ===');
  console.log('Options:', opts);
  console.log();

  try {
    const query = buildPersonQuery({
      birthYearStart: opts.birthYearStart,
      birthYearEnd: opts.birthYearEnd,
      occupation: opts.occupation,
      limit: opts.limit ?? 50,
    });

    console.log('Sending SPARQL query...');

    const response = await runWikidataSparqlQuery(query);

    const people: Person[] = response.results.bindings.map(mapWikidataPerson);

    console.log(`\nFound ${people.length} persons`);

    if (people.length > 0) {
      console.log('\nFirst 5 results:');
      for (const p of people.slice(0, 5)) {
        const years = p.birthYear ? `${p.birthYear}–${p.deathYear ?? '?'}` : 'unknown dates';
        console.log(`  - ${p.name} (${years})`);
      }
    }

    if (opts.dryRun) {
      console.log('\n[Dry run] No data saved.');
      return;
    }

    const importDir = path.join(__dirname, '..', 'src', 'data', 'imported');
    if (!fs.existsSync(importDir)) {
      fs.mkdirSync(importDir, { recursive: true });
    }

    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    const outputPath = path.join(importDir, `wikidata-people-${timestamp}.json`);
    fs.writeFileSync(outputPath, JSON.stringify(people, null, 2), 'utf-8');

    console.log(`\nSaved ${people.length} persons to: ${outputPath}`);
  } catch (error) {
    const importDir = path.join(__dirname, '..', 'src', 'data', 'imported');
    if (!fs.existsSync(importDir)) {
      fs.mkdirSync(importDir, { recursive: true });
    }
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    const errorPath = path.join(importDir, `import-errors-${timestamp}.json`);
    const errorMessage = error instanceof Error ? error.message : String(error);
    fs.writeFileSync(errorPath, JSON.stringify({ error: errorMessage, timestamp }, null, 2), 'utf-8');
    console.error(`\nImport failed: ${errorMessage}`);
    console.error(`Error report: ${errorPath}`);
    process.exit(1);
  }

  process.exit(0);
}

main();
