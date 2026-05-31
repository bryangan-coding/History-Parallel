import { people, events, regions, sources } from '@/data/mockData';
import { initData } from '@/data/helpers';
import PeoplePageClient from './PeoplePageClient';

initData(people, events, regions, sources);
const published = people.filter((p) => p.dataStatus === 'published');

export default function PeoplePage() {
  return <PeoplePageClient published={published} regions={regions} />;
}
