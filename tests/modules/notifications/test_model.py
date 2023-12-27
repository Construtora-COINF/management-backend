from datetime import datetime

from tortoise import Model

from app.abstracts.database.base_model import BaseModel
from app.modules.notifications.model import Notification


def test_notification_model_should_return_valid_instance_when_valid_data_is_passed(
    notification_fake_dict,
):
    model = Notification(**notification_fake_dict)
    assert isinstance(model, Model)
    assert isinstance(model, BaseModel)

    assert isinstance(model.id, int)
    assert isinstance(model.uuid, str)
    assert isinstance(model.created_at, datetime)
    assert isinstance(model.updated_at, datetime)


def test_notification_model_should_return_valid_fields_when_valid_data_is_passed(
    notification_fake_dict,
):
    model = Notification(**notification_fake_dict)

    assert isinstance(model.type, str)
    assert isinstance(model.ip_address, str)
    assert isinstance(model.payload, dict)
