'use client';

import { useState } from 'react';

type FeedbackType = 'bug' | 'feature' | 'suggestion' | 'data';

interface FeedbackEntry {
  type: FeedbackType;
  message: string;
  email: string;
  timestamp: string;
  url: string;
}

const FEEDBACK_KEY = 'history-parallel-feedback';

const typeLabels: Record<FeedbackType, { zh: string; en: string }> = {
  bug: { zh: '🐛 报告问题', en: '🐛 Bug Report' },
  feature: { zh: '💡 功能建议', en: '💡 Feature Request' },
  suggestion: { zh: '📝 使用反馈', en: '📝 General Feedback' },
  data: { zh: '📊 数据问题', en: '📊 Data Issue' },
};

export function FeedbackButton() {
  const [open, setOpen] = useState(false);
  const [type, setType] = useState<FeedbackType>('suggestion');
  const [message, setMessage] = useState('');
  const [email, setEmail] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [expanded, setExpanded] = useState(false);

  const handleSubmit = () => {
    if (!message.trim()) return;

    const entry: FeedbackEntry = {
      type,
      message: message.trim(),
      email: email.trim(),
      timestamp: new Date().toISOString(),
      url: typeof window !== 'undefined' ? window.location.href : '',
    };

    try {
      const existing = JSON.parse(localStorage.getItem(FEEDBACK_KEY) || '[]');
      existing.push(entry);
      localStorage.setItem(FEEDBACK_KEY, JSON.stringify(existing));
    } catch {
      // localStorage unavailable
    }

    setSubmitted(true);
    setMessage('');
    setTimeout(() => {
      setSubmitted(false);
      setOpen(false);
      setExpanded(false);
    }, 2000);
  };

  if (!open) {
    return (
      <div className="fixed bottom-6 right-6 z-50">
        <button
          onClick={() => { setOpen(true); setSubmitted(false); }}
          className="flex items-center gap-2 px-4 py-2.5 rounded-full bg-stone-900 text-white text-sm font-medium shadow-lg hover:bg-stone-800 transition-all hover:scale-105 active:scale-95"
          title="提交反馈 / Submit Feedback"
        >
          <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
          </svg>
          {expanded ? '提交反馈' : '反馈'}
        </button>
      </div>
    );
  }

  return (
    <div className="fixed inset-0 z-50 flex items-end sm:items-center justify-center">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-black/20"
        onClick={() => { setOpen(false); setExpanded(false); }}
      />

      {/* Modal */}
      <div className="relative w-full max-w-md mx-4 bg-white rounded-2xl shadow-2xl border border-stone-200 overflow-hidden">
        {submitted ? (
          <div className="p-8 text-center">
            <div className="text-3xl mb-3">🎉</div>
            <p className="text-stone-900 font-semibold text-lg">感谢反馈！</p>
            <p className="text-stone-500 text-sm mt-1">Thank you for your feedback!</p>
          </div>
        ) : (
          <>
            {/* Header */}
            <div className="px-6 py-4 border-b border-stone-100 flex items-center justify-between">
              <h3 className="font-semibold text-stone-900">提交反馈 / Submit Feedback</h3>
              <button
                onClick={() => { setOpen(false); setExpanded(false); }}
                className="text-stone-400 hover:text-stone-600"
              >
                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>

            {/* Body */}
            <div className="p-6 space-y-4">
              {/* Type */}
              <div>
                <label className="block text-xs font-medium text-stone-500 mb-2">类型 / Type</label>
                <div className="grid grid-cols-2 gap-2">
                  {(Object.keys(typeLabels) as FeedbackType[]).map((t) => (
                    <button
                      key={t}
                      onClick={() => setType(t)}
                      className={`text-left px-3 py-2 rounded-lg text-sm border transition-colors ${
                        type === t
                          ? 'border-stone-900 bg-stone-900 text-white'
                          : 'border-stone-200 text-stone-600 hover:border-stone-400'
                      }`}
                    >
                      {typeLabels[t].zh}
                    </button>
                  ))}
                </div>
              </div>

              {/* Message */}
              <div>
                <label className="block text-xs font-medium text-stone-500 mb-2">
                  描述 / Description
                </label>
                <textarea
                  value={message}
                  onChange={(e) => setMessage(e.target.value)}
                  placeholder="请描述你的反馈或建议..."
                  rows={4}
                  className="w-full p-3 text-sm border border-stone-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-stone-400 focus:border-stone-400 resize-none placeholder:text-stone-300"
                />
              </div>

              {/* Email (optional) */}
              <div>
                <label className="block text-xs font-medium text-stone-500 mb-2">
                  邮箱（选填）/ Email (optional)
                </label>
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="your@email.com"
                  className="w-full p-2.5 text-sm border border-stone-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-stone-400 focus:border-stone-400 placeholder:text-stone-300"
                />
              </div>
            </div>

            {/* Footer */}
            <div className="px-6 py-4 border-t border-stone-100 bg-stone-50 flex justify-end gap-3">
              <button
                onClick={() => { setOpen(false); setExpanded(false); }}
                className="px-4 py-2 text-sm text-stone-500 hover:text-stone-700"
              >
                取消
              </button>
              <button
                onClick={handleSubmit}
                disabled={!message.trim()}
                className={`px-5 py-2 text-sm font-medium rounded-lg transition-colors ${
                  message.trim()
                    ? 'bg-stone-900 text-white hover:bg-stone-800'
                    : 'bg-stone-200 text-stone-400 cursor-not-allowed'
                }`}
              >
                提交 / Submit
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  );
}
