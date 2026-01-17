# Computer Vision & Generative Strategy: Project OVERLORD

## 1. Objective
To automate the visual storytelling process by transforming textual "Visual Cues" into high-impact video assets. This involves two core CV disciplines:
1.  **Auto-Cut & Reframing:** Intelligence to transform horizontal footage into vertical (9:16) while keeping the subject centered.
2.  **Scene Generation:** Utilizing Latent Diffusion Models to create bespoke visual overlays when stock footage is unavailable or insufficient.

## 2. Technical Stack
- **OpenCV & MediaPipe:** For real-time face/object tracking and shot boundary detection.
- **PyTorch & Diffusers:** Running Stable Diffusion XL (SDXL) for high-quality scene generation.
- **MoviePy/FFmpeg:** For programmatic timeline assembly.

## 3. The "Smart-Crop" Logic
Instead of a static center crop, our CV engine calculates a "Saliency Score" for each frame:
- **Priority 1:** Human Faces (MediaPipe Face Detection).
- **Priority 2:** Moving Objects (Optical Flow).
- **Priority 3:** Text/Overlays.
The crop window (9:16) smoothly interpolates between these focal points to prevent jarring movement.

## 4. Generative Scene Workflow
1. **Prompt Enhancement:** The Virtual Editor expands a simple cue (e.g., "Cyberpunk city") into a detailed SDXL prompt.
2. **Consistency check:** Using ControlNet or LoRA to maintain visual style across all scenes in a single video.
3. **Temporal Upscaling:** Using interpolation (RIFE) to add subtle motion to static generated images.