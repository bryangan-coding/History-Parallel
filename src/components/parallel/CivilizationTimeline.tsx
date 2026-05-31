'use client';

import { useState, useMemo, useRef, useCallback } from 'react';
import { useLocale } from '@/i18n/LocaleProvider';
import { civilizations, getCivilizationById, type Civilization, type CivilizationEvent } from '@/data/civilizations';

const YEAR_MIN = -3200;
const YEAR_MAX = 2000;
const LABEL_HEIGHT = 30;
const BAR_HEIGHT = 24;
const BAR_GAP = 4;
const PADDING_LEFT = 100;
const PADDING_RIGHT = 40;
const TOP_PADDING = 40;

const YEAR_TICK_INTERVALS = [
  { range: 500, interval: 100, label: '每百年', labelEn: 'per century' },
  { range: 1000, interval: 100, label: '每百年', labelEn: 'per century' },
  { range: Infinity, interval: 500, label: '每五百年', labelEn: 'every 500y' },
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

  const totalHeight = filteredCivs.length * (BAR_HEIGHT + BAR_GAP) + TOP_PADDING + 40;
  const ticks: number[] = [];
  for (let y = Math.ceil(YEAR_MIN / yearInterval) * yearInterval; y <= YEAR_MAX; y += yearInterval) {
    ticks.push(y);
  }

  // Check for active overlaps
  const getActivePeriods = useCallback(() => {
    const activeMap = new Map<string, number>();
    for (let year = YEAR_MIN; year <= YEAR_MAX; year += 10) {
      let count = 0;
      const overlapping: string[] = [];
      for (const civ of filteredCivs) {
        for (const period of civ.periods) {
          if (year >= period.startYear && year <= period.endYear) {
            count++;
            overlapping.push(civ.id);
            break;
          }
        }
      }
      if (count >= 3) {
        for (const cid of overlapping) {
          activeMap.set(cid, (activeMap.get(cid) || 0) + 1);
        }
      }
    }
    return activeMap;
  }, [filteredCivs]);

  const overlapMap = useMemo(() => getActivePeriods(), [getActivePeriods]);

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
          <span className="text-xs text-stone-500">{Math.round(zoomLevel * 100)}%</span>
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
            height={totalHeight}
            viewBox={`0 0 ${baseWidth} ${totalHeight}`}
            className="w-full"
          >
            {/* Year axis */}
            <line
              x1={PADDING_LEFT}
              y1={TOP_PADDING}
              x2={PADDING_LEFT + chartWidth}
              y2={TOP_PADDING}
              stroke="#d6d3d1"
              strokeWidth={1}
            />

            {/* Year ticks */}
            {ticks.map((year) => {
              const x = PADDING_LEFT + yearToX(year, YEAR_MIN, chartWidth, totalYears);
              return (
                <g key={year}>
                  <line
                    x1={x}
                    y1={TOP_PADDING - 4}
                    x2={x}
                    y2={TOP_PADDING + 4}
                    stroke="#a8a29e"
                    strokeWidth={0.5}
                  />
                  <text
                    x={x}
                    y={TOP_PADDING - 8}
                    textAnchor="middle"
                    style={{ fontSize: 10, fill: '#78716c' }}
                  >
                    {year < 0 ? `${Math.abs(year)} BCE` : year}
                  </text>
                </g>
              );
            })}

            {/* Civilization bars */}
            {filteredCivs.map((civ, civIndex) => {
              const y = TOP_PADDING + 10 + civIndex * (BAR_HEIGHT + BAR_GAP);
              const isHighlighted = !highlightedCiv || highlightedCiv === civ.id;
              const opacity = isHighlighted ? 1 : 0.3;

              return (
                <g key={civ.id} opacity={opacity}>
                  {/* Civi name label */}
                  <text
                    x={PADDING_LEFT - 10}
                    y={y + BAR_HEIGHT / 2 + 4}
                    textAnchor="end"
                    style={{
                      fontSize: 11,
                      fontWeight: 600,
                      fill: civ.color,
                      cursor: 'pointer',
                    }}
                    onClick={() =>
                      setHighlightedCiv(
                        highlightedCiv === civ.id ? null : civ.id
                      )
                    }
                  >
                    {locale === 'en' ? civ.nameEn : civ.name}
                  </text>

                  {/* Period bars */}
                  {civ.periods.map((period) => {
                    const startX =
                      PADDING_LEFT +
                      yearToX(period.startYear, YEAR_MIN, chartWidth, totalYears);
                    const endX =
                      PADDING_LEFT +
                      yearToX(period.endYear, YEAR_MIN, chartWidth, totalYears);
                    const width = Math.max(endX - startX, 4);

                    return (
                      <g key={period.id}>
                        <rect
                          x={startX}
                          y={y}
                          width={width}
                          height={BAR_HEIGHT}
                          rx={3}
                          fill={civ.color}
                          opacity={0.85}
                          className="cursor-pointer hover:opacity-100 transition-opacity"
                          onClick={() =>
                            setHighlightedCiv(
                              highlightedCiv === civ.id ? null : civ.id
                            )
                          }
                        />
                        {/* Period label on bar if wide enough */}
                        {width > 60 && (
                          <text
                            x={startX + width / 2}
                            y={y + BAR_HEIGHT / 2 + 4}
                            textAnchor="middle"
                            style={{
                              fontSize: 9,
                              fill: '#fff',
                              pointerEvents: 'none',
                            }}
                          >
                            {locale === 'en'
                              ? period.nameEn
                              : period.name}
                          </text>
                        )}
                      </g>
                    );
                  })}

                  {/* Key events */}
                  {isHighlighted &&
                    civ.keyEvents.map((event) => {
                      const ex =
                        PADDING_LEFT +
                        yearToX(event.year, YEAR_MIN, chartWidth, totalYears);
                      return (
                        <g key={`${civ.id}-${event.year}-${event.title}`}>
                          <circle
                            cx={ex}
                            cy={y + BAR_HEIGHT / 2}
                            r={3}
                            fill="#292524"
                            stroke="#fff"
                            strokeWidth={1}
                            className="cursor-pointer hover:r-[4]"
                            onClick={() => setSelectedEvent(event)}
                          />
                        </g>
                      );
                    })}

                  {/* Overlap highlight */}
                  {overlapMap.has(civ.id) && overlapMap.get(civ.id)! > 20 && (
                    <rect
                      x={-10}
                      y={y - 1}
                      width={8}
                      height={BAR_HEIGHT + 2}
                      rx={2}
                      fill="#f59e0b"
                      opacity={0.6}
                    />
                  )}
                </g>
              );
            })}

            {/* Legend */}
            <g transform={`translate(${PADDING_LEFT}, ${totalHeight - 16})`}>
              <text style={{ fontSize: 9, fill: '#a8a29e' }}>
                ● = {locale === 'en' ? 'Key Event' : '重大事件'}  |  ▲ ={' '}
                {locale === 'en'
                  ? 'Active overlaps'
                  : '多文明重叠时期'}
              </text>
            </g>
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
                <h3 className="text-base font-semibold text-stone-900">
                  {locale === 'en' ? civ.nameEn : civ.name}
                </h3>
                <p className="text-xs text-stone-400 mt-0.5">
                  {civ.periods.length}{' '}
                  {locale === 'en' ? 'dynasties/periods' : '个朝代/时期'}
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
                <div
                  key={`${event.year}-${event.title}`}
                  className="flex items-center gap-2 text-sm"
                >
                  <span className="text-xs font-mono text-stone-400 tabular-nums w-14 text-right">
                    {event.year < 0
                      ? `${Math.abs(event.year)} BCE`
                      : event.year}
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
            {selectedEvent.year < 0
              ? `${Math.abs(selectedEvent.year)} BCE`
              : selectedEvent.year}
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
