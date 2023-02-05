import pytest
from .conf_test_db import override_get_db
from app.Users import crud as user_crud, schemas as user_schemas, models as user_models
from app.auth import services
from faker import Faker


@pytest.fixture
def dummy_user(faker: Faker) -> user_models.User:
    data = {'name': faker.name(),
            'email': faker.email(),
            'password': faker.password()}
    database = next(override_get_db())
    created_user_data = user_crud.create_user_in_db(user_schemas.User(**data), database)
    yield created_user_data

    user_crud.delete_user_in_db(created_user_data.id, database)


@pytest.fixture
def auth_token(dummy_user: user_models.User) -> str:
    token = services.create_access_token({'sub': dummy_user.email})
    return token
