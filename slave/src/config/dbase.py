from utils.db.mongo import DBOpen
from utils.db.redis import RedisClient
from .setting import WebIP


localhost = 'localhost'


class Session:
    # HOST = "redis.service"
    HOST = localhost
    DBPWD = "su7vu9xyzlakklmo121s"
    PORT = 6379
    DB = 3
    def __new__(cls):
        return RedisClient(host=cls.HOST,port=cls.PORT,db=cls.DB,password=cls.DBPWD)

class RPC:
    # HOST = "redis.service"
    HOST = localhost
    DBPWD = "su7vu9xyzlakklmo121s"
    PORT = 6379
    DB = 6

    @classmethod
    def RPCServer(cls,alias:str):
        '''微服务地址'''
        endpoint = RedisClient(host=cls.HOST,port=cls.PORT,db=cls.DB,password=cls.DBPWD).load(alias)
        if isinstance(endpoint, bytes):
            endpoint = endpoint.decode('utf-8')
        return endpoint
        
    @classmethod
    def RPCStore(cls):
        '存储示例'
        success = RedisClient(host=cls.HOST,port=cls.PORT,db=cls.DB,password=cls.DBPWD).store(alias='slave',value='tcp://localhost:4242')
        if success:
            print("RPCSlave存储成功")

class MongoDB():
    # HOST = "mongo.service"
    HOST = localhost
    PORT = 27017
    DBUSER = 'root'
    DBPWD = 'you_paseworkey'
    def __new__(cls,database):
        return DBOpen(host=cls.HOST,port=cls.PORT,user=cls.DBUSER,password=cls.DBPWD,database=database)

