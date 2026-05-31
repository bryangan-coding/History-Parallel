'use client';

import { useState, useMemo } from 'react';
import Link from 'next/link';
import type { HistoricalEvent } from '@/lib/types';
import { useLocale } from '@/i18n/LocaleProvider';
import { eventTitle, regionName } from '@/lib/types';
import { getRegionById } from '@/data/mockData';

interface EventMapViewProps {
  events: HistoricalEvent[];
  focusYear: number;
  range: number;
}

// Simple world map outline paths (Mercator-like projection, normalized to 0-1000)
const CONTINENTS = [
  // North America
  'M 100,150 L 250,120 L 280,200 L 260,300 L 200,350 L 120,300 Z',
  // South America
  'M 230,380 L 280,370 L 300,500 L 280,600 L 250,620 L 220,550 Z',
  // Europe
  'M 430,100 L 520,90 L 550,150 L 540,200 L 500,220 L 460,200 L 440,160 Z',
  // Africa
  'M 440,230 L 540,220 L 570,300 L 560,450 L 520,550 L 470,530 L 450,400 L 430,300 Z',
  // Asia
  'M 550,90 L 750,60 L 850,100 L 880,180 L 840,250 L 800,300 L 720,280 L 650,250 L 580,200 L 550,150 Z',
  // Southeast Asia & Islands
  'M 780,250 L 820,280 L 850,320 L 830,350 L 790,340 L 760,300 Z',
  // Japan
  'M 880,150 L 890,180 L 885,210 L 875,190 Z',
  // Australia
  'M 750,480 L 830,460 L 850,520 L 810,560 L 760,550 Z',
  // India subcontinent
  'M 680,250 L 720,240 L 740,300 L 720,350 L 690,340 Z',
  // Middle East
  'M 580,200 L 620,190 L 640,220 L 620,250 L 590,240 Z',
  // Central America
  'M 210,320 L 240,310 L 250,340 L 230,360 L 200,350 Z',
];

// Helper: convert lat/lng to SVG x/y coordinates (simple equirectangular projection)
function latLngToXY(lat: number, lng: number): { x: number; y: number } {
  // Normalize to 0-1000 range
  const x = ((lng + 180) / 360) * 1000;
  const y = ((90 - lat) / 180) * 520; // Height ~520
  return { x, y };
}

// Region color palette
const REGION_COLORS: Record<string, string> = {
  'song-dynasty': '#d97706',
  'tang-dynasty': '#d97706',
  'ming-dynasty': '#d97706',
  china: '#d97706',
  europe: '#2563eb',
  england: '#3b82f6',
  byzantine: '#8b5cf6',
  'renaissance-europe': '#2563eb',
  'roman-empire': '#8b5cf6',
  'middle-east': '#059669',
  seljuk: '#10b981',
  'mongol-empire': '#dc2626',
  japan: '#ec4899',
  india: '#f59e0b',
};

function getRegionColor(regionId?: string): string {
  if (!regionId) return '#78716c';
  return REGION_COLORS[regionId] ?? '#78716c';
}

