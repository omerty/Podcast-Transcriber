import librosa
import numpy as np 
import whisper

y, sr = librosa.load("podcast.mp3")
audio_array = np.array(y)


model = whisper.load_model("base")
result = model.transcribe(audio_array)

for segment in result["segments"]:
    start_time = segment["start"]
    end_time = segment["end"]
    text = segment["text"]
    print(f"{start_time:.2f} - {end_time:.2f}: {text}")



