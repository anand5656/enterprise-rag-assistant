import numpy as np

from app.services.embeddings import (
    embed_text
)

from app.vectorstore.faiss_store import (
    search_index,
    metadata_store
)


def retrieve_chunks(
    query,
    top_k=3
):

    query_embedding = embed_text(
        [query]
    )

    distances, indices = search_index.search(
        np.array(query_embedding).astype("float32"),
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