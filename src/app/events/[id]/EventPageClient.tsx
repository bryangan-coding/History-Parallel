'use client';

import { notFound } from 'next/navigation';
import Link from 'next/link';
import { useLocale } from '@/i18n/LocaleProvider';
import PageHeader from '@/components/common/PageHeader';
import Tag from '@/components/common/Tag';
import EventCard from '@/components/cards/EventCard';
import SourceList from '@/components/cards/SourceList';
import PersonCard from '@/components/cards/PersonCard';
import {
  getEventById,
  getPersonsForEvent,
  getRegionById,
  events,
} from '@/data/mockData';
import {
  eventTitle,
  eventDescription,
  eventPlaceName,
  eventTags,
  regionName,
} from '@/lib/types';

export function EventPageClient({ id }: { id: string }) {
  const { locale, t } = useLocale();
  const event = getEventById(id);

  if (!event) {
    notFound();
  }

  const persons = getPersonsForEvent(event.id);
  const region = getRegionById(event.regionId);
  const tags = eventTags(event, locale);
  const displayPlaceName = eventPlaceName(event, locale);

  const relatedEvents = events
    .filter(
      (e) =>
        e.id !== event.id &&
        e.regionId === event.regionId &&
        Math.abs(e.startYear - event.startYear) <= 50,
    )
    .slice(0, 5);

  return (
    <div>
      <PageHeader
        title={eventTitle(event, locale)}
        backTo="/"
        backLabel={t.nav.backToHome}
      />

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 space-y-6">
          <article>
            <div className="p-6 rounded-xl border border-stone-200 bg-white">
              <div className="flex flex-wrap items-center gap-2 mb-2">
                {tags.map((tag) => (
                  <Tag key={tag} label={tag} />
                ))}
              </div>
              <p className="text-stone-600 leading-relaxed">
                {eventDescription(event, locale)}
              </p>
            </div>
          </article>
          <SourceList sourceIds={event.sourceIds} />
        </div>

        <div className="space-y-6">
          <div className="p-5 rounded-xl border border-stone-200 bg-white">
            <h4 className="text-xs font-semibold text-stone-400 uppercase tracking-wide mb-3">
              {t.event.eventInfo}
            </h4>
            <dl className="space-y-2 text-sm">
              <div className="flex justify-between">
                <dt className="text-stone-500">{t.event.time}</dt>
                <dd className="text-stone-700 font-medium">
                  {event.approximateDateText ?? `${event.startYear}${locale === 'en' ? '' : '年'}`}
                  {event.endYear && event.endYear !== event.startYear
                    ? ` — ${event.endYear}${locale === 'en' ? '' : '年'}`
                    : ''}
                </dd>
              </div>
              {displayPlaceName && (
                <div className="flex justify-between">
                  <dt className="text-stone-500">{t.event.location}</dt>
                  <dd className="text-stone-700 font-medium">
                    {displayPlaceName}
                  </dd>
                </div>
              )}
              {region && (
                <div className="flex justify-between">
                  <dt className="text-stone-500">{t.event.region}</dt>
                  <dd className="text-stone-700 font-medium">
                    {regionName(region, locale)}
                  </dd>
                </div>
              )}
              <div className="flex justify-between">
                <dt className="text-stone-500">{t.event.importance}</dt>
                <dd className="text-amber-500 font-medium">
                  {'★'.repeat(event.importance)}
                </dd>
              </div>
            </dl>
          </div>

          {persons.length > 0 && (
            <div>
              <h4 className="text-xs font-semibold text-stone-400 uppercase tracking-wide mb-3">
                {t.event.relatedPeople}
              </h4>
              <div className="space-y-2">
                {persons.map((p) => (
                  <PersonCard key={p.id} person={p} />
                ))}
              </div>
            </div>
          )}

          <Link
            href={`/parallel?year=${event.startYear}&focusEvent=${event.id}`}
            className="block p-4 rounded-xl border border-stone-300 bg-stone-50 hover:bg-stone-100 hover:border-stone-400 transition-colors text-center"
          >
            <p className="text-sm font-medium text-stone-700">
              {t.event.viewParallel}
            </p>
          </Link>
        </div>
      </div>

      {relatedEvents.length > 0 && (
        <section className="mt-10 pt-8 border-t border-stone-200">
          <h3 className="text-sm font-semibold text-stone-500 uppercase tracking-wide mb-4">
            {t.event.relatedEventsTitle}
          </h3>
          <div className="space-y-3">
            {relatedEvents.map((e) => (
              <EventCard key={e.id} event={e} showParallelButton />
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
