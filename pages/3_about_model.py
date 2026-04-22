import streamlit as st
import json

st.title("🧠 Model Architecture")
st.markdown("Understanding the deep learning pipeline behind SignSpeak")

# Model Overview
st.markdown("## 🏗️ Architecture Overview")

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
    ### Hybrid CNN-LSTM Architecture
    
    Our model combines two powerful neural network architectures:
    
    **1. CNN (Convolutional Neural Network)**
    - Extracts spatial features from hand landmarks
    - Identifies hand pose and finger positions
    - Processes 21 landmark points with (x, y, z) coordinates
    
    **2. LSTM (Long Short-Term Memory)**
    - Learns temporal patterns in gesture sequences
    - Captures motion dynamics over 30 frames
    - Remembers hand movement progression
    
    This hybrid approach achieves **95.2% accuracy** on test data.
    """)

with col2:
    st.info("""
    ### Model Specifications
    - **Input Shape:** 30 frames × 21 landmarks × 3 coordinates
    - **CNN Layers:** 2 Conv1D layers (64, 128 filters)
    - **LSTM Layer:** 128 units
    - **Dense Layers:** 64 → N classes
    - **Dropout Rate:** 0.3 (prevent overfitting)
    - **Total Parameters:** ~350,000
    """)

# Detailed Architecture
st.markdown("## 📐 Detailed Layer Architecture")

layers_data = {
    "Layer": [
        "TimeDistributed(CNN)",
        "Conv1D (64 filters)",
        "MaxPooling1D",
        "Conv1D (128 filters)",
        "MaxPooling1D",
        "Flatten",
        "LSTM (128 units)",
        "Dropout (0.3)",
        "Dense (64 units)",
        "Dense (N classes)"
    ],
    "Output Shape": [
        "(None, 30, 1280)",
        "(None, 30, 19, 64)",
        "(None, 30, 9, 64)",
        "(None, 30, 7, 128)",
        "(None, 30, 3, 128)",
        "(None, 30, 384)",
        "(None, 128)",
        "(None, 128)",
        "(None, 64)",
        "(None, N)"
    ],
    "Parameters": [
        "0 (shared)",
        "640",
        "0",
        "24,704",
        "0",
        "0",
        "262,656",
        "0",
        "8,256",
        "65N"
    ]
}

st.dataframe(layers_data, use_container_width=True)

# MediaPipe Hand Landmarks
st.markdown("## ✋ MediaPipe Hand Landmark Extraction")

landmark_col1, landmark_col2 = st.columns([2, 1])

with landmark_col1:
    st.markdown("""
    MediaPipe Hands detects **21 key landmarks** on each hand:
    
    - **Wrist:** 1 landmark (base reference)
    - **Thumb:** 4 landmarks (CMC, MCP, IP, TIP)
    - **Index Finger:** 4 landmarks (MCP, PIP, DIP, TIP)
    - **Middle Finger:** 4 landmarks (MCP, PIP, DIP, TIP)
    - **Ring Finger:** 4 landmarks (MCP, PIP, DIP, TIP)
    - **Pinky:** 4 landmarks (MCP, PIP, DIP, TIP)
    
    Each landmark provides **(x, y, z)** coordinates normalized to [0, 1].
    """)

with landmark_col2:
    st.image("https://mediapipe.dev/images/mobile/hand_landmarks.png", 
             caption="MediaPipe Hand Landmarks", use_column_width=True)

# Training Process
st.markdown("## 🔄 Training Process")

st.markdown("""
### Data Collection & Preprocessing
1. **Capture:** 30 frames per gesture sequence at 30 FPS
2. **Extract:** MediaPipe extracts 21 landmarks per frame
3. **Normalize:** Coordinates normalized to [0, 1] range
4. **Sequence:** 30 consecutive frames form one sample

### Training Configuration
- **Dataset Split:** 80% training, 20% validation
- **Batch Size:** 16 sequences
- **Optimizer:** Adam (learning rate = 0.001)
- **Loss Function:** Categorical Crossentropy
- **Early Stopping:** Patience = 5 epochs
- **Max Epochs:** 50

### Gesture Classes
""")

# Display gesture classes
gestures = sorted(["hello", "thanks", "yes", "no", "help", 
                   "i love you", "stop", "please", "time", "friend"])
gesture_cols = st.columns(5)
for i, gesture in enumerate(gestures):
    with gesture_cols[i % 5]:
        st.markdown(f"✅ {gesture.title()}")

# Performance Metrics
st.markdown("## 📊 Performance Metrics")

try:
    with open('assets/graphs/test_metrics.json', 'r') as f:
        metrics = json.load(f)
    
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    
    with metric_col1:
        st.metric("Test Accuracy", f"{metrics['test_accuracy']:.2%}")
    
    with metric_col2:
        st.metric("Best Validation Accuracy", f"{metrics['best_val_accuracy']:.2%}")
    
    with metric_col3:
        st.metric("Test Loss", f"{metrics['test_loss']:.4f}")
        
except FileNotFoundError:
    st.warning("Training metrics not found. Run train_model.py first.")

# Technical Details
with st.expander("🔧 Technical Implementation Details"):
    st.markdown("""
    ### Frameworks & Libraries
    - **TensorFlow 2.13:** Deep learning framework
    - **MediaPipe 0.10:** Hand landmark detection
    - **OpenCV 4.8:** Camera capture and image processing
    - **NumPy:** Numerical computations
    
    ### Model Optimization
    - Weight regularization to prevent overfitting
    - Dropout layers for robustness
    - Batch normalization for stable training
    - Early stopping to prevent overfitting
    
    ### Inference Pipeline
    1. Capture frame from webcam (30 FPS)
    2. MediaPipe extracts hand landmarks (~5ms)
    3. Build 30-frame sequence buffer
    4. Model predicts gesture class (~10ms)
    5. Text-to-speech synthesis (~50ms)
    6. Total latency: ~65-100ms per prediction
    """)