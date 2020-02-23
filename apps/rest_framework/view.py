from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
import asyncio
from starlette.concurrency import run_in_threadpool
from exceptions import JsonValidateError
from my_app import settings
from starlette import status


class APIView(HTTPEndpoint):
    parser_class = None
    permission_class = None

    def __init__(self, *args, **kwargs):
        self.request = None
        super(APIView, self).__init__(*args, **kwargs)

    async def dispatch(self) -> None:
        request = Request(self.scope, receive=self.receive)
        self.request = request

        await self.get_permission_classes()
        await self.get_parser_classes()

        handler_name = "get" if request.method == "HEAD" else request.method.lower()
        handler = getattr(self, handler_name, self.method_not_allowed)
        is_async = asyncio.iscoroutinefunction(handler)
        if is_async:
            response = await handler(request)
        else:
            response = await run_in_threadpool(handler, request)
        await response(self.scope, self.receive, self.send)

    async def get_permission_classes(self):
        if self.permission_class is None:
            if hasattr(settings, 'DEFAULT_PERMISSION_CLASS'):
                self.permission_class = settings.DEFAULT_PERMISSION_CLASS
        result = await self.permission_class().has_permission(self.request)
        if result is False:
            error_message = {'detail': 'permission denied'}
            raise JsonValidateError(error_messages=error_message, status_code=status.HTTP_403_FORBIDDEN)

    async def get_parser_classes(self):
        if self.parser_class is None:
            if hasattr(settings, 'DEFAULT_PARSER_CLASS'):
                self.parser_class = [settings.DEFAULT_PARSER_CLASS]
        for parser in self.parser_class:
            await parser().parse(self.request)
