/**
 * Create an admin user in the database.
 *
 * Usage: npx tsx scripts/create-admin.ts <username> <password>
 *   e.g. npx tsx scripts/create-admin.ts admin my-secret-password
 *
 * The password is hashed with bcrypt before storage.
 */

import bcrypt from 'bcryptjs';
import { resolve } from 'node:path';
import { mkdirSync } from 'node:fs';

// Set DATABASE_URL if not set
process.env.DATABASE_URL = process.env.DATABASE_URL || 'file:./data/db.sqlite';

import Database from 'better-sqlite3';
import { drizzle } from 'drizzle-orm/better-sqlite3';
import { user } from '../src/server/db/schema';
import { eq } from 'drizzle-orm';

const DB_PATH = resolve(process.cwd(), process.env.DATABASE_URL.replace('file:', ''));
mkdirSync(resolve(DB_PATH, '..'), { recursive: true });

const sqlite = new Database(DB_PATH);
sqlite.pragma('journal_mode = WAL');
sqlite.pragma('foreign_keys = ON');
const db = drizzle(sqlite);

async function main() {
  const username = process.argv[2];
  const password = process.argv[3];

  if (!username || !password) {
    console.error('Usage: npx tsx scripts/create-admin.ts <username> <password>');
    console.error('Example: npx tsx scripts/create-admin.ts admin my-secret-password');
    process.exit(1);
  }

  // Check if user already exists
  const existing = await db
    .select()
    .from(user)
    .where(eq(user.email, username))
    .limit(1)
    .then((rows) => rows[0]);

  if (existing) {
    const hash = await bcrypt.hash(password, 12);
    await db
      .update(user)
      .set({ passwordHash: hash })
      .where(eq(user.email, username));
    console.log(`✅ Password updated for existing user: ${username}`);
  } else {
    const hash = await bcrypt.hash(password, 12);
    const id = `usr-${Date.now()}`;
    await db.insert(user).values({
      id,
      name: username,
      email: username, // use email field as username
      passwordHash: hash,
      role: 'admin',
      emailVerified: true,
    });
    console.log(`✅ Admin user created: ${username} (id: ${id})`);
  }

  sqlite.close();
}

main().catch((err) => {
  console.error('Failed:', err);
  process.exit(1);
});
