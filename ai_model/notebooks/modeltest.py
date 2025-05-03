
# Step 2: Import libraries
import sounddevice as sd
from scipy.io.wavfile import write
import torch
import torchaudio
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import soundfile as sf

# Step 3: Record audio
def record_audio(filename="urdu_test.wav", duration=5, fs=16000):
    print(f"🎙️ Recording for {duration} seconds... Speak now!")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    write(filename, fs, recording)
    print("✅ Recording saved as", filename)

# Record 5 seconds of audio
record_audio(duration=5)

# Step 4: Load Whisper tiny model for Urdu transcription
model_name = "openai/whisper-tiny"
processor = WhisperProcessor.from_pretrained(model_name)
model = WhisperForConditionalGeneration.from_pretrained(model_name)
model.to("cpu")

# Step 5: Load and preprocess audio
audio_path = "urdu_test.wav"
waveform, sample_rate = sf.read(audio_path)

# Resample if needed
if sample_rate != 16000:
    resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
    waveform = resampler(waveform)
    sample_rate = 16000

# Step 6: Prepare input features
input_features = processor(waveform, sampling_rate=16000, return_tensors="pt").input_features
forced_decoder_ids = processor.get_decoder_prompt_ids(language="ur", task="transcribe")

# Step 7: Generate transcription
with torch.no_grad():
    predicted_ids = model.generate(input_features, forced_decoder_ids=forced_decoder_ids)

# Step 8: Decode and display
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
print("📝 Urdu Transcription:", transcription)
