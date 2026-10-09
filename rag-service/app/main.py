from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.check_routes import router as check_router
from app.api.ask.ask_routes import router as ask_router
from app.api.policy.policy_api import router as policy_api
from app.api.healthcare.patient_routes import router as patient_router
from app.api.healthcare.doctor_routes import router as doctor_router
from app.api.healthcare.appointment_routes import router as appointment_router
from app.api.healthcare.prescription_routes import router as prescription_router
from app.api.healthcare.billing_routes import router as billing_router
from app.api.healthcare.dashboard_routes import router as dashboard_router


app = FastAPI(
    title="Health Policy RAG API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(check_router, prefix="/api")
app.include_router(ask_router, prefix="/api")
app.include_router(policy_api)
app.include_router(patient_router)
app.include_router(doctor_router)
app.include_router(appointment_router)
app.include_router(prescription_router)
app.include_router(billing_router)
app.include_router(dashboard_router)