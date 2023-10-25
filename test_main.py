# test with pytest for main.py

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# test root
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

