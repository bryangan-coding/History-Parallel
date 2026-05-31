'use client';

import { useSearchParams } from 'next/navigation';
import Link from 'next/link';
import { useLocale } from '@/i18n/LocaleProvider';
import SearchBox from '@/components/common/SearchBox';
import PageHeader from '@/components/common/PageHeader';
import EmptyState from '@/components/common/EmptyState';
import PersonCard from '@/components/cards/PersonCard';
import EventCard from '@/components/cards/EventCard';
import { search } from '@/lib/search';
import { formatYearRange } from '@/lib/date';
import { regionName, regionDescription } from '@/lib/types';

export default function SearchResults() {
  const searchParams = useSearchParams();
  const { locale, t } = useLocale();
  const query = searchParams.get('q') ?? '';
  const results = search(query);

  const hasResults =
    results.people.length > 0 ||
    results.events.length > 0 ||
    results.regions.length > 0 ||
    results.yearMatches.length > 0;

  return (
    <div>
      <PageHeader
        title={t.search.title}
        subtitle={
          query
            ? t.search.subtitleWithQuery.replace('{query}', query)
            : t.search.subtitle
        }
      />
      <SearchBox defaultValue={query} placeholder={t.search.searchPlaceholder} className="mb-8" />

      {!query && (
        <EmptyState
          title={t.search.noQueryTitle}
          description={t.search.noQueryDesc}
        />
      )}

      {query && !hasResults && (
        <EmptyState
          title={t.search.noResults.replace('{query}', query)}
          description={t.search.noResultsDesc}
        />
      )}

      {query && hasResults && (
        <div className="space-y-8">
          {results.people.length > 0 && (
            <section>
              <h2 className="text-sm font-semibold text-stone-500 uppercase tracking-wide mb-3">
                {t.search.sectionPeople} ({results.people.length})
              </h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                {results.people.map((person) => (
                  <PersonCard key={person.id} person={person} />
                ))}
              </div>
            </section>
          )}

          {results.events.length > 0 && (
            <section>
              <h2 className="text-sm font-semibold text-stone-500 uppercase tracking-wide mb-3">
                {t.search.sectionEvents} ({results.events.length})
              </h2>
              <div className="space-y-3">
                {results.events.map((event) => (
                  <EventCard
                    key={event.id}
                    event={event}
                    showParallelButton
                  />
                ))}
              </div>
            </section>
          )}

          {results.regions.length > 0 && (
            <section>
              <h2 className="text-sm font-semibold text-stone-500 uppercase tracking-wide mb-3">
                {t.search.sectionRegions} ({results.regions.length})
              </h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {results.regions.map((region) => (
                  <Link
                    key={region.id}
                    href="/parallel?year=1080"
                    className="block p-4 rounded-xl border border-stone-200 bg-white hover:border-stone-400 transition-colors"
                  >
                    <h3 className="font-medium text-stone-900">
                      {regionName(region, locale)}
                    </h3>
                    {regionDescription(region, locale) && (
                      <p className="mt-1 text-sm text-stone-500 line-clamp-2">
                        {regionDescription(region, locale)}
                      </p>
                    )}
                  </Link>
                ))}
              </div>
            </section>
          )}

          {results.yearMatches.length > 0 && (
            <section>
              <h2 className="text-sm font-semibold text-stone-500 uppercase tracking-wide mb-3">
                {t.search.sectionYears} ({results.yearMatches.length})
              </h2>
              {results.yearMatches.map((ym) => (
                <div key={ym.year}>
                  <div className="flex items-center justify-between mb-3">
                    <h3 className="text-base font-semibold text-stone-700">
                      {t.common.yearsAround.replace('{year}', String(ym.year))}
                    </h3>
                    <Link
                      href={`/parallel?year=${ym.year}`}
                      className="text-xs font-medium text-stone-500 hover:text-stone-800 transition-colors"
                    >
                      {t.search.viewParallel}
                    </Link>
                  </div>
                  <div className="space-y-2">
                    {ym.nearEvents.slice(0, 5).map((event) => (
                      <div key={event.id} className="text-sm text-stone-600">
                        <span className="text-stone-400 tabular-nums mr-2">
                          {formatYearRange(event.startYear, event.endYear)}
                        </span>
                        {event.titleEn && locale === 'en' ? event.titleEn : event.title}
                      </div>
                    ))}
                    {ym.nearEvents.length > 5 && (
                      <p className="text-xs text-stone-400">
                        {t.search.moreEvents.replace('{count}', String(ym.nearEvents.length - 5))}
                      </p>
                    )}
                  </div>
                </div>
              ))}
            </section>
          )}
        </div>
      )}
    </div>
  );
}
