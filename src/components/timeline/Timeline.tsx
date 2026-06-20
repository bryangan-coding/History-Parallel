'use client';

import { useState, useMemo, useRef, useEffect } from 'react';
import type { HistoricalEvent, Region } from '@/lib/types';
import TimelineItem from './TimelineItem';
import { Minus, Plus } from 'lucide-react';

// ==================== Constants ====================
const DECADE_PX = 60; // pixels per 10-year block
const PADDING_TOP = 80; // space for header / zoom controls
const PADDING_BOTTOM = 60;
const AXIS_X = 20; // x position of the timeline axis
const CARD_MIN_GAP = 12; // minimum vertical gap between cards
const CARD_HEIGHT = 110; // estimated card height for overlap calculation
const CARD_OFFSET_STEP = 30; // px to shift right per overlapping card

// ==================== Helpers ====================

function fmtYear(y: number): string {
  if (y < 0) return `前${Math.abs(y)}`;
  return String(y);
}

interface LayoutItem {
  event: HistoricalEvent;
  /** Y position of the marker on the axis (top of duration bar for ranges) */
  dotY: number;
  /** Height of the duration bar (0 for point events) */
  barHeight: number;
  /** Horizontal offset for the card (px right from connector baseline) */
  cardOffset: number;
}

// ==================== Component ====================

interface TimelineProps {
  events: HistoricalEvent[];
  eventRegions?: Map<string, Region | undefined>;
}

