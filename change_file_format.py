from pydub import AudioSegment

wav_audio = AudioSegment.from_wav("louder_output.wav")
mp3_audio = wav_audio.export("louder.mp3", format="mp3")