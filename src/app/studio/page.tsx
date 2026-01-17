"use client";

import React from 'react';
import PromptInput from '@/components/studio/PromptInput';
import ScriptEditor from '@/components/studio/ScriptEditor';
import VideoPreview from '@/components/studio/VideoPreview';
import { useStudioStore } from '@/store/useStudioStore';
import { Loader2, Zap } from 'lucide-react';

export default function StudioPage() {
  const { status, script } = useStudioStore();

  return (
    <main className="flex h-screen w-full flex-col bg-[#0a0a0c]">
      {/* Header */}
      <header className="flex h-16 items-center justify-between border-b border-white/10 px-6">
        <div className="flex items-center gap-2">
          <div className="rounded bg-indigo-600 p-1">
            <Zap className="h-5 w-5 fill-white" />
          </div>
          <h1 className="text-xl font-bold tracking-tight">OVERLORD <span className="text-indigo-400">STUDIO</span></h1>
        </div>
        <button className="rounded-full bg-indigo-600 px-6 py-2 text-sm font-semibold hover:bg-indigo-500 transition-colors">
          Export Video
        </button>
      </header>

      {/* Main Studio Area */}
      <div className="flex flex-1 overflow-hidden">
        {/* Left Sidebar: Inputs & Logic */}
        <section className="flex w-[450px] flex-col border-r border-white/10 bg-[#0f0f12] p-6 overflow-y-auto">
          <PromptInput />
          
          {status === 'generating' && (
            <div className="mt-20 flex flex-col items-center justify-center gap-4 text-slate-400">
              <Loader2 className="h-8 w-8 animate-spin text-indigo-500" />
              <p>AI Virtual Editor is composing your script...</p>
            </div>
          )}

          {script.length > 0 && <ScriptEditor />}
        </section>

        {/* Right Area: Preview & Timeline */}
        <section className="flex flex-1 flex-col items-center justify-center bg-black/40 p-12">
          <VideoPreview />
        </section>
      </div>
    </main>
  );
}