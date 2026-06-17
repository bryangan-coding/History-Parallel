import { totalPublished } from '@/data/stats';
import { regions } from '@/data/regions';
import featuredPeopleData from '@/data/_featured.json';
import type { Person } from '@/lib/types';
import HomePageClient from './HomePageClient';

const featuredPeople = featuredPeopleData as Person[];

export default function HomePage() {
  return (
    <HomePageClient
      totalPublished={totalPublished}
      featuredPeople={featuredPeople}
      regions={regions}
    />
  );
}
