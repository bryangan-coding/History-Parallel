import AdminReviewEventsClient from './AdminReviewEventsClient';
import { listAllEvents, listRegions } from '@/server/db/queries';

export default async function AdminReviewEventsPage() {
  const [eventsResult, regions] = await Promise.all([
    listAllEvents({ limit: 2000, page: 1 }),
    listRegions(),
  ]);
  return <AdminReviewEventsClient events={eventsResult.items} regions={regions} />;
}
