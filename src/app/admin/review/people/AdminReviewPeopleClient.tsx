'use client';

import { useLocale } from '@/i18n/LocaleProvider';
import { personName, personSummary, personTags } from '@/lib/types';
import type { Person, DataStatus } from '@/lib/types';
import type { Region } from '@/lib/types';
import Link from 'next/link';
import { useState, useEffect, useRef } from 'react';
import { Search, CheckSquare, X, ChevronDown, ChevronUp, Edit3 } from 'lucide-react';

interface AdminReviewPeopleClientProps {
  totalCount: number;
  pendingCount: number;
  publishedCount: number;
}

const PAGE_SIZE = 50;
const statuses: DataStatus[] = ['imported', 'needs_review', 'verified', 'published', 'rejected'];

const statusColors: Record<string, string> = {
  imported: 'bg-blue-100 text-blue-700',
  needs_review: 'bg-amber-100 text-amber-700',
  verified: 'bg-green-100 text-green-700',
  published: 'bg-emerald-100 text-emerald-700',
  rejected: 'bg-red-100 text-red-700',
};

export default function AdminReviewPeopleClient({
  totalCount,
  pendingCount,
  publishedCount,
}: AdminReviewPeopleClientProps) {
  const { locale } = useLocale();

  const [people, setPeople] = useState<Person[]>([]);
  const [regions, setRegions] = useState<Region[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(0);

  const [searchQuery, setSearchQuery] = useState('');
  const [statusFilter, setStatusFilter] = useState<string>('all');
  const [regionFilter, setRegionFilter] = useState<string>('all');
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());
  const [expandedId, setExpandedId] = useState<string | null>(null);
  const [editingScore, setEditingScore] = useState<string | null>(null);
  const [editValue, setEditValue] = useState('');
  const debounceRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  // Fetch regions once
  useEffect(() => {
    fetch('/api/data/regions')
      .then((r) => r.json())
      .then((data) => setRegions(data.items || data))
      .catch(() => setError('Failed to load regions'));
  }, []);

  // Debounced search: when searchQuery changes, reset page and debounce fetch
  const [debouncedQuery, setDebouncedQuery] = useState('');
  useEffect(() => {
    if (debounceRef.current) clearTimeout(debounceRef.current);
    debounceRef.current = setTimeout(() => {
      setDebouncedQuery(searchQuery);
      setPage(1);
    }, 300);
    return () => {
      if (debounceRef.current) clearTimeout(debounceRef.current);
    };
  }, [searchQuery]);

  // Fetch people with filters (uses debounced query)
  useEffect(() => {
    setLoading(true);
    setError(null);
    const params = new URLSearchParams({
      page: String(page),
      limit: String(PAGE_SIZE),
      published: 'false',
    });
    if (debouncedQuery) params.set('q', debouncedQuery);
    if (statusFilter !== 'all') params.set('status', statusFilter);
    if (regionFilter !== 'all') params.set('region', regionFilter);

    fetch(`/api/data/people?${params}`)
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then((data) => {
        setPeople(data.items || []);
        setTotalPages(data.totalPages || 1);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, [page, debouncedQuery, statusFilter, regionFilter]);

  // Reset page when filters change
  useEffect(() => {
    setPage(1);
    setSelectedIds(new Set());
  }, [statusFilter, regionFilter]);

  const toggleSelect = (id: string) => {
    setSelectedIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  const handleScoreEdit = (id: string, currentScore: number) => {
    setEditingScore(id);
    setEditValue(String(currentScore));
  };

  const commitScoreEdit = (id: string) => {
    const val = parseFloat(editValue);
    if (!isNaN(val) && val >= 0 && val <= 1) {
      setPeople((prev) =>
        prev.map((p) => (p.id === id ? { ...p, confidenceScore: val } : p))
      );
    }
    setEditingScore(null);
  };

  return (
    <div className="max-w-5xl">
      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <Link href="/admin" className="text-sm text-stone-400 hover:text-stone-600 transition-colors">
            ← Dashboard
          </Link>
          <h1 className="text-xl font-bold text-stone-900">Review: People</h1>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-xs text-stone-400">{totalCount} total</span>
          {pendingCount > 0 && (
            <span className="text-[10px] px-2 py-0.5 rounded-full font-medium bg-amber-100 text-amber-700">
              pending: {pendingCount}
            </span>
          )}
          <span className="text-[10px] px-2 py-0.5 rounded-full font-medium bg-emerald-100 text-emerald-700">
            published: {publishedCount}
          </span>
        </div>
      </div>

      {/* Filters */}
      <div className="flex flex-wrap items-center gap-3 mb-4">
        <div className="relative flex-1 min-w-[200px] max-w-xs">
          <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2 text-stone-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search by name..."
            className="w-full pl-9 pr-3 py-2 text-sm border border-stone-200 rounded-lg bg-white focus:outline-none focus:ring-2 focus:ring-stone-200 focus:border-stone-300 transition-all placeholder:text-stone-300"
          />
        </div>

        <div className="flex items-center gap-1.5 bg-stone-100 rounded-lg p-1">
          {['all', ...statuses].map((s) => (
            <button
              key={s}
              onClick={() => setStatusFilter(s)}
              className={`text-xs px-2.5 py-1 rounded-md transition-colors ${
                statusFilter === s
                  ? 'bg-white text-stone-900 shadow-sm'
                  : 'text-stone-500 hover:text-stone-700'
              }`}
            >
              {s === 'all' ? 'All' : s.replace('_', ' ')}
            </button>
          ))}
        </div>

        <select
          value={regionFilter}
          onChange={(e) => setRegionFilter(e.target.value)}
          className="text-xs border border-stone-200 rounded-lg px-2.5 py-1.5 bg-white text-stone-600 focus:outline-none focus:ring-2 focus:ring-stone-200"
        >
          <option value="all">All Regions</option>
          {regions.map((r) => (
            <option key={r.id} value={r.id}>{r.name}</option>
          ))}
        </select>
      </div>

      {/* Error state */}
      {error && (
        <div className="mb-4 p-4 border border-red-200 bg-red-50 rounded-lg text-sm text-red-700">
          Error: {error}
        </div>
      )}

      {/* Selection bar */}
      {selectedIds.size > 0 && (
        <div className="flex items-center gap-2 mb-3 px-3 py-2 bg-stone-100 rounded-lg text-sm">
          <span className="text-stone-500 text-xs">{selectedIds.size} selected</span>
          <div className="flex-1" />
          <button
            onClick={() => setSelectedIds(new Set())}
            className="text-xs px-2 py-1 text-stone-400 hover:text-stone-600"
          >
            <X size={14} />
          </button>
        </div>
      )}

      {/* Loading */}
      {loading && (
        <div className="flex items-center justify-center py-16">
          <div className="animate-spin w-6 h-6 border-2 border-stone-300 border-t-stone-600 rounded-full" />
        </div>
      )}

      {/* People List */}
      {!loading && people.length === 0 ? (
        <div className="border border-stone-200 rounded-xl bg-white p-8 text-center text-stone-400 text-sm">
          No people match your filters.
        </div>
      ) : !loading ? (
        <div className="space-y-2">
          {people.map((p) => {
            const sel = selectedIds.has(p.id);
            return (
              <div
                key={p.id}
                className={`border rounded-xl bg-white transition-all duration-150 ${
                  sel ? 'border-stone-400 bg-stone-50' : 'border-stone-200 hover:border-stone-300'
                }`}
              >
                <div className="p-4">
                  <div className="flex items-start gap-3">
                    <button
                      onClick={() => toggleSelect(p.id)}
                      className={`mt-0.5 w-4 h-4 rounded border-2 flex items-center justify-center flex-shrink-0 transition-colors ${
                        sel ? 'bg-stone-900 border-stone-900 text-white' : 'border-stone-300 hover:border-stone-400'
                      }`}
                    >
                      {sel && <CheckSquare size={12} />}
                    </button>

                    <div className="flex-1 min-w-0">
                      <div className="flex items-start justify-between gap-4">
                        <div className="min-w-0">
                          <h3 className="font-semibold text-stone-900 truncate">{personName(p, locale)}</h3>
                          <p className="text-xs text-stone-400 mt-0.5">
                            {p.birthYear ?? '?'}–{p.deathYear ?? '?'} · {p.regionId ?? 'No region'}
                          </p>
                          <p className="text-sm text-stone-500 mt-1 line-clamp-2">{personSummary(p, locale)}</p>
                        </div>

                        <div className="flex flex-col items-end gap-1 flex-shrink-0">
                          <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${statusColors[p.dataStatus] ?? 'bg-stone-100 text-stone-600'}`}>
                            {p.dataStatus.replace('_', ' ')}
                          </span>
                          {editingScore === p.id ? (
                            <input
                              type="number"
                              min="0"
                              max="1"
                              step="0.01"
                              value={editValue}
                              onChange={(e) => setEditValue(e.target.value)}
                              onBlur={() => commitScoreEdit(p.id)}
                              onKeyDown={(e) => {
                                if (e.key === 'Enter') commitScoreEdit(p.id);
                                if (e.key === 'Escape') setEditingScore(null);
                              }}
                              className="w-16 text-xs text-right border border-stone-300 rounded px-1 py-0.5 focus:outline-none focus:ring-2 focus:ring-stone-200"
                              autoFocus
                            />
                          ) : (
                            <button
                              onClick={(e) => { e.stopPropagation(); handleScoreEdit(p.id, p.confidenceScore); }}
                              className="text-xs text-stone-400 hover:text-stone-600 flex items-center gap-1 transition-colors"
                            >
                              {p.confidenceScore.toFixed(2)}
                              <Edit3 size={10} />
                            </button>
                          )}
                        </div>
                      </div>

                      <div className="flex flex-wrap gap-1 mt-2">
                        {personTags(p, locale).map((tag) => (
                          <span key={tag} className="text-[10px] px-1.5 py-0.5 rounded bg-stone-100 text-stone-500">
                            {tag}
                          </span>
                        ))}
                      </div>
                    </div>

                    <button
                      onClick={() => setExpandedId(expandedId === p.id ? null : p.id)}
                      className="text-stone-400 hover:text-stone-600 p-1 flex-shrink-0 transition-colors"
                    >
                      {expandedId === p.id ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                    </button>
                  </div>
                </div>

                {expandedId === p.id && (
                  <div className="border-t border-stone-100 bg-stone-50/50 px-4 py-3 rounded-b-xl">
                    <div className="grid grid-cols-2 md:grid-cols-3 gap-3 text-sm">
                      <DetailField label="ID" value={p.id} mono />
                      <DetailField label="Birth Year" value={p.birthYear?.toString() ?? 'Unknown'} />
                      <DetailField label="Death Year" value={p.deathYear?.toString() ?? 'Unknown'} />
                      <DetailField label="Region" value={p.regionId ?? 'None'} />
                      <DetailField label="Confidence" value={p.confidenceScore.toFixed(3)} />
                      <DetailField label="Wikidata QID" value={p.wikidataQid ?? 'None'} mono />
                      <DetailField label="Sources" value={p.sourceIds.join(', ') || 'None'} mono span />
                      <DetailField label="Alternative Names" value={p.alternativeNames.join(', ') || 'None'} span />
                    </div>
                  </div>
                )}
              </div>
            );
          })}

          {/* Pagination */}
          {totalPages > 1 && (
            <div className="flex items-center justify-center gap-4 mt-6 pb-8">
              <button
                onClick={() => setPage((p) => Math.max(1, p - 1))}
                disabled={page <= 1}
                className="text-xs px-3 py-1.5 rounded border border-stone-200 bg-white text-stone-600 hover:border-stone-400 disabled:opacity-30 disabled:cursor-not-allowed transition-colors"
              >
                ← Previous
              </button>
              <span className="text-xs text-stone-500">
                {page} / {totalPages}
              </span>
              <button
                onClick={() => setPage((p) => Math.min(totalPages, p + 1))}
                disabled={page >= totalPages}
                className="text-xs px-3 py-1.5 rounded border border-stone-200 bg-white text-stone-600 hover:border-stone-400 disabled:opacity-30 disabled:cursor-not-allowed transition-colors"
              >
                Next →
              </button>
            </div>
          )}
        </div>
      ) : null}
    </div>
  );
}

function DetailField({ label, value, mono, span }: { label: string; value: string; mono?: boolean; span?: boolean }) {
  return (
    <div className={span ? 'col-span-full' : ''}>
      <div className="text-[10px] text-stone-400 uppercase tracking-wider">{label}</div>
      <div className={`text-xs mt-0.5 ${mono ? 'font-mono text-stone-600' : 'text-stone-700'}`}>{value}</div>
    </div>
  );
}
