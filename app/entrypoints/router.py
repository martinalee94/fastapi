from app.entrypoints.api.api import router as api_router
from fastapi import APIRouter

api = APIRouter()

api.include_router(api_router, prefix="/external")
