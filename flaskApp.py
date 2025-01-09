from flask import Flask, request, jsonify
from flask_cors import CORS
import librosa
import numpy as np
import whisper
import tempfile
import os

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    if hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"

app = Flask(__name__)
CORS(app)

model = whisper.load_model("base")

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            file.save(temp_file.name)
            y, sr = librosa.load(temp_file.name)
        
        os.unlink(temp_file.name)
        
        audio_array = np.array(y)
        result = model.transcribe(audio_array)
        
        segments = [
            {
                "start": format_time(segment["start"]),
                "end": format_time(segment["end"]),
                "text": segment["text"]
            }
            for segment in result["segments"]
        ]
        
        return jsonify({"segments": segments})

if __name__ == '__main__':
    app.run(debug=True)
