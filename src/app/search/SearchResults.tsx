'use client';

import { useState, useMemo, useEffect, useTransition } from 'react';
import { useSearchParams } from 'next/navigation';
import Link from 'next/link';
import { useLocale } from '@/i18n/LocaleProvider';
import SearchBox from '@/components/common/SearchBox';
import PageHeader from '@/components/common/PageHeader';
import EmptyState from '@/components/common/EmptyState';
import PersonCard from '@/components/cards/PersonCard';
import EventCard from '@/components/cards/EventCard';
import { searchData } from '@/data/server-actions';
import { formatYearRange } from '@/lib/date';
import { regionName, regionDescription } from '@/lib/types';
import { buildRegionMap } from '@/data/clientLookup';
import type { SearchResult, Region, Person, HistoricalEvent } from '@/lib/types';
import { Funnel } from 'lucide-react';

interface SearchPageClientProps {
  regions: Region[];
}

// Highlight matching text
function highlightText(text: string, query: string): React.ReactNode {
  if (!query.trim()) return text;
  const escaped = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  // Use 'i' flag without 'g' — global flag causes lastIndex issues with test()
  const regex = new RegExp(`(${escaped})`, 'i');
  const qLower = query.toLowerCase();
  const parts = text.split(regex);
  return parts.map((part, i) =>
    part.toLowerCase() === qLower ? (
      <mark key={i} className="bg-amber-100 text-amber-900 rounded px-0.5">
        {part}
      </mark>
    ) : (
      part
    )
  );
}

// Filter configurations
const ERA_FILTERS = [
  { value: 'all', label: '全部时代', labelEn: 'All Eras' },
  { value: 'ancient', label: '古代（-3000 至 500）', labelEn: 'Ancient (-3000 to 500)', min: -3000, max: 500 },
  { value: 'medieval', label: '中世纪（501 至 1500）', labelEn: 'Medieval (501-1500)', min: 501, max: 1500 },
  { value: 'renaissance', label: '文艺复兴/近代早期（1501-1800）', labelEn: 'Renaissance/Early Modern (1501-1800)', min: 1501, max: 1800 },
  { value: 'modern', label: '近现代（1801+）', labelEn: 'Modern (1801+)', min: 1801, max: Infinity },
] as const;

const TOP_REGION_IDS = ['asia', 'europe', 'africa', 'americas'];

const SORT_OPTIONS = [
  { value: 'relevance', label: '按相关度', labelEn: 'By Relevance' },
  { value: 'year-asc', label: '按年份（早→晚）', labelEn: 'By Year (Asc)' },
  { value: 'year-desc', label: '按年份（晚→早）', labelEn: 'By Year (Desc)' },
  { value: 'name', label: '按名称', labelEn: 'By Name' },
];

const SEARCH_SUGGESTIONS = [
  { query: '苏轼', label: '苏轼', labelEn: 'Su Shi' },
  { query: '汉武帝', label: '汉武帝', labelEn: 'Emperor Wu' },
  { query: '凯撒', label: '凯撒', labelEn: 'Caesar' },
  { query: '1066', label: '1066年', labelEn: 'Year 1066' },
  { query: '诺曼', label: '诺曼征服', labelEn: 'Norman Conquest' },
  { query: '孔子', label: '孔子', labelEn: 'Confucius' },
];

