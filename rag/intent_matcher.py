# rag/intent_matcher.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

INTENTS = {
    "most_expensive": [
        "most expensive product",
        "highest price product",
        "priciest item",
        "costliest product",
        "which product costs the most"
    ],

    "cheapest": [
        "cheapest product",
        "lowest price product",
        "least expensive item",
        "budget product",
        "which product costs the least"
    ],

    "highest_rated": [
        "highest rated product",
        "best rated product",
        "top rated item",
        "most stars",
        "best review score"
    ],

    "lowest_rated": [
        "lowest rated product",
        "worst rated product",
        "least stars",
        "worst review score"
    ],

    "most_reviewed": [
        "most reviewed product",
        "highest number of reviews",
        "most customer reviews",
        "most popular product"
    ]
}

INTENT_EMBEDDINGS = {}

for intent, examples in INTENTS.items():

    INTENT_EMBEDDINGS[intent] = []

    for example in examples:

        embedding = model.encode(
            example
        )

        INTENT_EMBEDDINGS[intent].append(
            embedding
        )

def detect_intent(user_question):

    question_embedding = model.encode(
        user_question
    )

    best_intent = None
    best_score = 0

    for intent, embeddings in INTENT_EMBEDDINGS.items():

        for example_embedding in embeddings:

            score = cosine_similarity(
                [question_embedding],
                [example_embedding]
            )[0][0]

            if score > best_score:
                best_score = score
                best_intent = intent

    print(
        f"Intent: {best_intent} | Score: {best_score:.3f}"
    )

    if best_score >= 0.70:
        return best_intent, best_score

    return None, best_score