
from pydantic import BaseModel, Field


class AppointmentCreate(BaseModel):
    appointment_id: str = Field(..., min_length=1)
    patient_id: str
    doctor_id: str
    appointment_date: str
    reason: str
    status: str = "Scheduled"


class AppointmentUpdate(BaseModel):
    patient_id: str
    doctor_id: str
    appointment_date: str
    reason: str
    status: str
