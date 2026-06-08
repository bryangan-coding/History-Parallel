import type { HistoricalEvent, Region } from '@/lib/types';
import TimelineItem from './TimelineItem';

export default function Timeline({
  events,
  eventRegions,
}: {
  events: HistoricalEvent[];
  /** Pre-resolved regions for each event — avoids importing mockData in client */
  eventRegions?: Map<string, Region | undefined>;
}) {
  if (events.length === 0) {
    return (
      <p className="text-sm text-stone-400 py-8 text-center">
        暂无时间线数据
      </p>
    );
  }

  const sorted = [...events].sort((a, b) => (a.startYear ?? 0) - (b.startYear ?? 0));

  return (
    <div className="relative">
      {/* Vertical line */}
      <div className="absolute left-[19px] top-0 bottom-0 w-px bg-stone-200" />

      <div className="space-y-0">
        {sorted.map((event, index) => (
          <TimelineItem
            key={event.id}
            event={event}
            isLast={index === sorted.length - 1}
            region={eventRegions?.get(event.id)}
          />
        ))}
      </div>
    </div>
  );
}
