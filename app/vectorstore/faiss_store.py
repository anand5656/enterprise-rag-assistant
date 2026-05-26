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

    texts = chunks

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


    for i, chunk in enumerate(chunks):

        metadata_store.append({

            "text": chunk,

            "source": sources[i],

            "chunk": i + 1
        })