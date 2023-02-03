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

def test_update_user(client: TestClient):
    # First, create a user
    user_data = {
        "email": "test@example.com",
        "password": "secret"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201
    user_id = response.json()["id"]

    # Then, update the user
    update_data = {
        "email": "updated@example.com",
        "password": "newsecret"
    }
    response = client.put(f"/users/{user_id}", json=update_data)
    assert response.status_code == 200

    # Finally, retrieve the updated user and check that the data is correct
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["email"] == "updated@example.com"
    assert response.json()["password"] == "newsecret"
