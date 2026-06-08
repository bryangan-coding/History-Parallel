'use client';

import Link from 'next/link';
import { LocaleProvider, useLocale } from '@/i18n/LocaleProvider';
import { FeedbackButton } from '@/components/ui/FeedbackButton';
import { localeLabel, nextLocale, localeTitle } from '@/i18n/useTextScript';

function LangToggle() {
  const { locale, setLocale } = useLocale();

  return (
    <button
      onClick={() => setLocale(nextLocale(locale))}
      className="relative inline-flex items-center gap-1 text-xs font-medium 
                 px-2.5 py-1.5 rounded-full border border-stone-200
                 bg-stone-50 hover:bg-stone-100 cursor-pointer select-none
                 text-stone-500 hover:text-stone-800 
                 transition-all duration-200 active:scale-95
                 focus:outline-none focus:ring-2 focus:ring-stone-300 focus:ring-offset-1"
      title={localeTitle(locale)}
    >
      {/* Three-segment indicator */}
      <span className="flex items-center gap-0.5">
        <span className={`w-1 h-1 rounded-full transition-colors duration-300 ${
          locale === 'zh-CN' ? 'bg-amber-500' : 'bg-stone-300'
        }`} />
        <span className={`w-1 h-1 rounded-full transition-colors duration-300 ${
          locale === 'zh-TW' ? 'bg-amber-500' : 'bg-stone-300'
        }`} />
        <span className={`w-1 h-1 rounded-full transition-colors duration-300 ${
          locale === 'en' ? 'bg-amber-500' : 'bg-stone-300'
        }`} />
      </span>
      <span className="tabular-nums min-w-[1.5rem] text-center font-semibold">
        {localeLabel(locale)}
      </span>
    </button>
  );
}

function Header() {
  const { locale, t } = useLocale();

  return (
    <header className="border-b border-stone-200 bg-white sticky top-0 z-50">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 h-14 flex items-center justify-between">
        <Link
          href="/"
          className="text-lg font-bold text-stone-900 tracking-tight hover:text-stone-700 transition-colors"
        >
          {t.app.title}
        </Link>
        <div className="flex items-center gap-4">
          <nav className="flex items-center gap-4 text-sm text-stone-500">
            <Link
              href="/compare"
              className="hover:text-stone-800 transition-colors"
            >
              {locale === 'en' ? 'Compare' : '人物对比'}
            </Link>
            <Link
              href="/relationships"
              className="hover:text-stone-800 transition-colors"
            >
              {t.nav.relationships}
            </Link>
            <Link
              href="/civilizations"
              className="hover:text-stone-800 transition-colors"
            >
              {t.nav.civilizations}
            </Link>
            <Link
              href="/about-data"
              className="hover:text-stone-800 transition-colors"
            >
              {t.nav.aboutData}
            </Link>
          </nav>
          <LangToggle />
        </div>
      </div>
    </header>
  );
}

function Footer() {
  const { t } = useLocale();
  return (
    <footer className="border-t border-stone-200 bg-white py-6 mt-auto">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 text-center text-xs text-stone-400">
        <p>{t.app.footer}</p>
      </div>
    </footer>
  );
}

export function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <LocaleProvider>
      <Header />
      <main className="flex-1">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 py-8">{children}</div>
      </main>
      <Footer />
      <FeedbackButton />
    </LocaleProvider>
  );
}
