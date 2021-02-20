from flask import make_response
from src.Util.Serializer import Serializer


class ApiResponse:
    def __init__(self, data, status_code):
        data = Serializer().encode(data)
        self.response = make_response(data)
        self.response.status_code = status_code
        self.response.mimetype = 'application/json'

    def get_response(self) -> make_response:
        return self.response
