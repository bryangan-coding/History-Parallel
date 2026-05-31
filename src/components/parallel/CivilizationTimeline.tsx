'use client';

import { useState, useMemo, useRef, useCallback } from 'react';
import { useLocale } from '@/i18n/LocaleProvider';
import { civilizations, getCivilizationById, type Civilization, type CivilizationEvent, type CivilizationPeriod } from '@/data/civilizations';

const YEAR_MIN = -3200;
const YEAR_MAX = 2000;
const PADDING_LEFT = 108;
const PADDING_RIGHT = 40;
const TOP_PADDING = 54;
const BAR_HEIGHT = 22;
const BAR_GAP = 3;
const CIV_GAP = 8;

/** Dynamically pick tick interval based on visible years (affected by zoom) */
function getTickInterval(visibleYears: number): number {
  if (visibleYears <= 600) return 50;
  if (visibleYears <= 1200) return 100;
  if (visibleYears <= 2600) return 200;
  return 500;
}

function yearToX(year: number, minYear: number, totalPixels: number, totalYears: number): number {
  return ((year - minYear) / totalYears) * totalPixels;
}

/** Format a year for display */
function fmtYear(y: number): string {
  return y < 0 ? `${Math.abs(y)} BCE` : String(y);
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
  // Track hovered period for tooltip
  const [hoveredPeriod, setHoveredPeriod] = useState<{ id: string; name: string; nameEn: string; startYear: number; endYear: number; x: number; y: number } | null>(null);

  const filteredCivs = useMemo(
    () => civilizations.filter((c) => enabledCivs.has(c.id)),
    [enabledCivs]
  );

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
  const visibleYears = totalYears / zoomLevel;
  const tickInterval = getTickInterval(visibleYears);
  const showInlineLabels = zoomLevel >= 1.5;

  const toggleCiv = (id: string) => {
    setEnabledCivs((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  const ticks: number[] = [];
  for (let y = Math.ceil(YEAR_MIN / tickInterval) * tickInterval; y <= YEAR_MAX; y += tickInterval) {
    ticks.push(y);
  }

  const totalChartHeight = civLayouts.reduce((sum, l) => sum + l.height + CIV_GAP, TOP_PADDING + 40);

  return (
    <div>
      {/* Controls */}
      <div className="mb-4 flex flex-wrap items-center gap-3">
        <span className="text-xs font-semibold text-stone-500 uppercase tracking-wide">
          {locale === 'en' ? 'Civilizations:' : '文明：'}
        </span>
        {civilizations.map((civ) => (
          <label key={civ.id} className="flex items-center gap-1.5 text-sm cursor-pointer select-none">
            <input type="checkbox" checked={enabledCivs.has(civ.id)} onChange={() => toggleCiv(civ.id)}
              className="rounded border-stone-300" style={{ accentColor: civ.color }} />
            <span className="text-stone-600">{locale === 'en' ? civ.nameEn : civ.name}</span>
          </label>
        ))}
        <div className="ml-auto flex items-center gap-2">
          <span className="text-xs text-stone-400">{locale === 'en' ? 'Zoom:' : '缩放：'}</span>
          <button onClick={() => setZoomLevel((z) => Math.max(0.5, z - 0.25))}
            className="px-2 py-1 text-xs border border-stone-200 rounded hover:bg-stone-50 text-stone-600">−</button>
          <span className="text-xs text-stone-500 tabular-nums w-10 text-center">{Math.round(zoomLevel * 100)}%</span>
          <button onClick={() => setZoomLevel((z) => Math.min(3, z + 0.25))}
            className="px-2 py-1 text-xs border border-stone-200 rounded hover:bg-stone-50 text-stone-600">+</button>
        </div>
      </div>

      {/* Timeline */}
      <div ref={scrollRef} className="overflow-x-auto border border-stone-200 rounded-xl bg-white" style={{ position: 'relative' }}>
        {/* Hover tooltip */}
        {hoveredPeriod && (
          <div
            className="absolute z-20 bg-stone-800 text-white text-xs px-2 py-1 rounded shadow pointer-events-none whitespace-nowrap"
            style={{
              left: `${Math.min(hoveredPeriod.x + 12, baseWidth - 200)}px`,
              top: `${hoveredPeriod.y - 8}px`,
              transform: 'translateY(-100%)',
            }}
          >
            <span className="font-semibold">{locale === 'en' ? hoveredPeriod.nameEn : hoveredPeriod.name}</span>
            <span className="text-stone-400 ml-1.5">
              {fmtYear(hoveredPeriod.startYear)} – {fmtYear(hoveredPeriod.endYear)}
            </span>
          </div>
        )}

        <div style={{ minWidth: baseWidth }}>
          <svg width={baseWidth} height={totalChartHeight} viewBox={`0 0 ${baseWidth} ${totalChartHeight}`} className="w-full">
            {/* Grid */}
            {ticks.map((year) => {
              const x = PADDING_LEFT + yearToX(year, YEAR_MIN, chartWidth, totalYears);
              return (
                <line key={`grid-${year}`} x1={x} y1={TOP_PADDING} x2={x} y2={totalChartHeight - 30}
                  stroke={year % (tickInterval * 5) === 0 ? '#e7e5e4' : '#f5f5f4'}
                  strokeWidth={year % (tickInterval * 5) === 0 ? 0.5 : 0.3}
                  strokeDasharray={year % (tickInterval * 5) === 0 ? undefined : '3,3'}
                />
              );
            })}

            {/* Year axis */}
            <line x1={PADDING_LEFT} y1={TOP_PADDING - 14} x2={PADDING_LEFT + chartWidth} y2={TOP_PADDING - 14} stroke="#a8a29e" strokeWidth={0.5} />
            {ticks.map((year) => {
              const x = PADDING_LEFT + yearToX(year, YEAR_MIN, chartWidth, totalYears);
              const isMajor = year % (tickInterval * 5) === 0;
              return (
                <g key={`tick-${year}`}>
                  <line x1={x} y1={TOP_PADDING - (isMajor ? 18 : 14)} x2={x} y2={TOP_PADDING - 10} stroke="#a8a29e" strokeWidth={isMajor ? 0.8 : 0.4} />
                  {isMajor && (
                    <text x={x} y={TOP_PADDING - 22} textAnchor="middle" style={{ fontSize: 10, fill: '#57534e', fontWeight: 500 }}>
                      {fmtYear(year)}
                    </text>
                  )}
                </g>
              );
            })}

            {/* Civilization rows */}
            {civLayouts.map(({ civ, lanes, maxLanes, height }, civIndex) => {
              const civY = civLayouts.slice(0, civIndex).reduce((sum, l) => sum + l.height + CIV_GAP, TOP_PADDING);
              const isHighlighted = !highlightedCiv || highlightedCiv === civ.id;
              const opacity = isHighlighted ? 1 : 0.25;

              return (
                <g key={civ.id} opacity={opacity}>
                  {/* Row background */}
                  <rect x={0} y={civY - 2} width={baseWidth} height={height + 4} fill={civIndex % 2 === 0 ? '#fafaf9' : '#f5f5f4'} rx={2} opacity={0.5} />

                  {/* Label */}
                  <text x={PADDING_LEFT - 16} y={civY + height / 2 + 4} textAnchor="end"
                    style={{ fontSize: 12, fontWeight: 700, fill: civ.color, cursor: 'pointer' }}
                    onClick={() => setHighlightedCiv(highlightedCiv === civ.id ? null : civ.id)}>
                    {locale === 'en' ? civ.nameEn : civ.name}
                  </text>
                  <line x1={PADDING_LEFT - 4} y1={civY - 2} x2={PADDING_LEFT - 4} y2={civY + height + 2} stroke={civ.color} strokeWidth={2.5} opacity={0.3} />

                  {/* Lanes */}
                  {lanes.map((lane, laneIndex) => {
                    const laneY = civY + laneIndex * (BAR_HEIGHT + BAR_GAP);
                    const isContinuation = lane.length > 1;

                    return (
                      <g key={`${civ.id}-lane-${laneIndex}`}>
                        {/* Continuation track — thin bar spanning the entire lane range */}
                        {isContinuation && (() => {
                          const firstX = PADDING_LEFT + yearToX(lane[0].startYear, YEAR_MIN, chartWidth, totalYears);
                          const lastX = PADDING_LEFT + yearToX(lane[lane.length - 1].endYear, YEAR_MIN, chartWidth, totalYears);
                          return (
                            <rect x={firstX} y={laneY + BAR_HEIGHT / 2 - 1.5} width={lastX - firstX}
                              height={3} rx={1.5} fill={civ.color} opacity={0.15} />
                          );
                        })()}

                        {lane.map((period, periodIndex) => {
                          const startX = PADDING_LEFT + yearToX(period.startYear, YEAR_MIN, chartWidth, totalYears);
                          const endX = PADDING_LEFT + yearToX(period.endYear, YEAR_MIN, chartWidth, totalYears);
                          const width = Math.max(endX - startX, 3);
                          const showLabel = showInlineLabels || width > 60;
                          const isFirst = periodIndex === 0;
                          const isLast = periodIndex === lane.length - 1;

                          return (
                            <g key={period.id}
                              onMouseEnter={(e) => {
                                const rect = (e.currentTarget.closest('svg')?.parentElement?.parentElement as HTMLElement)?.getBoundingClientRect();
                                setHoveredPeriod({
                                  id: period.id, name: period.name, nameEn: period.nameEn,
                                  startYear: period.startYear, endYear: period.endYear,
                                  x: rect ? e.clientX - rect.left : 0,
                                  y: laneY,
                                });
                              }}
                              onMouseMove={(e) => {
                                const rect = (e.currentTarget.closest('svg')?.parentElement?.parentElement as HTMLElement)?.getBoundingClientRect();
                                if (rect) setHoveredPeriod(prev => prev ? { ...prev, x: e.clientX - rect.left, y: laneY } : null);
                              }}
                              onMouseLeave={() => setHoveredPeriod(null)}
                            >
                              {/* Connector arrow from previous period */}
                              {periodIndex > 0 && (() => {
                                const prev = lane[periodIndex - 1];
                                const prevEndX = PADDING_LEFT + yearToX(prev.endYear, YEAR_MIN, chartWidth, totalYears);
                                const arrowY = laneY + BAR_HEIGHT / 2;
                                const gapPixels = startX - prevEndX;
                                // Only show connector if there's a visible gap
                                if (gapPixels > 2) {
                                  return (
                                    <>
                                      <line x1={prevEndX} y1={arrowY} x2={startX - 3} y2={arrowY}
                                        stroke={civ.color} strokeWidth={1.5} opacity={0.5} strokeDasharray="4,3" />
                                      <polygon
                                        points={`${startX - 3},${arrowY - 3} ${startX},${arrowY} ${startX - 3},${arrowY + 3}`}
                                        fill={civ.color} opacity={0.5}
                                      />
                                    </>
                                  );
                                }
                                return null;
                              })()}

                              {/* Period bar */}
                              <rect x={startX} y={laneY} width={width} height={BAR_HEIGHT}
                                rx={isFirst && isLast ? 3 : isFirst ? 3 : isLast ? 3 : 0}
                                fill={civ.color} opacity={0.88}
                                className="cursor-pointer hover:opacity-100 transition-opacity" />

                              {/* Inline label */}
                              {showLabel && (
                                <text x={startX + width / 2} y={laneY + BAR_HEIGHT / 2 + 4}
                                  textAnchor="middle" style={{ fontSize: Math.max(8, 9 * zoomLevel / 1.5), fill: '#fff', pointerEvents: 'none', fontWeight: 600 }}>
                                  {locale === 'en' ? period.nameEn : period.name}
                                </text>
                              )}

                              {/* SVG title for native tooltip */}
                              <title>
                                {locale === 'en' ? period.nameEn : period.name}: {fmtYear(period.startYear)} – {fmtYear(period.endYear)}
                              </title>
                            </g>
                          );
                        })}
                      </g>
                    );
                  })}

                  {/* Key events */}
                  {isHighlighted && civ.keyEvents.map((event) => {
                    const ex = PADDING_LEFT + yearToX(event.year, YEAR_MIN, chartWidth, totalYears);
                    const ey = civY + height / 2;
                    return (
                      <g key={`${civ.id}-evt-${event.year}`}>
                        <line x1={ex} y1={civY + 4} x2={ex} y2={civY + height - 4} stroke="#292524" strokeWidth={0.5} opacity={0.12} />
                        <circle cx={ex} cy={ey} r={3.5} fill="#292524" stroke="#fff" strokeWidth={1.5}
                          className="cursor-pointer" onClick={() => setSelectedEvent(event)} />
                        <title>{fmtYear(event.year)}: {locale === 'en' ? event.titleEn : event.title}</title>
                      </g>
                    );
                  })}
                </g>
              );
            })}

            {/* Legend */}
            <text x={PADDING_LEFT} y={totalChartHeight - 12} style={{ fontSize: 9, fill: '#a8a29e' }}>
              ● = {locale === 'en' ? 'Key Event' : '重大事件'} &nbsp; — &nbsp;
              {locale === 'en' ? 'Gray bar = continuous timeline, arrow = gap between eras' : '灰条 = 连续时间线，箭头 = 朝代间隙'}
            </text>
          </svg>
        </div>
      </div>

      {/* Civilization detail panel */}
      {highlightedCiv && (() => {
        const civ = getCivilizationById(highlightedCiv);
        if (!civ) return null;
        return (
          <div className="mt-4 p-5 border border-stone-200 rounded-xl bg-white">
            <div className="flex items-start justify-between">
              <div>
                <h3 className="text-base font-semibold text-stone-900">{locale === 'en' ? civ.nameEn : civ.name}</h3>
                <p className="text-xs text-stone-400 mt-0.5">{civ.periods.length} {locale === 'en' ? 'dynasties/periods' : '个朝代/时期'}</p>
              </div>
              <button onClick={() => setHighlightedCiv(null)} className="text-stone-400 hover:text-stone-600 text-xs">{locale === 'en' ? 'Close' : '关闭'}</button>
            </div>
            <div className="mt-3 space-y-1.5">
              <h4 className="text-xs font-semibold text-stone-500 uppercase tracking-wide">{locale === 'en' ? 'Key Events' : '重大事件'}</h4>
              {civ.keyEvents.map((event) => (
                <div key={`detail-${event.year}-${event.title}`} className="flex items-center gap-2 text-sm">
                  <span className="text-xs font-mono text-stone-400 tabular-nums w-14 text-right">{fmtYear(event.year)}</span>
                  <span className="text-stone-600">{locale === 'en' ? event.titleEn : event.title}</span>
                </div>
              ))}
            </div>
          </div>
        );
      })()}

      {/* Selected event tooltip */}
      {selectedEvent && (
        <div className="fixed bottom-6 left-1/2 -translate-x-1/2 px-4 py-2 rounded-lg bg-stone-800 text-white text-sm shadow-lg z-50">
          <span className="font-mono text-xs opacity-75 mr-2">{fmtYear(selectedEvent.year)}</span>
          {locale === 'en' ? selectedEvent.titleEn : selectedEvent.title}
          <button onClick={() => setSelectedEvent(null)} className="ml-2 text-stone-400 hover:text-white text-xs">×</button>
        </div>
      )}
    </div>
  );
}
