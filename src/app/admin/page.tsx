import AdminDashboardClient from './AdminDashboardClient';
import { totalPeople, totalEvents, totalRegions, statusCounts, distribution } from '@/data/stats';

export default function AdminDashboardPage() {
  const maxDist = Math.max(...distribution.map((d) => d.count), 1);

  return (
    <AdminDashboardClient
      totalPeople={totalPeople}
      totalEvents={totalEvents}
      totalRegions={totalRegions}
      statusCounts={statusCounts}
      distribution={distribution}
      maxDist={maxDist}
    />
  );
}
