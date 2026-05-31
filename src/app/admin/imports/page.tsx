'use client';

import { useLocale } from '@/i18n/LocaleProvider';
import React, { useState } from 'react';
import Link from 'next/link';
import { ChevronDown, ChevronUp, Upload, X } from 'lucide-react';
import { regions } from '@/data/mockData';

type BatchStatus = 'processing' | 'completed' | 'failed';

interface ImportBatch {
  id: string;
  name: string;
  source: string;
  date: string;
  count: number;
  status: BatchStatus;
  imported: number;
  duplicates: number;
  needReview: number;
}

export default function AdminImportsPage() {
  const { t } = useLocale();
  const [batches, setBatches] = useState<ImportBatch[]>([
    { id: '1', name: 'wikidata-people-2026-05-31.json', source: 'wikidata', date: '2026-05-31', count: 50, status: 'completed', imported: 42, duplicates: 3, needReview: 5 },
    { id: '2', name: 'wikidata-events-2026-05-30.json', source: 'wikidata', date: '2026-05-30', count: 39, status: 'completed', imported: 30, duplicates: 4, needReview: 5 },
    { id: '3', name: 'manual-people-2026-05-28.json', source: 'manual', date: '2026-05-28', count: 15, status: 'processing', imported: 8, duplicates: 0, needReview: 7 },
    { id: '4', name: 'wikipedia-articles-2026-05-25.json', source: 'wikipedia', date: '2026-05-25', count: 22, status: 'completed', imported: 18, duplicates: 2, needReview: 2 },
    { id: '5', name: 'encyclopedia-import-2026-05-20.json', source: 'encyclopedia', date: '2026-05-20', count: 10, status: 'failed', imported: 0, duplicates: 0, needReview: 10 },
  ]);
  const [expandedId, setExpandedId] = useState<string | null>(null);
  const [showModal, setShowModal] = useState(false);
  const [isImporting, setIsImporting] = useState(false);

  // New import form state
  const [importSource, setImportSource] = useState('wikidata');
  const [yearFrom, setYearFrom] = useState('-500');
  const [yearTo, setYearTo] = useState('2000');
  const [importRegion, setImportRegion] = useState('');

  const toggleExpand = (id: string) => {
    setExpandedId(expandedId === id ? null : id);
  };

  const handleStartImport = () => {
    setIsImporting(true);
    setTimeout(() => {
      const newBatch: ImportBatch = {
        id: String(batches.length + 1),
        name: `${importSource}-import-${new Date().toISOString().split('T')[0]}.json`,
        source: importSource,
        date: new Date().toISOString().split('T')[0],
        count: Math.floor(Math.random() * 50) + 10,
        status: 'processing',
        imported: 0,
        duplicates: 0,
        needReview: 0,
      };
      setBatches([newBatch, ...batches]);
      setIsImporting(false);
      setShowModal(false);
      setImportSource('wikidata');
      setYearFrom('-500');
      setYearTo('2000');
      setImportRegion('');
    }, 1500);
  };

  const statusColors: Record<BatchStatus, string> = {
    completed: 'bg-emerald-100 text-emerald-700',
    processing: 'bg-blue-100 text-blue-700',
    failed: 'bg-red-100 text-red-700',
  };

  return (
    <div className="max-w-4xl">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <Link href="/admin" className="text-sm text-stone-400 hover:text-stone-600 transition-colors">
            ← Dashboard
          </Link>
          <h1 className="text-xl font-bold text-stone-900">Import Batches</h1>
        </div>
        <button
          onClick={() => setShowModal(true)}
          className="flex items-center gap-2 px-4 py-2 text-sm bg-stone-900 text-white rounded-lg hover:bg-stone-800 transition-colors active:scale-[0.98]"
        >
          <Upload size={14} />
          Start New Import
        </button>
      </div>

      <div className="border border-stone-200 rounded-xl bg-white overflow-hidden">
        <table className="w-full text-sm">
          <thead className="bg-stone-50 text-stone-500 uppercase text-xs tracking-wider">
            <tr>
              <th className="text-left p-3 w-8"></th>
              <th className="text-left p-3">File</th>
              <th className="text-left p-3">Source</th>
              <th className="text-right p-3">Count</th>
              <th className="text-left p-3">Status</th>
              <th className="text-right p-3">Date</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-stone-100">
            {batches.map((batch) => (
              <React.Fragment key={batch.id}>
                <tr
                  onClick={() => toggleExpand(batch.id)}
                  className="hover:bg-stone-50 cursor-pointer transition-colors"
                >
                  <td className="p-3 text-stone-400">
                    {expandedId === batch.id ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
                  </td>
                  <td className="p-3 font-mono text-xs text-stone-700">{batch.name}</td>
                  <td className="p-3">
                    <span className="text-xs px-2 py-0.5 rounded bg-stone-100 text-stone-600 capitalize">
                      {batch.source}
                    </span>
                  </td>
                  <td className="p-3 text-right text-stone-600">{batch.count}</td>
                  <td className="p-3">
                    <span className={`text-xs px-2 py-0.5 rounded-full ${statusColors[batch.status]} ${batch.status === 'processing' ? 'animate-pulse' : ''}`}>
                      {batch.status}
                    </span>
                  </td>
                  <td className="p-3 text-right text-stone-400 text-xs">{batch.date}</td>
                </tr>
                {expandedId === batch.id && (
                  <tr key={`${batch.id}-detail`}>
                    <td colSpan={6} className="bg-stone-50/50 p-4">
                      <div className="grid grid-cols-4 gap-4 text-sm">
                        <div className="border border-stone-200 rounded-lg bg-white p-3 text-center">
                          <div className="text-2xl font-bold text-blue-600">{batch.imported}</div>
                          <div className="text-xs text-stone-400 mt-1">Imported</div>
                        </div>
                        <div className="border border-stone-200 rounded-lg bg-white p-3 text-center">
                          <div className="text-2xl font-bold text-amber-600">{batch.duplicates}</div>
                          <div className="text-xs text-stone-400 mt-1">Duplicates</div>
                        </div>
                        <div className="border border-stone-200 rounded-lg bg-white p-3 text-center">
                          <div className="text-2xl font-bold text-red-600">{batch.needReview}</div>
                          <div className="text-xs text-stone-400 mt-1">Need Review</div>
                        </div>
                        <div className="border border-stone-200 rounded-lg bg-white p-3 text-center">
                          <div className="text-2xl font-bold text-stone-600">{batch.count}</div>
                          <div className="text-xs text-stone-400 mt-1">Total</div>
                        </div>
                      </div>
                    </td>
                    </tr>
                  )}
                </React.Fragment>
              ))}
            </tbody>
          </table>
          {batches.length === 0 && (
            <div className="p-8 text-center text-stone-400 text-sm">No import batches found.</div>
          )}
      </div>

      {/* Import Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-black/20 backdrop-blur-sm flex items-center justify-center z-50">
          <div className="bg-white rounded-2xl border border-stone-200 shadow-xl w-full max-w-md p-6 mx-4 animate-in">
            <div className="flex items-center justify-between mb-5">
              <h2 className="text-lg font-semibold text-stone-900">Start New Import</h2>
              <button
                onClick={() => setShowModal(false)}
                className="p-1.5 rounded-lg hover:bg-stone-100 transition-colors"
              >
                <X size={16} className="text-stone-400" />
              </button>
            </div>

            <div className="space-y-4">
              <div>
                <label className="block text-xs font-medium text-stone-500 mb-1.5">Source</label>
                <select
                  value={importSource}
                  onChange={(e) => setImportSource(e.target.value)}
                  className="w-full border border-stone-200 rounded-lg px-3 py-2 text-sm bg-stone-50 focus:outline-none focus:ring-2 focus:ring-stone-200 focus:border-stone-300 transition-all"
                >
                  <option value="wikidata">Wikidata</option>
                  <option value="wikipedia">Wikipedia</option>
                  <option value="manual">Manual</option>
                  <option value="encyclopedia">Encyclopedia</option>
                </select>
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs font-medium text-stone-500 mb-1.5">Year From</label>
                  <input
                    type="text"
                    value={yearFrom}
                    onChange={(e) => setYearFrom(e.target.value)}
                    className="w-full border border-stone-200 rounded-lg px-3 py-2 text-sm bg-stone-50 focus:outline-none focus:ring-2 focus:ring-stone-200 focus:border-stone-300 transition-all"
                    placeholder="-500"
                  />
                </div>
                <div>
                  <label className="block text-xs font-medium text-stone-500 mb-1.5">Year To</label>
                  <input
                    type="text"
                    value={yearTo}
                    onChange={(e) => setYearTo(e.target.value)}
                    className="w-full border border-stone-200 rounded-lg px-3 py-2 text-sm bg-stone-50 focus:outline-none focus:ring-2 focus:ring-stone-200 focus:border-stone-300 transition-all"
                    placeholder="2000"
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-medium text-stone-500 mb-1.5">Region</label>
                <select
                  value={importRegion}
                  onChange={(e) => setImportRegion(e.target.value)}
                  className="w-full border border-stone-200 rounded-lg px-3 py-2 text-sm bg-stone-50 focus:outline-none focus:ring-2 focus:ring-stone-200 focus:border-stone-300 transition-all"
                >
                  <option value="">All Regions</option>
                  {regions.map((r) => (
                    <option key={r.id} value={r.id}>{r.name}</option>
                  ))}
                </select>
              </div>
            </div>

            <div className="flex gap-3 mt-6">
              <button
                onClick={() => setShowModal(false)}
                className="flex-1 px-4 py-2 text-sm border border-stone-200 rounded-lg text-stone-600 hover:bg-stone-50 transition-colors"
              >
                Cancel
              </button>
              <button
                onClick={handleStartImport}
                disabled={isImporting}
                className="flex-1 px-4 py-2 text-sm bg-stone-900 text-white rounded-lg hover:bg-stone-800 transition-colors disabled:opacity-50 flex items-center justify-center gap-2 active:scale-[0.98]"
              >
                {isImporting ? (
                  <>
                    <svg className="animate-spin h-4 w-4" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                    </svg>
                    Importing...
                  </>
                ) : (
                  <>
                    <Upload size={14} />
                    Start Import
                  </>
                )}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
