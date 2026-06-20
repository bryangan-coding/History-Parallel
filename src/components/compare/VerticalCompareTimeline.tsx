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
const CARD_WIDTH = 300;
const CARD_MIN_GAP = 12;
const MERGE_WINDOW = 5;

// Layout constants
const REF_CARD_RIGHT = 310; // right edge of reference cards (left of axis)
const AXIS_X = REF_CARD_RIGHT + 28; // timeline axis X position
const YEAR_LABEL_LEFT = AXIS_X + 8; // year labels on right of axis
const COMPARE_START_X = AXIS_X + 50; // first comparison column left

// ==================== Helpers ====================

function fmtYear(y: number): string {
  if (y < 0) return `前${Math.abs(y)}`;
  return String(y);
}

interface MergedCard {
  events: HistoricalEvent[];
  startYear: number;
  endYear: number;
}

interface LayoutCard extends MergedCard {
  y: number;
  /** Leftward shift for overlap avoidance (reference only) */
  shiftLeft: number;
}

// ==================== Card sub-component ====================

function EventCard({
  card,
  person,
  color,
  isReference,
  shiftLeft,
  onExpand,
}: {
  card: MergedCard;
  person: Person;
  color: string;
  isReference: boolean;
  shiftLeft: number;
  onExpand: (card: MergedCard, person: Person) => void;
}) {
  const { locale } = useLocale();
  const count = card.events.length;
  const primary = card.events[0];
  const isBirth = primary.tags?.includes('出生');
  const isDeath = primary.tags?.includes('逝世');

  return (
    <div
      className="bg-white border border-stone-200 rounded-lg hover:border-stone-400 hover:shadow-md transition-all cursor-pointer group"
      style={{
        borderLeftWidth: 3,
        borderLeftColor: color,
        minHeight: 42,
        marginLeft: shiftLeft,
        marginRight: shiftLeft > 0 ? -shiftLeft : 0,
      }}
    >
      <div className="px-3 py-2">
        <div className="flex items-start justify-between gap-1">
          <div className="min-w-0 flex-1">
            <div className="flex items-center gap-1.5">
              <div
                className="w-1.5 h-1.5 rounded-full flex-shrink-0"
                style={{
                  backgroundColor: isBirth || isDeath ? color : 'transparent',
                  border: isBirth || isDeath ? 'none' : `2px solid ${color}`,
                }}
              />
              <span className="text-xs font-medium text-stone-800 leading-snug line-clamp-1">
                {eventTitle(primary, locale)}
              </span>
              {count > 1 && (
                <span
                  className="text-[10px] font-medium px-1 rounded flex-shrink-0"
                  style={{ backgroundColor: `${color}15`, color }}
                >
                  +{count - 1}
                </span>
              )}
            </div>
            <div className="flex items-center gap-1.5 mt-1 ml-[18px]">
              <span className="text-[10px] font-mono text-stone-400">
                {fmtYear(card.startYear)}
                {card.endYear !== card.startYear ? ` – ${fmtYear(card.endYear)}` : ''}
              </span>
              {primary.importance >= 4 && (
                <span className="text-[9px] text-amber-500">
                  {'★'.repeat(Math.min(primary.importance - 3, 2))}
                </span>
              )}
            </div>
          </div>
          <button
            onClick={(e) => { e.stopPropagation(); onExpand(card, person); }}
            className="flex-shrink-0 p-1 rounded-md opacity-0 group-hover:opacity-100 hover:bg-stone-100 text-stone-400 hover:text-stone-600 transition-all"
            title="展开详情"
          >
            <Maximize2 size={12} />
          </button>
        </div>
        {isReference && primary.summary && (
          <p className="text-[11px] text-stone-500 leading-relaxed mt-1.5 ml-[18px] line-clamp-2">
            {primary.summary}
          </p>
        )}
      </div>
    </div>
  );
}

// ==================== Main Component ====================

interface VerticalCompareTimelineProps {
  referencePerson: Person | null;
  comparisonPeople: Person[];
  allEvents: Map<string, HistoricalEvent[]>;
}

