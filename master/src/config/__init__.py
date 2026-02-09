from .dbase import RPCServer
from .setting import WebIP
from .setting import HTML,LOGS,IMGS,DIST


DEBUG = False
RPC = RPCServer(
    host="redis.service",
    port = 6379, db = 6,
    password="su7vu9xyzlakklmo121s"
)
