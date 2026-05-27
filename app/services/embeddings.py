from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

documents = []

def embed_texts(texts):

    global documents
    global vectorizer

    documents.extend(texts)

    vectors = vectorizer.fit_transform(
        documents
    )

    return vectors.toarray()[-len(texts):]