'use client';

import { useState, useMemo, useCallback } from 'react';
import { useSearchParams } from 'next/navigation';
import type { Person, HistoricalEvent } from '@/lib/types';
import { useLocale } from '@/i18n/LocaleProvider';
import PageHeader from '@/components/common/PageHeader';
import PersonSelector from '@/components/compare/PersonSelector';
import CompareTimeline from '@/components/compare/CompareTimeline';
import { people, getEventsForPerson, getPersonById } from '@/data/mockData';

export default function ComparePageClient() {
  const { t } = useLocale();
  const searchParams = useSearchParams();

  // Compute initial selected people (handle preselect from URL)
  const initialPeople = useMemo(() => {
    const preselectId = searchParams.get('preselect');
    if (!preselectId) return [];
    const person = getPersonById(preselectId);
    if (person && person.dataStatus === 'published') return [person];
    return [];
  }, [searchParams]);

  const [selectedPeople, setSelectedPeople] = useState<Person[]>(initialPeople);

  const handleAdd = useCallback((person: Person) => {
    setSelectedPeople((prev) => {
      if (prev.find((p) => p.id === person.id)) return prev;
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
      map.set(p.id, getEventsForPerson(p.id));
    });
    return map;
  }, [selectedPeople]);

  // Filter out only published people
  const availablePeople = useMemo(
    () => people.filter((p) => p.dataStatus === 'published'),
    []
  );

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
        </label>
        <PersonSelector
          allPeople={availablePeople}
          selected={selectedPeople}
          onAdd={handleAdd}
          onRemove={handleRemove}
        />
      </div>

      <CompareTimeline people={selectedPeople} allEvents={eventsMap} />
    </div>
  );
}
