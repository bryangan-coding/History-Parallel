import Link from 'next/link';
import type { HistoricalEvent } from '@/lib/types';
import { formatYearRange } from '@/lib/date';
import { getRegionById, getPersonsForEvent } from '@/data/mockData';
import { useLocale } from '@/i18n/LocaleProvider';
import {
  eventTitle,
  eventSummary,
  eventTags,
  eventPlaceName,
  regionName,
  personName,
} from '@/lib/types';
import Tag from '@/components/common/Tag';

export default function EventCard({
  event,
  showParallelButton = false,
}: {
  event: HistoricalEvent;
  showParallelButton?: boolean;
}) {
  const { locale } = useLocale();
  const region = event.regionId ? getRegionById(event.regionId) : undefined;
  const persons = getPersonsForEvent(event.id);
  const tags = eventTags(event, locale);
  const displayPlaceName = eventPlaceName(event, locale);

  const importanceDots = {
    1: '•',
    2: '••',
    3: '•••',
    4: '••••',
    5: '•••••',
  };

  return (
    <div className="p-5 rounded-xl border border-stone-200 bg-white">
      <div className="flex items-start justify-between gap-3">
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 flex-wrap">
            <h3 className="text-base font-semibold text-stone-900">
              {eventTitle(event, locale)}
            </h3>
            <span
              className="text-xs text-amber-500 shrink-0"
              title={`${locale === 'en' ? 'Importance' : '重要性'}: ${event.importance}/5`}
            >
              {importanceDots[event.importance]}
            </span>
          </div>
          <div className="flex items-center gap-2 mt-1 text-sm text-stone-500">
            <span>{formatYearRange(event.startYear ?? 0, event.endYear)}</span>
            {displayPlaceName && (
              <>
                <span className="text-stone-300">·</span>
                <span>{displayPlaceName}</span>
              </>
            )}
            {region && (
              <>
                <span className="text-stone-300">·</span>
                <span>{regionName(region, locale)}</span>
              </>
            )}
          </div>
        </div>
      </div>

      <p className="mt-2 text-sm text-stone-600 leading-relaxed">
        {eventSummary(event, locale)}
      </p>

      {persons.length > 0 && (
        <div className="flex flex-wrap items-center gap-1 mt-2">
          {persons.map((p) => (
            <Link
              key={p.id}
              href={`/people/${p.id}`}
              className="text-xs text-stone-500 hover:text-stone-800 transition-colors underline underline-offset-2"
            >
              {personName(p, locale)}
            </Link>
          ))}
        </div>
      )}

      <div className="flex flex-wrap items-center gap-2 mt-3 pt-3 border-t border-stone-100">
        <div className="flex flex-wrap gap-1">
          {tags.slice(0, 3).map((tag) => (
            <Tag key={tag} label={tag} />
          ))}
        </div>

        {showParallelButton && (
          <Link
            href={`/parallel?year=${event.startYear ?? 0}&focusEvent=${event.id}`}
            className="ml-auto text-xs font-medium text-stone-500 hover:text-stone-800 transition-colors border border-stone-200 rounded-md px-2 py-0.5 hover:border-stone-400"
          >
            {locale === 'en' ? 'Parallel World →' : '同时期世界 →'}
          </Link>
        )}
      </div>
    </div>
  );
}
