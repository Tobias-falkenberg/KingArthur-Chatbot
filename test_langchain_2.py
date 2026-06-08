import os

os.environ["NO_PROXY"] = "localhost,127.0.0.1"

from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2:3b"
)

print(
    llm.invoke(
        "hello"
    )
)