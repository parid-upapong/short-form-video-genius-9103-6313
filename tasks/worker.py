from celery import Celery
from src.agents.orchestrator import VirtualEditorOrchestrator
from src.video_engine.assembly import VideoAssembler

app = Celery('overlord_tasks', broker='redis://localhost:6379/0')

@app.task(name="tasks.generate_full_video")
def generate_full_video_task(prompt: str):
    """
    Entry point for the background worker to start the Virtual Editor loop.
    """
    # Dependency Injection
    orchestrator = VirtualEditorOrchestrator(...)
    assembler = VideoAssembler()
    
    # Run Async Loop inside Celery Worker
    import asyncio
    project_result = asyncio.run(orchestrator.create_video(prompt))
    
    return {"status": "completed", "url": project_result}