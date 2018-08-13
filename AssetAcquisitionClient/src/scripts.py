"--wallace--"
from .client import AutoAgent
from .client import AutoSSH
from .client import AutoSalt

from config import settings

def client():
    '''
    根据配置文件中的获取资产模式实例化对应的对象
    :return:
    '''
    if settings.MODE == "agent":  #agent模式是服务端主动提交数据到API
        cli = AutoAgent()
    elif settings.MODE == "ssh":  #ssh模式是先充服务端获取需要采集的资产明细，然后远程连接服务器，通过命令获取数据
        cli = AutoSSH()
    elif settings.MODE == "salt": #流程和ssh类似，不过资产采集时的方式稍微有些不同
        cli = AutoSalt()
    else:
        raise Exception('请配置资产采集模式，如：agent,ssh,salt')
    cli.process()




