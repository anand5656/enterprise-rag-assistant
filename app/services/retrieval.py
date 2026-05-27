from app.vectorstore.faiss_store import (
    search
)

def retrieve_chunks(query):

    results = search(query)

    return results