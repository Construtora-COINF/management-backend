from tortoise.fields import DatetimeField, IntField, CharField
from tortoise.models import Model


class BaseModel(Model):
    id = IntField(pk=True)
    uuid = CharField(max_length=32)
    created_at = DatetimeField(auto_now_add=True)
    updated_at = DatetimeField(auto_now=True)

    class Meta:
        abstract = True
