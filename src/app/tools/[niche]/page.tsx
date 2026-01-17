import { Metadata } from 'next';
import { notFound } from 'next/navigation';

// This is a Programmatic SEO Template for Niche Landing Pages
interface Props {
  params: { niche: string };
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const nicheName = params.niche.replace(/-/g, ' ');
  return {
    title: `Best AI Video Generator for ${nicheName} | Overlord`,
    description: `Create viral ${nicheName} videos in seconds. Use our AI to generate scripts, voices, and visuals for your ${nicheName} channel.`,
  };
}

export default function NichePage({ params }: Props) {
  const nicheName = params.niche.replace(/-/g, ' ');

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-8 bg-black text-white">
      <h1 className="text-5xl font-bold mb-4 capitalize">
        AI Video Revolution for {nicheName}
      </h1>
      <p className="text-xl text-gray-400 mb-8 max-w-2xl text-center">
        Stop spending hours editing. Overlord's AI understands the nuances of {nicheName} content
        and builds high-retention videos that dominate the algorithm.
      </p>
      
      <div className="bg-gradient-to-r from-purple-600 to-blue-600 p-1 rounded-lg">
        <button className="bg-black px-8 py-4 rounded-md font-bold hover:bg-transparent transition">
          Create Your First {nicheName} Video Free
        </button>
      </div>

      <section className="mt-20 grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="p-6 border border-gray-800 rounded-xl">
          <h3 className="font-bold text-lg mb-2">Automated Scripting</h3>
          <p className="text-gray-500">AI-driven hooks tailored specifically for {nicheName} trends.</p>
        </div>
        <div className="p-6 border border-gray-800 rounded-xl">
          <h3 className="font-bold text-lg mb-2">Smart Visuals</h3>
          <p className="text-gray-500">Dynamic overlays and b-roll that match the {nicheName} aesthetic.</p>
        </div>
        <div className="p-6 border border-gray-800 rounded-xl">
          <h3 className="font-bold text-lg mb-2">Voice & Tone</h3>
          <p className="text-gray-500">Professional TTS with the right emotional inflection for your audience.</p>
        </div>
      </section>
    </main>
  );
}