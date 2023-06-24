from fastapi_utils.cbv import cbv
from loguru import logger

from app.schemas.entrypoints import api as api_schemas
from fastapi import APIRouter, Path

router = APIRouter()


@cbv(router)
class Example:
    @router.get("/example/{num}", response_model=api_schemas.ExampleOutSchemas)
    def get_example(
        self,
        num: str = Path(example="get example"),
    ):
        logger.info(f"/example/{num}")
        logger.success(f"/example/{num}")
        return api_schemas.ExampleOutSchemas(message="get example")
