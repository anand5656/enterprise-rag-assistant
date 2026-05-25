from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.upload import router as upload_router

from app.routes.chat import router as chat_router


app = FastAPI(title="RAG GenAI Assistant")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


app.include_router(chat_router, prefix="/api")
app.include_router(
    upload_router,
    prefix="/api"
)