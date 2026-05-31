'use client';

import React, { createContext, useContext, useState, useCallback, useEffect } from 'react';
import type { Locale } from '@/lib/types';
import type { Dictionary } from './dictionaries/zh';
import { zh } from './dictionaries/zh';
import { en } from './dictionaries/en';

const LOCALE_COOKIE = 'hp-locale';

const dictionaries: Record<Locale, Dictionary> = { zh, en };

interface LocaleContextValue {
  locale: Locale;
  t: Dictionary;
  setLocale: (locale: Locale) => void;
}

const LocaleContext = createContext<LocaleContextValue | null>(null);

function readCookieLocale(): Locale {
  if (typeof document === 'undefined') return 'zh';
  const match = document.cookie.match(new RegExp(`(?:^|; )${LOCALE_COOKIE}=([^;]*)`));
  return match?.[1] === 'en' ? 'en' : 'zh';
}

function setLocaleCookie(locale: Locale) {
  document.cookie = `${LOCALE_COOKIE}=${locale};path=/;max-age=${60 * 60 * 24 * 365};SameSite=Lax`;
}

export function LocaleProvider({ children }: { children: React.ReactNode }) {
  // Always start with 'zh' for SSR compatibility
  const [locale, _setLocale] = useState<Locale>('zh');

  // Read cookie after mount to avoid hydration mismatch
  useEffect(() => {
    const cookieLocale = readCookieLocale();
    if (cookieLocale !== 'zh') {
      // eslint-disable-next-line react-hooks/set-state-in-effect -- syncing with external system (cookie)
      _setLocale(cookieLocale);
    }
  }, []);

  const setLocale = useCallback((newLocale: Locale) => {
    _setLocale(newLocale);
    setLocaleCookie(newLocale);
  }, []);

  const t = dictionaries[locale];

  return (
    <LocaleContext.Provider value={{ locale, t, setLocale }}>
      {children}
    </LocaleContext.Provider>
  );
}

export function useLocale(): LocaleContextValue {
  const ctx = useContext(LocaleContext);
  if (!ctx) {
    throw new Error('useLocale must be used within a LocaleProvider');
  }
  return ctx;
}
