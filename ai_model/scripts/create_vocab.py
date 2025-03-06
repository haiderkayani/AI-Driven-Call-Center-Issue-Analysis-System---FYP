import json
from collections import Counter

# Define paths
DATASET_PATH = "ai_model/data/dataset.tsv"
VOCAB_PATH = "ai_model/data/vocab.json"

# Count character occurrences
char_counter = Counter()
with open(DATASET_PATH, "r", encoding="utf-8") as f:
    next(f)  # Skip header if needed
    for line in f:
        sentence = line.strip().split("\t")[2]  # Assuming text is in the last column
        char_counter.update(sentence)

# Create vocab dictionary
vocab = {char: i for i, (char, _) in enumerate(char_counter.items(), start=1)}
vocab["|"] = len(vocab) + 1  # Space character
vocab["<pad>"] = 0  # Padding token

# Save vocab file
with open(VOCAB_PATH, "w", encoding="utf-8") as f:
    json.dump(vocab, f, ensure_ascii=False, indent=4)

print(f"Vocabulary created and saved at {VOCAB_PATH}!")
