import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize



device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('/Users/felixschekerka/Desktop/Strive School/ai_jan22_felix/Chapter 03/15. Chatbot/felix_intents.json', 'r') as json_data:
    intents = json.load(json_data)

data = torch.load('/Users/felixschekerka/Desktop/Strive School/ai_jan22_felix/Chapter 03/15. Chatbot/trained.pth')

model_state = data['model_state']
input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']




model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# TBD: prepare a command-line conversation (don't forget something to make the user exit the script!)

bot_name = 'Felix'
print('Lets have a chat! (type "exit" to stop chatting')

while True:
    sentence = input('You: ')
    if sentence == 'exit':
        print('Thanks for showing')
        break
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    print(prob)
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: I do not understand. Try to be more specific")