'use client';

import { useState } from 'react';
import { useSearchParams } from 'next/navigation';
import { useLocale } from '@/i18n/LocaleProvider';
import PageHeader from '@/components/common/PageHeader';
import TimeRangeSelector from '@/components/parallel/TimeRangeSelector';
import ParallelWorldView from '@/components/parallel/ParallelWorldView';
import ParallelTimelineView from '@/components/parallel/ParallelTimelineView';
import EmptyState from '@/components/common/EmptyState';
import { getParallelEvents } from '@/lib/parallel';
import { getEventById, getPersonById } from '@/data/mockData';
import { formatYearRange } from '@/lib/date';
import { eventTitle, personName } from '@/lib/types';
import type { TimeRange } from '@/lib/types';
import { LayoutGrid, GitCommitHorizontal } from 'lucide-react';

type ViewMode = 'card' | 'timeline';

export default function ParallelPageContent() {
  const { locale, t } = useLocale();
  const searchParams = useSearchParams();

  const year = parseInt(searchParams.get('year') ?? '1080', 10);
  searchParams.get('startYear');
  searchParams.get('endYear');
  const focusEventId = searchParams.get('focusEvent') ?? undefined;
  const personId = searchParams.get('personId') ?? undefined;
  const range = (parseInt(searchParams.get('range') ?? '20', 10) || 20) as TimeRange;

  const [viewMode, setViewMode] = useState<ViewMode>('card');

  const focusEvent = focusEventId ? getEventById(focusEventId) : undefined;
  const focusPerson = personId ? getPersonById(personId) : undefined;

  const groups = getParallelEvents({
    year,
    range,
    focusEventId,
    focusPersonId: personId,
  });

  let title: string;
  if (focusEvent) {
    title = `${formatYearRange(focusEvent.startYear, focusEvent.endYear)}, ${eventTitle(focusEvent, locale)}`;
  } else if (focusPerson) {
    title = `${formatYearRange(focusPerson.birthYear, focusPerson.deathYear)}, ${personName(focusPerson, locale)}`;
  } else {
    title = locale === 'en' ? `Around ${year}` : `${year}年前后`;
  }

  const subtitle = range > 0
    ? (locale === 'en' ? `Time range: ${year - range} — ${year + range}` : `时间范围：${year - range} — ${year + range}年`)
    : undefined;

  const totalEvents = groups.reduce((sum, g) => sum + g.events.length, 0);

  return (
    <div>
      <PageHeader
        title={title}
        subtitle={subtitle}
        backTo="/"
        backLabel={t.nav.backToHome}
      />

      <div className="mb-6 flex flex-wrap items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <TimeRangeSelector currentRange={range} />

          {/* View mode toggle */}
          <div className="flex items-center bg-white border border-stone-200 rounded-lg overflow-hidden">
            <button
              onClick={() => setViewMode('card')}
              className={`flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium transition-colors
                ${viewMode === 'card'
                  ? 'bg-stone-800 text-white'
                  : 'text-stone-500 hover:text-stone-700 hover:bg-stone-50'
                }
              `}
              aria-pressed={viewMode === 'card'}
            >
              <LayoutGrid className="w-3.5 h-3.5" />
              {t.parallel.viewModeCard}
            </button>
            <button
              onClick={() => setViewMode('timeline')}
              className={`flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium transition-colors
                ${viewMode === 'timeline'
                  ? 'bg-stone-800 text-white'
                  : 'text-stone-500 hover:text-stone-700 hover:bg-stone-50'
                }
              `}
              aria-pressed={viewMode === 'timeline'}
            >
              <GitCommitHorizontal className="w-3.5 h-3.5" />
              {t.parallel.viewModeTimeline}
            </button>
          </div>
        </div>

        <p className="text-xs text-stone-400">
          {t.parallel.eventsCount
            .replace('{events}', String(totalEvents))
            .replace('{regions}', String(groups.length))}
        </p>
      </div>

      {groups.length === 0 ? (
        <EmptyState
          title={t.parallel.noData}
          description={t.parallel.noDataDesc}
        />
      ) : viewMode === 'timeline' ? (
        <ParallelTimelineView
          groups={groups}
          centerYear={year}
          range={range}
        />
      ) : (
        <ParallelWorldView groups={groups} />
      )}
    </div>
  );
}
