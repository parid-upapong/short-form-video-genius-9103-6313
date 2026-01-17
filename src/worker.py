import os
from celery import Celery
from src.engine.renderer import VideoRenderer
from src.tasks.video_tasks import VirtualEditorOrchestrator

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
celery_app = Celery("video_worker", broker=CELERY_BROKER_URL, backend=CELERY_BROKER_URL)

@celery_app.task(name="generate_video_task", bind=True)
def generate_video_task(self, job_id: str, request_data: dict):
    """
    Orchestrates the Virtual Editor's workflow.
    """
    orchestrator = VirtualEditorOrchestrator(job_id)
    
    try:
        # 1. Concept Extraction (Scripting)
        self.update_state(state='PROCESSING', meta={'progress': 10})
        script_data = orchestrator.generate_script(request_data['prompt'])
        
        # 2. Asset Production (Parallel Audio & Visual Generation)
        self.update_state(state='PROCESSING', meta={'progress': 30})
        assets = orchestrator.produce_assets(script_data)
        
        # 3. Video Assembly (Rendering)
        self.update_state(state='PROCESSING', meta={'progress': 70})
        renderer = VideoRenderer(job_id)
        final_video_path = renderer.assemble_video(assets)
        
        # 4. Upload & Cleanup
        video_url = orchestrator.upload_to_s3(final_video_path)
        
        return {"status": "COMPLETED", "video_url": video_url}
        
    except Exception as e:
        self.update_state(state='FAILED', meta={'exc': str(e)})
        raise e