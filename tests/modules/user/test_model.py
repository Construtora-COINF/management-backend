from datetime import datetime

from tortoise import Model

from app.abstracts.database.base_model import BaseModel
from app.modules.user.model import User


def test_user_model_should_return_valid_instance_when_valid_data_is_passed(
    user_fake_dict,
):
    model = User(**user_fake_dict)
    assert isinstance(model, Model)
    assert isinstance(model, BaseModel)

    assert isinstance(model.id, int)
    assert isinstance(model.uuid, str)
    assert isinstance(model.created_at, datetime)
    assert isinstance(model.updated_at, datetime)


def test_user_model_should_return_valid_fields_when_valid_data_is_passed(
    user_fake_dict,
):
    user = User(**user_fake_dict)

    assert isinstance(user.name, str)
    assert isinstance(user.email, str)
    assert isinstance(user.password, str)
    assert isinstance(user.is_active, bool)
