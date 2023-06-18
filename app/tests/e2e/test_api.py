import pytest
from fastapi.testclient import TestClient
from app.main import app


def test_get_example(client: TestClient):
    URL = app.url_path_for("get_example")
    res = client.get(url=URL)
    assert res
