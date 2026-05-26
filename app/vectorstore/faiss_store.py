import faiss
import numpy as np

from app.services.embeddings import embed_texts

documents = []

index = None


def add_documents(chunks, source):

    global index

    embeddings = embed_texts(chunks)

    embeddings = np.array(
        embeddings
    ).astype("float32")

    if index is None:

        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(
            dimension
        )

    index.add(embeddings)

    for chunk in chunks:

        documents.append({
            "text": chunk,
            "source": source
        })


def search(query, top_k=3):

    global index

    if index is None:

        return []

    query_embedding = embed_texts(
        [query]
    )

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(documents):

            results.append(
                documents[idx]
            )

    return results