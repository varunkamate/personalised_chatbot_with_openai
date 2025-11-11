import random
import numpy as np
import json
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download NLTK resources
nltk.download('punkt')

intent={
    'intent':[
        {
            'tag':'greeting',
            'patterns':['Hi','Hello','Hey','Good morning','Good evening'],
            'response':['Hello','Hi','Hey how are you',"How can i help you!"]
        },
        {
            'tag':'goodbye',
            'patterns':['Bye','See you later','Good bye'],
            "responses": ["Goodbye!", "See you soon!", "Take care!"]
        },
        {
            "tag": "thanks",
            "patterns": ["Thanks", "Thank you", "Appreciate it"],
            "responses": ["You're welcome!", "Glad to help!", "Anytime!"]
        },
        {
            "tag": "help",
            "patterns": ["I need help", "Can you assist me?", "Please help me"],
            "responses": ["Sure, what do you need help with?", "I'm here to help!"]
        }
    ]
}

tags=[]
patterns=[]
for i in intent["intent"]:
    for j in i['patterns']:
        patterns.append(j)
        tags.append(i['tag'])


vectorization=CountVectorizer()
x=vectorization.fit_transform(patterns)

model=MultinomialNB()
model.fit(x,tags)

def chatbot_response(text):
    tex_vector=vectorization.transform([text])
    tag=model.predict(tex_vector)[0]

    for i in intent['intent']:
        if i['tag']==tag:
            return random.choice(i['response'])
        else:
            return "Sorry didn't understood what your saying"
        
    
#chat bot loop
print("hey! type qite or bye to exit from the chat")

while True:
    user_input=input("you:")
    if user_input.lower()=='quit' or user_input.lower()=='bye':
        print('chatbot:bye have a good day😊🙏')
        break
    else:
        response=chatbot_response(user_input)
        print('chatbot:',response)
