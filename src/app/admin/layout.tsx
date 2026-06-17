import AdminLayoutClient from './AdminLayoutClient';
import { peoplePending, eventsPending, totalRecords } from '@/data/stats';

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
