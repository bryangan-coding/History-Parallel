'use client';

import { useMemo, useState, useCallback, useEffect, useRef } from 'react';
import type { Person, HistoricalEvent } from '@/lib/types';
import { useLocale } from '@/i18n/LocaleProvider';
import { personName, eventTitle, eventSummary } from '@/lib/types';
import { Minus, Plus, X, Maximize2 } from 'lucide-react';

// ==================== Constants ====================

const PERSON_COLORS = [
  '#d97706', '#2563eb', '#059669', '#dc2626',
  '#7c3aed', '#0d9488', '#ea580c', '#ca8a04',
];

const BASE_PX_PER_YEAR = 6;
const ZOOM_STEPS = [0.5, 0.75, 1, 1.5, 2, 3];
const PADDING_TOP = 56;
const PADDING_BOTTOM = 48;
const AXIS_WIDTH = 52;
const MAIN_PANEL_WIDTH = 420;
const COMPARE_COL_WIDTH = 240;
const CARD_MIN_HEIGHT = 40;
const MERGE_WINDOW = 5; // merge events within 5 years

// ==================== Helpers ====================

function fmtYear(y: number): string {
  if (y < 0) return `前${Math.abs(y)}`;
  return String(y);
}

interface MergedCard {
  events: HistoricalEvent[];
  startYear: number;
  endYear: number;
  y: number;
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
  const [expandedCard, setExpandedCard] = useState<MergedCard | null>(null);
  const [expandedPerson, setExpandedPerson] = useState<Person | null>(null);
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

  // 上方=更早: year越小Y越小
  function yearToY(year: number): number {
    return PADDING_TOP + (year - minYear) * pixelsPerYear;
  }

  // ===== Merge events into cards =====
  function mergeEvents(events: HistoricalEvent[]): MergedCard[] {
    if (events.length === 0) return [];
    const sorted = [...events]
      .filter(e => e.startYear != null)
      .sort((a, b) => (a.startYear ?? 0) - (b.startYear ?? 0));

    const cards: MergedCard[] = [];
    for (const evt of sorted) {
      const last = cards[cards.length - 1];
      const year = evt.startYear!;
      if (last && Math.abs(year - last.startYear) <= MERGE_WINDOW) {
        last.events.push(evt);
        last.endYear = Math.max(last.endYear, evt.endYear ?? year);
        last.y = yearToY(last.startYear);
      } else {
        cards.push({
          events: [evt],
          startYear: year,
          endYear: evt.endYear ?? year,
          y: yearToY(year),
        });
      }
    }
    return cards;
  }

  const mainCards = useMemo(() => {
    if (!mainPerson) return [];
    return mergeEvents(allEvents.get(mainPerson.id) ?? []);
  }, [mainPerson, allEvents, pixelsPerYear, minYear]);

  const compareCardsMap = useMemo(() => {
    const map = new Map<string, MergedCard[]>();
    for (const p of comparisonPeople) {
      map.set(p.id, mergeEvents(allEvents.get(p.id) ?? []));
    }
    return map;
  }, [comparisonPeople, allEvents, pixelsPerYear, minYear]);

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

  const openExpand = useCallback((card: MergedCard, person: Person) => {
    setExpandedCard(card);
    setExpandedPerson(person);
  }, []);
  const closeExpand = useCallback(() => { setExpandedCard(null); setExpandedPerson(null); }, []);
  useEffect(() => {
    if (!expandedCard) return;
    const h = (e: KeyboardEvent) => { if (e.key === 'Escape') closeExpand(); };
    window.addEventListener('keydown', h);
    return () => window.removeEventListener('keydown', h);
  }, [expandedCard, closeExpand]);

  const scrollContainerRef = useRef<HTMLDivElement>(null);
  const savedCenterYearRef = useRef<number | null>(null);

  const handleZoomIn = useCallback(() => {
    const newIndex = Math.min(ZOOM_STEPS.length - 1, zoomIndex + 1);
    const container = scrollContainerRef.current;
    if (container) {
      const centerY = container.scrollTop + container.clientHeight / 2;
      savedCenterYearRef.current = minYear + (centerY - PADDING_TOP) / pixelsPerYear;
    }
    setZoomIndex(newIndex);
  }, [zoomIndex, minYear, pixelsPerYear]);

