import uvicorn
from starlette.applications import Starlette
from my_app.settings import DATABASE, DEBUG
from my_app.middleware import middleware
from gino.ext.starlette import Gino

app = Starlette(debug=DEBUG, middleware=middleware)
db = Gino(dsn=DATABASE)
db.init_app(app)
from views import *

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
