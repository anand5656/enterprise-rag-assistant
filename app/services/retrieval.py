from app.services.embeddings import (
    embedding_model
)

from app.vectorstore.faiss_store import (

    search_index,

    document_store,

    metadata_store
)


def retrieve_chunks(
    query,
    top_k=3
):

    if len(document_store) == 0:

        return []

    query_embedding = embedding_model.encode(
        [query]
    )

    indices = search_index(
        query_embedding,
        top_k
    )

    retrieved = []

    for idx in indices:

        if (
            idx >= 0 and
            idx < len(document_store)
        ):

            retrieved.append({

                "text":
                    document_store[idx],

                "source":
                    metadata_store[idx]
            })

    return retrieved