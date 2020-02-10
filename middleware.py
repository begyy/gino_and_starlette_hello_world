from starlette.authentication import (
    AuthenticationBackend, AuthenticationError, SimpleUser, AuthCredentials
)
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

from starlette.responses import JSONResponse


class User:
    name = 'begyy'
    nickname = 'dota2'


def on_auth_error(request, exc):
    return JSONResponse({"error": str(exc)}, status_code=401)


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        token = request.headers.get("Authorization")
        #
        # if "Authorization" not in request.headers:
        #     raise AuthenticationError("invalid token")
        #
        # auth = request.headers["Authorization"]
        # try:
        #     scheme, credentials = auth.split()
        #     if scheme.lower() != 'basic':
        #         return
        #     decoded = base64.b64decode(credentials).decode("ascii")
        # except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
        #     raise AuthenticationError('Invalid basic auth credentials')
        #
        # username, _, password = decoded.partition(":")
        return AuthCredentials(["authenticated"]), User()


middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend(), on_error=on_auth_error)
]
