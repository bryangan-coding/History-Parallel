'use client';

import React, { createContext, useContext, useState, useCallback, useEffect, useRef, useMemo } from 'react';
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

// Split context into two parts to minimize re-renders:
// 1. LocaleContext — only changes when locale actually changes
// 2. TranslationContext — dictionary changes with locale
// Most components only need locale, not the full dictionary

interface LocaleContextValue {
  locale: Locale;
  setLocale: (locale: Locale) => void;
}

interface TranslationContextValue {
  t: Dictionary;
  toScript: (text: string | undefined | null) => string;
}

const LocaleContext = createContext<LocaleContextValue | null>(null);
const TranslationContext = createContext<TranslationContextValue | null>(null);

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
  const converterRef = useRef<((text: string) => string) | null>(null);

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

  // Memoize toScript — only recreate when locale actually changes
  const toScript = useCallback(
    (text: string | undefined | null): string => {
      if (!text || locale !== 'zh-TW') return text ?? '';
      if (!converterRef.current) return text;
      return converterRef.current(text);
    },
    [locale]
  );

  // Stable locale context value — only changes when locale changes
  const localeValue = useMemo(() => ({
    locale,
    setLocale,
  }), [locale, setLocale]);

  // Translation context value — changes with locale
  const translationValue = useMemo(() => ({
    t,
    toScript,
  }), [t, toScript]);

  return (
    <LocaleContext.Provider value={localeValue}>
      <TranslationContext.Provider value={translationValue}>
        {children}
      </TranslationContext.Provider>
    </LocaleContext.Provider>
  );
}

/** Get just the locale and setLocale — minimal re-render impact */
export function useLocale(): LocaleContextValue & TranslationContextValue {
  const localeCtx = useContext(LocaleContext);
  const translationCtx = useContext(TranslationContext);
  if (!localeCtx || !translationCtx) {
    throw new Error('useLocale must be used within a LocaleProvider');
  }
  return { ...localeCtx, ...translationCtx };
}

/** Get only the locale string — avoids re-render when t/toScript change */
export function useLocaleOnly(): Locale {
  const ctx = useContext(LocaleContext);
  if (!ctx) {
    throw new Error('useLocaleOnly must be used within a LocaleProvider');
  }
  return ctx.locale;
}
