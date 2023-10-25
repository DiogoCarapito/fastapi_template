# lest build a test main.py with pytest

import pytest
from fastapi.testclient import TestClient
from main import app


# Web Application Testing
@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


# Test the root endpoint
def test_main_read(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


# Test the items endpoint
def test_read_item(client):
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}


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
