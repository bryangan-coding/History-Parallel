/**
 * Async database queries — the single source of truth for data access.
 *
 * All functions are async (SQLite via better-sqlite3 is sync, but wrapping
 * in async keeps the API consistent and allows future migration to other DBs).
 *
 * Replaces the sync helpers in src/data/mockData.ts for all server-side reads
 * and writes.
 */

import 'server-only';
import { eq, and, like, or, sql, inArray, desc, asc } from 'drizzle-orm';
import { db } from './index';
import {
  person as personTable,
  event as eventTable,
  source as sourceTable,
  region as regionTable,
} from './schema';
import type {
  Person,
  HistoricalEvent,
  Source,
  Region,
  DataStatus,
  DatePrecision,
} from '@/lib/types';

// ==================== Type mappers ====================
// Drizzle returns raw DB rows; these map them to the app's TypeScript types.

function mapPersonRow(row: typeof personTable.$inferSelect): Person {
  return {
    id: row.id,
    name: row.name,
    nameEn: row.nameEn ?? undefined,
    alternativeNames: row.alternativeNames ?? [],
    birthYear: row.birthYear ?? undefined,
    deathYear: row.deathYear ?? undefined,
    birthDatePrecision: row.birthDatePrecision as DatePrecision | undefined,
    deathDatePrecision: row.deathDatePrecision as DatePrecision | undefined,
    regionId: row.regionId ?? undefined,
    civilizationId: row.civilizationId ?? undefined,
    occupations: row.occupations ?? [],
    tags: row.tags ?? [],
    tagsEn: row.tagsEn ?? [],
    summary: row.summary ?? undefined,
    summaryEn: row.summaryEn ?? undefined,
    description: row.description ?? undefined,
    descriptionEn: row.descriptionEn ?? undefined,
    sourceIds: row.sourceIds ?? [],
    wikidataQid: row.wikidataQid ?? undefined,
    wikipediaPageId: row.wikipediaPageId ?? undefined,
    wikipediaSlug: row.wikipediaSlug ?? undefined,
    dataStatus: row.dataStatus as DataStatus,
    confidenceScore: row.confidenceScore,
    externalReferences: row.externalReferences ?? [],
    lastReviewedAt: row.lastReviewedAt ?? undefined,
    reviewedBy: row.reviewedBy ?? undefined,
  };
}

function mapEventRow(row: typeof eventTable.$inferSelect): HistoricalEvent {
  return {
    id: row.id,
    title: row.title,
    titleEn: row.titleEn ?? undefined,
    startYear: row.startYear ?? undefined,
    endYear: row.endYear ?? undefined,
    startDateText: row.startDateText ?? undefined,
    endDateText: row.endDateText ?? undefined,
    approximateDateText: row.approximateDateText ?? undefined,
    datePrecision: row.datePrecision as DatePrecision,
    isApproximate: row.isApproximate,
    regionId: row.regionId ?? undefined,
    civilizationId: row.civilizationId ?? undefined,
    placeName: row.placeName ?? undefined,
    placeNameEn: row.placeNameEn ?? undefined,
    coordinates: row.coordinates ?? undefined,
    personIds: row.personIds ?? [],
    tags: row.tags ?? [],
    tagsEn: row.tagsEn ?? [],
    importance: row.importance as 1 | 2 | 3 | 4 | 5,
    summary: row.summary ?? undefined,
    summaryEn: row.summaryEn ?? undefined,
    description: row.description ?? undefined,
    descriptionEn: row.descriptionEn ?? undefined,
    sourceIds: row.sourceIds ?? [],
    relatedEventIds: row.relatedEventIds ?? [],
    wikidataQid: row.wikidataQid ?? undefined,
    wikipediaPageId: row.wikipediaPageId ?? undefined,
    wikipediaSlug: row.wikipediaSlug ?? undefined,
    dataStatus: row.dataStatus as DataStatus,
    confidenceScore: row.confidenceScore,
    externalReferences: row.externalReferences ?? [],
    lastReviewedAt: row.lastReviewedAt ?? undefined,
    reviewedBy: row.reviewedBy ?? undefined,
  };
}