export default function EventMapView({ events, focusYear }: EventMapViewProps) {
  const { locale } = useLocale();
  const [hoveredId, setHoveredId] = useState<string | null>(null);
  const [selectedId, setSelectedId] = useState<string | null>(null);

  const markers = useMemo(() => {
    return events
      .filter((e) => e.coordinates)
      .map((e) => {
        const pos = latLngToXY(e.coordinates!.lat, e.coordinates!.lng);
        const color = getRegionColor(e.regionId);
        const size = Math.max(6, e.importance * 3 + 3);
        return { event: e, x: pos.x, y: pos.y, color, size };
      });
  }, [events]);

  const selectedEvent = useMemo(
    () => markers.find((m) => m.event.id === selectedId)?.event ?? null,
    [markers, selectedId],
  );

  return (
    <div className="relative bg-stone-50 rounded-xl border border-stone-200 overflow-hidden">
      <div className="p-3 border-b border-stone-200 flex items-center gap-4 text-xs text-stone-500">
        <span>Map View · {focusYear}</span>
        <span className="text-stone-300">|</span>
        <span>{markers.length} events with coordinates</span>
      </div>

      <div className="relative" style={{ height: 520 }}>
        <svg
          viewBox="0 0 1000 520"
          className="w-full h-full"
          style={{ background: '#e8e4df' }}
        >
          {/* Ocean */}
          <rect width="1000" height="520" fill="#d6d3cf" />

          {/* Continents */}
          {CONTINENTS.map((d, i) => (
            <path
              key={i}
              d={d}
              fill="#c4c0ba"
              stroke="#b8b4ae"
              strokeWidth="0.5"
            />
          ))}

          {/* Event markers */}
          {markers.map(({ event, x, y, color, size }) => {
            const isHovered = hoveredId === event.id;
            const isSelected = selectedId === event.id;

            return (
              <g key={event.id}>
                {/* Pulse ring for selected/hovered */}
                {(isSelected || isHovered) && (
                  <circle
                    cx={x}
                    cy={y}
                    r={size + 6}
                    fill="none"
                    stroke={color}
                    strokeWidth="1.5"
                    opacity={0.4}
                  >
                    <animate
                      attributeName="r"
                      from={size + 4}
                      to={size + 10}
                      dur="1.5s"
                      repeatCount="indefinite"
                    />
                    <animate
                      attributeName="opacity"
                      from="0.4"
                      to="0"
                      dur="1.5s"
                      repeatCount="indefinite"
                    />
                  </circle>
                )}

                {/* Marker dot */}
                <circle
                  cx={x}
                  cy={y}
                  r={size}
                  fill={color}
                  fillOpacity={isSelected ? 1 : 0.85}
                  stroke="white"
                  strokeWidth="1"
                  className="cursor-pointer transition-transform hover:scale-125"
                  style={{ transformOrigin: `${x}px ${y}px` }}
                  onMouseEnter={() => setHoveredId(event.id)}
                  onMouseLeave={() => setHoveredId(null)}
                  onClick={() => setSelectedId(isSelected ? null : event.id)}
                />

                {/* Hover tooltip */}
                {isHovered && !isSelected && (
                  <g>
                    <rect
                      x={x + 10}
                      y={y - 20}
                      width={Math.min(event.title.length * 7 + 20, 180)}
                      height={32}
                      rx="4"
                      fill="white"
                      stroke={color}
                      strokeWidth="1"
                      opacity="0.95"
                    />
                    <text
                      x={x + 16}
                      y={y - 1}
                      fontSize="10"
                      fill="#292524"
                      fontWeight="500"
                    >
                      {eventTitle(event, locale).substring(0, 25)}
                      {eventTitle(event, locale).length > 25 ? '...' : ''}
                    </text>
                  </g>
                )}
              </g>
            );
          })}
        </svg>

        {/* Selected event detail panel */}
        {selectedEvent && (
          <div className="absolute bottom-3 left-3 right-3 bg-white/95 backdrop-blur rounded-lg border border-stone-300 p-4 shadow-lg max-w-md">
            <div className="flex items-start justify-between">
              <div>
                <h4 className="font-semibold text-stone-900 text-sm">
                  {eventTitle(selectedEvent, locale)}
                </h4>
                <p className="text-xs text-stone-500 mt-1">
                  {selectedEvent.startYear ?? '?'}
                  {selectedEvent.endYear && selectedEvent.endYear !== selectedEvent.startYear
                    ? `–${selectedEvent.endYear}`
                    : ''}
                  {selectedEvent.regionId && (
                    <>
                      {' · '}
                      {(() => {
                        const r = getRegionById(selectedEvent.regionId ?? '');
                        return r ? regionName(r, locale) : selectedEvent.regionId;
                      })()}
                    </>
                  )}
                </p>
              </div>
              <button
                className="text-stone-400 hover:text-stone-600 text-lg leading-none"
                onClick={() => setSelectedId(null)}
              >
                ×
              </button>
            </div>
            <p className="text-xs text-stone-600 mt-2 line-clamp-2">
              {selectedEvent.summary ?? selectedEvent.summaryEn ?? ''}
            </p>
            <Link
              href={`/events/${selectedEvent.id}`}
              className="inline-block mt-2 text-xs font-medium text-amber-600 hover:text-amber-800"
            >
              {locale === 'en' ? 'View Details →' : '查看详情 →'}
            </Link>
          </div>
        )}

        {/* Legend */}
        <div className="absolute top-3 right-3 bg-white/90 rounded-md border border-stone-200 p-2 text-[10px]">
          <div className="text-stone-500 mb-1 font-semibold">Importance</div>
          {[5, 4, 3, 2, 1].map((imp) => (
            <div key={imp} className="flex items-center gap-1.5">
              <span
                className="inline-block rounded-full"
                style={{
                  width: Math.max(4, imp * 2 + 2),
                  height: Math.max(4, imp * 2 + 2),
                  backgroundColor: '#78716c',
                }}
              />
              <span className="text-stone-400">{'★'.repeat(imp)}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
