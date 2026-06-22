'use client';

import { useState, useMemo, useRef, useEffect } from 'react';
import type { HistoricalEvent, Region } from '@/lib/types';
import { formatYearRange } from '@/lib/date';
import { useLocale } from '@/i18n/LocaleProvider';
import { eventTitle, eventSummary } from '@/lib/types';
import { Minus, Plus } from 'lucide-react';

// ==================== Constants ====================

const DECADE_PX = 60; // pixels per 10-year block
const PADDING_TOP = 80;
const PADDING_BOTTOM = 60;
const AXIS_X = 120; // timeline axis X position (left side, after year labels)
const CARD_WIDTH = 380; // event card width
const CARD_GAP = 12; // min vertical gap between cards
const CARD_EST_HEIGHT = 120; // estimated card height for overlap calc
const OVERLAP_SHIFT = 50; // px to shift card right when overlapping
const AXIS_GAP = 20; // gap between axis and cards

// ==================== Helpers ====================

function fmtYear(y: number): string {
  if (y < 0) return `前${Math.abs(y)}`;
  return String(y);
}

interface LayoutItem {
  event: HistoricalEvent;
  /** Y position on timeline */
  dotY: number;
  /** Duration bar height (0 = point event) */
  barHeight: number;
  /** Rightward shift for overlap avoidance */
  shiftRight: number;
}

// ==================== Component ====================

interface TimelineProps {
  events: HistoricalEvent[];
  eventRegions?: Map<string, Region | undefined>;
}

