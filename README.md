# OVERLORD: Backend Engine

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Start Redis: `docker run -p 6379:6379 redis`
3. Start Worker: `celery -A src.worker.celery_app worker --loglevel=info`
4. Start API: `uvicorn src.main:app --reload`

## Architecture Note
The `VirtualEditorOrchestrator` handles the intelligence of "what" to create, while `VideoRenderer` handles the heavy lifting of FFmpeg via MoviePy to "build" the binary file.