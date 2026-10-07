from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    age: int
    id: int | None = None  # Optional ID field, will be assigned when creating a new user