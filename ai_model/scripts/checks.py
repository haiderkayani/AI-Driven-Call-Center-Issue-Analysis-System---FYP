import json
from transformers import Wav2Vec2CTCTokenizer

# Define paths
tokenizer_dir = "e:/AI-Driven-Call-Center-Issue-Analysis-System---FYP/ai_model/data"
vocab_path = f"{tokenizer_dir}/vocab.json"
added_tokens_path = f"{tokenizer_dir}/added_tokens.json"

# Load vocab.json
with open(vocab_path, "r", encoding="utf-8") as f:
    vocab = json.load(f)

# Load added_tokens.json
with open(added_tokens_path, "r", encoding="utf-8") as f:
    added_tokens = json.load(f)

# Merge added tokens into vocab (if not already included)
for token in added_tokens:
    if token not in vocab:
        vocab[token] = len(vocab)  # Assign a new index

# Save the merged vocab (optional, for debugging)
merged_vocab_path = f"{tokenizer_dir}/merged_vocab.json"
with open(merged_vocab_path, "w", encoding="utf-8") as f:
    json.dump(vocab, f, ensure_ascii=False, indent=4)

# Load tokenizer with the fixed vocab
tokenizer = Wav2Vec2CTCTokenizer(merged_vocab_path, unk_token="[UNK]", pad_token="<pad>", bos_token="<s>", eos_token="</s>")

# Test encoding
test_sentence = "یہ ایک ٹیسٹ ہے۔"
encoded = tokenizer(test_sentence)
print("Encoded:", encoded)

decoded_text = tokenizer.decode(encoded["input_ids"])
print("Decoded:", decoded_text)

unknown_test = "یہ ایک ٹیسٹ 🚀 ہے۔"
encoded_unknown = tokenizer(unknown_test)
print("Encoded with unknown char:", encoded_unknown)

