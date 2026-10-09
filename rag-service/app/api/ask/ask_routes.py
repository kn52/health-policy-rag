from fastapi import APIRouter
from .ask_models import (
    AskRequest,
    AskResponse,
    IngestRequest
)
from .ask_api import(
    health_check,
    list_documents,
    ingest_document,
    ask_question
)

router = APIRouter(
    prefix="/ask", 
    tags=["Rag"]
)

@router.get("/health")
def health_check_endpoint():
    return health_check()


@router.get("/documents")
def list_documents_endpoint():
    return list_documents()


@router.post("/documents/ingest")
def ingest_document_endpoint(request: IngestRequest):
    return ingest_document(request)


@router.post("/ask")
def ask_question_endpoint(request: AskRequest):
    return ask_question(request)