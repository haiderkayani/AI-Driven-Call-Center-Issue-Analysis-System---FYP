from transformers import Wav2Vec2Tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-large-960h")
print(tokenizer.convert_tokens_to_ids("[UNK]"))  # Check the index of [UNK]