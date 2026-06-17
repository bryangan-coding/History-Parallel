/**
 * Database singleton — better-sqlite3 + Drizzle ORM.
 *
 * IMPORTANT: better-sqlite3 is a native Node module and CANNOT run in
 * Edge runtime (middleware). All DB access must go through Node-runtime
 * server actions or route handlers.
 */

import 'server-only';
import Database from 'better-sqlite3';
import { drizzle } from 'drizzle-orm/better-sqlite3';
import * as schema from './schema';
import { resolve } from 'node:path';

const DB_PATH = resolve(process.cwd(), process.env.DATABASE_URL?.replace('file:', '') || 'data/db.sqlite');

// Ensure data directory exists
import { mkdirSync } from 'node:fs';
mkdirSync(resolve(process.cwd(), 'data'), { recursive: true });

const sqlite = new Database(DB_PATH);

// Enable WAL mode for better concurrent read performance
sqlite.pragma('journal_mode = WAL');
sqlite.pragma('foreign_keys = ON');

export const db = drizzle(sqlite, { schema });
export type Database = typeof db;
