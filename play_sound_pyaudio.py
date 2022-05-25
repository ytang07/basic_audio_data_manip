import pyaudio
import wave

# declare constants and initialize portaudio/pyaudio object
filename = 'output_pyaudio.wav'
chunk = 1024
wf = wave.open(filename, 'rb')
pa = pyaudio.PyAudio()

# create stream using info from the file
stream = pa.open(format = pa.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# read in the frames as data
data = wf.readframes(chunk)

# while the data isn't empty
while data != b'':
    stream.write(data)
    data = wf.readframes(chunk)

# cleanup
stream.close()
pa.terminate()