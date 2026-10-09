
from fastapi import APIRouter, HTTPException

from app.api.healthcare.healthcare_store import HealthcareStore
from app.api.healthcare.doctor_models import DoctorCreate, DoctorUpdate

router = APIRouter(prefix="/api/doctors", tags=["Doctors"])
store = HealthcareStore("health_doctors")


@router.get("/")
def get_doctors():
    return store.get_all()


@router.get("/{doctor_id}")
def get_doctor(doctor_id: str):
    doctor = store.get(doctor_id)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


@router.post("/", status_code=201)
def create_doctor(payload: DoctorCreate):
    try:
        return store.create(
            payload.doctor_id,
            payload.model_dump(exclude={"doctor_id"}),
        )
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))


@router.put("/{doctor_id}")
def update_doctor(doctor_id: str, payload: DoctorUpdate):
    doctor = store.update(doctor_id, payload.model_dump())
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: str):
    if not store.delete(doctor_id):
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {"message": "Doctor deleted successfully"}
