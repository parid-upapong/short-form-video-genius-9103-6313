from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from .worker.tasks import generate_video_task
import uuid

app = FastAPI(title="OVERLORD API")

class VideoRequest(BaseModel):
    prompt: str
    style_preset: str = "modern_minimalist"

@app.post("/generate-video")
async def create_video(request: VideoRequest):
    project_id = str(uuid.uuid4())
    
    # Push to Celery worker queue
    task = generate_video_task.delay(
        project_id=project_id,
        user_prompt=request.prompt,
        style_preset=request.style_preset
    )
    
    return {
        "project_id": project_id,
        "task_id": task.id,
        "status": "QUEUED"
    }

@app.get("/status/{task_id}")
async def get_status(task_id: str):
    from .worker.celery_app import celery_app
    task_result = celery_app.AsyncResult(task_id)
    
    return {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result if task_result.ready() else task_result.info
    }