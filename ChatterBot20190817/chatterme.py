'''
Created on Aug 17, 2019

@author: amitbatajoo
'''
# 
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# 
# bot = ChatBot('MyChand')
# bot.set_trainer(cha)
# 
# conversation=open('chats.txt').readlines()
# bot.train(conversation)
#  
# while True:
#     message = input('You:')
#     if message.strip()!= 'Bye':
#      reply = bot.get_response(message)
#     print('ChatBot:',reply)
#     if message.strip()=='Bye':
#         print('ChatBot:Bye')
#         break
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
print(chatbot.get_response("Hello, how are you today?"))