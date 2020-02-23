import os
import sys
from alembic.config import Config
from rest_framework.parser import JSONParser
from rest_framework.permissions import IsAuthenticated

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'apps'))
SECRET_KEY = 'SECRET_KEY'
DEBUG = os.environ.get('DEBUG', True)

DATABASE_NAME = os.environ.get('DATABASE_NAME', 'gino')
DATABASE_USER = os.environ.get('DATABASE_USER', 'gino_user')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'gino_password')

DATABASE = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}"

ALEMBIC_CFG = Config(os.path.join(BASE_DIR, 'alembic.ini'))
PAGE_SIZE = 25

DEFAULT_PARSER_CLASS = JSONParser
DEFAULT_PERMISSION_CLASS = IsAuthenticated
