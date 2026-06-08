'use client';

import { notFound } from 'next/navigation';
import Link from 'next/link';
import { useLocale } from '@/i18n/LocaleProvider';
import PageHeader from '@/components/common/PageHeader';
import Tag from '@/components/common/Tag';
import Timeline from '@/components/timeline/Timeline';
import EmptyState from '@/components/common/EmptyState';
import { formatLifespan } from '@/lib/date';
import { personName, personSummary, personTags, regionName } from '@/lib/types';
import type { Person, HistoricalEvent, Region } from '@/lib/types';

interface PersonPageClientProps {
  id: string;
  person?: Person;
  region?: Region;
  personEvents: HistoricalEvent[];
  /** Pre-resolved event regions for the timeline */
  eventRegions: Map<string, Region | undefined>;
}

export function PersonPageClient({ id, person, region, personEvents, eventRegions }: PersonPageClientProps) {
  const { locale, t, toScript } = useLocale();

  if (!person) {
    notFound();
  }

  const tags = personTags(person, locale);

  return (
    <div>
      <PageHeader
        backTo="/"
        backLabel={t.nav.backToHome}
        title={toScript(personName(person, locale))}
      />

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-1">
          <div className="p-5 rounded-xl border border-stone-200 bg-white sticky top-20">
            {region && (
              <p className="text-xs text-stone-400 font-medium uppercase tracking-wide mb-1">
                {regionName(region, locale)}
              </p>
            )}
            {person.alternativeNames.length > 0 && (
              <p className="text-sm text-stone-500 mt-1">
                {toScript(person.alternativeNames.join(' / '))}
              </p>
            )}
            <p className="text-sm text-stone-500 mt-3">
              {formatLifespan(person.birthYear ?? 0, person.deathYear ?? 0)}
            </p>
            <div className="flex flex-wrap gap-1.5 mt-3">
              {tags.map((tag) => (
                <Tag key={tag} label={toScript(tag)} />
              ))}
            </div>
            <p className="mt-4 text-sm text-stone-600 leading-relaxed">
              {toScript(personSummary(person, locale))}
            </p>
          </div>
        </div>

        <div className="lg:col-span-2">
          <h2 className="text-sm font-semibold text-stone-500 uppercase tracking-wide mb-4 flex items-center justify-between">
            <span>{t.person.timeline} ({personEvents.length})</span>
            <Link
              href={`/compare?preselect=${person.id}`}
              className="text-xs font-medium text-stone-400 hover:text-stone-600 transition-colors border border-stone-200 rounded-md px-2 py-0.5 hover:border-stone-300"
            >
              {locale === 'en' ? 'Compare →' : '对比他人 →'}
            </Link>
          </h2>
          {personEvents.length === 0 ? (
            <EmptyState
              title={t.person.noEvents}
              description={t.person.noEventsDesc}
            />
          ) : (
            <Timeline events={personEvents} eventRegions={eventRegions} />
          )}
        </div>
      </div>
    </div>
  );
}
