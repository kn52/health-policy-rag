
from pydantic import BaseModel, Field


class BillingCreate(BaseModel):
    bill_id: str = Field(..., min_length=1)
    patient_id: str
    amount: float = Field(..., ge=0)
    description: str
    status: str = "Pending"
    due_date: str | None = None


class BillingUpdate(BaseModel):
    patient_id: str
    amount: float = Field(..., ge=0)
    description: str
    status: str
    due_date: str | None = None
