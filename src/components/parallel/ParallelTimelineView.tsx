'use client';

import { useState, useMemo, useRef, useCallback } from 'react';
import type { ParallelRegionGroup, ScoredEvent } from '@/lib/types';
import { useLocale } from '@/i18n/LocaleProvider';
import { eventTitle, eventPlaceName, regionName } from '@/lib/types';
import { formatYearRange } from '@/lib/date';
import TimelineTrack from './TimelineTrack';
import EventPreviewPanel from './EventPreviewPanel';

interface Props {
  groups: ParallelRegionGroup[];
  centerYear: number;
  range: number;
}

/**
 * Horizontal parallel timeline:
 * - X axis = years
 * - Each region = a track (row)
 * - Events = nodes positioned by year
 * - Click node → open preview panel
 * - Mobile: degrades to vertical list
 */
export default function ParallelTimelineView({ groups, centerYear, range }: Props) {
  const { locale } = useLocale();
  const minYear = centerYear - range;
  const maxYear = centerYear + range;
  const totalSpan = maxYear - minYear;
  const [selectedEvent, setSelectedEvent] = useState<{
    event: ScoredEvent;
    region: ReturnType<typeof regionName>;
  } | null>(null);
  const [hoveredId, setHoveredId] = useState<string | null>(null);
  const scrollRef = useRef<HTMLDivElement>(null);

  // Build a flat list of all events with their region for mobile degrade
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const allEvents = useMemo(() => {
    const items: { scored: ScoredEvent; regionName: string }[] = [];
    for (const g of groups) {
      const rn = regionName(g.region, locale);
      for (const e of g.events) {
        items.push({ scored: e, regionName: rn });
      }
    }
    items.sort((a, b) => (a.scored.event.startYear ?? 0) - (b.scored.event.startYear ?? 0));
    return items;
  }, [groups, locale]);

  // Responsive: use a hook to detect mobile
  // For simplicity, we use CSS (@media) to hide/show.

  const handleNodeClick = useCallback(
    (scored: ScoredEvent, regionNameStr: string) => {
      setSelectedEvent({ event: scored, region: regionNameStr });
    },
    [],
  );

  const closePreview = useCallback(() => setSelectedEvent(null), []);

  // Calculate x position (percentage) for an event
  const getXPercent = (year: number) => {
    return ((year - minYear) / totalSpan) * 100;
  };

  // Importance → node size (px)
  const nodeSize = (imp: number) => {
    const sizes: Record<number, number> = { 1: 6, 2: 8, 3: 10, 4: 13, 5: 16 };
    return sizes[imp] ?? 8;
  };

  // Importance → node color
  const nodeColor = (imp: number) => {
    if (imp >= 4) return 'bg-amber-500 border-amber-600';
    if (imp >= 3) return 'bg-blue-500 border-blue-600';
    return 'bg-stone-400 border-stone-500';
  };

  const trackHeight = 56; // px per track
  const headerHeight = 36;
  const yearLabelCount = Math.min(totalSpan, 20); // max year labels

  return (
    <div className="relative">
      {/* View toggle is in ParallelPageContent, not here */}

      {/* Desktop: horizontal timeline */}
      <div className="hidden md:block">
        <div className="overflow-x-auto border border-stone-200 rounded-xl bg-white" ref={scrollRef}>
          <div className="relative" style={{ minWidth: 900, height: headerHeight + groups.length * trackHeight + 16 }}>
            {/* Year axis */}
            <div className="sticky top-0 z-10 bg-white border-b border-stone-100" style={{ height: headerHeight }}>
              <div className="relative" style={{ height: headerHeight }}>
                {/* Center marker */}
                <div
                  className="absolute top-0 bottom-0 border-l-2 border-red-400 z-10"
                  style={{ left: `${getXPercent(centerYear)}%` }}
                />
                <div
                  className="absolute -translate-x-1/2 text-[10px] font-semibold text-red-500 bg-white px-1"
                  style={{ left: `${getXPercent(centerYear)}%`, top: 2 }}
                >
                  {centerYear}
                </div>
                {/* Year ticks */}
                {Array.from({ length: yearLabelCount + 1 }, (_, i) => {
                  const y = Math.round(minYear + (totalSpan / yearLabelCount) * i);
                  if (y === centerYear) return null;
                  return (
                    <div
                      key={y}
                      className="absolute top-5 text-[9px] text-stone-400 -translate-x-1/2"
                      style={{ left: `${getXPercent(y)}%` }}
                    >
                      {y}
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Tracks */}
            {groups.map((group, trackIdx) => {
              const rn = regionName(group.region, locale);
              return (
                <TimelineTrack
                  key={group.region.id}
                  trackIndex={trackIdx}
                  regionName={rn}
                  events={group.events}
                  minYear={minYear}
                  totalSpan={totalSpan}
                  centerYear={centerYear}
                  trackHeight={trackHeight}
                  nodeSize={nodeSize}
                  nodeColor={nodeColor}
                  hoveredId={hoveredId}
                  selectedEventId={selectedEvent?.event.event.id ?? null}
                  onHover={setHoveredId}
                  onClick={handleNodeClick}
                  locale={locale}
                />
              );
            })}
          </div>
        </div>
      </div>

      {/* Mobile: vertical list degrade */}
      <div className="md:hidden space-y-4">
        {groups.map((group) => {
          const rn = regionName(group.region, locale);
          return (
            <div key={group.region.id}>
              <h4 className="text-xs font-semibold text-stone-500 uppercase tracking-wide mb-2 flex items-center gap-2">
                <span className="w-1.5 h-1.5 rounded-full bg-stone-400" />
                {rn}
              </h4>
              <div className="space-y-2">
                {group.events.map((scored) => (
                  <button
                    key={scored.event.id}
                    onClick={() => handleNodeClick(scored, rn)}
                    className="block w-full text-left p-3 rounded-lg border border-stone-200 bg-white hover:border-stone-400 transition-colors"
                  >
                    <div className="flex items-center gap-2 text-xs text-stone-500">
                      <span className="font-medium tabular-nums">
                        {formatYearRange(scored.event.startYear, scored.event.endYear)}
                      </span>
                      {eventPlaceName(scored.event, locale) && (
                        <span>{eventPlaceName(scored.event, locale)}</span>
                      )}
                    </div>
                    <p className="mt-0.5 text-sm font-medium text-stone-900">
                      {eventTitle(scored.event, locale)}
                    </p>
                  </button>
                ))}
              </div>
            </div>
          );
        })}
      </div>

      {/* Event preview panel (desktop) */}
      {selectedEvent && (
        <EventPreviewPanel
          scored={selectedEvent.event}
          regionName={selectedEvent.region}
          onClose={closePreview}
          locale={locale}
        />
      )}
    </div>
  );
}
