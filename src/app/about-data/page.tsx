'use client';

import { useLocale } from '@/i18n/LocaleProvider';
import PageHeader from '@/components/common/PageHeader';

export default function AboutDataPage() {
  const { t } = useLocale();

  return (
    <div className="max-w-2xl">
      <PageHeader title={t.about.title} subtitle={t.about.subtitle} />

      <div className="prose prose-stone max-w-none space-y-6">
        <section>
          <h2 className="text-lg font-semibold text-stone-800 mt-8 mb-3">
            {t.about.dataSources}
          </h2>
          <p className="text-stone-600 leading-relaxed">{t.about.dataSourcesText}</p>
          <p className="text-stone-600 leading-relaxed mt-2">{t.about.dataSourcesText2}</p>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-stone-800 mt-8 mb-3">
            {t.about.dataStructure}
          </h2>
          <ul className="list-disc pl-5 text-stone-600 space-y-1">
            <li><strong>{t.about.itemRegion}</strong></li>
            <li><strong>{t.about.itemPerson}</strong></li>
            <li><strong>{t.about.itemEvent}</strong></li>
            <li><strong>{t.about.itemSource}</strong></li>
          </ul>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-stone-800 mt-8 mb-3">
            {t.about.license}
          </h2>
          <div className="space-y-3">
            <div className="p-4 rounded-lg border border-stone-200 bg-white">
              <h3 className="font-medium text-stone-800">{t.about.licenseCode}</h3>
              <p className="text-sm text-stone-500 mt-1">{t.about.licenseCodeDesc}</p>
            </div>
            <div className="p-4 rounded-lg border border-stone-200 bg-white">
              <h3 className="font-medium text-stone-800">{t.about.licenseData}</h3>
              <p className="text-sm text-stone-500 mt-1">{t.about.licenseDataDesc}</p>
            </div>
            <div className="p-4 rounded-lg border border-stone-200 bg-white">
              <h3 className="font-medium text-stone-800">{t.about.licenseBrand}</h3>
              <p className="text-sm text-stone-500 mt-1">{t.about.licenseBrandDesc}</p>
            </div>
          </div>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-stone-800 mt-8 mb-3">
            {t.about.coverage}
          </h2>
          <p className="text-stone-600 leading-relaxed">{t.about.coverageDesc}</p>
          <ul className="list-disc pl-5 text-stone-600 space-y-1 mt-2">
            {t.about.coverageItems.map((item, i) => (
              <li key={i}>{item}</li>
            ))}
          </ul>
        </section>

        <section>
          <h2 className="text-lg font-semibold text-stone-800 mt-8 mb-3">
            {t.about.roadmap}
          </h2>
          <ol className="list-decimal pl-5 text-stone-600 space-y-1">
            {t.about.roadmapItems.map((item, i) => (
              <li key={i}>{item}</li>
            ))}
          </ol>
        </section>
      </div>
    </div>
  );
}
