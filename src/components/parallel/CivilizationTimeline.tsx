'use client';

import { useState, useMemo, useRef, useCallback } from 'react';
import { useLocale } from '@/i18n/LocaleProvider';
import { civilizations, getCivilizationById, type Civilization, type CivilizationEvent, type CivilizationPeriod } from '@/data/civilizations';

const YEAR_MIN = -3200;
const YEAR_MAX = 2000;
const PADDING_LEFT = 108;
const PADDING_RIGHT = 40;
const TOP_PADDING = 50;
const BAR_HEIGHT = 22;
const BAR_GAP = 3;
const CIV_GAP = 8; // extra gap between civilizations

const YEAR_TICK_INTERVALS = [
  { range: 500, interval: 100 },
  { range: 1000, interval: 200 },
  { range: Infinity, interval: 500 },
];

function getYearInterval(totalYears: number): number {
  for (const ti of YEAR_TICK_INTERVALS) {
    if (totalYears <= ti.range) return ti.interval;
  }
  return 500;
}

function yearToX(year: number, minYear: number, totalPixels: number, totalYears: number): number {
  return ((year - minYear) / totalYears) * totalPixels;
}

/** Assign periods to vertical lanes so overlapping periods don't collide */
function computeLanes(periods: CivilizationPeriod[]): CivilizationPeriod[][] {
  if (periods.length === 0) return [];
  const sorted = [...periods].sort((a, b) => a.startYear - b.startYear);
  const lanes: CivilizationPeriod[][] = [];

  for (const period of sorted) {
    let placed = false;
    for (const lane of lanes) {
      const lastInLane = lane[lane.length - 1];
      // Non-overlapping: this period starts after the last one in this lane ends
      if (period.startYear >= lastInLane.endYear) {
        lane.push(period);
        placed = true;
        break;
      }
    }
    if (!placed) {
      lanes.push([period]);
    }
  }
  return lanes;
}

