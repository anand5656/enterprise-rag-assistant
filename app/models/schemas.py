from pydantic import BaseModel


class ChatRequest(BaseModel):
    sessionId: str
    message: str


class ChatResponse(BaseModel):
    reply: str
    tokensUsed: int
    retrievedChunks: int