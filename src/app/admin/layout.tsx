import AdminLayoutClient from './AdminLayoutClient';
import { people, events } from '@/data/mockData';

// Pre-compute stats on the server
const peoplePending = people.filter((p) => p.dataStatus !== 'published').length;
const eventsPending = events.filter((e) => e.dataStatus !== 'published').length;
const totalRecords = people.length + events.length;

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  return (
    <AdminLayoutClient
      peoplePending={peoplePending}
      eventsPending={eventsPending}
      totalRecords={totalRecords}
    >
      {children}
    </AdminLayoutClient>
  );
}