export default function Timeline({ events, eventRegions }: TimelineProps) {
  const { locale, toScript } = useLocale();
  const [hoveredId, setHoveredId] = useState<string | null>(null);
  const [zoom, setZoom] = useState(1);
  const scrollRef = useRef<HTMLDivElement>(null);
  const [containerRect, setContainerRect] = useState<DOMRect | null>(null);

  const zoomLevels = [0.5, 0.75, 1, 1.5, 2, 3];
  const pxPerDecade = DECADE_PX * zoom;

  // Year range
  const { minYear, maxYear } = useMemo(() => {
    if (events.length === 0) return { minYear: 0, maxYear: 100 };
    let min = Infinity, max = -Infinity;
    for (const e of events) {
      if (e.startYear != null && e.startYear < min) min = e.startYear;
      if (e.endYear != null && e.endYear > max) max = e.endYear;
      if (e.startYear != null && e.startYear > max) max = e.startYear;
    }
    if (!isFinite(min)) min = 0;
    if (!isFinite(max)) max = 100;
    return {
      minYear: Math.floor(min / 10) * 10 - 5,
      maxYear: Math.ceil(max / 10) * 10 + 5,
    };
  }, [events]);

  function yearToY(year: number): number {
    return PADDING_TOP + (year - minYear) / 10 * pxPerDecade;
  }

  const totalSpan = maxYear - minYear;
  const totalHeight = totalSpan / 10 * pxPerDecade + PADDING_TOP + PADDING_BOTTOM;

  // Sort events
  const sorted = useMemo(
    () => [...events].sort((a, b) => (a.startYear ?? 0) - (b.startYear ?? 0)),
    [events]
  );

  // Decade ticks
  const decadeTicks = useMemo(() => {
    const ticks: { year: number; y: number }[] = [];
    const start = Math.floor(minYear / 10) * 10;
    for (let y = start; y <= maxYear; y += 10) {
      ticks.push({ year: y, y: yearToY(y) });
    }
    return ticks;
  }, [minYear, maxYear, pxPerDecade]);

  // Layout with overlap avoidance
  // Strategy: stack cards vertically when they overlap in time,
  // using horizontal offset (shiftRight) to stagger them side-by-side.
  const layout = useMemo((): LayoutItem[] => {
    const items: LayoutItem[] = [];

    for (const event of sorted) {
      const startY = yearToY(event.startYear ?? 0);
      const endY = event.endYear != null && event.endYear !== event.startYear
        ? yearToY(event.endYear) : startY;
      const barHeight = Math.max(endY - startY, 0);
      const rawDotY = startY;
      const isDuration = barHeight > 4;

      // Card vertical span (centered on dotY for point events)
      const naturalCardTop = isDuration ? rawDotY : rawDotY - CARD_EST_HEIGHT / 2;
      const naturalCardBottom = naturalCardTop + CARD_EST_HEIGHT;

      // Check ALL previous items (not just same-layer) for vertical overlap
      let pushedDotY = rawDotY;
      let layer = 0;

      for (const prev of items) {
        const prevIsDuration = prev.barHeight > 4;
        const prevCardTop = prevIsDuration ? prev.dotY : prev.dotY - CARD_EST_HEIGHT / 2;
        const prevCardBottom = prevCardTop + CARD_EST_HEIGHT;

        // Check if natural position of this card overlaps with previous card
        const thisTop = isDuration ? pushedDotY : pushedDotY - CARD_EST_HEIGHT / 2;
        const thisBottom = thisTop + CARD_EST_HEIGHT;

        if (thisTop < prevCardBottom + CARD_GAP && thisBottom > prevCardTop - CARD_GAP) {
          // Overlap detected: push this card down past the previous card
          const newDotY = prevCardBottom + CARD_GAP + (isDuration ? 0 : CARD_EST_HEIGHT / 2);
          pushedDotY = Math.max(pushedDotY, newDotY);
          // Alternate horizontal layer
          layer = (layer + 1) % 4;
        }
      }

      items.push({
        event,
        dotY: pushedDotY,
        barHeight: isDuration ? (barHeight + (pushedDotY - rawDotY)) : 0,
        shiftRight: layer * OVERLAP_SHIFT,
      });
    }

    return items;
  }, [sorted, pxPerDecade, minYear]);

  // Scroll to first event
  useEffect(() => {
    if (events.length === 0 || !scrollRef.current) return;
    const y = yearToY(events[0].startYear ?? 0);
    scrollRef.current.scrollTop = y - 200;
  }, []);

  // Track scroll container position for fixed-positioned zoom controls
  useEffect(() => {
    const el = scrollRef.current;
    if (!el) return;
    const update = () => setContainerRect(el.getBoundingClientRect());
    update();
    const ro = new ResizeObserver(update);
    ro.observe(el);
    // Also update on scroll (for any layout shift)
    el.addEventListener('scroll', update, { passive: true });
    return () => {
      ro.disconnect();
      el.removeEventListener('scroll', update);
    };
  }, []);

  if (events.length === 0) {
    return <p className="text-sm text-stone-400 py-8 text-center">暂无时间线数据</p>;
  }

  const maxShift = Math.max(...layout.map(l => l.shiftRight), 0);
  // Total width: axis + max cards shifted right + card width + some padding
  const totalWidth = AXIS_X + AXIS_GAP + CARD_WIDTH + maxShift + 40;

  return (
    <div
      ref={scrollRef}
      className="overflow-auto relative"
      style={{ maxHeight: 'calc(100vh - 160px)' }}
    >
      <div className="relative" style={{ height: totalHeight, minWidth: totalWidth }}>

        {/* ===== Zoom controls — fixed to scroll container's top-right corner ===== */}
        {containerRect && (
          <div
            className="z-30 pointer-events-none"
            style={{
              position: 'fixed',
              top: containerRect.top + 12,
              left: containerRect.right - 90,
            }}
          >
            <div className="flex items-center gap-0.5 bg-white/95 backdrop-blur-sm border border-stone-200 rounded-lg p-0.5 shadow-sm pointer-events-auto">
              <button
                onClick={() => setZoom(Math.max(zoomLevels[0], zoomLevels[zoomLevels.indexOf(zoom) - 1] || zoom))}
                disabled={zoom <= zoomLevels[0]}
                className="p-1 rounded-md hover:bg-stone-100 disabled:opacity-25 text-stone-500"
              ><Minus size={14} /></button>
              <span className="text-xs font-semibold text-stone-600 w-12 text-center tabular-nums">{Math.round(zoom * 100)}%</span>
              <button
                onClick={() => setZoom(Math.min(zoomLevels[zoomLevels.length - 1], zoomLevels[zoomLevels.indexOf(zoom) + 1] || zoom))}
                disabled={zoom >= zoomLevels[zoomLevels.length - 1]}
                className="p-1 rounded-md hover:bg-stone-100 disabled:opacity-25 text-stone-500"
              ><Plus size={14} /></button>
            </div>
          </div>
        )}

          {/* ===== Decade grid lines (full width) ===== */}
          {decadeTicks.map(({ year, y }) => (
            <div key={year} className="absolute left-0 right-0" style={{ top: y }}>
              <div
                className="absolute left-0 right-0 h-px"
                style={{ backgroundColor: year % 50 === 0 ? '#d6d3d1' : '#e7e5e4', opacity: year % 50 === 0 ? 0.6 : 0.3 }}
              />
            </div>
          ))}

          {/* ===== Timeline axis (vertical line) ===== */}
          <div
            className="absolute top-0 bottom-0"
            style={{ left: AXIS_X, width: 2, backgroundColor: '#c4b5a5' }}
          />

          {/* ===== Year labels (LEFT of axis) + tick marks ON axis ===== */}
          {decadeTicks.map(({ year, y }) => (
            <div key={year} className="absolute" style={{ left: 0, top: y, width: '100%' }}>
              {/* Year label — left of axis */}
              <div
                className="absolute text-xs font-mono select-none whitespace-nowrap text-right"
                style={{
                  right: `calc(100% - ${AXIS_X - 8}px)`,
                  top: -8,
                  color: year % 50 === 0 ? '#57534e' : '#a8a29e',
                  fontWeight: year % 50 === 0 ? 600 : 400,
                }}
              >
                {fmtYear(year)}
              </div>
              {/* Tick mark — ON the axis line */}
              <div
                className="absolute rounded-full"
                style={{
                  left: AXIS_X,
                  top: -2.5,
                  width: year % 50 === 0 ? 8 : 5,
                  height: year % 50 === 0 ? 8 : 5,
                  backgroundColor: '#78716c',
                  transform: 'translate(-50%, -50%)',
                }}
              />
            </div>
          ))}

          {/* ===== Event items ===== */}
          {layout.map((item) => {
            const { event, dotY, barHeight, shiftRight } = item;
            const isDuration = barHeight > 4;
            const isHovered = hoveredId === event.id;

            // Card position: to the RIGHT of axis
            const cardLeft = AXIS_X + AXIS_GAP + shiftRight;

            // Connector line: from axis to card left edge
            const connectorWidth = AXIS_GAP + shiftRight;

            return (
              <div
                key={event.id}
                className={`absolute ${isHovered ? 'z-20' : 'z-10'}`}
                style={{
                  left: 0,
                  top: dotY,
                  width: '100%',
                  height: Math.max(barHeight, 10),
                  minHeight: 10,
                }}
                onMouseEnter={() => setHoveredId(event.id)}
                onMouseLeave={() => setHoveredId(null)}
              >
                {/* ===== Axis marker (ON the axis line) ===== */}
                {isDuration ? (
                  // Duration bar — vertical orange bar ON the axis
                  <div
                    className="absolute rounded-sm transition-all duration-300"
                    style={{
                      left: AXIS_X - 2,
                      top: 0,
                      width: 4,
                      height: barHeight,
                      backgroundColor: isHovered ? '#f59e0b' : '#d97706',
                      opacity: isHovered ? 1 : 0.75,
                    }}
                  />
                ) : (
                  // Single point — orange dot ON the axis
                  <div
                    className="absolute rounded-full transition-all duration-300"
                    style={{
                      left: AXIS_X - 5,
                      top: -5,
                      width: isHovered ? 12 : 10,
                      height: isHovered ? 12 : 10,
                      backgroundColor: isHovered ? '#f59e0b' : '#d97706',
                      boxShadow: isHovered ? '0 0 8px rgba(245,158,11,0.4)' : 'none',
                    }}
                  />
                )}

                {/* ===== Connector line from axis to card ===== */}
                <div
                  className="absolute h-px transition-all duration-300"
                  style={{
                    left: AXIS_X,
                    top: isDuration ? 2 : 0,
                    width: connectorWidth,
                    backgroundColor: isHovered ? '#f59e0b' : '#d4a574',
                    opacity: isHovered ? 1 : 0.6,
                  }}
                />

                {/* ===== Event card (right of axis) ===== */}
                <div
                  className="absolute p-3 rounded-lg border transition-all duration-300 bg-white"
                  style={{
                    left: cardLeft,
                    top: isDuration ? 0 : -CARD_EST_HEIGHT / 2 + 5,
                    width: CARD_WIDTH,
                    borderColor: isHovered ? '#f59e0b' : '#e7e5e4',
                    borderLeftWidth: 3,
                    borderLeftColor: '#d97706',
                    boxShadow: isHovered ? '0 4px 16px rgba(0,0,0,0.1)' : '0 1px 3px rgba(0,0,0,0.04)',
                  }}
                >
                  {/* Year */}
                  <div className="flex items-center gap-2 mb-1">
                    <span className="text-xs font-semibold text-stone-500 tabular-nums">
                      {formatYearRange(event.startYear, event.endYear)}
                    </span>
                    {event.importance >= 4 && (
                      <span className="text-[10px] text-amber-500">
                        {'★'.repeat(Math.min(event.importance - 3, 2))}
                      </span>
                    )}
                  </div>

                  {/* Title */}
                  <h4 className="text-sm font-semibold text-stone-800 leading-snug">
                    {toScript(eventTitle(event, locale))}
                  </h4>

                  {/* Summary */}
                  {event.summary && (
                    <p className="mt-1 text-xs text-stone-600 leading-relaxed line-clamp-2">
                      {toScript(eventSummary(event, locale))}
                    </p>
                  )}
                </div>
              </div>
            );
          })}

        <div style={{ height: PADDING_BOTTOM }} />
      </div>
    </div>
  );
}
