import streamlit as st
import cv2
import numpy as np
import time
import plotly.graph_objects as go
from collections import deque
import pandas as pd
import os

if os.path.exists('assets/style.css'):
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Custom header with styled title
st.markdown("""
<div style='border-bottom: 3px solid #2E86AB; padding-bottom: 10px; margin-bottom: 20px;'>
    <h1 style='color: #2E4057; margin: 0;'>Live Gesture Recognition</h1>
    <p style='color: #666; font-size: 1.1rem; margin: 5px 0 0 0;'>Real-time sign language interpretation with webcam feed</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'recognizer' not in st.session_state:
    # Import here to avoid duplicate layer name issues
    from inference.realtime_prediction import GestureRecognizer
    st.session_state.recognizer = GestureRecognizer(confidence_threshold=0.7)
    
if 'is_running' not in st.session_state:
    st.session_state.is_running = False
if 'prediction_history' not in st.session_state:
    st.session_state.prediction_history = deque(maxlen=10)
if 'confidence_history' not in st.session_state:
    st.session_state.confidence_history = deque(maxlen=50)
if 'spoken_gestures' not in st.session_state:
    st.session_state.spoken_gestures = set()

# Control Panel with styled background
st.markdown("""
<div style='background: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
""", unsafe_allow_html=True)

control_col1, control_col2, control_col3 = st.columns([1, 1, 2])

with control_col1:
    # Styled button
    button_label = "Start Recognition" if not st.session_state.is_running else "Stop Recognition"
    button_type = "primary" if not st.session_state.is_running else "secondary"
    
    if st.button(button_label, use_container_width=True, type=button_type):
        st.session_state.is_running = not st.session_state.is_running
        if not st.session_state.is_running:
            # Clear spoken gestures set when stopping
            st.session_state.spoken_gestures.clear()
        else:
            # Only reinitialize if starting fresh
            if len(st.session_state.prediction_history) == 0:
                from inference.realtime_prediction import GestureRecognizer
                st.session_state.recognizer = GestureRecognizer(
                    confidence_threshold=st.session_state.recognizer.confidence_threshold
                )

with control_col2:
    confidence_threshold = st.slider(
        "Confidence Threshold",
        min_value=0.5,
        max_value=0.95,
        value=st.session_state.recognizer.confidence_threshold,
        step=0.05,
        help="Minimum confidence required to accept a prediction"
    )
    st.session_state.recognizer.confidence_threshold = confidence_threshold

with control_col3:
    voice_enabled = st.checkbox("Enable Voice Output", value=True)
    
    # Show status
    if st.session_state.is_running:
        st.markdown("""
        <div style='background: #d4edda; padding: 8px; border-radius: 5px; text-align: center; margin-top: 10px;'>
            <span style='color: #155724; font-weight: bold;'>[REC] Active</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='background: #f8d7da; padding: 8px; border-radius: 5px; text-align: center; margin-top: 10px;'>
            <span style='color: #721c24; font-weight: bold;'>[ ] Inactive</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Main Interface
main_col1, main_col2 = st.columns([3, 2])

with main_col1:
    st.markdown("""
    <div style='border-left: 5px solid #7B8065; padding-left: 15px; margin: 10px 0 15px 0;'>
        <h3 style='color: #2E4057; margin: 0;'>[o] Camera Feed</h3>
    </div>
    """, unsafe_allow_html=True)
    
    camera_placeholder = st.empty()
    
    if st.session_state.is_running:
        cap = cv2.VideoCapture(0)
        
        # Set camera properties for better performance
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_FPS, 30)
        
        while st.session_state.is_running:
            ret, frame = cap.read()
            if not ret:
                st.error("[!] Failed to access webcam")
                break
            
            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)
            
            # Process frame
            processed_frame, prediction_info = st.session_state.recognizer.process_frame(frame)
            
            # Add text overlay
            if prediction_info['gesture']:
                color = (0, 255, 0) if prediction_info['gesture'] != "Unknown" else (0, 0, 255)
                cv2.putText(
                    processed_frame,
                    f"{prediction_info['gesture']} ({prediction_info['confidence']:.1%})",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    color,
                    2
                )
                
                # Add confidence bar
                bar_width = int(prediction_info['confidence'] * 200)
                cv2.rectangle(processed_frame, (10, 50), (10 + bar_width, 65), color, -1)
                cv2.rectangle(processed_frame, (10, 50), (210, 65), (255, 255, 255), 1)
            
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
                
                # Speak if enabled (only once per gesture per session)
                if voice_enabled and prediction_info['speak']:
                    gesture_key = prediction_info['gesture']
                    if gesture_key not in st.session_state.spoken_gestures:
                        st.session_state.spoken_gestures.add(gesture_key)
                        try:
                            st.session_state.recognizer.speak_gesture(prediction_info['gesture'])
                        except Exception:
                            pass  # Silently ignore speech errors
        
        cap.release()
    else:
        camera_placeholder.markdown("""
        <div style='background: #f8f9fa; padding: 60px 20px; border-radius: 10px; text-align: center; border: 2px dashed #2E86AB;'>
            <p style='color: #666; font-size: 1.2rem; margin: 0;'>[o] Camera feed will appear here</p>
            <p style='color: #999; margin-top: 10px;'>Click 'Start Recognition' to begin</p>
        </div>
        """, unsafe_allow_html=True)

