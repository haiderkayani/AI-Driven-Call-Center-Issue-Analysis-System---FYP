import librosa
import numpy as np

def extract_features(audio_path, sr=16000, n_mels=128, duration=5):
    try:
        audio, _ = librosa.load(audio_path, sr=sr, mono=True, duration=duration)

        # Pad/truncate for fixed length
        target_length = sr * duration
        if len(audio) < target_length:
            audio = np.pad(audio, (0, target_length - len(audio)))
        else:
            audio = audio[:target_length]

        # Compute mel spectrogram
        mel_spec = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=n_mels)  # ✅ FIX: Ensure `y=` is used
        log_mel_spec = librosa.power_to_db(mel_spec, ref=np.max)  # Convert to log scale

        return log_mel_spec
    except Exception as e:
        print(f"Error processing {audio_path}: {e}")
        return None
