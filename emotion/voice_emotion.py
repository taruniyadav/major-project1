import sounddevice as sd
import numpy as np
import librosa
import tempfile
import scipy.io.wavfile as wav

def record_audio(duration=3, fs=22050):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print("Recording complete.")

    return recording.flatten(), fs


def extract_mfcc(audio, fs):
    mfcc = librosa.feature.mfcc(y=audio, sr=fs, n_mfcc=13)
    return np.mean(mfcc.T, axis=0)


def detect_voice_emotion():
    audio, fs = record_audio()

    mfcc_features = extract_mfcc(audio, fs)

    # TEMPORARY RULE-BASED PLACEHOLDER
    energy = np.mean(np.abs(audio))

    if energy > 0.05:
        return "excited", 0.75
    else:
        return "calm", 0.70
