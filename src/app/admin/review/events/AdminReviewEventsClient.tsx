'use client';

import { useLocale } from '@/i18n/LocaleProvider';
import { eventTitle, eventSummary, eventTags, eventPlaceName } from '@/lib/types';
import type { HistoricalEvent, DataStatus } from '@/lib/types';
import type { Region } from '@/lib/types';
import Link from 'next/link';
import { useState, useMemo } from 'react';
import { Search, CheckSquare, X, ChevronDown, ChevronUp, Edit3 } from 'lucide-react';

interface AdminReviewEventsClientProps {
  events: HistoricalEvent[];
  regions: Region[];
}

export default function AdminReviewEventsClient({ events: allEvents, regions }: AdminReviewEventsClientProps) {
  const { locale } = useLocale();

  const [eventsData, setEventsData] = useState<HistoricalEvent[]>(() =>
    allEvents.map((e) => ({ ...e }))
  );

  const [searchQuery, setSearchQuery] = useState('');
  const [statusFilter, setStatusFilter] = useState<string>('all');
  const [regionFilter, setRegionFilter] = useState<string>('all');
  const [importanceFilter, setImportanceFilter] = useState<string>('all');
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());
  const [expandedId, setExpandedId] = useState<string | null>(null);
  const [editingScore, setEditingScore] = useState<string | null>(null);
  const [editValue, setEditValue] = useState('');
  const [toast, setToast] = useState<{ message: string; type: 'success' | 'error' } | null>(null);

  const filteredEvents = useMemo(() => {
    return eventsData.filter((evt) => {
      if (statusFilter !== 'all' && evt.dataStatus !== statusFilter) return false;
      if (regionFilter !== 'all' && evt.regionId !== regionFilter) return false;
      if (importanceFilter !== 'all' && String(evt.importance) !== importanceFilter) return false;
      if (searchQuery) {
        const q = searchQuery.toLowerCase();
        const titleMatch = evt.title.toLowerCase().includes(q) ||
          evt.titleEn?.toLowerCase().includes(q);
        if (!titleMatch) return false;
      }
      return true;
    });
  }, [eventsData, statusFilter, regionFilter, importanceFilter, searchQuery]);

  const statusCounts = useMemo(() => {
    const counts: Record<string, number> = { all: eventsData.length };
    for (const evt of eventsData) {
      counts[evt.dataStatus] = (counts[evt.dataStatus] || 0) + 1;
    }
    return counts;
  }, [eventsData]);

  const showToast = (message: string, type: 'success' | 'error' = 'success') => {
    setToast({ message, type });
    setTimeout(() => setToast(null), 2500);
  };

  const updateStatus = (id: string, status: DataStatus) => {
    setEventsData((prev) =>
      prev.map((evt) => (evt.id === id ? { ...evt, dataStatus: status } : evt))
    );
    showToast(`Status updated to "${status}"`);
  };

  const updateScore = (id: string, score: number) => {
    setEventsData((prev) =>
      prev.map((evt) => (evt.id === id ? { ...evt, confidenceScore: score } : evt))
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

  const bulkUpdateStatus = (status: DataStatus) => {
    setEventsData((prev) =>
      prev.map((evt) => (selectedIds.has(evt.id) ? { ...evt, dataStatus: status } : evt))
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

  const importanceColors: Record<number, string> = {
    1: 'bg-stone-100 text-stone-600',
    2: 'bg-stone-100 text-stone-600',
    3: 'bg-amber-100 text-amber-700',
    4: 'bg-orange-100 text-orange-700',
    5: 'bg-red-100 text-red-700',
  };

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
          <h1 className="text-xl font-bold text-stone-900">Review: Events</h1>
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
            {filteredEvents.length} of {eventsData.length}
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
            placeholder="Search by title..."
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

        {/* Importance Filter */}
        <select
          value={importanceFilter}
          onChange={(e) => { setImportanceFilter(e.target.value); setSelectedIds(new Set()); }}
          className="text-xs border border-stone-200 rounded-lg px-2.5 py-1.5 bg-white text-stone-600 focus:outline-none focus:ring-2 focus:ring-stone-200"
        >
          <option value="all">All Importance</option>
          {[5, 4, 3, 2, 1].map((i) => (
            <option key={i} value={String(i)}>Importance {i}</option>
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

      {/* Events List */}
      {filteredEvents.length === 0 ? (
        <div className="border border-stone-200 rounded-xl bg-white p-8 text-center text-stone-400 text-sm">
          No events match your filters.
        </div>
      ) : (
        <div className="space-y-2">
          {filteredEvents.map((evt) => (
            <div
              key={evt.id}
              className={`border rounded-xl bg-white transition-all duration-150 ${
                selectedIds.has(evt.id) ? 'border-stone-400 bg-stone-50' : 'border-stone-200 hover:border-stone-300'
              }`}
            >
              <div className="p-4">
                <div className="flex items-start gap-3">
                  {/* Checkbox */}
                  <button
                    onClick={() => toggleSelect(evt.id)}
                    className={`mt-0.5 w-4 h-4 rounded border-2 flex items-center justify-center flex-shrink-0 transition-colors ${
                      selectedIds.has(evt.id)
                        ? 'bg-stone-900 border-stone-900 text-white'
                        : 'border-stone-300 hover:border-stone-400'
                    }`}
                  >
                    {selectedIds.has(evt.id) && <CheckSquare size={12} />}
                  </button>

                  {/* Content */}
                  <div className="flex-1 min-w-0">
                    <div className="flex items-start justify-between gap-4">
                      <div className="min-w-0">
                        <h3 className="font-semibold text-stone-900 truncate">{eventTitle(evt, locale)}</h3>
                        <p className="text-xs text-stone-400 mt-0.5">
                          {evt.startYear ?? '?'}{evt.endYear && evt.endYear !== evt.startYear ? `–${evt.endYear}` : ''}
                          {' · '}{evt.regionId ?? eventPlaceName(evt, locale) ?? 'No location'}
                          {evt.datePrecision !== 'year' && <> · precision: {evt.datePrecision}</>}
                        </p>
                        <p className="text-sm text-stone-500 mt-1 line-clamp-2">{eventSummary(evt, locale)}</p>
                      </div>

                      <div className="flex flex-col items-end gap-1 flex-shrink-0">
                        <div className="flex items-center gap-1.5">
                          <span className={`text-[10px] px-1.5 py-0.5 rounded ${importanceColors[evt.importance]}`}>
                            {'★'.repeat(evt.importance)}
                          </span>
                          <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${statusColors[evt.dataStatus] ?? 'bg-stone-100 text-stone-600'}`}>
                            {evt.dataStatus.replace('_', ' ')}
                          </span>
                        </div>
                        {editingScore === evt.id ? (
                          <input
                            type="number"
                            min="0"
                            max="1"
                            step="0.01"
                            value={editValue}
                            onChange={(e) => setEditValue(e.target.value)}
                            onBlur={() => commitScoreEdit(evt.id)}
                            onKeyDown={(e) => {
                              if (e.key === 'Enter') commitScoreEdit(evt.id);
                              if (e.key === 'Escape') setEditingScore(null);
                            }}
                            className="w-16 text-xs text-right border border-stone-300 rounded px-1 py-0.5 focus:outline-none focus:ring-2 focus:ring-stone-200"
                            autoFocus
                          />
                        ) : (
                          <button
                            onClick={(e) => { e.stopPropagation(); handleScoreEdit(evt.id, evt.confidenceScore); }}
                            className="text-xs text-stone-400 hover:text-stone-600 flex items-center gap-1 transition-colors"
                          >
                            {evt.confidenceScore.toFixed(2)}
                            <Edit3 size={10} />
                          </button>
                        )}
                      </div>
                    </div>

                    {/* Tags */}
                    <div className="flex flex-wrap gap-1 mt-2">
                      {eventTags(evt, locale).map((tag) => (
                        <span key={tag} className="text-[10px] px-1.5 py-0.5 rounded bg-stone-100 text-stone-500">
                          {tag}
                        </span>
                      ))}
                    </div>
                  </div>

                  {/* Expand button */}
                  <button
                    onClick={() => setExpandedId(expandedId === evt.id ? null : evt.id)}
                    className="text-stone-400 hover:text-stone-600 p-1 flex-shrink-0 transition-colors"
                  >
                    {expandedId === evt.id ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                  </button>
                </div>

                {/* Action Buttons */}
                <div className="flex gap-2 mt-3 pt-3 border-t border-stone-100">
                  <button
                    onClick={() => updateStatus(evt.id, 'published')}
                    className="text-xs px-3 py-1 rounded border border-emerald-200 text-emerald-700 hover:bg-emerald-50 transition-colors active:scale-[0.97]"
                  >
                    Publish
                  </button>
                  <button
                    onClick={() => updateStatus(evt.id, 'needs_review')}
                    className="text-xs px-3 py-1 rounded border border-amber-200 text-amber-700 hover:bg-amber-50 transition-colors active:scale-[0.97]"
                  >
                    Needs Review
                  </button>
                  <button
                    onClick={() => updateStatus(evt.id, 'rejected')}
                    className="text-xs px-3 py-1 rounded border border-red-200 text-red-700 hover:bg-red-50 transition-colors active:scale-[0.97]"
                  >
                    Reject
                  </button>
                </div>
              </div>

              {/* Expanded Detail View */}
              {expandedId === evt.id && (
                <div className="border-t border-stone-100 bg-stone-50/50 px-4 py-3 rounded-b-xl">
                  <div className="grid grid-cols-2 md:grid-cols-3 gap-3 text-sm">
                    <DetailField label="ID" value={evt.id} mono />
                    <DetailField label="Start Year" value={evt.startYear?.toString() ?? 'Unknown'} />
                    <DetailField label="End Year" value={evt.endYear?.toString() ?? 'Unknown'} />
                    <DetailField label="Region" value={evt.regionId ?? 'None'} />
                    <DetailField label="Place" value={eventPlaceName(evt, locale) ?? 'Unknown'} />
                    <DetailField label="Date Precision" value={evt.datePrecision} />
                    <DetailField label="Importance" value={'★'.repeat(evt.importance)} />
                    <DetailField label="Confidence" value={evt.confidenceScore.toFixed(3)} />
                    <DetailField label="Wikidata QID" value={evt.wikidataQid ?? 'None'} mono />
                    <DetailField label="Approximate" value={evt.isApproximate ? 'Yes' : 'No'} />
                    <DetailField label="Related People" value={evt.personIds.length > 0 ? evt.personIds.join(', ') : 'None'} mono span />
                    <DetailField label="Sources" value={evt.sourceIds.length > 0 ? evt.sourceIds.join(', ') : 'None'} mono span />
                    {evt.description && (
                      <div className="col-span-full">
                        <div className="text-[10px] text-stone-400 uppercase tracking-wider mb-0.5">Description</div>
                        <div className="text-xs text-stone-700 leading-relaxed">{evt.description}</div>
                      </div>
                    )}
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
