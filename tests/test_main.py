import pytest
import json
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    """Тест главной страницы"""
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert data['message'] == 'Hello from CI/CD App!'

def test_health_endpoint(client):
    """Тест health check"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_users_endpoint(client):
    """Тест API пользователей"""
    response = client.get('/api/users')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    assert data['name'] == 'John Doe'
