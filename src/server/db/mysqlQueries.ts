/**
 * MySQL queries — drop-in replacement for src/server/db/queries.ts
 *
 * 使用方式：在 server-actions.ts 中将 import 切换到本文件
 * import { listPeople, ... } from '@/server/db/mysqlQueries';
 *
 * 所有查询通过 MySQL 连接池执行，支持 JSON 列（person_ids, tags 等）
 */
import 'server-only';
import pool, { parseJsonArray } from '@/server/db/mysql';
import type {
  Person,
  HistoricalEvent,
  Source,
  Region,
  DataStatus,
} from '@/lib/types';
import type { RowDataPacket, ResultSetHeader } from 'mysql2';

// Re-export MySQL pool for direct access
export { pool };

// ==================== Type mappers ====================

function mapPerson(row: RowDataPacket): Person {
  return {
    id: row.id, name: row.name,
    nameEn: row.name_en ?? undefined,
    alternativeNames: parseJsonArray(row.alternative_names),
    birthYear: row.birth_year ?? undefined,
    deathYear: row.death_year ?? undefined,
    birthDatePrecision: (row.birth_date_precision ?? 'year') as Person['birthDatePrecision'],
    deathDatePrecision: (row.death_date_precision ?? 'year') as Person['deathDatePrecision'],
    regionId: row.region_id ?? undefined,
    civilizationId: row.civilization_id ?? undefined,
    occupations: parseJsonArray(row.occupations),
    tags: parseJsonArray(row.tags),
    tagsEn: parseJsonArray(row.tags_en),
    summary: row.summary ?? undefined,
    summaryEn: row.summary_en ?? undefined,
    description: row.description ?? undefined,
    descriptionEn: row.description_en ?? undefined,
    sourceIds: parseJsonArray(row.source_ids),
    wikidataQid: row.wikidata_qid ?? undefined,
    wikipediaPageId: row.wikipedia_page_id ?? undefined,
    wikipediaSlug: row.wikipedia_slug ?? undefined,
    dataStatus: (row.data_status ?? 'imported') as DataStatus,
    confidenceScore: row.confidence_score ?? 0.5,
    externalReferences: [],
    lastReviewedAt: row.last_reviewed_at ?? undefined,
    reviewedBy: row.reviewed_by ?? undefined,
  };
}

function mapEvent(row: RowDataPacket): HistoricalEvent {
  return {
    id: row.id, title: row.title,
    titleEn: row.title_en ?? undefined,
    startYear: row.start_year ?? undefined,
    endYear: row.end_year ?? undefined,
    startDateText: row.start_date_text ?? undefined,
    endDateText: row.end_date_text ?? undefined,
    approximateDateText: row.approximate_date_text ?? undefined,
    datePrecision: (row.date_precision ?? 'year') as HistoricalEvent['datePrecision'],
    isApproximate: Boolean(row.is_approximate),
    regionId: row.region_id ?? undefined,
    civilizationId: row.civilization_id ?? undefined,
    placeName: row.place_name ?? undefined,
    placeNameEn: row.place_name_en ?? undefined,
    coordinates: (() => {
      if (!row.coordinates) return undefined;
      if (typeof row.coordinates === 'object') return row.coordinates;
      try { return JSON.parse(row.coordinates as string); } catch { return undefined; }
    })(),
    personIds: parseJsonArray(row.person_ids),
    tags: parseJsonArray(row.tags),
    tagsEn: parseJsonArray(row.tags_en),
    importance: (row.importance ?? 2) as 1 | 2 | 3 | 4 | 5,
    summary: row.summary ?? undefined,
    summaryEn: row.summary_en ?? undefined,
    description: row.description ?? undefined,
    descriptionEn: row.description_en ?? undefined,
    sourceIds: parseJsonArray(row.source_ids),
    relatedEventIds: parseJsonArray(row.related_event_ids),
    wikidataQid: row.wikidata_qid ?? undefined,
    wikipediaPageId: row.wikipedia_page_id ?? undefined,
    wikipediaSlug: row.wikipedia_slug ?? undefined,
    dataStatus: (row.data_status ?? 'published') as DataStatus,
    confidenceScore: row.confidence_score ?? 0.5,
    externalReferences: [],
    lastReviewedAt: row.last_reviewed_at ?? undefined,
    reviewedBy: row.reviewed_by ?? undefined,
  };
}