function mapSourceRow(row: typeof sourceTable.$inferSelect): Source {
  return {
    id: row.id,
    title: row.title,
    titleEn: row.titleEn ?? undefined,
    author: row.author ?? undefined,
    url: row.url ?? undefined,
    publisher: row.publisher ?? undefined,
    year: row.year ?? undefined,
    note: row.note ?? undefined,
    license: row.license ?? undefined,
  };
}

function mapRegionRow(row: typeof regionTable.$inferSelect): Region {
  return {
    id: row.id,
    name: row.name,
    nameEn: row.nameEn ?? undefined,
    slug: row.slug,
    parentRegionId: row.parentRegionId ?? undefined,
    description: row.description ?? undefined,
    descriptionEn: row.descriptionEn ?? undefined,
  };
}

// ==================== Read operations ====================

export async function listPeople(opts?: {
  publishedOnly?: boolean;
  dataStatus?: string;
  regionId?: string;
  query?: string;
  era?: { min: number; max: number | null };
  page?: number;
  limit?: number;
}): Promise<{ items: Person[]; total: number }> {
  const conditions = [];

  if (opts?.publishedOnly) {
    conditions.push(eq(personTable.dataStatus, 'published'));
  }
  if (opts?.dataStatus && opts.dataStatus !== 'all') {
    conditions.push(eq(personTable.dataStatus, opts.dataStatus));
  }
  if (opts?.regionId && opts.regionId !== 'all') {
    conditions.push(eq(personTable.regionId, opts.regionId));
  }
  if (opts?.query) {
    const q = `%${opts.query}%`;
    conditions.push(
      or(
        like(personTable.name, q),
        like(personTable.nameEn, q),
        like(personTable.summary, q),
        like(personTable.summaryEn, q),
      ),
    );
  }
  if (opts?.era) {
    if (opts.era.max === null) {
      conditions.push(sql`${personTable.birthYear} >= ${opts.era.min}`);
    } else {
      conditions.push(
        and(
          sql`${personTable.birthYear} >= ${opts.era.min}`,
          sql`${personTable.birthYear} < ${opts.era.max}`,
        ),
      );
    }
  }

  const whereClause = conditions.length > 0 ? and(...conditions) : undefined;

  const allRows = await db
    .select()
    .from(personTable)
    .where(whereClause)
    .orderBy(personTable.name);

  const total = allRows.length;
  const items = allRows.map(mapPersonRow);

  if (opts?.page && opts?.limit) {
    const start = (opts.page - 1) * opts.limit;
    return { items: items.slice(start, start + opts.limit), total };
  }
  return { items, total };
}

export async function findPersonById(id: string): Promise<Person | undefined> {
  const row = await db
    .select()
    .from(personTable)
    .where(eq(personTable.id, id))
    .limit(1)
    .then((rows) => rows[0]);
  return row ? mapPersonRow(row) : undefined;
}

export async function findPeopleByIds(ids: string[]): Promise<Person[]> {
  if (ids.length === 0) return [];
  const rows = await db
    .select()
    .from(personTable)
    .where(inArray(personTable.id, ids));
  return rows.map(mapPersonRow);
}

export async function listEvents(opts?: {
  publishedOnly?: boolean;
  dataStatus?: string;
  regionId?: string;
  ids?: string[];
}): Promise<HistoricalEvent[]> {
  const conditions = [];
  if (opts?.publishedOnly) {
    conditions.push(eq(eventTable.dataStatus, 'published'));
  }
  if (opts?.dataStatus && opts.dataStatus !== 'all') {
    conditions.push(eq(eventTable.dataStatus, opts.dataStatus));
  }
  if (opts?.regionId) {
    conditions.push(eq(eventTable.regionId, opts.regionId));
  }
  if (opts?.ids && opts.ids.length > 0) {
    conditions.push(inArray(eventTable.id, opts.ids));
  }
  const whereClause = conditions.length > 0 ? and(...conditions) : undefined;
  const rows = await db.select().from(eventTable).where(whereClause);
  return rows.map(mapEventRow);
}

export async function listAllEvents(): Promise<HistoricalEvent[]> {
  const rows = await db.select().from(eventTable);
  return rows.map(mapEventRow);
}

export async function findEventById(id: string): Promise<HistoricalEvent | undefined> {
  const row = await db
    .select()
    .from(eventTable)
    .where(eq(eventTable.id, id))
    .limit(1)
    .then((rows) => rows[0]);
  return row ? mapEventRow(row) : undefined;
}

