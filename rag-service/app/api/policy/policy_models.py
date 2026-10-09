from pydantic import BaseModel, Field


class PolicyCreate(BaseModel):
    source: str = Field(min_length=1, max_length=200)
    content: str = Field(min_length=1)


class PolicyUpdate(BaseModel):
    content: str = Field(min_length=1)