import os
import time
import torch
import librosa
import pandas as pd
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

#loading model and proc
model_name = "Talha/URDU-ASR"
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)

#defining paths
audio_dir = r"E:\AI-Driven-Call-Center-Issue-Analysis-System---FYP\\ai_model\data\\limited_wav_files\\limited_wav_files"
dataset_path = r"E:\AI-Driven-Call-Center-Issue-Analysis-System---FYP\\ai_model\data\dataset.tsv" 
output_file = "ai_model/data/processed_data/transcribed_audio.csv" 

df = pd.read_csv(dataset_path, sep="\t")
audio_files = df["path"]  
start_time = time.time()
transcriptions = []

#transcription
for idx, file_name in enumerate(audio_files, start=1):
    file_path = os.path.join(audio_dir, file_name)
    
    if not os.path.exists(file_path):
        print(f"Skipping {file_name}, file not found.")
        continue

    #load and process audio
    audio, rate = librosa.load(file_path, sr=16000)
    input_values = processor(audio, return_tensors="pt", sampling_rate=rate).input_values
    with torch.no_grad():
        logits = model(input_values).logits

    #prediction
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])
    transcriptions.append([file_name, transcription])

    elapsed_time = time.time() - start_time
    avg_time_per_file = elapsed_time / idx
    remaining_time = avg_time_per_file * (len(audio_files) - idx)
    print(f"Processed {idx}/{len(audio_files)} files | Time left: {remaining_time:.2f}s")

    if idx % 100 == 0:
        pd.DataFrame(transcriptions, columns=["path", "transcription"]).to_csv(output_file, index=False)

#saving
pd.DataFrame(transcriptions, columns=["path", "transcription"]).to_csv(output_file, index=False)
print("Transcription complete.")