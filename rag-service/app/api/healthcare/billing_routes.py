
from fastapi import APIRouter, HTTPException

from app.api.healthcare.healthcare_store import HealthcareStore
from app.api.healthcare.billing_models import BillingCreate, BillingUpdate

router = APIRouter(prefix="/api/billing", tags=["Billing"])
store = HealthcareStore("health_billing")


@router.get("/")
def get_bills():
    return store.get_all()


@router.get("/{bill_id}")
def get_bill(bill_id: str):
    bill = store.get(bill_id)
    if bill is None:
        raise HTTPException(status_code=404, detail="Bill not found")
    return bill


@router.post("/", status_code=201)
def create_bill(payload: BillingCreate):
    try:
        return store.create(
            payload.bill_id,
            payload.model_dump(exclude={"bill_id"}),
        )
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))


@router.put("/{bill_id}")
def update_bill(bill_id: str, payload: BillingUpdate):
    bill = store.update(bill_id, payload.model_dump())
    if bill is None:
        raise HTTPException(status_code=404, detail="Bill not found")
    return bill


@router.delete("/{bill_id}")
def delete_bill(bill_id: str):
    if not store.delete(bill_id):
        raise HTTPException(status_code=404, detail="Bill not found")
    return {"message": "Bill deleted successfully"}
