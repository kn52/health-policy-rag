
from fastapi import APIRouter, HTTPException

from app.api.healthcare.healthcare_store import HealthcareStore
from app.api.healthcare.patient_models import PatientCreate, PatientUpdate

router = APIRouter(prefix="/api/patients", tags=["Patients"])
store = HealthcareStore("health_patients")


@router.get("/")
def get_patients():
    return store.get_all()


@router.get("/{patient_id}")
def get_patient(patient_id: str):
    patient = store.get(patient_id)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@router.post("/", status_code=201)
def create_patient(payload: PatientCreate):
    try:
        return store.create(
            payload.patient_id,
            payload.model_dump(exclude={"patient_id"}),
        )
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))


@router.put("/{patient_id}")
def update_patient(patient_id: str, payload: PatientUpdate):
    patient = store.update(patient_id, payload.model_dump())
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@router.delete("/{patient_id}")
def delete_patient(patient_id: str):
    if not store.delete(patient_id):
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient deleted successfully"}
