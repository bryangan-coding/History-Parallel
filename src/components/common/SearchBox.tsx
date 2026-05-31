'use client';

import { Search } from 'lucide-react';
import { useRouter } from 'next/navigation';
import { useState, FormEvent } from 'react';

export default function SearchBox({
  placeholder = '搜索人物、事件、地点、年份…',
  defaultValue = '',
  large = false,
  className = '',
}: {
  placeholder?: string;
  defaultValue?: string;
  large?: boolean;
  className?: string;
}) {
  const router = useRouter();
  const [query, setQuery] = useState(defaultValue);

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    const trimmed = query.trim();
    if (!trimmed) return;
    router.push(`/search?q=${encodeURIComponent(trimmed)}`);
  };

  return (
    <form onSubmit={handleSubmit} className={`w-full ${className}`}>
      <div
        className={`relative flex items-center w-full rounded-xl border border-stone-200 bg-white shadow-sm transition-shadow focus-within:border-stone-400 focus-within:shadow-md ${
          large ? 'h-14' : 'h-11'
        }`}
      >
        <Search className="absolute left-4 h-4 w-4 text-stone-400 shrink-0" />
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder={placeholder}
          className={`w-full h-full pl-11 pr-4 bg-transparent text-stone-900 placeholder-stone-400 outline-none text-base rounded-xl ${
            large ? 'text-lg' : 'text-base'
          }`}
        />
      </div>
    </form>
  );
}
