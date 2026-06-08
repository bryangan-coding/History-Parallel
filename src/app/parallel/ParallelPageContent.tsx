'use client';

import { useState, useMemo, useEffect, useCallback } from 'react';
import { useSearchParams } from 'next/navigation';
import { useLocale } from '@/i18n/LocaleProvider';
import PageHeader from '@/components/common/PageHeader';
import TimeRangeSelector from '@/components/parallel/TimeRangeSelector';
import ParallelWorldView from '@/components/parallel/ParallelWorldView';
import ParallelTimelineView from '@/components/parallel/ParallelTimelineView';
import EmptyState from '@/components/common/EmptyState';
import { formatYearRange } from '@/lib/date';
import { eventTitle, personName } from '@/lib/types';
import type { ParallelRegionGroup, Region, TimeRange } from '@/lib/types';
import { fetchParallelEvents, fetchPerson, fetchEvent } from '@/data/server-actions';
import { LayoutGrid, GitCommitHorizontal, Map } from 'lucide-react';
import EventMapView from '@/components/parallel/EventMapView';
import TimeRangeSlider from '@/components/parallel/TimeRangeSlider';
import { buildRegionMap } from '@/data/clientLookup';

type ViewMode = 'card' | 'timeline' | 'map';

interface ParallelPageContentProps {
  regions: Region[];
}

export default function ParallelPageContent({ regions }: ParallelPageContentProps) {
  const { locale, t } = useLocale();
  const searchParams = useSearchParams();

  const rawYear = parseInt(searchParams.get('year') ?? '1080', 10);
  const year = isNaN(rawYear) ? 1080 : rawYear;
  const focusEventId = searchParams.get('focusEvent') ?? undefined;
  const personId = searchParams.get('personId') ?? undefined;
  const rangeVal = parseInt(searchParams.get('range') ?? '20', 10);
  const range = (isNaN(rangeVal) || ![0, 5, 20, 100].includes(rangeVal) ? 20 : rangeVal) as TimeRange;

  const [viewMode, setViewMode] = useState<ViewMode>('card');
  const [groups, setGroups] = useState<ParallelRegionGroup[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [focusEvent, setFocusEvent] = useState<Awaited<ReturnType<typeof fetchEvent>>>(undefined);
  const [focusPerson, setFocusPerson] = useState<Awaited<ReturnType<typeof fetchPerson>>>(undefined);
  const [yearRange, setYearRange] = useState<[number, number]>([-3000, 2000]);
  // Separate data range for TimeRangeSlider bounds (doesn't change with user selection)
  const [dataRange, setDataRange] = useState<[number, number]>([-3000, 2000]);

  const regionMap = useMemo(() => buildRegionMap(regions), [regions]);

  // Fetch parallel events via Server Action
  useEffect(() => {
    setLoading(true);
    setError(null);
    fetchParallelEvents({ year, range, focusEventId, focusPersonId: personId })
      .then(setGroups)
      .catch((err) => {
        setError(err instanceof Error ? err.message : 'Failed to load data');
        setGroups([]);
      })
      .finally(() => setLoading(false));
  }, [year, range, focusEventId, personId]);

  // Fetch focus event if needed
  useEffect(() => {
    if (focusEventId) {
      fetchEvent(focusEventId).then(setFocusEvent).catch(() => {});
    } else {
      setFocusEvent(undefined);
    }
  }, [focusEventId]);

  // Fetch focus person if needed
  useEffect(() => {
    if (personId) {
      fetchPerson(personId).then(setFocusPerson).catch(() => {});
    } else {
      setFocusPerson(undefined);
    }
  }, [personId]);

  // Compute full year range from loaded groups (for slider bounds, not user selection)
  useEffect(() => {
    if (groups.length > 0) {
      let min = Infinity;
      let max = -Infinity;
      for (const g of groups) {
        for (const s of g.events) {
          const ey = s.event.startYear ?? 0;
          const end = s.event.endYear ?? ey;
          if (ey < min) min = ey;
          if (end > max) max = end;
        }
      }
      if (min !== Infinity) {
        setDataRange([min, max]);
        // Only update yearRange if it hasn't been user-modified (matches default)
        setYearRange((prev) => {
          if (prev[0] === -3000 && prev[1] === 2000) return [min, max];
          return prev;
        });
      }
    }
  }, [groups]);

  // Filter groups by yearRange
  const filteredGroups = useMemo(() => {
    return groups.map((g) => ({
      ...g,
      events: g.events.filter((s) => {
        const ey = s.event.startYear ?? 0;
        const end = s.event.endYear ?? ey;
        return ey <= yearRange[1] && end >= yearRange[0];
      }),
    })).filter((g) => g.events.length > 0);
  }, [groups, yearRange]);

  const allEventsForSlider = useMemo(
    () => groups.flatMap((g) => g.events.map((s) => s.event)),
    [groups],
  );

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

  const totalEvents = filteredGroups.reduce((sum, g) => sum + g.events.length, 0);

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
            <button
              onClick={() => setViewMode('map')}
              className={`flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium transition-colors
                ${viewMode === 'map'
                  ? 'bg-stone-800 text-white'
                  : 'text-stone-500 hover:text-stone-700 hover:bg-stone-50'
                }
              `}
              aria-pressed={viewMode === 'map'}
            >
              <Map className="w-3.5 h-3.5" />
              {locale === 'en' ? 'Map' : '地图'}
            </button>
          </div>
        </div>

        <p className="text-xs text-stone-400">
          {t.parallel.eventsCount
            .replace('{events}', String(totalEvents))
            .replace('{regions}', String(filteredGroups.length))}
        </p>
      </div>

      {/* Loading state */}
      {loading && (
        <div className="flex items-center justify-center py-16">
          <div className="animate-spin w-8 h-8 border-2 border-stone-300 border-t-stone-600 rounded-full" />
        </div>
      )}

      {/* Error state */}
      {error && !loading && (
        <EmptyState
          title={locale === 'en' ? 'Failed to load' : '加载失败'}
          description={error}
        />
      )}

      {/* Time Range Slider */}
      {!loading && allEventsForSlider.length > 0 && (
        <div className="mb-6 p-4 bg-white rounded-lg border border-stone-200">
          <TimeRangeSlider
            events={allEventsForSlider}
            value={yearRange}
            onChange={setYearRange}
            minYear={dataRange[0]}
            maxYear={dataRange[1]}
          />
        </div>
      )}

      {!loading && filteredGroups.length === 0 ? (
        <EmptyState
          title={t.parallel.noData}
          description={t.parallel.noDataDesc}
        />
      ) : !loading && viewMode === 'timeline' ? (
        <ParallelTimelineView
          groups={filteredGroups}
          centerYear={year}
          range={range}
        />
      ) : !loading && viewMode === 'map' ? (
        <EventMapView
          events={filteredGroups.flatMap((g) => g.events.map((s) => s.event))}
          focusYear={year}
          range={range}
          yearRange={yearRange}
          regionMap={regionMap}
        />
      ) : !loading ? (
        <ParallelWorldView groups={filteredGroups} />
      ) : null}
    </div>
  );
}
