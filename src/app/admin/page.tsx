'use client';

import { useLocale } from '@/i18n/LocaleProvider';
import { people, events, regions } from '@/data/mockData';
import { BarChart3, Users, Calendar, Globe, Clock } from 'lucide-react';

export default function AdminDashboardPage() {
  const { locale } = useLocale();

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

  // Confidence score distribution
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

  const mockImports = [
    { id: '1', name: 'wikidata-people-2026-05-31.json', source: 'wikidata', date: '2026-05-31', status: 'completed' as const, count: 50 },
    { id: '2', name: 'wikidata-events-2026-05-30.json', source: 'wikidata', date: '2026-05-30', status: 'completed' as const, count: 39 },
    { id: '3', name: 'manual-import-2026-05-28.json', source: 'manual', date: '2026-05-28', status: 'processing' as const, count: 15 },
  ];

  const pendingReview = statusCounts.needs_review + statusCounts.imported;

  return (
    <div className="space-y-8">
      <h1 className="text-2xl font-bold text-stone-900">Dashboard</h1>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard icon={<Users size={18} />} label="People" value={totalPeople} color="blue" />
        <StatCard icon={<Calendar size={18} />} label="Events" value={totalEvents} color="amber" />
        <StatCard icon={<Globe size={18} />} label="Regions" value={totalRegions} color="emerald" />
        <StatCard icon={<Clock size={18} />} label="Pending Review" value={pendingReview} color="red" />
      </div>

      {/* Status Breakdown */}
      <div className="grid grid-cols-1 md:grid-cols-5 gap-3">
        {[
          { label: 'Published', count: statusCounts.published, color: 'bg-emerald-50 text-emerald-700 border-emerald-200' },
          { label: 'Needs Review', count: statusCounts.needs_review, color: 'bg-amber-50 text-amber-700 border-amber-200' },
          { label: 'Imported', count: statusCounts.imported, color: 'bg-blue-50 text-blue-700 border-blue-200' },
          { label: 'Verified', count: statusCounts.verified, color: 'bg-green-50 text-green-700 border-green-200' },
          { label: 'Rejected', count: statusCounts.rejected, color: 'bg-red-50 text-red-700 border-red-200' },
        ].map((item) => (
          <div key={item.label} className={`border rounded-xl p-4 ${item.color} transition-all hover:shadow-sm`}>
            <div className="text-2xl font-bold">{item.count}</div>
            <div className="text-xs mt-1 opacity-80">{item.label}</div>
          </div>
        ))}
      </div>

      {/* Confidence Score Distribution */}
      <div className="border border-stone-200 rounded-xl bg-white p-6">
        <div className="flex items-center gap-2 mb-4">
          <BarChart3 size={18} className="text-stone-400" />
          <h2 className="text-lg font-semibold text-stone-800">Confidence Score Distribution</h2>
        </div>
        <div className="flex items-end gap-2 h-32">
          {distribution.map((d) => (
            <div key={d.label} className="flex-1 flex flex-col items-center gap-1">
              <div className="text-xs font-mono text-stone-500">{d.count}</div>
              <div
                className="w-full bg-stone-400 rounded-t transition-all duration-500 hover:bg-stone-500"
                style={{ height: `${(d.count / maxDist) * 100}%` }}
              />
              <div className="text-[10px] text-stone-400">{d.label}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Recent Imports */}
      <div className="border border-stone-200 rounded-xl bg-white p-6">
        <h2 className="text-lg font-semibold text-stone-800 mb-4">Recent Imports</h2>
        <div className="divide-y divide-stone-100">
          {mockImports.map((imp) => (
            <div key={imp.id} className="flex items-center justify-between py-3 px-1">
              <div>
                <div className="text-sm font-medium text-stone-700 font-mono">{imp.name}</div>
                <div className="text-xs text-stone-400">{imp.source} · {imp.date}</div>
              </div>
              <div className="flex items-center gap-3">
                <span className="text-xs text-stone-500">{imp.count} entries</span>
                <span className={`text-xs px-2 py-0.5 rounded-full ${
                  imp.status === 'completed' ? 'bg-emerald-100 text-emerald-700' :
                  imp.status === 'processing' ? 'bg-blue-100 text-blue-700 animate-pulse' :
                  'bg-red-100 text-red-700'
                }`}>
                  {imp.status}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

function StatCard({ icon, label, value, color }: {
  icon: React.ReactNode;
  label: string;
  value: number;
  color: 'blue' | 'amber' | 'emerald' | 'red';
}) {
  const colorMap = {
    blue: 'bg-blue-50 text-blue-600',
    amber: 'bg-amber-50 text-amber-600',
    emerald: 'bg-emerald-50 text-emerald-600',
    red: 'bg-red-50 text-red-600',
  };
  return (
    <div className="border border-stone-200 rounded-xl bg-white p-5 transition-all hover:shadow-sm">
      <div className="flex items-center justify-between">
        <div className={`p-2 rounded-lg ${colorMap[color]}`}>{icon}</div>
        <div className="text-3xl font-bold text-stone-900">{value}</div>
      </div>
      <div className="text-xs text-stone-400 mt-3">{label}</div>
    </div>
  );
}
