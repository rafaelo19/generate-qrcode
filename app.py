from flask import Flask, request
from src.Util.ApiResponse import ApiResponse
from src.Exception.CreateQrcodeException import CreateQrcodeException
from src.Middleware.ValidationDataMiddleware import validation

from src.Service.GenerateQrcode import GenerateQrcode

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return ApiResponse({"data": "Api-Qrcode"}, 200).get_response()


@app.route("/generates", methods=['POST'])
@validation
def generate():
    try:
        return ApiResponse(GenerateQrcode().generate(request.data), 201).get_response()
    except CreateQrcodeException as e:
        return ApiResponse(e, e.get_status_code()).get_response()
    except Exception as e:
        return ApiResponse(e, 500).get_response()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
