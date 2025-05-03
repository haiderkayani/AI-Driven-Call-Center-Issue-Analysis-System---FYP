import sounddevice as sd
import numpy as np
import keyboard

def record_audio(sr=16000):
    print("\nRecording... Press ENTER to stop.")
    audio = []

    def callback(indata, frames, time, status):
        if status:
            print(status)
        audio.extend(indata[:, 0])

    stream = sd.InputStream(samplerate=sr, channels=1, callback=callback)
    stream.start()
    keyboard.wait("enter")
    stream.stop()
    print("Recording stopped!\n")
    return np.array(audio)