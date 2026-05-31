'use client';

import { useLocale } from '@/i18n/LocaleProvider';
import Link from 'next/link';

export default function AdminImportsPage() {
  const { t } = useLocale();

  const mockImportBatches = [
    { id: '1', name: 'wikidata-people-2026-05-31.json', count: 50, source: 'wikidata', date: '2026-05-31' },
  ];

  return (
    <div className="max-w-4xl mx-auto p-6">
      <div className="flex items-center gap-4 mb-6">
        <Link href="/" className="text-sm text-stone-500 hover:text-stone-700">← Back</Link>
        <h1 className="text-xl font-bold text-stone-900">Import Batches</h1>
      </div>

      <div className="border border-stone-200 rounded-xl bg-white overflow-hidden">
        <table className="w-full text-sm">
          <thead className="bg-stone-50 text-stone-500 uppercase text-xs">
            <tr>
              <th className="text-left p-3">File</th>
              <th className="text-left p-3">Source</th>
              <th className="text-right p-3">Count</th>
              <th className="text-right p-3">Date</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-stone-100">
            {mockImportBatches.map((batch) => (
              <tr key={batch.id} className="hover:bg-stone-50">
                <td className="p-3 font-mono text-xs">{batch.name}</td>
                <td className="p-3">{batch.source}</td>
                <td className="p-3 text-right">{batch.count}</td>
                <td className="p-3 text-right text-stone-400">{batch.date}</td>
              </tr>
            ))}
            {mockImportBatches.length === 0 && (
              <tr>
                <td colSpan={4} className="p-6 text-center text-stone-400">No import batches found.</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
