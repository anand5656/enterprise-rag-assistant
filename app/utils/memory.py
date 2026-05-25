conversation_memory = {}


def get_conversation_history(session_id):

    return conversation_memory.get(
        session_id,
        []
    )


def update_memory(
    session_id,
    user_message,
    assistant_response
):

    if session_id not in conversation_memory:

        conversation_memory[session_id] = []

    conversation_memory[session_id].append(
        {
            "user": user_message,
            "assistant": assistant_response
        }
    )