'use client';

import { useLocale } from '@/i18n/LocaleProvider';
import { events as allEvents } from '@/data/mockData';
import { eventTitle, eventSummary } from '@/lib/types';
import Link from 'next/link';

export default function AdminReviewEventsPage() {
  const { locale } = useLocale();

  const reviewEvents = allEvents.filter((e) => e.dataStatus !== 'published');

  return (
    <div className="max-w-4xl mx-auto p-6">
      <div className="flex items-center gap-4 mb-6">
        <Link href="/admin/imports" className="text-sm text-stone-500 hover:text-stone-700">← Imports</Link>
        <h1 className="text-xl font-bold text-stone-900">Review: Events</h1>
        <span className="text-xs bg-amber-100 text-amber-700 px-2 py-0.5 rounded">{reviewEvents.length} pending</span>
      </div>

      {reviewEvents.length === 0 ? (
        <p className="text-stone-400 text-sm">No events pending review.</p>
      ) : (
        <div className="space-y-3">
          {reviewEvents.map((e) => (
            <div key={e.id} className="border border-stone-200 rounded-xl bg-white p-4">
              <div className="flex items-start justify-between">
                <div>
                  <h3 className="font-semibold text-stone-900">{eventTitle(e, locale)}</h3>
                  <p className="text-xs text-stone-400">
                    {e.startYear ?? '?'}{e.endYear && e.endYear !== e.startYear ? `–${e.endYear}` : ''} · {e.regionId ?? e.placeName ?? 'No location'}
                  </p>
                  <p className="text-sm text-stone-500 mt-1">{eventSummary(e, locale)}</p>
                </div>
                <StatusBadge status={e.dataStatus} score={e.confidenceScore} />
              </div>
              <div className="flex gap-2 mt-3 pt-3 border-t border-stone-100">
                <button className="text-xs px-3 py-1 rounded border border-green-200 text-green-700 hover:bg-green-50">Publish</button>
                <button className="text-xs px-3 py-1 rounded border border-amber-200 text-amber-700 hover:bg-amber-50">Needs Review</button>
                <button className="text-xs px-3 py-1 rounded border border-red-200 text-red-700 hover:bg-red-50">Reject</button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function StatusBadge({ status, score }: { status: string; score: number }) {
  const colors: Record<string, string> = {
    imported: 'bg-blue-100 text-blue-700',
    needs_review: 'bg-amber-100 text-amber-700',
    verified: 'bg-green-100 text-green-700',
    published: 'bg-emerald-100 text-emerald-700',
    rejected: 'bg-red-100 text-red-700',
  };
  return (
    <div className="flex flex-col items-end gap-1">
      <span className={`text-xs px-2 py-0.5 rounded ${colors[status] ?? 'bg-stone-100 text-stone-600'}`}>
        {status}
      </span>
      <span className="text-xs text-stone-400">{score.toFixed(2)}</span>
    </div>
  );
}