function mapRegion(row: RowDataPacket): Region {
  return {
    id: row.id, name: row.name,
    nameEn: row.name_en ?? undefined,
    slug: row.slug,
    parentRegionId: row.parent_region_id ?? undefined,
    description: row.description ?? undefined,
    descriptionEn: row.description_en ?? undefined,
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
  const conditions: string[] = [];
  const params: unknown[] = [];

  if (opts?.publishedOnly) {
    conditions.push('data_status = ?'); params.push('published');
  }
  if (opts?.dataStatus && opts.dataStatus !== 'all') {
    conditions.push('data_status = ?'); params.push(opts.dataStatus);
  }
  if (opts?.regionId && opts.regionId !== 'all') {
    conditions.push('region_id = ?'); params.push(opts.regionId);
  }
  if (opts?.query) {
    const q = `%${opts.query}%`;
    conditions.push('(name LIKE ? OR name_en LIKE ? OR summary LIKE ?)');
    params.push(q, q, q);
  }
  if (opts?.era) {
    if (opts.era.max === null) {
      conditions.push('birth_year >= ?'); params.push(opts.era.min);
    } else {
      conditions.push('birth_year >= ? AND birth_year < ?');
      params.push(opts.era.min, opts.era.max);
    }
  }

  const where = conditions.length > 0 ? `WHERE ${conditions.join(' AND ')}` : '';

  // If pagination requested, do it in SQL (not in memory)
  if (opts?.page && opts?.limit) {
    const offset = (opts.page - 1) * opts.limit;
    const [countRows] = await pool.query<RowDataPacket[]>(
      `SELECT COUNT(*) as total FROM people ${where}`, params,
    );
    const total = countRows[0].total;
    const [rows] = await pool.query<RowDataPacket[]>(
      `SELECT * FROM people ${where} ORDER BY name LIMIT ? OFFSET ?`,
      [...params, opts.limit, offset],
    );
    return { items: rows.map(mapPerson), total };
  }

  // Default: hard limit of 500 to prevent accidental full-table loads
  const effectiveLimit = opts?.limit ?? 500;
  const [countRows] = await pool.query<RowDataPacket[]>(
    `SELECT COUNT(*) as total FROM people ${where}`, params,
  );
  const total = countRows[0].total as number;
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT * FROM people ${where} ORDER BY name LIMIT ?`, [effectiveLimit],
  );
  const items = rows.map(mapPerson);
  return { items, total };
}

export async function findPersonById(id: string): Promise<Person | undefined> {
  const [rows] = await pool.query<RowDataPacket[]>(
    'SELECT * FROM people WHERE id = ?', [id],
  );
  return rows.length ? mapPerson(rows[0]) : undefined;
}

export async function findPeopleByIds(ids: string[]): Promise<Person[]> {
  if (ids.length === 0) return [];
  const placeholders = ids.map(() => '?').join(',');
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT * FROM people WHERE id IN (${placeholders})`, ids,
  );
  return rows.map(mapPerson);
}

