import json
from json import JSONEncoder


class Serializer(JSONEncoder):
    def default(self, entity):
        return entity.__dict__

    def decode(self, data):
        return json.loads(data)
