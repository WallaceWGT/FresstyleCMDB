"--wallace--"
import os
import sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#获取资产的模式，根据可以支持的情况选择
MODE = 'agent' # salt,ssh

PLUGINS_DICT= {
    'cpu':'src.plugin.cpu.CpuPlugin',
    'disk':'src.plugin.disk.DiskPlugin',
    'main_board':'src.plugin.main_board.MainBoardPlugin',
    'memory':'src.plugin.memory.MemoryPlugin',
    'nic':'src.plugin.nic.NicPlugin'
}

#用于对API进行认证
KEY = '299095cc-1330-11e5-b06a-a45e60bec08b'
#用于对API认证的请求头
AUTH_KEY_NAME = 'auth-key'
ERROR_LOG_FILE = os.path.join(BASEDIR, 'log', 'error.log')
RUN_LOG_FILE = os.path.join(BASEDIR, 'log', 'run.log')
#Agent模式保存服务器的唯一ID的文件
CERT_FILE_PATH = os.path.join(BASEDIR, 'config', 'cert')
#资产信息API
ASSET_API = 'WWW'

#是否为测试模式，若为测试模式，这运行的数据则是从本地获取
TEST_MODE = True