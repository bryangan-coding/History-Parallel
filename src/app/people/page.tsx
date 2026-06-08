import { people } from '@/data/mockData';
import PeoplePageClient from './PeoplePageClient';

// Pre-compute era stats only — return lightweight metadata, not full data
// IMPORTANT: boundaries must match ERA_MAP in src/app/api/data/people/route.ts
const published = people.filter((p) => p.dataStatus === 'published');

interface EraGroupStat {
  key: string;
  label: string;
  labelEn: string;
  count: number;
  minYear: number;
  maxYear: number;
}

const eraStats: EraGroupStat[] = [
  {
    key: 'ancient',
    label: '公元前',
    labelEn: 'BCE',
    count: published.filter((p) => (p.birthYear ?? 0) < 0).length,
    minYear: -3000,
    maxYear: 0,
  },
  {
    key: 'earlyMedieval',
    label: '1–10 世纪',
    labelEn: '1st–10th Century',
    count: published.filter((p) => {
      const by = p.birthYear ?? 0;
      return by >= 1 && by < 960;
    }).length,
    minYear: 1,
    maxYear: 960,
  },
  {
    key: 'song',
    label: '宋（960–1279）',
    labelEn: 'Song (960–1279)',
    count: published.filter((p) => {
      const by = p.birthYear ?? 0;
      return by >= 960 && by < 1279;
    }).length,
    minYear: 960,
    maxYear: 1279,
  },
  {
    key: 'postSong',
    label: '宋后–明（1279–1500）',
    labelEn: 'Post-Song to Ming (1279–1500)',
    count: published.filter((p) => {
      const by = p.birthYear ?? 0;
      return by >= 1279 && by < 1500;
    }).length,
    minYear: 1279,
    maxYear: 1500,
  },
  {
    key: 'modern',
    label: '1500 年后',
    labelEn: 'After 1500',
    count: published.filter((p) => (p.birthYear ?? 0) >= 1500).length,
    minYear: 1500,
    maxYear: 3000,
  },
];

export default function PeoplePage() {
  return (
    <PeoplePageClient totalCount={published.length} eraStats={eraStats} />
  );
}
