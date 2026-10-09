
from pydantic import BaseModel, Field


class PrescriptionCreate(BaseModel):
    prescription_id: str = Field(..., min_length=1)
    patient_id: str
    doctor_id: str
    medication: str
    dosage: str
    instructions: str = ""


class PrescriptionUpdate(BaseModel):
    patient_id: str
    doctor_id: str
    medication: str
    dosage: str
    instructions: str = ""
