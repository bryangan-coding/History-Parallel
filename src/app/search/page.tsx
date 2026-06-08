import { Suspense } from 'react';
import SearchResults from './SearchResults';
import { regions } from '@/data/mockData';

export default function SearchPage() {
  return (
    <Suspense
      fallback={
        <div className="animate-pulse">
          <div className="mb-8">
            <div className="h-8 bg-stone-100 rounded w-24" />
            <div className="h-4 bg-stone-100 rounded w-64 mt-2" />
          </div>
          <div className="h-11 bg-stone-100 rounded-xl mb-4" />
          <div className="flex gap-2 mb-4">
            <div className="h-7 bg-stone-100 rounded w-16" />
            <div className="h-7 bg-stone-100 rounded w-16" />
            <div className="h-7 bg-stone-100 rounded w-16" />
          </div>
        </div>
      }
    >
      <SearchResults regions={regions} />
    </Suspense>
  );
}
