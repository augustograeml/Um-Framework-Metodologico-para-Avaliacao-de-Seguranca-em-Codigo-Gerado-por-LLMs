import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_download_content_success():
    response = client.post("/download", json={"url": "https://example.com/sample.txt"})
    assert response.status_code == 200
    assert response.json() == {"message": "File downloaded successfully."}

def test_download_content_invalid_url():
    response = client.post("/download", json={"url": "invalid-url"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid URL provided."}

def test_download_content_missing_url():
    response = client.post("/download", json={})
    assert response.status_code == 422
    assert response.json() == {"detail": [{"loc": ["body", "url"], "msg": "field required", "type": "value_error.missing"}]}