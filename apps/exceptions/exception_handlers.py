from exceptions import JsonValidateError
from exceptions.http_exception import http_exception

exception_handlers = {
    JsonValidateError: http_exception
}
