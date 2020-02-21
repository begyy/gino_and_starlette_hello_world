from models.user import User


async def auth(login, password):
    user = await User.filter_and_first(User.username == login)
    if user is None:
        return None

    check = await User.check_password(password, user.password)
    if check is False:
        return None
    return user
