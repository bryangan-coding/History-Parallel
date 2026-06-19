import AdminReviewPeopleClient from './AdminReviewPeopleClient';
import { listPeople } from '@/server/db/queries';

export default async function AdminReviewPeoplePage() {
  // Compute counts on the server from the DB
  const [all, published] = await Promise.all([
    listPeople(),
    listPeople({ publishedOnly: true }),
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
