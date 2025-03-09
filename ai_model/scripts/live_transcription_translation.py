import sounddevice as sd
import numpy as np
import torch
import psycopg2
import keyboard
from datetime import datetime
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor, MarianMTModel, MarianTokenizer

# Load Speech-to-Text (ASR) Model
asr_model_name = "Talha/URDU-ASR"
asr_processor = Wav2Vec2Processor.from_pretrained(asr_model_name)
asr_model = Wav2Vec2ForCTC.from_pretrained(asr_model_name)

# Load Translation Model
translation_model_path = r"E:\\Urdu-To-English-Machine-Translation\\opus-mt-ur-en-finetuned-ur-to-en\\checkpoint-1260"
translation_tokenizer = MarianTokenizer.from_pretrained(translation_model_path)
translation_model = MarianMTModel.from_pretrained(translation_model_path)

# Database Connection
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
cursor = conn.cursor()

# Function to record audio (Manual Stop)
def record_audio(sr=16000):
    print("\nRecording... Press ENTER to stop.")
    audio = []

    def callback(indata, frames, time, status):
        if status:
            print(status)
        audio.extend(indata[:, 0])

    stream = sd.InputStream(samplerate=sr, channels=1, callback=callback)
    stream.start()

    keyboard.wait("enter")  # Wait for user to press Enter to stop recording
    stream.stop()
    print("Recording stopped!\n")
    
    return np.array(audio)

# Function to transcribe Urdu speech
def transcribe_audio(audio):
    input_values = asr_processor(audio, return_tensors="pt", sampling_rate=16000).input_values
    with torch.no_grad():
        logits = asr_model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    return asr_processor.decode(predicted_ids[0])

# Function to translate Urdu text to English
def translate_text(urdu_text):
    inputs = translation_tokenizer(urdu_text, return_tensors="pt", padding=True, truncation=True)
    translated_tokens = translation_model.generate(**inputs)
    return translation_tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

# Function to store transcription in the database
def save_to_database(audio_filename, urdu_transcription, english_translation):
    query = """
    INSERT INTO transcriptions (audio_filename, urdu_transcription, english_translation)
    VALUES (%s, %s, %s);
    """
    cursor.execute(query, (audio_filename, urdu_transcription, english_translation))
    conn.commit()
    print("Data saved to database!")

# Real-time processing loop
def live_transcribe_and_translate():
    while True:
        audio_data = record_audio()  # No fixed duration, stops on Enter
        urdu_transcription = transcribe_audio(audio_data)
        
        print(f"Transcription (Urdu): {urdu_transcription}")

        if urdu_transcription.strip():
            english_translation = translate_text(urdu_transcription)
            print(f"Translation (English): {english_translation}")

            # Save to DB
            audio_filename = f"recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
            save_to_database(audio_filename, urdu_transcription, english_translation)
        
        cont = input("\nPress Enter to continue, or type 'exit' to quit: ")
        if cont.lower() == "exit":
            print("Exiting live demo...")
            break

# Run the live transcription & translation
if __name__ == "__main__":
    live_transcribe_and_translate()

# Close database connection on exit
cursor.close()
conn.close()
