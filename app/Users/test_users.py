import pytest
from fastapi import Depends
from fastapi.testclient import TestClient
from app.Users.user import get_all_users, get_user, create_user 
from sqlalchemy.orm import Session
from app.database import  get_db

def test_get_all_users(client: TestClient, db: Session = Depends(get_db)):
    response = get_all_users()
    assert response.status_code == 200
    assert response.json() == []

def test_get_user(client: TestClient, db: Session = Depends(get_db)):
    response = get_user(1)
    assert response.status_code == 404
    assert response.json() == {'detail': 'User with id 1 does not exist!'}

def test_create_user(client: TestClient, db: Session = Depends(get_db)):
    response = create_user()
    assert response.status_code == 201
    assert response.json() == {'id': 1, 'email': '  ', 'name': '  ', 'password': '  '}
