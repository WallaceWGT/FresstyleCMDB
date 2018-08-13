"--wallace--"
import os
import sys
from src.plugin.basic import BasicPlugin
from config import settings
import importlib
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

def get_server_info(hostname=None):
    '''
    获取服务端信息
    :param hosename: agent模式时，hostname为空,原因是agent是服务器主动提交数据
    ，salt或ssh时是先从后台管理哪里获取需要提交的服务器名，然后从服务器获取数据，
    hostname表示要链接的服务器
    :return:
    '''
    response = BasicPlugin(hostname).execute()
    if not response.status:
        return response
    for k,v in settings.PLUGINS_DICT.items(): #根据配置文件来获取需要采集的资产信息
        module_path,cls_name = v.rsplit('.',1)
        cls = getattr(importlib.import_module(module_path),cls_name)
        obj = cls(hostname).execute()
        response.data[k]=obj
    return response

if __name__ == '__main__':
    ret = get_server_info()
    print(ret.__dict__)