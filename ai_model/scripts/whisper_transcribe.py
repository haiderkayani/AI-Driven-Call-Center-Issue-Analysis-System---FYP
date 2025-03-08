import os
import whisper
import pandas as pd

# Load Whisper model
model = whisper.load_model("base")  # Change to "small", "medium", or "large" if needed

# Path to audio files
audio_dir = r"E:\AI-Driven-Call-Center-Issue-Analysis-System---FYP\\ai_model\data\\limited_wav_files\\limited_wav_files"
dataset_path = "ai_model/data/dataset.tsv"
output_file = "ai_model/data/transcriptions.csv"

# Load dataset
df = pd.read_csv(dataset_path, sep="\t")  # Adjust if file format is different

# Pick a random sample of 100 files
sample_files = df.sample(n=50, random_state=42)  # Change number if needed

# Store results
results = []

for _, row in sample_files.iterrows():
    file_name = row["path"]
    actual_transcription = row["sentence"]  # The dataset's existing transcription

    file_path = os.path.join(audio_dir, file_name)
    
    if not os.path.exists(file_path):
        print(f"Skipping {file_name}, file not found.")
        continue

    print(f"Transcribing: {file_name}")
    whisper_transcription = model.transcribe(file_path)["text"]

    results.append({
        "filename": file_name,
        "dataset_transcription": actual_transcription,
        "whisper_transcription": whisper_transcription
    })

# Save results to a CSV file
comparison_df = pd.DataFrame(results)
comparison_df.to_csv(output_file, index=False)

print(f"Sample transcriptions saved to {output_file}")