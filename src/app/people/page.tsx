import { totalPublished, eraStats } from '@/data/stats';
import PeoplePageClient from './PeoplePageClient';

export default function PeoplePage() {
  return (
    <PeoplePageClient totalCount={totalPublished} eraStats={eraStats} />
  );
}
