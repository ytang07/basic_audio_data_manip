from pydub import AudioSegment

# start at 0 milliseconds
# end at 1500 milliseconds
start = 0
end = 1500

sound = AudioSegment.from_wav("output_pyaudio.wav")
extract = sound[start:end]

extract.export("trimmed_output_pydub.wav", format="wav")