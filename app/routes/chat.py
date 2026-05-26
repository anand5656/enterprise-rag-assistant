from fastapi import APIRouter
from pydantic import BaseModel

from app.services.rag import chat

router = APIRouter()


class ChatRequest(BaseModel):
    query: str


@router.post("/chat")
async def chat_endpoint(data: ChatRequest):

    try:

        response = chat(data.query)

        return {
            "answer": response
        }

    except Exception as e:

        return {
            "answer": f"Backend Error: {str(e)}"
        }