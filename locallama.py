# from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama 
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["OLLAMA_API_KEY"] = os.getenv("OLLAMA_API_KEY")  
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")
# os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

## prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "{input}"),
    ]
)

## streamlit app
st.title("Local Llama Chatbot")
st.write("This is a simple chatbot using Local Llama.")
input_text = st.text_input("Enter your message:")

## ollama LLAma2 LLM
llm = Ollama(model="llama2:7B")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    with st.spinner("Generating response..."):
        try:
            response = chain.invoke({"input": input_text})
            st.write("Response:", response)
        except Exception as e:
            st.error(f"Error: {e}")
