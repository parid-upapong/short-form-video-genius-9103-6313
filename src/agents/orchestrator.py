import asyncio
from typing import Dict
from .prompts import SCRIPT_GEN_PROMPT
from ..schema.state import VideoProject, VideoSegment

class VirtualEditorOrchestrator:
    """
    The central hub that coordinates LLMs, TTS, and Video Generation.
    """
    def __init__(self, llm_provider, tts_engine, asset_manager):
        self.llm = llm_provider
        self.tts = tts_engine
        self.assets = asset_manager

    async def create_video(self, prompt: str) -> str:
        # 1. Generate Structured Script
        print(f"[*] Orchestrator: Generating script for: {prompt}")
        script_data = await self.llm.generate_json(SCRIPT_GEN_PROMPT, prompt)
        
        project = VideoProject(
            project_id="vid_123", # UUID in production
            prompt=prompt,
            script=[VideoSegment(**s) for s in script_data['segments']]
        )

        # 2. Parallel Asset Generation (Voice & Visuals)
        tasks = []
        for segment in project.script:
            tasks.append(self._process_segment(segment))
        
        await asyncio.gather(*tasks)

        # 3. Trigger Rendering
        print("[*] Orchestrator: Sending to Rendering Engine...")
        render_task = await self.assets.render_video(project)
        
        return render_task

    async def _process_segment(self, segment: VideoSegment):
        """Processes a single segment: Voice + Visuals in parallel."""
        audio_task = self.tts.generate_audio(segment.text)
        visual_task = self.assets.find_or_generate_visual(segment.visual_description)
        
        segment.audio_path, segment.visual_path = await asyncio.gather(
            audio_task, visual_task
        )