import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

def record_voice(seconds, file, samplerate=44100):
    # Print recording status
    print("Recording Starting.....")
    
    # Fix the sample rate typo (41100 -> 44100)
    # Use float32 dtype for better quality
    recording = sd.rec(int(seconds * samplerate),
                      samplerate=samplerate,
                      channels=2,
                      dtype='float32')
    
    # Wait until recording is finished
    sd.wait()
    
    # Normalize the audio data to prevent clipping
    recording = np.clip(recording, -1, 1)
    # Convert to 16-bit integer format for WAV file
    recording = (recording * 32767).astype(np.int16)
    
    # Save the file
    write(file, samplerate, recording)
    print("Recording is Finished.....")

# Test recording for 10 seconds
record_voice(10, "recordsave.wav")


