from pydantic import BaseModel, Field
from typing import List, Optional

class VideoSegment(BaseModel):
    text: str
    visual_description: str
    duration_estimate: float
    overlay_text: Optional[str] = None
    audio_path: Optional[str] = None
    visual_path: Optional[str] = None

class VideoProject(BaseModel):
    project_id: str
    status: str = "pending"
    prompt: str
    script: List[VideoSegment] = []
    final_video_url: Optional[str] = None
    error: Optional[str] = None