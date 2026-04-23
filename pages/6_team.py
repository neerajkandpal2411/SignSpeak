# Import pandas and plotly for timeline and work distribution
import pandas as pd
import plotly.express as px
import streamlit as st
import os

st.set_page_config(page_title="Team - SignSpeak", page_icon="👥")

if os.path.exists('assets/style.css'):
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# header
st.markdown("""
<div style='border-bottom: 3px solid #2E86AB; padding-bottom: 10px; margin-bottom: 20px;'>
    <h1 style='color: #2E4057; margin: 0;'>Project Information</h1>
    <p style='color: #666; font-size: 1.1rem; margin: 5px 0 0 0;'>Final Year Major Project • Computer Science & Engineering</p>
</div>
""", unsafe_allow_html=True)

# Team Member Section
st.markdown("""
<div style='border-left: 5px solid #7B8065; padding-left: 15px; margin: 30px 0 20px 0;'>
    <h2 style='color: #2E4057; margin: 0;'>// Development Team</h2>
</div>
""", unsafe_allow_html=True)

# Team Member 1
col1, col2 = st.columns([1, 3])
with col1:
    st.image("images/nee.jpg", width=150)
with col2:
    st.markdown("""
    <h3 style='color: #2E4057; margin-bottom: 5px;'>Neeraj Kandpal <span style='background: #F18F01; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; margin-left: 10px;'>Team Lead</span></h3>
    
    **Bachelor of Technology - Computer Science & Engineering**  
    **Student ID:** 22019143
    
    *Graphic Era Hill University*
    
    **Email:** neerajkandpal265@gmail.com  
    **LinkedIn:** linkedin.com/in/neeraj-kandpal  
    **GitHub:** github.com/neerajkandpal2411
    
    **Role:** Full Stack Developer, ML Engineer
    """, unsafe_allow_html=True)
st.markdown("<hr style='margin: 20px 0; border: 0; border-top: 1px solid #ddd;'>", unsafe_allow_html=True)

# Team Member 2
col1, col2 = st.columns([1, 3])
with col1:
    st.image("images/ved.jpeg", width=150)
with col2:
    st.markdown("""
    ### Vedaansh Vishwakarma
    **Bachelor of Technology - Computer Science & Engineering**  
    **Student ID:** 220112216
    
    *Graphic Era Hill University*
    
    **Email:** vedaanshvishwakarma896@gmail.com  
    **LinkedIn:** linkedin.com/in/vedaansh-vishwakarma-057a7124b  
    **GitHub:** github.com/vedaansh12
    
    **Role:** Full Stack Developer, ML Engineer
    """)
st.markdown("<hr style='margin: 20px 0; border: 0; border-top: 1px solid #ddd;'>", unsafe_allow_html=True)

# Team Member 3
col1, col2 = st.columns([1, 3])
with col1:
    st.image("images/abhi.jpeg", width=150)
with col2:
    st.markdown("""
    ### Abhishek Rawal
    **Bachelor of Technology - Computer Science & Engineering**  
    **Student ID:** 220112084
    
    *Graphic Era Hill University*
    
    **Email:** darkg0027@gmail.com  
    **LinkedIn:** linkedin.com/in/abhishek-rawal955  
    **GitHub:** github.com/abhi-rawal
    
    **Role:** Full Stack Developer, ML Engineer
    """)
st.markdown("<hr style='margin: 20px 0; border: 0; border-top: 1px solid #ddd;'>", unsafe_allow_html=True)

# Team Member 4
col1, col2 = st.columns([1, 3])
with col1:
    st.image("images/har.jpg", width=150)
with col2:
    st.markdown("""
    ### Harsh Bahuguna
    **Bachelor of Technology - Computer Science & Engineering**  
    **Student ID:** 220111105
    
    *Graphic Era Hill University*
    
    **Email:** harshbahuguna789@gmail.com  
    **LinkedIn:** linkedin.com/in/harsh-bahuguna-32a331355
    
    **Role:** Full Stack Developer, ML Engineer
    """)

