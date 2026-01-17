# System Architecture: Scalable Video Processing Pipeline (Project OVERLORD)

## 1. Architectural Strategy
To achieve the goal of generating high-quality short videos in under 120 seconds, we utilize an **Asynchronous Event-Driven Architecture**. This decouples the user-facing API from the resource-intensive video rendering process, allowing for horizontal scaling of worker nodes.

## 2. Core Components
- **API Gateway (FastAPI):** Handles user requests, authentication, and status polling.
- **Message Broker (Redis/RabbitMQ):** Orchestrates the task queue for video generation.
- **Orchestrator Worker (Celery):** Manages the lifecycle of a video project (Script -> Voice -> Visuals -> Assembly).
- **Asset Storage (AWS S3/GCS):** Stores intermediate assets (audio clips, generated images) and final MP4 files.
- **State Store (PostgreSQL + Redis):** Tracks job metadata and real-time progress percentages.

## 3. The Pipeline Flow
1. **Script Stage:** LLM generates a structured JSON (Script, Visual Cues, Timestamps).
2. **Audio Stage:** Parallelized TTS generation for each script segment.
3. **Visual Stage:** Concurrent fetching of stock footage or generation of AI images.
4. **Composition Stage:** FFmpeg/MoviePy engine stitches assets, adds background music, and overlays dynamic captions.
5. **Optimization Stage:** Final compression and metadata tagging for TikTok/Reels specifications.

## 4. Infrastructure Diagram (Conceptual)
`[User] -> [FastAPI] -> [Redis Queue] -> [Worker Cluster (Auto-scaling)]`
`                                          |-> [LLM API]`
`                                          |-> [TTS API]`
`                                          |-> [Image Gen API/Stock API]`
`                                          |-> [FFmpeg Engine]`