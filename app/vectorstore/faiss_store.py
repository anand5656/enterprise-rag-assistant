import faiss
import numpy as np

from app.services.embeddings import (
    embed_documents
)


dimension = 1000

search_index = faiss.IndexFlatL2(
    dimension
)

metadata_store = []


def add_to_index(
    chunks,
    sources
):

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


    global search_index

    if search_index.ntotal == 0:

        dimension = embeddings.shape[1]

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