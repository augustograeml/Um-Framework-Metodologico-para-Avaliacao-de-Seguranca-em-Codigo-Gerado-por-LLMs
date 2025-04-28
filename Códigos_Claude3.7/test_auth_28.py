import pytest
from app.auth.routes import login, register
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    from app.main import app
    return TestClient(app)

def test_register(client):
    response = client.post("/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"

def test_login(client):
    client.post("/register", json={"username": "testuser", "password": "testpass"})
    response = client.post("/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_invalid_user(client):
    response = client.post("/login", json={"username": "invaliduser", "password": "wrongpass"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"