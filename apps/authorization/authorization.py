from models.user import User


async def auth(login, password):
    user = await User.query.where(User.username == login).gino.first()
    if user is None:
        return None

    check = await User.check_password(password, user.password)
    if check is False:
        return None
    return user
