'use client';

import { useState, useMemo, useRef, useCallback } from 'react';
import Link from 'next/link';
import type { HistoricalEvent } from '@/lib/types';
import { useLocale } from '@/i18n/LocaleProvider';
import { eventTitle, regionName } from '@/lib/types';
import { getRegionById } from '@/data/mockData';

interface EventMapViewProps {
  events: HistoricalEvent[];
  focusYear: number;
  range: number;
  yearRange?: [number, number];
  onYearRangeChange?: (range: [number, number]) => void;
}

function formatYearLabel(year: number): string {
  if (year < 0) {
    return `${Math.abs(year)} BCE`;
  }
  return String(year);
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
  const x = ((lng + 180) / 360) * 1000;
  const y = ((90 - lat) / 180) * 520;
  return { x, y };
}

// Region color palette — grouped by continent
const REGION_COLORS: Record<string, string> = {
  // Asia — warm spectrum (amber/red/orange)
  china: '#d97706',
  'song-dynasty': '#d97706',
  'tang-dynasty': '#d97706',
  'ming-dynasty': '#d97706',
  india: '#f59e0b',
  japan: '#ef4444',
  'mongol-empire': '#dc2626',
  'middle-east': '#b45309',
  seljuk: '#b45309',
  asia: '#d97706',
  // Europe — cool spectrum (blue/indigo/purple)
  europe: '#2563eb',
  england: '#3b82f6',
  byzantine: '#8b5cf6',
  'renaissance-europe': '#6366f1',
  'roman-empire': '#4f46e5',
  // Africa — green
  africa: '#059669',
  // Americas — teal
  americas: '#0d9488',
};

function getRegionColor(regionId?: string): string {
  if (!regionId) return '#78716c';
  return REGION_COLORS[regionId] ?? '#78716c';
}

// Quadratic bezier control point offset for map connections
function computeControlPoint(
  x1: number, y1: number, x2: number, y2: number,
): { cx: number; cy: number } {
  const midX = (x1 + x2) / 2;
  const midY = (y1 + y2) / 2;
  const dx = x2 - x1;
  const dy = y2 - y1;
  const dist = Math.sqrt(dx * dx + dy * dy);
  const offset = Math.min(dist * 0.4, 80);
  const cx = midX + (dy / dist) * offset * 0.3;
  const cy = midY - (dx / dist) * offset * 0.3;
  return { cx, cy };
}

