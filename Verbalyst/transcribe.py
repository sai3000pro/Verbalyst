import assemblyai as aai

def transcribe_audio(file_path):
    aai.settings.api_key = "eaa0657c5e5844c383119c365b4a5831"
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_path)
    return transcript.text

# lets me test stuff just in this file
if __name__ == "__main__":
    result = transcribe_audio("./downloads/enoch.mp4")
    print(result)