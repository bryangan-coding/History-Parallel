import { NextRequest, NextResponse } from 'next/server';
import { ERAS } from '@/lib/eras.js';
import { listPeople, findPeopleByIds } from '@/server/db/queries';
import { auth } from '@/auth';

// Compute ERA_MAP from shared definitions (exclusive upper bound)
const ERA_MAP: Record<string, { min: number; max: number }> = Object.fromEntries(
  ERAS.map((era) => [
    era.key,
    { min: era.min, max: era.max === null ? Infinity : era.max },
  ])
);

export async function GET(request: NextRequest) {
  const { searchParams } = request.nextUrl;
  const page = Math.max(1, parseInt(searchParams.get('page') || '1'));
  const limit = Math.min(Math.max(1, parseInt(searchParams.get('limit') || '50')), 200);
  const ids = searchParams.get('ids')?.split(',').filter(Boolean);
  const publishedOnly = searchParams.get('published') !== 'false';
  const query = searchParams.get('q')?.trim();
  const era = searchParams.get('era');
  const status = searchParams.get('status');
  const region = searchParams.get('region');

  // Lookup by IDs
  if (ids && ids.length > 0) {
    const items = await findPeopleByIds(ids);
    return NextResponse.json({ items, total: items.length });
  }

  // Determine if this request needs auth (non-public data access)
  const needsAuth = !publishedOnly || (status && status !== 'all');
  if (needsAuth) {
    const session = await auth();
    if (!session) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }
  }

  // Build DB query options
  const opts: Parameters<typeof listPeople>[0] = { page, limit };

  if (status && status !== 'all') {
    opts.dataStatus = status;
  } else {
    // Default: only published data for public access
    opts.publishedOnly = true;
  }

  if (region && region !== 'all') {
    opts.regionId = region;
  }

  if (query) {
    opts.query = query;
  }

  // Era filter
  if (era) {
    const range = ERA_MAP[era];
    if (range) {
      opts.era = {
        min: range.min,
        max: isFinite(range.max) ? range.max : null,
      };
    }
  }

  const { items, total } = await listPeople(opts);

  return NextResponse.json({
    items,
    total,
    page,
    limit,
    totalPages: Math.ceil(total / limit),
  });
}
