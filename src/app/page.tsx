import { people, regions } from '@/data/mockData';
import HomePageClient from './HomePageClient';
import type { Person } from '@/lib/types';

// Pre-compute stats server-side — only pass lightweight data to client
const publishedPeople = people.filter((p) => p.dataStatus === 'published');
const totalPublished = publishedPeople.length;

// Only pick a small featured subset for display on the homepage
const featuredPeople = publishedPeople.slice(0, 12);

export default function HomePage() {
  return (
    <HomePageClient
      totalPublished={totalPublished}
      featuredPeople={featuredPeople}
      regions={regions}
    />
  );
}
