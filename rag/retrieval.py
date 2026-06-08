import numpy as np

def build_context(
    retrieved_documents
):
    context_parts = []

    for doc in retrieved_documents:
        context_parts.append(
            doc["text"]
        )

    return "\n\n".join(
        context_parts
    )
    
    
def retrieve_documents(
    user_question,
    model,
    index,
    embeddings_data,
    top_k=3
):
    query_embedding = model.encode(
        user_question
    )

    query_embedding = np.array(
        [query_embedding],
        dtype="float32"
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )
    
    for rank, (idx, score) in enumerate(
        zip(indices[0], distances[0]),
        start=1
    ):
        print(
            f"{rank}. Score={score}"
        )

    retrieved_documents = []

    for idx in indices[0]:
        retrieved_documents.append(
            embeddings_data[idx]
        )

    return retrieved_documents
