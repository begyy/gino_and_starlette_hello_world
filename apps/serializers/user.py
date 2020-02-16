from marshmallow import fields
from serializers import MainSerializer


class UserSerializer(MainSerializer):
    username = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    password = fields.String(required=True)


class UserLoginSerializer(MainSerializer):
    username = fields.String(required=True)
    password = fields.String(required=True)


class UserListSerializer(MainSerializer):
    id = fields.Integer()
    username = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    is_active = fields.Boolean()
    is_superuser = fields.Boolean()
