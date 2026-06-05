def build_prompt(
    user_question,
    context
):
    return f"""
You are a helpful baking assistant.

Use only the provided product information.

Answer the user's question clearly and naturally.

Do not repeat the context.
Do not repeat the question.
Do not mention "Context".
Do not mention "Retrieved Context".

Product Information:
{context}

Question:
{user_question}

Answer:
"""