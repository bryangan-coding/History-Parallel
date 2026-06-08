import { regions } from '@/data/mockData';
import AdminImportsClient from './AdminImportsClient';

export default function AdminImportsPage() {
  return <AdminImportsClient regions={regions} />;
}
