from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch

asr_model_name = "Talha/URDU-ASR"
asr_processor = Wav2Vec2Processor.from_pretrained(asr_model_name)
asr_model = Wav2Vec2ForCTC.from_pretrained(asr_model_name)

def transcribe_audio(audio):
    input_values = asr_processor(audio, return_tensors="pt", sampling_rate=16000).input_values
    with torch.no_grad():
        logits = asr_model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    return asr_processor.decode(predicted_ids[0])