export default function CivilizationTimeline() {
  const { locale } = useLocale();
  const scrollRef = useRef<HTMLDivElement>(null);

  const [enabledCivs, setEnabledCivs] = useState<Set<string>>(
    new Set(civilizations.map((c) => c.id))
  );
  const [highlightedCiv, setHighlightedCiv] = useState<string | null>(null);
  const [selectedEvent, setSelectedEvent] = useState<CivilizationEvent | null>(null);
  const [zoomLevel, setZoomLevel] = useState(1);

  const filteredCivs = useMemo(
    () => civilizations.filter((c) => enabledCivs.has(c.id)),
    [enabledCivs]
  );

  // Compute lanes for each civilization
  const civLayouts = useMemo(() => {
    return filteredCivs.map((civ) => {
      const lanes = computeLanes(civ.periods);
      const maxLanes = Math.max(lanes.length, 1);
      const height = maxLanes * (BAR_HEIGHT + BAR_GAP);
      return { civ, lanes, maxLanes, height };
    });
  }, [filteredCivs]);

  const totalYears = YEAR_MAX - YEAR_MIN;
  const baseWidth = 1200 * zoomLevel;
  const chartWidth = baseWidth - PADDING_LEFT - PADDING_RIGHT;
  const yearInterval = getYearInterval(totalYears * zoomLevel);

  const toggleCiv = (id: string) => {
    setEnabledCivs((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  const ticks: number[] = [];
  for (let y = Math.ceil(YEAR_MIN / yearInterval) * yearInterval; y <= YEAR_MAX; y += yearInterval) {
    ticks.push(y);
  }

  // Calculate height
  const totalChartHeight = civLayouts.reduce((sum, l) => sum + l.height + CIV_GAP, TOP_PADDING + 40);

  return (
    <div>
      {/* Controls */}
      <div className="mb-4 flex flex-wrap items-center gap-3">
        <span className="text-xs font-semibold text-stone-500 uppercase tracking-wide">
          {locale === 'en' ? 'Civilizations:' : '文明：'}
        </span>
        {civilizations.map((civ) => (
          <label
            key={civ.id}
            className="flex items-center gap-1.5 text-sm cursor-pointer select-none"
          >
            <input
              type="checkbox"
              checked={enabledCivs.has(civ.id)}
              onChange={() => toggleCiv(civ.id)}
              className="rounded border-stone-300"
              style={{ accentColor: civ.color }}
            />
            <span className="text-stone-600">{locale === 'en' ? civ.nameEn : civ.name}</span>
          </label>
        ))}
        <div className="ml-auto flex items-center gap-2">
          <span className="text-xs text-stone-400">
            {locale === 'en' ? 'Zoom:' : '缩放：'}
          </span>
          <button
            onClick={() => setZoomLevel((z) => Math.max(0.5, z - 0.25))}
            className="px-2 py-1 text-xs border border-stone-200 rounded hover:bg-stone-50 text-stone-600"
          >
            −
          </button>
          <span className="text-xs text-stone-500 tabular-nums w-10 text-center">{Math.round(zoomLevel * 100)}%</span>
          <button
            onClick={() => setZoomLevel((z) => Math.min(3, z + 0.25))}
            className="px-2 py-1 text-xs border border-stone-200 rounded hover:bg-stone-50 text-stone-600"
          >
            +
          </button>
        </div>
      </div>

      {/* Timeline */}
      <div
        ref={scrollRef}
        className="overflow-x-auto border border-stone-200 rounded-xl bg-white"
      >
        <div style={{ minWidth: baseWidth }}>
          <svg
            width={baseWidth}
            height={totalChartHeight}
            viewBox={`0 0 ${baseWidth} ${totalChartHeight}`}
            className="w-full"
          >
            {/* Background grid lines for centuries */}
            {ticks.map((year) => {
              const x = PADDING_LEFT + yearToX(year, YEAR_MIN, chartWidth, totalYears);
              return (
                <line
                  key={`grid-${year}`}
                  x1={x}
                  y1={TOP_PADDING}
                  x2={x}
                  y2={totalChartHeight - 30}
                  stroke="#f5f5f4"
                  strokeWidth={0.5}
                  strokeDasharray="3,3"
                />
              );
            })}

            {/* Year axis */}
            <line
              x1={PADDING_LEFT}
              y1={TOP_PADDING - 10}
              x2={PADDING_LEFT + chartWidth}
              y2={TOP_PADDING - 10}
              stroke="#a8a29e"
              strokeWidth={0.5}
            />
            {ticks.map((year) => {
              const x = PADDING_LEFT + yearToX(year, YEAR_MIN, chartWidth, totalYears);
              return (
                <g key={`tick-${year}`}>
                  <line x1={x} y1={TOP_PADDING - 14} x2={x} y2={TOP_PADDING - 6} stroke="#a8a29e" strokeWidth={0.5} />
                  <text x={x} y={TOP_PADDING - 18} textAnchor="middle" style={{ fontSize: 10, fill: '#78716c' }}>
                    {year < 0 ? `${Math.abs(year)} BCE` : year}
                  </text>
                </g>
              );
            })}

            {/* Civilization rows */}
            {civLayouts.map(({ civ, lanes, maxLanes, height }, civIndex) => {
              // Calculate the y position for this civilization block
              const civY = civLayouts
                .slice(0, civIndex)
                .reduce((sum, l) => sum + l.height + CIV_GAP, TOP_PADDING);

              const isHighlighted = !highlightedCiv || highlightedCiv === civ.id;
              const opacity = isHighlighted ? 1 : 0.3;

              return (
                <g key={civ.id} opacity={opacity}>
                  {/* Row background */}
                  <rect
                    x={0}
                    y={civY - 2}
                    width={baseWidth}
                    height={height + 4}
                    fill={civIndex % 2 === 0 ? '#fafaf9' : '#f5f5f4'}
                    rx={2}
                    opacity={0.5}
                  />

                  {/* Civilization label */}
                  <text
                    x={PADDING_LEFT - 16}
                    y={civY + height / 2 + 4}
                    textAnchor="end"
                    style={{
                      fontSize: 12,
                      fontWeight: 700,
                      fill: civ.color,
                      cursor: 'pointer',
                    }}
                    onClick={() => setHighlightedCiv(highlightedCiv === civ.id ? null : civ.id)}
                  >
                    {locale === 'en' ? civ.nameEn : civ.name}
                  </text>

                  {/* Separator line after label */}
                  <line
                    x1={PADDING_LEFT - 4}
                    y1={civY - 2}
                    x2={PADDING_LEFT - 4}
                    y2={civY + height + 2}
                    stroke={civ.color}
                    strokeWidth={2}
                    opacity={0.3}
                  />

                  {/* Render each lane */}
                  {lanes.map((lane, laneIndex) => {
                    const laneY = civY + laneIndex * (BAR_HEIGHT + BAR_GAP);

                    // Draw lane background
                    return (
                      <g key={`${civ.id}-lane-${laneIndex}`}>
                        {lane.map((period) => {
                          const startX = PADDING_LEFT + yearToX(period.startYear, YEAR_MIN, chartWidth, totalYears);
                          const endX = PADDING_LEFT + yearToX(period.endYear, YEAR_MIN, chartWidth, totalYears);
                          const width = Math.max(endX - startX, 3);

                          return (
                            <g key={period.id}>
                              {/* Period bar */}
                              <rect
                                x={startX}
                                y={laneY}
                                width={width}
                                height={BAR_HEIGHT}
                                rx={3}
                                fill={civ.color}
                                opacity={0.85}
                                className="cursor-pointer hover:opacity-100 transition-opacity"
                              />

                              {/* Period label */}
                              {width > 50 && (
                                <text
                                  x={startX + width / 2}
                                  y={laneY + BAR_HEIGHT / 2 + 4}
                                  textAnchor="middle"
                                  style={{ fontSize: 9, fill: '#fff', pointerEvents: 'none', fontWeight: 500 }}
                                >
                                  {locale === 'en' ? period.nameEn : period.name}
                                </text>
                              )}

                              {/* Leading arrow if this period follows another in same lane */}
                              {lane.indexOf(period) > 0 && (() => {
                                const prev = lane[lane.indexOf(period) - 1];
                                const prevEndX = PADDING_LEFT + yearToX(prev.endYear, YEAR_MIN, chartWidth, totalYears);
                                const arrowY = laneY + BAR_HEIGHT / 2;
                                return (
                                  <line
                                    x1={prevEndX}
                                    y1={arrowY}
                                    x2={startX}
                                    y2={arrowY}
                                    stroke={civ.color}
                                    strokeWidth={1}
                                    opacity={0.4}
                                    strokeDasharray="3,2"
                                  />
                                );
                              })()}
                            </g>
                          );
                        })}
                      </g>
                    );
                  })}

                  {/* Key events */}
                  {isHighlighted &&
                    civ.keyEvents.map((event) => {
                      const ex = PADDING_LEFT + yearToX(event.year, YEAR_MIN, chartWidth, totalYears);
                      const ey = civY + height / 2;
                      return (
                        <g key={`${civ.id}-event-${event.year}-${event.title}`}>
                          <line x1={ex} y1={civY + 2} x2={ex} y2={civY + height - 2} stroke="#292524" strokeWidth={0.5} opacity={0.15} />
                          <circle
                            cx={ex}
                            cy={ey}
                            r={4}
                            fill="#292524"
                            stroke="#fff"
                            strokeWidth={1.5}
                            className="cursor-pointer"
                            onClick={() => setSelectedEvent(event)}
                          />
                          <title>{event.year < 0 ? `${Math.abs(event.year)} BCE` : event.year}: {locale === 'en' ? event.titleEn : event.title}</title>
                        </g>
                      );
                    })}
                </g>
              );
            })}

            {/* Legend */}
            <text x={PADDING_LEFT} y={totalChartHeight - 12} style={{ fontSize: 9, fill: '#a8a29e' }}>
              ● = {locale === 'en' ? 'Key Event' : '重大事件'}  —  {locale === 'en' ? 'Same-lane periods show succession' : '同行时期表示继承/连续关系'}
            </text>
          </svg>
        </div>
      </div>

      {/* Legend for lane logic */}
      <div className="mt-2 flex items-center gap-4 text-xs text-stone-400">
        <span>
          {locale === 'en'
            ? 'Overlapping periods are split into separate rows. Same-lane periods represent chronological succession.'
            : '重叠的时期会自动分成不同行。同行内的时期按时间顺序排列。'}
        </span>
      </div>

      {/* Civilization detail panel */}
      {highlightedCiv && (() => {
        const civ = getCivilizationById(highlightedCiv);
        if (!civ) return null;
        return (
          <div className="mt-4 p-5 border border-stone-200 rounded-xl bg-white">
            <div className="flex items-start justify-between">
              <div>
                <h3 className="text-base font-semibold text-stone-900">
                  {locale === 'en' ? civ.nameEn : civ.name}
                </h3>
                <p className="text-xs text-stone-400 mt-0.5">
                  {civ.periods.length} {locale === 'en' ? 'dynasties/periods' : '个朝代/时期'}
                </p>
              </div>
              <button
                onClick={() => setHighlightedCiv(null)}
                className="text-stone-400 hover:text-stone-600 text-xs"
              >
                {locale === 'en' ? 'Close' : '关闭'}
              </button>
            </div>
            <div className="mt-3 space-y-1.5">
              <h4 className="text-xs font-semibold text-stone-500 uppercase tracking-wide">
                {locale === 'en' ? 'Key Events' : '重大事件'}
              </h4>
              {civ.keyEvents.map((event) => (
                <div key={`detail-${event.year}-${event.title}`} className="flex items-center gap-2 text-sm">
                  <span className="text-xs font-mono text-stone-400 tabular-nums w-14 text-right">
                    {event.year < 0 ? `${Math.abs(event.year)} BCE` : event.year}
                  </span>
                  <span className="text-stone-600">
                    {locale === 'en' ? event.titleEn : event.title}
                  </span>
                </div>
              ))}
            </div>
          </div>
        );
      })()}

      {/* Selected event tooltip */}
      {selectedEvent && (
        <div className="fixed bottom-6 left-1/2 -translate-x-1/2 px-4 py-2 rounded-lg bg-stone-800 text-white text-sm shadow-lg z-50">
          <span className="font-mono text-xs opacity-75 mr-2">
            {selectedEvent.year < 0 ? `${Math.abs(selectedEvent.year)} BCE` : selectedEvent.year}
          </span>
          {locale === 'en' ? selectedEvent.titleEn : selectedEvent.title}
          <button
            onClick={() => setSelectedEvent(null)}
            className="ml-2 text-stone-400 hover:text-white text-xs"
          >
            ×
          </button>
        </div>
      )}
    </div>
  );
}
