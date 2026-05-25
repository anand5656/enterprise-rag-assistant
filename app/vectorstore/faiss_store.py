import faiss
import numpy as np

from app.services.embeddings import (
    embedding_model
)


document_store = []

metadata_store = []


dimension = 384


index = faiss.IndexFlatL2(
    dimension
)


def add_documents(
    text_chunks,
    filename
):

    global document_store
    global metadata_store

    embeddings = embedding_model.encode(
        text_chunks
    )

    index.add(
        np.array(embeddings)
    )

    for i, chunk in enumerate(text_chunks):

        document_store.append(chunk)

        metadata_store.append({

            "source": filename,

            "chunk": i + 1
        })


def search_index(
    query_embedding,
    top_k=3
):

    distances, indices = index.search(
        np.array(query_embedding),
        top_k
    )

    return indices[0]