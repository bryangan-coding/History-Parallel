'use client';

import Link from 'next/link';
import type { HistoricalEvent, Region } from '@/lib/types';
import { formatYearRange } from '@/lib/date';
import { useLocale } from '@/i18n/LocaleProvider';
import { eventTitle, eventSummary, regionName } from '@/lib/types';

/**
 * Detect if an event should be rendered as a lightweight badge
 * instead of a full event card.
 *
 * Lightweight badge criteria:
 * - tags include '时代', '时代背景', '生平', '人生阶段'
 * - OR summary matches generic era-context or life-activity patterns
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
  // Era-context events: "XXX生活在XX时期。"
  if (/^[\u4e00-\u9fff]+生活在[\u4e00-\u9fff]+时期/.test(s)) {
    return true;
  }
  return false;
}

interface TimelineItemProps {
  event: HistoricalEvent;
  isLast: boolean;
  /** Pre-resolved region — avoids importing mockData in client */
  region?: Region;
  /** Whether this item's badge is being hovered */
  isHovered: boolean;
  /** Called when a badge is hovered or unhovered */
  onHover: (hovered: boolean) => void;
}

export default function TimelineItem({
  event,
  isLast,
  region,
  isHovered,
  onHover,
}: TimelineItemProps) {
  const { locale, toScript } = useLocale();
  const badge = isBadgeEvent(event);

  // ============================================================
  // Badge render: lightweight tag on the timeline
  // ============================================================
  if (badge) {
    return (
      <div className={`relative pl-12 ${isLast ? 'pb-0' : 'pb-8'}`}>
        {/* Dot on timeline */}
        <div
          className={`absolute left-[17px] top-2 w-1.5 h-1.5 rounded-full transition-all duration-300 ${
            isHovered ? 'bg-amber-500 scale-150' : 'bg-stone-300'
          }`}
        />

        {/* Badge label */}
        <button
          onMouseEnter={() => onHover(true)}
          onMouseLeave={() => onHover(false)}
          className={`block text-left w-full max-w-[200px] px-2.5 py-1 rounded-md border transition-all duration-300 ${
            isHovered
              ? 'border-amber-300 bg-amber-50 scale-105 shadow-sm'
              : 'border-stone-100 bg-stone-50/50 hover:border-stone-200'
          }`}
        >
          <span className="text-[11px] text-stone-400 tabular-nums mr-1.5">
            {formatYearRange(event.startYear, event.endYear)}
          </span>
          <span className={`text-[11px] transition-colors duration-300 ${
            isHovered ? 'text-stone-700 font-medium' : 'text-stone-500'
          }`}>
            {toScript(eventTitle(event, locale))}
          </span>
        </button>
      </div>
    );
  }

  // ============================================================
  // Full card render: normal event
  // ============================================================
  return (
    <div className={`relative pl-12 ${isLast ? 'pb-0' : 'pb-8'}`}>
      <div className="absolute left-[15px] top-1.5 w-2.5 h-2.5 rounded-full bg-stone-400 border-2 border-white ring-1 ring-stone-200" />

      <div className="p-4 rounded-lg border border-stone-200 bg-white hover:border-stone-300 transition-colors">
        <div className="flex items-center gap-2 text-sm">
          <span className="font-semibold text-stone-600 tabular-nums">
            {formatYearRange(event.startYear, event.endYear)}
          </span>
          {event.placeNameEn && locale === 'en' && (
            <>
              <span className="text-stone-300">·</span>
              <span className="text-stone-500">{event.placeNameEn}</span>
            </>
          )}
          {event.placeName && !(locale === 'en' && event.placeNameEn) && (
            <>
              <span className="text-stone-300">·</span>
              <span className="text-stone-500">{event.placeName}</span>
            </>
          )}
        </div>
        <h4 className="mt-1 text-base font-medium text-stone-900">
          {toScript(eventTitle(event, locale))}
        </h4>
        <p className="mt-1 text-sm text-stone-600 leading-relaxed">
          {toScript(eventSummary(event, locale))}
        </p>
        <div className="flex items-center gap-2 mt-2">
          {region && (
            <span className="text-xs text-stone-400">
              {regionName(region, locale)}
            </span>
          )}
          <Link
            href={`/parallel?year=${event.startYear}&focusEvent=${event.id}`}
            className="ml-auto text-xs font-medium text-stone-500 hover:text-stone-800 transition-colors border border-stone-200 rounded-md px-2 py-0.5 hover:border-stone-400"
          >
            {locale === 'en' ? 'Parallel World →' : '同时期世界 →'}
          </Link>
        </div>
      </div>
    </div>
  );
}
