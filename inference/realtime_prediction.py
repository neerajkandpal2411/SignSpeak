import os
from collections import deque

os.environ["MEDIAPIPE_DISABLE_TASKS"] = "1"
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

import cv2
import numpy as np
import tensorflow as tf
from mediapipe.python.solutions import drawing_utils as mp_draw
from mediapipe.python.solutions import hands as mp_hands
from models.lstm_model import build_lstm
from speech.text_to_speech import speak

class GestureRecognizer:
    def __init__(self, sequence_length=30, confidence_threshold=0.7):
        self.SEQUENCE_LENGTH = sequence_length
        self.confidence_threshold = confidence_threshold
        
        # Load gesture labels
        self.gesture_labels = sorted(os.listdir("data/processed_frames"))
        self.NUM_CLASSES = len(self.gesture_labels)
        
        # Load model
        self.model = build_lstm(num_classes=self.NUM_CLASSES)
        self.model.load_weights("models/gesture_model.weights.h5")
        
        # Initialize MediaPipe
        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        
        self.sequence = deque(maxlen=self.SEQUENCE_LENGTH)
        self.last_spoken_gesture = None
        
    def process_frame(self, frame):
        """Process a single frame and return prediction"""
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image)
        
        prediction_info = {
            "gesture": None,
            "confidence": 0.0,
            "landmarks_detected": False,
            "speak": False
        }
        
        if results.multi_hand_landmarks:
            prediction_info["landmarks_detected"] = True
            
            for hand in results.multi_hand_landmarks:
                landmarks = []
                for lm in hand.landmark:
                    landmarks.append([lm.x, lm.y, lm.z])
                
                self.sequence.append(landmarks)
                
                # Draw landmarks on frame
                mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
                
                if len(self.sequence) == self.SEQUENCE_LENGTH:
                    input_data = np.expand_dims(np.array(self.sequence), axis=0)
                    prediction = self.model.predict(input_data, verbose=0)[0]
                    
                    confidence = np.max(prediction)
                    gesture = self.gesture_labels[np.argmax(prediction)]
                    
                    prediction_info["confidence"] = float(confidence)
                    prediction_info["gesture"] = gesture if confidence >= self.confidence_threshold else "Unknown"
                    
                    # Check if should speak
                    if (prediction_info["gesture"] != "Unknown" and 
                        prediction_info["gesture"] != self.last_spoken_gesture):
                        prediction_info["speak"] = True
                        self.last_spoken_gesture = prediction_info["gesture"]
        
        return frame, prediction_info
    
    def speak_gesture(self, gesture):
        """Convert gesture to speech"""
        speak(gesture)
    
    def release(self):
        """Clean up resources"""
        self.hands.close()