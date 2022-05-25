from pydub import AudioSegment
from pydub.playback import play

sound1 = AudioSegment.from_wav("louder_output.wav")
sound2 = AudioSegment.from_wav("quieter_output.wav")

combined = sound1 + sound2

play(combined)
combined.export("louder_and_quieter.wav", format="wav")