import AdminReviewPeopleClient from './AdminReviewPeopleClient';
import { listPeople } from '@/server/db/queries';

export default async function AdminReviewPeoplePage() {
  // Compute counts on the server from the DB.
  // Use limit:0 + page:1 to get only the count without loading rows into memory.
  const [all, published] = await Promise.all([
    listPeople({ page: 1, limit: 1 }),
    listPeople({ publishedOnly: true, page: 1, limit: 1 }),
  ]);

  const totalCount = all.total;
  const publishedCount = published.total;
  const pendingCount = totalCount - publishedCount;

  return (
    <AdminReviewPeopleClient
      totalCount={totalCount}
      pendingCount={pendingCount}
      publishedCount={publishedCount}
    />
  );
}
