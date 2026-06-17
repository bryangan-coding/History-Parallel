import type { Config } from 'drizzle-kit';
import path from 'node:path';

export default {
  schema: './src/server/db/schema.ts',
  out: './drizzle',
  dialect: 'sqlite',
  dbCredentials: {
    url: process.env.DATABASE_URL || 'file:./data/db.sqlite',
  },
  tablesFilter: ['_*'],
} satisfies Config;
