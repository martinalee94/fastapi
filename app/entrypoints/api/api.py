from fastapi import APIRouter, Path
from loguru import logger
from app.schemas.entrypoints import api as api_schemas

router = APIRouter()


class Example:
    @router.get("/example/{num}", response_model=api_schemas.ExampleOutSchemas)
    def get_example(
        num: str = Path(example="get example"),
    ):
        logger.info(f"/example/{num}")
        logger.success(f"/example/{num}")
        return api_schemas.ExampleOutSchemas(message="get example")
