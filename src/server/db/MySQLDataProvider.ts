/**
 * MySQLDataProvider — 历史平行线 MySQL 数据访问层
 *
 * 替代 SupabaseDataProvider 骨架，直接连接本地 MySQL 数据库。
 * 所有方法实现 DataProvider 接口，页面/组件层无需改动。
 *
 * 使用方式：设置环境变量 NEXT_PUBLIC_DATA_PROVIDER=mysql
 * 默认值保持 mock（兼容无 MySQL 环境）
 */
import type {
  Region,
  Person,
  HistoricalEvent,
  Source,
  ParallelRegionGroup,
  ScoredEvent,
  TimeRange,
} from '@/lib/types';
import type { DataProvider } from '@/lib/dataProvider';
import pool, { parseJsonArray } from '@/server/db/mysql';
import type { RowDataPacket } from 'mysql2';

// ============================================================
// Row mappers — convert DB rows to TypeScript types
// ============================================================

function mapRegion(row: RowDataPacket): Region {
  return {
    id: row.id,
    name: row.name,
    nameEn: row.name_en ?? undefined,
    slug: row.slug,
    parentRegionId: row.parent_region_id ?? undefined,
    description: row.description ?? undefined,
    descriptionEn: row.description_en ?? undefined,
  };
}

function mapPerson(row: RowDataPacket): Person {
  return {
    id: row.id,
    name: row.name,
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
    dataStatus: (row.data_status ?? 'imported') as Person['dataStatus'],
    confidenceScore: row.confidence_score ?? 0.5,
    externalReferences: [],
    lastReviewedAt: row.last_reviewed_at ?? undefined,
    reviewedBy: row.reviewed_by ?? undefined,
  };
}

function mapEvent(row: RowDataPacket): HistoricalEvent {
  return {
    id: row.id,
    title: row.title,
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
      if (typeof row.coordinates === 'object') return row.coordinates as { lat: number; lng: number };
      try { return JSON.parse(row.coordinates as string) as { lat: number; lng: number }; }
      catch { return undefined; }
    })(),
    personIds: parseJsonArray(row.person_ids),
    tags: parseJsonArray(row.tags),
    tagsEn: parseJsonArray(row.tags_en),
    importance: (row.importance ?? 2) as HistoricalEvent['importance'],
    summary: row.summary ?? undefined,
    summaryEn: row.summary_en ?? undefined,
    description: row.description ?? undefined,
    descriptionEn: row.description_en ?? undefined,
    sourceIds: parseJsonArray(row.source_ids),
    relatedEventIds: parseJsonArray(row.related_event_ids),
    wikidataQid: row.wikidata_qid ?? undefined,
    wikipediaPageId: row.wikipedia_page_id ?? undefined,
    wikipediaSlug: row.wikipedia_slug ?? undefined,
    dataStatus: (row.data_status ?? 'published') as HistoricalEvent['dataStatus'],
    confidenceScore: row.confidence_score ?? 0.5,
    externalReferences: [],
    lastReviewedAt: row.last_reviewed_at ?? undefined,
    reviewedBy: row.reviewed_by ?? undefined,
  };
}

function mapSource(row: RowDataPacket): Source {
  return {
    id: row.id,
    title: row.title,
    titleEn: row.title_en ?? undefined,
    author: row.author ?? undefined,
    url: row.url ?? undefined,
    publisher: row.publisher ?? undefined,
    year: row.year ?? undefined,
    note: row.note ?? undefined,
    license: row.license ?? undefined,
  };
}

// ============================================================
// MySQLDataProvider
// ============================================================

export class MySQLDataProvider implements DataProvider {
  // ---- Regions ----

  async getRegions(): Promise<Region[]> {
    const [rows] = await pool.query<RowDataPacket[]>('SELECT * FROM regions');
    return rows.map(mapRegion);
  }

  async getRegionById(id: string): Promise<Region | undefined> {
    const [rows] = await pool.query<RowDataPacket[]>(
      'SELECT * FROM regions WHERE id = ?', [id],
    );
    return rows.length ? mapRegion(rows[0]) : undefined;
  }

  // ---- Persons ----

