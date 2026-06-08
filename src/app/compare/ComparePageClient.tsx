'use client';

import { useState, useMemo, useCallback, useEffect } from 'react';
import { useSearchParams } from 'next/navigation';
import type { Person, HistoricalEvent } from '@/lib/types';
import { useLocale } from '@/i18n/LocaleProvider';
import PageHeader from '@/components/common/PageHeader';
import PersonSelector from '@/components/compare/PersonSelector';
import VerticalCompareTimeline from '@/components/compare/VerticalCompareTimeline';
import { lookupEventsForPerson } from '@/data/clientLookup';

interface ComparePageClientProps {
  allEvents: HistoricalEvent[];
}

export default function ComparePageClient({ allEvents }: ComparePageClientProps) {
  const { locale, t } = useLocale();
  const searchParams = useSearchParams();

  const [initialPeople, setInitialPeople] = useState<Person[]>([]);
  const [selectedPeople, setSelectedPeople] = useState<Person[]>([]);

  // Handle URL preselect by fetching the person — useEffect with proper cleanup
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

  // Collect all events for selected people
  const eventsMap = useMemo(() => {
    const map = new Map<string, HistoricalEvent[]>();
    selectedPeople.forEach((p) => {
      map.set(p.id, lookupEventsForPerson(allEvents, p.id));
    });
    return map;
  }, [selectedPeople, allEvents]);

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
              ? 'Maximum 6 people (1 main + 5 comparisons)'
              : '已选满 6 人（1 位主体 + 5 位对比），请先移除再添加'}
          </p>
        )}
      </div>

      <VerticalCompareTimeline people={selectedPeople} allEvents={eventsMap} />
    </div>
  );
}
