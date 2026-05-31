'use client';

import { useRouter, useSearchParams } from 'next/navigation';
import type { TimeRange } from '@/lib/types';

const RANGE_OPTIONS: { value: TimeRange; label: string }[] = [
  { value: 0, label: '同年' },
  { value: 5, label: '±5年' },
  { value: 20, label: '±20年' },
  { value: 100, label: '±100年' },
];

export default function TimeRangeSelector({
  currentRange,
}: {
  currentRange: TimeRange;
}) {
  const router = useRouter();
  const searchParams = useSearchParams();

  const handleRangeChange = (range: TimeRange) => {
    const params = new URLSearchParams(searchParams.toString());
    params.set('range', range.toString());
    router.push(`/parallel?${params.toString()}`);
  };

  return (
    <div className="flex items-center gap-1 bg-stone-100 rounded-lg p-1">
      {RANGE_OPTIONS.map((opt) => (
        <button
          key={opt.value}
          onClick={() => handleRangeChange(opt.value)}
          className={`px-3 py-1.5 text-xs font-medium rounded-md transition-all ${
            currentRange === opt.value
              ? 'bg-white text-stone-900 shadow-sm'
              : 'text-stone-500 hover:text-stone-700'
          }`}
        >
          {opt.label}
        </button>
      ))}
    </div>
  );
}
