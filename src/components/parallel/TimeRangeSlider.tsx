'use client';

import { useState, useCallback, useRef, useEffect } from 'react';
import type { HistoricalEvent } from '@/lib/types';

interface TimeRangeSliderProps {
  events: HistoricalEvent[];
  value: [number, number];
  onChange: (range: [number, number]) => void;
  minYear?: number;
  maxYear?: number;
}

function formatYearLabel(year: number): string {
  if (year < 0) {
    return `${Math.abs(year)} BCE`;
  }
  return String(year);
}

function countEventsInRange(events: HistoricalEvent[], min: number, max: number): number {
  return events.filter((e) => {
    if (e.startYear === undefined) return false;
    const end = e.endYear ?? e.startYear;
    return e.startYear <= max && end >= min;
  }).length;
}

export default function TimeRangeSlider({
  events,
  value,
  onChange,
  minYear: propMinYear,
  maxYear: propMaxYear,
}: TimeRangeSliderProps) {
  const [dragging, setDragging] = useState<'min' | 'max' | null>(null);
  const trackRef = useRef<HTMLDivElement>(null);

  const minYear = propMinYear ?? events.reduce((m, e) => {
    const y = e.startYear;
    if (y === undefined) return m;
    const end = e.endYear ?? y;
    return Math.min(m, y, end);
  }, 0);
  const maxYear = propMaxYear ?? events.reduce((m, e) => {
    const y = e.startYear;
    if (y === undefined) return m;
    const end = e.endYear ?? y;
    return Math.max(m, y, end);
  }, 0);

  const range = maxYear - minYear;

  const valueToPercent = useCallback(
    (v: number) => ((v - minYear) / range) * 100,
    [minYear, range],
  );

  const [minVal, maxVal] = value;
  const leftPct = valueToPercent(minVal);
  const rightPct = valueToPercent(maxVal);

  const eventCount = countEventsInRange(events, minVal, maxVal);

  const getValueFromPosition = useCallback(
    (clientX: number): number => {
      const track = trackRef.current;
      if (!track) return 0;
      const rect = track.getBoundingClientRect();
      const pct = Math.max(0, Math.min(1, (clientX - rect.left) / rect.width));
      return Math.round(minYear + pct * range);
    },
    [minYear, range],
  );

  useEffect(() => {
    if (!dragging) return;

    const handleMove = (e: MouseEvent | TouchEvent) => {
      const clientX = 'touches' in e ? e.touches[0].clientX : e.clientX;
      const newVal = getValueFromPosition(clientX);
      const clamped = Math.max(minYear, Math.min(maxYear, newVal));

      if (dragging === 'min') {
        const nextMin = Math.min(clamped, maxVal - 1);
        onChange([nextMin, maxVal]);
      } else {
        const nextMax = Math.max(clamped, minVal + 1);
        onChange([minVal, nextMax]);
      }
    };

    const handleUp = () => setDragging(null);

    window.addEventListener('mousemove', handleMove);
    window.addEventListener('mouseup', handleUp);
    window.addEventListener('touchmove', handleMove);
    window.addEventListener('touchend', handleUp);

    return () => {
      window.removeEventListener('mousemove', handleMove);
      window.removeEventListener('mouseup', handleUp);
      window.removeEventListener('touchmove', handleMove);
      window.removeEventListener('touchend', handleUp);
    };
  }, [dragging, minYear, maxYear, minVal, maxVal, getValueFromPosition, onChange]);

  return (
    <div className="w-full">
      <div className="flex items-center justify-between mb-2">
        <div className="text-xs font-medium text-stone-700">
          <span className="font-mono">{formatYearLabel(minVal)}</span>
          <span className="mx-2 text-stone-400">–</span>
          <span className="font-mono">{formatYearLabel(maxVal)}</span>
        </div>
        <span className="text-[10px] text-stone-400">
          {eventCount} event{eventCount !== 1 ? 's' : ''} in range
        </span>
      </div>

      <div
        ref={trackRef}
        className="relative w-full h-8 flex items-center cursor-pointer select-none"
        onMouseDown={(e) => {
          if ((e.target as HTMLElement).classList.contains('slider-handle')) return;
          const clickedVal = getValueFromPosition(e.clientX);
          const distToMin = Math.abs(clickedVal - minVal);
          const distToMax = Math.abs(clickedVal - maxVal);
          setDragging(distToMin <= distToMax ? 'min' : 'max');
        }}
      >
        {/* Track background */}
        <div className="absolute inset-x-0 h-1.5 rounded-full bg-stone-200" />

        {/* Active range */}
        <div
          className="absolute h-1.5 rounded-full bg-stone-700"
          style={{
            left: `${leftPct}%`,
            width: `${rightPct - leftPct}%`,
          }}
        />

        {/* Min handle */}
        <div
          className="slider-handle absolute w-4 h-4 rounded-full bg-white border-2 border-stone-700 shadow-sm transition-shadow hover:shadow-md cursor-grab active:cursor-grabbing"
          style={{ left: `calc(${leftPct}% - 8px)` }}
          onMouseDown={(e) => {
            e.preventDefault();
            setDragging('min');
          }}
          onTouchStart={(e) => {
            e.preventDefault();
            setDragging('min');
          }}
        />

        {/* Max handle */}
        <div
          className="slider-handle absolute w-4 h-4 rounded-full bg-white border-2 border-stone-700 shadow-sm transition-shadow hover:shadow-md cursor-grab active:cursor-grabbing"
          style={{ left: `calc(${rightPct}% - 8px)` }}
          onMouseDown={(e) => {
            e.preventDefault();
            setDragging('max');
          }}
          onTouchStart={(e) => {
            e.preventDefault();
            setDragging('max');
          }}
        />

        {/* Min year label */}
        <div
          className="absolute -top-1 text-[10px] text-stone-400 font-mono pointer-events-none"
          style={{ left: `calc(${leftPct}% - 16px)` }}
        >
          {formatYearLabel(minVal)}
        </div>

        {/* Max year label */}
        <div
          className="absolute -top-1 text-[10px] text-stone-400 font-mono pointer-events-none"
          style={{ left: `calc(${rightPct}% - 16px)` }}
        >
          {formatYearLabel(maxVal)}
        </div>

        {/* Range endpoints */}
        <div className="absolute -bottom-4 left-0 text-[9px] text-stone-300 font-mono pointer-events-none">
          {formatYearLabel(minYear)}
        </div>
        <div className="absolute -bottom-4 right-0 text-[9px] text-stone-300 font-mono pointer-events-none">
          {formatYearLabel(maxYear)}
        </div>
      </div>
    </div>
  );
}
