import Link from 'next/link';

export default function PageHeader({
  title,
  subtitle,
  backTo,
  backLabel,
}: {
  title: string;
  subtitle?: string;
  backTo?: string;
  backLabel?: string;
}) {
  return (
    <div className="mb-8">
      {backTo && backLabel && (
        <Link
          href={backTo}
          className="inline-flex items-center text-sm text-stone-500 hover:text-stone-800 transition-colors mb-2"
        >
          <svg
            className="w-4 h-4 mr-1"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M15 19l-7-7 7-7"
            />
          </svg>
          {backLabel}
        </Link>
      )}
      <h1 className="text-2xl font-bold text-stone-900 tracking-tight">
        {title}
      </h1>
      {subtitle && (
        <p className="mt-1 text-stone-500">{subtitle}</p>
      )}
    </div>
  );
}
