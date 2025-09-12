'''
VOICE ASSISTANT "GOSHA" V0.0.1 
COPYRIGHT, 2025 (C)

LICENSE: GNU GENERAL PUBLIC LICENSE V3.0
FILE: voice.py
'''

import wave
import pyaudio

def voiceStart(file_path):
    wf = wave.open(file_path, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    chunk_size = 1024
    data = wf.readframes(chunk_size)
    while data:
        stream.write(data)
        data = wf.readframes(chunk_size)
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()
