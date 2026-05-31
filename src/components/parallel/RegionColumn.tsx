import Link from 'next/link';
import type { ScoredEvent } from '@/lib/types';
import { formatYearRange } from '@/lib/date';
import { useLocale } from '@/i18n/LocaleProvider';
import { eventTitle, eventSummary, eventPlaceName, personName } from '@/lib/types';

export default function RegionColumn({
  title,
  events,
  className,
}: {
  title: string;
  events: ScoredEvent[];
  className?: string;
}) {
  const { locale } = useLocale();

  if (events.length === 0) return null;

  return (
    <div className={`${className ?? ''}`}>
      <h3 className="text-sm font-semibold text-stone-500 uppercase tracking-wide mb-3 flex items-center gap-2">
        <span className="w-1.5 h-1.5 rounded-full bg-stone-400" />
        {title}
        <span className="text-xs text-stone-400 font-normal tabular-nums">
          ({events.length})
        </span>
      </h3>
      <div className="space-y-3">
        {events.map((scored) => {
          const evt = scored.event;
          const displayTitle = eventTitle(evt, locale);
          const displaySummary = eventSummary(evt, locale);
          const displayPlace = eventPlaceName(evt, locale);

          return (
            <Link
              key={evt.id}
              href={`/events/${evt.id}`}
              className="block p-3 rounded-lg border border-stone-200 bg-white hover:border-stone-400 transition-colors"
            >
              <div className="flex items-center gap-2 text-xs">
                <span className="font-medium text-stone-600 tabular-nums">
                  {formatYearRange(evt.startYear, evt.endYear)}
                </span>
                {displayPlace && (
                  <span className="text-stone-400">{displayPlace}</span>
                )}
                {evt.importance >= 4 && (
                  <span className="ml-auto text-amber-500">
                    {'★'.repeat(evt.importance - 2)}
                  </span>
                )}
              </div>
              <h4 className="mt-1 text-sm font-medium text-stone-900">
                {displayTitle}
              </h4>
              <p className="mt-1 text-xs text-stone-500 leading-relaxed line-clamp-2">
                {displaySummary}
              </p>
              {scored.persons.length > 0 && (
                <div className="flex flex-wrap gap-1 mt-1.5">
                  {scored.persons.map((p) => (
                    <span key={p.id} className="text-[11px] text-stone-400">
                      {personName(p, locale)}
                    </span>
                  ))}
                </div>
              )}
            </Link>
          );
        })}
      </div>
    </div>
  );
}
