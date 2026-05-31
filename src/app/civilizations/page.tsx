'use client';

import { useLocale } from '@/i18n/LocaleProvider';
import CivilizationTimeline from '@/components/parallel/CivilizationTimeline';

export default function CivilizationsPage() {
  const { locale } = useLocale();

  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-bold text-stone-900">
          {locale === 'en' ? 'Civilization Timeline' : '文明时间轴'}
        </h1>
        <p className="mt-1 text-sm text-stone-500">
          {locale === 'en'
            ? 'Compare the rise and fall of major world civilizations side by side'
            : '横向对比世界各大文明的兴衰起落'}
        </p>
      </div>
      <CivilizationTimeline />
    </div>
  );
}
