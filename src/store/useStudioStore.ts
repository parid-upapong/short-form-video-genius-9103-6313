import { create } from 'zustand';

interface ScriptSegment {
  id: string;
  text: string;
  visualPrompt: string;
  duration: number;
}

interface StudioState {
  prompt: string;
  status: 'idle' | 'generating' | 'ready' | 'rendering';
  script: ScriptSegment[];
  previewUrl: string | null;
  setPrompt: (prompt: string) => void;
  generateScript: () => Promise<void>;
  updateSegment: (id: string, updates: Partial<ScriptSegment>) => void;
}

export const useStudioStore = create<StudioState>((set, get) => ({
  prompt: '',
  status: 'idle',
  script: [],
  previewUrl: null,

  setPrompt: (prompt) => set({ prompt }),

  generateScript: async () => {
    set({ status: 'generating' });
    // Mocking API Call to Backend (FastAPI)
    await new Promise((resolve) => setTimeout(resolve, 2000));
    
    const mockScript: ScriptSegment[] = [
      { id: '1', text: "Stop scrolling!", visualPrompt: "Cinematic close-up of a person looking shocked", duration: 3 },
      { id: '2', text: "Here is how AI is changing video forever.", visualPrompt: "Fast cuts of digital matrices and glowing screens", duration: 5 },
      { id: '3', text: "Check the link to start today.", visualPrompt: "A sleek hand pointing at a futuristic interface", duration: 4 },
    ];
    
    set({ script: mockScript, status: 'ready' });
  },

  updateSegment: (id, updates) => {
    set((state) => ({
      script: state.script.map((s) => (s.id === id ? { ...s, ...updates } : s)),
    }));
  },
}));