from datetime import datetime
from uuid import uuid4

import pytest
from faker import Factory

from app.modules.notifications.enum import NotificationTypesEnum
from app.services.amazon_ses import AmazonSimpleEmailService

faker = Factory.create("pt_BR")


@pytest.fixture()
def notification_fake_dict():
    return {
        "id": faker.random_int(min=1, max=9999),
        "uuid": uuid4().hex,
        "type": NotificationTypesEnum.EMAIL_FIRST_CONTACT.value,
        "ip_address": faker.ipv4(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "payload": {"teste": "teste"},
    }


@pytest.fixture()
def send_email_first_contact_fake_dict():
    return {
        "from_email": faker.email(),
        "ip_address": faker.ipv4(),
        "text": faker.name(),
        "phone_number": faker.phone_number(),
    }


@pytest.fixture
async def mock_monkey_patch(monkeypatch):
    async def mock_amazon_ses_send_email(*args, **kwargs):
        return True

    monkeypatch.setattr(
        AmazonSimpleEmailService,
        "send_email",
        mock_amazon_ses_send_email,
    )
