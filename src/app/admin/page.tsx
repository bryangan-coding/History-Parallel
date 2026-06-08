import { people, events, regions } from '@/data/mockData';
import AdminDashboardClient from './AdminDashboardClient';

export default function AdminDashboardPage() {
  const totalPeople = people.length;
  const totalEvents = events.length;
  const totalRegions = regions.length;

  const statusCounts = {
    published: people.filter((p) => p.dataStatus === 'published').length + events.filter((e) => e.dataStatus === 'published').length,
    needs_review: people.filter((p) => p.dataStatus === 'needs_review').length + events.filter((e) => e.dataStatus === 'needs_review').length,
    imported: people.filter((p) => p.dataStatus === 'imported').length + events.filter((e) => e.dataStatus === 'imported').length,
    verified: people.filter((p) => p.dataStatus === 'verified').length + events.filter((e) => e.dataStatus === 'verified').length,
    rejected: people.filter((p) => p.dataStatus === 'rejected').length + events.filter((e) => e.dataStatus === 'rejected').length,
  };

  const allScores = [...people.map((p) => p.confidenceScore), ...events.map((e) => e.confidenceScore)];
  const buckets = [
    { label: '0–0.3', min: 0, max: 0.3 },
    { label: '0.3–0.5', min: 0.3, max: 0.5 },
    { label: '0.5–0.7', min: 0.5, max: 0.7 },
    { label: '0.7–0.85', min: 0.7, max: 0.85 },
    { label: '0.85–1.0', min: 0.85, max: 1.0 },
  ];
  const distribution = buckets.map((b) => ({
    ...b,
    count: allScores.filter((s) => s >= b.min && (b.max === 1.0 ? s <= b.max : s < b.max)).length,
  }));
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
