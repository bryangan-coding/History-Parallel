import type { HistoricalEvent } from '@/lib/types';
import TimelineItem from './TimelineItem';

export default function Timeline({
  events,
  personId,
}: {
  events: HistoricalEvent[];
  personId: string;
}) {
  if (events.length === 0) {
    return (
      <p className="text-sm text-stone-400 py-8 text-center">
        暂无时间线数据
      </p>
    );
  }

  const sorted = [...events].sort((a, b) => a.startYear - b.startYear);

  return (
    <div className="relative">
      {/* Vertical line */}
      <div className="absolute left-[19px] top-0 bottom-0 w-px bg-stone-200" />

      <div className="space-y-0">
        {sorted.map((event, index) => (
          <TimelineItem
            key={event.id}
            event={event}
            personId={personId}
            isLast={index === sorted.length - 1}
          />
        ))}
      </div>
    </div>
  );
}
