from transformers import Wav2Vec2CTCTokenizer

# Define paths
VOCAB_PATH = "ai_model/data/vocab.json"

# Create tokenizer
tokenizer = Wav2Vec2CTCTokenizer(
    vocab_file=VOCAB_PATH,
    unk_token="[UNK]",
    pad_token="<pad>",
    word_delimiter_token="|"
)

# Save tokenizer
tokenizer.save_pretrained("ai_model/data/")
print("Tokenizer saved successfully!")
