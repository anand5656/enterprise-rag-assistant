import numpy as np

from app.services.embeddings import (
    embed_query
)

from app.vectorstore.faiss_store import (
    search_index,
    metadata_store
)


def retrieve_chunks(
    query,
    top_k=3
):

    if search_index is None:

        return []

    if len(metadata_store) == 0:

        return []

    query_embedding = embed_query(
        query
    )

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    distances, indices = search_index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(metadata_store):

            results.append({

                "text": metadata_store[idx]["text"],

                "source": metadata_store[idx]
            })

    return results