export async function listEvents(opts?: {
  publishedOnly?: boolean;
  dataStatus?: string;
  regionId?: string;
  ids?: string[];
  page?: number;
  limit?: number;
}): Promise<HistoricalEvent[]> {
  const conditions: string[] = [];
  const params: unknown[] = [];

  if (opts?.publishedOnly) { conditions.push('data_status = ?'); params.push('published'); }
  if (opts?.dataStatus && opts.dataStatus !== 'all') { conditions.push('data_status = ?'); params.push(opts.dataStatus); }
  if (opts?.regionId) { conditions.push('region_id = ?'); params.push(opts.regionId); }
  if (opts?.ids && opts.ids.length > 0) {
    conditions.push(`id IN (${opts.ids.map(() => '?').join(',')})`);
    params.push(...opts.ids);
  }

  const where = conditions.length > 0 ? `WHERE ${conditions.join(' AND ')}` : '';
  const effectiveLimit = opts?.limit ?? 500;
  const offset = opts?.page ? (opts.page - 1) * effectiveLimit : 0;

  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT * FROM events ${where} ORDER BY start_year DESC LIMIT ? OFFSET ?`,
    [...params, effectiveLimit, offset],
  );
  return rows.map(mapEvent);
}

export async function listAllEvents(opts?: {
  page?: number;
  limit?: number;
  dataStatus?: string;
}): Promise<{ items: HistoricalEvent[]; total: number }> {
  const conditions: string[] = [];
  const params: unknown[] = [];
  if (opts?.dataStatus && opts.dataStatus !== 'all') {
    conditions.push('data_status = ?'); params.push(opts.dataStatus);
  }
  const where = conditions.length > 0 ? `WHERE ${conditions.join(' AND ')}` : '';

  if (opts?.page && opts?.limit) {
    const offset = (opts.page - 1) * opts.limit;
    const [countRows] = await pool.query<RowDataPacket[]>(
      `SELECT COUNT(*) as total FROM events ${where}`, params,
    );
    const total = countRows[0].total as number;
    const [rows] = await pool.query<RowDataPacket[]>(
      `SELECT * FROM events ${where} ORDER BY start_year DESC LIMIT ? OFFSET ?`,
      [...params, opts.limit, offset],
    );
    return { items: rows.map(mapEvent), total };
  }

  // Default: hard limit of 500 to prevent accidental full-table loads
  const effectiveLimit = opts?.limit ?? 500;
  const [countRows] = await pool.query<RowDataPacket[]>(
    `SELECT COUNT(*) as total FROM events ${where}`, params,
  );
  const total = countRows[0].total as number;
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT * FROM events ${where} ORDER BY start_year DESC LIMIT ?`, [effectiveLimit],
  );
  return { items: rows.map(mapEvent), total };
}

export async function findEventById(id: string): Promise<HistoricalEvent | undefined> {
  const [rows] = await pool.query<RowDataPacket[]>(
    'SELECT * FROM events WHERE id = ?', [id],
  );
  return rows.length ? mapEvent(rows[0]) : undefined;
}

export async function findEventsForPerson(personId: string): Promise<HistoricalEvent[]> {
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT e.* FROM events e
     INNER JOIN event_persons ep ON e.id = ep.event_id
     WHERE ep.person_id = ? AND e.data_status = 'published'`,
    [personId],
  );
  return rows.map(mapEvent);
}

export async function findEventsByRegion(regionId: string): Promise<HistoricalEvent[]> {
  const [rows] = await pool.query<RowDataPacket[]>(
    "SELECT * FROM events WHERE region_id = ? AND data_status = 'published' ORDER BY start_year LIMIT 500",
    [regionId],
  );
  return rows.map(mapEvent);
}

export async function listEventsBySearch(query: string, limit = 50): Promise<HistoricalEvent[]> {
  const q = `%${query}%`;
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT * FROM events 
     WHERE data_status = 'published' 
     AND (title LIKE ? OR title_en LIKE ? OR summary LIKE ? OR summary_en LIKE ?)
     ORDER BY importance DESC, start_year DESC
     LIMIT ?`,
    [q, q, q, q, limit],
  );
  return rows.map(mapEvent);
}

export async function findEventsByYearRange(minYear: number, maxYear: number): Promise<HistoricalEvent[]> {
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT * FROM events 
     WHERE data_status = 'published' AND start_year IS NOT NULL
     AND (
       (start_year >= ? AND start_year <= ?)
       OR (end_year IS NOT NULL AND end_year >= ? AND end_year <= ?)
       OR (start_year <= ? AND end_year IS NOT NULL AND end_year >= ?)
     )
     ORDER BY start_year
     LIMIT 500`,
    [minYear, maxYear, minYear, maxYear, minYear, maxYear],
  );
  return rows.map(mapEvent);
}

export async function findPersonsForEvent(eventId: string): Promise<Person[]> {
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT p.* FROM people p
     INNER JOIN event_persons ep ON p.id = ep.person_id
     WHERE ep.event_id = ?`,
    [eventId],
  );
  return rows.map(mapPerson);
}

export async function listRegions(): Promise<Region[]> {
  const [rows] = await pool.query<RowDataPacket[]>('SELECT * FROM regions');
  return rows.map(mapRegion);
}

export async function findRegionById(id: string): Promise<Region | undefined> {
  const [rows] = await pool.query<RowDataPacket[]>(
    'SELECT * FROM regions WHERE id = ?', [id],
  );
  return rows.length ? mapRegion(rows[0]) : undefined;
}

export async function findSubRegions(regionId: string): Promise<Region[]> {
  const [rows] = await pool.query<RowDataPacket[]>(
    'SELECT * FROM regions WHERE parent_region_id = ?', [regionId],
  );
  return rows.map(mapRegion);
}

