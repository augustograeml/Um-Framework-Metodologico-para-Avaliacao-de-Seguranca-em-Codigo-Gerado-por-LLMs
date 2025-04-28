from .base import BaseSerializer
import json

class JsonSerializer(BaseSerializer):
    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, json_string):
        return json.loads(json_string)