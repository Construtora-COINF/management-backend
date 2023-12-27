from tortoise import fields
from app.abstracts.database.base_model import BaseModel


class Notification(BaseModel):
    type = fields.CharField(max_length=100)
    ip_address = fields.CharField(max_length=100)
    payload = fields.JSONField(null=True)

    class Meta:
        table = "notification"
