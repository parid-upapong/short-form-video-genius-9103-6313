import moviepy.editor as mp
from ..schema.state import VideoProject

class VideoAssembler:
    """
    Handles the programmatic stitching of assets.
    """
    def assemble(self, project: VideoProject, output_path: str):
        clips = []
        
        for segment in project.script:
            # 1. Load Visual (Video or Image)
            clip = mp.VideoFileClip(segment.visual_path).subclip(0, segment.duration_estimate)
            
            # 2. Attach Audio
            audio = mp.AudioFileClip(segment.audio_path)
            clip = clip.set_audio(audio)
            
            # 3. Add Dynamic Overlays (Subtitles/Text)
            if segment.overlay_text:
                txt_clip = mp.TextClip(
                    segment.overlay_text, 
                    fontsize=70, 
                    color='yellow', 
                    font='Arial-Bold',
                    stroke_color='black',
                    stroke_width=2,
                    method='caption',
                    size=(clip.w * 0.8, None)
                ).set_duration(clip.duration).set_position(('center', 'center'))
                
                clip = mp.CompositeVideoClip([clip, txt_clip])
            
            clips.append(clip)

        # 4. Final Concatenation
        final_video = mp.concatenate_videoclips(clips, method="compose")
        final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
        return output_path