
from fastapi import APIRouter, HTTPException

from app.api.healthcare.healthcare_store import HealthcareStore
from app.api.healthcare.appointment_models import (
    AppointmentCreate,
    AppointmentUpdate,
)

router = APIRouter(prefix="/api/appointments", tags=["Appointments"])
store = HealthcareStore("health_appointments")


@router.get("/")
def get_appointments():
    return store.get_all()


@router.get("/{appointment_id}")
def get_appointment(appointment_id: str):
    appointment = store.get(appointment_id)
    if appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment


@router.post("/", status_code=201)
def create_appointment(payload: AppointmentCreate):
    try:
        return store.create(
            payload.appointment_id,
            payload.model_dump(exclude={"appointment_id"}),
        )
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))


@router.put("/{appointment_id}")
def update_appointment(
    appointment_id: str,
    payload: AppointmentUpdate,
):
    appointment = store.update(appointment_id, payload.model_dump())
    if appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment


@router.delete("/{appointment_id}")
def delete_appointment(appointment_id: str):
    if not store.delete(appointment_id):
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": "Appointment deleted successfully"}
