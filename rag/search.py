import json
import numpy as np
import faiss

from sentence_transformers import SentenceTransformer

# Load embeddings data

with open(
    "data/processed/embeddings.json",
    "r",
    encoding="utf-8"
) as f:

    embeddings_data = json.load(f)

print(
    f"Embeddings Loaded: {len(embeddings_data)}"
)

# Load FAISS index

index = faiss.read_index(
    "data/processed/faiss_index.bin"
)

print(
    f"Vectors in Index: {index.ntotal}"
)

# Load model

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Model Loaded")

# Ask question

user_question = input(
    "\nAsk a question: "
)

# Create embedding

query_embedding = model.encode(
    user_question
)

print(type(query_embedding))
print(len(query_embedding))

# Convert for FAISS

query_embedding = np.array(
    [query_embedding],
    dtype="float32"
)

print(query_embedding.shape)

# Search

distances, indices = index.search(
    query_embedding,
    3
)

print(distances)
print(indices)

for idx in indices[0]:
    print(
        "index : ",
        embeddings_data[idx]["id"]
    )
    
for idx in indices[0]:
    print(
        embeddings_data[idx]["text"]
    )