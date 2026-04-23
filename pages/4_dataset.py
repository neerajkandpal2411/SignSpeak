import streamlit as st
import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os

st.set_page_config(page_title="Dataset - SignSpeak", page_icon="📊")

if os.path.exists('assets/style.css'):
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# header
st.markdown("""
<div style='border-bottom: 3px solid #2E86AB; padding-bottom: 10px; margin-bottom: 20px;'>
    <h1 style='color: #2E4057; margin: 0;'>Dataset Overview</h1>
    <p style='color: #666; font-size: 1.1rem; margin: 5px 0 0 0;'>Gesture dataset statistics and distribution analysis</p>
</div>
""", unsafe_allow_html=True)

# Load dataset stats
try:
    with open('assets/dataset_stats.json', 'r') as f:
        stats = json.load(f)
    
    st.markdown("""
    <div style='border-left: 5px solid #7B8065; padding-left: 15px; margin: 30px 0 20px 0;'>
        <h2 style='color: #2E4057; margin: 0;'>[=] Dataset Summary</h2>
    </div>
    """, unsafe_allow_html=True)
    
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    
    with metric_col1:
        st.metric("Total Samples", stats['total_samples'])
    
    with metric_col2:
        st.metric("Gesture Classes", stats['gesture_classes'])
    
    with metric_col3:
        st.metric("Sequence Length", f"{stats['sequence_length']} frames")
    
    with metric_col4:
        avg_samples = stats['total_samples'] / stats['gesture_classes']
        st.metric("Avg Samples/Class", f"{avg_samples:.1f}")
    
    # Sample Distribution Chart
    st.markdown("""
    <div style='border-left: 5px solid #B1B5A0; padding-left: 15px; margin: 30px 0 20px 0;'>
        <h2 style='color: #2E4057; margin: 0;'>// Samples per Gesture</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Prepare data for chart
    gesture_data = []
    for gesture, data in stats.items():
        if gesture not in ['total_samples', 'gesture_classes', 'sequence_length']:
            gesture_data.append({
                'Gesture': gesture.title(),
                'Samples': data['samples'],
                'Valid Files': data['valid_files']
            })
    
    df = pd.DataFrame(gesture_data)
    
    # Bar chart
    fig = px.bar(
        df,
        x='Gesture',
        y='Samples',
        title='Number of Samples per Gesture Class',
        color='Samples',
        color_continuous_scale='Viridis',
        text='Samples'
    )
    fig.update_traces(textposition='outside')
    fig.update_layout(
        xaxis_title="Gesture",
        yaxis_title="Number of Samples",
        showlegend=False,
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Pie Chart for Distribution
    st.markdown("""
    <div style='border-left: 5px solid #A23B72; padding-left: 15px; margin: 30px 0 20px 0;'>
        <h2 style='color: #2E4057; margin: 0;'>(%) Dataset Distribution</h2>
    </div>
    """, unsafe_allow_html=True)
    
    fig_pie = px.pie(
        df,
        values='Samples',
        names='Gesture',
        title='Percentage Distribution of Gesture Classes',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    fig_pie.update_layout(height=500)
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # Dataset Structure
    st.markdown("""
    <div style='border-left: 5px solid #73AB84; padding-left: 15px; margin: 30px 0 20px 0;'>
        <h2 style='color: #2E4057; margin: 0;'>{ } Dataset Structure</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
data/processed_frames/
├── hello/
│   ├── seq_000.npy (30 frames * 21 landmarks * 3 coords)
│   ├── seq_001.npy
│   └── ...
├── thanks/
│   └── ...
├── yes/
├── no/
├── help/
├── i love you/
├── stop/
├── please/
├── time/
└── friend/
    """, language="text")
    
    # Statistics Table
    st.markdown("""
    <div style='border-left: 5px solid #C73E1D; padding-left: 15px; margin: 30px 0 20px 0;'>
        <h2 style='color: #2E4057; margin: 0;'>[#] Detailed Statistics</h2>
    </div>
    """, unsafe_allow_html=True)
    
    detailed_df = pd.DataFrame(gesture_data)
    detailed_df['Percentage'] = (detailed_df['Samples'] / stats['total_samples'] * 100).round(1)
    detailed_df = detailed_df.sort_values('Samples', ascending=False)
    
    st.dataframe(
        detailed_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Gesture": "Gesture Class",
            "Samples": st.column_config.NumberColumn("Total Samples"),
            "Valid Files": st.column_config.NumberColumn("Valid Sequences"),
            "Percentage": st.column_config.NumberColumn("% of Dataset", format="%.1f%%")
        }
    )
    
    # Data Collection Process
    st.markdown("""
    <div style='border-left: 5px solid #2E4057; padding-left: 15px; margin: 30px 0 20px 0;'>
        <h2 style='color: #2E4057; margin: 0;'>>>> Data Collection Process</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: #f8f9fa; padding: 20px; border-radius: 10px; height: 100%;'>
            <h4 style='color: #2E4057; margin-top: 0;'>Collection Protocol</h4>
            <ol style='padding-left: 20px;'>
                <li><strong>Setup:</strong> Webcam positioned at eye level</li>
                <li><strong>Lighting:</strong> Consistent, even lighting</li>
                <li><strong>Distance:</strong> Hand 1-2 feet from camera</li>
                <li><strong>Background:</strong> Plain, non-distracting background</li>
                <li><strong>Duration:</strong> 1 second per gesture (30 frames)</li>
                <li><strong>Repetitions:</strong> 30 samples per gesture</li>
            </ol>
            <h4 style='color: #2E4057; margin: 20px 0 10px 0;'>Quality Control</h4>
            <ul style='list-style-type: none; padding-left: 0;'>
                <li>► All sequences verified for 21 landmarks</li>
                <li>► Consistent hand positioning</li>
                <li>► Clear visibility of all fingers</li>
                <li>► Smooth motion without jerks</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; color: white; height: 100%;'>
            <h4 style='color: white; margin-top: 0;'>Data Specifications</h4>
            <ul style='list-style-type: none; padding-left: 0;'>
                <li><strong>Format:</strong> NumPy array (.npy)</li>
                <li><strong>Shape:</strong> (30, 21, 3)</li>
                <li><strong>Data Type:</strong> float32</li>
                <li><strong>Range:</strong> [0.0, 1.0] normalized</li>
                <li><strong>Size per Sample:</strong> ~7.5 KB</li>
                <li><strong>Total Dataset Size:</strong> ~2.25 MB</li>
            </ul>
            <h4 style='color: white; margin: 20px 0 10px 0;'>Landmark Coordinates</h4>
            <ul style='list-style-type: none; padding-left: 0;'>
                <li><strong>X:</strong> Horizontal position (0 = left, 1 = right)</li>
                <li><strong>Y:</strong> Vertical position (0 = top, 1 = bottom)</li>
                <li><strong>Z:</strong> Depth (relative to wrist)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Sample Visualization
    st.markdown("""
    <div style='border-left: 5px solid #B1B5A0; padding-left: 15px; margin: 30px 0 20px 0;'>
        <h2 style='color: #2E4057; margin: 0;'>[~] Sample Sequence Visualization</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("Each sequence contains 30 frames of hand landmark data:")
    
    # Create sample visualization
    frames = list(range(30))
    landmarks = list(range(21))
    
    fig = go.Figure(data=go.Heatmap(
        z=[[i+j for j in landmarks] for i in frames],
        colorscale='Viridis',
        showscale=True,
        colorbar=dict(title="Landmark Value")
    ))
    
    fig.update_layout(
        title="Data Matrix: 30 Frames * 21 Landmarks",
        xaxis_title="Landmark Index (0-20)",
        yaxis_title="Frame Number (0-29)",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Sample Count Chart
    st.markdown("""
    <div style='border-left: 5px solid #73AB84; padding-left: 15px; margin: 30px 0 20px 0;'>
        <h2 style='color: #2E4057; margin: 0;'><> Sample Count Comparison</h2>
    </div>
    """, unsafe_allow_html=True)
    
    fig_bar = go.Figure()
    
    fig_bar.add_trace(go.Bar(
        x=df['Gesture'],
        y=df['Samples'],
        marker_color='#2E86AB',
        text=df['Samples'],
        textposition='outside',
        name='Samples per Class'
    ))
    
    fig_bar.add_hline(
        y=30, 
        line_dash="dash", 
        line_color="#C73E1D",
        annotation_text="Target (30 samples)",
        annotation_position="bottom right"
    )
    
    fig_bar.update_layout(
        title="Samples per Gesture Class vs Target",
        xaxis_title="Gesture Class",
        yaxis_title="Number of Samples",
        height=400,
        showlegend=True
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)
    
except FileNotFoundError:
    st.markdown("""
    <div style='background: #fff3cd; padding: 20px; border-radius: 10px; border-left: 5px solid #B1B5A0; margin: 20px 0;'>
        <h3 style='color: #856404; margin-top: 0;'>[!] Dataset statistics not found</h3>
        <p style='color: #856404;'>Please run prepare_data.py first to generate statistics.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: #f8f9fa; padding: 20px; border-radius: 10px;'>
        <h3 style='color: #2E4057; margin-top: 0;'>» To generate dataset statistics:</h3>
        <code style='background: #2E4057; color: white; padding: 10px; display: block; border-radius: 5px;'>
        python -m training.prepare_data
        </code>
    </div>
    """, unsafe_allow_html=True)

# Data Augmentation Section
with st.expander("[+] Data Augmentation Techniques (Planned)"):
    st.markdown("""
    <div style='padding: 10px;'>
        <h4 style='color: #2E4057;'>» Spatial Augmentation</h4>
        <ul>
            <li>Random rotation (+/- 15 degrees)</li>
            <li>Random scaling (0.8x - 1.2x)</li>
            <li>Random translation (+/- 10%)</li>
            <li>Horizontal flipping</li>
        </ul>
        <h4 style='color: #2E4057; margin-top: 20px;'>» Temporal Augmentation</h4>
        <ul>
            <li>Frame skipping (drop every 5th frame)</li>
            <li>Temporal scaling (speed up/slow down)</li>
            <li>Reverse sequences</li>
        </ul>
        <h4 style='color: #2E4057; margin-top: 20px;'>» Noise Addition</h4>
        <ul>
            <li>Gaussian noise to coordinates (sigma=0.01)</li>
            <li>Random landmark dropout (5% probability)</li>
            <li>Coordinate jittering</li>
        </ul>
        <h4 style='color: #155724; margin-top: 20px;'>» Expected Benefits</h4>
        <ul>
            <li>15-20% improvement in generalization</li>
            <li>Better robustness to variations</li>
            <li>Reduced overfitting</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Dataset Collection Code
with st.expander("[<>] Dataset Collection Code"):
    st.code("""
import cv2
import numpy as np
import mediapipe as mp

def collect_gesture(gesture_name):
    \"\"\"Collect 30 samples of a gesture\"\"\"
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.7
    )
    
    cap = cv2.VideoCapture(0)
    sequence = []
    
    while len(sequence) < 30:
        ret, frame = cap.read()
        results = hands.process(frame)
        
        if results.multi_hand_landmarks:
            landmarks = []
            for lm in results.multi_hand_landmarks[0].landmark:
                landmarks.append([lm.x, lm.y, lm.z])
            sequence.append(landmarks)
    
    np.save(f"{gesture_name}_seq.npy", np.array(sequence))
    """, language="python")

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem; background: #f8f9fa; border-radius: 8px;'>
    <p style='margin: 0;'>[i] Dataset collected using MediaPipe Hand Landmark Detection</p>
    <p style='margin: 5px 0 0 0; font-size: 0.9rem;'>Total Dataset Size: ~2.25 MB | 10 Gesture Classes | 30 Samples per Class</p>
</div>
""", unsafe_allow_html=True)
