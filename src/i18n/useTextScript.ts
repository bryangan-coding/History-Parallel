'use client';

import type { Locale } from '@/lib/types';

/** Helper to get locale display label: 简 / 繁 / EN */
export function localeLabel(locale: Locale): string {
  switch (locale) {
    case 'zh-CN': return '简';
    case 'zh-TW': return '繁';
    case 'en': return 'EN';
  }
}

/** Helper to get the next locale: 简→繁→EN→简 */
export function nextLocale(locale: Locale): Locale {
  switch (locale) {
    case 'zh-CN': return 'zh-TW';
    case 'zh-TW': return 'en';
    case 'en': return 'zh-CN';
  }
}

/** Helper to get a human-readable locale title */
export function localeTitle(locale: Locale): string {
  switch (locale) {
    case 'zh-CN': return '简体中文';
    case 'zh-TW': return '繁體中文';
    case 'en': return 'English';
  }
}
