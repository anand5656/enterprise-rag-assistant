from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    sessionId: str
    message: str

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):

    return {
        "reply": f"You said: {request.message}",
        "sources": []
    }