'''

VOICE ASSISTANT "GOSHA" V0.0.1 
COPYRIGHT, 2025 (C)

LICENSE: GNU GENERAL PUBLIC LICENSE V3.0
FILE: config.py

'''

import sys
import os
import random

from ai.chatbot import aiReturn
from voice import voiceStart

FULL_NAME = "Гоша | Голосовой ассистент"
VERSION = "0.0.1"
STATUS = "BETA VERSION"
AUTHOR = "FILCHER"
AUTHOR_GITHUB = "https://github.com/filcherock"
LICENSE = "GNU GENERAL PUBLIC LICENSE V3.0"
REPOS = "https://github.com/filcherock/gosha"

def play_greetings():
    voiceStart(f"{os.getcwd()}/voice/greeting{random.randint(1, 3)}.wav")
    print("Done!")

def play_quit():
    voiceStart(f"{os.getcwd()}/voice/end{random.randint(1, 3)}.wav")
    sys.exit()

def recog(text):
    for command_tuple, action in keyword.items():
        if text.lower() in command_tuple:
            action()
            return
    if text != "":
        aiReturn(text)
    else:
        pass

keyword = {
    ("привет", "здарова", "приветствую", "здравствуйте", "доброе утро","добрый день",
    "добрый вечер","доброй ночи","доброго дня", "доброго утра","доброго вечера"): play_greetings,
    ("пока", "до свидания", "до встречи", "прощай", "всего доброго"): play_quit,
}