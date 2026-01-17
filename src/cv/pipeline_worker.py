from src.cv.smart_cropper import SmartCropper
from src.cv.scene_generator import SceneGenerator
import logging

class CVPipelineWorker:
    """
    The Orchestrator's CV bridge. Handles asset preparation.
    """
    def __init__(self):
        self.cropper = SmartCropper()
        self.generator = SceneGenerator()
        logging.info("CV Pipeline Worker Initialized")

    def prepare_visuals(self, segments):
        """
        Input: List of segments from Virtual Editor JSON.
        Output: Paths to processed or generated visual assets.
        """
        processed_assets = []
        for segment in segments:
            if segment['type'] == 'gen_ai':
                path = f"outputs/gen_{segment['id']}.png"
                img = self.generator.generate_scene(segment['visual_cue'])
                self.generator.save_scene(img, path)
                processed_assets.append(path)
            elif segment['type'] == 'stock_reframing':
                # Logic to download stock and run self.cropper.process_frame()
                pass
        
        return processed_assets