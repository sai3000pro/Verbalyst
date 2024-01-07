from flask import Flask, request, render_template
import assemblyai as aai
from ai import AIResponse

app = Flask(__name__)


# aai.settings.api_key = '${process.env.AAI}'
aai.settings.api_key = 'eaa0657c5e5844c383119c365b4a5831'

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

    transcription_result = transcribe_audio(uploaded_file)

    response_html = AIResponse(transcription_result)
    return render_template('stats.html', response_html=response_html, transcription_result=transcription_result)


@app.route('/stats.html')
def stats():
    return render_template('stats.html')
    
@app.route('/inspiration')
def inspiration():
    return render_template('inspiration.html')

@app.route('/exercises')
def exercises():
    return render_template('exercises.html')


if __name__ == '__main__':
    app.run()