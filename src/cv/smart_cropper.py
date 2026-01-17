import cv2
import mediapipe as mp
import numpy as np

class SmartCropper:
    """
    Automated 9:16 Reframing Engine.
    Detects the most important subject (ROI) and centers the crop window.
    """
    def __init__(self, target_ratio=(9, 16)):
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)
        self.target_ratio = target_ratio

    def get_crop_coordinates(self, frame):
        h, w, _ = frame.shape
        target_w = int(h * (self.target_ratio[0] / self.target_ratio[1]))
        
        # Default center
        center_x = w // 2
        
        # Detect ROI (Faces)
        results = self.face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        if results.detections:
            # Get the first face detected
            bbox = results.detections[0].location_data.relative_bounding_box
            face_center_x = int((bbox.xmin + bbox.width / 2) * w)
            center_x = face_center_x

        # Clamping to frame boundaries
        left = max(0, center_x - target_w // 2)
        right = min(w, left + target_w)
        
        # Adjust if right boundary exceeded
        if right == w:
            left = w - target_w
            
        return left, 0, right, h

    def process_frame(self, frame):
        left, top, right, bottom = self.get_crop_coordinates(frame)
        return frame[top:bottom, left:right]

# Usage Example:
# cropper = SmartCropper()
# vertical_frame = cropper.process_frame(landscape_frame)