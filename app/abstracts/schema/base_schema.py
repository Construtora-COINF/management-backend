from abc import ABCMeta

from fastapi_camelcase import CamelModel


class BaseSchema(CamelModel, metaclass=ABCMeta):
    class Config:
        orm_mode = True
