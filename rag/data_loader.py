import json
import faiss

from sentence_transformers import (
    SentenceTransformer
)

from langchain_ollama import (
    OllamaLLM
)

from langchain_core.output_parsers import (
    StrOutputParser
)

from prompts_langchain import (
    prompt_template
)


def load_embeddings():

    with open(
        "data/processed/embeddings.json",
        "r",
        encoding="utf-8"
    ) as f:

        embeddings_data = json.load(f)

    print(
        f"Embeddings Loaded: "
        f"{len(embeddings_data)}"
    )

    return embeddings_data


def load_faiss_index():

    index = faiss.read_index(
        "data/processed/faiss_index.bin"
    )

    print(
        f"Vectors in Index: "
        f"{index.ntotal}"
    )

    return index


def load_embedding_model():

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    print(
        "Embedding Model Loaded"
    )

    return model


def load_llm_chain():

    llm = OllamaLLM(
        model="llama3.2:3b",
        num_ctx=2048
    )

    parser = StrOutputParser()

    chain = (
        prompt_template
        | llm
        | parser
    )

    print(
        "LLM Chain Loaded"
    )

    return chain