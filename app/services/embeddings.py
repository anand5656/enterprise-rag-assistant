from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def embed_texts(texts):

    embeddings = model.encode(
        texts
    )

    return embeddings.tolist()


def embed_query(query):

    embedding = model.encode(
        query
    )

    return embedding.tolist()