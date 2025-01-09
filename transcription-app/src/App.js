import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [transcription, setTranscription] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file) {
      alert('Please select a file first!');
      return;
    }

    setIsLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/transcribe', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setTranscription(response.data.segments);
    } catch (error) {
      console.error('Error transcribing file:', error);
      alert('Error transcribing file. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Audio Transcription</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} accept=".mp3" />
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Transcribing...' : 'Transcribe'}
        </button>
      </form>
      {transcription.length > 0 && (
        <div>
          <h2>Transcription:</h2>
          {transcription.map((segment, index) => (
            <p key={index}>
              <strong>{segment.start} - {segment.end}:</strong> {segment.text}
            </p>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
