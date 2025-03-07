import os
from transformers import Wav2Vec2Processor, Wav2Vec2FeatureExtractor, Wav2Vec2CTCTokenizer

# Define paths
data_dir = "ai_model/data"
vocab_path = os.path.join(data_dir, "merged_vocab.json")  # Ensure this is the correct vocab file
processor_path = data_dir  # Where to save the processor

# Load tokenizer
tokenizer = Wav2Vec2CTCTokenizer(
    vocab_path,
    unk_token="[UNK]",
    pad_token="<pad>",
    bos_token="<s>",
    eos_token="</s>"
)

# Create feature extractor
feature_extractor = Wav2Vec2FeatureExtractor(
    feature_size=1,
    sampling_rate=16000,
    padding_value=0.0,
    do_normalize=True,
    return_attention_mask=True
)

# Combine tokenizer and feature extractor into a processor
processor = Wav2Vec2Processor(feature_extractor=feature_extractor, tokenizer=tokenizer)

# Save processor
processor.save_pretrained(processor_path)

print(f"Processor saved successfully at {processor_path}")
