from uuid import uuid4

from tortoise import Model


class BaseRepository:
    def __init__(self):
        self.entity = Model

    async def create(self, payload: dict):
        payload["uuid"] = uuid4().hex
        return await self.entity.create(**payload)

    async def update(self, payload: dict, _id: int) -> Model:
        await self.entity.filter(id=_id).update(**payload)
        return await self.get_by_id(_id)

    async def get_all(self) -> list:
        return await self.entity.all()

    async def get_by_id(self, _id: int) -> [dict, None]:
        return await self.entity.get_or_none(id=_id)

    async def delete(self, _id: int) -> bool:
        await self.entity.filter(id=_id).delete()
        return True

    async def get_or_none(self, **kwargs):
        return await self.entity.get_or_none(**kwargs)

    async def filter(self, get_first: bool = False, **kwargs):
        if get_first:
            return await self.entity.filter(**kwargs).first()
        return await self.entity.filter(**kwargs)