with main_col2:
    st.markdown("""
    <div style='border-left: 5px solid #B1B5A0; padding-left: 15px; margin: 10px 0 15px 0;'>
        <h3 style='color: #2E4057; margin: 0;'>[=] Live Statistics</h3>
    </div>
    """, unsafe_allow_html=True)
    
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
                    'line': {'color': "#C73E1D", 'width': 2},
                    'thickness': 0.75,
                    'value': confidence_threshold * 100
                }
            }
        ))
        fig.update_layout(height=220, margin=dict(t=50, b=0, l=20, r=20))
        st.plotly_chart(fig, use_container_width=True)
        
        # Metrics
        metric_col1, metric_col2 = st.columns(2)
        with metric_col1:
            confidence_color = "#155724" if current['confidence'] >= 0.7 else "#856404"
            st.markdown(f"""
            <div style='background: #f8f9fa; padding: 10px; border-radius: 8px; text-align: center;'>
                <p style='color: #666; margin: 0; font-size: 0.8rem;'>Confidence</p>
                <p style='color: {confidence_color}; margin: 5px 0 0 0; font-size: 1.5rem; font-weight: bold;'>{current['confidence']:.1%}</p>
            </div>
            """, unsafe_allow_html=True)
        with metric_col2:
            st.markdown(f"""
            <div style='background: #f8f9fa; padding: 10px; border-radius: 8px; text-align: center;'>
                <p style='color: #666; margin: 0; font-size: 0.8rem;'>Time</p>
                <p style='color: #2E4057; margin: 5px 0 0 0; font-size: 1.2rem; font-weight: bold;'>{current['timestamp']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='background: #f8f9fa; padding: 20px; border-radius: 10px; text-align: center;'>
            <p style='color: #666; margin: 0;'>Waiting for predictions...</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Confidence Trend
    if len(st.session_state.confidence_history) > 1:
        st.markdown("""
        <div style='margin-top: 20px;'>
            <h4 style='color: #2E4057;'>[~] Confidence Trend</h4>
        </div>
        """, unsafe_allow_html=True)
        
        trend_data = pd.DataFrame({
            'Frame': range(len(st.session_state.confidence_history)),
            'Confidence': list(st.session_state.confidence_history)
        })
        st.line_chart(trend_data.set_index('Frame'), height=150)
    
    # Prediction History
    st.markdown("""
    <div style='margin-top: 20px;'>
        <h4 style='color: #2E4057;'>{ } Recent Predictions</h4>
    </div>
    """, unsafe_allow_html=True)
    
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
        
        # Clear history button
        if st.button("Clear History", use_container_width=True):
            st.session_state.prediction_history.clear()
            st.session_state.confidence_history.clear()
            st.session_state.spoken_gestures.clear()
            st.rerun()
    else:
        st.info("No predictions yet. Start recognition to see history.")

# Tips Section
with st.expander("[?] Tips for Best Results"):
    tip_col1, tip_col2 = st.columns(2)
    with tip_col1:
        st.markdown("""
        **» Before You Start:**
        - Ensure good lighting conditions
        - Keep hand clearly visible in frame
        - Position hand 1-2 feet from camera
        - Avoid busy backgrounds
        """)
    with tip_col2:
        st.markdown("""
        **» During Recognition:**
        - Maintain steady hand movements
        - Complete gestures fully before changing
        - Hold each gesture for 1-2 seconds
        - Keep hand within the green bounding box
        """)

# Supported Gestures
with st.expander("[#] Supported Gestures"):
    gestures = st.session_state.recognizer.gesture_labels
    
    st.markdown("<div style='display: flex; flex-wrap: wrap; gap: 10px;'>", unsafe_allow_html=True)
    gesture_cols = st.columns(5)
    for i, gesture in enumerate(gestures):
        with gesture_cols[i % 5]:
            st.markdown(f"""
            <div style='background: #2E86AB; color: white; padding: 8px; border-radius: 5px; text-align: center; margin: 3px 0;'>
                {gesture.title()}
            </div>
            """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem; background: #f8f9fa; border-radius: 8px;'>
    <p style='margin: 0;'>[i] Real-time gesture recognition | CNN-LSTM Model | 30 FPS | 10 Gesture Classes</p>
</div>
""", unsafe_allow_html=True)
