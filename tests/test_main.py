from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello world!"}


def test_items():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}
