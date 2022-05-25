from pydub import AudioSegment
from pydub.playback import play

sound1 = AudioSegment.from_wav("louder_output.wav")
sound2 = AudioSegment.from_wav("quieter_output.wav")

overlay = sound1.overlay(sound2, position=1000)

play(overlay)
overlay.export("overlaid_1sec_offset.wav", format="wav")