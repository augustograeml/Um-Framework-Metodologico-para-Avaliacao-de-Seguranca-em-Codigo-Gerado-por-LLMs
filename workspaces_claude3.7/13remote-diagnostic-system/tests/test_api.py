import pytest
from app.api.routes import register_routes
from fastapi import FastAPI

@pytest.fixture
def client():
    app = FastAPI()
    register_routes(app)
    with TestClient(app) as client:
        yield client

def test_execute_command(client):
    response = client.post("/api/execute", json={"command": "echo Hello World"})
    assert response.status_code == 200
    assert response.json() == {"output": "Hello World\n", "error": ""}

def test_execute_invalid_command(client):
    response = client.post("/api/execute", json={"command": "invalid_command"})
    assert response.status_code == 400
    assert "error" in response.json()