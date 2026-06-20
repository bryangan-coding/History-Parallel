'use client';

import { useMemo, useState, useCallback, useEffect, useRef } from 'react';
import type { Person, HistoricalEvent } from '@/lib/types';
import { useLocale } from '@/i18n/LocaleProvider';
import { personName, eventTitle, eventSummary } from '@/lib/types';
import { Minus, Plus, X } from 'lucide-react';

// ==================== Constants ====================

const PERSON_COLORS = [
  '#d97706', '#2563eb', '#059669', '#dc2626',
  '#7c3aed', '#0d9488', '#ea580c', '#ca8a04',
];

const BASE_PX_PER_YEAR = 6;
const ZOOM_STEPS = [0.5, 0.75, 1, 1.5, 2, 3];
const PADDING_TOP = 72;
const PADDING_BOTTOM = 48;
const AXIS_WIDTH = 48;
const MAIN_PANEL_WIDTH = 420;
const COMPARE_COL_WIDTH = 280;
const EVENT_CARD_HEIGHT = 48;
const MIN_EVENT_GAP = 8;
const EVENT_LIMIT_MAIN = 80;
const EVENT_LIMIT_COMPARE = 40;
const LANE_OFFSETS = [16, 150, 284];

// ==================== Helpers ====================

function fmtYear(y: number): string {
  if (y < 0) return `前${Math.abs(y)}`;
  return String(y);
}

// ==================== Component ====================

interface VerticalCompareTimelineProps {
  people: Person[];
  allEvents: Map<string, HistoricalEvent[]>;
}

