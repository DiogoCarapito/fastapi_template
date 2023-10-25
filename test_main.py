"""
import pytest
from fastapi.testclient import TestClient
from main import app


#### Web Application Testing
@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_main_read(client):
    response = client.get("/")
    assert response.status_code == 200
    # assert response.json() == {"Hello": "Hello world!"}

"""
