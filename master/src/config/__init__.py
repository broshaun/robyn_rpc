from .dbase import RPCServer
from .setting import WebIP
from .setting import HTML,LOGS,IMGS,DIST


DEBUG = False
RPC = RPCServer(
    host="103.186.108.161",
    # host="192.168.2.2",
    port = 6379, 
    db = 6,
    password="su7vu9xyzlakklmo121s"
)
