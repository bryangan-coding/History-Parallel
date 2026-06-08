import { Suspense } from 'react';
import ParallelPageContent from './ParallelPageContent';
import { regions } from '@/data/mockData';

export default function ParallelPage() {
  return (
    <Suspense
      fallback={
        <div className="animate-pulse space-y-6">
          <div className="h-8 bg-stone-100 rounded w-64" />
          <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
            {[1, 2, 3, 4, 5, 6].map((i) => (
              <div key={i} className="space-y-3">
                <div className="h-4 bg-stone-100 rounded w-24" />
                {[1, 2].map((j) => (
                  <div key={j} className="h-20 bg-stone-100 rounded-lg" />
                ))}
              </div>
            ))}
          </div>
        </div>
      }
    >
      <ParallelPageContent regions={regions} />
    </Suspense>
  );
}