  async getPersons(): Promise<Person[]> {
    // WARNING: This loads ALL published people (~77K rows) into memory.
    // Prefer findPeopleByIds() or listPeople() with pagination in production code.
    // Hard limit of 5000 to prevent OOM.
    const [rows] = await pool.query<RowDataPacket[]>(
      'SELECT * FROM people WHERE data_status = ? LIMIT 5000', ['published'],
    );
    return rows.map(mapPerson);
  }

  async getPersonById(id: string): Promise<Person | undefined> {
    const [rows] = await pool.query<RowDataPacket[]>(
      'SELECT * FROM people WHERE id = ?', [id],
    );
    return rows.length ? mapPerson(rows[0]) : undefined;
  }

  async getPersonsForEvent(eventId: string): Promise<Person[]> {
    const [rows] = await pool.query<RowDataPacket[]>(
      `SELECT p.* FROM people p
       INNER JOIN event_persons ep ON p.id = ep.person_id
       WHERE ep.event_id = ?`, [eventId],
    );
    return rows.map(mapPerson);
  }

  // ---- Events ----

  async getEvents(): Promise<HistoricalEvent[]> {
    // WARNING: This loads ALL published events (~891K rows) into memory.
    // Prefer findEventsByYearRange() or listEvents() with filtering in production code.
    // Hard limit of 5000 to prevent OOM.
    const [rows] = await pool.query<RowDataPacket[]>(
      'SELECT * FROM events WHERE data_status = ? LIMIT 5000', ['published'],
    );
    return rows.map(mapEvent);
  }

  async getEventById(id: string): Promise<HistoricalEvent | undefined> {
    const [rows] = await pool.query<RowDataPacket[]>(
      'SELECT * FROM events WHERE id = ?', [id],
    );
    return rows.length ? mapEvent(rows[0]) : undefined;
  }

  async getEventsForPerson(personId: string): Promise<HistoricalEvent[]> {
    const [rows] = await pool.query<RowDataPacket[]>(
      `SELECT e.* FROM events e
       INNER JOIN event_persons ep ON e.id = ep.event_id
       WHERE ep.person_id = ? AND e.data_status = 'published'`,
      [personId],
    );
    return rows.map(mapEvent);
  }

  async getEventsByYearRange(startYear: number, endYear: number): Promise<HistoricalEvent[]> {
    const [rows] = await pool.query<RowDataPacket[]>(
      `SELECT * FROM events 
       WHERE data_status = 'published' 
       AND start_year IS NOT NULL
       AND (
         (start_year >= ? AND start_year <= ?)
         OR (end_year IS NOT NULL AND end_year >= ? AND end_year <= ?)
         OR (start_year <= ? AND end_year IS NOT NULL AND end_year >= ?)
       )
       ORDER BY start_year
       LIMIT 2000`,
      [startYear, endYear, startYear, endYear, startYear, endYear],
    );
    return rows.map(mapEvent);
  }

  // ---- Sources ----

  async getSources(): Promise<Source[]> {
    const [rows] = await pool.query<RowDataPacket[]>('SELECT * FROM sources');
    return rows.map(mapSource);
  }

  async getSourceById(id: string): Promise<Source | undefined> {
    const [rows] = await pool.query<RowDataPacket[]>(
      'SELECT * FROM sources WHERE id = ?', [id],
    );
    return rows.length ? mapSource(rows[0]) : undefined;
  }

  async getSourcesForEvent(eventId: string): Promise<Source[]> {
    const [eventRows] = await pool.query<RowDataPacket[]>(
      'SELECT source_ids FROM events WHERE id = ?', [eventId],
    );
    if (!eventRows.length) return [];
    const sourceIds = parseJsonArray(eventRows[0].source_ids);
    if (!sourceIds.length) return [];

    const placeholders = sourceIds.map(() => '?').join(',');
    const [rows] = await pool.query<RowDataPacket[]>(
      `SELECT * FROM sources WHERE id IN (${placeholders})`, sourceIds,
    );
    return rows.map(mapSource);
  }

  // ---- Search ----

