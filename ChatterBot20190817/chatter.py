'''
Created on Aug 17, 2019

@author: amitbatajoo
'''
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot("Candice")
#bot.set_trainer(ListTrainer)
#bot.set_trainer(ChatterBotCorpusTrainer)
#bot.train("chatterbot.corpus.english")

conversation = open('chats.txt','r').readlines()
 
#bot.train(conversation)
 
while True:
    message = input('You:')
    if message.strip()!= 'Bye':
     reply = bot.get_response(message)
    print('ChatBot:',reply)
    if message.strip()=='Bye':
        print('ChatBot:Bye')
        break