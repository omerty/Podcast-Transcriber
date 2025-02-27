﻿# Podcast Transcriber

Podcast Transcriber is a web application that allows users to upload audio files and receive accurate transcriptions using OpenAI's Whisper model. This tool is perfect for podcast creators, journalists, and anyone who needs to convert spoken content into text.

## Features

- **Audio file upload and transcription**
- **Support for multiple audio formats**
- **Real-time transcription progress updates**
- **Formatted output with timestamps**
- **Easy-to-use web interface**

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** React (JavaScript)
- **Transcription:** OpenAI Whisper
- **Audio Processing:** librosa

## Installation

### Backend Setup

```bash
# Clone the repository
git clone https://github.com/omerty/podcast-transcriber.git
cd podcast-transcriber

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install required packages
pip install -r requirements.txt

# Start the Flask server
python app.py
```

### Front-End Setup

```bash
# Navigate to the frontend directory
cd frontend

# Install required npm packages
npm install

# Start the React development server
npm start
```
