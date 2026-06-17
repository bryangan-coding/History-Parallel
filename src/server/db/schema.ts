/**
 * Drizzle ORM schema — SQLite.
 *
 * Aligns with src/lib/types.ts (Person, HistoricalEvent, Source, Region)
 * plus Auth.js required tables (user, session, account, verificationToken).
 */

import { sqliteTable, text, integer, real } from 'drizzle-orm/sqlite-core';
import { relations } from 'drizzle-orm';

// ==================== Auth.js tables ====================
// Required by @auth/drizzle-adapter

export const user = sqliteTable('user', {
  id: text('id').primaryKey(),
  name: text('name').notNull(),
  email: text('email').notNull().unique(),
  emailVerified: integer('email_verified', { mode: 'boolean' }),
  image: text('image'),
  passwordHash: text('password_hash'),
  role: text('role').default('admin'), // future: 'admin' | 'editor' | 'viewer'
  createdAt: integer('created_at', { mode: 'timestamp' }).$defaultFn(() => new Date()),
});

export const session = sqliteTable('session', {
  id: text('id').primaryKey(),
  sessionToken: text('session_token').notNull().unique(),
  userId: text('user_id')
    .notNull()
    .references(() => user.id, { onDelete: 'cascade' }),
  expires: integer('expires', { mode: 'timestamp' }).notNull(),
});

export const account = sqliteTable('account', {
  id: text('id').primaryKey(),
  accountId: text('account_id').notNull(),
  providerId: text('provider_id').notNull(),
  userId: text('user_id')
    .notNull()
    .references(() => user.id, { onDelete: 'cascade' }),
  access_token: text('access_token'),
  refresh_token: text('refresh_token'),
  expires_at: integer('expires_at'),
  token_type: text('token_type'),
  scope: text('scope'),
  id_token: text('id_token'),
  session_state: text('session_state'),
});

export const verificationToken = sqliteTable('verification_token', {
  identifier: text('identifier').notNull(),
  token: text('token').notNull().unique(),
  expires: integer('expires', { mode: 'timestamp' }).notNull(),
});

// ==================== Application data tables ====================

/**
 * Historical person — aligns with Person in src/lib/types.ts
 */
export const person = sqliteTable('person', {
  id: text('id').primaryKey(),

  // Names
  name: text('name').notNull(),
  nameEn: text('name_en'),
  alternativeNames: text('alternative_names', { mode: 'json' }).$type<string[]>().default([]),

  // Dates
  birthYear: integer('birth_year'),
  deathYear: integer('death_year'),
  birthDatePrecision: text('birth_date_precision'), // DatePrecision enum as string
  deathDatePrecision: text('death_date_precision'),

  // Classification
  regionId: text('region_id'),
  civilizationId: text('civilization_id'),
  occupations: text('occupations', { mode: 'json' }).$type<string[]>().default([]),

  // Tags (i18n)
  tags: text('tags', { mode: 'json' }).$type<string[]>().default([]),
  tagsEn: text('tags_en', { mode: 'json' }).$type<string[]>().default([]),

  // Content (i18n)
  summary: text('summary'),
  summaryEn: text('summary_en'),
  description: text('description'),
  descriptionEn: text('description_en'),

  // Sources
  sourceIds: text('source_ids', { mode: 'json' }).$type<string[]>().default([]),

  // Wikidata integration
  wikidataQid: text('wikidata_qid'),
  wikipediaPageId: text('wikipedia_page_id'),
  wikipediaSlug: text('wikipedia_slug'),

  // Data pipeline
  dataStatus: text('data_status').notNull().default('imported'), // DataStatus enum as string
  confidenceScore: real('confidence_score').notNull().default(0),
  externalReferences: text('external_references', { mode: 'json' }).$type<unknown[]>().default([]),
  lastReviewedAt: text('last_reviewed_at'),
  reviewedBy: text('reviewed_by'),
});

/**
 * Historical event — aligns with HistoricalEvent in src/lib/types.ts
 */
export const event = sqliteTable('event', {
  id: text('id').primaryKey(),

  // Titles
  title: text('title').notNull(),
  titleEn: text('title_en'),

  // Dates
  startYear: integer('start_year'),
  endYear: integer('end_year'),
  startDateText: text('start_date_text'),
  endDateText: text('end_date_text'),
  approximateDateText: text('approximate_date_text'),
  datePrecision: text('date_precision').notNull().default('year'),
  isApproximate: integer('is_approximate', { mode: 'boolean' }).notNull().default(false),

  // Location
  regionId: text('region_id'),
  civilizationId: text('civilization_id'),
  placeName: text('place_name'),
  placeNameEn: text('place_name_en'),
  coordinates: text('coordinates', { mode: 'json' }).$type<{ lat: number; lng: number } | null>(),

  // Associations
  personIds: text('person_ids', { mode: 'json' }).$type<string[]>().default([]),

  // Tags (i18n)
  tags: text('tags', { mode: 'json' }).$type<string[]>().default([]),
  tagsEn: text('tags_en', { mode: 'json' }).$type<string[]>().default([]),

  // Importance
  importance: integer('importance').notNull().default(3),

  // Content (i18n)
  summary: text('summary'),
  summaryEn: text('summary_en'),
  description: text('description'),
  descriptionEn: text('description_en'),

  // Sources
  sourceIds: text('source_ids', { mode: 'json' }).$type<string[]>().default([]),

  // Related events
  relatedEventIds: text('related_event_ids', { mode: 'json' }).$type<string[]>().default([]),

  // Wikidata integration
  wikidataQid: text('wikidata_qid'),
  wikipediaPageId: text('wikipedia_page_id'),
  wikipediaSlug: text('wikipedia_slug'),

  // Data pipeline
  dataStatus: text('data_status').notNull().default('imported'),
  confidenceScore: real('confidence_score').notNull().default(0),
  externalReferences: text('external_references', { mode: 'json' }).$type<unknown[]>().default([]),
  lastReviewedAt: text('last_reviewed_at'),
  reviewedBy: text('reviewed_by'),
});

/**
 * Source citation — aligns with Source in src/lib/types.ts
 */
export const source = sqliteTable('source', {
  id: text('id').primaryKey(),
  title: text('title').notNull(),
  titleEn: text('title_en'),
  author: text('author'),
  url: text('url'),
  publisher: text('publisher'),
  year: integer('year'),
  note: text('note'),
  license: text('license'),
});

/**
 * Geographic/civilizational region — aligns with Region in src/lib/types.ts
 */
export const region = sqliteTable('region', {
  id: text('id').primaryKey(),
  name: text('name').notNull(),
  nameEn: text('name_en'),
  slug: text('slug').notNull().unique(),
  parentRegionId: text('parent_region_id'),
  description: text('description'),
  descriptionEn: text('description_en'),
});

// ==================== Relations (for Drizzle queries) ====================

export const userRelations = relations(user, ({ many }) => ({
  accounts: many(account),
  sessions: many(session),
}));

export const sessionRelations = relations(session, ({ one }) => ({
  user: one(user, { fields: [session.userId], references: [user.id] }),
}));

export const accountRelations = relations(account, ({ one }) => ({
  user: one(user, { fields: [account.userId], references: [user.id] }),
}));
