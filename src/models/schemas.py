from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class VideoRequest(BaseModel):
    prompt: str = Field(..., example="A short motivational video about productivity for software engineers.")
    style: str = Field(default="modern", example="dark_minimalist")
    duration_seconds: int = Field(default=30, ge=15, le=60)
    aspect_ratio: str = Field(default="9:16")

class VideoStatus(BaseModel):
    job_id: str
    status: str # PENDING, PROCESSING, COMPLETED, FAILED
    progress: int
    video_url: Optional[str] = None
    metadata: Optional[Dict] = None

class ScriptSegment(BaseModel):
    text: str
    visual_cue: str
    duration: float