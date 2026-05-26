import os
import pickle
import faiss
import numpy as np

INDEX_PATH = "faiss.index"
DOCS_PATH = "documents.pkl"

dimension = 384

index = faiss.IndexFlatL2(dimension)

documents = []


if os.path.exists(INDEX_PATH):
    index = faiss.read_index(INDEX_PATH)

if os.path.exists(DOCS_PATH):
    with open(DOCS_PATH, "rb") as f:
        documents = pickle.load(f)


def add_documents(chunks, filename):

    global documents

    from app.services.embeddings import embed_texts

    embeddings = embed_texts(chunks)

    embeddings = np.array(
        embeddings
    ).astype("float32")

    index.add(embeddings)

    for chunk in chunks:

        documents.append({
            "text": chunk,
            "source": filename
        })

    faiss.write_index(
        index,
        INDEX_PATH
    )

    with open(DOCS_PATH, "wb") as f:
        pickle.dump(
            documents,
            f
        )


def search_documents(query_embedding, top_k=3):

    if len(documents) == 0:
        return []

    query_embedding = np.array(
        [query_embedding]
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(documents):

            results.append(
                documents[idx]["text"]
            )

    return results