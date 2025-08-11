from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()   

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

app = FastAPI(
    title="langserve-ollama",
    version="0.1.0",
    description="A simple FastAPI app using langserve with Ollama LLM.",
)


llm = Ollama(model="llama2:7B")


prompt1 = ChatPromptTemplate.from_template(
    "write me a poem about {topic}."    
)

prompt2 = ChatPromptTemplate.from_template(
    "write me a story about {topic}."
)    
add_routes(
    app,
    prompt1|llm,
    path="/poem"
)

# add_routes(
#     app,
#     prompt2|llm,
#     path="/story",
# )

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",port=8000)