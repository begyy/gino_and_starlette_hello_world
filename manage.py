import uvicorn
from starlette.applications import Starlette
from my_app.settings import DATABASE, DEBUG, ALEMBIC_CFG
from my_app.middleware import middleware
from my_app.commands import args
from gino.ext.starlette import Gino
from alembic import command

app = Starlette(debug=DEBUG, middleware=middleware)
db = Gino(dsn=DATABASE)
db.init_app(app)
from views import *

if __name__ == "__main__":
    if args.command == 'runserver':
        uvicorn.run(app, host="127.0.0.1", port=8000)
    if args.command == 'makemigrations':
        print(ALEMBIC_CFG)
        command.revision(ALEMBIC_CFG, autogenerate=True)
    if args.command == "migrate":
        command.upgrade(ALEMBIC_CFG, "head")
