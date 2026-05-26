from app.services.embeddings import embed_query
from app.vectorstore.faiss_store import search_documents

from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def chat(query: str):

    query_embedding = embed_query(query)

    retrieved_chunks = search_documents(
        query_embedding
    )

    if not retrieved_chunks:

        return "No relevant information found in uploaded documents."

    context = "\n".join(
        retrieved_chunks
    )

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}
"""

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = completion.choices[0].message.content

    return answer