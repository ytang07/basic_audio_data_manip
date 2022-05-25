from pydub import AudioSegment

sound = AudioSegment.from_wav('output_pyaudio.wav')
sound_w_new_fs = sound.set_frame_rate(16000)
sound_w_new_fs.export("new_fs_output_pydub.wav", format="wav")
