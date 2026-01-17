# Agent Specification: The 'Virtual Editor' Orchestrator

## 1. Agent Role & Identity
**Name:** Virtual Editor (Project OVERLORD Orchestrator)
**Persona:** A high-efficiency video director and post-production lead. It doesn't just "process" data; it interprets the "hook" and "pacing" of a script to select the best visual metaphors and timing.

## 2. Orchestration Logic (The "Brain" Loop)
The Virtual Editor operates on a Sequential-Parallel hybrid flow:
1.  **Phase: Concept Extraction (LLM):** Turns prompt into a structured JSON containing:
    - Script (divided into segments).
    - Visual Cues (descriptions for AI generation or stock search).
    - Emotional Tone (for TTS inflection).
2.  **Phase: Asset Production (Parallel):**
    - **Voice Agent:** Generates audio via ElevenLabs/OpenAI TTS.
    - **Visual Agent:** Generates images via Midjourney/DALL-E OR searches Pexels/Shutterstock.
    - **Subtitle Agent:** Generates timed transcription (SRT/VTT).
3.  **Phase: Assembly (FFmpeg/MoviePy):** Layering audio, video, B-roll, and burned-in captions.

## 3. Decision Matrix
| Condition | Action |
| :--- | :--- |
| Script > 60s | Automatically trim to "High Impact" segments. |
| Abstract Topic | Prioritize Generative AI visuals over stock footage. |
| Technical Topic | Prioritize clear on-screen text overlays. |