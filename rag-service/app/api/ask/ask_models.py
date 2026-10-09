from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="Question about a healthcare policy",
    )



class AskResponse(BaseModel):
    question: str
    answer: str
    sources: list[str] = []


class AskRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)


class IngestRequest(BaseModel):
    filename: str = Field(min_length=1, max_length=255)