'use client';

import Link from 'next/link';
import { useLocale } from '@/i18n/LocaleProvider';
import SearchBox from '@/components/common/SearchBox';
import PersonCard from '@/components/cards/PersonCard';
import ExamplePromptCard, {
  MOCK_PROMPTS,
} from '@/components/cards/ExamplePromptCard';
import { people } from '@/data/mockData';

export default function HomePage() {
  const { locale, t } = useLocale();
  const publishedPeople = people.filter((p) => p.dataStatus === 'published');

  return (
    <div className="min-h-[calc(100vh-10rem)] flex flex-col items-center justify-center">
      {/* Hero */}
      <div className="text-center max-w-2xl mx-auto">
        <h1 className="text-4xl sm:text-5xl font-bold text-stone-900 tracking-tight">
          {t.home.heroTitle}
        </h1>
        <p className="mt-3 text-lg text-stone-500">
          {t.home.heroSubtitle}
        </p>
      </div>

      {/* Search */}
      <div className="mt-10 w-full max-w-xl mx-auto">
        <SearchBox large placeholder={t.home.searchPlaceholder} />
      </div>

      {/* Example prompts */}
      <div className="mt-8 w-full max-w-xl mx-auto">
        <p className="text-xs text-stone-400 font-medium uppercase tracking-wide mb-3">
          {t.home.exampleTitle}
        </p>
        <div className="space-y-2">
          {MOCK_PROMPTS.map((prompt) => (
            <ExamplePromptCard key={prompt.label} prompt={prompt} />
          ))}
        </div>
      </div>

      {/* Entry cards */}
      <div className="mt-12 grid grid-cols-1 sm:grid-cols-3 gap-4 w-full max-w-3xl mx-auto">
        <Link
          href="/people"
          className="group flex flex-col items-center p-6 rounded-xl border border-stone-200 bg-white hover:border-stone-400 hover:shadow-sm transition-all text-center"
        >
          <div className="w-10 h-10 rounded-lg bg-stone-100 flex items-center justify-center mb-3 group-hover:bg-stone-200 transition-colors">
            <svg
              className="w-5 h-5 text-stone-500"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={1.5}
                d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"
              />
            </svg>
          </div>
          <h3 className="text-sm font-semibold text-stone-700">{t.home.exploreByPerson}</h3>
          <p className="mt-1 text-xs text-stone-400">{publishedPeople.length} {locale === 'en' ? 'figures' : '位人物'}</p>
        </Link>

        <Link
          href="/parallel?year=1400&range=2000"
          className="group flex flex-col items-center p-6 rounded-xl border border-stone-200 bg-white hover:border-stone-400 hover:shadow-sm transition-all text-center"
        >
          <div className="w-10 h-10 rounded-lg bg-stone-100 flex items-center justify-center mb-3 group-hover:bg-stone-200 transition-colors">
            <svg
              className="w-5 h-5 text-stone-500"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={1.5}
                d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </div>
          <h3 className="text-sm font-semibold text-stone-700">{t.home.exploreByYear}</h3>
          <p className="mt-1 text-xs text-stone-400">{locale === 'en' ? '221 BCE – 1840 CE' : '公元前 221 年 – 公元 1840 年'}</p>
        </Link>

        <Link
          href="/parallel?year=1080&range=2000"
          className="group flex flex-col items-center p-6 rounded-xl border border-stone-200 bg-white hover:border-stone-400 hover:shadow-sm transition-all text-center"
        >
          <div className="w-10 h-10 rounded-lg bg-stone-100 flex items-center justify-center mb-3 group-hover:bg-stone-200 transition-colors">
            <svg
              className="w-5 h-5 text-stone-500"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={1.5}
                d="M12.75 3.03v.568c0 .334.148.65.405.864l1.068.89c.442.369.535 1.01.216 1.49l-.51.766a2.25 2.25 0 01-1.161.886l-.143.048a1.107 1.107 0 00-.57 1.664c.369.555.169 1.307-.427 1.605L9 13.125l.423 1.059a.956.956 0 01-1.652.928l-.679-.906a1.125 1.125 0 00-1.906.172L4.5 15.75l-.612.153M12.75 3.031a9 9 0 00-8.862 12.872M12.75 3.031a9 9 0 016.69 14.036m0 0l-.177-.529A2.25 2.25 0 0017.128 15H16.5l-.324-.324a1.453 1.453 0 00-2.328.377l-.036.073a1.586 1.586 0 01-.982.816l-.99.282c-.55.157-.894.702-.8 1.267l.073.438c.08.474.49.821.97.821.846 0 1.598.376 2.063.977l.389.504c.22.287.524.497.875.568l.069.014z"
              />
            </svg>
          </div>
          <h3 className="text-sm font-semibold text-stone-700">{t.home.exploreByRegion}</h3>
          <p className="mt-1 text-xs text-stone-400">{locale === 'en' ? '14 regions' : '14 个地区'}</p>
        </Link>
      </div>

      {/* Browse all people */}
      <div className="mt-16 w-full max-w-3xl mx-auto">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-sm font-semibold text-stone-500 uppercase tracking-wide">
            {t.home.exploreByPerson} ({publishedPeople.length})
          </h2>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          {publishedPeople.map((p) => (
            <PersonCard key={p.id} person={p} />
          ))}
        </div>
      </div>
    </div>
  );
}
