import os
import openai
from dotenv import load_dotenv

load_dotenv()

#set_up_api
openai.api_key=os.getenv("you_api_key")

#creating function for it
def chatbot_response(prompt):
    try:
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {'role':'system','content':"hey your helpful chat bot"},
                {'role':'user','content':prompt}
                ],
                max_tokens=100,
                temperature=0.7
        )
        reply=response['choices'][0]['message']['content'].strip()
        return reply
    except Exception as e:
        return f"Error:{e}"
    

print("hey type quite or bye to exit the chat")

#loop
while True:
    user_input=input("you:")
    if user_input in ['quite','bye']:
        print("Bye have a good day")
        break
    else:
        response=chatbot_response(user_input)
        print("cahtbot",response)

        
