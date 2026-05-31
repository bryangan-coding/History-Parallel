'use client';

import { useLocale } from '@/i18n/LocaleProvider';
import { people as allPeople } from '@/data/mockData';
import { regions } from '@/data/mockData';
import { personName, personSummary, personTags } from '@/lib/types';
import type { Person, DataStatus } from '@/lib/types';
import Link from 'next/link';
import { useState, useMemo, useEffect } from 'react';
import { Search, Filter, CheckSquare, X, ChevronDown, ChevronUp, Edit3 } from 'lucide-react';

export default function AdminReviewPeoplePage() {
  const { locale } = useLocale();

  // Local state for mutable status/score
  const [peopleData, setPeopleData] = useState<Person[]>(() =>
    allPeople.map((p) => ({ ...p }))
  );

  const [searchQuery, setSearchQuery] = useState('');
  const [statusFilter, setStatusFilter] = useState<string>('all');
  const [regionFilter, setRegionFilter] = useState<string>('all');
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());
  const [expandedId, setExpandedId] = useState<string | null>(null);
  const [editingScore, setEditingScore] = useState<string | null>(null);
  const [editValue, setEditValue] = useState('');
  const [toast, setToast] = useState<{ message: string; type: 'success' | 'error' } | null>(null);

  // Filtered people
  const filteredPeople = useMemo(() => {
    return peopleData.filter((p) => {
      if (statusFilter !== 'all' && p.dataStatus !== statusFilter) return false;
      if (regionFilter !== 'all' && p.regionId !== regionFilter) return false;
      if (searchQuery) {
        const q = searchQuery.toLowerCase();
        const nameMatch = p.name.toLowerCase().includes(q) ||
          p.nameEn?.toLowerCase().includes(q) ||
          p.alternativeNames.some((n) => n.toLowerCase().includes(q));
        if (!nameMatch) return false;
      }
      return true;
    });
  }, [peopleData, statusFilter, regionFilter, searchQuery]);

  // Status counts
  const statusCounts = useMemo(() => {
    const counts: Record<string, number> = { all: peopleData.length };
    for (const p of peopleData) {
      counts[p.dataStatus] = (counts[p.dataStatus] || 0) + 1;
    }
    return counts;
  }, [peopleData]);

  const showToast = (message: string, type: 'success' | 'error' = 'success') => {
    setToast({ message, type });
    setTimeout(() => setToast(null), 2500);
  };

  const updateStatus = (id: string, status: DataStatus) => {
    setPeopleData((prev) =>
      prev.map((p) => (p.id === id ? { ...p, dataStatus: status } : p))
    );
    showToast(`Status updated to "${status}"`);
  };

  const updateScore = (id: string, score: number) => {
    setPeopleData((prev) =>
      prev.map((p) => (p.id === id ? { ...p, confidenceScore: score } : p))
    );
  };

  const toggleSelect = (id: string) => {
    setSelectedIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  const toggleSelectAll = () => {
    if (selectedIds.size === filteredPeople.length) {
      setSelectedIds(new Set());
    } else {
      setSelectedIds(new Set(filteredPeople.map((p) => p.id)));
    }
  };

  const bulkUpdateStatus = (status: DataStatus) => {
    setPeopleData((prev) =>
      prev.map((p) => (selectedIds.has(p.id) ? { ...p, dataStatus: status } : p))
    );
    const count = selectedIds.size;
    setSelectedIds(new Set());
    showToast(`Updated ${count} items to "${status}"`);
  };

  const handleScoreEdit = (id: string, currentScore: number) => {
    setEditingScore(id);
    setEditValue(String(currentScore));
  };

  const commitScoreEdit = (id: string) => {
    const val = parseFloat(editValue);
    if (!isNaN(val) && val >= 0 && val <= 1) {
      updateScore(id, val);
      showToast(`Confidence score updated to ${val.toFixed(2)}`);
    }
    setEditingScore(null);
  };

  const statusColors: Record<string, string> = {
    imported: 'bg-blue-100 text-blue-700',
    needs_review: 'bg-amber-100 text-amber-700',
    verified: 'bg-green-100 text-green-700',
    published: 'bg-emerald-100 text-emerald-700',
    rejected: 'bg-red-100 text-red-700',
  };

  const statuses: DataStatus[] = ['imported', 'needs_review', 'verified', 'published', 'rejected'];

  return (
    <div className="max-w-5xl">
      {/* Toast */}
      {toast && (
        <div className={`fixed top-4 right-4 z-50 px-4 py-2.5 rounded-lg shadow-lg text-sm font-medium transition-all animate-in ${
          toast.type === 'success' ? 'bg-stone-900 text-white' : 'bg-red-600 text-white'
        }`}>
          {toast.message}
        </div>
      )}

      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <Link href="/admin" className="text-sm text-stone-400 hover:text-stone-600 transition-colors">
            ← Dashboard
          </Link>
          <h1 className="text-xl font-bold text-stone-900">Review: People</h1>
        </div>
        <div className="flex items-center gap-2">
          {statuses.map((s) => {
            const count = statusCounts[s] || 0;
            if (count === 0) return null;
            return (
              <span key={s} className={`text-[10px] px-2 py-0.5 rounded-full font-medium ${statusColors[s]}`}>
                {s}: {count}
              </span>
            );
          })}
          <span className="text-xs text-stone-400 ml-1">
            {filteredPeople.length} of {peopleData.length}
          </span>
        </div>
      </div>

      {/* Filters */}
      <div className="flex flex-wrap items-center gap-3 mb-4">
        {/* Search */}
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

        {/* Status Filter */}
        <div className="flex items-center gap-1.5 bg-stone-100 rounded-lg p-1">
          {['all', ...statuses].map((s) => {
            const count = s === 'all' ? statusCounts.all : (statusCounts[s] || 0);
            return (
              <button
                key={s}
                onClick={() => { setStatusFilter(s); setSelectedIds(new Set()); }}
                className={`text-xs px-2.5 py-1 rounded-md transition-colors ${
                  statusFilter === s
                    ? 'bg-white text-stone-900 shadow-sm'
                    : 'text-stone-500 hover:text-stone-700'
                }`}
              >
                {s === 'all' ? 'All' : s.replace('_', ' ')}
                <span className="ml-1 text-stone-400">{count}</span>
              </button>
            );
          })}
        </div>

        {/* Region Filter */}
        <select
          value={regionFilter}
          onChange={(e) => { setRegionFilter(e.target.value); setSelectedIds(new Set()); }}
          className="text-xs border border-stone-200 rounded-lg px-2.5 py-1.5 bg-white text-stone-600 focus:outline-none focus:ring-2 focus:ring-stone-200"
        >
          <option value="all">All Regions</option>
          {regions.map((r) => (
            <option key={r.id} value={r.id}>{r.name}</option>
          ))}
        </select>
      </div>

      {/* Bulk Actions */}
      {selectedIds.size > 0 && (
        <div className="flex items-center gap-2 mb-3 px-3 py-2 bg-stone-100 rounded-lg text-sm">
          <span className="text-stone-500 text-xs">{selectedIds.size} selected</span>
          <div className="flex-1" />
          <button
            onClick={() => bulkUpdateStatus('published')}
            className="text-xs px-3 py-1 rounded bg-emerald-600 text-white hover:bg-emerald-700 transition-colors"
          >
            Publish All
          </button>
          <button
            onClick={() => bulkUpdateStatus('needs_review')}
            className="text-xs px-3 py-1 rounded bg-amber-600 text-white hover:bg-amber-700 transition-colors"
          >
            Needs Review
          </button>
          <button
            onClick={() => bulkUpdateStatus('rejected')}
            className="text-xs px-3 py-1 rounded bg-red-600 text-white hover:bg-red-700 transition-colors"
          >
            Reject All
          </button>
          <button
            onClick={() => setSelectedIds(new Set())}
            className="text-xs px-2 py-1 text-stone-400 hover:text-stone-600"
          >
            <X size={14} />
          </button>
        </div>
      )}

      {/* People List */}
      {filteredPeople.length === 0 ? (
        <div className="border border-stone-200 rounded-xl bg-white p-8 text-center text-stone-400 text-sm">
          No people match your filters.
        </div>
      ) : (
        <div className="space-y-2">
          {filteredPeople.map((p) => (
            <div
              key={p.id}
              className={`border rounded-xl bg-white transition-all duration-150 ${
                selectedIds.has(p.id) ? 'border-stone-400 bg-stone-50' : 'border-stone-200 hover:border-stone-300'
              }`}
            >
              <div className="p-4">
                <div className="flex items-start gap-3">
                  {/* Checkbox */}
                  <button
                    onClick={() => toggleSelect(p.id)}
                    className={`mt-0.5 w-4 h-4 rounded border-2 flex items-center justify-center flex-shrink-0 transition-colors ${
                      selectedIds.has(p.id)
                        ? 'bg-stone-900 border-stone-900 text-white'
                        : 'border-stone-300 hover:border-stone-400'
                    }`}
                  >
                    {selectedIds.has(p.id) && <CheckSquare size={12} />}
                  </button>

                  {/* Content */}
                  <div className="flex-1 min-w-0">
                    <div className="flex items-start justify-between gap-4">
                      <div className="min-w-0">
                        <h3 className="font-semibold text-stone-900 truncate">{personName(p, locale)}</h3>
                        <p className="text-xs text-stone-400 mt-0.5">
                          {p.birthYear ?? '?'}–{p.deathYear ?? '?'} · {p.regionId ?? 'No region'}
                          {p.occupations.length > 0 && <> · {p.occupations.join(', ')}</>}
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

                    {/* Tags */}
                    <div className="flex flex-wrap gap-1 mt-2">
                      {personTags(p, locale).map((tag) => (
                        <span key={tag} className="text-[10px] px-1.5 py-0.5 rounded bg-stone-100 text-stone-500">
                          {tag}
                        </span>
                      ))}
                    </div>
                  </div>

                  {/* Expand button */}
                  <button
                    onClick={() => setExpandedId(expandedId === p.id ? null : p.id)}
                    className="text-stone-400 hover:text-stone-600 p-1 flex-shrink-0 transition-colors"
                  >
                    {expandedId === p.id ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                  </button>
                </div>

                {/* Action Buttons */}
                <div className="flex gap-2 mt-3 pt-3 border-t border-stone-100">
                  <button
                    onClick={() => updateStatus(p.id, 'published')}
                    className="text-xs px-3 py-1 rounded border border-emerald-200 text-emerald-700 hover:bg-emerald-50 transition-colors active:scale-[0.97]"
                  >
                    Publish
                  </button>
                  <button
                    onClick={() => updateStatus(p.id, 'needs_review')}
                    className="text-xs px-3 py-1 rounded border border-amber-200 text-amber-700 hover:bg-amber-50 transition-colors active:scale-[0.97]"
                  >
                    Needs Review
                  </button>
                  <button
                    onClick={() => updateStatus(p.id, 'rejected')}
                    className="text-xs px-3 py-1 rounded border border-red-200 text-red-700 hover:bg-red-50 transition-colors active:scale-[0.97]"
                  >
                    Reject
                  </button>
                </div>
              </div>

              {/* Expanded Detail View */}
              {expandedId === p.id && (
                <div className="border-t border-stone-100 bg-stone-50/50 px-4 py-3 rounded-b-xl">
                  <div className="grid grid-cols-2 md:grid-cols-3 gap-3 text-sm">
                    <DetailField label="ID" value={p.id} mono />
                    <DetailField label="Birth Year" value={p.birthYear?.toString() ?? 'Unknown'} />
                    <DetailField label="Death Year" value={p.deathYear?.toString() ?? 'Unknown'} />
                    <DetailField label="Region" value={p.regionId ?? 'None'} />
                    <DetailField label="Birth Precision" value={p.birthDatePrecision ?? 'N/A'} />
                    <DetailField label="Death Precision" value={p.deathDatePrecision ?? 'N/A'} />
                    <DetailField label="Confidence" value={p.confidenceScore.toFixed(3)} />
                    <DetailField label="Wikidata QID" value={p.wikidataQid ?? 'None'} mono />
                    <DetailField label="Sources" value={p.sourceIds.length > 0 ? p.sourceIds.join(', ') : 'None'} mono span />
                    <DetailField label="Alternative Names" value={p.alternativeNames.length > 0 ? p.alternativeNames.join(', ') : 'None'} span />
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
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
