from fastapi import APIRouter
from app.utils.log_utils import detailed_logging

router = APIRouter()
LOGGING_PATH = "app.entrypoints.api.api.Example"


class Example:
    @router.get("/example")
    @detailed_logging(LOGGING_PATH)
    def get_example():
        return "example"
