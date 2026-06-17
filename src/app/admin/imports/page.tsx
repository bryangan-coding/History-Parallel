import { regions } from '@/data/regions';
import AdminImportsClient from './AdminImportsClient';

export default function AdminImportsPage() {
  return <AdminImportsClient regions={regions} />;
}
