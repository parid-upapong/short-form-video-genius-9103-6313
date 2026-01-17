import os
import cv2
import pytest
import numpy as np
from pathlib import Path

# Configuration for Video Standards
EXPECTED_WIDTH = 1080
EXPECTED_HEIGHT = 1920
EXPECTED_FPS = 30.0
MAX_VIDEO_DURATION_SECONDS = 60
MIN_VIDEO_DURATION_SECONDS = 15

def get_video_properties(filepath):
    """Utility to extract metadata using OpenCV."""
    cap = cv2.VideoCapture(filepath)
    if not cap.isOpened():
        return None
    
    properties = {
        "width": int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        "height": int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        "fps": cap.get(cv2.CAP_PROP_FPS),
        "frame_count": int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),
    }
    properties["duration"] = properties["frame_count"] / properties["fps"]
    cap.release()
    return properties

@pytest.mark.parametrize("video_sample", [str(p) for p in Path("tests/samples/renders").glob("*.mp4")])
class TestVideoIntegrity:
    """Automated checks for rendered MP4 output quality and specs."""

    def test_resolution_9_16(self, video_sample):
        """Ensure video is vertical (Shorts/TikTok/Reels format)."""
        props = get_video_properties(video_sample)
        assert props["width"] == EXPECTED_WIDTH, f"Invalid width: {props['width']}"
        assert props["height"] == EXPECTED_HEIGHT, f"Invalid height: {props['height']}"

    def test_frame_rate(self, video_sample):
        """Ensure smooth playback at 30fps."""
        props = get_video_properties(video_sample)
        assert props["fps"] == pytest.approx(EXPECTED_FPS, abs=0.1)

    def test_duration_bounds(self, video_sample):
        """Ensure the video stays within MVP constraints."""
        props = get_video_properties(video_sample)
        assert MIN_VIDEO_DURATION_SECONDS <= props["duration"] <= MAX_VIDEO_DURATION_SECONDS

    def test_no_black_frames(self, video_sample):
        """Detect render failures where frames are empty/black."""
        cap = cv2.VideoCapture(video_sample)
        success, frame = cap.read()
        black_frame_count = 0
        total_frames = 0

        while success:
            if np.mean(frame) < 2.0:  # Threshold for 'nearly black'
                black_frame_count += 1
            total_frames += 1
            success, frame = cap.read()
        cap.release()

        black_ratio = black_frame_count / total_frames
        assert black_ratio < 0.05, f"Video has too many black frames ({black_ratio:.2%})"

    def test_audio_stream_exists(self, video_sample):
        """Verify the FFmpeg stitch included an audio track (TTS)."""
        # Note: CV2 doesn't handle audio well, using FFprobe logic via shell
        import subprocess
        cmd = f"ffprobe -i {video_sample} -show_streams -select_streams a -loglevel error"
        output = subprocess.check_output(cmd, shell=True).decode()
        assert "codec_type=audio" in output, "No audio stream found in render"