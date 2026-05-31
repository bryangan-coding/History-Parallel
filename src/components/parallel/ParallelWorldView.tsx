'use client';

import type { ParallelRegionGroup } from '@/lib/types';
import RegionColumn from './RegionColumn';

export default function ParallelWorldView({
  groups,
}: {
  groups: ParallelRegionGroup[];
}) {
  if (groups.length === 0) {
    return (
      <div className="text-center py-16">
        <p className="text-stone-400 text-sm">
          该时间范围内暂无匹配的历史事件
        </p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
      {groups.map((group) => (
        <RegionColumn
          key={group.region.id}
          title={group.region.name}
          events={group.events}
        />
      ))}
    </div>
  );
}
