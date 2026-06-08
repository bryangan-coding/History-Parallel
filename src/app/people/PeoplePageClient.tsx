'use client';

import { useState, useEffect, useMemo, useCallback } from 'react';
import { useLocale } from '@/i18n/LocaleProvider';
import PageHeader from '@/components/common/PageHeader';
import PersonCard from '@/components/cards/PersonCard';
import EmptyState from '@/components/common/EmptyState';
import type { Person, Region } from '@/lib/types';

interface EraGroupStat {
  key: string;
  label: string;
  labelEn: string;
  count: number;
  minYear: number;
  maxYear: number;
}

const PAGE_SIZE = 50;

export default function PeoplePageClient({
  totalCount,
  eraStats,
}: {
  totalCount: number;
  eraStats: EraGroupStat[];
}) {
  const { locale, t } = useLocale();
  const [selectedEra, setSelectedEra] = useState<string>('all');
  const [people, setPeople] = useState<Person[]>([]);
  const [regions, setRegions] = useState<Region[]>([]);
  const [loading, setLoading] = useState(true);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(0);
  const [error, setError] = useState<string | null>(null);

  // Fetch regions once
  useEffect(() => {
    fetch('/api/data/regions')
      .then((r) => r.json())
      .then((data) => setRegions(data.items || data))
      .catch(() => setError(locale === 'en' ? 'Failed to load region data' : '地区数据加载失败'));
  }, [locale]);

  // Fetch people when era or page changes
  useEffect(() => {
    setLoading(true);
    setError(null);
    const params = new URLSearchParams({
      page: String(page),
      limit: String(PAGE_SIZE),
      published: 'true',
    });
    if (selectedEra !== 'all') {
      params.set('era', selectedEra);
    }

    fetch(`/api/data/people?${params}`)
      .then((r) => {
        if (!r.ok) throw new Error('Failed to fetch');
        return r.json();
      })
      .then((data) => {
        setPeople(data.items);
        setTotalPages(data.totalPages);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, [selectedEra, page]);

  const handleEraChange = useCallback((era: string) => {
    setSelectedEra(era);
    setPage(1);
  }, []);

  const activeEra = eraStats.find((e) => e.key === selectedEra);
  const subtitle =
    locale === 'en'
      ? `${totalCount} figures across ${eraStats.length} eras`
      : `${totalCount} 位人物，跨越 ${eraStats.length} 个时期`;

  return (
    <div className="max-w-3xl mx-auto">
      <PageHeader
        title={locale === 'en' ? 'Historical People' : '历史人物'}
        subtitle={subtitle}
        backTo="/"
        backLabel={t.nav.backToHome}
      />

      {/* Era filter tabs */}
      <div className="flex flex-wrap gap-2 mb-6">
        <button
          onClick={() => handleEraChange('all')}
          className={`text-xs px-3 py-1.5 rounded-full border transition-colors ${
            selectedEra === 'all'
              ? 'bg-stone-800 text-white border-stone-800'
              : 'bg-white text-stone-600 border-stone-200 hover:border-stone-400'
          }`}
        >
          {locale === 'en' ? 'All' : '全部'} ({totalCount})
        </button>
        {eraStats.map((era) => (
          <button
            key={era.key}
            onClick={() => handleEraChange(era.key)}
            className={`text-xs px-3 py-1.5 rounded-full border transition-colors ${
              selectedEra === era.key
                ? 'bg-stone-800 text-white border-stone-800'
                : 'bg-white text-stone-600 border-stone-200 hover:border-stone-400'
            }`}
          >
            {locale === 'en' ? era.labelEn : era.label} ({era.count})
          </button>
        ))}
      </div>

      {/* Loading state */}
      {loading && (
        <div className="flex items-center justify-center py-16">
          <div className="animate-spin w-6 h-6 border-2 border-stone-300 border-t-stone-600 rounded-full" />
        </div>
      )}

      {/* Error state */}
      {error && (
        <EmptyState
          title={locale === 'en' ? 'Failed to load' : '加载失败'}
          description={error}
        />
      )}

      {/* Empty state */}
      {!loading && !error && people.length === 0 && (
        <EmptyState title={t.parallel.noData} description="" />
      )}

      {/* People grid */}
      {!loading && !error && people.length > 0 && (
        <>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {people.map((person) => (
              <PersonCard key={person.id} person={person} regions={regions} />
            ))}
          </div>

          {/* Pagination */}
          {totalPages > 1 && (
            <div className="flex items-center justify-center gap-4 mt-8 pb-8">
              <button
                onClick={() => setPage((p) => Math.max(1, p - 1))}
                disabled={page <= 1}
                className="text-xs px-3 py-1.5 rounded border border-stone-200 bg-white text-stone-600 hover:border-stone-400 disabled:opacity-30 disabled:cursor-not-allowed transition-colors"
              >
                {locale === 'en' ? '← Previous' : '← 上一页'}
              </button>
              <span className="text-xs text-stone-500">
                {page} / {totalPages}
              </span>
              <button
                onClick={() => setPage((p) => Math.min(totalPages, p + 1))}
                disabled={page >= totalPages}
                className="text-xs px-3 py-1.5 rounded border border-stone-200 bg-white text-stone-600 hover:border-stone-400 disabled:opacity-30 disabled:cursor-not-allowed transition-colors"
              >
                {locale === 'en' ? 'Next →' : '下一页 →'}
              </button>
            </div>
          )}
        </>
      )}
    </div>
  );
}