# Project Guide Section
st.markdown("---")
st.markdown("""
<div style='border-left: 5px solid #B1B5A0; padding-left: 15px; margin: 30px 0 20px 0;'>
    <h2 style='color: #2E4057; margin: 0;'>// Project Guide</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='background: linear-gradient(135deg, #f5f7fa 0%, #e8ecf1 100%); padding: 20px; border-radius: 10px;'>
    <h3 style='color: #2E4057; margin-top: 0;'>Dr. Seema Gulati</h3>
    <p><strong>Assistant Professor</strong><br>
    Department of Computer Science & Engineering<br>
    Graphic Era Hill University</p><br>
    <p><strong>Expertise:</strong> Machine Learning, Computer Vision, Deep Learning</p>
    <p><strong>Role:</strong> Project Supervisor & Technical Mentor</p>
</div>
""", unsafe_allow_html=True)

# Project Details
st.markdown("---")
st.markdown("""
<div style='border-left: 5px solid #7B8065; padding-left: 15px; margin: 30px 0 20px 0;'>
    <h2 style='color: #2E4057; margin: 0;'>{ } Project Information</h2>
</div>
""", unsafe_allow_html=True)

details_col1, details_col2 = st.columns(2)

with details_col1:
    st.markdown("""
    ### » Academic Details
    - **Course:** B.Tech Final Year Project
    - **Semester:** 8th Semester
    - **Academic Year:** 2025-2026
    - **Project Duration:** 6 months
    - **Project Type:** Research & Development
    - **Credit Hours:** 12
    
    ### » Technical Domain
    - Deep Learning
    - Computer Vision
    - Human-Computer Interaction
    - Accessibility Technology
    - Real-Time Systems
    """)

with details_col2:
    st.markdown("""
    ### » Project Objectives
    1. Real-time sign language recognition
    2. Accessibility for deaf/mute community
    3. Bridge communication gaps
    4. Demonstrate CNN-LSTM architecture
    5. Achieve >90% accuracy
    6. User-friendly interface
    
    ### » Target Users
    - Deaf and hard-of-hearing individuals
    - Sign language learners
    - Educational institutions
    - Healthcare facilities
    - Public service centers
    """)

# Technologies Used
st.markdown("---")
st.markdown("""
<div style='border-left: 5px solid #A23B72; padding-left: 15px; margin: 30px 0 20px 0;'>
    <h2 style='color: #2E4057; margin: 0;'># Technologies & Tools</h2>
</div>
""", unsafe_allow_html=True)

tech_col1, tech_col2, tech_col3 = st.columns(3)