export default function VerticalCompareTimeline({
  people,
  allEvents,
}: VerticalCompareTimelineProps) {
  const { locale, t } = useLocale();
  const [zoomIndex, setZoomIndex] = useState(2);
  const [selectedEvent, setSelectedEvent] = useState<HistoricalEvent | null>(null);
  const [selectedEventPerson, setSelectedEventPerson] = useState<Person | null>(null);
  const [showAllMain, setShowAllMain] = useState(false);
  const [showAllCompare, setShowAllCompare] = useState<Record<string, boolean>>({});
  const zoom = ZOOM_STEPS[zoomIndex];
  const pixelsPerYear = BASE_PX_PER_YEAR * zoom;

  const { minYear, maxYear, totalSpan } = useMemo(() => {
    if (people.length === 0) return { minYear: 0, maxYear: 100, totalSpan: 100 };
    let min = Infinity;
    let max = -Infinity;
    people.forEach((p) => {
      if (p.birthYear != null && p.birthYear < min) min = p.birthYear;
      if (p.deathYear != null && p.deathYear > max) max = p.deathYear;
    });
    if (!isFinite(min)) min = 0;
    if (!isFinite(max)) max = 100;
    const pad = Math.max((max - min) * 0.08, 10);
    return {
      minYear: Math.floor(min - pad),
      maxYear: Math.ceil(max + pad),
      totalSpan: max - min + pad * 2,
    };
  }, [people]);

  const totalHeight = totalSpan * pixelsPerYear + PADDING_TOP + PADDING_BOTTOM;

  const mainPerson = people[0];
  const comparisonPeople = people.slice(1, 6);

  function yearToY(year: number): number {
    return PADDING_TOP + (maxYear - year) * pixelsPerYear;
  }

  const yearTicks = useMemo(() => {
    const span = maxYear - minYear;
    let step: number;
    if (span <= 50) step = 5;
    else if (span <= 200) step = 10;
    else if (span <= 500) step = 25;
    else if (span <= 1000) step = 50;
    else if (span <= 2000) step = 100;
    else step = 200;

    const ticks: { year: number; y: number }[] = [];
    const start = Math.ceil(minYear / step) * step;
    for (let y = start; y <= maxYear; y += step) {
      ticks.push({ year: y, y: yearToY(y) });
    }
    return ticks;
  }, [minYear, maxYear, pixelsPerYear]);

  const layoutMainEvents = useMemo(() => {
    if (!mainPerson) return [];
    const rawEvents = (allEvents.get(mainPerson.id) ?? [])
      .filter((e) => e.startYear != null)
      .sort((a, b) => (a.startYear ?? 0) - (b.startYear ?? 0));

    interface Placed { event: HistoricalEvent; y: number; lane: number; }
    const placed: Placed[] = [];
    const lastYPerLane: number[] = [-Infinity, -Infinity, -Infinity];

    for (const event of rawEvents) {
      const baseY = yearToY(event.startYear!);
      let bestLane = -1;

      for (let lane = 0; lane < 3; lane++) {
        if (lastYPerLane[lane] === -Infinity) { bestLane = lane; break; }
        if (lastYPerLane[lane] - baseY >= EVENT_CARD_HEIGHT + MIN_EVENT_GAP) {
          if (bestLane === -1 || lastYPerLane[lane] > lastYPerLane[bestLane]) {
            bestLane = lane;
          }
        }
      }
      if (bestLane === -1) bestLane = lastYPerLane.indexOf(Math.max(...lastYPerLane));

      placed.push({ event, y: baseY, lane: bestLane });
      lastYPerLane[bestLane] = baseY;
    }
    return placed;
  }, [mainPerson, allEvents, pixelsPerYear, minYear, maxYear]);

  const layoutCompareEvents = useCallback(
    (person: Person) => {
      const rawEvents = (allEvents.get(person.id) ?? [])
        .filter((e) => e.startYear != null)
        .sort((a, b) => (a.startYear ?? 0) - (b.startYear ?? 0));
      interface Placed { event: HistoricalEvent; y: number; }
      const placed: Placed[] = [];
      const lastYPerLane: number[] = [-Infinity, -Infinity];
      for (const event of rawEvents) {
        const baseY = yearToY(event.startYear!);
        let bestLane = 0;
        const minGap = 18;
        let maxLastY = -Infinity;
        for (let lane = 0; lane < 2; lane++) {
          if (lastYPerLane[lane] === -Infinity) { bestLane = lane; break; }
          if (lastYPerLane[lane] - baseY >= minGap) {
            if (maxLastY === -Infinity || lastYPerLane[lane] > maxLastY) {
              bestLane = lane; maxLastY = lastYPerLane[lane];
            }
          }
        }
        if (maxLastY === -Infinity && lastYPerLane[0] !== -Infinity) {
          bestLane = lastYPerLane[0] > lastYPerLane[1] ? 0 : 1;
        }
        placed.push({ event, y: baseY });
        lastYPerLane[bestLane] = baseY;
      }
      return placed;
    },
    [allEvents, pixelsPerYear, minYear, maxYear],
  );

  const openModal = useCallback((event: HistoricalEvent, person: Person) => {
    setSelectedEvent(event);
    setSelectedEventPerson(person);
  }, []);
  const closeModal = useCallback(() => { setSelectedEvent(null); setSelectedEventPerson(null); }, []);
  useEffect(() => {
    if (!selectedEvent) return;
    const handler = (e: KeyboardEvent) => { if (e.key === 'Escape') closeModal(); };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, [selectedEvent, closeModal]);

  const scrollContainerRef = useRef<HTMLDivElement>(null);
  const savedCenterYearRef = useRef<number | null>(null);

  const handleZoomIn = useCallback(() => {
    const newIndex = Math.min(ZOOM_STEPS.length - 1, zoomIndex + 1);
    const container = scrollContainerRef.current;
    if (container) {
      const centerY = container.scrollTop + container.clientHeight / 2;
      savedCenterYearRef.current = maxYear - (centerY - PADDING_TOP) / pixelsPerYear;
    }
    setZoomIndex(newIndex);
  }, [zoomIndex, maxYear, pixelsPerYear]);

  const handleZoomOut = useCallback(() => {
    const newIndex = Math.max(0, zoomIndex - 1);
    const container = scrollContainerRef.current;
    if (container) {
      const centerY = container.scrollTop + container.clientHeight / 2;
      savedCenterYearRef.current = maxYear - (centerY - PADDING_TOP) / pixelsPerYear;
    }
    setZoomIndex(newIndex);
  }, [zoomIndex, maxYear, pixelsPerYear]);

  useEffect(() => {
    if (savedCenterYearRef.current == null) return;
    const container = scrollContainerRef.current;
    if (!container) return;
    const centerYear = savedCenterYearRef.current;
    savedCenterYearRef.current = null;
    requestAnimationFrame(() => {
      const targetY = PADDING_TOP + (maxYear - centerYear) * pixelsPerYear;
      container.scrollTop = targetY - container.clientHeight / 2;
    });
  }, [pixelsPerYear, maxYear]);

  // --- Horizontal mouse wheel scroll ---
  const hScrollRef = useRef<HTMLDivElement>(null);
  const handleHScrollWheel = useCallback((e: React.WheelEvent) => {
    const el = hScrollRef.current;
    if (!el) return;
    // If horizontal scroll is possible, translate vertical wheel to horizontal
    if (el.scrollWidth > el.clientWidth) {
      e.preventDefault();
      el.scrollLeft += e.deltaY;
    }
  }, []);

  if (people.length === 0) {
    return (
      <div className="mt-6 py-16 text-center">
        <p className="text-stone-400 text-sm">{t.compare.noPeople}</p>
        <p className="text-stone-300 text-xs mt-2">{t.compare.noPeopleDesc}</p>
      </div>
    );
  }

  const totalColsWidth = MAIN_PANEL_WIDTH + AXIS_WIDTH + Math.max(comparisonPeople.length * COMPARE_COL_WIDTH, 200);

  return (
    <div className="mt-4">
      {/* Toolbar */}
      <div className="flex items-center justify-between mb-3 px-1">
        <div className="flex items-center gap-3">
          {mainPerson && (
            <div className="flex items-center gap-1.5">
              <div className="w-2.5 h-2.5 rounded-full flex-shrink-0" style={{ backgroundColor: PERSON_COLORS[0] }} />
              <span className="text-xs font-medium text-stone-600">{personName(mainPerson, locale)}</span>
              <span className="text-[10px] text-stone-400 bg-stone-100 px-1.5 py-0.5 rounded">{t.compare.mainPerson || '主体'}</span>
            </div>
          )}
          {comparisonPeople.length > 0 && (
            <span className="text-[10px] text-stone-400">vs {comparisonPeople.length} {locale === 'en' ? 'others' : '人对比'}</span>
          )}
        </div>
        <div className="flex items-center gap-0.5 bg-stone-100 rounded-lg p-0.5">
          <button onClick={handleZoomOut} disabled={zoomIndex === 0} className="p-1.5 rounded-md hover:bg-white disabled:opacity-25 disabled:hover:bg-transparent text-stone-500" aria-label="Zoom out"><Minus size={14} /></button>
          <span className="text-xs font-semibold text-stone-600 w-12 text-center tabular-nums select-none">{Math.round(zoom * 100)}%</span>
          <button onClick={handleZoomIn} disabled={zoomIndex === ZOOM_STEPS.length - 1} className="p-1.5 rounded-md hover:bg-white disabled:opacity-25 disabled:hover:bg-transparent text-stone-500" aria-label="Zoom in"><Plus size={14} /></button>
        </div>
      </div>

      {/* ========== Main Comparison Area: horizontal scroll via mouse wheel ========== */}
      <div className="border border-stone-200 rounded-xl bg-white shadow-sm overflow-hidden">
        <div
          ref={hScrollRef}
          className="overflow-x-auto"
          onWheel={handleHScrollWheel}
          style={{ maxHeight: 'calc(100vh - 260px)' }}
        >
          <div className="flex" style={{ minHeight: totalHeight, width: totalColsWidth, minWidth: '100%' }}>
            {/* ===== LEFT: Main Person ===== */}
            <div className="flex-shrink-0 border-r border-stone-200/60 bg-gradient-to-r from-stone-50/50 to-white" style={{ width: MAIN_PANEL_WIDTH }}>
              <div className="relative" style={{ height: totalHeight }}>
                <div className="sticky top-0 z-20 bg-white/95 backdrop-blur-sm border-b border-stone-100 px-4 py-3">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2 min-w-0">
                      <div className="w-2.5 h-2.5 rounded-full flex-shrink-0" style={{ backgroundColor: PERSON_COLORS[0], boxShadow: `0 0 0 1px #fff, 0 0 0 3px ${PERSON_COLORS[0]}30` }} />
                      <span className="text-sm font-semibold text-stone-800 truncate">{mainPerson ? personName(mainPerson, locale) : ''}</span>
                    </div>
                    {mainPerson?.birthYear != null && mainPerson?.deathYear != null && (
                      <span className="text-[11px] font-mono text-stone-400 tabular-nums flex-shrink-0 ml-2">{fmtYear(mainPerson.birthYear)}–{fmtYear(mainPerson.deathYear)}</span>
                    )}
                  </div>
                </div>

                {mainPerson?.birthYear != null && mainPerson?.deathYear != null && (() => {
                  const barTop = yearToY(mainPerson.deathYear);
                  const barBottom = yearToY(mainPerson.birthYear);
                  const barHeight = Math.max(barBottom - barTop, 6);
                  return <div className="absolute left-0 w-1 rounded-full z-0 opacity-20" style={{ top: barTop, height: barHeight, backgroundColor: PERSON_COLORS[0] }} />;
                })()}

                {(() => {
                  const totalCount = layoutMainEvents.length;
                  const displayedEvents = showAllMain ? layoutMainEvents : layoutMainEvents.slice(0, EVENT_LIMIT_MAIN);
                  const hasMore = totalCount > EVENT_LIMIT_MAIN;
                  return (
                    <>
                      {displayedEvents.map(({ event, y, lane }) => {
                        const color = PERSON_COLORS[0];
                        const evtTitle = eventTitle(event, locale);
                        const evtSummary = eventSummary(event, locale);
                        const year = event.startYear;
                        const isBirth = event.tags?.includes('出生');
                        const isDeath = event.tags?.includes('逝世');
                        const leftOffset = LANE_OFFSETS[lane] ?? LANE_OFFSETS[0];
                        const cardMaxWidth = MAIN_PANEL_WIDTH - leftOffset - 16;
                        return (
                          <div key={event.id} className="absolute" style={{ top: y, left: leftOffset, zIndex: 10 }}>
                            <div className="bg-white border border-stone-200 rounded-md px-3 py-2 hover:border-stone-400 hover:shadow-md transition-all duration-150 cursor-pointer select-none"
                              role="button" tabIndex={0} onClick={() => mainPerson && openModal(event, mainPerson)}
                              onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); mainPerson && openModal(event, mainPerson); } }}
                              style={{ width: cardMaxWidth, borderLeftWidth: 3, borderLeftColor: color, minHeight: EVENT_CARD_HEIGHT }}>
                              <div className="flex items-start gap-1.5">
                                <div className="w-2 h-2 rounded-full mt-0.5 flex-shrink-0" style={{ backgroundColor: isBirth || isDeath ? color : 'transparent', border: isBirth || isDeath ? 'none' : `2px solid ${color}` }} />
                                <div className="min-w-0 flex-1">
                                  <div className="text-xs font-medium text-stone-800 leading-tight line-clamp-2">{evtTitle}</div>
                                  <div className="flex items-center gap-2 mt-0.5">
                                    {year != null && <span className="text-[10px] font-mono text-stone-400 whitespace-nowrap tabular-nums">{fmtYear(year)}</span>}
                                    {evtSummary && <span className="text-[10px] text-stone-400 truncate">{evtSummary}</span>}
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        );
                      })}
                      {hasMore && (
                        <div className="sticky bottom-0 z-20 bg-white/90 backdrop-blur-sm border-t border-stone-100 py-2 px-4 text-center">
                          <button onClick={() => setShowAllMain(!showAllMain)} className="text-xs text-blue-600 hover:text-blue-700 font-medium">
                            {showAllMain ? (locale === 'en' ? 'Show fewer' : '收起') : (locale === 'en' ? `Show all ${totalCount} events` : `显示全部 ${totalCount} 条事件`)}
                          </button>
                        </div>
                      )}
                    </>
                  );
                })()}

                {layoutMainEvents.length === 0 && mainPerson && (
                  <div className="absolute inset-0 flex items-center justify-center"><p className="text-xs text-stone-300">{t.compare.empty}</p></div>
                )}
              </div>
            </div>

            {/* ===== CENTER: Timeline Axis ===== */}
            <div className="flex-shrink-0 relative bg-white" style={{ width: AXIS_WIDTH }}>
              <div className="relative" style={{ height: totalHeight }}>
                <div className="sticky top-0 z-20 bg-white/95 backdrop-blur-sm border-b border-stone-100" style={{ height: 49 }} />
                <div className="absolute left-1/2 top-0 bottom-0" style={{ width: 1, backgroundColor: '#d6d3d1', transform: 'translateX(-0.5px)' }} />
                {yearTicks.map(({ year, y }) => (
                  <div key={year} className="absolute left-0 right-0 flex items-center" style={{ top: y, transform: 'translateY(-0.5px)' }}>
                    <span className={`text-[9px] px-1 select-none whitespace-nowrap font-mono tabular-nums w-full text-center ${yearTicks.length <= 10 ? 'text-stone-500 font-medium' : (Math.abs(year) < 100 || year === 0 ? 'text-stone-500 font-medium' : 'text-stone-400')}`}>{fmtYear(year)}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* ===== RIGHT: Comparison People ===== */}
            <div className="flex-1 overflow-x-auto min-w-0">
              <div className="flex" style={{ height: totalHeight, minWidth: Math.max(comparisonPeople.length * COMPARE_COL_WIDTH, 200) }}>
                {comparisonPeople.length === 0 && (
                  <div className="flex-1 flex items-center justify-center" style={{ height: totalHeight }}>
                    <p className="text-xs text-stone-300">{locale === 'en' ? 'Add comparison people above' : '在上方搜索框中添加对比人物'}</p>
                  </div>
                )}
                {comparisonPeople.map((person, idx) => {
                  const color = PERSON_COLORS[(idx + 1) % PERSON_COLORS.length];
                  const events = layoutCompareEvents(person);
                  const birth = person.birthYear;
                  const death = person.deathYear;
                  return (
                    <div key={person.id} className="flex-shrink-0 border-r border-stone-100 last:border-r-0" style={{ width: COMPARE_COL_WIDTH }}>
                      <div className="relative" style={{ height: totalHeight }}>
                        <div className="sticky top-0 z-20 bg-white/95 backdrop-blur-sm border-b border-stone-100 px-4 py-3">
                          <div className="flex items-center gap-1.5">
                            <div className="w-2 h-2 rounded-full flex-shrink-0" style={{ backgroundColor: color }} />
                            <span className="text-xs font-medium text-stone-700 truncate flex-1">{personName(person, locale)}</span>
                          </div>
                          {birth != null && death != null && <span className="text-[10px] font-mono text-stone-400 tabular-nums">{fmtYear(birth)}–{fmtYear(death)}</span>}
                        </div>
                        {birth != null && death != null && (() => {
                          const barTop = yearToY(death); const barBottom = yearToY(birth);
                          const barHeight = Math.max(barBottom - barTop, 6);
                          return <div className="absolute left-5 w-1 rounded-full z-0 opacity-25" style={{ top: barTop, height: barHeight, backgroundColor: color }} />;
                        })()}
                        {(() => {
                          const allCount = events.length;
                          const displayedEvents = showAllCompare[person.id] ? events : events.slice(0, EVENT_LIMIT_COMPARE);
                          const hasMore = allCount > EVENT_LIMIT_COMPARE;
                          return (
                            <>
                              {displayedEvents.map(({ event, y }) => {
                                const shortTitle = eventTitle(event, locale);
                                const shortSummary = eventSummary(event, locale);
                                const isBirth = event.tags?.includes('出生');
                                const isDeath = event.tags?.includes('逝世');
                                return (
                                  <div key={event.id} className="absolute left-3 z-10" style={{ top: y, transform: 'translateY(-50%)' }}>
                                    <div role="button" tabIndex={0} onClick={() => openModal(event, person)} onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openModal(event, person); } }}
                                      className="cursor-pointer hover:bg-stone-50 rounded px-2 py-1 -mx-2 -my-1 transition-colors max-w-[240px]">
                                      <div className="flex items-center gap-1.5">
                                        <div className="flex-shrink-0 rounded-full" style={{ width: isBirth || isDeath ? 8 : 6, height: isBirth || isDeath ? 8 : 6, backgroundColor: isBirth || isDeath ? color : '#fff', border: `2px solid ${color}` }} />
                                        <div className="min-w-0">
                                          <span className="text-[11px] text-stone-700 font-medium leading-tight line-clamp-1">{shortTitle}</span>
                                          {shortSummary && <span className="block text-[10px] text-stone-400 leading-tight line-clamp-1 mt-0.5">{shortSummary}</span>}
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                );
                              })}
                              {hasMore && (
                                <div className="sticky bottom-0 z-20 bg-white/90 backdrop-blur-sm border-t border-stone-100 py-1.5 px-3 text-center">
                                  <button onClick={() => setShowAllCompare((prev) => ({ ...prev, [person.id]: !prev[person.id] }))} className="text-[10px] text-blue-600 hover:text-blue-700 font-medium">
                                    {showAllCompare[person.id] ? (locale === 'en' ? 'Show fewer' : '收起') : (locale === 'en' ? `Show all ${allCount} events` : `显示全部 ${allCount} 条事件`)}
                                  </button>
                                </div>
                              )}
                            </>
                          );
                        })()}
                        {events.length === 0 && <div className="absolute inset-0 flex items-center justify-center"><p className="text-[10px] text-stone-300">{t.compare.empty}</p></div>}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>
        </div>

        {/* Horizontal scroll hint */}
        {comparisonPeople.length > 1 && (
          <div className="border-t border-stone-100 bg-stone-50/50 px-4 py-1.5">
            <p className="text-[10px] text-stone-400 text-right">
              {locale === 'en' ? `← Scroll to see all people →` : `← 滚轮滑动查看全部对比人物 →`}
            </p>
          </div>
        )}
      </div>

      {/* ========== Event Detail Modal ========== */}
      {selectedEvent && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4" style={{ backgroundColor: 'rgba(0,0,0,0.45)' }} onClick={closeModal}>
          <div role="dialog" aria-modal="true" className="relative bg-white rounded-xl shadow-2xl max-w-lg w-full max-h-[80vh] overflow-y-auto" onClick={(e) => e.stopPropagation()}>
            <button onClick={closeModal} className="absolute top-3 right-3 p-1.5 rounded-full hover:bg-stone-100 text-stone-400 hover:text-stone-600 transition-colors z-10" aria-label="Close"><X size={16} /></button>
            <div className="px-6 pt-5 pb-3 border-b border-stone-100" style={{ borderLeftWidth: 4, borderLeftColor: (() => { if (!selectedEventPerson) return PERSON_COLORS[0]; const idx = people.indexOf(selectedEventPerson); return PERSON_COLORS[idx >= 0 ? idx : 0]; })() }}>
              <div className="pr-8">
                <h3 className="text-base font-semibold text-stone-800 leading-snug">{eventTitle(selectedEvent, locale)}</h3>
                {selectedEventPerson && <p className="text-[11px] text-stone-400 mt-1">{personName(selectedEventPerson, locale)}{selectedEvent.startYear != null && <span className="ml-2 font-mono">{fmtYear(selectedEvent.startYear)}</span>}</p>}
              </div>
            </div>
            <div className="px-6 py-4 space-y-3">
              {eventSummary(selectedEvent, locale) && <p className="text-sm text-stone-600 leading-relaxed">{eventSummary(selectedEvent, locale)}</p>}
              {selectedEvent.description && <div className="text-sm text-stone-500 leading-relaxed whitespace-pre-wrap">{selectedEvent.description}</div>}
              <div className="flex flex-wrap gap-2 pt-2 border-t border-stone-100">
                {selectedEvent.startYear != null && <span className="inline-flex items-center gap-1 text-[11px] text-stone-500 bg-stone-100 px-2 py-0.5 rounded">{locale === 'en' ? 'Start Year' : '起始年份'}: {fmtYear(selectedEvent.startYear)}</span>}
                {selectedEvent.endYear != null && <span className="inline-flex items-center gap-1 text-[11px] text-stone-500 bg-stone-100 px-2 py-0.5 rounded">{locale === 'en' ? 'End Year' : '结束年份'}: {fmtYear(selectedEvent.endYear)}</span>}
                {selectedEvent.importance != null && <span className="inline-flex items-center gap-1 text-[11px] text-stone-500 bg-stone-100 px-2 py-0.5 rounded">{locale === 'en' ? 'Importance' : '重要性'}: {'★'.repeat(selectedEvent.importance)}{'☆'.repeat(5 - selectedEvent.importance)}</span>}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
