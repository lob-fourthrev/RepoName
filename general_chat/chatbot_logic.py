# First we will import the ChatBot module
from chatterbot import ChatBot
# Then we will need a way to train our chatbot so we will use ChatterBotCorpusTrainer for a general purpuse chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Now we will create an name our chatbot, I have named mine Lyra but feed free to play around
chatbot = ChatBot('Lyra')

# We need to create a trainer of type ChatterBotCorpusTrainer from the module that we imported and pass along our chatbot Lyra over to the class constructor
trainer = ChatterBotCorpusTrainer(chatbot)

# Next up we need to use the newly create trainer to train our chatbot we will use the provided training sets from github for english, you can change the language here as well if you wish
trainer.train("chatterbot.corpus.english")

# Here we will make a function that will take in a string and will pass that string to the chatbot in order to get a response from the chatbot
def talk(msg):
    return chatbot.get_response(msg)
