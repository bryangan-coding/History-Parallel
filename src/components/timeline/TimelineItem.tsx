import Link from 'next/link';
import type { HistoricalEvent } from '@/lib/types';
import { formatYearRange } from '@/lib/date';
import { getRegionById } from '@/data/mockData';
import { useLocale } from '@/i18n/LocaleProvider';
import { eventTitle, eventSummary, regionName } from '@/lib/types';

export default function TimelineItem({
  event,
  isLast,
}: {
  event: HistoricalEvent;
  personId: string;
  isLast: boolean;
}) {
  const { locale } = useLocale();
  const region = getRegionById(event.regionId ?? '');

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
          {eventTitle(event, locale)}
        </h4>
        <p className="mt-1 text-sm text-stone-600 leading-relaxed">
          {eventSummary(event, locale)}
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
