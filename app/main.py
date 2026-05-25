from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat import router as chat_router
from app.routes.upload import router as upload_router


app = FastAPI(
    title="Enterprise GenAI RAG Assistant"
)


# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routes

app.include_router(
    chat_router,
    prefix="/api"
)

app.include_router(
    upload_router,
    prefix="/api"
)


@app.get("/")
def root():

    return {
        "message": "Enterprise GenAI RAG Assistant Running"
    }