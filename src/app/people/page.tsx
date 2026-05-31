'use client';

import Link from 'next/link';
import { useLocale } from '@/i18n/LocaleProvider';
import PageHeader from '@/components/common/PageHeader';
import PersonCard from '@/components/cards/PersonCard';
import EmptyState from '@/components/common/EmptyState';
import { people } from '@/data/mockData';

export default function PeoplePage() {
  const { locale, t } = useLocale();

  const published = people.filter((p) => p.dataStatus === 'published');

  // Group by era
  const ancient = published.filter((p) => (p.birthYear ?? 0) < 0);
  const earlyMedieval = published.filter((p) => (p.birthYear ?? 0) >= 0 && (p.birthYear ?? 0) < 1000);
  const songEra = published.filter((p) => (p.birthYear ?? 0) >= 960 && (p.birthYear ?? 0) < 1127);
  const postSong = published.filter((p) => (p.birthYear ?? 0) >= 1127 && (p.birthYear ?? 0) < 1500);
  const modern = published.filter((p) => (p.birthYear ?? 0) >= 1500);

  const groups: { label: string; labelEn: string; items: typeof published }[] = [];
  if (ancient.length) groups.push({ label: '公元前', labelEn: 'BCE', items: ancient });
  if (earlyMedieval.length) groups.push({ label: '1–10 世纪', labelEn: '1st–10th Century', items: earlyMedieval });
  if (songEra.length) groups.push({ label: '11–12 世纪（北宋）', labelEn: '11th–12th C. (Northern Song)', items: songEra });
  if (postSong.length) groups.push({ label: '12–15 世纪', labelEn: '12th–15th Century', items: postSong });
  if (modern.length) groups.push({ label: '15 世纪之后', labelEn: 'After 15th Century', items: modern });

  if (published.length === 0) {
    return <EmptyState title={t.parallel.noData} description="" />;
  }

  return (
    <div className="max-w-3xl mx-auto">
      <PageHeader
        title={locale === 'en' ? 'Historical People' : '历史人物'}
        subtitle={locale === 'en' ? `${published.length} figures across ${groups.length} eras` : `${published.length} 位人物，跨越 ${groups.length} 个时期`}
        backTo="/"
        backLabel={t.nav.backToHome}
      />

      {groups.map((group) => (
        <section key={group.label} className="mt-8">
          <h2 className="text-xs font-semibold text-stone-400 uppercase tracking-wide mb-3">
            {locale === 'en' ? group.labelEn : group.label}
            <span className="ml-2 text-stone-300 font-normal">({group.items.length})</span>
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {group.items.map((p) => (
              <PersonCard key={p.id} person={p} />
            ))}
          </div>
        </section>
      ))}
    </div>
  );
}
