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
const AXIS_X = 480; // timeline axis X position (center-right area)
const CARD_WIDTH = 380; // event card width
const CARD_GAP = 16; // min vertical gap between cards
const CARD_EST_HEIGHT = 100; // estimated card height for overlap calc
const OVERLAP_SHIFT = 40; // px to shift card left when overlapping

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
  /** Leftward shift for overlap avoidance */
  shiftLeft: number;
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

  // Layout with overlap avoidance (cards to LEFT of axis)
  const layout = useMemo((): LayoutItem[] => {
    const items: LayoutItem[] = [];

    for (const event of sorted) {
      const startY = yearToY(event.startYear ?? 0);
      const endY = event.endYear != null && event.endYear !== event.startYear
        ? yearToY(event.endYear) : startY;
      const barHeight = Math.max(endY - startY, 0);
      const dotY = startY;
      const isDuration = barHeight > 4;

      // Card vertical span
      const cardTop = isDuration ? dotY : dotY - CARD_EST_HEIGHT / 2;
      const cardBottom = cardTop + CARD_EST_HEIGHT;

      // Find a non-overlapping layer
      let layer = 0;
      let found = false;
      const maxLayers = 10;

      while (!found && layer < maxLayers) {
        let overlaps = false;
        const thisLeft = AXIS_X - 12 - CARD_WIDTH - layer * OVERLAP_SHIFT;
        for (const prev of items) {
          if (prev.shiftLeft !== layer * OVERLAP_SHIFT) continue;
          const prevCardTop = prev.barHeight > 4 ? prev.dotY : prev.dotY - CARD_EST_HEIGHT / 2;
          const prevCardBottom = prevCardTop + CARD_EST_HEIGHT;
          if (cardTop < prevCardBottom + CARD_GAP && cardBottom > prevCardTop - CARD_GAP) {
            overlaps = true;
            break;
          }
        }
        if (!overlaps) found = true;
        else layer++;
      }

      items.push({ event, dotY, barHeight, shiftLeft: layer * OVERLAP_SHIFT });
    }

    return items;
  }, [sorted, pxPerDecade, minYear]);

  // Scroll to first event
  useEffect(() => {
    if (events.length === 0 || !scrollRef.current) return;
    const y = yearToY(events[0].startYear ?? 0);
    scrollRef.current.scrollTop = y - 200;
  }, []);

  if (events.length === 0) {
    return <p className="text-sm text-stone-400 py-8 text-center">暂无时间线数据</p>;
  }

  const maxShift = Math.max(...layout.map(l => l.shiftLeft), 0);
  const totalWidth = AXIS_X + 100;

  return (
    <div className="relative">
      {/* Zoom controls */}
      <div className="sticky top-0 z-30 bg-white/95 backdrop-blur-sm border-b border-stone-100 mb-4 flex items-center justify-between px-2 py-2">
        <span className="text-xs text-stone-400">
          {events.length} 个事件 · {fmtYear(minYear)} – {fmtYear(maxYear)}
        </span>
        <div className="flex items-center gap-0.5 bg-stone-100 rounded-lg p-0.5">
          <button
            onClick={() => setZoom(Math.max(zoomLevels[0], zoomLevels[zoomLevels.indexOf(zoom) - 1] || zoom))}
            disabled={zoom <= zoomLevels[0]}
            className="p-1 rounded-md hover:bg-white disabled:opacity-25 text-stone-500"
          ><Minus size={14} /></button>
          <span className="text-xs font-semibold text-stone-600 w-12 text-center tabular-nums">{Math.round(zoom * 100)}%</span>
          <button
            onClick={() => setZoom(Math.min(zoomLevels[zoomLevels.length - 1], zoomLevels[zoomLevels.indexOf(zoom) + 1] || zoom))}
            disabled={zoom >= zoomLevels[zoomLevels.length - 1]}
            className="p-1 rounded-md hover:bg-white disabled:opacity-25 text-stone-500"
          ><Plus size={14} /></button>
        </div>
      </div>

      {/* Scrollable */}
      <div
        ref={scrollRef}
        className="overflow-auto"
        style={{ maxHeight: 'calc(100vh - 160px)' }}
      >
        <div className="relative" style={{ height: totalHeight, minWidth: totalWidth }}>

          {/* ===== Decade grid lines (full width) ===== */}
          {decadeTicks.map(({ year, y }) => (
            <div key={year} className="absolute left-0 right-0" style={{ top: y }}>
              {/* Grid line */}
              <div
                className="absolute left-0 right-0 h-px"
                style={{ backgroundColor: year % 50 === 0 ? '#d6d3d1' : '#e7e5e4', opacity: year % 50 === 0 ? 0.6 : 0.3 }}
              />
            </div>
          ))}

          {/* ===== Timeline axis (vertical) ===== */}
          <div
            className="absolute top-0 bottom-0"
            style={{ left: AXIS_X, width: 1, backgroundColor: '#c4b5a5' }}
          />

          {/* ===== Year labels + tick marks on the RIGHT of axis ===== */}
          {decadeTicks.map(({ year, y }) => (
            <div key={year} className="absolute" style={{ left: AXIS_X, top: y }}>
              {/* Tick mark */}
              <div
                className="absolute rounded-full"
                style={{
                  left: 6,
                  top: -2.5,
                  width: year % 50 === 0 ? 8 : 5,
                  height: year % 50 === 0 ? 8 : 5,
                  backgroundColor: '#78716c',
                  transform: 'translate(-50%, -50%)',
                }}
              />
              {/* Year label */}
              <div
                className="absolute text-xs font-mono select-none whitespace-nowrap"
                style={{
                  left: 16,
                  top: -8,
                  color: year % 50 === 0 ? '#57534e' : '#a8a29e',
                  fontWeight: year % 50 === 0 ? 600 : 400,
                }}
              >
                {fmtYear(year)}
              </div>
            </div>
          ))}

          {/* ===== Event items ===== */}
          {layout.map((item) => {
            const { event, dotY, barHeight, shiftLeft } = item;
            const isDuration = barHeight > 4;
            const isHovered = hoveredId === event.id;

            // Card position: to the LEFT of axis
            const cardRight = AXIS_X - 12 - shiftLeft; // card right edge, with gap to axis
            const cardLeft = cardRight - CARD_WIDTH;

            // Connector line from axis to card right edge
            const connectorX1 = AXIS_X;
            const connectorX2 = cardRight;

            return (
              <div
                key={event.id}
                className={`absolute ${isHovered ? 'z-20' : 'z-10'}`}
                style={{
                  left: 0,
                  top: dotY,
                  height: Math.max(barHeight, 10),
                  minHeight: 10,
                }}
                onMouseEnter={() => setHoveredId(event.id)}
                onMouseLeave={() => setHoveredId(null)}
              >
                {/* ===== Axis marker ===== */}
                {isDuration ? (
                  <div
                    className="absolute rounded-full transition-all duration-300"
                    style={{
                      left: AXIS_X - 2,
                      top: 0,
                      width: 4,
                      height: barHeight,
                      backgroundColor: isHovered ? '#f59e0b' : '#d97706',
                      opacity: isHovered ? 1 : 0.7,
                    }}
                  />
                ) : (
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

                {/* ===== Connector line ===== */}
                <div
                  className="absolute h-px transition-all duration-300"
                  style={{
                    left: connectorX2,
                    top: isDuration ? 2 : 0,
                    width: connectorX1 - connectorX2,
                    backgroundColor: isHovered ? '#f59e0b' : '#d4a574',
                    opacity: isHovered ? 1 : 0.6,
                  }}
                />

                {/* ===== Event card (left of axis) ===== */}
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
    </div>
  );
}
