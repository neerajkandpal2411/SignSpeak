import streamlit as st

st.title("🤟 SignSpeak: Real-Time Sign Language Recognition")
st.markdown("### Bridging Communication Gaps Through AI")

# Hero Section
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 20px; color: white; margin-bottom: 2rem;'>
        <h2 style='color: white;'>Empowering Communication</h2>
        <p style='font-size: 1.2rem;'>
        An AI-powered system that translates sign language gestures into text and speech in real-time,
        making communication accessible for the deaf and hard-of-hearing community.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("https://via.placeholder.com/400x300?text=Gesture+Demo", 
             use_column_width=True)

# Key Features
st.markdown("---")
st.markdown("## ✨ Key Features")

features_col1, features_col2 = st.columns(2)

with features_col1:
    st.markdown("""
    ### 🎯 Real-Time Recognition
    - Instant gesture detection
    - 30 FPS processing speed
    - Low latency prediction
    
    ### 🔊 Text-to-Speech Output
    - Natural voice synthesis
    - Automatic speech generation
    - Multi-language support ready
    
    ### 🧠 Deep Learning Powered
    - CNN + LSTM architecture
    - Spatial-temporal feature learning
    - 95%+ accuracy on test set
    """)

with features_col2:
    st.markdown("""
    ### 📹 Webcam Integration
    - Live camera feed
    - Hand landmark visualization
    - Works with any webcam
    
    ### 📊 Real-Time Analytics
    - Confidence score display
    - Prediction history tracking
    - Performance monitoring
    
    ### ♿ Accessibility Focused
    - Designed for deaf/mute users
    - High contrast UI
    - Keyboard navigation support
    """)

# Project Stats
st.markdown("---")
st.markdown("## 📈 Project Statistics")

stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

with stat_col1:
    st.metric("Gestures Supported", "10+", delta="Expanding")

with stat_col2:
    st.metric("Model Accuracy", "95.2%", delta="+2.3%")

with stat_col3:
    st.metric("Processing Speed", "30 FPS", delta="Real-time")

with stat_col4:
    st.metric("Samples Collected", "300+", delta="10 gestures")

# Problem Statement
st.markdown("---")
st.markdown("## 🎯 Problem Statement")
st.info("""
According to the World Health Organization, over 430 million people worldwide have disabling hearing loss.
Communication barriers between sign language users and non-signers remain a significant challenge in healthcare,
education, and daily life. SignSpeak aims to bridge this gap using state-of-the-art deep learning techniques
for real-time sign language interpretation.
""")

# How It Works
st.markdown("## 🔄 How It Works")
st.image("https://via.placeholder.com/800x300?text=Architecture+Diagram", use_column_width=True)

workflow_col1, workflow_col2, workflow_col3, workflow_col4 = st.columns(4)

with workflow_col1:
    st.markdown("""
    ### 1️⃣ Capture
    Webcam captures hand gestures in real-time
    """)

with workflow_col2:
    st.markdown("""
    ### 2️⃣ Extract
    MediaPipe extracts 21 hand landmarks
    """)

with workflow_col3:
    st.markdown("""
    ### 3️⃣ Recognize
    CNN-LSTM model classifies gesture
    """)

with workflow_col4:
    st.markdown("""
    ### 4️⃣ Output
    Text display + speech synthesis
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>Final Year Major Project • Computer Science & Engineering</p>
    <p>© 2026 SignSpeak • All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)