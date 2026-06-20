'use client';

import { useState, useMemo, useCallback, useEffect } from 'react';
import { useSearchParams } from 'next/navigation';
import type { Person, HistoricalEvent } from '@/lib/types';
import { useLocale } from '@/i18n/LocaleProvider';
import { personName } from '@/lib/types';
import PageHeader from '@/components/common/PageHeader';
import PersonSelector from '@/components/compare/PersonSelector';
import VerticalCompareTimeline from '@/components/compare/VerticalCompareTimeline';
import { X, ArrowLeftRight } from 'lucide-react';

export default function ComparePageClient() {
  const { locale, t } = useLocale();
  const searchParams = useSearchParams();

  const [initialPeople, setInitialPeople] = useState<Person[]>([]);
  const [selectedPeople, setSelectedPeople] = useState<Person[]>([]);
  const [personEvents, setPersonEvents] = useState<Map<string, HistoricalEvent[]>>(new Map());

  // The first person is the "reference" (left side), others are "comparisons" (right side)
  const referencePerson = selectedPeople[0] ?? null;
  const comparisonPeople = selectedPeople.slice(1);

  // Handle URL preselect by fetching the person
  const preselectId = searchParams.get('preselect');
  useEffect(() => {
    if (!preselectId) return;
    fetch(`/api/data/people?ids=${preselectId}&limit=1`)
      .then((r) => r.json())
      .then((data) => {
        if (data.items?.length > 0) {
          setInitialPeople(data.items);
        }
      })
      .catch(() => {});
  }, [preselectId]);

  // Sync initial people into selected list when they load
  useEffect(() => {
    if (initialPeople.length > 0 && selectedPeople.length === 0) {
      setSelectedPeople(initialPeople);
    }
  }, [initialPeople, selectedPeople.length]);

  const handleAdd = useCallback((person: Person) => {
    setSelectedPeople((prev) => {
      if (prev.find((p) => p.id === person.id)) return prev;
      if (prev.length >= 6) return prev;
      return [...prev, person];
    });
  }, []);

  const handleRemove = useCallback((personId: string) => {
    setSelectedPeople((prev) => prev.filter((p) => p.id !== personId));
  }, []);

  // Switch reference person: move a comparison person to be the reference
  const handleSetReference = useCallback((personId: string) => {
    setSelectedPeople((prev) => {
      const idx = prev.findIndex((p) => p.id === personId);
      if (idx <= 0) return prev; // already reference or not found
      const person = prev[idx];
      const rest = [...prev.slice(0, idx), ...prev.slice(idx + 1)];
      return [person, ...rest];
    });
  }, []);

  // Fetch events for selected people on demand
  const [eventsMap, setEventsMap] = useState<Map<string, HistoricalEvent[]>>(new Map());
  useEffect(() => {
    let cancelled = false;
    async function fetchEventsForSelected() {
      const map = new Map<string, HistoricalEvent[]>();
      for (const p of selectedPeople) {
        if (personEvents.has(p.id)) {
          map.set(p.id, personEvents.get(p.id)!);
        } else {
          try {
            const { fetchEventsForPerson } = await import('@/data/server-actions');
            const events = await fetchEventsForPerson(p.id);
            if (!cancelled) map.set(p.id, events);
          } catch {
            if (!cancelled) map.set(p.id, []);
          }
        }
      }
      if (!cancelled) {
        setPersonEvents(prev => { const m = new Map(prev); map.forEach((v, k) => m.set(k, v)); return m; });
        setEventsMap(map);
      }
    }
    fetchEventsForSelected();
    return () => { cancelled = true; };
  }, [selectedPeople]);

  return (
    <div>
      <PageHeader
        backTo="/"
        backLabel={t.nav.backToHome}
        title={t.compare.title}
        subtitle={t.compare.subtitle}
      />

      <div className="mt-6">
        <label className="block text-sm font-medium text-stone-700 mb-2">
          {t.compare.selectPeople}
          {selectedPeople.length > 0 && (
            <span className="text-stone-400 font-normal ml-1">
              ({selectedPeople.length}/6)
            </span>
          )}
        </label>
        <PersonSelector
          selected={selectedPeople}
          onAdd={handleAdd}
          onRemove={handleRemove}
        />
        {selectedPeople.length >= 6 && (
          <p className="text-xs text-amber-600 mt-1.5">
            {locale === 'en'
              ? 'Maximum 6 people (1 reference + 5 comparisons)'
              : '已选满 6 人（1 位参照 + 5 位对比），请先移除再添加'}
          </p>
        )}
      </div>

      {/* ===== Reference & Comparison bar ===== */}
      {selectedPeople.length > 0 && (
        <div className="mt-4 flex items-center gap-3 flex-wrap">
          {/* Reference person */}
          {referencePerson && (
            <div className="flex items-center gap-2 px-3 py-1.5 rounded-lg border-2 border-orange-400 bg-orange-50">
              <span className="text-[10px] font-medium text-orange-600 uppercase tracking-wide">
                {locale === 'en' ? 'Reference' : '参照'}
              </span>
              <div className="w-2.5 h-2.5 rounded-full bg-orange-600" />
              <span className="text-sm font-semibold text-stone-800">
                {personName(referencePerson, locale)}
              </span>
              <button
                onClick={() => handleRemove(referencePerson.id)}
                className="p-0.5 rounded hover:bg-orange-200 text-orange-500 transition-colors"
                title={locale === 'en' ? 'Remove' : '移除'}
              >
                <X size={14} />
              </button>
            </div>
          )}

          {/* Separator */}
          {referencePerson && comparisonPeople.length > 0 && (
            <span className="text-stone-300 text-lg">vs</span>
          )}

          {/* Comparison people */}
          {comparisonPeople.map((person, idx) => {
            const colors = ['#2563eb', '#059669', '#dc2626', '#7c3aed', '#0d9488'];
            const color = colors[idx % colors.length];
            return (
              <div
                key={person.id}
                className="flex items-center gap-2 px-3 py-1.5 rounded-lg border border-stone-200 bg-white hover:border-stone-300 transition-colors group"
              >
                <div className="w-2.5 h-2.5 rounded-full flex-shrink-0" style={{ backgroundColor: color }} />
                <span className="text-sm font-medium text-stone-700">
                  {personName(person, locale)}
                </span>
                {/* Set as reference button */}
                <button
                  onClick={() => handleSetReference(person.id)}
                  className="p-0.5 rounded hover:bg-stone-100 text-stone-400 hover:text-stone-600 opacity-0 group-hover:opacity-100 transition-all"
                  title={locale === 'en' ? 'Set as reference' : '设为参照'}
                >
                  <ArrowLeftRight size={12} />
                </button>
                <button
                  onClick={() => handleRemove(person.id)}
                  className="p-0.5 rounded hover:bg-stone-100 text-stone-400 hover:text-red-500 opacity-0 group-hover:opacity-100 transition-all"
                  title={locale === 'en' ? 'Remove' : '移除'}
                >
                  <X size={14} />
                </button>
              </div>
            );
          })}
        </div>
      )}

      <VerticalCompareTimeline
        referencePerson={referencePerson}
        comparisonPeople={comparisonPeople}
        allEvents={eventsMap}
      />
    </div>
  );
}
