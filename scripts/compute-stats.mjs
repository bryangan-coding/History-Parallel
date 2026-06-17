/**
 * 预计算数据统计，生成轻量 JSON，供 admin 等页面导入（避免全量 mockData）
 *
 * Usage: node scripts/compute-stats.mjs
 * Output: src/data/_stats.json (~2KB vs 117MB full data)
 */

import { readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { ERAS } from '../src/lib/eras.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PEOPLE_DIR = join(__dirname, '..', 'src', 'data', 'people');
const EVENTS_FILE = join(__dirname, '..', 'src', 'data', 'people', '_biographicalEvents.json');
const OUTPUT = join(__dirname, '..', 'src', 'data', '_stats.json');

// Load all people JSON files
const peopleFiles = readdirSync(PEOPLE_DIR)
  .filter((f) => f.endsWith('.json') && f !== '_biographicalEvents.json')
  .sort();

let allPeople = [];
for (const file of peopleFiles) {
  const raw = readFileSync(join(PEOPLE_DIR, file), 'utf-8');
  allPeople.push(...JSON.parse(raw));
}

// Load events
let allEvents = [];
if (readFileSync(EVENTS_FILE, 'utf-8')) {
  allEvents = JSON.parse(readFileSync(EVENTS_FILE, 'utf-8'));
}

const published = allPeople.filter((p) => p.dataStatus === 'published');

// Status counts (people + events)
const statusCounts = { published: 0, needs_review: 0, imported: 0, verified: 0, rejected: 0 };
for (const key of Object.keys(statusCounts)) {
  statusCounts[key] =
    allPeople.filter((p) => p.dataStatus === key).length +
    allEvents.filter((e) => e.dataStatus === key).length;
}

// People pending (not published)
const peoplePending = allPeople.filter((p) => p.dataStatus !== 'published').length;
const eventsPending = allEvents.filter((e) => e.dataStatus !== 'published').length;

// Confidence score distribution
const allScores = [...allPeople.map((p) => p.confidenceScore ?? 0), ...allEvents.map((e) => e.confidenceScore ?? 0)];
const buckets = [
  { label: '0–0.3', min: 0, max: 0.3 },
  { label: '0.3–0.5', min: 0.3, max: 0.5 },
  { label: '0.5–0.7', min: 0.5, max: 0.7 },
  { label: '0.7–0.85', min: 0.7, max: 0.85 },
  { label: '0.85–1.0', min: 0.85, max: 1.0 },
];
const distribution = buckets.map((b) => ({
  ...b,
  count: allScores.filter((s) => s >= b.min && (b.max === 1.0 ? s <= b.max : s < b.max)).length,
}));

// Era stats (computed from shared ERAS definitions)
const eraStats = ERAS.map(era => {
  const count = era.max === null
    ? published.filter(p => (p.birthYear ?? 0) >= era.min).length
    : published.filter(p => {
        const by = p.birthYear ?? 0;
        return by >= era.min && by < era.max;
      }).length;
  return {
    key: era.key,
    label: era.label,
    labelEn: era.labelEn,
    count,
    minYear: era.min,
    maxYear: era.max,
  };
});

const stats = {
  totalPeople: allPeople.length,
  totalEvents: allEvents.length,
  totalPublished: published.length,
  peoplePending,
  eventsPending,
  totalRecords: allPeople.length + allEvents.length,
  statusCounts,
  distribution,
  eraStats,
  totalRegions: 34,
};

// Also write featured people (first 12 published) to a separate lightweight file
const FEATURED_OUTPUT = join(__dirname, '..', 'src', 'data', '_featured.json');
writeFileSync(FEATURED_OUTPUT, JSON.stringify(published.slice(0, 12), null, 2), 'utf-8');
console.log(`Featured written to ${FEATURED_OUTPUT}`);

writeFileSync(OUTPUT, JSON.stringify(stats, null, 2), 'utf-8');
console.log(`Stats written to ${OUTPUT} (${JSON.stringify(stats).length} bytes)`);
console.log(`People: ${stats.totalPeople}, Events: ${stats.totalEvents}, Published: ${stats.totalPublished}`);
