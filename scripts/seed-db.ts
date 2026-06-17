/**
 * Seed the SQLite database from the current mockData.ts arrays.
 *
 * Usage: npm run db:seed
 * Prerequisite: npm run db:push (creates the tables)
 *
 * This is a one-time migration script. After seeding, the DB becomes
 * the source of truth and mockData.ts will be deprecated for server-side use.
 */

import { resolve } from 'node:path';
import { mkdirSync } from 'node:fs';

// Set DATABASE_URL if not set
process.env.DATABASE_URL = process.env.DATABASE_URL || 'file:./data/db.sqlite';

import Database from 'better-sqlite3';
import { drizzle } from 'drizzle-orm/better-sqlite3';

const DB_PATH = resolve(process.cwd(), process.env.DATABASE_URL.replace('file:', ''));
mkdirSync(resolve(DB_PATH, '..'), { recursive: true });

const sqlite = new Database(DB_PATH);
sqlite.pragma('journal_mode = WAL');
sqlite.pragma('foreign_keys = ON');
const db = drizzle(sqlite);

// Import mockData arrays (current source of truth)
// Note: this imports the FULL mockData.ts (~1.9MB). That's fine for a one-time script.
import {
  regions,
  people,
  events,
  sources,
} from '../src/data/mockData';

async function seedRegions() {
  console.log('Seeding regions...');
  const count = regions.length;

  // Insert in batches using raw SQL for speed
  const insert = sqlite.prepare(`
    INSERT OR REPLACE INTO region (id, name, name_en, slug, parent_region_id, description, description_en)
    VALUES (?, ?, ?, ?, ?, ?, ?)
  `);

  const tx = sqlite.transaction((items: typeof regions) => {
    for (const r of items) {
      insert.run(
        r.id,
        r.name,
        r.nameEn ?? null,
        r.slug,
        r.parentRegionId ?? null,
        r.description ?? null,
        r.descriptionEn ?? null,
      );
    }
  });

  tx(regions);
  console.log(`  ✓ ${count} regions`);
}

async function seedSources() {
  console.log('Seeding sources...');
  const count = sources.length;

  const insert = sqlite.prepare(`
    INSERT OR REPLACE INTO source (id, title, title_en, author, url, publisher, year, note, license)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
  `);

  const tx = sqlite.transaction((items: typeof sources) => {
    for (const s of items) {
      insert.run(
        s.id,
        s.title,
        s.titleEn ?? null,
        s.author ?? null,
        s.url ?? null,
        s.publisher ?? null,
        s.year ?? null,
        s.note ?? null,
        s.license ?? null,
      );
    }
  });

  tx(sources);
  console.log(`  ✓ ${count} sources`);
}

async function seedPeople() {
  console.log('Seeding people...');
  const count = people.length;

  const insert = sqlite.prepare(`
    INSERT OR REPLACE INTO person (
      id, name, name_en, alternative_names,
      birth_year, death_year, birth_date_precision, death_date_precision,
      region_id, civilization_id, occupations,
      tags, tags_en, summary, summary_en, description, description_en,
      source_ids, wikidata_qid, wikipedia_page_id, wikipedia_slug,
      data_status, confidence_score, external_references, last_reviewed_at, reviewed_by
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `);

  const tx = sqlite.transaction((items: typeof people) => {
    for (const p of items) {
      insert.run(
        p.id,
        p.name,
        p.nameEn ?? null,
        JSON.stringify(p.alternativeNames),
        p.birthYear ?? null,
        p.deathYear ?? null,
        p.birthDatePrecision ?? null,
        p.deathDatePrecision ?? null,
        p.regionId ?? null,
        p.civilizationId ?? null,
        JSON.stringify(p.occupations),
        JSON.stringify(p.tags),
        JSON.stringify(p.tagsEn),
        p.summary ?? null,
        p.summaryEn ?? null,
        p.description ?? null,
        p.descriptionEn ?? null,
        JSON.stringify(p.sourceIds),
        p.wikidataQid ?? null,
        p.wikipediaPageId ?? null,
        p.wikipediaSlug ?? null,
        p.dataStatus,
        p.confidenceScore,
        JSON.stringify(p.externalReferences),
        p.lastReviewedAt ?? null,
        p.reviewedBy ?? null,
      );
    }
  });

  tx(people);
  console.log(`  ✓ ${count} people`);
}

async function seedEvents() {
  console.log('Seeding events...');
  const count = events.length;

  const insert = sqlite.prepare(`
    INSERT OR REPLACE INTO event (
      id, title, title_en,
      start_year, end_year, start_date_text, end_date_text, approximate_date_text,
      date_precision, is_approximate,
      region_id, civilization_id, place_name, place_name_en, coordinates,
      person_ids, tags, tags_en, importance,
      summary, summary_en, description, description_en,
      source_ids, related_event_ids,
      wikidata_qid, wikipedia_page_id, wikipedia_slug,
      data_status, confidence_score, external_references, last_reviewed_at, reviewed_by
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `);

  const tx = sqlite.transaction((items: typeof events) => {
    for (const e of items) {
      insert.run(
        e.id,
        e.title,
        e.titleEn ?? null,
        e.startYear ?? null,
        e.endYear ?? null,
        e.startDateText ?? null,
        e.endDateText ?? null,
        e.approximateDateText ?? null,
        e.datePrecision,
        e.isApproximate ? 1 : 0,
        e.regionId ?? null,
        e.civilizationId ?? null,
        e.placeName ?? null,
        e.placeNameEn ?? null,
        e.coordinates ? JSON.stringify(e.coordinates) : null,
        JSON.stringify(e.personIds),
        JSON.stringify(e.tags),
        JSON.stringify(e.tagsEn),
        e.importance,
        e.summary ?? null,
        e.summaryEn ?? null,
        e.description ?? null,
        e.descriptionEn ?? null,
        JSON.stringify(e.sourceIds),
        JSON.stringify(e.relatedEventIds),
        e.wikidataQid ?? null,
        e.wikipediaPageId ?? null,
        e.wikipediaSlug ?? null,
        e.dataStatus,
        e.confidenceScore,
        JSON.stringify(e.externalReferences),
        e.lastReviewedAt ?? null,
        e.reviewedBy ?? null,
      );
    }
  });

  tx(events);
  console.log(`  ✓ ${count} events`);
}

async function main() {
  console.log('Database:', DB_PATH);
  console.log('');

  await seedRegions();
  await seedSources();
  await seedPeople();
  await seedEvents();

  console.log('');
  console.log('✅ Seed complete');

  // Print summary
  const regionCount = sqlite.prepare('SELECT COUNT(*) as c FROM region').get() as { c: number };
  const sourceCount = sqlite.prepare('SELECT COUNT(*) as c FROM source').get() as { c: number };
  const peopleCount = sqlite.prepare('SELECT COUNT(*) as c FROM person').get() as { c: number };
  const eventCount = sqlite.prepare('SELECT COUNT(*) as c FROM event').get() as { c: number };
  console.log(`  Regions: ${regionCount.c}, Sources: ${sourceCount.c}, People: ${peopleCount.c}, Events: ${eventCount.c}`);

  sqlite.close();
}

main().catch((err) => {
  console.error('Seed failed:', err);
  process.exit(1);
});
