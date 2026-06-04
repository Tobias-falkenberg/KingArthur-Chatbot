def build_prompt(
    user_question,
    context
):
    return f"""
You are a helpful baking assistant.

Use the following product information to answer the user's question.

Context:
{context}

Question:
{user_question}
"""