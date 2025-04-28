import pytest
from app.routes.commands import execute_command

def test_execute_command_success(client):
    response = client.post('/execute', json={'command': 'echo Hello, World!'})
    assert response.status_code == 200
    assert response.json['output'] == 'Hello, World!\n'

def test_execute_command_failure(client):
    response = client.post('/execute', json={'command': 'invalid_command'})
    assert response.status_code == 400
    assert 'error' in response.json

def test_execute_command_empty(client):
    response = client.post('/execute', json={'command': ''})
    assert response.status_code == 400
    assert 'error' in response.json

def test_execute_command_injection(client):
    response = client.post('/execute', json={'command': 'ls; rm -rf /'})
    assert response.status_code == 400
    assert 'error' in response.json