  const handleZoomOut = useCallback(() => {
    const newIndex = Math.max(0, zoomIndex - 1);
    const container = scrollContainerRef.current;
    if (container) {
      const centerY = container.scrollTop + container.clientHeight / 2;
      savedCenterYearRef.current = minYear + (centerY - PADDING_TOP) / pixelsPerYear;
    }
    setZoomIndex(newIndex);
  }, [zoomIndex, minYear, pixelsPerYear]);

  useEffect(() => {
    if (savedCenterYearRef.current == null) return;
    const container = scrollContainerRef.current;
    if (!container) return;
    const centerYear = savedCenterYearRef.current;
    savedCenterYearRef.current = null;
    requestAnimationFrame(() => {
      const targetY = yearToY(centerYear);
      container.scrollTop = targetY - container.clientHeight / 2;
    });
  }, [pixelsPerYear, minYear]);

  const hScrollRef = useRef<HTMLDivElement>(null);
  const handleHScrollWheel = useCallback((e: React.WheelEvent) => {
    const el = hScrollRef.current;
    if (!el) return;
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

  // Scroll to birth year on mount
  useEffect(() => {
    const container = scrollContainerRef.current;
    if (!container || !mainPerson?.birthYear) return;
    const y = yearToY(mainPerson.birthYear);
    container.scrollTop = y - container.clientHeight / 3;
  }, []);

  return (
    <div className="mt-4">
      {/* Toolbar */}
      <div className="flex items-center justify-between mb-3 px-1">
        <div className="flex items-center gap-3">
          {mainPerson && (
            <div className="flex items-center gap-1.5">
              <div className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: PERSON_COLORS[0] }} />
              <span className="text-xs font-medium text-stone-600">{personName(mainPerson, locale)}</span>
            </div>
          )}
        </div>
        <div className="flex items-center gap-0.5 bg-stone-100 rounded-lg p-0.5">
          <button onClick={handleZoomOut} disabled={zoomIndex === 0} className="p-1.5 rounded-md hover:bg-white disabled:opacity-25 text-stone-500"><Minus size={14} /></button>
          <span className="text-xs font-semibold text-stone-600 w-12 text-center tabular-nums">{Math.round(zoom * 100)}%</span>
          <button onClick={handleZoomIn} disabled={zoomIndex === ZOOM_STEPS.length - 1} className="p-1.5 rounded-md hover:bg-white disabled:opacity-25 text-stone-500"><Plus size={14} /></button>
        </div>
      </div>

      <div className="border border-stone-200 rounded-xl bg-white shadow-sm overflow-hidden">
        <div ref={hScrollRef} className="overflow-x-auto" onWheel={handleHScrollWheel} style={{ maxHeight: 'calc(100vh - 200px)' }}>
          <div ref={scrollContainerRef} className="overflow-y-auto" style={{ maxHeight: 'calc(100vh - 200px)' }}>
            <div className="flex" style={{ minHeight: totalHeight, width: totalColsWidth, minWidth: '100%' }}>
              {/* ===== LEFT: Main Person ===== */}
              <div className="flex-shrink-0 border-r border-stone-200/60 bg-gradient-to-r from-stone-50/50 to-white" style={{ width: MAIN_PANEL_WIDTH }}>
                <div className="relative" style={{ height: totalHeight }}>
                  <div className="sticky top-0 z-20 bg-white/95 backdrop-blur-sm border-b border-stone-100 px-4 py-2.5">
                    <div className="flex items-center justify-between">
                      <span className="text-sm font-semibold text-stone-800 truncate">{mainPerson ? personName(mainPerson, locale) : ''}</span>
                      {mainPerson?.birthYear != null && mainPerson?.deathYear != null && (
                        <span className="text-[11px] font-mono text-stone-400 ml-2">{fmtYear(mainPerson.birthYear)}–{fmtYear(mainPerson.deathYear)}</span>
                      )}
                    </div>
                  </div>

                  {/* Lifespan bar */}
                  {mainPerson?.birthYear != null && mainPerson?.deathYear != null && (() => {
                    const barTop = yearToY(mainPerson.birthYear);
                    const barHeight = Math.max(yearToY(mainPerson.deathYear) - barTop, 4);
                    return <div className="absolute left-2 w-1 rounded-full z-0 opacity-15" style={{ top: barTop, height: barHeight, backgroundColor: PERSON_COLORS[0] }} />;
                  })()}

                  {/* Cards */}
                  {(() => {
                    const displayed = showAllMain ? mainCards : mainCards.slice(0, 30);
                    return (
                      <>
                        {displayed.map((card, i) => {
                          const color = PERSON_COLORS[0];
                          const count = card.events.length;
                          const primaryEvent = card.events[0];
                          const isBirth = primaryEvent.tags?.includes('出生');
                          const isDeath = primaryEvent.tags?.includes('逝世');
                          return (
                            <div key={i} className="absolute left-2 right-3 z-10" style={{ top: card.y }}>
                              <div
                                className="bg-white border border-stone-200 rounded-md px-2.5 py-1.5 hover:border-stone-400 hover:shadow-sm transition-all cursor-pointer"
                                style={{ borderLeftWidth: 3, borderLeftColor: color, minHeight: CARD_MIN_HEIGHT }}
                              >
                                <div className="flex items-start gap-1.5">
                                  <div className="w-1.5 h-1.5 rounded-full mt-1 flex-shrink-0" style={{ backgroundColor: isBirth || isDeath ? color : 'transparent', border: isBirth || isDeath ? 'none' : `2px solid ${color}` }} />
                                  <div className="min-w-0 flex-1">
                                    <div className="flex items-center gap-1">
                                      <span className="text-[11px] font-medium text-stone-800 leading-tight line-clamp-1">{eventTitle(primaryEvent, locale)}</span>
                                      {count > 1 && <span className="text-[10px] text-stone-400 bg-stone-100 px-1 rounded">+{count - 1}</span>}
                                    </div>
                                    <div className="flex items-center gap-2 mt-0.5">
                                      <span className="text-[10px] font-mono text-stone-400">{fmtYear(card.startYear)}{card.endYear !== card.startYear ? `–${fmtYear(card.endYear)}` : ''}</span>
                                    </div>
                                  </div>
                                  <button
                                    onClick={(e) => { e.stopPropagation(); mainPerson && openExpand(card, mainPerson); }}
                                    className="flex-shrink-0 p-0.5 rounded hover:bg-stone-100 text-stone-400 hover:text-stone-600 transition-colors"
                                    title="展开详情"
                                  >
                                    <Maximize2 size={12} />
                                  </button>
                                </div>
                              </div>
                            </div>
                          );
                        })}
                        {mainCards.length > 30 && !showAllMain && (
                          <div className="absolute bottom-0 left-0 right-0 z-20 bg-white/90 border-t border-stone-100 py-2 text-center">
                            <button onClick={() => setShowAllMain(true)} className="text-xs text-blue-600">显示全部 {mainCards.length} 条</button>
                          </div>
                        )}
                      </>
                    );
                  })()}
                </div>
              </div>

              {/* ===== CENTER: Axis ===== */}
              <div className="flex-shrink-0 relative bg-white" style={{ width: AXIS_WIDTH }}>
                <div className="relative" style={{ height: totalHeight }}>
                  <div className="sticky top-0 z-20 bg-white/95 border-b border-stone-100" style={{ height: 41 }} />
                  <div className="absolute left-1/2 top-0 bottom-0" style={{ width: 1, backgroundColor: '#d6d3d1' }} />
                  {yearTicks.map(({ year, y }) => (
                    <div key={year} className="absolute left-0 right-0 text-center" style={{ top: y, transform: 'translateY(-50%)' }}>
                      <span className="text-[9px] text-stone-400 font-mono select-none">{fmtYear(year)}</span>
                    </div>
                  ))}
                </div>
              </div>

              {/* ===== RIGHT: Comparison People ===== */}
              <div className="flex-1 overflow-x-auto min-w-0">
                <div className="flex" style={{ height: totalHeight, minWidth: Math.max(comparisonPeople.length * COMPARE_COL_WIDTH, 200) }}>
                  {comparisonPeople.map((person, idx) => {
                    const color = PERSON_COLORS[(idx + 1) % PERSON_COLORS.length];
                    const cards = compareCardsMap.get(person.id) ?? [];
                    const displayed = showAllCompare[person.id] ? cards : cards.slice(0, 20);
                    return (
                      <div key={person.id} className="flex-shrink-0 border-r border-stone-100 last:border-r-0" style={{ width: COMPARE_COL_WIDTH }}>
                        <div className="relative" style={{ height: totalHeight }}>
                          <div className="sticky top-0 z-20 bg-white/95 border-b border-stone-100 px-3 py-2.5">
                            <div className="flex items-center gap-1.5">
                              <div className="w-2 h-2 rounded-full" style={{ backgroundColor: color }} />
                              <span className="text-xs font-medium text-stone-700 truncate">{personName(person, locale)}</span>
                            </div>
                            {person.birthYear != null && person.deathYear != null && (
                              <span className="text-[10px] font-mono text-stone-400">{fmtYear(person.birthYear)}–{fmtYear(person.deathYear)}</span>
                            )}
                          </div>
                          {person.birthYear != null && person.deathYear != null && (() => {
                            const barTop = yearToY(person.birthYear);
                            const barHeight = Math.max(yearToY(person.deathYear) - barTop, 4);
                            return <div className="absolute left-4 w-1 rounded-full z-0 opacity-15" style={{ top: barTop, height: barHeight, backgroundColor: color }} />;
                          })()}
                          {displayed.map((card, i) => {
                            const count = card.events.length;
                            const primary = card.events[0];
                            return (
                              <div key={i} className="absolute left-3 right-2 z-10" style={{ top: card.y }}>
                                <div
                                  className="cursor-pointer hover:bg-stone-50 rounded px-1.5 py-1 transition-colors"
                                  onClick={() => openExpand(card, person)}
                                >
                                  <div className="flex items-center gap-1">
                                    <div className="w-1.5 h-1.5 rounded-full flex-shrink-0" style={{ border: `2px solid ${color}` }} />
                                    <span className="text-[10px] text-stone-700 font-medium line-clamp-1">{eventTitle(primary, locale)}</span>
                                    {count > 1 && <span className="text-[9px] text-stone-400">+{count - 1}</span>}
                                  </div>
                                  <span className="text-[9px] font-mono text-stone-400 ml-2.5">{fmtYear(card.startYear)}</span>
                                </div>
                              </div>
                            );
                          })}
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* ========== Expand Modal ========== */}
      {expandedCard && expandedPerson && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4" style={{ backgroundColor: 'rgba(0,0,0,0.35)' }} onClick={closeExpand}>
          <div
            role="dialog" aria-modal="true"
            className="relative bg-white rounded-xl shadow-2xl max-w-xl w-full max-h-[75vh] flex flex-col"
            onClick={(e) => e.stopPropagation()}
          >
            {/* Header */}
            <div className="flex items-center justify-between px-5 py-3 border-b border-stone-100 flex-shrink-0"
              style={{ borderLeftWidth: 4, borderLeftColor: (() => {
                const idx = people.indexOf(expandedPerson);
                return PERSON_COLORS[idx >= 0 ? idx % PERSON_COLORS.length : 0];
              })() }}
            >
              <div>
                <span className="text-sm font-semibold text-stone-800">{personName(expandedPerson, locale)}</span>
                <span className="text-[11px] text-stone-400 ml-2">
                  {fmtYear(expandedCard.startYear)}{expandedCard.endYear !== expandedCard.startYear ? `–${fmtYear(expandedCard.endYear)}` : ''}
                </span>
                <span className="text-[11px] text-stone-400 ml-1">· {expandedCard.events.length} 件事</span>
              </div>
              <button onClick={closeExpand} className="p-1 rounded-full hover:bg-stone-100 text-stone-400"><X size={16} /></button>
            </div>
            {/* Body */}
            <div className="px-5 py-3 overflow-y-auto flex-1 space-y-4">
              {expandedCard.events.map((evt) => (
                <div key={evt.id} className="border-b border-stone-100 pb-3 last:border-0">
                  <div className="flex items-center gap-2 mb-1">
                    <span className="text-[11px] font-mono text-stone-400">{fmtYear(evt.startYear ?? 0)}</span>
                    <span className="text-[10px] text-stone-400">
                      {'★'.repeat(evt.importance)}{'☆'.repeat(5 - evt.importance)}
                    </span>
                  </div>
                  <h4 className="text-sm font-semibold text-stone-800">{eventTitle(evt, locale)}</h4>
                  <p className="text-xs text-stone-600 leading-relaxed mt-1">{eventSummary(evt, locale)}</p>
                  {evt.description && evt.description !== eventSummary(evt, locale) && (
                    <p className="text-xs text-stone-500 leading-relaxed mt-1 whitespace-pre-wrap">{evt.description}</p>
                  )}
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
