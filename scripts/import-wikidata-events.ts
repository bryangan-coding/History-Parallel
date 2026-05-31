#!/usr/bin/env tsx
/**
 * Import historical events from Wikidata.
 *
 * Usage:
 *   npm run import:wikidata:events -- --startYear 1000 --endYear 1100 --limit 100 --dry-run
 */

import * as fs from 'fs';
import * as path from 'path';
import { runWikidataSparqlQuery } from './wikidata/client';
import { buildEventQuery } from './wikidata/queries';
import { mapWikidataEvent } from './wikidata/mapper';
import type { HistoricalEvent } from '../src/lib/types';

interface ImportOptions {
  startYear?: number;
  endYear?: number;
  region?: string;
  tag?: string;
  limit?: number;
  dryRun?: boolean;
}

function parseArgs(): ImportOptions {
  const args = process.argv.slice(2);
  const opts: ImportOptions = {};

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case '--startYear': opts.startYear = parseInt(args[++i], 10); break;
      case '--endYear': opts.endYear = parseInt(args[++i], 10); break;
      case '--region': opts.region = args[++i]; break;
      case '--tag': opts.tag = args[++i]; break;
      case '--limit': opts.limit = parseInt(args[++i], 10); break;
      case '--dry-run': opts.dryRun = true; break;
    }
  }
  return opts;
}

async function main(): Promise<void> {
  const opts = parseArgs();

  console.log('=== Wikidata Event Import ===');
  console.log('Options:', opts);
  console.log();

  try {
    const query = buildEventQuery({
      startYear: opts.startYear,
      endYear: opts.endYear,
      limit: opts.limit ?? 100,
    });

    console.log('Sending SPARQL query...');

    const response = await runWikidataSparqlQuery(query);

    const events: HistoricalEvent[] = response.results.bindings.map(mapWikidataEvent);

    console.log(`\nFound ${events.length} events`);

    if (events.length > 0) {
      console.log('\nFirst 5 results:');
      for (const e of events.slice(0, 5)) {
        const year = e.startYear ?? 'unknown';
        console.log(`  - ${e.title} (${year})`);
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
    const outputPath = path.join(importDir, `wikidata-events-${timestamp}.json`);
    fs.writeFileSync(outputPath, JSON.stringify(events, null, 2), 'utf-8');

    console.log(`\nSaved ${events.length} events to: ${outputPath}`);
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
