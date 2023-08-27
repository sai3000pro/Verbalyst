import assemblyai as aai

def transcribe_audio(file_path):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_path)
    return transcript.text

if __name__ == "__main__":
    result = transcribe_audio("uploadedFile")
    print(result)