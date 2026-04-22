"""Session state management utilities"""
import streamlit as st

def initialize_session_state():
    """Initialize all session state variables"""
    
    if 'initialized' not in st.session_state:
        st.session_state.initialized = True
        
        # Recognition state
        st.session_state.is_running = False
        st.session_state.prediction_history = []
        st.session_state.confidence_scores = []
        
        # Settings
        st.session_state.confidence_threshold = 0.7
        st.session_state.voice_enabled = True
        st.session_state.show_landmarks = True
        
        # Statistics
        st.session_state.total_predictions = 0
        st.session_state.correct_predictions = 0
        st.session_state.session_start_time = None

def reset_session():
    """Reset session state"""
    for key in st.session_state.keys():
        del st.session_state[key]
    initialize_session_state()