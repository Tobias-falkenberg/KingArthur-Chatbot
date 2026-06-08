from retrieval import (
    retrieve_documents,
    build_context,
)

from llm_service import (
    ask_llm
)


def run_rag_pipeline(
    question,
    state,
    model,
    index,
    embeddings_data,
    chain,
    top_k
):

    search_query = (
        state.get_history_text()
        + "\n"
        + question
    )

    retrieved_documents = retrieve_documents(
        search_query,
        model,
        index,
        embeddings_data,
        top_k
    )

    context = build_context(
        retrieved_documents
    )

    answer = ask_llm(
        chain,
        state.get_history_text(),
        context,
        question
    )

    return answer