# from starlette.applications import Starlette
# import uvicorn
# from gino.ext.starlette import Gino
# from settings import DATABASE
# from view import homepage
from starlette.routing import Route
#
# app = Starlette(debug=True,routes=[Route('/', homepage)])
# db = Gino(dsn=DATABASE)
# db.init_app(app)
#
#
#
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)


import os

from starlette.applications import Starlette
import uvicorn
from gino.ext.starlette import Gino
from view import homepage

DB_ARGS = dict(
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", 5432),
    user=os.getenv("DB_USER", "gino_user"),
    password=os.getenv("DB_PASS", "gino_password"),
    database=os.getenv("DB_NAME", "gino"),
)
PG_URL = "postgresql://{user}:{password}@{host}:{port}/{database}".format(
    **DB_ARGS
)

# Initialize Starlette app
app = Starlette(routes=[Route('/', homepage)])

# Initialize Gino object
db = Gino(dsn=PG_URL)
db.init_app(app)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
