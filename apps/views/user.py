from starlette.responses import JSONResponse
from models import User, Token
from authorization.authorization import auth
from manage import app, db
from starlette.authentication import requires
from serializers.user import UserSerializer, UserLoginSerializer, UserListSerializer
from paganation import PaginationResponse

@app.route("/signup/", methods=['POST'])
async def signup(request):
    data = await request.json()
    serializer = await UserSerializer().is_valid(data=data)

    username = serializer['username']
    first_name = serializer['first_name']
    last_name = serializer['last_name']
    password = serializer['password']

    check = await User.query.where(User.username == username).gino.first()
    if check:
        return JSONResponse({"error": "User already exists"}, status_code=400)
    hash_password = await User.hash_password(password)
    await User.create(username=username, first_name=first_name, last_name=last_name, password=hash_password)
    return JSONResponse({"detail": "successfully"})


@app.route("/login/", methods=['POST'])
async def login(request):
    data = await request.json()
    serializer = await UserLoginSerializer().is_valid(data=data)

    username = serializer['username']
    password = serializer['password']

    user = await auth(username, password)
    if user is None:
        return JSONResponse({"detail": "username or password not properly"}, status_code=401)
    token = await Token.get_or_create(user.id)
    return JSONResponse({"token": token})


@app.route("/users/", methods=['GET'])
@requires('authenticated', status_code=401)
async def user_list(request):
    #query = db.select([User]).limit(2)
    users = await User.all()

    serializer = UserListSerializer(many=True).dump(users)
    return PaginationResponse(serializer)


@app.route("/my_profile/", methods=['GET'])
@requires("authenticated", status_code=401)
async def my_profile(request):
    serializer = UserListSerializer().dump(request.user)
    return JSONResponse(serializer)
