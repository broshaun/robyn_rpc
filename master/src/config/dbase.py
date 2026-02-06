from utils.db.redis import AsynClient


localhost = '127.0.0.1'

class RPC:
    # HOST = "redis.service"
    HOST = localhost
    DBPWD = "su7vu9xyzlakklmo121s"
    PORT = 6379
    DB = 6

    @classmethod
    async def RPCServer(cls,alias:str):
        '''微服务地址'''
        endpoint = await AsynClient(host=cls.HOST,port=cls.PORT,db=cls.DB,password=cls.DBPWD).load(alias)
        if isinstance(endpoint, bytes):
            endpoint = endpoint.decode('utf-8')
        return endpoint
        
    @classmethod
    async def RPCStore(cls):
        '存储示例'
        success = await AsynClient(host=cls.HOST,port=cls.PORT,db=cls.DB,password=cls.DBPWD).store(alias='slave',value='tcp://127.0.0.1:4242')
        if success:
            print("RPCSuper存储成功")
