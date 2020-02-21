from manage import db
from datetime import datetime


class BaseModel(db.Model):
    __tablename__ = None
    id = db.Column(db.BigInteger(), primary_key=True)
    created_datetime = db.Column(db.DateTime(), default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)
        assert self.__tablename__, 'Table name is not defined'

    @classmethod
    async def all(cls) -> list or None:
        return await cls.query.gino.all()

    @classmethod
    async def filter(cls, *args) -> list or None:
        return await cls.query.where(*args).gino.all()

    @classmethod
    async def filter_and_first(cls, *args) -> object or None:
        return await cls.query.where(*args).gino.first()

    @classmethod
    async def filter_and_last(cls, *args) -> object or None:
        return await cls.query.where(*args).gino.last()

    @classmethod
    async def get_or_create(cls, *args) -> object:
        check = await cls.query.where(*args).gino.first()
        if check:
            return check
        return await cls.create(*args)
