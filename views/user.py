from starlette.responses import JSONResponse
from models import User, Token
from authorization.authorization import auth
from manage import app
from starlette.authentication import requires


@app.route("/signup/", methods=['POST'])
async def signup(request):
    data = await request.json()
    check = await User.query.where(User.username == data['username']).gino.first()
    if check:
        return JSONResponse({"error": "User already exists"}, status_code=400)
    hash_password = await User.encode_password(data['password'])
    await User.create(username=data['username'], password=hash_password)
    return JSONResponse({"detail": "successfully"})


@app.route("/login/", methods=['POST'])
async def login(request):
    data = await request.json()
    user = await auth(data['username'], data['password'])
    if user is None:
        return JSONResponse({"detail": "username or password not properly"}, status_code=401)
    token = await Token.get_or_create(user.id)
    return JSONResponse({"token": token})


@app.route("/users/", methods=['GET'])
@requires('authenticated', status_code=401)
async def user_list(request):
    results = list()
    users = await User.all()
    for user in users:
        results.append(dict(
            id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            is_active=user.is_active,
            is_superuser=user.is_superuser
        ))
    return JSONResponse(results)


@app.route("/my_profile/", methods=['GET'])
@requires("authenticated", status_code=401)
async def my_profile(request):
    return JSONResponse({
        "id": request.user.id,
        "username": request.user.username,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "is_active": request.user.is_active,
        "is_superuser": request.user.is_superuser
    })
