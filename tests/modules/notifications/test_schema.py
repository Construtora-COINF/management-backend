from datetime import datetime

import pytest
from fastapi_camelcase import CamelModel

from pydantic import BaseModel, ValidationError
from app.modules.notifications import schema
from app.modules.notifications.enum import NotificationTypesEnum


def test_get_notification_schema_with_valid_models(notification_fake_dict):
    notification_schema = schema.GetNotificationSchema(**notification_fake_dict)
    assert isinstance(notification_schema, schema.GetNotificationSchema)
    assert isinstance(notification_schema, CamelModel)
    assert isinstance(notification_schema, BaseModel)


def test_get_notification_schema_with_valid_fields_values(notification_fake_dict):
    notification_schema = schema.GetNotificationSchema(**notification_fake_dict)
    assert isinstance(notification_schema.id, int)
    assert isinstance(notification_schema.uuid, str)
    assert isinstance(notification_schema.type, NotificationTypesEnum)
    assert isinstance(notification_schema.ip_address, str)
    assert isinstance(notification_schema.payload, dict)
    assert isinstance(notification_schema.created_at, datetime)
    assert isinstance(notification_schema.updated_at, datetime)


def test_get_simple_notification_schema_with_valid_models(notification_fake_dict):
    notification_schema = schema.GetSimpleNotificationSchema(**notification_fake_dict)
    assert isinstance(notification_schema, schema.GetSimpleNotificationSchema)
    assert isinstance(notification_schema, CamelModel)
    assert isinstance(notification_schema, BaseModel)


def test_get_simple_notification_schema_with_valid_fields_values(
    notification_fake_dict,
):
    notification_schema = schema.GetSimpleNotificationSchema(**notification_fake_dict)
    assert isinstance(notification_schema.uuid, str)
    assert isinstance(notification_schema.type, NotificationTypesEnum)
    assert isinstance(notification_schema.created_at, datetime)


def test_create_notification_schema_with_valid_models(notification_fake_dict):
    notification_schema = schema.CreateNotificationSchema(**notification_fake_dict)
    assert isinstance(notification_schema, schema.CreateNotificationSchema)
    assert isinstance(notification_schema, CamelModel)
    assert isinstance(notification_schema, BaseModel)


def test_create_notification_schema_with_valid_fields_values(notification_fake_dict):
    notification_schema = schema.CreateNotificationSchema(**notification_fake_dict)
    assert isinstance(notification_schema.type, NotificationTypesEnum)
    assert isinstance(notification_schema.ip_address, str)
    assert isinstance(notification_schema.payload, dict)


def test_send_email_first_contact_schema_with_valid_models(
    send_email_first_contact_fake_dict,
):
    notification_schema = schema.SendEmailFirstContactSchema(
        **send_email_first_contact_fake_dict
    )
    assert isinstance(notification_schema, schema.SendEmailFirstContactSchema)
    assert isinstance(notification_schema, CamelModel)
    assert isinstance(notification_schema, BaseModel)


def test_send_email_first_contact_schema_with_valid_fields_values(
    send_email_first_contact_fake_dict,
):
    notification_schema = schema.SendEmailFirstContactSchema(
        **send_email_first_contact_fake_dict
    )
    assert isinstance(notification_schema.ip_address, str)
    assert isinstance(notification_schema.from_email, str)
    assert isinstance(notification_schema.text, str)
    assert isinstance(notification_schema.phone_number, str)


def test_send_email_first_contact_attributes_schema_with_invalid_email_field_value(
    send_email_first_contact_fake_dict,
):
    send_email_first_contact_fake_dict["from_email"] = "teste"
    with pytest.raises(ValidationError):
        schema.SendEmailFirstContactSchema(**send_email_first_contact_fake_dict)


def test_send_email_first_contact_attributes_schema_with_invalid_ip_address_field_value(
    send_email_first_contact_fake_dict,
):
    send_email_first_contact_fake_dict["ip_address"] = "teste"
    with pytest.raises(ValidationError):
        schema.SendEmailFirstContactSchema(**send_email_first_contact_fake_dict)


def test_send_email_first_contact_attributes_schema_with_invalid_phone_number_field_value(
    send_email_first_contact_fake_dict,
):
    send_email_first_contact_fake_dict["phone_number"] = "teste"
    with pytest.raises(ValidationError):
        schema.SendEmailFirstContactSchema(**send_email_first_contact_fake_dict)


def test_send_email_first_contact_attributes_schema_with_invalid_text_field_value(
    send_email_first_contact_fake_dict,
):
    send_email_first_contact_fake_dict["text"] = ""
    with pytest.raises(ValidationError):
        schema.SendEmailFirstContactSchema(**send_email_first_contact_fake_dict)
