import Link from 'next/link';
import { ArrowRight } from 'lucide-react';
import { useLocale } from '@/i18n/LocaleProvider';

interface ExamplePrompt {
  label: string;
  labelEn?: string;
  searchQuery: string;
  link?: string;
  description?: string;
  descriptionEn?: string;
}

const MOCK_PROMPTS: ExamplePrompt[] = [
  {
    label: '苏轼被贬黄州时，欧洲正在发生什么？',
    labelEn: 'When Su Shi was exiled to Huangzhou, what was happening in Europe?',
    searchQuery: '苏轼',
    link: '/people/su-shi',
    description: '1080年 · 诺曼征服后的欧洲',
    descriptionEn: '1080 · Post-Conquest Europe',
  },
  {
    label: '玄奘西行时，拜占庭帝国处于什么阶段？',
    labelEn: 'When Xuanzang journeyed west, what stage was the Byzantine Empire in?',
    searchQuery: '玄奘',
    description: '627—645年 · 拜占庭希拉克略王朝',
    descriptionEn: '627–645 · Byzantine Heraclian Dynasty',
  },
  {
    label: '达·芬奇创作时期，中国处于哪个朝代？',
    labelEn: 'During Leonardo da Vinci\'s career, which dynasty ruled China?',
    searchQuery: '达芬奇',
    description: '1452—1519年 · 明朝中期',
    descriptionEn: '1452–1519 · Mid-Ming Dynasty',
  },
  {
    label: '拿破仑称帝时，东亚正在发生什么？',
    labelEn: 'When Napoleon became Emperor, what was happening in East Asia?',
    searchQuery: '拿破仑',
    description: '1804年 · 清朝嘉庆年间',
    descriptionEn: '1804 · Qing Jiaqing Era',
  },
];

export default function ExamplePromptCard({
  prompt,
}: {
  prompt: ExamplePrompt;
}) {
  const { locale } = useLocale();
  const href = prompt.link ?? `/search?q=${encodeURIComponent(prompt.searchQuery)}`;
  const displayLabel = (locale === 'en' && prompt.labelEn) ? prompt.labelEn : prompt.label;
  const displayDesc = (locale === 'en' && prompt.descriptionEn) ? prompt.descriptionEn : prompt.description;

  return (
    <Link
      href={href}
      className="block p-4 rounded-xl border border-stone-200 bg-white hover:border-stone-400 hover:shadow-sm transition-all group"
    >
      <div className="flex items-start gap-3">
        <ArrowRight className="w-4 h-4 text-stone-300 mt-0.5 shrink-0 group-hover:text-stone-500 transition-colors" />
        <div>
          <p className="text-sm text-stone-700 group-hover:text-stone-900 transition-colors leading-relaxed">
            {displayLabel}
          </p>
          {displayDesc && (
            <p className="mt-1 text-xs text-stone-400">{displayDesc}</p>
          )}
        </div>
      </div>
    </Link>
  );
}

export { MOCK_PROMPTS };
