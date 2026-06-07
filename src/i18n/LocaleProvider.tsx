'use client';

import React, { createContext, useContext, useState, useCallback, useEffect, useRef } from 'react';
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

// ---- Text script conversion (简→繁) ----
let _converterPromise: Promise<(text: string) => string> | null = null;
let _converterFn: ((text: string) => string) | null = null;
const _scriptCache = new Map<string, string>();
const MAX_CACHE = 3000;

async function loadConverter() {
  if (_converterFn) return _converterFn;
  if (_converterPromise) return _converterPromise;
  _converterPromise = (async () => {
    const { Converter } = await import('opencc-js');
    _converterFn = Converter({ from: 'cn', to: 'twp' });
    return _converterFn!;
  })();
  return _converterPromise;
}

function convertToTraditional(text: string): string {
  if (!_converterFn) return text;
  const cached = _scriptCache.get(text);
  if (cached) return cached;
  try {
    const result = _converterFn(text);
    if (_scriptCache.size >= MAX_CACHE) {
      const first = _scriptCache.keys().next().value;
      if (first) _scriptCache.delete(first);
    }
    _scriptCache.set(text, result);
    return result;
  } catch {
    return text;
  }
}

// Preload converter on first import
if (typeof window !== 'undefined') {
  loadConverter().catch(() => {});
}

interface LocaleContextValue {
  locale: Locale;
  t: Dictionary;
  setLocale: (locale: Locale) => void;
  /** Convert Chinese text to the appropriate script for current locale (简/繁) */
  toScript: (text: string | undefined | null) => string;
}

const LocaleContext = createContext<LocaleContextValue | null>(null);

function isLocale(v: string): v is Locale {
  return v === 'zh-CN' || v === 'zh-TW' || v === 'en';
}

function readCookieLocale(): Locale {
  if (typeof document === 'undefined') return 'zh-CN';
  const match = document.cookie.match(new RegExp(`(?:^|; )${LOCALE_COOKIE}=([^;]*)`));
  const val = match?.[1];
  if (!val || val === 'zh') return 'zh-CN';
  return isLocale(val) ? val : 'zh-CN';
}

function setLocaleCookie(locale: Locale) {
  document.cookie = `${LOCALE_COOKIE}=${locale};path=/;max-age=${60 * 60 * 24 * 365};SameSite=Lax`;
}

export function LocaleProvider({ children }: { children: React.ReactNode }) {
  const [locale, _setLocale] = useState<Locale>('zh-CN');

  useEffect(() => {
    const cookieLocale = readCookieLocale();
    if (cookieLocale !== 'zh-CN') {
      // eslint-disable-next-line react-hooks/set-state-in-effect
      _setLocale(cookieLocale);
    }
  }, []);

  const setLocale = useCallback((newLocale: Locale) => {
    _setLocale(newLocale);
    setLocaleCookie(newLocale);
  }, []);

  const t = dictionaries[locale];

  const toScript = useCallback(
    (text: string | undefined | null): string => {
      if (!text || locale !== 'zh-TW') return text ?? '';
      return convertToTraditional(text);
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
