"--wallace--"
import json as default_json
from json.encoder import JSONEncoder

from .response import BaseResponse

'''
自定制Json数据的序列化
'''
class JsonEncode(JSONEncoder):
    def default(self, o):
        if isinstance(o,BaseResponse):
            return o.__dict__
        return JSONEncoder.default(self,o)

class Json(object):
    @staticmethod
    def dumps(response,ensure_ascii=True):
        return default_json.dumps(response,ensure_ascii=ensure_ascii,cls=JsonEncode)