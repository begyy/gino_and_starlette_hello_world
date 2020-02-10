from starlette.responses import JSONResponse
from user import User


async def homepage(request):
    results = []
    users = await User.query.gino.all()
    for user in users:
        results.append({
            "id": user.id,
            "name": user.username
        })
    return JSONResponse(results)
