"use client";

import React from 'react';
import { useStudioStore } from '@/store/useStudioStore';
import { MessageSquare, Image as ImageIcon, Clock } from 'lucide-react';

export default function ScriptEditor() {
  const { script, updateSegment } = useStudioStore();

  return (
    <div className="mt-10 space-y-6">
      <h3 className="text-sm font-medium text-slate-400 uppercase tracking-widest">Storyboard Timeline</h3>
      <div className="space-y-4">
        {script.map((segment, index) => (
          <div key={segment.id} className="group relative rounded-xl border border-white/5 bg-white/[0.02] p-4 hover:border-indigo-500/50 transition-all">
            <div className="mb-3 flex items-center justify-between">
              <span className="text-xs font-bold text-indigo-400 uppercase">Scene {index + 1}</span>
              <div className="flex items-center gap-1 text-[10px] text-slate-500">
                <Clock className="h-3 w-3" />
                {segment.duration}s
              </div>
            </div>
            
            <div className="space-y-3">
              <div className="flex gap-3">
                <MessageSquare className="h-4 w-4 mt-1 text-slate-600" />
                <textarea
                  value={segment.text}
                  onChange={(e) => updateSegment(segment.id, { text: e.target.value })}
                  className="w-full bg-transparent text-sm text-slate-200 focus:outline-none"
                  rows={2}
                />
              </div>
              
              <div className="flex gap-3 rounded-lg bg-black/30 p-2 border border-white/5">
                <ImageIcon className="h-4 w-4 mt-1 text-slate-600" />
                <input
                  value={segment.visualPrompt}
                  onChange={(e) => updateSegment(segment.id, { visualPrompt: e.target.value })}
                  className="w-full bg-transparent text-xs italic text-slate-400 focus:outline-none"
                />
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}