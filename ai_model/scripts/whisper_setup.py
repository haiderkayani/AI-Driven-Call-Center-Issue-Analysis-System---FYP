import whisper

# Load Whisper model
model = whisper.load_model("base")

def transcribe_audio(file_path):
    result = model.transcribe(file_path)
    return result["text"]


def extract_text(file_path):
    result = model.transcribe(file_path)
    return result["text"]