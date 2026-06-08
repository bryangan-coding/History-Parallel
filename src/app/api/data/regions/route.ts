import { NextResponse } from 'next/server';
import { regions } from '@/data/mockData';

export async function GET() {
  return NextResponse.json({ items: regions });
}
