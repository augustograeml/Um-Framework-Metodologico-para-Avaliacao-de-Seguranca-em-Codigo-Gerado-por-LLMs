import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/?param1=value1&param2=value2')
    assert response.status_code == 200
    assert b'value1' in response.data
    assert b'value2' in response.data

def test_index_route_no_params(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Default content' in response.data  # Assuming default content is displayed when no params are provided

def test_invalid_route(client):
    response = client.get('/invalid-route')
    assert response.status_code == 404