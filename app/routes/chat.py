from fastapi import APIRouter
from pydantic import BaseModel

from app.services.rag import chat

router = APIRouter()

class ChatRequest(BaseModel):

    sessionId: str
    message: str

@router.post("/chat")
async def chat_endpoint(
    request: ChatRequest
):

    response = chat(
        request.message
    )

    return response