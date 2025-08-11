import requests
import streamlit as st

def get_response_from_ollama(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={'input': {"topic": input_text}}  # Correct usage
    )
    return response.json().get('output', 'No response from model')  

# Streamlit framework
st.title("Ollama LLM Chatbot")
input_text = st.text_input("Enter a topic for the poem:")
if input_text:
    with st.spinner("Generating poem..."):
        try:
            response = get_response_from_ollama(input_text)
            st.write("Generated Poem:")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
