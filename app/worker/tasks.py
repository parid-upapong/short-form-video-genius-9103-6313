import time
from .celery_app import celery_app
from .video_composer import VideoComposer
# Mock wrappers for AI Services
from .services import ScriptEngine, AudioEngine, VisualEngine

@celery_app.task(bind=True)
def generate_video_task(self, project_id, user_prompt, style_preset):
    """
    The main orchestration task for video generation.
    """
    try:
        # Step 1: Generate Script
        self.update_state(state='PROGRESS', meta={'progress': 10, 'status': 'Generating script...'})
        script_data = ScriptEngine.generate(user_prompt, style_preset)
        
        # Step 2: Generate Audio (TTS)
        self.update_state(state='PROGRESS', meta={'progress': 30, 'status': 'Creating voiceover...'})
        audio_path = AudioEngine.generate_full_audio(script_data['segments'])
        
        # Step 3: Source Visuals (Images/Stock)
        self.update_state(state='PROGRESS', meta={'progress': 50, 'status': 'Sourcing visuals...'})
        visual_assets = VisualEngine.get_assets(script_data['segments'])
        
        # Step 4: Video Composition (The bottleneck)
        self.update_state(state='PROGRESS', meta={'progress': 70, 'status': 'Assembling video...'})
        composer = VideoComposer(project_id)
        final_video_url = composer.render(
            script_data=script_data,
            audio_path=audio_path,
            visual_assets=visual_assets
        )
        
        return {
            'status': 'COMPLETED',
            'video_url': final_video_url,
            'project_id': project_id
        }

    except Exception as e:
        self.update_state(state='FAILURE', meta={'exc': str(e)})
        raise e