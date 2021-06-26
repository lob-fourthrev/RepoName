# First we will import the ChatBot module
from chatterbot import ChatBot
# Then we will need a way to train our chatbot so we will use ChatterBotCorpusTrainer for a general purpuse chatbot
from chatterbot.trainers import ListTrainer
import json
from django.conf import settings


# Open the nfL6.json file that we downloaded and copied over to the project with read permissions then read the file into qa_data
with open(str(settings.BASE_DIR) + '/qa_chat/nfL6.json', 'r') as f:
    qa_data = f.read()

qa_json = json.loads(qa_data)


# Declare a variable that will be used to hold the training data as a list for our chatbot
train = []
# Populate our list train with questions and answers by extracting them from json
# The process might take a while! Do not interrupt it.
for k, r in enumerate(qa_json):
    train.append(r['question'])
    train.append(r['answer'])

# Now we will create an name our chatbot, I have named mine Lyra but feed free to play around
chatbot = ChatBot('Lyra')

# Next up we need to use the newly create trainer to train our chatbot we will use the provided training sets from github for english, you can change the language here as well if you wish
trainer = ListTrainer(chatbot)
trainer.train(train)

# Here we will make a function that will take in a string and will pass that string to the chatbot in order to get a response from the chatbot
def talk(msg):
    return chatbot.get_response(msg)
