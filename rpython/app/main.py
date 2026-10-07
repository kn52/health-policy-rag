from fastapi import FastAPI

from .api.user.user_routes import router as user_router

app = FastAPI(
    title="RAG Service API",
    description="CRUD API using JSON file storage",
    version="1.0.0"
)

app.include_router(user_router, prefix="/api");