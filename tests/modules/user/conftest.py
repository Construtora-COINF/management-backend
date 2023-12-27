from datetime import datetime
from uuid import uuid4

import pytest
from faker import Factory
from fastapi import status

faker = Factory.create("pt_BR")


@pytest.fixture()
def user_fake_dict():
    return {
        "id": faker.random_int(min=1, max=9999),
        "name": faker.name(),
        "uuid": uuid4().hex,
        "is_active": True,
        "email": faker.email(),
        "password": faker.password(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }


@pytest.fixture()
def user_post_fake_dict():
    return {
        "name": faker.name(),
        "uuid": uuid4().hex,
        "email": faker.email(),
        "password": faker.password(),
        "is_active": True,
    }


@pytest.fixture()
def user_put_fake_dict():
    return {
        "name": faker.name(),
        "password": faker.password(),
        "is_active": False,
    }


@pytest.fixture()
def user_login_fake_dict():
    return {
        "email": faker.email(),
        "password": faker.password(),
    }


@pytest.fixture()
def registered_user_db(test_app_with_db, access_token, user_post_fake_dict):
    response = test_app_with_db.post(
        "/users/", json=user_post_fake_dict, headers=access_token
    )
    assert response.status_code == status.HTTP_201_CREATED
    return response.json()
