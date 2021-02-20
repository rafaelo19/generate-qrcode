from flask import request
from functools import wraps
from src.Util.Serializer import Serializer
from src.Util.ApiResponse import ApiResponse
from src.Exception.InvalidDataException import InvalidDataException


def validation(func):
    @wraps(func)
    def validation_decorator(*args, **kwargs):
        try:
            data = Serializer().decode(request.data)
            if type(data['data']) is not str and type(data['data']) is not int and type(data['data']) is not float:
                raise InvalidDataException("Dados inválidos", 400)
        except InvalidDataException as e:
            return ApiResponse(e, e.get_status_code()).get_response()

        return func(*args, **kwargs)

    return validation_decorator
