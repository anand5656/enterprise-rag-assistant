from app.services.embeddings import (
    embed_query
)

from app.vectorstore.faiss_store import (
    search_documents
)


def retrieve_chunks(
    query,
    top_k=3
):

    query_embedding = embed_query(
        query
    )

    results = search_documents(
        query_embedding,
        top_k
    )

    return results