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
    async def all(cls):
        return cls.query.gino.all()
