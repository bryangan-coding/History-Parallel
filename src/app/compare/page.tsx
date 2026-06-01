import { Suspense } from 'react';
import ComparePageClient from './ComparePageClient';

export default function ComparePage() {
  return (
    <Suspense
      fallback={
        <div className="animate-pulse space-y-6">
          <div className="h-8 w-48 bg-stone-100 rounded" />
          <div className="h-5 w-96 bg-stone-100 rounded" />
          <div className="h-12 w-full bg-stone-100 rounded-lg" />
          <div className="h-64 w-full bg-stone-100 rounded-lg" />
        </div>
      }
    >
      <ComparePageClient />
    </Suspense>
  );
}
