'use client';

import Link from 'next/link';
import { X, MapPin, Calendar, Users } from 'lucide-react';
import type { ScoredEvent } from '@/lib/types';
import { eventTitle, eventSummary, eventPlaceName, personName } from '@/lib/types';
import { formatYearRange } from '@/lib/date';
import type { Locale } from '@/lib/types';
import { getPersonsForEvent, getRegionById } from '@/data/mockData';

interface Props {
  scored: ScoredEvent;
  regionName: string;
  onClose: () => void;
  locale: Locale;
}

export default function EventPreviewPanel({ scored, regionName, onClose, locale }: Props) {
  const evt = scored.event;
  const persons = getPersonsForEvent(evt.id);
  const region = getRegionById(evt.regionId);

  return (
    <div className="mt-4 border border-stone-200 rounded-xl bg-white p-5 animate-in fade-in slide-in-from-bottom-2 duration-200">
      <div className="flex items-start justify-between gap-4">
        <div className="flex-1 min-w-0">
          <h3 className="text-base font-semibold text-stone-900 leading-snug">
            {eventTitle(evt, locale)}
          </h3>
          <div className="mt-1.5 flex flex-wrap items-center gap-3 text-xs text-stone-500">
            <span className="flex items-center gap-1">
              <Calendar className="w-3 h-3" />
              {formatYearRange(evt.startYear, evt.endYear)}
            </span>
            {eventPlaceName(evt, locale) && (
              <span className="flex items-center gap-1">
                <MapPin className="w-3 h-3" />
                {eventPlaceName(evt, locale)}
              </span>
            )}
            {region && (
              <span className="flex items-center gap-1">
                <span className="w-1.5 h-1.5 rounded-full bg-stone-400" />
                {region?.name ?? regionName}
              </span>
            )}
          </div>
        </div>
        <button
          onClick={onClose}
          className="shrink-0 p-1 rounded-md hover:bg-stone-100 text-stone-400 hover:text-stone-600 transition-colors"
          aria-label="Close"
        >
          <X className="w-4 h-4" />
        </button>
      </div>

      {eventSummary(evt, locale) && (
        <p className="mt-3 text-sm text-stone-600 leading-relaxed">
          {eventSummary(evt, locale)}
        </p>
      )}

      {persons.length > 0 && (
        <div className="mt-3 flex items-center gap-2 text-xs text-stone-500">
          <Users className="w-3 h-3" />
          <span>
            {persons.map((p) => personName(p, locale)).join('、')}
          </span>
        </div>
      )}

      <div className="mt-4 flex items-center gap-3">
        <Link
          href={`/events/${evt.id}`}
          className="inline-flex items-center text-xs font-medium text-stone-700 hover:text-stone-900 bg-stone-100 hover:bg-stone-200 px-3 py-1.5 rounded-md transition-colors"
        >
          {locale === 'en' ? 'View details →' : '查看详情 →'}
        </Link>
      </div>
    </div>
  );
}
