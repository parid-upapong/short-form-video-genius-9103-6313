"use client";

import React from 'react';
import { useStudioStore } from '@/store/useStudioStore';
import { Play, RotateCcw, Maximize2 } from 'lucide-react';

export default function VideoPreview() {
  const { status } = useStudioStore();

  return (
    <div className="relative aspect-[9/16] w-full max-w-[360px] overflow-hidden rounded-3xl border-[8px] border-slate-800 bg-slate-900 shadow-2xl">
      {status === 'idle' || status === 'generating' ? (
        <div className="flex h-full flex-col items-center justify-center p-8 text-center">
          <div className="mb-4 h-16 w-16 rounded-full bg-white/5 flex items-center justify-center">
             <Play className="h-8 w-8 text-white/20" />
          </div>
          <p className="text-sm text-slate-500 font-medium">Your video preview will appear here after generation.</p>
        </div>
      ) : (
        <>
          {/* Placeholder for the real video stream/canvas */}
          <div className="absolute inset-0 bg-gradient-to-b from-transparent to-black/60" />
          <img 
            src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&q=80&w=1000" 
            alt="Preview Frame" 
            className="h-full w-full object-cover"
          />
          
          {/* Mock Overlays (TikTok Style) */}
          <div className="absolute bottom-10 left-4 right-4">
             <div className="h-1 w-full bg-white/20 rounded-full mb-4">
                <div className="h-full w-1/3 bg-indigo-500 rounded-full" />
             </div>
             <div className="flex justify-between items-center">
                <div className="flex gap-4">
                   <RotateCcw className="h-5 w-5 text-white" />
                   <Play className="h-5 w-5 fill-white text-white" />
                </div>
                <Maximize2 className="h-5 w-5 text-white" />
             </div>
          </div>
        </>
      )}
    </div>
  );
}