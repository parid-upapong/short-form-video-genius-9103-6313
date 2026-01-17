import os
from moviepy.editor import (
    TextClip, AudioFileClip, ImageClip, 
    VideoFileClip, CompositeVideoClip, concatenate_videoclips
)

class VideoComposer:
    def __init__(self, project_id):
        self.project_id = project_id
        self.output_dir = f"/tmp/overlord/{project_id}"
        os.makedirs(self.output_dir, exist_ok=True)

    def render(self, script_data, audio_path, visual_assets):
        """
        Engineers the video using MoviePy/FFmpeg.
        """
        clips = []
        audio = AudioFileClip(audio_path)
        
        for segment, asset in zip(script_data['segments'], visual_assets):
            duration = segment['duration']
            
            # Create Visual Base
            if asset['type'] == 'image':
                clip = ImageClip(asset['path']).set_duration(duration)
            else:
                clip = VideoFileClip(asset['path']).subclip(0, duration)
            
            # Add dynamic captions/subtitles
            txt_clip = TextClip(
                segment['text'], 
                fontsize=70, 
                color='white', 
                font='Arial-Bold',
                stroke_color='black',
                stroke_width=2,
                method='caption',
                size=(1080 * 0.8, None)
            ).set_duration(duration).set_position(('center', 1400)) # TikTok style positioning
            
            video_segment = CompositeVideoClip([clip.resize(height=1920), txt_clip])
            clips.append(video_segment)

        # Stitch everything together
        final_video = concatenate_videoclips(clips, method="compose")
        final_video = final_video.set_audio(audio)
        
        output_path = f"{self.output_dir}/final_short.mp4"
        
        # Export with optimized settings for mobile
        final_video.write_videofile(
            output_path, 
            fps=30, 
            codec="libx264", 
            audio_codec="aac",
            threads=4,
            preset="ultrafast" # Priority on speed for MVP
        )
        
        # In production, we would upload to S3 here
        # upload_to_s3(output_path)
        
        return output_path