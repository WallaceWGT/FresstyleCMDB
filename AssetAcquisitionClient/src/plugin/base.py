"--wallace--"
from config import settings
from lib.log import Logger

class BasePlugin(object):
    def __init__(self,hostname=''):
        self.logger = Logger()
        self.test_mode = settings.TEST_MODE
        self.mode_list = ['agent','salt','ssh']
        if hasattr(settings,'MODE'):
            self.mode = settings.MODE
        else:
            self.mode = 'agent'
        self.hostname = hostname
    def ssh(self,cmd):
        pass
    def agent(self,cmd):
        '''
        agent形式是在服务器本地执行命令
        :param cmd:
        :return:
        '''
        import subprocess
        output = subprocess.getoutput(cmd)
        return output
    def salt(self,cmd):
        pass
    def exec_shell_cmd(self,cmd):
        if self.mode not in self.mode_list:
            raise Exception('settings.mode must be one of ["agent","ssh","salt"]')
        func = getattr(self,self.mode)
        output = func(cmd)
        return output
    def execute(self): #更加平台处理对应平台的命令，这里是linux()
        return self.linux()
    def linux(self):
        raise Exception('..........')

