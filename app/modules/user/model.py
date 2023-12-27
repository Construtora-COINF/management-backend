from tortoise import fields
from app.abstracts.database.base_model import BaseModel


class User(BaseModel):
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=100)
    is_active = fields.BooleanField(default=True)

    class Meta:
        table = "user"
