"use client";
import React, { useState } from 'react';

export default function CreatorDashboard() {
  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    setLoading(true);
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/generate-video`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt, target_platform: 'tiktok' })
    });
    const data = await res.json();
    alert(`Magic started! Task ID: ${data.task_id}`);
    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-black text-white p-8 flex flex-col items-center justify-center">
      <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-purple-400 to-pink-600 bg-clip-text text-transparent">
        OVERLORD AI
      </h1>
      <p className="text-gray-400 mb-8">Turn your thoughts into viral videos instantly.</p>
      
      <div className="w-full max-w-2xl bg-zinc-900 p-6 rounded-2xl border border-zinc-800">
        <textarea 
          className="w-full bg-transparent border-none focus:ring-0 text-xl resize-none"
          placeholder="What is your video about?"
          rows={3}
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />
        <div className="flex justify-end mt-4">
          <button 
            onClick={handleGenerate}
            disabled={loading}
            className="bg-white text-black px-6 py-2 rounded-full font-bold hover:bg-zinc-200 transition disabled:opacity-50"
          >
            {loading ? "Igniting AI..." : "Generate Magic ✨"}
          </button>
        </div>
      </div>
      
      <div className="mt-12 grid grid-cols-3 gap-4 opacity-50">
        <div className="border border-dashed p-4 rounded text-center">Scripting...</div>
        <div className="border border-dashed p-4 rounded text-center">Voiceover...</div>
        <div className="border border-dashed p-4 rounded text-center">Rendering...</div>
      </div>
    </main>
  );
}