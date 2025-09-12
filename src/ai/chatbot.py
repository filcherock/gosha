from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def aiReturn(text):
    chatbot = ChatBot('MyChatBot')
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.russian') 
    response = chatbot.get_response(text)
    print(response)
