import { people, events, regions, sources } from '@/data/mockData';
import { initData } from '@/data/helpers';
import HomePageClient from './HomePageClient';

// Initialize client-side helper data on server render
initData(people, events, regions, sources);
const publishedPeople = people.filter((p) => p.dataStatus === 'published');

export default function HomePage() {
  return <HomePageClient publishedPeople={publishedPeople} regions={regions} />;
}
