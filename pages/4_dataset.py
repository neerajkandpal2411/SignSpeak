import streamlit as st
import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os

st.set_page_config(page_title="Dataset - SignSpeak", page_icon="📊")

st.title("📊 Dataset Overview")
st.markdown("Gesture dataset statistics and distribution")

# Load dataset statistics
try:
    with open('assets/dataset_stats.json', 'r') as f:
        stats = json.load(f)
    
    # Overview Metrics
    st.markdown("## 📈 Dataset Summary")
    
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
    st.markdown("## 📊 Samples per Gesture")
    
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
    st.markdown("## 🥧 Dataset Distribution")
    
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
    st.markdown("## 📁 Dataset Structure")
    st.code("""
data/processed_frames/
├── hello/
│   ├── seq_000.npy (30 frames × 21 landmarks × 3 coords)
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
    
    # Detailed Statistics Table
    st.markdown("## 📋 Detailed Statistics")
    
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
    st.markdown("## 🎥 Data Collection Process")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Collection Protocol
        1. **Setup:** Webcam positioned at eye level
        2. **Lighting:** Consistent, even lighting
        3. **Distance:** Hand 1-2 feet from camera
        4. **Background:** Plain, non-distracting background
        5. **Duration:** 1 second per gesture (30 frames)
        6. **Repetitions:** 30 samples per gesture
        
        ### Quality Control
        - All sequences verified for 21 landmarks
        - Consistent hand positioning
        - Clear visibility of all fingers
        - Smooth motion without jerks
        """)
    
    with col2:
        st.info("""
        ### Data Specifications
        - **Format:** NumPy array (.npy)
        - **Shape:** (30, 21, 3)
        - **Data Type:** float32
        - **Range:** [0.0, 1.0] normalized
        - **Size per Sample:** ~7.5 KB
        - **Total Dataset Size:** ~2.25 MB
        
        ### Landmark Coordinates
        - **X:** Horizontal position (0 = left, 1 = right)
        - **Y:** Vertical position (0 = top, 1 = bottom)
        - **Z:** Depth (relative to wrist)
        """)
    
    # Sample Visualization
    st.markdown("## 🖼️ Sample Sequence Visualization")
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
        title="Data Matrix: 30 Frames × 21 Landmarks",
        xaxis_title="Landmark Index (0-20)",
        yaxis_title="Frame Number (0-29)",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Sample Count Chart
    st.markdown("## 📉 Sample Count Comparison")
    
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
        line_color="red",
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
    st.warning("⚠️ Dataset statistics not found. Please run prepare_data.py first to generate statistics.")
    
    st.markdown("""
    ### To generate dataset statistics:
    ```bash
    python training/prepare_data.py""")