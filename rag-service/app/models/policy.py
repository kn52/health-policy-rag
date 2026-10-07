from pydantic import BaseModel


class PolicyCreate(BaseModel):
    policy_name: str
    content: str


class PolicyUpdate(BaseModel):
    policy_name: str
    content: str


class Policy(BaseModel):
    id: int
    policy_name: str
    content: str