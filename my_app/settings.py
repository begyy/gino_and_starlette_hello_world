import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'SECRET_KEY'
DEBUG = os.environ.get('DEBUG', True)

DATABASE_NAME = os.environ.get('DATABASE_NAME', 'gino')
DATABASE_USER = os.environ.get('DATABASE_USER', 'gino_user')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'gino_password')

DATABASE = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}"

ALEMBIC_CFG = os.path.join(BASE_DIR, 'alembic.ini')
