# SignSpeak - Real-Time Sign Language Recognition

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13-orange.svg)](https://tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Final Year Major Project - Computer Science & Engineering**

SignSpeak is an AI-powered system that translates sign language gestures into text and speech in real-time, making communication accessible for the deaf and hard-of-hearing community.

![Demo](assets/banner.gif)

## Features

- 🎥 **Real-Time Recognition** - Instant gesture detection at 30 FPS
- 🧠 **Deep Learning** - Hybrid CNN-LSTM architecture with 95.2% accuracy
- 🔊 **Text-to-Speech** - Automatic speech synthesis for recognized gestures
- 📊 **Live Analytics** - Confidence scores and prediction history
- 🎨 **Modern UI** - Professional Streamlit interface
- ♿ **Accessibility** - Designed for users with hearing/speech impairments

## Architecture

Webcam → MediaPipe (21 landmarks) → CNN (Spatial) → LSTM (Temporal) → Gesture → Speech


## Performance

| Metric | Value |
|--------|-------|
| Test Accuracy | 95.2% |
| Inference Time | ~10ms |
| FPS | 30 |
| Supported Gestures | 10 |

## Quick Start

### Prerequisites
- Python 3.9+
- Webcam
- 4GB+ RAM

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/signspeak.git
cd signspeak
