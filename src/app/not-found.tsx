'use client';

import Link from 'next/link';
import { useLocale } from '@/i18n/LocaleProvider';

export default function NotFound() {
  const { t } = useLocale();

  return (
    <div className="min-h-[50vh] flex flex-col items-center justify-center text-center">
      <p className="text-6xl font-bold text-stone-200">404</p>
      <h2 className="mt-4 text-xl font-semibold text-stone-700">
        {t.common.notFound}
      </h2>
      <p className="mt-2 text-stone-400 max-w-md">
        {t.common.notFoundDesc}
      </p>
      <Link
        href="/"
        className="mt-6 inline-flex items-center px-4 py-2 rounded-lg bg-stone-900 text-white text-sm font-medium hover:bg-stone-800 transition-colors"
      >
        {t.common.backToHome}
      </Link>
    </div>
  );
}
