from flask import Flask, request, render_template
import assemblyai as aai
from ai import AIResponse

app = Flask(__name__)


aai.settings.api_key = "eaa0657c5e5844c383119c365b4a5831"

# Import the transcribe_audio function from transcribe.py
from transcribe import transcribe_audio

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return "No file part"

    uploaded_file = request.files['file']

    if uploaded_file.filename == '':
        return "No selected file"

    # Save the uploaded file temporarily
    temp_file_path = './temp_file.mp4'
    uploaded_file.save(temp_file_path)

    # Perform transcription using the transcribe_audio function
    transcription_result = transcribe_audio(temp_file_path)

    # Remove the temporary file
    import os
    os.remove(temp_file_path)

    response_html = AIResponse(transcription_result)
    return render_template('stats.html', response_html=response_html)

@app.route('/stats.html')
def stats():
    return render_template('stats.html')



if __name__ == '__main__':
    app.run()