export default function SearchResults({ regions }: SearchPageClientProps) {
  const searchParams = useSearchParams();
  const { locale, t, toScript } = useLocale();
  const query = searchParams.get('q') ?? '';

  const [eraFilter, setEraFilter] = useState<string>('all');
  const [regionFilter, setRegionFilter] = useState<string>('all');
  const [sortOption, setSortOption] = useState<string>('relevance');
  const [showAdvanced, setShowAdvanced] = useState(false);
  const [yearFrom, setYearFrom] = useState('');
  const [yearTo, setYearTo] = useState('');
  const [showFilters, setShowFilters] = useState(false);

  // Server action for search — avoids importing mockData in client
  const [isPending, startTransition] = useTransition();
  const [rawResults, setRawResults] = useState<SearchResult>({ people: [], events: [], regions: [], yearMatches: [] });

  // Trigger search via Server Action when query changes — useEffect with cancellation
  useEffect(() => {
    if (!query) {
      setRawResults({ people: [], events: [], regions: [], yearMatches: [] });
      return;
    }
    let cancelled = false;
    startTransition(async () => {
      try {
        const result = await searchData(query);
        if (!cancelled) setRawResults(result);
      } catch {
        if (!cancelled) setRawResults({ people: [], events: [], regions: [], yearMatches: [] });
      }
    });
    return () => { cancelled = true; };
  }, [query, startTransition]);

  const regionMap = useMemo(() => buildRegionMap(regions), [regions]);

  // Apply filters
  const results = useMemo(() => {
    let filtered = { ...rawResults };

    // Era filter for people
    if (eraFilter !== 'all') {
      const era = ERA_FILTERS.find((e) => e.value === eraFilter);
      if (era && 'min' in era && 'max' in era) {
        filtered = {
          ...filtered,
          people: filtered.people.filter((p) => {
            const year = p.birthYear ?? p.deathYear ?? 0;
            return year >= era.min && year <= era.max;
          }),
          events: filtered.events.filter((e) => {
            const year = e.startYear ?? 0;
            return year >= era.min && year <= era.max;
          }),
        };
      }
    }

    // Region filter
    if (regionFilter !== 'all') {
      filtered = {
        ...filtered,
        people: filtered.people.filter((p) => {
          const region = p.regionId ? regionMap.get(p.regionId) : null;
          const topId = region?.parentRegionId || region?.id;
          return topId === regionFilter;
        }),
        events: filtered.events.filter((e) => {
          const region = e.regionId ? regionMap.get(e.regionId) : null;
          const topId = region?.parentRegionId || region?.id;
          return topId === regionFilter;
        }),
      };
    }

    // Year range filter
    if (yearFrom || yearTo) {
      const from = yearFrom ? parseInt(yearFrom) : -Infinity;
      const to = yearTo ? parseInt(yearTo) : Infinity;
      filtered = {
        ...filtered,
        people: filtered.people.filter((p) => {
          const year = p.birthYear ?? p.deathYear ?? 0;
          return year >= from && year <= to;
        }),
        events: filtered.events.filter((e) => {
          const year = e.startYear ?? 0;
          return year >= from && year <= to;
        }),
      };
    }

    // Sort
    if (sortOption !== 'relevance') {
      const sortPeople = [...filtered.people];
      const sortEvents = [...filtered.events];

      if (sortOption === 'year-asc') {
        sortPeople.sort((a, b) => (a.birthYear ?? 0) - (b.birthYear ?? 0));
        sortEvents.sort((a, b) => (a.startYear ?? 0) - (b.startYear ?? 0));
      } else if (sortOption === 'year-desc') {
        sortPeople.sort((a, b) => (b.birthYear ?? 0) - (a.birthYear ?? 0));
        sortEvents.sort((a, b) => (b.startYear ?? 0) - (a.startYear ?? 0));
      } else if (sortOption === 'name') {
        sortPeople.sort((a, b) => a.name.localeCompare(b.name, 'zh'));
        sortEvents.sort((a, b) => a.title.localeCompare(b.title, 'zh'));
      }

      filtered = { ...filtered, people: sortPeople, events: sortEvents };
    }

    return filtered;
  }, [rawResults, eraFilter, regionFilter, sortOption, yearFrom, yearTo, regionMap]);

  const hasResults =
    results.people.length > 0 ||
    results.events.length > 0 ||
    results.regions.length > 0 ||
    results.yearMatches.length > 0;

  const totalResults =
    results.people.length + results.events.length + results.regions.length;

  // Get top-level regions for filter
  const topRegions = useMemo(() => {
    return TOP_REGION_IDS.map((id) => {
      const region = regionMap.get(id);
      return region ? { id, name: regionName(region, locale) } : null;
    }).filter(Boolean) as { id: string; name: string }[];
  }, [locale, regionMap]);

  // Active filter count
  const activeFilterCount =
    (eraFilter !== 'all' ? 1 : 0) +
    (regionFilter !== 'all' ? 1 : 0) +
    (yearFrom || yearTo ? 1 : 0);

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
      <SearchBox defaultValue={query} placeholder={t.search.searchPlaceholder} className="mb-4" />

      {/* Loading indicator */}
      {isPending && (
        <div className="flex items-center gap-2 mb-4 text-sm text-stone-400">
          <div className="animate-spin w-4 h-4 border-2 border-stone-300 border-t-stone-600 rounded-full" />
          {locale === 'en' ? 'Searching...' : '搜索中...'}
        </div>
      )}

      {/* Result summary */}
      {query && hasResults && (
        <div className="flex items-center justify-between mb-4">
          <p className="text-sm text-stone-500">
            {locale === 'en'
              ? `${totalResults} results found`
              : `找到 ${totalResults} 条结果`}
            {results.people.length > 0 && (
              <span className="ml-2 text-stone-400">
                {locale === 'en' ? 'People' : '人物'}: {results.people.length}
              </span>
            )}
            {results.events.length > 0 && (
              <span className="ml-2 text-stone-400">
                {locale === 'en' ? 'Events' : '事件'}: {results.events.length}
              </span>
            )}
            {results.regions.length > 0 && (
              <span className="ml-2 text-stone-400">
                {locale === 'en' ? 'Regions' : '地区'}: {results.regions.length}
              </span>
            )}
          </p>
          <div className="flex items-center gap-2">
            <button
              onClick={() => setShowFilters(!showFilters)}
              className={`flex items-center gap-1 text-xs px-2 py-1 rounded border transition-colors ${
                showFilters || activeFilterCount > 0
                  ? 'border-stone-400 bg-stone-100 text-stone-800'
                  : 'border-stone-200 text-stone-500 hover:text-stone-800'
              }`}
            >
              <Funnel className="w-3 h-3" />
              {locale === 'en' ? 'Filters' : '筛选'}
              {activeFilterCount > 0 && (
                <span className="ml-1 w-4 h-4 rounded-full bg-stone-600 text-white text-[10px] flex items-center justify-center">
                  {activeFilterCount}
                </span>
              )}
            </button>
            <select
              value={sortOption}
              onChange={(e) => setSortOption(e.target.value)}
              className="text-xs border border-stone-200 rounded px-2 py-1 bg-white text-stone-600 focus:outline-none focus:border-stone-400"
            >
              {SORT_OPTIONS.map((opt) => (
                <option key={opt.value} value={opt.value}>
                  {locale === 'en' ? opt.labelEn : opt.label}
                </option>
              ))}
            </select>
          </div>
        </div>
      )}

      {/* Filter panel */}
      {showFilters && query && hasResults && (
        <div className="mb-4 p-4 border border-stone-200 rounded-xl bg-white space-y-3">
          <div className="flex flex-wrap gap-3">
            {/* Era filter chips */}
            <div>
              <span className="text-xs font-semibold text-stone-500 uppercase block mb-1.5">
                {locale === 'en' ? 'Era' : '时代'}
              </span>
              <div className="flex flex-wrap gap-1">
                {ERA_FILTERS.map((era) => (
                  <button
                    key={era.value}
                    onClick={() => setEraFilter(era.value)}
                    className={`text-xs px-2 py-1 rounded border transition-colors ${
                      eraFilter === era.value
                        ? 'border-stone-400 bg-stone-100 text-stone-800'
                        : 'border-stone-200 text-stone-500 hover:border-stone-300'
                    }`}
                  >
                    {locale === 'en' ? era.labelEn : era.label}
                  </button>
                ))}
              </div>
            </div>

            {/* Region filter */}
            <div>
              <span className="text-xs font-semibold text-stone-500 uppercase block mb-1.5">
                {locale === 'en' ? 'Region' : '地区'}
              </span>
              <div className="flex flex-wrap gap-1">
                <button
                  onClick={() => setRegionFilter('all')}
                  className={`text-xs px-2 py-1 rounded border transition-colors ${
                    regionFilter === 'all'
                      ? 'border-stone-400 bg-stone-100 text-stone-800'
                      : 'border-stone-200 text-stone-500 hover:border-stone-300'
                  }`}
                >
                  {locale === 'en' ? 'All' : '全部'}
                </button>
                {topRegions.map((r) => (
                  <button
                    key={r.id}
                    onClick={() => setRegionFilter(r.id)}
                    className={`text-xs px-2 py-1 rounded border transition-colors ${
                      regionFilter === r.id
                        ? 'border-stone-400 bg-stone-100 text-stone-800'
                        : 'border-stone-200 text-stone-500 hover:border-stone-300'
                    }`}
                  >
                    {r.name}
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Advanced search: year range */}
          <div>
            <button
              onClick={() => setShowAdvanced(!showAdvanced)}
              className="text-xs text-stone-500 hover:text-stone-800 transition-colors"
            >
              {showAdvanced
                ? locale === 'en'
                  ? '− Hide Advanced'
                  : '− 收起高级搜索'
                : locale === 'en'
                  ? '+ Advanced Search'
                  : '+ 高级搜索'}
            </button>
            {showAdvanced && (
              <div className="mt-2 flex flex-wrap gap-3">
                <div className="flex items-center gap-2">
                  <label className="text-xs text-stone-500">
                    {locale === 'en' ? 'Year:' : '年份：'}
                  </label>
                  <input
                    type="number"
                    value={yearFrom}
                    onChange={(e) => setYearFrom(e.target.value)}
                    placeholder={locale === 'en' ? 'From' : '起始'}
                    className="w-20 text-xs border border-stone-200 rounded px-2 py-1 focus:outline-none focus:border-stone-400"
                  />
                  <span className="text-xs text-stone-400">—</span>
                  <input
                    type="number"
                    value={yearTo}
                    onChange={(e) => setYearTo(e.target.value)}
                    placeholder={locale === 'en' ? 'To' : '结束'}
                    className="w-20 text-xs border border-stone-200 rounded px-2 py-1 focus:outline-none focus:border-stone-400"
                  />
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Empty state - no query */}
      {!query && (
        <div>
          <EmptyState
            title={t.search.noQueryTitle}
            description={t.search.noQueryDesc}
          />
          <div className="mt-4">
            <p className="text-xs font-semibold text-stone-400 uppercase tracking-wide mb-2">
              {locale === 'en' ? 'Try searching for:' : '试试搜索：'}
            </p>
            <div className="flex flex-wrap gap-2">
              {SEARCH_SUGGESTIONS.map((s) => (
                <Link
                  key={s.query}
                  href={`/search?q=${encodeURIComponent(s.query)}`}
                  className="text-xs px-3 py-1.5 rounded-full border border-stone-200 bg-white text-stone-600 hover:border-stone-400 hover:text-stone-900 transition-colors"
                >
                  {locale === 'en' ? s.labelEn : s.label}
                </Link>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Empty state - no results */}
      {query && !hasResults && !isPending && (
        <div>
          <EmptyState
            title={t.search.noResults.replace('{query}', query)}
            description={t.search.noResultsDesc}
          />
          <div className="mt-4">
            <p className="text-xs font-semibold text-stone-400 uppercase tracking-wide mb-2">
              {locale === 'en' ? 'Suggestions:' : '建议：'}
            </p>
            <ul className="text-sm text-stone-500 space-y-1 list-disc pl-5">
              <li>{locale === 'en' ? 'Try a different spelling or keyword' : '尝试不同的拼写或关键词'}</li>
              <li>{locale === 'en' ? 'Try a broader term (e.g., "China" instead of a dynasty name)' : '尝试更宽泛的词（如搜"中国"而不是朝代名）'}</li>
              <li>{locale === 'en' ? 'Search by year number (e.g., "1066")' : '用年份数字搜索（如"1066"）'}</li>
              <li>{locale === 'en' ? 'Try English if Chinese doesn\'t work' : '中文搜不到可以试试英文名'}</li>
            </ul>
          </div>
        </div>
      )}

      {/* Results */}
      {query && hasResults && (
        <div className="space-y-8">
          {/* People */}
          {results.people.length > 0 && (
            <section>
              <h2 className="text-sm font-semibold text-stone-500 uppercase tracking-wide mb-3">
                {t.search.sectionPeople} ({results.people.length})
              </h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                {results.people.map((person) => (
                  <div key={person.id} className="relative group">
                    <PersonCard person={person} regions={regions} />
                  </div>
                ))}
              </div>
            </section>
          )}

          {/* Events */}
          {results.events.length > 0 && (
            <section>
              <h2 className="text-sm font-semibold text-stone-500 uppercase tracking-wide mb-3">
                {t.search.sectionEvents} ({results.events.length})
              </h2>
              <div className="space-y-3">
                {results.events.map((event) => {
                  const region = event.regionId ? regionMap.get(event.regionId) : undefined;
                  return (
                    <EventCard
                      key={event.id}
                      event={event}
                      showParallelButton
                      region={region}
                    />
                  );
                })}
              </div>
            </section>
          )}

          {/* Regions */}
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
                      {highlightText(toScript(regionName(region, locale)), query)}
                    </h3>
                    {regionDescription(region, locale) && (
                      <p className="mt-1 text-sm text-stone-500 line-clamp-2">
                        {highlightText(toScript(regionDescription(region, locale)!), query)}
                      </p>
                    )}
                  </Link>
                ))}
              </div>
            </section>
          )}

          {/* Year matches */}
          {results.yearMatches.length > 0 && (
            <section>
              <h2 className="text-sm font-semibold text-stone-500 uppercase tracking-wide mb-3">
                {t.search.sectionYears} ({results.yearMatches.length})
              </h2>
              {results.yearMatches.map((ym) => (
                <div key={ym.year} className="mb-4">
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
                        {event.titleEn && locale === 'en' ? event.titleEn : toScript(event.title)}
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
