from fastapi import APIRouter
from pydantic import BaseModel

from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.pipeline import ask_question


router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.post("/ask")
def ask(request: QuestionRequest):

    result = ask_question(request.question)

    return {
        "question": request.question,
        "answer": result["answer"],
        "sources": result["sources"]
    }