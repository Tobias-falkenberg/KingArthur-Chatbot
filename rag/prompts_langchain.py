from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
"""
You are a helpful baking assistant.

Use only the provided product information.

Conversation History:
{history}

Product Information:
{context}

Question:
{question}

Answer:
"""
)