import assemblyai as aai

def transcribe_audio(file_path):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_path)
    return transcript.text

if __name__ == "__main__":
    result = transcribe_audio("uploadedFile")
    print(result)

# aai.settings.api_key = "eaa0657c5e5844c383119c365b4a5831"

# # URL of the file to transcribe
# FILE_URL = "https:p[-0;.f//github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"


# transcriber = aai.Transcriber()
# transcript = transcriber.transcribe(FILE_URL)

# print(transcript.text)
