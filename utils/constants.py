"""Application constants and configuration"""

# App Configuration
APP_NAME = "SignSpeak"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Real-Time Sign Language Recognition System"

# Model Configuration
SEQUENCE_LENGTH = 30
NUM_LANDMARKS = 21
NUM_COORDINATES = 3
CONFIDENCE_THRESHOLD = 0.7

# Gesture Classes
GESTURES = [
    "hello", "thanks", "yes", "no", "help",
    "i love you", "stop", "please", "time", "friend"
]

# Color Scheme
COLORS = {
    'primary': '#2E4057',
    'secondary': '#F18F01',
    'accent': '#048BA8',
    'success': '#28A745',
    'warning': '#FFC107',
    'danger': '#DC3545',
    'light': '#F8F9FA',
    'dark': '#343A40'
}

# API Configuration
API_HOST = "127.0.0.1"
API_PORT = 8000
API_URL = f"http://{API_HOST}:{API_PORT}"

# File Paths
MODEL_PATH = "models/gesture_model.weights.h5"
DATA_PATH = "data/processed_frames"
ASSETS_PATH = "assets"
GRAPHS_PATH = "assets/graphs"