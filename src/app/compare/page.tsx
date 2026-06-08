import { Suspense } from 'react';
import ComparePageClient from './ComparePageClient';
import { events } from '@/data/mockData';

const publishedEvents = events.filter((e) => e.dataStatus === 'published');

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
      <ComparePageClient allEvents={publishedEvents} />
    </Suspense>
  );
}
