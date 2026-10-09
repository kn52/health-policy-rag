
from fastapi import APIRouter

from app.api.healthcare.healthcare_store import HealthcareStore

router = APIRouter(prefix="/api/dashboard", tags=["Dashboard"])


@router.get("/")
def get_dashboard():
    patients = HealthcareStore("health_patients").get_all()
    doctors = HealthcareStore("health_doctors").get_all()
    appointments = HealthcareStore("health_appointments").get_all()
    prescriptions = HealthcareStore("health_prescriptions").get_all()
    bills = HealthcareStore("health_billing").get_all()

    return {
        "total_patients": len(patients),
        "total_doctors": len(doctors),
        "total_appointments": len(appointments),
        "total_prescriptions": len(prescriptions),
        "total_bills": len(bills),
        "pending_bills": sum(
            1 for bill in bills
            if bill.get("status", "").lower() == "pending"
        ),
    }
