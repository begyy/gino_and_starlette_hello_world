import uvicorn
from gino.ext.starlette import Gino
from starlette.applications import Starlette
from settings import DATABASE, middleware

app = Starlette(middleware=middleware)

db = Gino(dsn=DATABASE)
db.init_app(app)

from views.user import *

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
