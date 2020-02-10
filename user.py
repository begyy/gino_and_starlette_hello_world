from gino import Gino

db = Gino()


class User(db.Model):
    __tablename__ = "gino_users"

    id = db.Column(db.BigInteger(), primary_key=True)
    username = db.Column(db.String(50), default="unnamed")
    password = db.Column(db.String(250))
