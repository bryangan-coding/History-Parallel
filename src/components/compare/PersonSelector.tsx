'use client';

import { useState, useRef, useEffect, useMemo } from 'react';
import type { Person } from '@/lib/types';
import { useLocale } from '@/i18n/LocaleProvider';
import { personName, personSummary } from '@/lib/types';

interface PersonSelectorProps {
  selected: Person[];
  onAdd: (person: Person) => void;
  onRemove: (personId: string) => void;
}

export default function PersonSelector({
  selected,
  onAdd,
  onRemove,
}: PersonSelectorProps) {
  const { locale, t } = useLocale();
  const [query, setQuery] = useState('');
  const [isOpen, setIsOpen] = useState(false);
  const [results, setResults] = useState<Person[]>([]);
  const [loading, setLoading] = useState(false);
  const [fetchError, setFetchError] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const debounceRef = useRef<ReturnType<typeof setTimeout>>(null);

  const selectedIds = useMemo(() => new Set(selected.map((p) => p.id)), [selected]);

  // Fetch from API when query changes (debounced)
  useEffect(() => {
    if (debounceRef.current) clearTimeout(debounceRef.current);

    if (query.trim().length === 0) {
      setResults([]);
      return;
    }

    debounceRef.current = setTimeout(() => {
      setLoading(true);
      setFetchError(false);
      fetch(`/api/data/people?q=${encodeURIComponent(query.trim())}&limit=8&published=true`)
        .then((r) => r.json())
        .then((data) => {
          setResults((data.items || []).filter((p: Person) => !selectedIds.has(p.id)));
          setLoading(false);
        })
        .catch(() => {
          setResults([]);
          setFetchError(true);
          setLoading(false);
        });
    }, 200);

    return () => {
      if (debounceRef.current) clearTimeout(debounceRef.current);
    };
  }, [query, selectedIds]);

  useEffect(() => {
    function handleClickOutside(e: MouseEvent) {
      if (containerRef.current && !containerRef.current.contains(e.target as Node)) {
        setIsOpen(false);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  return (
    <div ref={containerRef} className="space-y-3">
      {/* Selected people chips */}
      {selected.length > 0 && (
        <div className="flex flex-wrap gap-2">
          {selected.map((person, i) => {
            const colors = ['#d97706', '#2563eb', '#059669', '#dc2626', '#7c3aed', '#0d9488', '#ea580c', '#ca8a04'];
            const color = colors[i % colors.length];
            return (
              <span
                key={person.id}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-sm font-medium border transition-colors"
                style={{ borderColor: color, color, backgroundColor: `${color}10` }}
              >
                {personName(person, locale)}
                <button
                  onClick={() => onRemove(person.id)}
                  className="ml-0.5 rounded-full p-0.5 hover:bg-black/5 transition-colors"
                  title={t.compare.removePerson}
                >
                  <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
                    <path d="M3 3L9 9M9 3L3 9" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
                  </svg>
                </button>
              </span>
            );
          })}
        </div>
      )}

      {/* Search input */}
      <div className="relative">
        <input
          ref={inputRef}
          type="text"
          value={query}
          onChange={(e) => {
            setQuery(e.target.value);
            setIsOpen(true);
          }}
          onFocus={() => setIsOpen(true)}
          placeholder={t.compare.selectPlaceholder}
          className="w-full px-4 py-2.5 text-sm border border-stone-200 rounded-lg bg-white placeholder:text-stone-400 focus:outline-none focus:ring-2 focus:ring-stone-300 focus:border-stone-300 transition-shadow"
        />

        {/* Dropdown */}
        {isOpen && query.trim().length > 0 && (
          <div className="absolute top-full mt-1 left-0 right-0 bg-white border border-stone-200 rounded-lg shadow-lg z-50 max-h-72 overflow-y-auto">
            {loading ? (
              <div className="flex items-center justify-center py-6">
                <div className="animate-spin w-5 h-5 border-2 border-stone-300 border-t-stone-600 rounded-full" />
              </div>
            ) : results.length === 0 ? (
              <p className="px-4 py-3 text-sm text-stone-400 text-center">
                {fetchError ? (locale === 'en' ? 'Search failed. Try again.' : '搜索失败，请重试。') : (locale === 'en' ? 'No matching people' : '无匹配人物')}
              </p>
            ) : (
              results.map((person) => (
                <button
                  key={person.id}
                  onClick={() => {
                    onAdd(person);
                    setQuery('');
                    setIsOpen(false);
                    inputRef.current?.focus();
                  }}
                  className="w-full text-left px-4 py-3 hover:bg-stone-50 transition-colors border-b border-stone-100 last:border-b-0"
                >
                  <div className="flex items-center justify-between">
                    <span className="text-sm font-medium text-stone-900">
                      {personName(person, locale)}
                    </span>
                    {person.birthYear && person.deathYear && (
                      <span className="text-xs text-stone-400">
                        {person.birthYear}–{person.deathYear}
                      </span>
                    )}
                  </div>
                  <p className="text-xs text-stone-500 mt-0.5 line-clamp-1">
                    {person.alternativeNames.slice(0, 3).join(' / ')}
                  </p>
                  <p className="text-xs text-stone-400 mt-0.5 line-clamp-1">
                    {personSummary(person, locale)}
                  </p>
                </button>
              ))
            )}
          </div>
        )}
      </div>
    </div>
  );
}
