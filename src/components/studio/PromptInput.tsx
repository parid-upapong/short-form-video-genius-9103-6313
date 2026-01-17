"use client";

import React from 'react';
import { useStudioStore } from '@/store/useStudioStore';
import { Sparkles } from 'lucide-react';

export default function PromptInput() {
  const { prompt, setPrompt, generateScript, status } = useStudioStore();

  return (
    <div className="space-y-4">
      <label className="text-sm font-medium text-slate-400 uppercase tracking-widest">
        Video Concept
      </label>
      <div className="relative">
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="e.g. A motivational video about the future of AI in 2024..."
          className="w-full min-h-[120px] rounded-xl border border-white/10 bg-white/5 p-4 text-white focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 transition-all"
        />
        <button
          onClick={generateScript}
          disabled={status === 'generating' || !prompt}
          className="mt-4 flex w-full items-center justify-center gap-2 rounded-xl bg-white px-4 py-3 text-black font-bold hover:bg-slate-200 disabled:opacity-50 transition-all"
        >
          <Sparkles className="h-5 w-5" />
          Generate Storyboard
        </button>
      </div>
    </div>
  );
}