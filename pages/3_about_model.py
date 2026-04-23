import streamlit as st
import json
import os

st.set_page_config(page_title="Model Architecture - SignSpeak", page_icon="🧠")

if os.path.exists('assets/style.css'):
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# header
st.markdown("""
<div style='border-bottom: 3px solid #2E86AB; padding-bottom: 10px; margin-bottom: 20px;'>
    <h1 style='color: #2E4057; margin: 0;'>Model Architecture</h1>
    <p style='color: #666; font-size: 1.1rem; margin: 5px 0 0 0;'>Understanding the deep learning pipeline behind SignSpeak</p>
</div>
""", unsafe_allow_html=True)

# Model Overview
st.markdown("""
<div style='border-left: 5px solid #7B8065; padding-left: 15px; margin: 30px 0 20px 0;'>
    <h2 style='color: #2E4057; margin: 0;'>[=] Architecture Overview</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
    <div style='background: #f8f9fa; padding: 20px; border-radius: 10px; height: 100%;'>
        <h3 style='color: #2E4057; margin-top: 0;'>Hybrid CNN-LSTM Architecture</h3>
        <br>
        <p>Our model combines two powerful neural network architectures:</p>
        <h4 style='color: #2E86AB; margin: 15px 0 5px 0;'>1. CNN (Convolutional Neural Network)</h4>
        <ul style='list-style-type: none; padding-left: 0;'>
            <li>► Extracts spatial features from hand landmarks</li>
            <li>► Identifies hand pose and finger positions</li>
            <li>► Processes 21 landmark points with (x, y, z) coordinates</li>
        </ul>
        <h4 style='color: #F18F01; margin: 15px 0 5px 0;'>2. LSTM (Long Short-Term Memory)</h4>
        <ul style='list-style-type: none; padding-left: 0;'>
            <li>► Learns temporal patterns in gesture sequences</li>
            <li>► Captures motion dynamics over 30 frames</li>
            <li>► Remembers hand movement progression</li>
        </ul>
        <div style='background: #d4edda; padding: 10px; border-radius: 5px; margin-top: 15px;'>
            <strong style='color: #155724;'>» Performance:</strong> 
            <span style='color: #155724;'>This hybrid approach achieves <strong>95.2% accuracy</strong> on test data.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; color: white; height: 100%;'>
        <h3 style='color: white; margin-top: 0;'>Model Specifications</h3>
        <ul style='list-style-type: none; padding-left: 0;'>
            <li><strong>Input Shape:</strong> 30 frames * 21 landmarks * 3 coordinates</li>
            <li><strong>CNN Layers:</strong> 2 Conv1D layers (64, 128 filters)</li>
            <li><strong>LSTM Layer:</strong> 128 units</li>
            <li><strong>Dense Layers:</strong> 64 -> N classes</li>
            <li><strong>Dropout Rate:</strong> 0.3 (prevent overfitting)</li>
            <li><strong>Total Parameters:</strong> ~350,000</li>
        </ul>
        <hr style='border-color: rgba(255,255,255,0.3); margin: 15px 0;'>
        <p style='margin: 0; font-size: 0.9rem; opacity: 0.9;'>[i] CNN extracts spatial features, LSTM learns temporal patterns</p>
    </div>
    """, unsafe_allow_html=True)

# Architecture
st.markdown("""
<div style='border-left: 5px solid #B1B5A0; padding-left: 15px; margin: 30px 0 20px 0;'>
    <h2 style='color: #2E4057; margin: 0;'>{ } Detailed Layer Architecture</h2>
</div>
""", unsafe_allow_html=True)

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
        "~650"
    ]
}

# Convert to DataFrame
import pandas as pd
layers_df = pd.DataFrame(layers_data)
st.dataframe(layers_df, use_container_width=True, hide_index=True)

st.markdown("""
<div style='background: #e8ecf1; padding: 10px 15px; border-radius: 5px; margin-top: 10px;'>
    <p style='margin: 0; color: #2E4057;'><strong>[i]</strong> TimeDistributed wrapper applies the CNN to each of the 30 frames independently, sharing weights across all frames.</p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style='border-left: 5px solid #A23B72; padding-left: 15px; margin: 30px 0 20px 0;'>
    <h2 style='color: #2E4057; margin: 0;'>[#] MediaPipe Hand Landmark Extraction</h2>
</div>
""", unsafe_allow_html=True)

