import { Suspense } from 'react';
import SearchResults from './SearchResults';

function SearchSkeleton() {
  return (
    <div className="animate-pulse">
      {/* Header skeleton */}
      <div className="mb-8">
        <div className="h-8 bg-stone-100 rounded w-24" />
        <div className="h-4 bg-stone-100 rounded w-64 mt-2" />
      </div>

      {/* Search box skeleton */}
      <div className="h-11 bg-stone-100 rounded-xl mb-4" />

      {/* Filter bar skeleton */}
      <div className="flex gap-2 mb-4">
        <div className="h-7 bg-stone-100 rounded w-16" />
        <div className="h-7 bg-stone-100 rounded w-16" />
        <div className="h-7 bg-stone-100 rounded w-16" />
      </div>

      {/* People section skeleton */}
      <div className="space-y-4">
        <div className="h-4 bg-stone-100 rounded w-20" />
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          {[1, 2, 3].map((i) => (
            <div key={i} className="h-36 bg-stone-100 rounded-xl" />
          ))}
        </div>
      </div>

      {/* Events section skeleton */}
      <div className="space-y-4 mt-8">
        <div className="h-4 bg-stone-100 rounded w-20" />
        <div className="space-y-3">
          {[1, 2].map((i) => (
            <div key={i} className="h-32 bg-stone-100 rounded-xl" />
          ))}
        </div>
      </div>
    </div>
  );
}

export default function SearchPage() {
  return (
    <Suspense fallback={<SearchSkeleton />}>
      <SearchResults />
    </Suspense>
  );
}