export default function EventMapView({
  events,
  focusYear,
  yearRange,
}: EventMapViewProps) {
  const { locale } = useLocale();
  const [hoveredId, setHoveredId] = useState<string | null>(null);
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [hoveredConnection, setHoveredConnection] = useState<string | null>(null);
  const [useFilter, setUseFilter] = useState(true);
  const mapRef = useRef<HTMLDivElement>(null);

  const filterActive = useFilter && yearRange !== undefined;

  const allMarkers = useMemo(() => {
    return events
      .filter((e) => e.coordinates)
      .map((e) => {
        const pos = latLngToXY(e.coordinates!.lat, e.coordinates!.lng);
        const color = getRegionColor(e.regionId);
        const size = Math.max(6, e.importance * 3 + 3);
        const eventYear = e.startYear ?? 0;
        const endYear = e.endYear ?? eventYear;
        return { event: e, x: pos.x, y: pos.y, color, size, eventYear, endYear };
      });
  }, [events]);

  const filteredMarkers = useMemo(() => {
    if (!filterActive) return allMarkers;
    const [min, max] = yearRange!;
    return allMarkers.filter((m) => m.eventYear <= max && m.endYear >= min);
  }, [allMarkers, filterActive, yearRange]);

  const markers = filteredMarkers;

  const selectedEvent = useMemo(
    () => markers.find((m) => m.event.id === selectedId)?.event ?? null,
    [markers, selectedId],
  );

  const connectionLines = useMemo(() => {
    if (!selectedEvent || !selectedEvent.relatedEventIds.length) return [];
    const selectedMarker = allMarkers.find((m) => m.event.id === selectedEvent.id);
    if (!selectedMarker) return [];

    const color = getRegionColor(selectedEvent.regionId);

    return selectedEvent.relatedEventIds
      .map((relId) => {
        const relMarker = allMarkers.find((m) => m.event.id === relId);
        if (!relMarker) return null;
        const cp = computeControlPoint(
          selectedMarker.x, selectedMarker.y,
          relMarker.x, relMarker.y,
        );
        const pathD = `M ${selectedMarker.x} ${selectedMarker.y} Q ${cp.cx} ${cp.cy} ${relMarker.x} ${relMarker.y}`;
        return {
          id: `${selectedEvent.id}-${relId}`,
          fromId: selectedEvent.id,
          toId: relId,
          toEvent: relMarker.event,
          pathD,
          color,
          x1: selectedMarker.x,
          y1: selectedMarker.y,
          x2: relMarker.x,
          y2: relMarker.y,
        };
      })
      .filter(Boolean) as Array<{
        id: string;
        fromId: string;
        toId: string;
        toEvent: HistoricalEvent;
        pathD: string;
        color: string;
        x1: number;
        y1: number;
        x2: number;
        y2: number;
      }>;
  }, [selectedEvent, allMarkers]);

  // Event count for header
  const markerCount = markers.length;

  const handleMarkerClick = useCallback((eventId: string) => {
    setSelectedId((prev) => (prev === eventId ? null : eventId));
  }, []);

  return (
    <div className="relative bg-stone-50 rounded-xl border border-stone-200 overflow-hidden">
      {/* Header bar */}
      <div className="p-3 border-b border-stone-200 flex items-center gap-4 text-xs text-stone-500 flex-wrap">
        <span>
          Map View{filterActive ? ` · ${formatYearLabel(yearRange[0])} – ${formatYearLabel(yearRange[1])}` : ''}
        </span>
        <span className="text-stone-300">|</span>
        <span>{markerCount} event{markerCount !== 1 ? 's' : ''} visible</span>
        {yearRange && (
          <>
            <span className="text-stone-300">|</span>
            <button
              onClick={() => setUseFilter(!useFilter)}
              className={`text-[11px] font-medium transition-colors ${
                useFilter
                  ? 'text-stone-700 hover:text-stone-900'
                  : 'text-stone-400 hover:text-stone-600'
              }`}
            >
              {useFilter ? 'Filter by range' : 'Show all'}
            </button>
          </>
        )}
        {selectedEvent && (
          <>
            <span className="text-stone-300">|</span>
            <span className="text-amber-600">
              {connectionLines.length} connection{connectionLines.length !== 1 ? 's' : ''}
            </span>
          </>
        )}
      </div>

      <div ref={mapRef} className="relative" style={{ height: 520 }}>
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

          {/* Connection lines */}
          {selectedEvent && connectionLines.length > 0 && (
            <g>
              {connectionLines.map((conn) => {
                const isConnHovered = hoveredConnection === conn.id;
                return (
                  <g key={conn.id}>
                    {/* Invisible wider line for hover detection */}
                    <path
                      d={conn.pathD}
                      fill="none"
                      stroke="transparent"
                      strokeWidth="12"
                      style={{ cursor: 'pointer' }}
                      onMouseEnter={() => setHoveredConnection(conn.id)}
                      onMouseLeave={() => setHoveredConnection(null)}
                    />
                    {/* Visible dashed line */}
                    <path
                      d={conn.pathD}
                      fill="none"
                      stroke={conn.color}
                      strokeWidth={isConnHovered ? 2 : 1}
                      strokeDasharray={isConnHovered ? '6 3' : '4 4'}
                      opacity={isConnHovered ? 0.7 : 0.4}
                      style={{ transition: 'all 0.2s ease', pointerEvents: 'none' }}
                    />
                    {/* Animated dot */}
                    <circle r="3" fill={conn.color} opacity={0.8}>
                      <animateMotion
                        dur="3s"
                        repeatCount="indefinite"
                        path={conn.pathD}
                      />
                    </circle>

                    {/* Hover label */}
                    {isConnHovered && (
                      <g>
                        <rect
                          x={(conn.x1 + conn.x2) / 2 - 50}
                          y={(conn.y1 + conn.y2) / 2 - 18}
                          width={Math.min(eventTitle(conn.toEvent, locale).length * 6 + 16, 110)}
                          height={22}
                          rx="4"
                          fill="white"
                          stroke={conn.color}
                          strokeWidth="1"
                          opacity="0.95"
                        />
                        <text
                          x={(conn.x1 + conn.x2) / 2 + 8 - Math.min(eventTitle(conn.toEvent, locale).length * 3, 50)}
                          y={(conn.y1 + conn.y2) / 2 - 3}
                          fontSize="10"
                          fill="#292524"
                          fontWeight="500"
                          textAnchor="middle"
                        >
                          {eventTitle(conn.toEvent, locale).substring(0, 18)}
                        </text>
                      </g>
                    )}
                  </g>
                );
              })}
            </g>
          )}

          {/* Event markers */}
          {allMarkers.map(({ event, x, y, color, size }) => {
            const isHovered = hoveredId === event.id;
            const isSelected = selectedId === event.id;
            const inFilter = markers.some((m) => m.event.id === event.id);
            const opacity = inFilter ? 1 : 0.15;

            return (
              <g key={event.id} style={{ transition: 'opacity 0.4s ease', opacity }}>
                {/* Pulse ring for selected/hovered */}
                {(isSelected || isHovered) && inFilter && (
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
                  className={inFilter ? 'cursor-pointer' : 'cursor-default pointer-events-none'}
                  style={{
                    transition: 'transform 0.2s ease',
                    transformOrigin: `${x}px ${y}px`,
                  }}
                  onMouseEnter={() => inFilter && setHoveredId(event.id)}
                  onMouseLeave={() => setHoveredId(null)}
                  onClick={() => inFilter && handleMarkerClick(event.id)}
                />

                {/* Hover tooltip */}
                {isHovered && !isSelected && inFilter && (
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
                  {selectedEvent.startYear !== undefined
                    ? formatYearLabel(selectedEvent.startYear)
                    : '?'}
                  {selectedEvent.endYear &&
                    selectedEvent.endYear !== selectedEvent.startYear
                    ? `–${formatYearLabel(selectedEvent.endYear)}`
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
            {connectionLines.length > 0 && (
              <p className="text-[10px] text-stone-400 mt-1.5">
                {connectionLines.length} related event{connectionLines.length !== 1 ? 's' : ''} shown on map
              </p>
            )}
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
