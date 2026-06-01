/**
 * Core type definitions for 历史平行线 (History Parallel)
 */

/** Supported locale */
export type Locale = 'zh' | 'en';

// ==================== Data Pipeline Types ====================

export type DatePrecision =
  | 'day'
  | 'month'
  | 'year'
  | 'decade'
  | 'century'
  | 'range'
  | 'unknown';

export type DataStatus =
  | 'imported'
  | 'needs_review'
  | 'verified'
  | 'published'
  | 'rejected';

export type SourceType =
  | 'wikidata'
  | 'wikipedia'
  | 'manual'
  | 'book'
  | 'article'
  | 'encyclopedia'
  | 'museum'
  | 'archive'
  | 'other';

export interface ExternalReference {
  id: string;
  sourceType: SourceType;
  externalId?: string;
  url?: string;
  title?: string;
  author?: string;
  publisher?: string;
  year?: number;
  license?: string;
  retrievedAt?: string;
  note?: string;
}

// ==================== Core Entity Types ====================

/** A geographic or civilizational region */
export interface Region {
  id: string;
  name: string;
  nameEn?: string;
  slug: string;
  parentRegionId?: string;
  description?: string;
  descriptionEn?: string;
}

/** A historical person */
export interface Person {
  id: string;
  name: string;
  nameEn?: string;
  alternativeNames: string[];
  birthYear?: number;
  deathYear?: number;
  birthDatePrecision?: DatePrecision;
  deathDatePrecision?: DatePrecision;
  regionId?: string;
  civilizationId?: string;
  occupations: string[];
  tags: string[];
  tagsEn?: string[];
  summary?: string;
  summaryEn?: string;
  description?: string;
  descriptionEn?: string;
  sourceIds: string[];

  // Wikidata integration
  wikidataQid?: string;
  wikipediaPageId?: string;
  wikipediaSlug?: string;

  // Data pipeline
  dataStatus: DataStatus;
  confidenceScore: number;
  externalReferences: ExternalReference[];
  lastReviewedAt?: string;
  reviewedBy?: string;
}

/** A historical event */
export interface HistoricalEvent {
  id: string;
  title: string;
  titleEn?: string;
  startYear?: number;
  endYear?: number;
  startDateText?: string;
  endDateText?: string;
  approximateDateText?: string;
  datePrecision: DatePrecision;
  isApproximate: boolean;

  regionId?: string;
  civilizationId?: string;
  placeName?: string;
  placeNameEn?: string;
  coordinates?: {
    lat: number;
    lng: number;
  };

  personIds: string[];
  tags: string[];
  tagsEn?: string[];
  importance: 1 | 2 | 3 | 4 | 5;

  summary?: string;
  summaryEn?: string;
  description?: string;
  descriptionEn?: string;
  sourceIds: string[];
  relatedEventIds: string[];

  // Wikidata integration
  wikidataQid?: string;
  wikipediaPageId?: string;
  wikipediaSlug?: string;

  // Data pipeline
  dataStatus: DataStatus;
  confidenceScore: number;
  externalReferences: ExternalReference[];
  lastReviewedAt?: string;
  reviewedBy?: string;
}

/** A source citation */
export interface Source {
  id: string;
  title: string;
  titleEn?: string;
  author?: string;
  url?: string;
  publisher?: string;
  year?: number;
  note?: string;
  license?: string;
}

// ==================== Search & Parallel Types ====================

/** Search result types for grouping */
export interface SearchResult {
  people: Person[];
  events: HistoricalEvent[];
  regions: Region[];
  yearMatches: YearMatch[];
}

/** A year-based search match */
export interface YearMatch {
  year: number;
  nearEvents: HistoricalEvent[];
  label: string;
}

/** Parallel event grouped by region */
export interface ParallelRegionGroup {
  region: Region;
  events: ScoredEvent[];
}

/** An event with its relevance score */
export interface ScoredEvent {
  event: HistoricalEvent;
  persons: Person[];
  score: number;
  distanceFromFocus: number;
}

/** Time range options for parallel view */
export type TimeRange = 0 | 5 | 20 | 100;

/** Route parameter for the parallel page */
export interface ParallelPageParams {
  year: number;
  startYear?: number;
  endYear?: number;
  focusEvent?: string;
  personId?: string;
  range?: TimeRange;
}

// ==================== Data Pipeline Helpers ====================

/** Check if an entity has published status */
export function isPublished(entity: { dataStatus: DataStatus }): boolean {
  return entity.dataStatus === 'published';
}

/** Filter a list to only published items */
export function filterPublished<T extends { dataStatus: DataStatus }>(items: T[]): T[] {
  return items.filter(isPublished);
}

// ==================== i18n accessors ====================

/** Get localized name for a person */
export function personName(p: Person, locale: Locale): string {
  return (locale === 'en' && p.nameEn) ? p.nameEn : p.name;
}

/** Get localized summary for a person */
export function personSummary(p: Person, locale: Locale): string {
  return (locale === 'en' && p.summaryEn) ? p.summaryEn : p.summary ?? '';
}

/** Get localized tags for a person */
export function personTags(p: Person, locale: Locale): string[] {
  return (locale === 'en' && p.tagsEn?.length) ? p.tagsEn : p.tags;
}

/** Get localized name for a region */
export function regionName(r: Region, locale: Locale): string {
  return (locale === 'en' && r.nameEn) ? r.nameEn : r.name;
}

/** Get localized description for a region */
export function regionDescription(r: Region, locale: Locale): string | undefined {
  return (locale === 'en' && r.descriptionEn) ? r.descriptionEn : r.description;
}

/** Get localized title for an event */
export function eventTitle(e: HistoricalEvent, locale: Locale): string {
  return (locale === 'en' && e.titleEn) ? e.titleEn : e.title;
}

/** Get localized summary for an event */
export function eventSummary(e: HistoricalEvent, locale: Locale): string {
  return (locale === 'en' && e.summaryEn) ? e.summaryEn : e.summary ?? '';
}

/** Get localized description for an event */
export function eventDescription(e: HistoricalEvent, locale: Locale): string {
  return (locale === 'en' && e.descriptionEn) ? e.descriptionEn : e.description ?? '';
}

/** Get localized place name for an event */
export function eventPlaceName(e: HistoricalEvent, locale: Locale): string | undefined {
  return (locale === 'en' && e.placeNameEn) ? e.placeNameEn : e.placeName;
}

/** Get localized tags for an event */
export function eventTags(e: HistoricalEvent, locale: Locale): string[] {
  return (locale === 'en' && e.tagsEn?.length) ? e.tagsEn : e.tags;
}
