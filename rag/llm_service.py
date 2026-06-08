def ask_llm(
    chain,
    history,
    context,
    question
):
    try:

        return chain.invoke(
            {
                "history": history,
                "context": context,
                "question": question
            }
        )

    except Exception as e:

        return (
            f"LLM Error: {e}"
        )