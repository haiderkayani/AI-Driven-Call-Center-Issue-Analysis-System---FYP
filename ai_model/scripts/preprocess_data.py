import pandas as pd
from transformers import Wav2Vec2CTCTokenizer

# Define paths
tokenizer_dir = "e:/AI-Driven-Call-Center-Issue-Analysis-System---FYP/ai_model/data"
merged_vocab_path = f"{tokenizer_dir}/merged_vocab.json"
dataset_path = f"{tokenizer_dir}/dataset.tsv"

# Load tokenizer
tokenizer = Wav2Vec2CTCTokenizer(
    merged_vocab_path, unk_token="[UNK]", pad_token="<pad>", bos_token="<s>", eos_token="</s>"
)

# Load dataset
df = pd.read_csv(dataset_path, sep="\t")

# Tokenize text column
df["encoded_text"] = df["sentence"].apply(lambda x: tokenizer(x)["input_ids"])

# Save processed dataset
processed_data_path = f"{tokenizer_dir}/processed_data/processed_data.csv"
df.to_csv(processed_data_path, index=False)

print(f"Processed dataset saved at {processed_data_path}")
