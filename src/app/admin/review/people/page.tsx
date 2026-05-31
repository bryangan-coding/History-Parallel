'use client';

import { useLocale } from '@/i18n/LocaleProvider';
import { people as allPeople } from '@/data/mockData';
import { personName, personSummary } from '@/lib/types';
import Link from 'next/link';

export default function AdminReviewPeoplePage() {
  const { locale } = useLocale();

  const reviewPeople = allPeople.filter((p) => p.dataStatus !== 'published');

  return (
    <div className="max-w-4xl mx-auto p-6">
      <div className="flex items-center gap-4 mb-6">
        <Link href="/admin/imports" className="text-sm text-stone-500 hover:text-stone-700">← Imports</Link>
        <h1 className="text-xl font-bold text-stone-900">Review: People</h1>
        <span className="text-xs bg-amber-100 text-amber-700 px-2 py-0.5 rounded">{reviewPeople.length} pending</span>
      </div>

      {reviewPeople.length === 0 ? (
        <p className="text-stone-400 text-sm">No people pending review.</p>
      ) : (
        <div className="space-y-3">
          {reviewPeople.map((p) => (
            <div key={p.id} className="border border-stone-200 rounded-xl bg-white p-4">
              <div className="flex items-start justify-between">
                <div>
                  <h3 className="font-semibold text-stone-900">{personName(p, locale)}</h3>
                  <p className="text-xs text-stone-400">
                    {p.birthYear ?? '?'}–{p.deathYear ?? '?'} · {p.regionId ?? 'No region'}
                  </p>
                  <p className="text-sm text-stone-500 mt-1">{personSummary(p, locale)}</p>
                  {p.wikidataQid && (
                    <span className="text-xs text-blue-500 font-mono">{p.wikidataQid}</span>
                  )}
                </div>
                <StatusBadge status={p.dataStatus} score={p.confidenceScore} />
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
