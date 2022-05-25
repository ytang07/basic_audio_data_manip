import ffmpeg

audio_input = ffmpeg.input("output_sounddevice.wav")
audio_cut = audio_input.audio.filter('atrim', duration=1)
audio_output = ffmpeg.output(audio_cut, 'trimmed_output_ffmpeg.wav', format='wav')
ffmpeg.run(audio_output)