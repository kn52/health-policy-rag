
from pydantic import BaseModel, Field, EmailStr


class DoctorCreate(BaseModel):
    doctor_id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    specialization: str
    phone: str
    email: EmailStr | None = None


class DoctorUpdate(BaseModel):
    name: str = Field(..., min_length=1)
    specialization: str
    phone: str
    email: EmailStr | None = None
