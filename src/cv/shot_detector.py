import cv2

class ShotDetector:
    """
    Detects scene changes (cuts) in source footage to assist Auto-Cut logic.
    """
    def __init__(self, threshold=30.0):
        self.threshold = threshold

    def detect_cuts(self, video_path):
        cap = cv2.VideoCapture(video_path)
        prev_frame = None
        cut_timestamps = []
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Convert to grayscale and blur to reduce noise
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)

            if prev_frame is not None:
                # Calculate Absolute Difference
                frame_diff = cv2.absdiff(gray, prev_frame)
                mean_diff = np.mean(frame_diff)

                if mean_diff > self.threshold:
                    timestamp = frame_count / fps
                    cut_timestamps.append(timestamp)

            prev_frame = gray
            frame_count += 1

        cap.release()
        return cut_timestamps

# Integration Note:
# This allows the Virtual Editor to know where existing B-roll has cuts,
# ensuring that TTS-aligned overlays don't clash with existing visual transitions.