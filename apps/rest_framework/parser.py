from exceptions import JsonValidateError


class BaseParser:
    """
    All parsers should extend `BaseParser`, specifying a `media_type`
    attribute, and overriding the `.parse()` method.
    """
    media_type = None

    def parse(self, request):
        """
        Given a stream to read from, return the parsed representation.
        Should return parsed data, or a `DataAndFiles` object consisting of the
        parsed data and files.
        """
        raise NotImplementedError(".parse() must be overridden.")


class JSONParser(BaseParser):
    """
    Parses JSON-serialized data.
    """
    media_type = 'application/json'

    async def parse(self, request):
        """
        Parses the incoming bytestream as JSON and returns the resulting data.
        """

        try:
            await request.json()
        except ValueError as exc:
            error_message = {'detail': 'JSON parse error - %s' % str(exc)}
            raise JsonValidateError(error_messages=error_message, status_code=400)
