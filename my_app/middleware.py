from starlette.authentication import (
    AuthenticationBackend, AuthCredentials, UnauthenticatedUser
)
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware


class CustomUnauthenticatedUser(UnauthenticatedUser):
    @property
    def is_superuser(self) -> bool:
        return False


class AuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        from models import Token, User
        token = request.headers.get("Authorization")
        check = await Token.check_token(token)
        if check is None:
            return AuthCredentials(), CustomUnauthenticatedUser()
        user = await User.get(check.user_id)
        return AuthCredentials(["authenticated"]), user


middleware = [
    Middleware(AuthenticationMiddleware, backend=AuthBackend())
]
