import Link from 'next/link';
import type { Person } from '@/lib/types';
import { formatLifespan } from '@/lib/date';
import { getRegionById } from '@/data/mockData';
import { useLocale } from '@/i18n/LocaleProvider';
import { personName, personSummary, personTags, regionName } from '@/lib/types';
import Tag from '@/components/common/Tag';

export default function PersonCard({ person }: { person: Person }) {
  const { locale } = useLocale();
  const region = person.regionId ? getRegionById(person.regionId) : undefined;
  const tags = personTags(person, locale);

  return (
    <Link
      href={`/people/${person.id}`}
      className="block p-5 rounded-xl border border-stone-200 bg-white hover:border-stone-400 hover:shadow-sm transition-all group"
    >
      <div className="flex items-start justify-between">
        <div>
          <h3 className="text-lg font-semibold text-stone-900 group-hover:text-stone-700 transition-colors">
            {personName(person, locale)}
          </h3>
          {person.alternativeNames.length > 0 && (
            <p className="text-sm text-stone-400 mt-0.5">
              {person.alternativeNames.slice(0, 2).join(' / ')}
            </p>
          )}
        </div>
        {region && (
          <span className="text-xs text-stone-400 bg-stone-50 px-2 py-0.5 rounded border border-stone-100">
            {regionName(region, locale)}
          </span>
        )}
      </div>
      <p className="mt-1 text-sm text-stone-500">
        {formatLifespan(person.birthYear ?? 0, person.deathYear ?? 0)}
      </p>
      <p className="mt-2 text-sm text-stone-600 leading-relaxed line-clamp-2">
        {personSummary(person, locale)}
      </p>
      <div className="flex flex-wrap gap-1 mt-2">
        {tags.slice(0, 4).map((tag) => (
          <Tag key={tag} label={tag} />
        ))}
      </div>
    </Link>
  );
}
