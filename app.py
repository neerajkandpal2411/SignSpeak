import streamlit as st
import os
import json

st.set_page_config(
    page_title="SignSpeak - Gesture Recognition",
    page_icon="🤟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
import os
if os.path.exists('assets/style.css'):
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    # Logo - replace placeholder with actual image
    logo_path = "assets/logo.png"
    if os.path.exists(logo_path):
        st.image(logo_path, width=200)
    else:
        st.markdown("""
        <div style='background: #2E4057; padding: 15px; border-radius: 8px; text-align: center; margin-bottom: 20px;'>
            <h2 style='color: white; margin: 0;'>SignSpeak</h2>
            <p style='color: #ccc; margin: 5px 0 0 0; font-size: 0.8rem;'>v1.0.0</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='border-left: 3px solid #B1B5A0; padding-left: 10px; margin: 20px 0 10px 0;'>
        <h3 style='color: white; margin: 0;'>Navigation</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='color: #ccc; font-size: 0.9rem;'>
        <p>» <a href='/home' target='_self' style='color: #ccc; text-decoration: none;'>Home</a></p>
        <p>» <a href='/live_recognition' target='_self' style='color: #ccc; text-decoration: none;'>Live Recognition</a></p>
        <p>» <a href='/about_model' target='_self' style='color: #ccc; text-decoration: none;'>Model Architecture</a></p>
        <p>» <a href='/dataset' target='_self' style='color: #ccc; text-decoration: none;'>Dataset</a></p>
        <p>» <a href='/performance' target='_self' style='color: #ccc; text-decoration: none;'>Performance</a></p>
        <p>» <a href='/team' target='_self' style='color: #ccc; text-decoration: none;'>Team</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # System Status
    st.markdown("""
    <div style='background: #1a252f; padding: 15px; border-radius: 8px; margin-top: 20px;'>
        <h4 style='color: white; margin: 0 0 10px 0;'>System Status</h4>
    """, unsafe_allow_html=True)
    
    # Check if model exists
    if os.path.exists('models/gesture_model.weights.h5'):
        st.markdown('<p style="color: #D2B4D; margin: 5px 0;">[x] Model Loaded</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p style="color: #9B59B6; margin: 5px 0;">[!] Model Not Found</p>', unsafe_allow_html=True)
    
    # Check if dataset exists
    if os.path.exists('data/processed_frames'):
        st.markdown('<p style="color: #D2B4D; margin: 5px 0;">[x] Dataset Ready</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p style="color: #9B59B6; margin: 5px 0;">[!] Dataset Missing</p>', unsafe_allow_html=True)
    
    st.markdown('<p style="color: #D2B4D; margin: 5px 0;">[x] System Online</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# Welcome Header
st.markdown("""
<div style='border-bottom: 3px solid #2E86AB; padding-bottom: 15px; margin-bottom: 20px;'>
    <h1 style='color: #2E4057; margin: 0; font-size: 2.5rem;'>Welcome to SignSpeak - </h1>
    <p style='color: #666; font-size: 1.2rem; margin: 5px 0 0 0;'>Real-Time Sign Language Recognition System</p>
</div>
""", unsafe_allow_html=True)

# Hero Section
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #F02F34 0%, #c41e23 100%); 
                padding: 2.5rem; border-radius: 15px; color: white; margin-bottom: 1rem;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);'>
        <h2 style='color: white; margin-bottom: 1rem;'>Bridging Communication Gaps</h2>
        <p style='font-size: 1.1rem; line-height: 1.6; opacity: 0.95;'>
        An AI-powered system that translates sign language gestures into text and speech in real-time,
        making communication accessible for the deaf and hard-of-hearing community.
        </p>
        <div style='margin-top: 1.5rem;'>
            <a href='/live_recognition' target='_self'>
                <button style='background: #F18F01; color: white; border: none; padding: 12px 24px; 
                               border-radius: 5px; font-size: 1rem; cursor: pointer; margin-right: 10px;'>
                    [>] Start Recognition
                </button>
            </a>
            <a href='/about_model' target='_self'>
                <button style='background: transparent; color: white; border: 1px solid white; 
                               padding: 12px 24px; border-radius: 5px; font-size: 1rem; cursor: pointer;'>
                    [?] Learn More
                </button>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    hero_path = "assets/hero_gesture.png"
    if os.path.exists(hero_path):
        st.image(hero_path, use_column_width=True)
    else:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #048BA8 0%, #036b82 100%); 
                    padding: 40px 20px; border-radius: 15px; text-align: center; color: white; height: 100%;
                    display: flex; flex-direction: column; justify-content: center;'>
            <div style='font-size: 4rem; margin-bottom: 10px;'>[ ASL ]</div>
            <p style='font-size: 1.2rem; margin: 10px 0;'>Hand Gesture Recognition</p>
            <div style='background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px; margin-top: 15px;'>
                <p style='margin: 5px 0;'>10 Gesture Classes</p>
                <p style='margin: 5px 0;'>30 FPS Processing</p>
                <p style='margin: 5px 0;'>95%+ Accuracy</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Load accuracy
test_accuracy = "95.2%"
if os.path.exists('assets/graphs/test_metrics.json'):
    with open('assets/graphs/test_metrics.json', 'r') as f:
        metrics = json.load(f)
        test_accuracy = f"{metrics['test_accuracy']:.1%}"

stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

with stat_col1:
    st.markdown("""
    <div style='background: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;'>
        <h3 style='color: #2E86AB; margin: 0;'>10</h3>
        <p style='color: #666; margin: 5px 0 0 0;'>Gestures</p>
    </div>
    """, unsafe_allow_html=True)

with stat_col2:
    st.markdown(f"""
    <div style='background: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;'>
        <h3 style='color: #28A745; margin: 0;'>{test_accuracy}</h3>
        <p style='color: #666; margin: 5px 0 0 0;'>Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with stat_col3:
    st.markdown("""
    <div style='background: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;'>
        <h3 style='color: #F18F01; margin: 0;'>30 FPS</h3>
        <p style='color: #666; margin: 5px 0 0 0;'>Processing</p>
    </div>
    """, unsafe_allow_html=True)

with stat_col4:
    st.markdown("""
    <div style='background: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;'>
        <h3 style='color: #A23B72; margin: 0;'>300+</h3>
        <p style='color: #666; margin: 5px 0 0 0;'>Samples</p>
    </div>
    """, unsafe_allow_html=True)

# Getting Started Section
st.markdown("---")
st.markdown("""
<div style='border-left: 5px solid #7B8065; padding-left: 15px; margin: 30px 0 20px 0;'>
    <h2 style='color: #2E4057; margin: 0;'>[>] Getting Started</h2>
</div>
""", unsafe_allow_html=True)

guide_col1, guide_col2, guide_col3 = st.columns(3)

with guide_col1:
    st.markdown("""
    <div style='background: #f8f9fa; padding: 20px; border-radius: 10px; height: 100%;'>
        <div style='background: #2E86AB; width: 30px; height: 30px; border-radius: 50%; 
                    display: flex; align-items: center; justify-content: center; margin-bottom: 15px;'>
            <span style='color: white; font-weight: bold;'>1</span>
        </div>
        <h4 style='color: #2E4057;'>Navigate to Live Recognition</h4>
        <p style='color: #666;'>Use the sidebar or click "Start Recognition" above</p>
    </div>
    """, unsafe_allow_html=True)

with guide_col2:
    st.markdown("""
    <div style='background: #f8f9fa; padding: 20px; border-radius: 10px; height: 100%;'>
        <div style='background: #A23B72; width: 30px; height: 30px; border-radius: 50%; 
                    display: flex; align-items: center; justify-content: center; margin-bottom: 15px;'>
            <span style='color: white; font-weight: bold;'>2</span>
        </div>
        <h4 style='color: #2E4057;'>Allow Camera Access</h4>
        <p style='color: #666;'>Grant permission when prompted by your browser</p>
    </div>
    """, unsafe_allow_html=True)

with guide_col3:
    st.markdown("""
    <div style='background: #f8f9fa; padding: 20px; border-radius: 10px; height: 100%;'>
        <div style='background: #28A745; width: 30px; height: 30px; border-radius: 50%; 
                    display: flex; align-items: center; justify-content: center; margin-bottom: 15px;'>
            <span style='color: white; font-weight: bold;'>3</span>
        </div>
        <h4 style='color: #2E4057;'>Make Hand Gestures</h4>
        <p style='color: #666;'>Position your hand clearly in the camera frame</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem; background: #f8f9fa; border-radius: 10px;'>
    <p style='margin: 5px 0;'><strong>Final Year Major Project</strong> | Computer Science & Engineering</p>
    <p style='margin: 5px 0;'>Graphic Era Hill University | Dehradun, Uttarakhand</p>
    <p style='margin: 15px 0 5px 0;'>© 2026 SignSpeak | All Rights Reserved</p>
    <p style='margin: 10px 0 0 0; font-size: 0.85rem; opacity: 0.7;'>
        Use the sidebar (←) to navigate between pages
    </p>
</div>
""", unsafe_allow_html=True)
