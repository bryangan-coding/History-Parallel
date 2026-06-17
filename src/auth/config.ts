/**
 * Auth.js configuration — edge-safe.
 *
 * This file is imported by middleware.ts (which runs on Edge runtime).
 * It must NOT import better-sqlite3 or any Node-only modules.
 * The Credentials provider is defined here (edge-compatible) but actual
 * password verification happens in src/auth.ts (Node runtime).
 */

import type { NextAuthConfig } from 'next-auth';

export const authConfig: NextAuthConfig = {
  pages: {
    signIn: '/login',
  },
  callbacks: {
    authorized({ auth, request: { nextUrl } }) {
      const isLoggedIn = !!auth?.user;
      const isOnAdmin = nextUrl.pathname.startsWith('/admin');

      if (isOnAdmin) {
        if (isLoggedIn) return true;
        // Redirect to login with callback URL
        return false; // next-auth will redirect to signIn page
      }
      return true;
    },
  },
  providers: [], // Credentials provider added in src/auth.ts (Node runtime)
  trustHost: true,
};
