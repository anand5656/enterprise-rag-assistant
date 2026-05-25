from fastapi import APIRouter, HTTPException

from app.models.schemas import ChatRequest
from app.services.rag import chat


router = APIRouter()


@router.post("/chat")
def chat_endpoint(request: ChatRequest):
    if not request.message:
        raise HTTPException(
            status_code=400,
            detail="Message field is required"
        )

    return chat(
        request.sessionId,
        request.message
    )