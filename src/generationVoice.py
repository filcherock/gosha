'''

VOICE ASSISTANT "GOSHA" V0.0.1 
COPYRIGHT, 2025 (C)

LICENSE: GNU GENERAL PUBLIC LICENSE V3.0
FILE: generationVoice.py

'''

import gtts

def greatingVoiceGenerated():
    tts = gtts.gTTS("Привет, рад тебя видеть!", lang='ru')
    tts.save("greeting1.mp3")

    tts = gtts.gTTS("Приветствую тебя", lang='ru')
    tts.save("greeting2.mp3")

    tts = gtts.gTTS("Здравствуй", lang='ru')
    tts.save("greeting3.mp3")

def endVoiceGenerated():
    tts = gtts.gTTS("Пока пока", lang='ru')
    tts.save("end1.mp3")

    tts = gtts.gTTS("До встречи!", lang='ru')
    tts.save("end2.mp3")

    tts = gtts.gTTS("Всего доброго", lang='ru')
    tts.save("end3.mp3")

def actionVoiceGenerated():
    tts = gtts.gTTS("Все к твоим услугам!", lang='ru')
    tts.save("action1.mp3")

    tts = gtts.gTTS("Считай что сделано!", lang='ru')
    tts.save("action2.mp3")

    tts = gtts.gTTS("Готово", lang='ru')
    tts.save("action3.mp3")

def allVoiceGenerated():
    greatingVoiceGenerated()
    endVoiceGenerated()
    actionVoiceGenerated()

def main():
    allVoiceGenerated()

if __name__ == '__main__':
    main()