
from fastapi import APIRouter, HTTPException

from app.api.healthcare.healthcare_store import HealthcareStore
from app.api.healthcare.prescription_models import (
    PrescriptionCreate,
    PrescriptionUpdate,
)

router = APIRouter(prefix="/api/prescriptions", tags=["Prescriptions"])
store = HealthcareStore("health_prescriptions")


@router.get("/")
def get_prescriptions():
    return store.get_all()


@router.get("/{prescription_id}")
def get_prescription(prescription_id: str):
    prescription = store.get(prescription_id)
    if prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return prescription


@router.post("/", status_code=201)
def create_prescription(payload: PrescriptionCreate):
    try:
        return store.create(
            payload.prescription_id,
            payload.model_dump(exclude={"prescription_id"}),
        )
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))


@router.put("/{prescription_id}")
def update_prescription(
    prescription_id: str,
    payload: PrescriptionUpdate,
):
    prescription = store.update(prescription_id, payload.model_dump())
    if prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return prescription


@router.delete("/{prescription_id}")
def delete_prescription(prescription_id: str):
    if not store.delete(prescription_id):
        raise HTTPException(status_code=404, detail="Prescription not found")
    return {"message": "Prescription deleted successfully"}
