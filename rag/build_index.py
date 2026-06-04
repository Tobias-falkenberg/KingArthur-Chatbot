import json
import numpy as np
import faiss

# Load embeddings

with open(
    "data/processed/embeddings.json",
    "r",
    encoding="utf-8"
) as f:

    embeddings_data = json.load(f)

print(
    f"Embeddings Loaded: {len(embeddings_data)}"
)

# Extract vectors

vectors = []

for item in embeddings_data:

    vectors.append(
        item["embedding"]
    )

# Convert to NumPy

vectors = np.array(
    vectors,
    dtype="float32"
)

print(type(vectors))
print(vectors.shape)

# Create FAISS index

dimension = vectors.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(vectors)

print(
    f"Vectors in Index: {index.ntotal}"
)

# Save index

faiss.write_index(
    index,
    "data/processed/faiss_index.bin"
)

print(
    "FAISS Index Saved!"
)