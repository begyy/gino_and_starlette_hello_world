from passlib.hash import pbkdf2_sha256
from models import BaseModel, db


class User(BaseModel):
    __tablename__ = "user"

    username = db.Column(db.String(50), default="unnamed")
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    is_active = db.Column(db.Boolean(), default=True)
    is_superuser = db.Column(db.Boolean(), default=False)
    password = db.Column(db.String(250))

    @staticmethod
    async def check_password(password, hash_password) -> bool:
        return pbkdf2_sha256.verify(password, hash_password)

    @property
    def is_authenticated(self) -> bool:
        return True

    @property
    def display_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @classmethod
    async def all(cls) -> list:
        return await cls.query.gino.all()

    @staticmethod
    async def hash_password(password) -> str:
        hash = pbkdf2_sha256.hash(password)
        return hash
