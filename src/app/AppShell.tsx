'use client';

import Link from 'next/link';
import { LocaleProvider, useLocale } from '@/i18n/LocaleProvider';

function Header() {
  const { locale, t, setLocale } = useLocale();

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
              href="/about-data"
              className="hover:text-stone-800 transition-colors"
            >
              {t.nav.aboutData}
            </Link>
          </nav>
          <button
            onClick={() => setLocale(locale === 'zh' ? 'en' : 'zh')}
            className="text-xs font-medium px-2 py-1 rounded border border-stone-200 text-stone-500 hover:text-stone-800 hover:border-stone-400 transition-colors"
            title={locale === 'zh' ? 'Switch to English' : '切换为中文'}
          >
            {locale === 'zh' ? 'EN' : '中'}
          </button>
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
    </LocaleProvider>
  );
}
