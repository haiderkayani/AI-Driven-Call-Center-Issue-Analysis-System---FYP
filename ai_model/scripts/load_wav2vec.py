from transformers import Wav2Vec2Processor

MODEL_NAME = "facebook/wav2vec2-large-xlsr-53"
processor = Wav2Vec2Processor.from_pretrained(MODEL_NAME, force_download=True)

