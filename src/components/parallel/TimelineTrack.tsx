'use client';

import { memo } from 'react';
import type { ScoredEvent } from '@/lib/types';
import { eventTitle, eventPlaceName } from '@/lib/types';
import { formatYearRange } from '@/lib/date';
import type { Locale } from '@/lib/types';

interface Props {
  trackIndex: number;
  regionName: string;
  events: ScoredEvent[];
  minYear: number;
  totalSpan: number;
  centerYear: number;
  trackHeight: number;
  nodeSize: (imp: number) => number;
  nodeColor: (imp: number) => string;
  hoveredId: string | null;
  selectedEventId: string | null;
  onHover: (id: string | null) => void;
  onClick: (scored: ScoredEvent, regionName: string) => void;
  locale: Locale;
}

const TimelineTrack = memo(function TimelineTrack({
  trackIndex: _trackIndex,
  regionName,
  events,
  minYear,
  totalSpan,
  trackHeight,
  nodeSize,
  nodeColor,
  centerYear,
  hoveredId,
  selectedEventId,
  onHover,
  onClick,
  locale,
}: Props) {
  const getXPercent = (year: number) => {
    return ((year - minYear) / totalSpan) * 100;
  };

  return (
    <div
      className="relative border-b border-stone-100 last:border-b-0"
      style={{ height: trackHeight }}
    >
      {/* Region label */}
      <div
        className="absolute left-0 top-0 z-20 bg-white/90 backdrop-blur px-2 py-1 text-[10px] font-semibold text-stone-500 uppercase tracking-wide"
        style={{ height: trackHeight, display: 'flex', alignItems: 'center' }}
      >
        {regionName}
      </div>

      {/* Center dashed line */}
      <div
        className="absolute top-0 bottom-0 border-l border-dashed border-stone-200"
        style={{ left: `${getXPercent(centerYear)}%` }}
      />

      {/* Event nodes */}
      {events.map((scored) => {
        const evt = scored.event;
        const x = getXPercent(evt.startYear);
        const size = nodeSize(evt.importance);
        const color = nodeColor(evt.importance);
        const isHovered = hoveredId === evt.id;
        const isSelected = selectedEventId === evt.id;

        return (
          <div
            key={evt.id}
            className="absolute"
            style={{
              left: `${x}%`,
              top: '50%',
              transform: 'translate(-50%, -50%)',
              zIndex: isHovered || isSelected ? 30 : 10,
            }}
          >
            {/* Tooltip */}
            {isHovered && (
              <div
                className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 z-40"
                style={{ width: 180 }}
              >
                <div className="bg-stone-800 text-white text-[11px] rounded-md px-3 py-2 shadow-lg">
                  <p className="font-semibold leading-tight">
                    {eventTitle(evt, locale)}
                  </p>
                  <p className="text-stone-300 mt-0.5">
                    {formatYearRange(evt.startYear, evt.endYear)}
                    {eventPlaceName(evt, locale) && ` · ${eventPlaceName(evt, locale)}`}
                  </p>
                  <p className="text-stone-400 mt-0.5">{regionName}</p>
                </div>
                <div className="w-0 h-0 border-l-[5px] border-r-[5px] border-t-[6px] border-l-transparent border-r-transparent border-t-stone-800 mx-auto" />
              </div>
            )}

            {/* Node */}
            <button
              onMouseEnter={() => onHover(evt.id)}
              onMouseLeave={() => onHover(null)}
              onClick={() => onClick(scored, regionName)}
              className={`rounded-full border-2 transition-transform duration-150 cursor-pointer
                ${color}
                ${isHovered || isSelected ? 'scale-150 ring-2 ring-stone-300' : 'hover:scale-125'}
              `}
              style={{
                width: size,
                height: size,
              }}
              title={eventTitle(evt, locale)}
            />
          </div>
        );
      })}
    </div>
  );
});

export default TimelineTrack;
