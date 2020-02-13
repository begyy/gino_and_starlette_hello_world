import binascii
from manage import db
import os


class Token(db.Model):
    __tablename__ = "token"
    id = db.Column(db.BigInteger(), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    token = db.Column(db.String(250))
    token1 = db.Column(db.String(250))

    @staticmethod
    async def generate_key():
        return binascii.hexlify(os.urandom(20)).decode()

    @staticmethod
    async def get_or_create(user_id):
        check = await Token.query.where(Token.user_id == user_id).gino.first()
        if check:
            return check.token
        key = await Token.generate_key()
        token = await Token.create(user_id=user_id, token=key)
        return token.token

    @staticmethod
    async def check_token(token):
        return await Token.query.where(Token.token == token).gino.first()
