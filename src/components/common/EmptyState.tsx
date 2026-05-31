import { SearchX } from 'lucide-react';

export default function EmptyState({
  title = '没有找到结果',
  description = '请尝试其他关键词',
  icon = true,
}: {
  title?: string;
  description?: string;
  icon?: boolean;
}) {
  return (
    <div className="flex flex-col items-center justify-center py-20 text-center">
      {icon && <SearchX className="h-12 w-12 text-stone-300 mb-4" />}
      <h3 className="text-lg font-medium text-stone-600">{title}</h3>
      <p className="mt-1 text-sm text-stone-400 max-w-md">{description}</p>
    </div>
  );
}
