import { people } from '@/data/mockData';
import AdminReviewPeopleClient from './AdminReviewPeopleClient';

// Only pass counts, not the full data
const totalCount = people.length;
const pendingCount = people.filter((p) => p.dataStatus !== 'published').length;
const publishedCount = people.filter((p) => p.dataStatus === 'published').length;

export default function AdminReviewPeoplePage() {
  return (
    <AdminReviewPeopleClient
      totalCount={totalCount}
      pendingCount={pendingCount}
      publishedCount={publishedCount}
    />
  );
}