export default function VerticalCompareTimeline({
  referencePerson,
  comparisonPeople,
  allEvents,
}: VerticalCompareTimelineProps) {
  const { locale, t } = useLocale();
  const [zoomIndex, setZoomIndex] = useState(2);
  const [expandedCard, setExpandedCard] = useState<MergedCard | null>(null);
  const [expandedPerson, setExpandedPerson] = useState<Person | null>(null);
  const [showAll, setShowAll] = useState<Record<string, boolean>>({});
  const zoom = ZOOM_STEPS[zoomIndex];
  const pixelsPerYear = BASE_PX_PER_YEAR * zoom;

  const allPeople = useMemo(() => {
    const list: Person[] = [];
    if (referencePerson) list.push(referencePerson);
    list.push(...comparisonPeople);
    return list;
  }, [referencePerson, comparisonPeople]);

  const { minYear, maxYear, totalSpan } = useMemo(() => {
    if (allPeople.length === 0) return { minYear: 0, maxYear: 100, totalSpan: 100 };
    let min = Infinity, max = -Infinity;
    allPeople.forEach((p) => {
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
  }, [allPeople]);

  const totalHeight = totalSpan * pixelsPerYear + PADDING_TOP + PADDING_BOTTOM;

  function yearToY(year: number): number {
    return PADDING_TOP + (year - minYear) * pixelsPerYear;
  }

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
      } else {
        cards.push({
          events: [evt],
          startYear: year,
          endYear: evt.endYear ?? year,
        });
      }
    }
    return cards;
  }

  // Compute cards for each person with overlap avoidance
  const personCardsMap = useMemo(() => {
    const map = new Map<string, LayoutCard[]>();

    for (const p of allPeople) {
      const merged = mergeEvents(allEvents.get(p.id) ?? []);
      const isReference = p === referencePerson;

      // Estimate card height for overlap calculation
      const estCardHeight = 80; // approximate pixel height per card

      // Layout with overlap avoidance (only for reference column)
      const layout: LayoutCard[] = [];
      for (const card of merged) {
        const y = yearToY(card.startYear);
        const cardTop = y;
        const cardBottom = cardTop + estCardHeight;

        let layer = 0;
        let found = false;
        const maxLayers = 6;

        while (!found && layer < maxLayers) {
          let overlaps = false;
          for (const prev of layout) {
            if (prev.shiftLeft !== layer * 20) continue;
            const prevBottom = prev.y + estCardHeight;
            if (cardTop < prevBottom + CARD_MIN_GAP && cardBottom > prev.y - CARD_MIN_GAP) {
              overlaps = true;
              break;
            }
          }
          if (!overlaps) found = true;
          else layer++;
        }

        layout.push({
          ...card,
          y,
          shiftLeft: isReference ? layer * 20 : 0,
        });
      }
      map.set(p.id, layout);
    }

    return map;
  }, [allPeople, allEvents, pixelsPerYear, minYear, referencePerson]);

  // Year ticks
  const yearTicks = useMemo(() => {
    const span = maxYear - minYear;
    let step = 10;
    if (span > 2000) step = 200;
    else if (span > 1000) step = 100;
    else if (span > 500) step = 50;
    else if (span > 200) step = 20;
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

  const scrolledRef = useRef(false);
  useEffect(() => {
    const container = scrollContainerRef.current;
    if (!container || !referencePerson?.birthYear || scrolledRef.current) return;
    scrolledRef.current = true;
    const y = yearToY(referencePerson.birthYear);
    container.scrollTop = y - container.clientHeight / 3;
  }, [referencePerson]);

  if (allPeople.length === 0) {
    return (
      <div className="mt-6 py-16 text-center">
        <p className="text-stone-400 text-sm">{t.compare.noPeople}</p>
        <p className="text-stone-300 text-xs mt-2">{t.compare.noPeopleDesc}</p>
      </div>
    );
  }

  const numComparisons = comparisonPeople.length;
  const totalWidth = COMPARE_START_X + numComparisons * (CARD_WIDTH + 20) + 40;

  return (
    <div className="mt-4">
      {/* Toolbar */}
      <div className="flex items-center justify-between mb-3 px-1">
        <span className="text-xs text-stone-400">
          {allPeople.length} 人 · {fmtYear(minYear)} – {fmtYear(maxYear)}
        </span>
        <div className="flex items-center gap-0.5 bg-stone-100 rounded-lg p-0.5 flex-shrink-0">
          <button onClick={handleZoomOut} disabled={zoomIndex === 0} className="p-1.5 rounded-md hover:bg-white disabled:opacity-25 text-stone-500"><Minus size={14} /></button>
          <span className="text-xs font-semibold text-stone-600 w-12 text-center tabular-nums">{Math.round(zoom * 100)}%</span>
          <button onClick={handleZoomIn} disabled={zoomIndex === ZOOM_STEPS.length - 1} className="p-1.5 rounded-md hover:bg-white disabled:opacity-25 text-stone-500"><Plus size={14} /></button>
        </div>
      </div>

      {/* Timeline */}
      <div className="border border-stone-200 rounded-xl bg-white shadow-sm overflow-hidden">
        <div className="overflow-auto" style={{ maxHeight: 'calc(100vh - 220px)' }}>
          <div ref={scrollContainerRef} className="overflow-auto" style={{ maxHeight: 'calc(100vh - 220px)' }}>
            <div className="relative" style={{ height: totalHeight, minWidth: totalWidth }}>

              {/* ===== Timeline axis ===== */}
              <div className="absolute top-0 bottom-0 z-0" style={{ left: AXIS_X, width: 1, backgroundColor: '#d6d3d1' }} />

              {/* ===== Year labels (RIGHT of axis, ABOVE cards via z-index) ===== */}
              {yearTicks.map(({ year, y }) => (
                <div
                  key={year}
                  className="absolute flex items-center z-30"
                  style={{ left: YEAR_LABEL_LEFT, top: y, transform: 'translateY(-50%)' }}
                >
                  {/* Small tick mark */}
                  <div
                    className="absolute rounded-full"
                    style={{
                      left: -4,
                      top: '50%',
                      transform: 'translate(-50%, -50%)',
                      width: year % 50 === 0 ? 6 : 4,
                      height: year % 50 === 0 ? 6 : 4,
                      backgroundColor: year % 50 === 0 ? '#78716c' : '#a8a29e',
                    }}
                  />
                  <span
                    className="text-[9px] font-mono select-none whitespace-nowrap"
                    style={{ color: year % 50 === 0 ? '#57534e' : '#a8a29e', fontWeight: year % 50 === 0 ? 600 : 400 }}
                  >
                    {fmtYear(year)}
                  </span>
                </div>
              ))}

              {/* ===== LEFT: Reference Person ===== */}
              {referencePerson && (() => {
                const color = PERSON_COLORS[0];
                const cards = personCardsMap.get(referencePerson.id) ?? [];
                const displayed = showAll[referencePerson.id] ? cards : cards.slice(0, 30);

                return (
                  <div className="absolute top-0" style={{ left: 0, width: REF_CARD_RIGHT }}>
                    {/* Column header */}
                    <div className="sticky top-0 z-20 bg-white/95 backdrop-blur-sm border-b border-stone-100 mb-2 px-2 py-2">
                      <div className="flex items-center justify-between">
                        <div className="flex items-center gap-1.5 min-w-0">
                          <div className="w-2 h-2 rounded-full flex-shrink-0" style={{ backgroundColor: color }} />
                          <span className="text-xs font-semibold text-stone-800 truncate">
                            {personName(referencePerson, locale)}
                          </span>
                        </div>
                        <span className="text-[10px] text-orange-500 font-medium flex-shrink-0 ml-1">
                          {locale === 'en' ? 'Ref' : '参照'}
                        </span>
                      </div>
                      {referencePerson.birthYear != null && referencePerson.deathYear != null && (
                        <span className="text-[10px] font-mono text-stone-400">
                          {fmtYear(referencePerson.birthYear)}–{fmtYear(referencePerson.deathYear)}
                        </span>
                      )}
                    </div>

                    {/* Lifespan bar */}
                    {referencePerson.birthYear != null && referencePerson.deathYear != null && (() => {
                      const barTop = yearToY(referencePerson.birthYear);
                      const barHeight = Math.max(yearToY(referencePerson.deathYear) - barTop, 4);
                      return (
                        <div
                          className="absolute w-0.5 rounded-full z-0"
                          style={{ right: 0, top: barTop, height: barHeight, backgroundColor: color, opacity: 0.12 }}
                        />
                      );
                    })()}

                    {/* Event cards */}
                    {displayed.map((card, i) => (
                      <div key={i} className="absolute z-10" style={{ top: card.y, left: 0, right: 0 }}>
                        <EventCard
                          card={card}
                          person={referencePerson}
                          color={color}
                          isReference={true}
                          shiftLeft={card.shiftLeft}
                          onExpand={openExpand}
                        />
                        <div style={{ height: CARD_MIN_GAP }} />
                      </div>
                    ))}

                    {cards.length > 30 && !showAll[referencePerson.id] && (
                      <div className="absolute bottom-0 left-0 right-0 z-20 bg-white/90 border-t border-stone-100 py-2 text-center">
                        <button
                          onClick={() => setShowAll(prev => ({ ...prev, [referencePerson.id]: true }))}
                          className="text-xs text-blue-600 hover:text-blue-800"
                        >
                          显示全部 {cards.length} 条
                        </button>
                      </div>
                    )}
                  </div>
                );
              })()}

              {/* ===== RIGHT: Comparison People ===== */}
              {comparisonPeople.map((person, idx) => {
                const color = PERSON_COLORS[(idx + 1) % PERSON_COLORS.length];
                const cards = personCardsMap.get(person.id) ?? [];
                const displayed = showAll[person.id] ? cards : cards.slice(0, 20);
                const colLeft = COMPARE_START_X + idx * (CARD_WIDTH + 20);

                return (
                  <div key={person.id} className="absolute top-0" style={{ left: colLeft, width: CARD_WIDTH }}>
                    {/* Column header */}
                    <div className="sticky top-0 z-20 bg-white/95 backdrop-blur-sm border-b border-stone-100 mb-2 px-2 py-2">
                      <div className="flex items-center justify-between">
                        <div className="flex items-center gap-1.5 min-w-0">
                          <div className="w-2 h-2 rounded-full flex-shrink-0" style={{ backgroundColor: color }} />
                          <span className="text-xs font-semibold text-stone-800 truncate">
                            {personName(person, locale)}
                          </span>
                        </div>
                      </div>
                      {person.birthYear != null && person.deathYear != null && (
                        <span className="text-[10px] font-mono text-stone-400">
                          {fmtYear(person.birthYear)}–{fmtYear(person.deathYear)}
                        </span>
                      )}
                    </div>

                    {/* Lifespan bar */}
                    {person.birthYear != null && person.deathYear != null && (() => {
                      const barTop = yearToY(person.birthYear);
                      const barHeight = Math.max(yearToY(person.deathYear) - barTop, 4);
                      return (
                        <div
                          className="absolute w-0.5 rounded-full z-0"
                          style={{ left: 0, top: barTop, height: barHeight, backgroundColor: color, opacity: 0.12 }}
                        />
                      );
                    })()}

                    {/* Event cards */}
                    {displayed.map((card, i) => (
                      <div key={i} className="absolute z-10" style={{ top: card.y, left: 0, right: 0 }}>
                        <EventCard
                          card={card}
                          person={person}
                          color={color}
                          isReference={false}
                          shiftLeft={0}
                          onExpand={openExpand}
                        />
                        <div style={{ height: CARD_MIN_GAP }} />
                      </div>
                    ))}

                    {cards.length > 20 && !showAll[person.id] && (
                      <div className="absolute bottom-0 left-0 right-0 z-20 bg-white/90 border-b border-stone-100 py-2 text-center">
                        <button
                          onClick={() => setShowAll(prev => ({ ...prev, [person.id]: true }))}
                          className="text-xs text-blue-600 hover:text-blue-800"
                        >
                          显示全部 {cards.length} 条
                        </button>
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </div>

      {/* ========== Expand Modal ========== */}
      {expandedCard && expandedPerson && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center p-4"
          style={{ backgroundColor: 'rgba(0,0,0,0.35)' }}
          onClick={closeExpand}
        >
          <div
            role="dialog" aria-modal="true"
            className="relative bg-white rounded-xl shadow-2xl max-w-xl w-full max-h-[75vh] flex flex-col"
            onClick={(e) => e.stopPropagation()}
          >
            <div
              className="flex items-center justify-between px-5 py-3 border-b border-stone-100 flex-shrink-0"
              style={{
                borderLeftWidth: 4,
                borderLeftColor: (() => {
                  const pi = allPeople.indexOf(expandedPerson);
                  return PERSON_COLORS[pi >= 0 ? pi % PERSON_COLORS.length : 0];
                })(),
              }}
            >
              <div>
                <span className="text-sm font-semibold text-stone-800">
                  {personName(expandedPerson, locale)}
                </span>
                <span className="text-[11px] text-stone-400 ml-2">
                  {fmtYear(expandedCard.startYear)}
                  {expandedCard.endYear !== expandedCard.startYear ? ` – ${fmtYear(expandedCard.endYear)}` : ''}
                </span>
                <span className="text-[11px] text-stone-400 ml-1">· {expandedCard.events.length} 件事</span>
              </div>
              <button onClick={closeExpand} className="p-1 rounded-full hover:bg-stone-100 text-stone-400">
                <X size={16} />
              </button>
            </div>
            <div className="px-5 py-3 overflow-y-auto flex-1 space-y-4">
              {expandedCard.events.map((evt) => (
                <div key={evt.id} className="border-b border-stone-100 pb-3 last:border-0">
                  <div className="flex items-center gap-2 mb-1">
                    <span className="text-[11px] font-mono text-stone-400">{fmtYear(evt.startYear ?? 0)}</span>
                    <span className="text-[10px] text-amber-500">
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
