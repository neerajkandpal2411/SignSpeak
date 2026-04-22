# Import pandas and plotly for timeline and work distribution
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Team - SignSpeak", page_icon="👥")

st.title("Project Information")
st.markdown("Final Year Major Project - Computer Science & Engineering")

# Project Header
st.markdown("---")

# Team Member Section
st.markdown("## Development Team")

# Team Member 1
col1, col2 = st.columns([1, 3])
with col1:
    st.image("images/nee.jpg", width=150)
with col2:
    st.markdown("""
    ### Neeraj Kandpal - [Team Lead]
    **Bachelor of Technology - Computer Science & Engineering**
    **Student ID:** 22019143
    
    *Graphic Era Hill University*
    
    **Email:** neerajkandpal265@gmail.com  
    **LinkedIn:** https://www.linkedin.com/in/neeraj-kandpal/ 
    **GitHub:** https://github.com/neerajkandpal2411
    
    **Role:** Full Stack Developer, ML Engineer
    """)
st.markdown("---")

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
    **LinkedIn:** https://www.linkedin.com/in/vedaansh-vishwakarma-057a7124b/
    **GitHub:** https://github.com/vedaansh12
    
    **Role:** Full Stack Developer, ML Engineer
    """)
st.markdown("---")

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
    **LinkedIn:** https://www.linkedin.com/in/abhishek-rawal955
    **GitHub:** https://github.com/abhi-rawal
    
    **Role:** Full Stack Developer, ML Engineer
    """)
st.markdown("---")

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
    **LinkedIn:** https://www.linkedin.com/in/harsh-bahuguna-32a331355/
    
    **Role:** Full Stack Developer, ML Engineer
    """)

# Project Guide
st.markdown("---")
st.markdown("## Project Guide")

st.markdown("""
    ### Dr. Seema Gulati
    **Assistant Professor**  
    Department of Computer Science & Engineering  
    Graphic Era Hill University

    **Expertise:** Machine Learning, Computer Vision, Deep Learning

    **Role:** Project Supervisor & Technical Mentor
    """)

# Project Details
st.markdown("---")
st.markdown("## Project Information")

details_col1, details_col2 = st.columns(2)

with details_col1:
    st.markdown("""
    ### Academic Details
    - **Course:** B.Tech Final Year Project
    - **Semester:** 8th Semester
    - **Academic Year:** 2025-2026
    - **Project Duration:** 6 months
    - **Project Type:** Research & Development
    - **Credit Hours:** 12
    
    ### Technical Domain
    - Deep Learning
    - Computer Vision
    - Human-Computer Interaction
    - Accessibility Technology
    - Real-Time Systems
    """)

with details_col2:
    st.markdown("""
    ### Project Objectives
    1. Real-time sign language recognition
    2. Accessibility for deaf/mute community
    3. Bridge communication gaps
    4. Demonstrate CNN-LSTM architecture
    5. Achieve >90% accuracy
    6. User-friendly interface
    
    ### Target Users
    - Deaf and hard-of-hearing individuals
    - Sign language learners
    - Educational institutions
    - Healthcare facilities
    - Public service centers
    """)

# Technologies Used
st.markdown("---")
st.markdown("## Technologies & Tools")

tech_col1, tech_col2, tech_col3 = st.columns(3)

with tech_col1:
    st.markdown("""
    ### Core Technologies
    - **Python 3.9+**
    - **TensorFlow 2.13**
    - **OpenCV 4.8**
    - **MediaPipe 0.10**
    - **NumPy**
    - **Scikit-learn**
    """)

with tech_col2:
    st.markdown("""
    ### Frontend & UI
    - **Streamlit 1.29**
    - **Plotly 5.18**
    - **Custom CSS**
    - **Real-time Updates**
    - **Responsive Design**
    
    ### APIs & Backend
    - **FastAPI**
    - **pyttsx3 (TTS)**
    - **WebSocket Support**
    - **RESTful APIs**
    """)

with tech_col3:
    st.markdown("""
    ### Development Tools
    - **VS Code**
    - **Git & GitHub**
    - **pip/venv**
    - **Docker (Planned)**
    - **Streamlit Cloud**
    """)

# Project Timeline
st.markdown("---")
st.markdown("## Project Timeline")

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
        "Completd",
        "Ongoing",
    ],
}

timeline_df = pd.DataFrame(timeline_data)
st.dataframe(timeline_df, use_container_width=True, hide_index=True)

# Work Distribution
st.markdown("## Work Distribution")

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
st.markdown("## Acknowledgments")

st.markdown("""
We would like to express our sincere gratitude to:

### Project Guidance
- **Dr. Seema Gulati** - For continuous guidance, technical expertise, and unwavering support throughout this project
- **Prof. Anupam Singh** - Head of Department, for providing necessary infrastructure and resources
- **All Faculty Members** - Department of CSE, for their valuable feedback and encouragement

### Open Source Community
- **TensorFlow Team** - For the excellent deep learning framework
- **MediaPipe Team** - For the robust hand tracking solution
- **Streamlit Team** - For the amazing UI framework
- **OpenCV Community** - For comprehensive computer vision tools

### Research & Inspiration
- Authors of research papers on CNN-LSTM architectures for gesture recognition
- Contributors to sign language recognition datasets
- Accessibility technology researchers and advocates

### Special Thanks
- **Dataset Contributors** - Volunteers who helped collect gesture samples
- **Deaf and Hard-of-Hearing Community** - Whose needs inspired this project
- **Family and Friends** - For their patience and moral support
- **Batchmates** - For testing and providing valuable feedback

This project would not have been possible without the collective support and contributions of all mentioned above.
""")

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
    st.markdown("""
    - [GitHub Repository](#)
    - [Project Report](#)
    - [Research Paper](#)
    """)
