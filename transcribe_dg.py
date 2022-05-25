from deepgram import Deepgram
from config import dg_secret_key
import asyncio, json

DEEPGRAM_API_KEY = dg_secret_key
PATH_TO_FILE = 'louder_output.wav'

async def main():
    # Initializes the Deepgram SDK
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    # Open the audio file
    with open(PATH_TO_FILE, 'rb') as audio:
        # ...or replace mimetype as appropriate
        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        response = await deepgram.transcription.prerecorded(source, {'punctuate': True})
        json_obj = json.dumps(response, indent=4)
        print(json_obj)
        with open("transcribed.txt", "w") as f:
            f.write(json_obj)

asyncio.run(main())
