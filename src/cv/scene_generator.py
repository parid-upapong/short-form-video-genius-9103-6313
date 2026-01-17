import torch
from diffusers import StableDiffusionXLPipeline, EulerDiscreteScheduler
from PIL import Image

class SceneGenerator:
    """
    Generates high-quality visual assets based on the Virtual Editor's cues.
    Optimized for SDXL Turbo for speed (< 10s per image).
    """
    def __init__(self, device="cuda" if torch.cuda.is_available() else "cpu"):
        self.model_id = "stabilityai/sdxl-turbo"
        self.pipe = StableDiffusionXLPipeline.from_pretrained(
            self.model_id, 
            torch_dtype=torch.float16 if device == "cuda" else torch.float32, 
            variant="fp16" if device == "cuda" else None
        )
        self.pipe.to(device)
        self.pipe.scheduler = EulerDiscreteScheduler.from_config(self.pipe.scheduler.config)

    def generate_scene(self, visual_cue: str, style_preset: str = "cinematic"):
        """
        Transforms a visual cue into a 1024x1024 image.
        """
        full_prompt = f"{visual_cue}, {style_preset}, high resolution, 4k, professional lighting, photorealistic"
        
        # Generate image (1 step for Turbo, or 20-30 for standard SDXL)
        image = self.pipe(
            prompt=full_prompt, 
            num_inference_steps=1, 
            guidance_scale=0.0
        ).images[0]
        
        return image

    def save_scene(self, image: Image, path: str):
        # Resize to vertical-friendly dimensions before saving
        # Note: SDXL is trained on square, we crop/pad later in assembly
        image.save(path)

# Usage Example:
# gen = SceneGenerator()
# img = gen.generate_scene("A futuristic laboratory with holographic displays")
# gen.save_scene(img, "assets/scene_01.png")