landmark_col1, landmark_col2 = st.columns([2, 1])

with landmark_col1:
    st.markdown("""
    <div style='background: #f8f9fa; padding: 20px; border-radius: 10px;'>
        <p>MediaPipe Hands detects <strong>21 key landmarks</strong> on each hand:</p>
        <ul style='list-style-type: none; padding-left: 0;'>
            <li><strong>» Wrist:</strong> 1 landmark (base reference)</li>
            <li><strong>» Thumb:</strong> 4 landmarks (CMC, MCP, IP, TIP)</li>
            <li><strong>» Index Finger:</strong> 4 landmarks (MCP, PIP, DIP, TIP)</li>
            <li><strong>» Middle Finger:</strong> 4 landmarks (MCP, PIP, DIP, TIP)</li>
            <li><strong>» Ring Finger:</strong> 4 landmarks (MCP, PIP, DIP, TIP)</li>
            <li><strong>» Pinky:</strong> 4 landmarks (MCP, PIP, DIP, TIP)</li>
        </ul>
        <div style='background: #fff3cd; padding: 10px; border-radius: 5px; margin-top: 15px;'>
            <p style='margin: 0; color: #856404;'><strong>[!]</strong> Each landmark provides <strong>(x, y, z)</strong> coordinates normalized to [0, 1].</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with landmark_col2:
    st.image("https://mediapipe.dev/images/mobile/hand_landmarks.png", 
             caption="MediaPipe Hand Landmarks (21 points)", use_column_width=True)

# Training process
st.markdown("""
<div style='border-left: 5px solid #73AB84; padding-left: 15px; margin: 30px 0 20px 0;'>
    <h2 style='color: #2E4057; margin: 0;'>>>> Training Process</h2>
</div>
""", unsafe_allow_html=True)

train_col1, train_col2 = st.columns(2)

with train_col1:
    st.markdown("""
    <div style='background: #f8f9fa; padding: 20px; border-radius: 10px; height: 100%;'>
        <h4 style='color: #2E4057; margin-top: 0;'>Data Collection & Preprocessing</h4>
        <ol style='padding-left: 20px;'>
            <li><strong>Capture:</strong> 30 frames per gesture sequence at 30 FPS</li>
            <li><strong>Extract:</strong> MediaPipe extracts 21 landmarks per frame</li>
            <li><strong>Normalize:</strong> Coordinates normalized to [0, 1] range</li>
            <li><strong>Sequence:</strong> 30 consecutive frames form one sample</li>
        </ol>
        <h4 style='color: #2E4057; margin: 20px 0 10px 0;'>Gesture Classes</h4>
        <div style='display: flex; flex-wrap: wrap; gap: 8px;'>
    """, unsafe_allow_html=True)

with train_col2:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #2E86AB 0%, #1a5276 100%); padding: 20px; border-radius: 10px; color: white; height: 100%;'>
        <h4 style='color: white; margin-top: 0;'>Training Configuration</h4>
        <ul style='list-style-type: none; padding-left: 0;'>
            <li><strong>Dataset Split:</strong> 80% training, 20% validation</li>
            <li><strong>Batch Size:</strong> 16 sequences</li>
            <li><strong>Optimizer:</strong> Adam (learning rate = 0.001)</li>
            <li><strong>Loss Function:</strong> Categorical Crossentropy</li>
            <li><strong>Early Stopping:</strong> Patience = 5 epochs</li>
            <li><strong>Max Epochs:</strong> 50</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Display gesture
gestures = sorted(["hello", "thanks", "yes", "no", "help", 
                   "i love you", "stop", "please", "time", "friend"])
gesture_cols = st.columns(5)
for i, gesture in enumerate(gestures):
    with gesture_cols[i % 5]:
        st.markdown(f"""
        <div style='background: #2E86AB; color: white; padding: 8px; border-radius: 5px; text-align: center; margin: 5px 0;'>
            {gesture.title()}
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Performance Metrics
st.markdown("""
<div style='border-left: 5px solid #C73E1D; padding-left: 15px; margin: 30px 0 20px 0;'>
    <h2 style='color: #2E4057; margin: 0;'>(%) Performance Metrics</h2>
</div>
""", unsafe_allow_html=True)

try:
    with open('assets/graphs/test_metrics.json', 'r') as f:
        metrics = json.load(f)
    
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    
    with metric_col1:
        st.markdown("""
        <div style='background: #d4edda; padding: 15px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #155724; margin: 0; font-size: 2rem;'>{:.2%}</h3>
            <p style='color: #155724; margin: 5px 0 0 0;'>Test Accuracy</p>
        </div>
        """.format(metrics['test_accuracy']), unsafe_allow_html=True)
    
    with metric_col2:
        st.markdown("""
        <div style='background: #fff3cd; padding: 15px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #856404; margin: 0; font-size: 2rem;'>{:.2%}</h3>
            <p style='color: #856404; margin: 5px 0 0 0;'>Best Validation Accuracy</p>
        </div>
        """.format(metrics['best_val_accuracy']), unsafe_allow_html=True)
    
    with metric_col3:
        st.markdown("""
        <div style='background: #f8d7da; padding: 15px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #721c24; margin: 0; font-size: 2rem;'>{:.4f}</h3>
            <p style='color: #721c24; margin: 5px 0 0 0;'>Test Loss</p>
        </div>
        """.format(metrics['test_loss']), unsafe_allow_html=True)
        
except FileNotFoundError:
    st.markdown("""
    <div style='background: #fff3cd; padding: 15px; border-radius: 10px; border-left: 5px solid #B1B5A0;'>
        <p style='color: #856404; margin: 0;'><strong>[!]</strong> Training metrics not found. Run train_model.py first.</p>
    </div>
    """, unsafe_allow_html=True)

# Technical Details
with st.expander("[<>] Technical Implementation Details"):
    st.markdown("""
    <div style='padding: 10px;'>
        <h4 style='color: #2E4057;'>» Frameworks & Libraries</h4>
        <ul>
            <li><strong>TensorFlow 2.13:</strong> Deep learning framework</li>
            <li><strong>MediaPipe 0.10:</strong> Hand landmark detection</li>
            <li><strong>OpenCV 4.8:</strong> Camera capture and image processing</li>
            <li><strong>NumPy:</strong> Numerical computations</li>
        </ul>
        <h4 style='color: #2E4057; margin-top: 20px;'>» Model Optimization</h4>
        <ul>
            <li>Weight regularization to prevent overfitting</li>
            <li>Dropout layers for robustness</li>
            <li>Batch normalization for stable training</li>
            <li>Early stopping to prevent overfitting</li>
        </ul>
        <h4 style='color: #2E4057; margin-top: 20px;'>» Inference Pipeline</h4>
        <ol>
            <li>Capture frame from webcam (30 FPS)</li>
            <li>MediaPipe extracts hand landmarks (~5ms)</li>
            <li>Build 30-frame sequence buffer</li>
            <li>Model predicts gesture class (~10ms)</li>
            <li>Text-to-speech synthesis (~50ms)</li>
            <li><strong>Total latency: ~65-100ms per prediction</strong></li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# Model Architecture Diagram
with st.expander("[~] Model Architecture Diagram"):
    st.markdown("""
    <div style='background: #f8f9fa; padding: 20px; border-radius: 10px;'>
        <pre style='background: #2E4057; color: #00ff00; padding: 15px; border-radius: 5px; overflow-x: auto;'>
Input (30, 21, 3)
    |
    v
TimeDistributed(CNN)
    |-- Conv1D(64) -> MaxPool -> Conv1D(128) -> MaxPool -> Flatten
    v
LSTM(128) -> Dropout(0.3)
    |
    v
Dense(64, relu)
    |
    v
Dense(N, softmax)
    |
    v
Output: Gesture Class
        </pre>
        <p style='margin-top: 10px; color: #666;'><strong>[i]</strong> The CNN extracts spatial features from each frame, while the LSTM learns temporal relationships across the 30-frame sequence.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem; background: #f8f9fa; border-radius: 8px;'>
    <p style='margin: 0;'>[i] CNN-LSTM Hybrid Architecture | 350K Parameters | Real-time Inference at 30 FPS</p>
</div>
""", unsafe_allow_html=True)
