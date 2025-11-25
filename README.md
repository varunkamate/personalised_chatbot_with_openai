# personalised_chatbot_with_openai
This repository contains two different implementations of a chatbot, demonstrating both a simple rule-based approach and a sophisticated AI-powered solution using the OpenAI API.

File Name,Description,Key Technologies
app.py,"Streamlit Web Chatbot (OpenAI API): A fully interactive, web-based chatbot interface built with Streamlit. It uses the gpt-3.5-turbo model via the OpenAI API to maintain conversation history across turns using Streamlit's session state.","Python, Streamlit, OpenAI API"
chatbot_with_openai.py,"Terminal Chatbot (OpenAI API): A command-line interface (CLI) chatbot that directly interacts with the gpt-3.5-turbo model. It is designed for simple, non-session-aware conversations in the terminal.","Python, OpenAI API, dotenv"
chatbot.py,"Rule-Based/NLTK Chatbot: A simple, foundational chatbot that uses classic Natural Language Processing (NLP) techniques, specifically Naive Bayes classification and Bag-of-Words (CountVectorizer), to match user input to pre-defined intents (like 'greeting', 'goodbye', 'help') and provide a random corresponding response.","Python, NLTK, Scikit-learn (CountVectorizer, MultinomialNB)"