export default function Timeline({ events, eventRegions }: TimelineProps) {
  const [hoveredBadgeId, setHoveredBadgeId] = useState<string | null>(null);
  const [zoom, setZoom] = useState(1); // 1 = 100%
  const scrollRef = useRef<HTMLDivElement>(null);
  const [containerWidth, setContainerWidth] = useState(800);

  // Measure container width
  useEffect(() => {
    const el = scrollRef.current?.parentElement;
    if (!el) return;
    const ro = new ResizeObserver((entries) => {
      for (const entry of entries) {
        setContainerWidth(entry.contentRect.width);
      }
    });
    ro.observe(el);
    return () => ro.disconnect();
  }, []);

  const zoomLevels = [0.5, 0.75, 1, 1.5, 2, 3];
  const pxPerDecade = DECADE_PX * zoom;

  // Compute year range
  const { minYear, maxYear, totalYears } = useMemo(() => {
    if (events.length === 0) return { minYear: 0, maxYear: 100, totalYears: 100 };
    let min = Infinity;
    let max = -Infinity;
    for (const e of events) {
      if (e.startYear != null && e.startYear < min) min = e.startYear;
      if (e.endYear != null && e.endYear > max) max = e.endYear;
      if (e.startYear != null && e.startYear > max) max = e.startYear;
    }
    if (!isFinite(min)) min = 0;
    if (!isFinite(max)) max = 100;
    // Round to nearest decade
    const pad = 5;
    return {
      minYear: Math.floor(min / 10) * 10 - pad,
      maxYear: Math.ceil(max / 10) * 10 + pad,
      totalYears: max - min + pad * 2,
    };
  }, [events]);

  // Generate decade ticks
  const decadeTicks = useMemo(() => {
    const ticks: { year: number; y: number; isMajor: boolean }[] = [];
    const startDecade = Math.floor(minYear / 10) * 10;
    for (let y = startDecade; y <= maxYear; y += 10) {
      ticks.push({
        year: y,
        y: yearToY(y),
        isMajor: y % 100 === 0 || y % 50 === 0,
      });
    }
    return ticks;
  }, [minYear, maxYear, pxPerDecade]);

  // Convert year to Y position on the timeline
  function yearToY(year: number): number {
    return PADDING_TOP + (year - minYear) / 10 * pxPerDecade;
  }

  // Sort events
  const sorted = useMemo(
    () => [...events].sort((a, b) => (a.startYear ?? 0) - (b.startYear ?? 0)),
    [events]
  );

  // Compute layout with overlap avoidance
  const layout = useMemo((): LayoutItem[] => {
    const items: LayoutItem[] = [];
    
    for (const event of sorted) {
      const startY = yearToY(event.startYear ?? 0);
      const endY = event.endYear != null && event.endYear !== event.startYear
        ? yearToY(event.endYear)
        : startY;
      const barHeight = Math.max(endY - startY, 0);
      const dotY = startY;

      // Card top Y position (centered on dot for point events, top-aligned for durations)
      const thisCardTop = barHeight > 4 ? dotY : dotY - CARD_HEIGHT / 2;
      const thisCardBottom = thisCardTop + CARD_HEIGHT;

      // Find a layer where this card doesn't overlap with any existing card
      let layer = 0;
      let foundLayer = false;
      const maxLayers = 10;

      while (!foundLayer && layer < maxLayers) {
        let overlaps = false;
        for (const prev of items) {
          if (prev.cardOffset !== layer * CARD_OFFSET_STEP) continue;
          
          const prevCardTop = prev.barHeight > 4 ? prev.dotY : prev.dotY - CARD_HEIGHT / 2;
          const prevCardBottom = prevCardTop + CARD_HEIGHT;

          if (thisCardTop < prevCardBottom + CARD_MIN_GAP &&
              thisCardBottom > prevCardTop - CARD_MIN_GAP) {
            overlaps = true;
            break;
          }
        }
        
        if (!overlaps) {
          foundLayer = true;
        } else {
          layer++;
        }
      }

      items.push({
        event,
        dotY,
        barHeight,
        cardOffset: layer * CARD_OFFSET_STEP,
      });
    }

    return items;
  }, [sorted, pxPerDecade, minYear]);

  const totalHeight = totalYears / 10 * pxPerDecade + PADDING_TOP + PADDING_BOTTOM;

  // Scroll to first event on mount
  useEffect(() => {
    if (events.length === 0 || !scrollRef.current) return;
    const first = events[0];
    const y = yearToY(first.startYear ?? 0);
    scrollRef.current.scrollTop = y - 200;
  }, []);

  if (events.length === 0) {
    return (
      <p className="text-sm text-stone-400 py-8 text-center">
        暂无时间线数据
      </p>
    );
  }

  const maxCardOffset = Math.max(...layout.map(l => l.cardOffset), 0);
  const totalWidth = AXIS_X + 60 + 320 + maxCardOffset + 40; // axis + connector + card + padding

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
          >
            <Minus size={14} />
          </button>
          <span className="text-xs font-semibold text-stone-600 w-12 text-center tabular-nums">
            {Math.round(zoom * 100)}%
          </span>
          <button
            onClick={() => setZoom(Math.min(zoomLevels[zoomLevels.length - 1], zoomLevels[zoomLevels.indexOf(zoom) + 1] || zoom))}
            disabled={zoom >= zoomLevels[zoomLevels.length - 1]}
            className="p-1 rounded-md hover:bg-white disabled:opacity-25 text-stone-500"
          >
            <Plus size={14} />
          </button>
        </div>
      </div>

      {/* Scrollable timeline */}
      <div
        ref={scrollRef}
        className="overflow-y-auto overflow-x-auto"
        style={{ maxHeight: 'calc(100vh - 160px)' }}
      >
        <div className="relative" style={{ height: totalHeight, minWidth: totalWidth }}>
          {/* ===== Decade grid lines ===== */}
          {decadeTicks.map(({ year, y, isMajor }) => (
            <div key={year} className="absolute left-0 right-0" style={{ top: y }}>
              {/* Horizontal grid line */}
              <div
                className="absolute left-0 right-0 h-px"
                style={{
                  backgroundColor: isMajor ? '#d6d3d1' : '#e7e5e4',
                  opacity: isMajor ? 0.8 : 0.5,
                }}
              />
              {/* Year label on axis */}
              <div
                className="absolute text-xs font-mono text-stone-400 select-none"
                style={{
                  left: AXIS_X - 4,
                  transform: 'translate(-100%, -50%)',
                  fontWeight: isMajor ? 600 : 400,
                  color: isMajor ? '#78716c' : '#a8a29e',
                }}
              >
                {fmtYear(year)}
              </div>
            </div>
          ))}

          {/* ===== Timeline axis (vertical line) ===== */}
          <div
            className="absolute top-0 bottom-0"
            style={{
              left: AXIS_X,
              width: 1,
              backgroundColor: '#d6d3d1',
            }}
          />

          {/* ===== Event items ===== */}
          {layout.map((item, index) => (
            <TimelineItem
              key={item.event.id}
              event={item.event}
              dotY={item.dotY}
              barHeight={item.barHeight}
              cardOffset={item.cardOffset}
              isLast={index === layout.length - 1}
              region={eventRegions?.get(item.event.id)}
              isHovered={hoveredBadgeId === item.event.id}
              onHover={(hovered) => setHoveredBadgeId(hovered ? item.event.id : null)}
            />
          ))}

          {/* ===== Bottom spacer to prevent last card cutoff ===== */}
          <div style={{ height: PADDING_BOTTOM }} />
        </div>
      </div>
    </div>
  );
}
