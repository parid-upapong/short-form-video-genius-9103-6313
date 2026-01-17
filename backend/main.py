from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from services.ai_engine import generate_video_content
from services.video_engine import assemble_video

app = FastAPI(title="AI Video Revolution API")

class VideoRequest(BaseModel):
    prompt: str
    target_platform: str  # tiktok, reels, shorts
    voice_id: str = "21m00Tcm4TlvDq8ikWAM" # Default Rachel

@app.post("/generate-video")
async def create_video(request: VideoRequest, background_tasks: BackgroundTasks):
    # 1. Immediate Response with Task ID
    task_id = "task_" + str(hash(request.prompt))
    
    # 2. Run the heavy lifting in background
    background_tasks.add_task(workflow_orchestrator, request, task_id)
    
    return {"status": "processing", "task_id": task_id}

async def workflow_orchestrator(request: VideoRequest, task_id: str):
    # Step 1: Script & Scene Planning
    content = await generate_video_content(request.prompt)
    
    # Step 2: Assemble (Voiceover + Images + Overlay)
    video_path = await assemble_video(content, task_id)
    
    print(f"Video ready at: {video_path}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)