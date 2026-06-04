import json

from sentence_transformers import SentenceTransformer

with open(
    "data/processed/documents.json",
    "r",
    encoding="utf-8"
) as f:
    documents = json.load(f)

print(
    f"Documents Loaded: {len(documents)}"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Model Loaded")

embeddings = []

for document in documents:

    embedding = model.encode(
        document["text"]
    )
    
    embeddings.append({
        "id": document["id"],
        "text": document["text"],
        "embedding": embedding.tolist()
    })

print(type(embedding))
print(len(embedding))

with open(
    "data/processed/embeddings.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        embeddings,
        f,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Embeddings Saved: {len(embeddings)}"
)