'''

VOICE ASSISTANT "GOSHA" V0.0.1 
COPYRIGHT, 2025 (C)

LICENSE: GNU GENERAL PUBLIC LICENSE V3.0
FILE: config.py

'''

import sys

from ai.chatbot import aiReturn

def play_greetings():
    print("Привет!")

def play_quit():
    print("Привет!")
    sys.exit()

def recog(text):
    for command_tuple, action in keyword.items():
        if text.lower() in command_tuple:
            action()  # Выполняем соответствующую функцию
            return  # Завершаем функцию после выполнения команды
    if text != "":
        aiReturn(text)
    else:
        pass

keyword = {
    ("привет", "здарова", "приветствую", "здравствуйте", "доброе утро","добрый день",
    "добрый вечер","доброй ночи","доброго дня", "доброго утра","доброго вечера"): play_greetings,
    ("пока", "до свидания", "до встречи", "прощай", "всего доброго"): play_quit,
}