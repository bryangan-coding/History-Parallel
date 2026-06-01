'use client';

import { useMemo, useEffect, useRef, useState } from 'react';
import type { Person, HistoricalEvent } from '@/lib/types';
import { useLocale } from '@/i18n/LocaleProvider';
import { personName, eventTitle, eventSummary } from '@/lib/types';
import { formatYear } from '@/lib/date';

const PERSON_COLORS = [
  '#d97706', '#2563eb', '#059669', '#dc2626',
  '#7c3aed', '#0d9488', '#ea580c', '#ca8a04',
];

const LANE_HEIGHT = 72;
const AXIS_HEIGHT = 28;
const LEFT_LABEL_WIDTH = 140;
const RIGHT_PADDING = 16;
const TIMELINE_WIDTH = 800;

interface CompareTimelineProps {
  people: Person[];
  allEvents: Map<string, HistoricalEvent[]>;
}

export default function CompareTimeline({ people, allEvents }: CompareTimelineProps) {
  const { locale, t } = useLocale();
  const containerRef = useRef<HTMLDivElement>(null);
  const [containerWidth, setContainerWidth] = useState(0);

  useEffect(() => {
    function update() {
      if (containerRef.current) {
        setContainerWidth(containerRef.current.clientWidth);
      }
    }
    update();
    window.addEventListener('resize', update);
    return () => window.removeEventListener('resize', update);
  }, []);

  // Compute global time range
  const { minYear, maxYear, totalSpan } = useMemo(() => {
    if (people.length === 0) return { minYear: 0, maxYear: 100, totalSpan: 100 };
    let min = Infinity;
    let max = -Infinity;
    people.forEach((p) => {
      if (p.birthYear != null && p.birthYear < min) min = p.birthYear;
      if (p.deathYear != null && p.deathYear > max) max = p.deathYear;
    });
    if (!isFinite(min)) min = 0;
    if (!isFinite(max)) max = 100;
    // If only one person, zoom in to their lifespan
    const pad = people.length === 1
      ? Math.max((max - min) * 0.3, 10)
      : Math.max((max - min) * 0.05, 5);
    return { minYear: min - pad, maxYear: max + pad, totalSpan: max - min + pad * 2 };
  }, [people]);

  // Generate year ticks
  const yearTicks = useMemo(() => {
    const ticks: number[] = [];
    const span = maxYear - minYear;
    let step: number;
    if (span <= 50) step = 5;
    else if (span <= 200) step = 20;
    else if (span <= 500) step = 50;
    else if (span <= 1500) step = 100;
    else step = 500;

    const startTick = Math.ceil(minYear / step) * step;
    for (let y = startTick; y <= maxYear; y += step) {
      ticks.push(y);
    }
    return ticks;
  }, [minYear, maxYear]);

  // Map year to x position in timeline space
  function yearToX(year: number): number {
    return LEFT_LABEL_WIDTH + ((year - minYear) / totalSpan) * TIMELINE_WIDTH;
  }

  // Get event label
  function getEventLabel(event: HistoricalEvent): string {
    const tags = event.tags;
    if (tags.includes('出生')) return t.compare.eventBirth;
    if (tags.includes('逝世')) return t.compare.eventDeath;
    if (tags.includes('成就')) return t.compare.eventAchievement;
    return eventTitle(event, locale);
  }

  if (people.length === 0) {
    return (
      <div className="py-16 text-center">
        <p className="text-stone-400 text-sm">{t.compare.noPeople}</p>
        <p className="text-stone-300 text-xs mt-2">{t.compare.noPeopleDesc}</p>
      </div>
    );
  }

  const svgViewWidth = LEFT_LABEL_WIDTH + TIMELINE_WIDTH + RIGHT_PADDING;
  const svgHeight = AXIS_HEIGHT + people.length * LANE_HEIGHT + 16;

  // responsive width: use container width if known, otherwise fallback to SVG view width
  const displayWidth = containerWidth > 0 ? containerWidth : '100%';

  return (
    <div className="mt-6" ref={containerRef}>
      <div className="overflow-x-auto rounded-lg border border-stone-200 bg-white">
        <svg
          viewBox={`0 0 ${svgViewWidth} ${svgHeight}`}
          width={displayWidth}
          height={containerWidth > 0 ? (svgHeight / svgViewWidth) * containerWidth : svgHeight}
          className="text-stone-600"
          preserveAspectRatio="xMidYMid meet"
        >
          {/* Year axis */}
          <line
            x1={LEFT_LABEL_WIDTH}
            y1={AXIS_HEIGHT}
            x2={svgViewWidth - RIGHT_PADDING}
            y2={AXIS_HEIGHT}
            stroke="#d6d3d1"
            strokeWidth="1"
          />
          {yearTicks.map((year) => (
            <g key={year}>
              <line
                x1={yearToX(year)}
                y1={AXIS_HEIGHT - 6}
                x2={yearToX(year)}
                y2={AXIS_HEIGHT}
                stroke="#a8a29e"
                strokeWidth="1"
              />
              <text
                x={yearToX(year)}
                y={AXIS_HEIGHT - 10}
                textAnchor="middle"
                className="fill-stone-400"
                style={{ fontSize: '11px' }}
              >
                {year < 0 ? `BC${Math.abs(year)}` : year}
              </text>
            </g>
          ))}

          {/* Person lanes */}
          {people.map((person, pi) => {
            const color = PERSON_COLORS[pi % PERSON_COLORS.length];
            const events = allEvents.get(person.id) ?? [];
            const birth = person.birthYear ?? 0;
            const death = person.deathYear ?? 0;
            const startX = yearToX(birth);
            const endX = yearToX(death);
            const laneY = AXIS_HEIGHT + pi * LANE_HEIGHT + 4;
            const barY = laneY + 2;
            const barH = 6;

            return (
              <g key={person.id}>
                {/* Person name label */}
                <text
                  x={LEFT_LABEL_WIDTH - 8}
                  y={laneY + 14}
                  textAnchor="end"
                  className="fill-stone-800"
                  style={{ fontSize: '13px', fontWeight: 600 }}
                >
                  {personName(person, locale)}
                </text>
                <text
                  x={LEFT_LABEL_WIDTH - 8}
                  y={laneY + 30}
                  textAnchor="end"
                  className="fill-stone-400"
                  style={{ fontSize: '11px' }}
                >
                  {birth === death ? formatYear(birth) : `${birth}–${death}`}
                </text>

                {/* Background lane */}
                <rect
                  x={LEFT_LABEL_WIDTH}
                  y={laneY}
                  width={TIMELINE_WIDTH}
                  height={LANE_HEIGHT - 8}
                  rx={6}
                  className="fill-stone-50"
                />
                {pi % 2 === 1 && (
                  <rect
                    x={LEFT_LABEL_WIDTH}
                    y={laneY}
                    width={TIMELINE_WIDTH}
                    height={LANE_HEIGHT - 8}
                    rx={6}
                    className="fill-stone-100/50"
                  />
                )}

                {/* Lifespan bar */}
                <rect
                  x={Math.max(startX, LEFT_LABEL_WIDTH)}
                  y={barY}
                  width={Math.max(endX - startX, 4)}
                  height={barH}
                  rx={3}
                  fill={color}
                  opacity={0.85}
                />

                {/* Event dots */}
                {events
                  .filter((e) => e.startYear != null)
                  .map((event) => {
                    const ex = yearToX(event.startYear!);
                    const ey = barY + barH / 2;
                    const isBirth = event.tags.includes('出生');
                    const isDeath = event.tags.includes('逝世');
                    const eventLabel = getEventLabel(event);

                    // Skip if event is way outside the visible area
                    if (ex < LEFT_LABEL_WIDTH - 30 || ex > svgViewWidth + 10) return null;

                    return (
                      <g key={event.id} className="group cursor-pointer">
                        {/* Vertical connector line */}
                        <line
                          x1={ex}
                          y1={barY + barH}
                          x2={ex}
                          y2={isBirth ? barY + barH + 16 : isDeath ? barY - 14 : barY - 8}
                          stroke={color}
                          strokeWidth="1"
                          opacity={0.3}
                        />
                        {/* Dot */}
                        <circle
                          cx={ex}
                          cy={ey}
                          r={isBirth || isDeath ? 4.5 : 3.5}
                          fill={isBirth || isDeath ? color : '#fff'}
                          stroke={color}
                          strokeWidth={isBirth || isDeath ? 2 : 1.5}
                        />
                        {/* Event label above/below */}
                        <text
                          x={ex}
                          y={isBirth ? barY + barH + 28 : barY - 18}
                          textAnchor="middle"
                          className="fill-stone-500"
                          style={{ fontSize: '10px' }}
                          opacity={0.8}
                        >
                          {eventLabel}
                        </text>

                        {/* Tooltip */}
                        <title>
                          {eventTitle(event, locale)}{'\n'}
                          {event.startYear}{'\n'}
                          {eventSummary(event, locale)}
                        </title>
                      </g>
                    );
                  })}
              </g>
            );
          })}
        </svg>
      </div>
    </div>
  );
}
