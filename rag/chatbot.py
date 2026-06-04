import json
import numpy as np
import faiss
from prompts import build_prompt
from local_llm import generate_answer
from sentence_transformers import SentenceTransformer

# Functions

def build_context(
    retrieved_documents
):
    return "\n\n".join(
        retrieved_documents
    )



def retrieve_documents(
    user_question,
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

    retrieved_documents = []

    for idx in indices[0]:

        retrieved_documents.append(
            embeddings_data[idx]["text"]
        )

    return retrieved_documents


# Load embeddings data:

with open(
    "data/processed/embeddings.json",
    "r",
    encoding="utf-8"
) as f:

    embeddings_data = json.load(f)

print(
    f"Embeddings Loaded: {len(embeddings_data)}"
)

# Load FAISS:

index = faiss.read_index(
    "data/processed/faiss_index.bin"
)

print(
    f"Vectors in Index: {index.ntotal}"
)

# Load model:

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Model Loaded")

# Ask the user:

user_question = input(
    "\nAsk a question: "
)

TOP_K = 3

retrieved_documents = retrieve_documents(
    user_question,
    TOP_K
)

context = build_context(
    retrieved_documents
)

prompt = build_prompt(
    user_question,
    context
)

answer = generate_answer(
    user_question,
    context
)

print("\nANSWER:\n")
print(answer)

print("\nQuestion:")
print(user_question)

print("\nRetrieved Context:")
print(context)