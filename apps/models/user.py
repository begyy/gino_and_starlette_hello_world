from manage import db
from passlib.hash import pbkdf2_sha256


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.BigInteger(), primary_key=True)
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

    @staticmethod
    async def all() -> list:
        return await User.query.gino.all()

    @staticmethod
    async def hash_password(password) -> str:
        hash = pbkdf2_sha256.hash(password)
        return hash
