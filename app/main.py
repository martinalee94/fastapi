import logging

from app.entrypoints.router import api
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="FastAPI mock architecture")
app.include_router(api)
