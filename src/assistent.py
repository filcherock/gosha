'''
VOICE ASSISTANT "GOSHA" V0.0.1 
COPYRIGHT, 2025 (C)

LICENSE: GNU GENERAL PUBLIC LICENSE V3.0
FILE: assistent.py
'''

import os
import sys
import json

import vosk
import pyaudio

from config import recog

model_path = "model/vosk-model-small-ru-0.22"

if not os.path.exists(model_path):
    print(f"Модель не найдена по пути: {model_path}")
    sys.exit(1)

vosk.SetLogLevel(0)
model = vosk.Model(model_path)
recognizer = vosk.KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("Скажите что-нибудь:")

while True:
    data = stream.read(4000)
    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()
        result_json = json.loads(result)
        recognized_text = result_json.get('text', '')
        recog(recognized_text)

stream.stop_stream()
stream.close()
p.terminate()
