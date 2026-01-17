from fastapi import FastAPI, HTTPException, BackgroundTasks
from src.models.schemas import VideoRequest, VideoStatus
from src.worker import generate_video_task
import uuid

app = FastAPI(title="Project OVERLORD - AI Video Engine")

# Simple in-memory store for MVP status (Use Redis for Production)
jobs = {}

@app.post("/generate", response_model=VideoStatus)
async def create_video_job(request: VideoRequest):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "PENDING", "progress": 0}
    
    # Trigger Celery Task
    generate_video_task.delay(job_id, request.dict())
    
    return {
        "job_id": job_id,
        "status": "PENDING",
        "progress": 0
    }

@app.get("/status/{job_id}", response_model=VideoStatus)
async def get_status(job_id: str):
    # In a real scenario, we'd fetch from Celery result backend or Redis
    from src.worker import celery_app
    res = celery_app.AsyncResult(job_id)
    
    # Mocking status retrieval for logic demonstration
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return {
        "job_id": job_id,
        **jobs[job_id]
    }