with tech_col1:
    st.markdown("""
    <div style='background: #f8f9fa; padding: 15px; border-radius: 8px; height: 100%;'>
        <h4 style='color: #2E4057; margin-top: 0;'>Core Technologies</h4>
        <ul style='list-style-type: none; padding-left: 0;'>
            <li><code>Python 3.9+</code></li>
            <li><code>TensorFlow 2.13</code></li>
            <li><code>OpenCV 4.8</code></li>
            <li><code>MediaPipe 0.10</code></li>
            <li><code>NumPy</code></li>
            <li><code>Scikit-learn</code></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tech_col2:
    st.markdown("""
    <div style='background: #f8f9fa; padding: 15px; border-radius: 8px; height: 100%;'>
        <h4 style='color: #2E4057; margin-top: 0;'>Frontend & UI</h4>
        <ul style='list-style-type: none; padding-left: 0;'>
            <li><code>Streamlit 1.29</code></li>
            <li><code>Plotly 5.18</code></li>
            <li><code>Custom CSS</code></li>
            <li><code>Real-time Updates</code></li>
            <li><code>Responsive Design</code></li>
        </ul>
        <h4 style='color: #2E4057; margin: 15px 0 5px 0;'>APIs & Backend</h4>
        <ul style='list-style-type: none; padding-left: 0;'>
            <li><code>FastAPI</code></li>
            <li><code>pyttsx3 (TTS)</code></li>
            <li><code>WebSocket Support</code></li>
            <li><code>RESTful APIs</code></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tech_col3:
    st.markdown("""
    <div style='background: #f8f9fa; padding: 15px; border-radius: 8px; height: 100%;'>
        <h4 style='color: #2E4057; margin-top: 0;'>Development Tools</h4>
        <ul style='list-style-type: none; padding-left: 0;'>
            <li><code>VS Code</code></li>
            <li><code>Git & GitHub</code></li>
            <li><code>pip/venv</code></li>
            <li><code>Docker (Planned)</code></li>
            <li><code>Streamlit Cloud</code></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Project Timeline
st.markdown("---")
st.markdown("""
<div style='border-left: 5px solid #73AB84; padding-left: 15px; margin: 30px 0 20px 0;'>
    <h2 style='color: #2E4057; margin: 0;'>|> Project Timeline</h2>
</div>
""", unsafe_allow_html=True)

timeline_data = {
    "Phase": [
        "Literature Review",
        "Data Collection",
        "Model Development",
        "Training & Optimization",
        "Frontend Development",
        "Integration & Testing",
        "Documentation",
        "Final Presentation",
    ],
    "Duration": [
        "2 weeks",
        "3 weeks",
        "4 weeks",
        "3 weeks",
        "3 weeks",
        "2 weeks",
        "2 weeks",
        "1 week",
    ],
    "Status": [
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Ongoing",
    ],
}

# status column
def style_status(val):
    if val == "Completed":
        return 'background-color: #d4edda; color: #155724; padding: 4px 8px; border-radius: 4px;'
    elif val == "Ongoing":
        return 'background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px;'
    return ''

timeline_df = pd.DataFrame(timeline_data)
st.dataframe(timeline_df, use_container_width=True, hide_index=True)

# Work Distribution
st.markdown("""
<div style='border-left: 5px solid #C73E1D; padding-left: 15px; margin: 30px 0 20px 0;'>
    <h2 style='color: #2E4057; margin: 0;'>(%) Work Distribution</h2>
</div>
""", unsafe_allow_html=True)

work_data = {
    "Task": [
        "Literature Survey",
        "Dataset Collection",
        "Model Architecture",
        "Training & Tuning",
        "Frontend UI",
        "Backend API",
        "Integration",
        "Testing",
        "Documentation",
    ],
    "Effort (%)": [10, 15, 15, 20, 15, 10, 5, 5, 5],
}

work_df = pd.DataFrame(work_data)

fig_work = px.pie(
    work_df,
    values="Effort (%)",
    names="Task",
    title="Project Effort Distribution",
    color_discrete_sequence=px.colors.qualitative.Set3,
)
fig_work.update_traces(textposition="inside", textinfo="percent+label")
fig_work.update_layout(height=500)

st.plotly_chart(fig_work, use_container_width=True)

# Acknowledgments
st.markdown("---")
st.markdown("""
<div style='border-left: 5px solid #2E4057; padding-left: 15px; margin: 30px 0 20px 0;'>
    <h2 style='color: #2E4057; margin: 0;'>@ Acknowledgments</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='background: #f8f9fa; padding: 20px; border-radius: 10px;'>
We would like to express our sincere gratitude to:

### » Project Guidance
- **Dr. Seema Gulati** - For continuous guidance, technical expertise, and unwavering support throughout this project
- **Prof. Anupam Singh** - Head of Department, for providing necessary infrastructure and resources
- **All Faculty Members** - Department of CSE, for their valuable feedback and encouragement

### » Open Source Community
- **TensorFlow Team** - For the excellent deep learning framework
- **MediaPipe Team** - For the robust hand tracking solution
- **Streamlit Team** - For the amazing UI framework
- **OpenCV Community** - For comprehensive computer vision tools

### » Special Thanks
- **Dataset Contributors** - Volunteers who helped collect gesture samples
- **Deaf and Hard-of-Hearing Community** - Whose needs inspired this project
- **Family and Friends** - For their patience and moral support

This project would not have been possible without the collective support and contributions of all mentioned above.
</div>
""", unsafe_allow_html=True)

# Publications & Achievements
with st.expander("Publications & Achievements"):
    st.markdown("""
    ### Planned Publications
    - "Real-Time Sign Language Recognition using Hybrid CNN-LSTM Architecture" - IEEE Conference Paper (In Preparation)
    - "Accessible Communication System for Deaf Community: A Deep Learning Approach" - Journal Paper (In Preparation)
    
    ### Achievements
    - Achieved 95.2% accuracy on test dataset
    - Real-time inference at 30 FPS
    - Successfully demonstrated to 50+ users
    """)

# Future Scope
with st.expander("Future Enhancements"):
    st.markdown("""
    ### Planned Features for v2.0
    
    **Multi-Language Support:**
    - American Sign Language (ASL)
    - British Sign Language (BSL)
    - Indian Sign Language (ISL)
    - International Sign (IS)
    
    **Advanced Recognition:**
    - Two-hand gesture recognition
    - Facial expression integration
    - Continuous sign language translation
    - Sentence formation from gesture sequences
    - Context-aware predictions
    
    **Platform Expansion:**
    - Mobile application (iOS/Android)
    - Browser extension for video calls
    - Desktop application (Windows/Mac/Linux)
    - API as a Service for developers
    
    **Performance Improvements:**
    - Model quantization for edge devices
    - Transfer learning for new gestures
    - Federated learning for privacy
    - On-device inference
    
    **User Experience:**
    - Custom gesture training
    - User profiles and preferences
    - Learning mode with tutorials
    - Gamification for practice
    - Community gesture sharing
    """)

# Contact & Collaboration
with st.expander("Contact & Collaboration"):
    st.markdown("""
    ### Get in Touch
    
    **For Academic Collaboration:**
    - Research partnerships welcome
    - Dataset sharing opportunities
    - Joint publications
    
    **Contact Information:**
    - **Email:** neerajkandpal265@gmail.com  
    - **LinkedIn:** https://www.linkedin.com/in/neeraj-kandpal/ 
    - **GitHub:** https://github.com/neerajkandpal2411
    """)

# Footer
st.markdown("---")
st.markdown(
    """
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>© 2026 SignSpeak • Final Year Major Project • All Rights Reserved</p>
    <br>
    <p style='font-size: 0.9rem;'>
        Department of Computer Science & Engineering<br>
        Graphic Era Hill University <br>
        Dehradun, Uttarakhand
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# Sidebar Info
with st.sidebar:
    st.markdown("## Project Info")
    st.info("""
    **Project ID:** GEHU-2026-CS-001
    
    **Submission Date:** 02 May 2026
    
    **Version:** 1.0.0
    
    **License:** MIT
    """)

    st.markdown("## Quick Links")

    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/neerajkandpal2411/SignSpeak)")

    report_path = "docs/Report_File.pdf"
    if os.path.exists(report_path):
        with open(report_path, "rb") as file:
            st.download_button(
                label="Download Project Report",
                data=file,
                file_name="Report_File.pdf",
                mime="application/pdf"
            )
    else:
        st.markdown("[Project Report](docs/Report_File.pdf)")

    paper_path = "docs/Research_Paper.pdf"
    if os.path.exists(paper_path):
        with open(paper_path, "rb") as file:
            st.download_button(
                label="Download Research Paper",
                data=file,
                file_name="Research_Paper.pdf",
                mime="application/pdf"
            )
    else:
        st.markdown("[Research Paper](docs/Research_Paper.pdf)")
    
    st.markdown("---")
