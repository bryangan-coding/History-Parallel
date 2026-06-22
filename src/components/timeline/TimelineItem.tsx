'use client';

import Link from 'next/link';
import type { HistoricalEvent, Region } from '@/lib/types';
import { formatYearRange } from '@/lib/date';
import { useLocale } from '@/i18n/LocaleProvider';
import { eventTitle, eventSummary, regionName } from '@/lib/types';

/**
 * Detect if an event should be rendered as a lightweight badge
 */
function isBadgeEvent(event: HistoricalEvent): boolean {
  const tags = event.tags;
  if (tags.includes('时代') || tags.includes('时代背景') || tags.includes('生平') || tags.includes('人生阶段')) {
    return true;
  }
  const s = event.summary ?? '';
  if (
    s.includes('留下了属于这个时代的历史印记') ||
    s.includes('生活并参与社会活动') ||
    s.includes('时期生活与活动')
  ) {
    return true;
  }
  if (/^[\u4e00-\u9fff]+生活在[\u4e00-\u9fff]+时期/.test(s)) {
    return true;
  }
  return false;
}

// ==================== Constants ====================
const AXIS_X = 20;
const CONNECTOR_BASE = 40; // base length of connector line from axis

interface TimelineItemProps {
  event: HistoricalEvent;
  /** Y position of the marker on the axis */
  dotY: number;
  /** Height of the duration bar (0 = point event) */
  barHeight: number;
  /** Horizontal offset layer (0, 1, 2...) for overlap avoidance */
  cardOffset: number;
  /** Whether this is the last event */
  isLast: boolean;
  region?: Region;
  isHovered: boolean;
  onHover: (hovered: boolean) => void;
}

export default function TimelineItem({
  event,
  dotY,
  barHeight,
  cardOffset,
  isLast,
  region,
  isHovered,
  onHover,
}: TimelineItemProps) {
  const { locale, toScript } = useLocale();
  const badge = isBadgeEvent(event);
  const isDuration = barHeight > 4;

  const connectorLen = CONNECTOR_BASE + cardOffset; // cardOffset is already in pixels
  const cardLeft = AXIS_X + connectorLen + 8;
  const cardWidth = 300;

  // ============================================================
  // Badge render: compact inline tag
  // ============================================================
  if (badge) {
    return (
      <div
        className={`absolute ${isHovered ? 'z-20' : 'z-0'}`}
        style={{ left: 0, top: dotY - 12 }}
        onMouseEnter={() => onHover(true)}
        onMouseLeave={() => onHover(false)}
      >
        {/* Dot on axis */}
        <div
          className={`absolute w-1.5 h-1.5 rounded-full transition-all duration-300 ${
            isHovered ? 'bg-amber-500 scale-150' : 'bg-stone-300'
          }`}
          style={{ left: AXIS_X - 3, top: 2 }}
        />
        {/* Short connector */}
        <div
          className={`absolute top-[4px] h-px transition-colors ${
            isHovered ? 'bg-amber-300' : 'bg-stone-200'
          }`}
          style={{ left: AXIS_X + 4, width: 16 }}
        />
        {/* Badge label */}
        <span
          className={`absolute top-0 inline-block max-w-[160px] px-2 py-0.5 rounded border text-left transition-all duration-300 ${
            isHovered
              ? 'border-amber-300 bg-amber-50 scale-110 shadow-sm'
              : 'border-stone-100 bg-stone-50/50'
          }`}
          style={{ left: AXIS_X + 24 }}
        >
          <span className="text-[10px] text-stone-400 tabular-nums mr-1">
            {formatYearRange(event.startYear, event.endYear)}
          </span>
          <span className={`text-[10px] transition-colors duration-300 ${
            isHovered ? 'text-stone-700 font-medium' : 'text-stone-500'
          }`}>
            {toScript(eventTitle(event, locale))}
          </span>
        </span>
      </div>
    );
  }

  // ============================================================
  // Full card render
  // ============================================================
  return (
    <div
      className={`absolute ${isHovered ? 'z-20' : 'z-10'}`}
      style={{
        left: 0,
        top: dotY,
        height: Math.max(barHeight, 10),
        minHeight: 10,
      }}
      onMouseEnter={() => onHover(true)}
      onMouseLeave={() => onHover(false)}
    >
      {/* ===== Timeline marker on axis ===== */}
      {isDuration ? (
        // Duration bar — vertical orange bar spanning the event's time range
        <div
          className="absolute rounded-full transition-all duration-300"
          style={{
            left: AXIS_X - 1.5,
            top: 0,
            width: 3,
            height: barHeight,
            backgroundColor: isHovered ? '#f59e0b' : '#d97706',
            opacity: isHovered ? 1 : 0.75,
          }}
        />
      ) : (
        // Single point — orange dot
        <div
          className={`absolute w-2.5 h-2.5 rounded-full transition-all duration-300 ${
            isHovered
              ? 'bg-amber-500 scale-150 shadow-lg shadow-amber-200/60'
              : 'bg-orange-600'
          }`}
          style={{
            left: AXIS_X - 5,
            top: -5,
          }}
        />
      )}

      {/* ===== Connector line from axis to card ===== */}
      <div
        className={`absolute h-px transition-colors duration-300 ${
          isHovered ? 'bg-amber-400' : 'bg-orange-300/70'
        }`}
        style={{
          left: AXIS_X + 2,
          top: isDuration ? 1 : -1,
          width: connectorLen,
        }}
      />

      {/* ===== Event Card ===== */}
      <div
        className="absolute p-4 rounded-lg border transition-all duration-300 bg-white"
        style={{
          left: cardLeft,
          top: isDuration ? 0 : -32,
          width: cardWidth,
          borderColor: isHovered ? '#f59e0b' : '#e7e5e4',
          boxShadow: isHovered ? '0 4px 16px rgba(0,0,0,0.1)' : '0 1px 3px rgba(0,0,0,0.04)',
          borderLeftWidth: 3,
          borderLeftColor: isHovered ? '#f59e0b' : '#d97706',
        }}
      >
        {/* Year and location */}
        <div className="flex items-center gap-2 text-sm">
          <span className="font-semibold text-stone-600 tabular-nums">
            {formatYearRange(event.startYear, event.endYear)}
          </span>
          {event.placeName && (
            <>
              <span className="text-stone-300">·</span>
              <span className="text-stone-500 text-xs">
                {locale === 'en' && event.placeNameEn ? event.placeNameEn : event.placeName}
              </span>
            </>
          )}
        </div>

        {/* Title */}
        <h4 className="mt-1 text-base font-medium text-stone-900 leading-snug">
          {toScript(eventTitle(event, locale))}
        </h4>

        {/* Summary */}
        <p className="mt-1.5 text-sm text-stone-600 leading-relaxed line-clamp-3">
          {toScript(eventSummary(event, locale))}
        </p>

        {/* Footer: region + link */}
        <div className="flex items-center gap-2 mt-2.5">
          {region && (
            <span className="text-xs text-stone-400 bg-stone-50 px-1.5 py-0.5 rounded">
              {regionName(region, locale)}
            </span>
          )}
          <Link
            href={`/parallel?year=${event.startYear}&focusEvent=${event.id}`}
            className="ml-auto text-xs font-medium text-amber-700 hover:text-amber-900 transition-colors border border-amber-200 rounded-md px-2 py-0.5 hover:border-amber-400 hover:bg-amber-50"
          >
            {locale === 'en' ? 'Parallel World →' : toScript('同时期世界 →')}
          </Link>
        </div>
      </div>
    </div>
  );
}
