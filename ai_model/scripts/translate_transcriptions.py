import pandas as pd
import torch
from transformers import MarianMTModel, MarianTokenizer

model_dir = r"E:\\Urdu-To-English-Machine-Translation\\opus-mt-ur-en-finetuned-ur-to-en\\checkpoint-1260"
tokenizer = MarianTokenizer.from_pretrained(model_dir)
model = MarianMTModel.from_pretrained(model_dir)

input_csv = "ai_model/data/processed_data/transcribed_audio.csv" 
output_csv = "ai_model/data/processed_data/translated_transcriptions.csv"  

df = pd.read_csv(input_csv)


if 'transcription' not in df.columns:
    raise ValueError("CSV file does not contain 'transcription' column")

translations = []
for idx, text in enumerate(df['transcription']):
    if pd.isna(text) or not text.strip(): 
        translations.append("")
        continue
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        translated_ids = model.generate(**inputs)
    translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)
    translations.append(translated_text)

    if idx % 100 == 0:
        print(f"Translated {idx}/{len(df)} transcriptions")

#saving
df["translated_text"] = translations
df.to_csv(output_csv, index=False)

print("Translation complete. Output saved to:", output_csv)