  async search(query: string) {
    // Server-side search using MySQL LIKE for simplicity
    // For production, consider full-text indexes (FULLTEXT on title/summary)
    const q = `%${query}%`;

    const [people] = await pool.query<RowDataPacket[]>(
      `SELECT * FROM people 
       WHERE data_status = 'published' 
       AND (name LIKE ? OR name_en LIKE ? OR summary LIKE ? OR summary_en LIKE ?)
       LIMIT 100`,
      [q, q, q, q],
    );

    const [events] = await pool.query<RowDataPacket[]>(
      `SELECT * FROM events 
       WHERE data_status = 'published' 
       AND (title LIKE ? OR title_en LIKE ? OR summary LIKE ?)
       LIMIT 100`,
      [q, q, q],
    );

    const [regions] = await pool.query<RowDataPacket[]>(
      `SELECT * FROM regions 
       WHERE name LIKE ? OR name_en LIKE ? OR description LIKE ?
       LIMIT 20`,
      [q, q, q],
    );

    // Year search: if query is a number, find events near that year
    const yearNum = parseInt(query, 10);
    let yearMatches: { year: number; nearEvents: HistoricalEvent[]; label: string }[] = [];

    if (!isNaN(yearNum)) {
      const range = 20;
      const [nearEvents] = await pool.query<RowDataPacket[]>(
        `SELECT * FROM events 
         WHERE data_status = 'published'
         AND start_year IS NOT NULL
         AND (
           ABS(start_year - ?) <= ?
           OR (end_year IS NOT NULL AND ABS(end_year - ?) <= ?)
           OR (start_year <= ? AND end_year IS NOT NULL AND end_year >= ?)
         )
         LIMIT 50`,
        [yearNum, range, yearNum, range, yearNum, yearNum],
      );
      if (nearEvents.length > 0) {
        yearMatches = [{
          year: yearNum,
          nearEvents: nearEvents.map(mapEvent),
          label: `${yearNum}年前后的事件`,
        }];
      }
    }

    return {
      people: people.map(mapPerson),
      events: events.map(mapEvent),
      regions: regions.map(mapRegion),
      yearMatches,
    };
  }

  // ---- Parallel events ----

  async getParallelEvents(opts: {
    year: number;
    range?: TimeRange;
    focusEventId?: string;
    focusPersonId?: string;
  }): Promise<ParallelRegionGroup[]> {
    const { year, range = 20 } = opts;
    const minYear = year - range;
    const maxYear = year + range;

    // Fetch published events in time window
    const [rows] = await pool.query<RowDataPacket[]>(
      `SELECT * FROM events 
       WHERE data_status = 'published'
       AND start_year IS NOT NULL
       AND (
         (start_year >= ? AND start_year <= ?)
         OR (end_year IS NOT NULL AND end_year >= ? AND end_year <= ?)
         OR (start_year <= ? AND end_year IS NOT NULL AND end_year >= ?)
       )
       ORDER BY start_year
       LIMIT 2000`,
      [minYear, maxYear, minYear, maxYear, minYear, maxYear],
    );

    const events = rows.map(mapEvent);

    // Score each event (same algorithm as parallel.ts)
    const scored: ScoredEvent[] = events.map((event) => {
      let score = 100;
      const eventStart = event.startYear ?? 0;
      const eventMid = event.endYear ? (eventStart + event.endYear) / 2 : eventStart;
      const distance = Math.abs(eventMid - year);
      score -= distance * 3;
      score += event.importance * 10;

      if (opts.focusEventId && event.id === opts.focusEventId) score += 200;
      if (opts.focusPersonId && event.personIds.includes(opts.focusPersonId)) score += 100;

      return { event, persons: [], score, distanceFromFocus: distance };
    });

    // Group by region
    const grouped = new Map<string, ScoredEvent[]>();
    for (const s of scored) {
      const regionId = s.event.regionId ?? 'unknown';
      if (!grouped.has(regionId)) grouped.set(regionId, []);
      grouped.get(regionId)!.push(s);
    }

    // Sort within groups
    for (const [, evts] of grouped) {
      evts.sort((a, b) => b.score - a.score);
    }

    // Build result with region info
    const regionMap = new Map<string, Region>();
    const allRegions = await this.getRegions();
    for (const r of allRegions) regionMap.set(r.id, r);

    const result: ParallelRegionGroup[] = [];
    for (const [regionId, evts] of grouped) {
      const region = regionMap.get(regionId);
      if (!region) continue;
      result.push({ region, events: evts });
    }

    result.sort((a, b) => {
      const aTop = a.events[0]?.score ?? 0;
      const bTop = b.events[0]?.score ?? 0;
      return bTop - aTop;
    });

    return result;
  }
}
