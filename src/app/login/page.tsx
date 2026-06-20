import { Suspense } from 'react';
import LoginForm from './LoginForm';

export const metadata = {
  title: '登录 — 历史平行线',
};

export default function LoginPage() {
  return (
    <div className="min-h-screen bg-stone-50 flex items-center justify-center px-4">
      <div className="max-w-sm w-full bg-white border border-stone-200 rounded-lg p-8 shadow-sm">
        <div className="text-center mb-6">
          <h1 className="text-xl font-bold text-stone-900">历史平行线</h1>
          <p className="text-sm text-stone-500 mt-1">管理后台登录</p>
        </div>
        <Suspense fallback={<div className="text-sm text-stone-400 text-center py-4">Loading...</div>}>
          <LoginForm />
        </Suspense>
      </div>
    </div>
  );
}
