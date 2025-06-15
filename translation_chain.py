import os
from langchain_groq.chat_models import ChatGroq
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema.runnable import Runnable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
from dotenv import load_dotenv
load_dotenv()
# Initialize Groq LLM
model = ChatGroq(api_key=GROQ_API_KEY, model="llama3-8b-70b")  # adjust model if necessary

# Prompt Template
prompt = ChatPromptTemplate.from_template("Translate this from English to French:\n{input}")

# Define a Runnable (Chain) to connect prompt + LLM
translation_chain = prompt | model
