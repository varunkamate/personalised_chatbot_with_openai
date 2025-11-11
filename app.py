import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("Your_Api_Key")

# App title
st.set_page_config(page_title="ChatBot with OpenAI", page_icon="🤖", layout="centered")
st.title("🤖 OpenAI Chatbot")
st.write("Ask me anything!")

# Store conversation in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful chatbot."}
    ]

# User input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate chatbot response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages,
            max_tokens=150,
            temperature=0.7,
        )
        reply = response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        reply = f"Error: {e}"

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": reply})

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(reply)

# Display chat history (when user refreshes)
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

