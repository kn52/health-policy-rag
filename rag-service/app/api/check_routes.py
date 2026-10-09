from fastapi import APIRouter

router = APIRouter(
    tags=["Default"],
)


@router.get("/")
def home():
    return {
        "message": "Healthcare RAG API is running"
    }


@router.get("/health")
def health_check():
    return {
        "status": "healthy"
    }