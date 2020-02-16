from marshmallow import Schema, ValidationError
from exceptions import JsonValidateError


class MainSerializer(Schema):

    async def is_valid(self, data):
        try:
            result = self.load(data)
            return result
        except ValidationError as err:
            raise JsonValidateError(error_messages=err.messages, status_code=400)
