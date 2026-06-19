'use client';

import { useEffect } from 'react';

export default function GlobalErrorPage({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error('[Global Error Boundary]', error);
  }, [error]);

  return (
    <div className="min-h-screen bg-stone-50 flex flex-col items-center justify-center px-4">
      <div className="max-w-md w-full bg-white border border-stone-200 rounded-lg p-8 shadow-sm">
        <div className="flex items-center gap-3 mb-4">
          <div className="w-10 h-10 rounded-full bg-red-50 flex items-center justify-center">
            <svg className="w-5 h-5 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <h2 className="text-lg font-semibold text-stone-900">出错了</h2>
        </div>

        <p className="text-sm text-stone-600 mb-6">
          页面加载时发生错误。请尝试重新加载，或返回首页。
        </p>

        {/* Only show error details in development.
            NEXT_PUBLIC_ prefix ensures the value is available client-side. */}
        {process.env.NEXT_PUBLIC_VERCEL_ENV !== 'production' && (
          <div className="mb-6 p-3 bg-stone-50 rounded border border-stone-200 text-xs text-stone-700 font-mono overflow-auto max-h-32">
            {error.message}
            {error.digest && (
              <span className="block mt-1 text-stone-400">digest: {error.digest}</span>
            )}
          </div>
        )}

        <div className="flex gap-3">
          <button
            onClick={() => reset()}
            className="px-4 py-2 bg-stone-900 text-white text-sm rounded-lg hover:bg-stone-800 transition-colors cursor-pointer"
          >
            重新加载
          </button>
          <a
            href="/"
            className="px-4 py-2 bg-stone-100 text-stone-700 text-sm rounded-lg hover:bg-stone-200 transition-colors inline-flex items-center"
          >
            返回首页
          </a>
        </div>
      </div>
    </div>
  );
}
