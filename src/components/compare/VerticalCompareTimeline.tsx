'use client';

import { useMemo, useState, useCallback } from 'react';
import type { Person, HistoricalEvent } from '@/lib/types';
import { useLocale } from '@/i18n/LocaleProvider';
import { personName, eventTitle, eventSummary } from '@/lib/types';
import { Minus, Plus } from 'lucide-react';

// ==================== Constants ====================

const PERSON_COLORS = [
  '#d97706', '#2563eb', '#059669', '#dc2626',
  '#7c3aed', '#0d9488', '#ea580c', '#ca8a04',
];

const BASE_PX_PER_YEAR = 6;
const ZOOM_STEPS = [0.5, 0.75, 1, 1.5, 2, 3];
const PADDING_TOP = 72;
const PADDING_BOTTOM = 48;
const AXIS_WIDTH = 64;
const MAIN_PANEL_WIDTH = 340;
const COMPARE_COL_WIDTH = 200;
const EVENT_CARD_MIN_HEIGHT = 44;
const MIN_EVENT_GAP = 6;

// ==================== Helpers ====================

/** Format year for display, handling BCE */
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
  const [zoomIndex, setZoomIndex] = useState(2); // index 2 = 1× (100%)
  const zoom = ZOOM_STEPS[zoomIndex];
  const pixelsPerYear = BASE_PX_PER_YEAR * zoom;

  // ---- Compute global year range ----
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
  const comparisonPeople = people.slice(1, 6); // max 5 comparison (6 total including main)

  // ---- Year → Y mapping ----
  function yearToY(year: number): number {
    return PADDING_TOP + (maxYear - year) * pixelsPerYear;
  }

  // ---- Year ticks ----
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

  // ---- Layout events with collision avoidance ----
  const layoutMainEvents = useMemo(() => {
    if (!mainPerson) return [];
    const rawEvents = (allEvents.get(mainPerson.id) ?? [])
      .filter((e) => e.startYear != null)
      .sort((a, b) => (a.startYear ?? 0) - (b.startYear ?? 0));

    interface Placed {
      event: HistoricalEvent;
      y: number;
      lane: number; // 0, 1, 2 for staggering
    }

    const placed: Placed[] = [];
    const lastYPerLane: number[] = [-Infinity, -Infinity, -Infinity];

    for (const event of rawEvents) {
      const baseY = yearToY(event.startYear!);
      // Find the first lane where this event won't overlap
      let bestLane = 0;
      let bestLastY = Infinity;
      for (let lane = 0; lane < 3; lane++) {
        if (baseY - lastYPerLane[lane] >= EVENT_CARD_MIN_HEIGHT + MIN_EVENT_GAP) {
          if (lastYPerLane[lane] < bestLastY) {
            bestLane = lane;
            bestLastY = lastYPerLane[lane];
          }
        }
      }
      // If all lanes are occupied, use the one with the most space
      if (!isFinite(bestLastY)) {
        bestLane = lastYPerLane.indexOf(Math.min(...lastYPerLane));
      }

      placed.push({ event, y: baseY, lane: bestLane });
      lastYPerLane[bestLane] = baseY;
    }

    return placed;
  }, [mainPerson, allEvents, pixelsPerYear, minYear, maxYear]);

  // Layout comparison events (simpler, just dots)
  const layoutCompareEvents = useCallback(
    (person: Person) => {
      const rawEvents = (allEvents.get(person.id) ?? [])
        .filter((e) => e.startYear != null)
        .sort((a, b) => (a.startYear ?? 0) - (b.startYear ?? 0));

      interface Placed {
        event: HistoricalEvent;
        y: number;
      }

      const placed: Placed[] = [];
      let lastY = -Infinity;

      for (const event of rawEvents) {
        const baseY = yearToY(event.startYear!);
        // Simple collision: push down if too close
        const adjustedY = Math.max(baseY, lastY + 20);
        placed.push({ event, y: adjustedY });
        lastY = adjustedY;
      }

      return placed;
    },
    [allEvents, pixelsPerYear, minYear, maxYear],
  );

  // ---- Empty state ----
  if (people.length === 0) {
    return (
      <div className="mt-6 py-16 text-center">
        <p className="text-stone-400 text-sm">{t.compare.noPeople}</p>
        <p className="text-stone-300 text-xs mt-2">{t.compare.noPeopleDesc}</p>
      </div>
    );
  }

  return (
    <div className="mt-4">
      {/* ========== Toolbar: Zoom + Legend ========== */}
      <div className="flex items-center justify-between mb-3 px-1">
        <div className="flex items-center gap-3">
          {mainPerson && (
            <div className="flex items-center gap-1.5">
              <div
                className="w-2.5 h-2.5 rounded-full flex-shrink-0"
                style={{ backgroundColor: PERSON_COLORS[0] }}
              />
              <span className="text-xs font-medium text-stone-600">
                {personName(mainPerson, locale)}
              </span>
              <span className="text-[10px] text-stone-400 bg-stone-100 px-1.5 py-0.5 rounded">
                {t.compare.mainPerson || '主体'}
              </span>
            </div>
          )}
          {comparisonPeople.length > 0 && (
            <span className="text-[10px] text-stone-400">
              vs {comparisonPeople.length} {locale === 'en' ? 'others' : '人对比'}
            </span>
          )}
        </div>

        {/* Zoom control */}
        <div className="flex items-center gap-0.5 bg-stone-100 rounded-lg p-0.5">
          <button
            onClick={() => setZoomIndex(Math.max(0, zoomIndex - 1))}
            disabled={zoomIndex === 0}
            className="p-1.5 rounded-md hover:bg-white disabled:opacity-25 disabled:hover:bg-transparent text-stone-500 transition-colors"
            title={t.compare.zoomOut || '缩小'}
          >
            <Minus size={14} strokeWidth={2} />
          </button>
          <span className="text-xs font-semibold text-stone-600 w-12 text-center tabular-nums select-none">
            {Math.round(zoom * 100)}%
          </span>
          <button
            onClick={() => setZoomIndex(Math.min(ZOOM_STEPS.length - 1, zoomIndex + 1))}
            disabled={zoomIndex === ZOOM_STEPS.length - 1}
            className="p-1.5 rounded-md hover:bg-white disabled:opacity-25 disabled:hover:bg-transparent text-stone-500 transition-colors"
            title={t.compare.zoomIn || '放大'}
          >
            <Plus size={14} strokeWidth={2} />
          </button>
        </div>
      </div>

      {/* ========== Main Comparison Area ========== */}
      <div className="border border-stone-200 rounded-xl bg-white overflow-hidden shadow-sm">
        <div
          className="overflow-y-auto"
          style={{ maxHeight: 'calc(100vh - 260px)' }}
        >
          <div className="flex" style={{ minHeight: totalHeight }}>
            {/* ===== LEFT: Main Person ===== */}
            <div
              className="flex-shrink-0 border-r border-stone-200/60 bg-gradient-to-r from-stone-50/50 to-white"
              style={{ width: MAIN_PANEL_WIDTH }}
            >
              <div className="relative" style={{ height: totalHeight }}>
                {/* Sticky header */}
                <div className="sticky top-0 z-20 bg-white/95 backdrop-blur-sm border-b border-stone-100 px-4 py-3">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <div
                        className="w-2.5 h-2.5 rounded-full flex-shrink-0"
                        style={{
                          backgroundColor: PERSON_COLORS[0],
                          boxShadow: `0 0 0 1px #fff, 0 0 0 3px ${PERSON_COLORS[0]}30`,
                        }}
                      />
                      <span className="text-sm font-semibold text-stone-800 truncate max-w-[200px]">
                        {mainPerson ? personName(mainPerson, locale) : ''}
                      </span>
                    </div>
                    {mainPerson?.birthYear && mainPerson?.deathYear && (
                      <span className="text-[11px] font-mono text-stone-400 tabular-nums">
                        {mainPerson.birthYear}–{mainPerson.deathYear}
                      </span>
                    )}
                  </div>
                </div>

                {/* Lifespan bar */}
                {mainPerson?.birthYear != null && mainPerson?.deathYear != null && (
                  <div
                    className="absolute left-0 w-1 rounded-full z-0 opacity-30"
                    style={{
                      top: yearToY(mainPerson.birthYear!),
                      height: Math.max(
                        (mainPerson.deathYear! - mainPerson.birthYear!) * pixelsPerYear,
                        6,
                      ),
                      backgroundColor: PERSON_COLORS[0],
                    }}
                  />
                )}

                {/* Event Cards */}
                {layoutMainEvents.map(({ event, y, lane }) => {
                  const color = PERSON_COLORS[0];
                  const evtTitle = eventTitle(event, locale);
                  const evtSummary = eventSummary(event, locale);
                  const year = event.startYear;
                  const isBirth = event.tags.includes('出生');
                  const isDeath = event.tags.includes('逝世');

                  // Left offset for lanes: lane 0 at 16px, lane 1 at 96px, lane 2 at 176px
                  const leftOffset = 16 + lane * 100;
                  const cardWidth = Math.min(MAIN_PANEL_WIDTH - leftOffset - 12, 300);

                  return (
                    <div
                      key={event.id}
                      className="absolute group"
                      style={{
                        top: y,
                        left: leftOffset,
                        zIndex: 10,
                      }}
                    >
                      {/* Connector line to axis edge */}
                      <div
                        className="absolute top-1/2 -translate-y-1/2"
                        style={{
                          right: '100%',
                          width: 12,
                          height: 1,
                          backgroundColor: color,
                          opacity: 0.25,
                        }}
                      />

                      {/* Event card */}
                      <div
                        className="bg-white border border-stone-200 rounded-md px-2.5 py-2
                                   hover:border-stone-400 hover:shadow-md transition-all duration-150
                                   cursor-default"
                        style={{
                          width: cardWidth,
                          borderLeftWidth: 3,
                          borderLeftColor: color,
                          minHeight: EVENT_CARD_MIN_HEIGHT,
                        }}
                      >
                        <div className="flex items-start gap-1.5">
                          {/* Dot indicator */}
                          <div
                            className="w-2 h-2 rounded-full mt-0.5 flex-shrink-0"
                            style={{
                              backgroundColor: isBirth || isDeath ? color : 'transparent',
                              border: isBirth || isDeath ? 'none' : `2px solid ${color}`,
                            }}
                          />
                          <div className="min-w-0 flex-1">
                            <div className="text-xs font-medium text-stone-800 leading-tight line-clamp-2">
                              {evtTitle}
                            </div>
                            <div className="flex items-center gap-2 mt-0.5">
                              {year != null && (
                                <span className="text-[10px] font-mono text-stone-400 whitespace-nowrap tabular-nums">
                                  {fmtYear(year)}
                                </span>
                              )}
                              {evtSummary && (
                                <span className="text-[10px] text-stone-400 truncate">
                                  {evtSummary}
                                </span>
                              )}
                            </div>
                          </div>
                        </div>

                        {/* Tooltip on hover */}
                        <div className="absolute left-full ml-2 top-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-30">
                          <div className="bg-stone-800 text-white text-[11px] rounded-md px-3 py-2 shadow-xl max-w-[260px]">
                            <div className="font-medium">{evtTitle}</div>
                            {year != null && (
                              <div className="text-stone-400 mt-0.5">{fmtYear(year)}</div>
                            )}
                            {evtSummary && (
                              <div className="text-stone-300 mt-1 leading-relaxed">{evtSummary}</div>
                            )}
                          </div>
                        </div>
                      </div>
                    </div>
                  );
                })}

                {/* Empty state for main person */}
                {layoutMainEvents.length === 0 && mainPerson && (
                  <div className="absolute inset-0 flex items-center justify-center">
                    <p className="text-xs text-stone-300">{t.compare.empty}</p>
                  </div>
                )}
              </div>
            </div>

            {/* ===== CENTER: Timeline Axis ===== */}
            <div
              className="flex-shrink-0 relative bg-white"
              style={{ width: AXIS_WIDTH }}
            >
              <div className="relative" style={{ height: totalHeight }}>
                {/* Sticky placeholder to align with headers */}
                <div className="sticky top-0 z-20 bg-white/95 backdrop-blur-sm border-b border-stone-100 h-[49px]" />

                {/* Axis vertical line */}
                <div
                  className="absolute left-1/2 top-0 bottom-0"
                  style={{
                    width: 1,
                    backgroundColor: '#d6d3d1',
                    transform: 'translateX(-0.5px)',
                  }}
                />

                {/* Year ticks */}
                {yearTicks.map(({ year, y }, i) => {
                  const isMajor = year % (yearTicks.length > 10 ? yearTicks[1].year - yearTicks[0].year : 10) === 0
                    || Math.abs(year) < 100;
                  return (
                    <div
                      key={year}
                      className="absolute left-0 right-0 flex items-center"
                      style={{ top: y, transform: 'translateY(-0.5px)' }}
                    >
                      {/* Left tick */}
                      <div className="flex-1 flex items-center">
                        <div className="flex-1 h-px bg-stone-100" />
                        <div
                          className="flex-shrink-0"
                          style={{
                            width: isMajor ? 8 : 4,
                            height: 1,
                            backgroundColor: isMajor ? '#a8a29e' : '#d6d3d1',
                          }}
                        />
                      </div>
                      {/* Year label */}
                      <span
                        className={`text-[10px] text-stone-400 px-1 select-none whitespace-nowrap font-mono tabular-nums ${
                          isMajor ? 'font-medium text-stone-500' : ''
                        }`}
                      >
                        {fmtYear(year)}
                      </span>
                      {/* Right tick */}
                      <div className="flex-1 flex items-center">
                        <div
                          className="flex-shrink-0"
                          style={{
                            width: isMajor ? 8 : 4,
                            height: 1,
                            backgroundColor: isMajor ? '#a8a29e' : '#d6d3d1',
                          }}
                        />
                        <div className="flex-1 h-px bg-stone-100" />
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* ===== RIGHT: Comparison People (horizontal scroll) ===== */}
            <div className="flex-1 overflow-x-auto min-w-0">
              <div
                className="flex"
                style={{
                  height: totalHeight,
                  minWidth: Math.max(comparisonPeople.length * COMPARE_COL_WIDTH, 200),
                }}
              >
                {comparisonPeople.length === 0 && (
                  <div className="flex-1 flex items-center justify-center" style={{ height: totalHeight }}>
                    <p className="text-xs text-stone-300">
                      {locale === 'en'
                        ? 'Add comparison people above'
                        : '在上方搜索框中添加对比人物'}
                    </p>
                  </div>
                )}

                {comparisonPeople.map((person, idx) => {
                  const color = PERSON_COLORS[(idx + 1) % PERSON_COLORS.length];
                  const events = layoutCompareEvents(person);
                  const birth = person.birthYear;
                  const death = person.deathYear;

                  return (
                    <div
                      key={person.id}
                      className="flex-shrink-0 border-r border-stone-100 last:border-r-0"
                      style={{ width: COMPARE_COL_WIDTH }}
                    >
                      <div className="relative" style={{ height: totalHeight }}>
                        {/* Sticky header */}
                        <div className="sticky top-0 z-20 bg-white/95 backdrop-blur-sm border-b border-stone-100 px-3 py-3">
                          <div className="flex items-center gap-1.5">
                            <div
                              className="w-2 h-2 rounded-full flex-shrink-0"
                              style={{ backgroundColor: color }}
                            />
                            <span className="text-xs font-medium text-stone-700 truncate flex-1">
                              {personName(person, locale)}
                            </span>
                          </div>
                          {birth != null && death != null && (
                            <span className="text-[10px] font-mono text-stone-400 ml-3.5 tabular-nums">
                              {birth}–{death}
                            </span>
                          )}
                        </div>

                        {/* Lifespan vertical bar */}
                        {birth != null && death != null && (
                          <div
                            className="absolute left-5 w-1 rounded-full z-0 opacity-35"
                            style={{
                              top: yearToY(birth),
                              height: Math.max((death - birth) * pixelsPerYear, 6),
                              backgroundColor: color,
                            }}
                          />
                        )}

                        {/* Horizontal year bands (subtle grid) */}
                        {yearTicks
                          .filter((_, i) => i % 2 === 0)
                          .map(({ year, y }) => (
                            <div
                              key={`band-${year}`}
                              className="absolute left-0 right-0 h-px bg-stone-50 z-0"
                              style={{ top: y }}
                            />
                          ))}

                        {/* Event dots with labels */}
                        {events.map(({ event, y }) => {
                          const shortTitle = eventTitle(event, locale);
                          const isBirth = event.tags.includes('出生');
                          const isDeath = event.tags.includes('逝世');

                          return (
                            <div
                              key={event.id}
                              className="absolute left-3.5 group z-10"
                              style={{ top: y }}
                            >
                              {/* Dot + horizontal bar */}
                              <div className="flex items-center gap-1.5">
                                <div
                                  className="flex-shrink-0 rounded-full transition-transform hover:scale-125"
                                  style={{
                                    width: isBirth || isDeath ? 8 : 6,
                                    height: isBirth || isDeath ? 8 : 6,
                                    backgroundColor: isBirth || isDeath ? color : '#fff',
                                    border: `2px solid ${color}`,
                                  }}
                                  title={`${shortTitle} (${event.startYear})`}
                                />
                                <div
                                  className="h-px flex-shrink-0"
                                  style={{ width: 8, backgroundColor: color, opacity: 0.3 }}
                                />
                                <span className="text-[9px] text-stone-500 leading-tight line-clamp-1 max-w-[130px]">
                                  {shortTitle}
                                </span>
                              </div>

                              {/* Tooltip */}
                              <div className="absolute left-0 bottom-full mb-1 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-30">
                                <div className="bg-stone-800 text-white text-[10px] rounded-md px-2.5 py-1.5 shadow-xl max-w-[200px] whitespace-normal">
                                  <div className="font-medium">{shortTitle}</div>
                                  {event.startYear != null && (
                                    <div className="text-stone-400 mt-0.5">
                                      {fmtYear(event.startYear)}
                                    </div>
                                  )}
                                  {eventSummary(event, locale) && (
                                    <div className="text-stone-300 mt-1 leading-relaxed">
                                      {eventSummary(event, locale)}
                                    </div>
                                  )}
                                </div>
                              </div>
                            </div>
                          );
                        })}

                        {/* Empty state */}
                        {events.length === 0 && (
                          <div className="absolute inset-0 flex items-center justify-center">
                            <p className="text-[10px] text-stone-300">{t.compare.empty}</p>
                          </div>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>
        </div>

        {/* Horizontal scroll hint */}
        {comparisonPeople.length > 2 && (
          <div className="border-t border-stone-100 bg-stone-50/50 px-4 py-1.5">
            <p className="text-[10px] text-stone-400 text-right">
              {locale === 'en'
                ? `← Scroll right to see all ${comparisonPeople.length} people →`
                : `← 向右滚动查看全部 ${comparisonPeople.length} 位对比人物 →`}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
