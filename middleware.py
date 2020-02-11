from starlette.responses import JSONResponse
from starlette.authentication import (
    AuthenticationBackend, AuthCredentials
)
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware


def on_auth_error(request, exc):
    return JSONResponse({"error": str(exc)}, status_code=401)


class AuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        from models import Token, User
        token = request.headers.get("Authorization")
        check = await Token.check_token(token)
        if check is None:
            return None
        user = await User.get(check.user_id)
        return AuthCredentials(["authenticated"]), user


middleware = [
    Middleware(AuthenticationMiddleware, backend=AuthBackend(), on_error=on_auth_error)
]
