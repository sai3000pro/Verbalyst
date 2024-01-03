from flask import Flask, request, render_template
import assemblyai as aai
from ai import AIResponse

app = Flask(__name__)


aai.settings.api_key = '${process.env.AAI}'

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
    # temp_file_path = './temp_file.mp3'
    # uploaded_file.save(temp_file_path)

    # Perform transcription using the transcribe_audio function
    transcription_result = transcribe_audio(uploaded_file)
    # Remove the temporary file
    # import os
    # os.remove(temp_file_path)

    response_html = AIResponse(transcription_result)
    return render_template('stats.html', response_html=response_html, transcription_result=transcription_result)


@app.route('/stats.html')
def stats():
    return render_template('stats.html')



if __name__ == '__main__':
    app.run()