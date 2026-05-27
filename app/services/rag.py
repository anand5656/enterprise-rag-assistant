from app.services.retrieval import (
    retrieve_chunks
)

def chat(message):

    results = retrieve_chunks(
        message
    )

    if not results:

        return {
            "reply":
                "No documents uploaded yet.",
            "sources": []
        }

    context = "\n".join(

        [r["text"] for r in results]
    )

    return {

        "reply":
            f"Relevant information:\n\n{context[:1000]}",

        "sources":

            [r["source"] for r in results]
    }