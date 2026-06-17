/**
 * Middleware — guards /admin/* routes.
 *
 * This runs on Edge runtime. It creates its own NextAuth instance
 * using ONLY the edge-safe authConfig (no DB adapter, no better-sqlite3).
 * Session is verified from the JWT cookie only — no DB access.
 *
 * The full auth config (with adapter + providers) lives in src/auth.ts (Node runtime).
 */

import NextAuth from 'next-auth';
import { authConfig } from '@/auth/config';

const edgeAuth = NextAuth(authConfig);

export default edgeAuth.auth;

export const config = {
  matcher: ['/admin/:path*'],
};
