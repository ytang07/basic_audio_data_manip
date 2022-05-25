import sounddevice
import soundfile

filename = "output_sounddevice.wav"
data, fs = soundfile.read(filename, dtype='float32')
sounddevice.play(data, fs)
status = sounddevice.wait()