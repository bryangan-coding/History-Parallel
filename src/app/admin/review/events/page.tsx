import { events, regions } from '@/data/mockData';
import AdminReviewEventsClient from './AdminReviewEventsClient';

export default function AdminReviewEventsPage() {
  return <AdminReviewEventsClient events={events} regions={regions} />;
}
