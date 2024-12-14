import librosa
import numpy as np

#extracting log-mel spectograms from an audio file
def extract_features(audio_path, sr=16000, n_mels=128, duration=5): #audio path, sampling rate, no. of mel bands, duration to truncate audio
    try:
        audio, _ = librosa.load(audio_path, sr=sr, mono=True, duration=duration)

        #pad/truncating for fixed length
        target_length = sr * duration
        if len(audio) < target_length:
            audio = np.pad(audio, (0, target_length - len(audio)))
        else:
            audio = audio[:target_length]

        #computing mel spectrogram
        mel_spec = librosa.feature.melspectrogram(audio, sr=sr, n_mels=n_mels)
        #converting to log scale
        log_mel_spec = librosa.power_to_db(mel_spec, ref=np.max)

        return log_mel_spec
    except Exception as e:
        print(f"Error processing {audio_path}: {e}")
        return None
