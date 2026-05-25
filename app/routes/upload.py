import os
from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from app.services.file_parser import (
    extract_text_from_pdf,
    extract_text_from_docx,
    extract_text_from_txt
)

from app.services.chunking import (
    chunk_text
)

from app.vectorstore.faiss_store import (
    add_documents
)


router = APIRouter()


UPLOAD_DIR = "uploads"


os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    try:

        file_path = os.path.join(
            UPLOAD_DIR,
            file.filename
        )

        with open(file_path, "wb") as f:

            f.write(await file.read())

        text = ""

        if file.filename.endswith(".pdf"):

            text = extract_text_from_pdf(
                file_path
            )

        elif file.filename.endswith(".docx"):

            text = extract_text_from_docx(
                file_path
            )

        elif file.filename.endswith(".txt"):

            text = extract_text_from_txt(
                file_path
            )

        else:

            return {
                "message":
                "Unsupported file type"
            }

        chunks = chunk_text(text)

        add_documents(
            chunks,
            file.filename
        )

        return {

            "message":
                f"{file.filename} uploaded successfully",

            "chunks":
                len(chunks)
        }

    except Exception as e:

        return {

            "message":
                f"Upload failed: {str(e)}"
        }