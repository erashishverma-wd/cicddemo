import pytest
from src.app import app


@pytest.fixture
def client():
    return app.test_client()

def test_hello(client):
    response = client.get('/api/hello/testuser')
    assert response.status_code == 200
    assert response.json == {'message': 'Hello, testuser!'}

def test_get_sum(client):
    response = client.get('/api/getSum/3/5')
    assert response.status_code == 200
    assert response.json == {'sum': 8}

    response = client.get('/api/getSum/3/a')
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid input. Please provide two numbers.'}