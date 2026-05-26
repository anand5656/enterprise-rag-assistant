import faiss
import numpy as np
import os
import pickle

from app.services.embeddings import (
    embed_documents
)

INDEX_FILE = "faiss.index"

METADATA_FILE = "metadata.pkl"


if os.path.exists(INDEX_FILE):

    search_index = faiss.read_index(
        INDEX_FILE
    )

else:

    search_index = None


if os.path.exists(METADATA_FILE):

    with open(METADATA_FILE, "rb") as f:

        metadata_store = pickle.load(f)

else:

    metadata_store = []


def save_index():

    global search_index

    if search_index is not None:

        faiss.write_index(
            search_index,
            INDEX_FILE
        )

    with open(METADATA_FILE, "wb") as f:

        pickle.dump(
            metadata_store,
            f
        )


def add_documents(
    chunks,
    source
):

    global search_index

    embeddings = embed_documents(
        chunks
    )

    embeddings = np.array(
        embeddings
    ).astype("float32")

    dimension = embeddings.shape[1]

    if search_index is None:

        search_index = faiss.IndexFlatL2(
            dimension
        )

    search_index.add(
        embeddings
    )

    for i, chunk in enumerate(chunks):

        metadata_store.append({

            "text": chunk,

            "source": source,

            "chunk": i + 1
        })

    save_index()


def search_documents(
    query_embedding,
    top_k=3
):

    global search_index

    if search_index is None:

        return []

    query_embedding = np.array(
        [query_embedding]
    ).astype("float32")

    distances, indices = search_index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(metadata_store):

            results.append(
                metadata_store[idx]
            )

    return results