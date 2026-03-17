from .dbase import RPCServer
from .setting import WebIP
from .setting import HTML,LOGS,IMGS,DIST


DEBUG = False
RPC = RPCServer(
    host="localhost",
    port = 6379, 
    db = 6,
    password="***********"
)
