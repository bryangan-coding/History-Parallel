'use server';

import { revalidatePath } from 'next/cache';
import type { DataStatus } from '@/lib/types';
import { auth } from '@/auth';
import {
  updatePersonStatus as dbUpdatePersonStatus,
  updatePersonScore as dbUpdatePersonScore,
  updateEventStatus as dbUpdateEventStatus,
  updateEventScore as dbUpdateEventScore,
} from '@/server/db/queries';

/**
 * Require an authenticated admin session.
 * Throws if not logged in — defense in depth on top of the middleware guard.
 */
async function requireAdmin(): Promise<string> {
  const session = await auth();
  if (!session?.user?.email) {
    throw new Error('Unauthorized: admin session required');
  }
  return session.user.email;
}

export async function setPersonStatus(ids: string[], status: DataStatus): Promise<{ updated: number }> {
  const reviewer = await requireAdmin();
  await dbUpdatePersonStatus(ids, status, reviewer);
  revalidatePath('/admin/review/people');
  revalidatePath('/admin');
  return { updated: ids.length };
}

export async function setPersonScore(id: string, score: number): Promise<{ updated: number }> {
  const reviewer = await requireAdmin();
  await dbUpdatePersonScore(id, score, reviewer);
  revalidatePath('/admin/review/people');
  return { updated: 1 };
}

export async function setEventStatus(ids: string[], status: DataStatus): Promise<{ updated: number }> {
  const reviewer = await requireAdmin();
  await dbUpdateEventStatus(ids, status, reviewer);
  revalidatePath('/admin/review/events');
  revalidatePath('/admin');
  return { updated: ids.length };
}

export async function setEventScore(id: string, score: number): Promise<{ updated: number }> {
  const reviewer = await requireAdmin();
  await dbUpdateEventScore(id, score, reviewer);
  revalidatePath('/admin/review/events');
  return { updated: 1 };
}
