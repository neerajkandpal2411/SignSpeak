import streamlit as st
import cv2
import numpy as np
from PIL import Image
import time
from inference.realtime_prediction import GestureRecognizer
import plotly.graph_objects as go
from collections import deque
import pandas as pd

# Initialize session state
if 'recognizer' not in st.session_state:
    st.session_state.recognizer = GestureRecognizer(confidence_threshold=0.7)
if 'is_running' not in st.session_state:
    st.session_state.is_running = False
if 'prediction_history' not in st.session_state:
    st.session_state.prediction_history = deque(maxlen=10)
if 'confidence_history' not in st.session_state:
    st.session_state.confidence_history = deque(maxlen=50)

st.title("🎥 Live Gesture Recognition")
st.markdown("Real-time sign language interpretation with webcam feed")

# Control Panel
control_col1, control_col2, control_col3 = st.columns([1, 1, 2])

with control_col1:
    if st.button("▶️ Start Recognition" if not st.session_state.is_running else "⏸️ Stop Recognition", 
                 use_container_width=True):
        st.session_state.is_running = not st.session_state.is_running
        if not st.session_state.is_running:
            st.session_state.recognizer = GestureRecognizer()

with control_col2:
    confidence_threshold = st.slider(
        "Confidence Threshold",
        min_value=0.5,
        max_value=0.95,
        value=0.7,
        step=0.05,
        help="Minimum confidence required to accept a prediction"
    )
    st.session_state.recognizer.confidence_threshold = confidence_threshold

with control_col3:
    voice_enabled = st.checkbox("🔊 Enable Voice Output", value=True)

# Main Interface
main_col1, main_col2 = st.columns([3, 2])

with main_col1:
    st.markdown("### 📹 Camera Feed")
    camera_placeholder = st.empty()
    
    if st.session_state.is_running:
        cap = cv2.VideoCapture(0)
        
        while st.session_state.is_running:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to access webcam")
                break
            
            # Process frame
            processed_frame, prediction_info = st.session_state.recognizer.process_frame(frame)
            
            # Add text overlay
            if prediction_info['gesture']:
                cv2.putText(
                    processed_frame,
                    f"{prediction_info['gesture']} ({prediction_info['confidence']:.1%})",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0) if prediction_info['gesture'] != "Unknown" else (0, 0, 255),
                    2
                )
            
            # Convert to RGB for Streamlit
            processed_frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            camera_placeholder.image(processed_frame_rgb, channels="RGB", use_column_width=True)
            
            # Update history
            if prediction_info['gesture'] and prediction_info['gesture'] != "Unknown":
                st.session_state.prediction_history.append({
                    'gesture': prediction_info['gesture'],
                    'confidence': prediction_info['confidence'],
                    'timestamp': time.strftime("%H:%M:%S")
                })
                st.session_state.confidence_history.append(prediction_info['confidence'])
                
                # Speak if enabled (only once per gesture)
                if voice_enabled and prediction_info['speak']:
                    # Use a flag to prevent multiple speech calls
                    gesture_key = f"spoken_{prediction_info['gesture']}"
                    if gesture_key not in st.session_state:
                        st.session_state[gesture_key] = True
                        try:
                            st.session_state.recognizer.speak_gesture(prediction_info['gesture'])
                        except RuntimeError:
                            pass 
        
        cap.release()
    else:
        camera_placeholder.info("Click 'Start Recognition' to begin")

with main_col2:
    st.markdown("### 📊 Live Statistics")
    
    # Current Prediction
    if st.session_state.prediction_history:
        current = st.session_state.prediction_history[-1]
        
        # Confidence Gauge
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=current['confidence'] * 100,
            title={'text': f"Current Gesture: {current['gesture']}"},
            delta={'reference': 70},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#2E4057"},
                'steps': [
                    {'range': [0, 50], 'color': "#ffcccc"},
                    {'range': [50, 70], 'color': "#ffffcc"},
                    {'range': [70, 100], 'color': "#ccffcc"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 2},
                    'thickness': 0.75,
                    'value': confidence_threshold * 100
                }
            }
        ))
        fig.update_layout(height=250)
        st.plotly_chart(fig, use_container_width=True)
        
        # Metrics
        metric_col1, metric_col2 = st.columns(2)
        with metric_col1:
            st.metric("Confidence", f"{current['confidence']:.1%}")
        with metric_col2:
            st.metric("Time", current['timestamp'])
    
    # Confidence Trend
    if len(st.session_state.confidence_history) > 1:
        st.markdown("### 📈 Confidence Trend")
        trend_data = pd.DataFrame({
            'Frame': range(len(st.session_state.confidence_history)),
            'Confidence': list(st.session_state.confidence_history)
        })
        st.line_chart(trend_data.set_index('Frame'))
    
    # Prediction History
    st.markdown("### 📜 Recent Predictions")
    if st.session_state.prediction_history:
        history_df = pd.DataFrame(list(st.session_state.prediction_history))
        st.dataframe(
            history_df[['gesture', 'confidence', 'timestamp']],
            use_container_width=True,
            hide_index=True,
            column_config={
                "gesture": "Gesture",
                "confidence": st.column_config.NumberColumn(
                    "Confidence",
                    format="%.1f%%",
                    min_value=0,
                    max_value=100
                ),
                "timestamp": "Time"
            }
        )
    else:
        st.info("No predictions yet. Start recognition to see history.")

# Tips Section
with st.expander("💡 Tips for Best Results"):
    st.markdown("""
    - Ensure good lighting conditions
    - Keep hand clearly visible in frame
    - Maintain steady hand movements
    - Position hand 1-2 feet from camera
    - Avoid busy backgrounds
    - Complete gestures fully before changing
    """)

# Supported Gestures
with st.expander("🤌 Supported Gestures"):
    gestures = st.session_state.recognizer.gesture_labels
    gesture_cols = st.columns(4)
    for i, gesture in enumerate(gestures):
        with gesture_cols[i % 4]:
            st.markdown(f"- {gesture.title()}")