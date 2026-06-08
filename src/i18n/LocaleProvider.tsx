'use client';

import React, { createContext, useContext, useState, useCallback, useEffect } from 'react';
import type { Locale } from '@/lib/types';
import type { Dictionary } from './dictionaries/zh';
import { zh } from './dictionaries/zh';
import { en } from './dictionaries/en';

const LOCALE_COOKIE = 'hp-locale';

const dictionaries: Record<Locale, Dictionary> = {
  'zh-CN': zh,
  'zh-TW': zh,
  en,
};

interface LocaleContextValue {
  locale: Locale;
  t: Dictionary;
  setLocale: (locale: Locale) => void;
  toScript: (text: string | undefined | null) => string;
}

const LocaleContext = createContext<LocaleContextValue | null>(null);

function isLocale(v: string): v is Locale {
  return v === 'zh-CN' || v === 'zh-TW' || v === 'en';
}

function readCookieLocale(): Locale {
  if (typeof document === 'undefined') return 'zh-CN';
  try {
    const match = document.cookie.match(new RegExp(`(?:^|; )${LOCALE_COOKIE}=([^;]*)`));
    const val = match?.[1];
    if (!val || val === 'zh') return 'zh-CN';
    return isLocale(val) ? val : 'zh-CN';
  } catch {
    return 'zh-CN';
  }
}

function setCookie(locale: Locale) {
  try {
    document.cookie = `${LOCALE_COOKIE}=${locale};path=/;max-age=${60 * 60 * 24 * 365};SameSite=Lax`;
  } catch { /* ignore */ }
}

export function LocaleProvider({ children }: { children: React.ReactNode }) {
  const [locale, setLocaleState] = useState<Locale>('zh-CN');
  const [converterReady, setConverterReady] = useState(false);
  const converterRef = React.useRef<((text: string) => string) | null>(null);

  // Read persisted locale on mount
  useEffect(() => {
    const cookie = readCookieLocale();
    if (cookie !== 'zh-CN') {
      setLocaleState(cookie);
    }
  }, []);

  // Load converter lazily
  useEffect(() => {
    let cancelled = false;
    import('opencc-js')
      .then((mod) => {
        if (!cancelled) {
          const Converter = mod.Converter || mod.default?.Converter;
          if (Converter) {
            converterRef.current = Converter({ from: 'cn', to: 'twp' });
          }
          setConverterReady(true);
        }
      })
      .catch(() => {
        if (!cancelled) setConverterReady(true);
      });
    return () => { cancelled = true; };
  }, []);

  const setLocale = useCallback((newLocale: Locale) => {
    setLocaleState(newLocale);
    setCookie(newLocale);
  }, []);

  const t = dictionaries[locale];

  const toScript = useCallback(
    (text: string | undefined | null): string => {
      if (!text || locale !== 'zh-TW') return text ?? '';
      if (!converterRef.current) return text;
      return converterRef.current(text);
    },
    [locale]
  );

  return (
    <LocaleContext.Provider value={{ locale, t, setLocale, toScript }}>
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