export async function findEventsForPerson(personId: string): Promise<HistoricalEvent[]> {
  // personIds is a JSON array column; use application-level filter
  const allEvents = await db.select().from(eventTable);
  return allEvents
    .filter((row) => (row.personIds as string[] | null)?.includes(personId))
    .map(mapEventRow);
}

export async function findEventsByRegion(regionId: string): Promise<HistoricalEvent[]> {
  const rows = await db
    .select()
    .from(eventTable)
    .where(eq(eventTable.regionId, regionId));
  return rows.map(mapEventRow);
}

export async function findPersonsForEvent(eventId: string): Promise<Person[]> {
  const event = await findEventById(eventId);
  if (!event || event.personIds.length === 0) return [];
  return findPeopleByIds(event.personIds);
}

export async function listRegions(): Promise<Region[]> {
  const rows = await db.select().from(regionTable);
  return rows.map(mapRegionRow);
}

export async function findRegionById(id: string): Promise<Region | undefined> {
  const row = await db
    .select()
    .from(regionTable)
    .where(eq(regionTable.id, id))
    .limit(1)
    .then((rows) => rows[0]);
  return row ? mapRegionRow(row) : undefined;
}

export async function findSubRegions(regionId: string): Promise<Region[]> {
  const rows = await db
    .select()
    .from(regionTable)
    .where(eq(regionTable.parentRegionId, regionId));
  return rows.map(mapRegionRow);
}

export async function listSources(): Promise<Source[]> {
  const rows = await db.select().from(sourceTable);
  return rows.map(mapSourceRow);
}

export async function findSourceById(id: string): Promise<Source | undefined> {
  const row = await db
    .select()
    .from(sourceTable)
    .where(eq(sourceTable.id, id))
    .limit(1)
    .then((rows) => rows[0]);
  return row ? mapSourceRow(row) : undefined;
}

export async function findSourcesForEvent(eventId: string): Promise<Source[]> {
  const event = await findEventById(eventId);
  if (!event || event.sourceIds.length === 0) return [];
  const ids = event.sourceIds;
  if (ids.length === 0) return [];
  const rows = await db
    .select()
    .from(sourceTable)
    .where(inArray(sourceTable.id, ids));
  return rows.map(mapSourceRow);
}

export async function findAllTags(): Promise<string[]> {
  const [people, events] = await Promise.all([
    db.select({ tags: personTable.tags }).from(personTable),
    db.select({ tags: eventTable.tags }).from(eventTable),
  ]);
  const tagSet = new Set<string>();
  for (const p of people) {
    for (const t of (p.tags as string[] | null) ?? []) tagSet.add(t);
  }
  for (const e of events) {
    for (const t of (e.tags as string[] | null) ?? []) tagSet.add(t);
  }
  return Array.from(tagSet).sort();
}

// ==================== Write operations ====================

export async function updatePersonStatus(
  ids: string[],
  status: DataStatus,
  reviewedBy: string,
): Promise<void> {
  if (ids.length === 0) return;
  await db
    .update(personTable)
    .set({
      dataStatus: status,
      lastReviewedAt: new Date().toISOString(),
      reviewedBy,
    })
    .where(inArray(personTable.id, ids));
}

export async function updatePersonScore(
  id: string,
  score: number,
  reviewedBy: string,
): Promise<void> {
  await db
    .update(personTable)
    .set({
      confidenceScore: score,
      lastReviewedAt: new Date().toISOString(),
      reviewedBy,
    })
    .where(eq(personTable.id, id));
}

export async function updateEventStatus(
  ids: string[],
  status: DataStatus,
  reviewedBy: string,
): Promise<void> {
  if (ids.length === 0) return;
  await db
    .update(eventTable)
    .set({
      dataStatus: status,
      lastReviewedAt: new Date().toISOString(),
      reviewedBy,
    })
    .where(inArray(eventTable.id, ids));
}

export async function updateEventScore(
  id: string,
  score: number,
  reviewedBy: string,
): Promise<void> {
  await db
    .update(eventTable)
    .set({
      confidenceScore: score,
      lastReviewedAt: new Date().toISOString(),
      reviewedBy,
    })
    .where(eq(eventTable.id, id));
}
