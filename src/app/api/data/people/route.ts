import { NextRequest, NextResponse } from 'next/server';
import { people, personMap } from '@/data/mockData';
import type { Person } from '@/lib/types';
import { ERAS } from '@/lib/eras.js';

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

  let items: Person[];

  if (ids && ids.length > 0) {
    items = ids.map((id) => personMap.get(id)).filter(Boolean) as Person[];
    return NextResponse.json({ items, total: items.length });
  }

  // Base filter
  if (publishedOnly) {
    items = people.filter((p) => p.dataStatus === 'published');
  } else {
    items = [...people];
  }

  // Status filter (for admin review UI)
  if (status && status !== 'all') {
    items = items.filter((p) => p.dataStatus === status);
  }

  // Region filter
  if (region && region !== 'all') {
    items = items.filter((p) => p.regionId === region);
  }

  // Search query
  if (query) {
    const q = query.toLowerCase();
    items = items.filter(
      (p) =>
        p.name.toLowerCase().includes(q) ||
        p.nameEn?.toLowerCase().includes(q) ||
        p.alternativeNames.some((a) => a.toLowerCase().includes(q)) ||
        p.tags.some((t) => t.toLowerCase().includes(q)) ||
        p.summary?.toLowerCase().includes(q) ||
        p.summaryEn?.toLowerCase().includes(q)
    );
  }

  // Era filter (exclusive upper bound, matching eras.js semantics)
  if (era) {
    const range = ERA_MAP[era];
    if (range) {
      items = items.filter((p) => {
        const y = p.birthYear ?? 0;
        if (!isFinite(range.max)) return y >= range.min;
        return y >= range.min && y < range.max;
      });
    }
  }

  const total = items.length;
  const start = (page - 1) * limit;
  const paged = items.slice(start, start + limit);

  return NextResponse.json({
    items: paged,
    total,
    page,
    limit,
    totalPages: Math.ceil(total / limit),
  });
}
