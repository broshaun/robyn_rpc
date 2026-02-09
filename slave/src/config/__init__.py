from .dbase import RPCServer
from utils.db.redis import RedisClient
from utils.db.mongo import DBOpen
from .setting import LOGS,WebIP

## 调试模式True/False
DEBUG = True
SECRET_KEY = '7aP!5hF&9sK*2dJ@3zX#8gH%0nM$4rC6vB8eG)9tY'

RPCServer(
    host="192.168.64.1",
    port = 6379, db = 6,
    password="su7vu9xyzlakklmo121s"
).Store(alias='slave',location='tcp://192.168.64.1:4242')


class Session:
    HOST = '192.168.64.1'
    DBPWD = "su7vu9xyzlakklmo121s"
    PORT = 6379
    DB = 3
    def __new__(cls):
        return RedisClient(host=cls.HOST,port=cls.PORT,db=cls.DB,password=cls.DBPWD)

class MongoDB():
    HOST = '192.168.64.1'
    PORT = 27017
    DBUSER = 'root'
    DBPWD = 'you_paseworkey'
    def __new__(cls,database):
        return DBOpen(host=cls.HOST,port=cls.PORT,user=cls.DBUSER,password=cls.DBPWD,database=database)