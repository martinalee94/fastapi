import pytest
from fastapi.testclient import TestClient
from app.main import app
from typing import Generator


@pytest.fixture(scope="function")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
