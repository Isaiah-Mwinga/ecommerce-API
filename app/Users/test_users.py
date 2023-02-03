import pytest
from fastapi import status
from fastapi.testclient import TestClient

from main import app

def test_create_user(client: TestClient):
    client = TestClient(app)
    # Test creating a user with an existing email
    user = {'email': 'existing_email@example.com', 'password': 'password123'}
    response = client.post('/users/', json=user)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {'detail': 'This email is already registered!'}

    # Test creating a user with a unique email
    user = {'email': 'new_email@example.com', 'password': 'password123'}
    response = client.post('/users/', json=user)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {'email': 'new_email@example.com', 'id': 1}

    # Test creating a user with missing required fields
    user = {'password': 'password123'}
    response = client.post('/users/', json=user)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {'detail': 'Input body requires an "email" field.'}