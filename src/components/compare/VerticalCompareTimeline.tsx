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
const AXIS_WIDTH = 48;
const CARD_WIDTH = 320;
const CARD_GAP = 8;
const MERGE_WINDOW = 5;

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

// ==================== Card sub-component ====================

function EventCard({
  card,
  person,
  color,
  isMain,
  onExpand,
}: {
  card: MergedCard;
  person: Person;
  color: string;
  isMain: boolean;
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
        minHeight: 44,
      }}
    >
      <div className="px-3 py-2">
        {/* Header row */}
        <div className="flex items-start justify-between gap-2">
          <div className="min-w-0 flex-1">
            <div className="flex items-center gap-1.5">
              {/* Dot indicator */}
              <div
                className="w-1.5 h-1.5 rounded-full flex-shrink-0"
                style={{
                  backgroundColor: isBirth || isDeath ? color : 'transparent',
                  border: isBirth || isDeath ? 'none' : `2px solid ${color}`,
                }}
              />
              {/* Title */}
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
            {/* Year */}
            <div className="flex items-center gap-1.5 mt-1 ml-[18px]">
              <span className="text-[10px] font-mono text-stone-400">
                {fmtYear(card.startYear)}
                {card.endYear !== card.startYear ? ` – ${fmtYear(card.endYear)}` : ''}
              </span>
              {primary.importance >= 4 && (
                <span className="text-[9px] text-amber-500">{'★'.repeat(Math.min(primary.importance - 3, 2))}</span>
              )}
            </div>
          </div>

          {/* Expand button */}
          <button
            onClick={(e) => { e.stopPropagation(); onExpand(card, person); }}
            className="flex-shrink-0 p-1 rounded-md opacity-0 group-hover:opacity-100 hover:bg-stone-100 text-stone-400 hover:text-stone-600 transition-all"
            title="展开详情"
          >
            <Maximize2 size={12} />
          </button>
        </div>

        {/* Summary preview (only for main person) */}
        {isMain && primary.summary && (
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
  const [showAll, setShowAll] = useState<Record<string, boolean>>({});
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

  // All people to display (max 6)
  const displayPeople = people.slice(0, 6);

  function yearToY(year: number): number {
    return PADDING_TOP + (year - minYear) * pixelsPerYear;
  }

  // Merge nearby events into cards
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

  // Cards for each person
  const personCardsMap = useMemo(() => {
    const map = new Map<string, MergedCard[]>();
    for (const p of displayPeople) {
      map.set(p.id, mergeEvents(allEvents.get(p.id) ?? []));
    }
    return map;
  }, [displayPeople, allEvents, pixelsPerYear, minYear]);

  // Year ticks (10-year intervals)
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

  // Scroll to main person's birth year on mount
  const scrolledRef = useRef(false);
  useEffect(() => {
    const container = scrollContainerRef.current;
    const mainPerson = displayPeople[0];
    if (!container || !mainPerson?.birthYear || scrolledRef.current) return;
    scrolledRef.current = true;
    const y = yearToY(mainPerson.birthYear);
    container.scrollTop = y - container.clientHeight / 3;
  }, [displayPeople]);

  if (people.length === 0) {
    return (
      <div className="mt-6 py-16 text-center">
        <p className="text-stone-400 text-sm">{t.compare.noPeople}</p>
        <p className="text-stone-300 text-xs mt-2">{t.compare.noPeopleDesc}</p>
      </div>
    );
  }

  // Total width: axis + N columns of cards
  const numPeople = displayPeople.length;
  const totalWidth = AXIS_WIDTH + numPeople * (CARD_WIDTH + CARD_GAP) + 20;

  return (
    <div className="mt-4">
      {/* Toolbar */}
      <div className="flex items-center justify-between mb-3 px-1">
        <div className="flex items-center gap-4 flex-wrap">
          {displayPeople.map((person, idx) => {
            const color = PERSON_COLORS[idx % PERSON_COLORS.length];
            return (
              <div key={person.id} className="flex items-center gap-1.5">
                <div className="w-2.5 h-2.5 rounded-full flex-shrink-0" style={{ backgroundColor: color }} />
                <span className="text-xs font-medium text-stone-600 truncate max-w-[120px]">
                  {personName(person, locale)}
                </span>
                {person.birthYear != null && person.deathYear != null && (
                  <span className="text-[10px] font-mono text-stone-400">
                    {fmtYear(person.birthYear)}–{fmtYear(person.deathYear)}
                  </span>
                )}
              </div>
            );
          })}
        </div>
        <div className="flex items-center gap-0.5 bg-stone-100 rounded-lg p-0.5 flex-shrink-0">
          <button onClick={handleZoomOut} disabled={zoomIndex === 0} className="p-1.5 rounded-md hover:bg-white disabled:opacity-25 text-stone-500"><Minus size={14} /></button>
          <span className="text-xs font-semibold text-stone-600 w-12 text-center tabular-nums">{Math.round(zoom * 100)}%</span>
          <button onClick={handleZoomIn} disabled={zoomIndex === ZOOM_STEPS.length - 1} className="p-1.5 rounded-md hover:bg-white disabled:opacity-25 text-stone-500"><Plus size={14} /></button>
        </div>
      </div>

      {/* Timeline */}
      <div className="border border-stone-200 rounded-xl bg-white shadow-sm overflow-hidden">
        <div className="overflow-auto" style={{ maxHeight: 'calc(100vh - 200px)' }}>
          <div ref={scrollContainerRef} className="overflow-auto" style={{ maxHeight: 'calc(100vh - 200px)' }}>
            <div className="relative" style={{ height: totalHeight, minWidth: totalWidth }}>

              {/* ===== Axis with year ticks ===== */}
              <div className="absolute top-0 bottom-0" style={{ left: AXIS_WIDTH / 2, width: 1, backgroundColor: '#d6d3d1' }} />
              {yearTicks.map(({ year, y }) => (
                <div
                  key={year}
                  className="absolute left-0 flex items-center"
                  style={{ top: y, transform: 'translateY(-50%)' }}
                >
                  <span className="text-[9px] text-stone-400 font-mono select-none w-full text-center">
                    {fmtYear(year)}
                  </span>
                </div>
              ))}

              {/* ===== Each person's column ===== */}
              {displayPeople.map((person, idx) => {
                const color = PERSON_COLORS[idx % PERSON_COLORS.length];
                const cards = personCardsMap.get(person.id) ?? [];
                const displayed = showAll[person.id] ? cards : cards.slice(0, 30);
                const isMain = idx === 0;
                const colLeft = AXIS_WIDTH + idx * (CARD_WIDTH + CARD_GAP) + 8;

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
                        {person.birthYear != null && person.deathYear != null && (
                          <span className="text-[10px] font-mono text-stone-400 flex-shrink-0 ml-1">
                            {fmtYear(person.birthYear)}–{fmtYear(person.deathYear)}
                          </span>
                        )}
                      </div>
                    </div>

                    {/* Lifespan bar */}
                    {person.birthYear != null && person.deathYear != null && (() => {
                      const barTop = yearToY(person.birthYear);
                      const barHeight = Math.max(yearToY(person.deathYear) - barTop, 4);
                      return (
                        <div
                          className="absolute w-0.5 rounded-full z-0"
                          style={{ left: -4, top: barTop, height: barHeight, backgroundColor: color, opacity: 0.12 }}
                        />
                      );
                    })()}

                    {/* Event cards */}
                    {displayed.map((card, i) => (
                      <div
                        key={i}
                        className="absolute z-10"
                        style={{ top: card.y, left: 0, right: 0 }}
                      >
                        <EventCard
                          card={card}
                          person={person}
                          color={color}
                          isMain={isMain}
                          onExpand={openExpand}
                        />
                        <div style={{ height: CARD_GAP }} />
                      </div>
                    ))}

                    {/* Show more button */}
                    {cards.length > 30 && !showAll[person.id] && (
                      <div
                        className="absolute bottom-0 left-0 right-0 z-20 bg-white/90 border-t border-stone-100 py-2 text-center"
                      >
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
            {/* Header */}
            <div
              className="flex items-center justify-between px-5 py-3 border-b border-stone-100 flex-shrink-0"
              style={{
                borderLeftWidth: 4,
                borderLeftColor: (() => {
                  const pi = displayPeople.indexOf(expandedPerson);
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
            {/* Body */}
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
