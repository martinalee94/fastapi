from fastapi import FastAPI
import logging
from app.entrypoints.router import api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="FastAPI mock architecture")
app.include_router(api)
