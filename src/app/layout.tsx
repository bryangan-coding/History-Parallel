import type { Metadata } from 'next';
import './globals.css';
import { AppShell } from './AppShell';

export const metadata: Metadata = {
  title: '历史平行线 — 在同一时间，看见世界不同角落的历史现场',
  description:
    '历史平行线是一个历史时空对照工具。选择历史上的某个时间点或人物，查看同一时间段内全球不同地区发生的历史事件。',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="zh-CN" className="h-full antialiased">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body className="min-h-full flex flex-col bg-stone-50 text-stone-900">
        <AppShell>{children}</AppShell>
      </body>
    </html>
  );
}
