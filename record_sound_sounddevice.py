import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 3

recording = sd.rec(int(seconds*fs), samplerate=fs, channels=1)
sd.wait()
write('output_sounddevice.wav', fs, recording)