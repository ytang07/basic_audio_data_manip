from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_wav("new_fs_output_pydub.wav")

# 3 dB up
louder = sound + 3
# 3 dB down
quieter = sound - 3

play(louder)
play(quieter)

louder.export("louder_output.wav", format="wav")
quieter.export("quieter_output.wav", format="wav")