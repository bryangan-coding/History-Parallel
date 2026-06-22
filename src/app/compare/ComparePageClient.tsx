'use client';

import { useState, useMemo, useCallback, useEffect } from 'react';
import { useSearchParams } from 'next/navigation';
import type { Person, HistoricalEvent } from '@/lib/types';
import { useLocale } from '@/i18n/LocaleProvider';
import PageHeader from '@/components/common/PageHeader';
import PersonSelector from '@/components/compare/PersonSelector';
import VerticalCompareTimeline from '@/components/compare/VerticalCompareTimeline';
import { Maximize2, Minimize2 } from 'lucide-react';

export default function ComparePageClient() {
  const { locale, t, toScript } = useLocale();
  const searchParams = useSearchParams();

  const [initialPeople, setInitialPeople] = useState<Person[]>([]);
  const [selectedPeople, setSelectedPeople] = useState<Person[]>([]);
  const [personEvents, setPersonEvents] = useState<Map<string, HistoricalEvent[]>>(new Map());
  const [isFullscreen, setIsFullscreen] = useState(false);

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
          onSetReference={handleSetReference}
        />
        {selectedPeople.length >= 6 && (
          <p className="text-xs text-amber-600 mt-1.5">
            {locale === 'en'
              ? 'Maximum 6 people (1 reference + 5 comparisons)'
              : toScript('已选满 6 人（1 位参照 + 5 位对比），请先移除再添加')}
          </p>
        )}
      </div>

      {/* ===== Compare timeline area with fullscreen toggle ===== */}
      {selectedPeople.length > 0 && (
        <div
          className={
            isFullscreen
              ? 'fixed inset-0 z-50 bg-stone-50 flex flex-col'
              : 'relative mt-6'
          }
        >
          <div className={isFullscreen ? 'flex-1 overflow-auto px-4 py-2' : ''}>
            <VerticalCompareTimeline
              referencePerson={referencePerson}
              comparisonPeople={comparisonPeople}
              allEvents={eventsMap}
              fullscreenButton={
                <button
                  onClick={() => setIsFullscreen(!isFullscreen)}
                  className={`absolute top-3 right-3 z-10 p-1.5 rounded-lg border border-stone-200 bg-white/90 hover:bg-white hover:border-stone-400 transition-all text-stone-400 hover:text-stone-600 ${
                    isFullscreen ? 'shadow-sm' : ''
                  }`}
                  title={isFullscreen ? (locale === 'en' ? 'Exit Fullscreen' : toScript('退出全屏')) : (locale === 'en' ? 'Fullscreen' : toScript('全屏'))}
                >
                  {isFullscreen ? <Minimize2 size={16} /> : <Maximize2 size={16} />}
                </button>
              }
            />
          </div>
        </div>
      )}
    </div>
  );
}
