import faiss
import numpy as np

from app.services.embeddings import (
    embed_texts
)

documents = []

dimension = 384

index = faiss.IndexFlatL2(
    dimension
)

def add_documents(chunks, filename):

    global documents

    embeddings = embed_texts(
        chunks
    )

    vectors = np.array(
        embeddings
    ).astype("float32")

    index.add(vectors)

    for chunk in chunks:

        documents.append({

            "text": chunk,
            "source": filename
        })

def search(query, top_k=3):

    if len(documents) == 0:

        return []

    query_embedding = embed_texts(
        [query]
    )

    query_vector = np.array(
        query_embedding
    ).astype("float32")

    distances, indices = index.search(
        query_vector,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(documents):

            results.append(
                documents[idx]
            )

    return results