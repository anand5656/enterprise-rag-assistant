from app.services.retrieval import retrieve_chunks

from app.prompts.prompt_template import build_prompt

from app.services.llm import generate_response

from app.utils.memory import (
    get_conversation_history,
    update_memory
)


def chat(session_id, message):

    # Retrieve relevant chunks
    retrieved_chunks = retrieve_chunks(message)

    # Build context
    context = "\n".join([
        chunk["text"]
        for chunk in retrieved_chunks
    ])

    # Get previous conversation
    history = get_conversation_history(session_id)

    # Build final prompt
    prompt = build_prompt(
        context=context,
        history=history,
        question=message
    )

    # Generate LLM response
    response = generate_response(prompt)

    # Save conversation memory
    update_memory(
        session_id,
        message,
        response
    )

    # Source tracking
    sources = []

    for chunk in retrieved_chunks:

        source = chunk["source"]

        sources.append(
            f"{source['source']} "
            f"(Chunk {source['chunk']})"
        )

    return {
        "reply": response,
        "sources": list(set(sources)),
        "retrievedChunks": len(retrieved_chunks),
        "tokensUsed": 0
    }