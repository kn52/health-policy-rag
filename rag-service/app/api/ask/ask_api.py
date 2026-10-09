from pathlib import Path
from fastapi import HTTPException

from .ask_models import (
    AskRequest, 
    AskResponse,
    IngestRequest
)
from app.services.rag_service import RAGService

rag_service = RAGService()

POLICY_DIR = (
    Path(__file__).resolve().parents[2]
    / "documents"
    / "policies"
)

def health_check():
    return {"status": "healthy"}


def list_documents():
    POLICY_DIR.mkdir(parents=True, exist_ok=True)

    files = [
        path.name
        for path in POLICY_DIR.glob("*.txt")
        if path.is_file()
    ]

    return {"documents": files}


def ingest_document(request: IngestRequest):
    filename = Path(request.filename).name

    if filename != request.filename or not filename.endswith(".txt"):
        raise HTTPException(
            status_code=400,
            detail="Provide a valid .txt filename.",
        )

    file_path = POLICY_DIR / filename

    if not file_path.is_file():
        raise HTTPException(
            status_code=404,
            detail="Policy document not found.",
        )

    try:
        count = rag_service.ingest_document(str(file_path))
        return {
            "message": "Document ingested successfully",
            "filename": filename,
            "chunks": count,
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        ) from exc


def ask_question(request: AskRequest):
    try:
        results = rag_service.retrieve(request.question, limit=3)

        return {
            "question": request.question,
            "results": results,
            "count": len(results),
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        ) from exc
