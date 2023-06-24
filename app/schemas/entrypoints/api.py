from pydantic import BaseModel, Field


class ExampleOutSchemas(BaseModel):
    message: str = Field("default")
