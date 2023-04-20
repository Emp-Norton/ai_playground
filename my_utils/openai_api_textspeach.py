import os
import openai


def transcribe(VID_DIR):
    if VID_DIR is not None:
        try:
            for file in os.listdir(VID_DIR):
                f = os.path.join(VID_DIR, file)
                if os.path.isfile(f):
                    audio_file = open(f, 'rb')
                    transcript = openai.Audio.transcribe('whisper-1', audio_file)
                    print(transcript)
                    print('-------------------------------\n\n')
        except Exception as e:
            print('Failed with {e} on file {file}')

