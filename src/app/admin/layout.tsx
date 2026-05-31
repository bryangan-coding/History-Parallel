'use client';

import { useLocale } from '@/i18n/LocaleProvider';
import { people, events } from '@/data/mockData';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useState } from 'react';
import { BarChart3, Users, Calendar, Upload, Database, ChevronDown, ChevronRight } from 'lucide-react';

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  const { locale } = useLocale();
  const pathname = usePathname();
  const [reviewOpen, setReviewOpen] = useState(true);

  const peoplePending = people.filter((p) => p.dataStatus !== 'published').length;
  const eventsPending = events.filter((e) => e.dataStatus !== 'published').length;

  const navItems = [
    { href: '/admin', label: 'Dashboard', icon: <BarChart3 size={16} /> },
  ];

  const isActive = (href: string) => {
    if (href === '/admin') return pathname === '/admin';
    return pathname.startsWith(href);
  };

  return (
    <div className="flex min-h-screen bg-stone-50">
      {/* Sidebar */}
      <aside className="w-56 border-r border-stone-200 bg-white flex-shrink-0">
        <div className="p-4 border-b border-stone-100">
          <Link href="/admin" className="text-sm font-bold text-stone-900 tracking-tight">
            Admin Panel
          </Link>
          <Link href="/" className="block text-xs text-stone-400 hover:text-stone-600 mt-1 transition-colors">
            ← Back to site
          </Link>
        </div>

        <nav className="p-3 space-y-1">
          {/* Dashboard */}
          <NavLink
            href="/admin"
            icon={<BarChart3 size={16} />}
            label="Dashboard"
            active={isActive('/admin') && pathname === '/admin'}
          />

          {/* Review Queue */}
          <div>
            <button
              onClick={() => setReviewOpen(!reviewOpen)}
              className="w-full flex items-center justify-between px-3 py-2 text-sm text-stone-500 hover:text-stone-700 rounded-lg transition-colors"
            >
              <div className="flex items-center gap-2.5">
                <Users size={16} />
                <span>Review Queue</span>
              </div>
              <div className="flex items-center gap-2">
                {(peoplePending > 0 || eventsPending > 0) && (
                  <span className="text-[10px] bg-amber-100 text-amber-700 px-1.5 py-0.5 rounded font-medium">
                    {peoplePending + eventsPending}
                  </span>
                )}
                {reviewOpen ? <ChevronDown size={14} /> : <ChevronRight size={14} />}
              </div>
            </button>
            {reviewOpen && (
              <div className="ml-4 mt-1 space-y-1 border-l border-stone-100 pl-3">
                <NavLink
                  href="/admin/review/people"
                  icon={<Users size={14} />}
                  label="People"
                  count={peoplePending}
                  active={pathname.startsWith('/admin/review/people')}
                />
                <NavLink
                  href="/admin/review/events"
                  icon={<Calendar size={14} />}
                  label="Events"
                  count={eventsPending}
                  active={pathname.startsWith('/admin/review/events')}
                />
              </div>
            )}
          </div>

          {/* Imports */}
          <NavLink
            href="/admin/imports"
            icon={<Upload size={16} />}
            label="Imports"
            active={pathname.startsWith('/admin/imports')}
          />

          {/* Data Stats */}
          <NavLink
            href="/admin"
            icon={<Database size={16} />}
            label="Data Stats"
            active={false}
          />
        </nav>

        <div className="absolute bottom-0 left-0 w-56 p-4 border-t border-stone-100">
          <div className="text-[10px] text-stone-400">
            {people.length + events.length} total records
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-8">
        {children}
      </main>
    </div>
  );
}

function NavLink({
  href,
  icon,
  label,
  active,
  count,
}: {
  href: string;
  icon: React.ReactNode;
  label: string;
  active: boolean;
  count?: number;
}) {
  return (
    <Link
      href={href}
      className={`flex items-center justify-between px-3 py-2 text-sm rounded-lg transition-colors ${
        active
          ? 'bg-stone-100 text-stone-900 font-medium'
          : 'text-stone-500 hover:text-stone-700 hover:bg-stone-50'
      }`}
    >
      <div className="flex items-center gap-2.5">
        {icon}
        <span>{label}</span>
      </div>
      {count !== undefined && count > 0 && (
        <span className={`text-[10px] px-1.5 py-0.5 rounded font-medium ${
          active ? 'bg-amber-200 text-amber-800' : 'bg-amber-100 text-amber-700'
        }`}>
          {count}
        </span>
      )}
    </Link>
  );
}
