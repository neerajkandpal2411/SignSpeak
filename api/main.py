from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from speech.text_to_speech import speak
import os
import json

app = FastAPI(title="Gesture Recognition API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GestureRequest(BaseModel):
    text: str

class FeedbackRequest(BaseModel):
    gesture: str
    correct: bool

@app.get("/")
def home():
    return {"status": "Gesture Recognition Backend Running"}

@app.post("/speak")
def speak_text(req: GestureRequest):
    speak(req.text)
    return {"spoken": req.text}

@app.get("/gestures")
def get_gestures():
    """Return list of available gestures"""
    gestures = sorted(os.listdir("data/processed_frames"))
    return {"gestures": gestures}

@app.get("/model/info")
def get_model_info():
    """Return model architecture information"""
    return {
        "model_type": "CNN + LSTM",
        "sequence_length": 30,
        "input_shape": [30, 21, 3],
        "gesture_classes": len(os.listdir("data/processed_frames")),
        "confidence_threshold": 0.7
    }