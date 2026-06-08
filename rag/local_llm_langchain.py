import os

os.environ["NO_PROXY"] = "localhost,127.0.0.1"

from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2:3b",
    base_url="http://127.0.0.1:11434"
)

def generate_answer(prompt):
    return llm.invoke(prompt)