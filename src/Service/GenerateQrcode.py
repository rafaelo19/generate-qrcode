import json
from pyqrcode import pyqrcode, QRCode
from src.Util.Serializer import Serializer
from src.Dto.Qrcode import Qrcode as QrcodeDto
from src.Exception.CreateQrcodeException import CreateQrcodeException


class GenerateQrcode:
    def __init__(self):
        self.serializer = Serializer()

    def generate(self, data: str) -> QrcodeDto:
        try:
            qrcode = self.create_qrcode(data)
            qrcode_dto = QrcodeDto()
            qrcode_dto.set_qrcode(qrcode.png_as_base64_str(scale=8))
            return qrcode_dto
        except Exception as e:
            raise CreateQrcodeException("Erro ao gerar Qrcode", 500)

    def create_qrcode(self, data) -> QRCode:
        data = json.loads(data)
        qrcode = pyqrcode.create(content=data['data'], error='M')
        return qrcode
