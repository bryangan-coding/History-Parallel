/**
 * Auth.js main configuration — Node runtime only.
 *
 * This file imports better-sqlite3 (via db/index.ts) and must NOT be
 * imported by middleware.ts or any Edge-runtime code.
 *
 * Middleware imports from auth/config.ts (edge-safe) only.
 */

import NextAuth from 'next-auth';
import Credentials from 'next-auth/providers/credentials';
import { DrizzleAdapter } from '@auth/drizzle-adapter';
import { eq } from 'drizzle-orm';
import bcrypt from 'bcryptjs';
import { authConfig } from './auth/config';
import { db } from '@/server/db';
import { user } from '@/server/db/schema';

export const { handlers, auth, signIn, signOut } = NextAuth({
  ...authConfig,
  adapter: DrizzleAdapter(db),
  providers: [
    Credentials({
      name: 'credentials',
      credentials: {
        username: { label: 'Username', type: 'text' },
        password: { label: 'Password', type: 'password' },
      },
      async authorize(credentials) {
        if (!credentials?.username || !credentials?.password) {
          return null;
        }

        const username = credentials.username as string;
        const password = credentials.password as string;

        const foundUser = await db
          .select()
          .from(user)
          .where(eq(user.email, username)) // we use email field as username
          .limit(1)
          .then((rows) => rows[0]);

        if (!foundUser || !foundUser.passwordHash) {
          return null;
        }

        const isValid = await bcrypt.compare(password, foundUser.passwordHash);
        if (!isValid) {
          return null;
        }

        return {
          id: foundUser.id,
          name: foundUser.name,
          email: foundUser.email,
        };
      },
    }),
  ],
  session: {
    strategy: 'jwt',
  },
  callbacks: {
    async jwt({ token, user: dbUser }) {
      if (dbUser) {
        token.id = dbUser.id;
        token.email = dbUser.email;
        token.name = dbUser.name;
      }
      return token;
    },
    async session({ session, token }) {
      if (session.user) {
        session.user.id = token.id as string;
        session.user.email = token.email as string;
        session.user.name = token.name as string;
      }
      return session;
    },
  },
});
