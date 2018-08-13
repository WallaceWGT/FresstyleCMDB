"--wallace--"
import os
import hashlib
import time
import requests
import json
from config import settings
from src import plugin
from lib.serialize import Json
from lib.log import Logger

class AutoBase(object):
    def __init__(self):
        self.asset_api = settings.ASSET_API
        self.key = settings.KEY
        self.key_name = settings.AUTH_KEY_NAME
    def auto_key(self):
        '''
        对API进行认证
        :return:
        '''
        ha = hashlib.md5(self.key.encode('utf-8'))
        time_span = time.time()
        ha.update(bytes("%s|%f" % (self.key, time_span), encoding='utf-8'))
        encryption = ha.hexdigest()
        result = "%s|%f" % (encryption, time_span)
        return {self.key_name: result}
    def get_asset(self):
        '''
        获取资产数据，在子类中从写
        :return:
        '''
        pass
    def post_asset(self,msg,callback=None):
        '''
        得到数据后，提交
        :param msg:
        :param callback:
        :return:
        '''
        status=True
        try:
            headers = {}
            headers.update(self.auto_key())
            response = requests.post(
                url=self.asset_api,
                headers=headers,
                json=msg
            )
        except Exception as e:
            response = e
            status=False
        if callback:
            callback(status,response)
    def process(self):
        '''
        获取服务器信息，必须在子类中定义
        :return:
        '''
        raise NotImplementedError('you must implement process method')
    def callback(self,status,response):
        if not status:
            Logger().log(str(response),False)
            return
        ret = json.loads(response.text)
        if ret['code']==1000:
            Logger.log(ret['message'],True)
        else:
            Logger.log(ret['message'], False)

class AutoAgent(AutoBase):
    def __init__(self):
        self.cert_file_path = settings.CERT_FILE_PATH  #加载服务端保持服务器ID文件路径
        super(AutoAgent,self).__init__()

    def load_local_cert(self):
        '''
        获取本地标识
        :return:
        '''
        if not os.path.exists(self.cert_file_path):
        #是否存在这个文件，如果不存在返回None
            return None
        with open(self.cert_file_path,mode='r') as f:
            data = f.read()
        if not data:
            return None
        cert = data.strip()
        return cert

    def write_local_cert(self,cert):
        '''
        写入本机标识，即主机名，主要是为了保证提交是第一的主机用户，防止被修改，而导致数据库存储出现问题
        :param cert:
        :return:
        '''
        if not os.path.exists(self.cert_file_path):
            os.makedirs(os.path.basename(self.cert_file_path))
        with open(settings.CERT_FILE_PATH,mode='w') as f:
            f.write(cert)

    def process(self):
        #获取服务器信息
        server_info = plugin.get_server_info()

        #接根据本地的服务器ID，从而保证在服务器的主机id被修改后，提交数据时是根据本地存储的来方法
        if not server_info:
            return
        local_cert = self.load_local_cert()
        if local_cert:
            if local_cert == server_info.data['hostname']:
                pass
            else:
                server_info.data['hostname'] = local_cert
        else:
            self.write_local_cert(server_info.data['hostname'])
        #接下来是对数据进行序列化，和发送到对应的url
        server_json = Json.dumps(server_info.data)
        self.post_asset(server_json,self.callback)

class AutoSSH(AutoBase):
    def process(self):
        pass
    def run(self):
        pass

class AutoSalt(AutoBase):
    def process(self):
        pass
    def run(self):
        pass