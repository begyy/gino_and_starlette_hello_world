from starlette.responses import JSONResponse


async def http_exception(request, exc):
    return JSONResponse(exc.error_messages, status_code=exc.status_code)
