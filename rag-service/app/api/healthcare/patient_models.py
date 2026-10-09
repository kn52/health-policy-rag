
from pydantic import BaseModel, Field


class PatientCreate(BaseModel):
    patient_id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=0, le=130)
    gender: str
    phone: str
    email: str | None = None


class PatientUpdate(BaseModel):
    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=0, le=130)
    gender: str
    phone: str
    email: str | None = None
