from tests.conf_test_db import client
from fastapi import status
from app.Users import models
from faker import Faker
from app.auth.services import create_access_token


def test_correct_get_user(dummy_user: models.User):
    response = client.get(f'/users/{dummy_user.id}')
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert dummy_user.id == data['id']
    assert dummy_user.email == data['email']


def test_incorrect_get_user():
    wrong_user_id = 10000
    response = client.get(f'/users/{wrong_user_id}')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': f'User with id {wrong_user_id} does not exist!'}


def test_empty_get_all_users():
    response = client.get('/users/all')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


def test_get_all_users(dummy_user: models.User):
    response = client.get('/users/all')
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 1
    assert data[0]['email'] == dummy_user.email


def test_delete_user(dummy_user: models.User):
    token = create_access_token({'sub': dummy_user.email})
    response = client.delete(f'/users/{dummy_user.id}', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == status.HTTP_204_NO_CONTENT

    get_user_response = client.get(f'/users/{dummy_user.id}')
    assert get_user_response.status_code == status.HTTP_404_NOT_FOUND
    assert get_user_response.json() == {'detail': f'User with id {dummy_user.id} does not exist!'}


def test_create_user(faker: Faker):
    user_data = {'name': faker.name(), 'email': faker.email(), 'password': faker.password()}
    response = client.post('/users/', json=user_data)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data['email'] == user_data['email']
    assert 'id' in data
    user_id = data['id']

    response = client.get(f'/users/{user_id}')
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data['email'] == user_data['email']
    assert data['id'] == user_id

    token = create_access_token({'sub': user_data['email']})
    client.delete(f'/users/{user_id}', headers={'Authorization': f'Bearer {token}'})


def test_bad_create_user(dummy_user: models.User):
    response = client.post('/users/', json={'name': dummy_user.name,
                                            'email': dummy_user.email,
                                            'password': dummy_user.password})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {'detail': 'This email is already registered!'}
