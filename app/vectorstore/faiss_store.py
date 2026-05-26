import faiss
import numpy as np

from app.services.embeddings import (
    embed_documents
)

search_index = None

metadata_store = []


def add_documents(
    chunks,
    sources
):

    global search_index

    texts = [
        chunk
        for chunk in chunks
    ]

    embeddings = embed_documents(
        texts
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


    for chunk, source in zip(
        chunks,
        sources
    ):

        metadata_store.append({

            "text": chunk,

            "source": source["source"],

            "chunk": source["chunk"]
        })