export async function listSources(): Promise<Source[]> {
  const [rows] = await pool.query<RowDataPacket[]>('SELECT * FROM sources');
  return rows.map(r => ({
    id: r.id, title: r.title, titleEn: r.title_en ?? undefined,
    author: r.author ?? undefined, url: r.url ?? undefined,
    publisher: r.publisher ?? undefined, year: r.year ?? undefined,
    note: r.note ?? undefined, license: r.license ?? undefined,
  }));
}

export async function findSourceById(id: string): Promise<Source | undefined> {
  const [rows] = await pool.query<RowDataPacket[]>(
    'SELECT * FROM sources WHERE id = ?', [id],
  );
  if (!rows.length) return undefined;
  const r = rows[0];
  return {
    id: r.id, title: r.title, titleEn: r.title_en ?? undefined,
    author: r.author ?? undefined, url: r.url ?? undefined,
    publisher: r.publisher ?? undefined, year: r.year ?? undefined,
    note: r.note ?? undefined, license: r.license ?? undefined,
  };
}

export async function findSourcesForEvent(eventId: string): Promise<Source[]> {
  const event = await findEventById(eventId);
  if (!event || event.sourceIds.length === 0) return [];
  const placeholders = event.sourceIds.map(() => '?').join(',');
  const [rows] = await pool.query<RowDataPacket[]>(
    `SELECT * FROM sources WHERE id IN (${placeholders})`, event.sourceIds,
  );
  return rows.map(r => ({
    id: r.id, title: r.title, titleEn: r.title_en ?? undefined,
    author: r.author ?? undefined, url: r.url ?? undefined,
    publisher: r.publisher ?? undefined, year: r.year ?? undefined,
    note: r.note ?? undefined, license: r.license ?? undefined,
  }));
}

let _tagsCache: string[] | null = null;
let _tagsCacheTime = 0;
const TAGS_CACHE_TTL = 10 * 60 * 1000; // 10 minutes

export async function findAllTags(): Promise<string[]> {
  if (_tagsCache && Date.now() - _tagsCacheTime < TAGS_CACHE_TTL) {
    return _tagsCache;
  }
  const [pRows] = await pool.query<RowDataPacket[]>('SELECT DISTINCT tags FROM people WHERE data_status = ?', ['published']);
  const [eRows] = await pool.query<RowDataPacket[]>('SELECT DISTINCT tags FROM events WHERE data_status = ?', ['published']);
  const tagSet = new Set<string>();
  for (const r of pRows) {
    for (const t of parseJsonArray(r.tags)) tagSet.add(t);
  }
  for (const r of eRows) {
    for (const t of parseJsonArray(r.tags)) tagSet.add(t);
  }
  _tagsCache = Array.from(tagSet).sort();
  _tagsCacheTime = Date.now();
  return _tagsCache;
}

// ==================== Write operations ====================

export async function updatePersonStatus(
  ids: string[], status: DataStatus, reviewedBy: string,
): Promise<void> {
  if (ids.length === 0) return;
  const placeholders = ids.map(() => '?').join(',');
  await pool.query(
    `UPDATE people SET data_status = ?, last_reviewed_at = NOW(), reviewed_by = ? WHERE id IN (${placeholders})`,
    [status, reviewedBy, ...ids],
  );
}

export async function updateEventStatus(
  ids: string[], status: DataStatus, reviewedBy: string,
): Promise<void> {
  if (ids.length === 0) return;
  const placeholders = ids.map(() => '?').join(',');
  await pool.query(
    `UPDATE events SET data_status = ?, last_reviewed_at = NOW(), reviewed_by = ? WHERE id IN (${placeholders})`,
    [status, reviewedBy, ...ids],
  );
}

export async function updatePersonScore(
  id: string, score: number, reviewedBy: string,
): Promise<void> {
  await pool.query(
    'UPDATE people SET confidence_score = ?, last_reviewed_at = NOW(), reviewed_by = ? WHERE id = ?',
    [score, reviewedBy, id],
  );
}

export async function updateEventScore(
  id: string, score: number, reviewedBy: string,
): Promise<void> {
  await pool.query(
    'UPDATE events SET confidence_score = ?, last_reviewed_at = NOW(), reviewed_by = ? WHERE id = ?',
    [score, reviewedBy, id],
  );
}
