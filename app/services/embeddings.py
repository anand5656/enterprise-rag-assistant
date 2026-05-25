from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()


def embed_documents(texts):

    vectors = vectorizer.fit_transform(texts)

    return vectors.toarray()


def embed_query(query):

    vector = vectorizer.transform([query])

    return vector.toarray()