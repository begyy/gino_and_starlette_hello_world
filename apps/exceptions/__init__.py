from starlette.exceptions import HTTPException
import typing
from exceptions.http_exception import http_exception


class JsonValidateError(HTTPException):
    def __init__(
            self,
            status_code: int,
            detail: typing.Optional[str] = None,
            error_messages: typing.Optional[dict] = None,
            exception: typing.Optional[Exception] = None,
    ) -> None:
        super().__init__(status_code, detail)
        self.error_messages = error_messages
        self.exception = exception
