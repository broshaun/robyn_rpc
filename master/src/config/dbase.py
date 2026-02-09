from utils.db.redis import AsynClient


class RPCServer:
    def __init__(self,host,port,db,password):
        self.host = host
        self.port = port
        self.db = db
        self.password = password

    async def HOST(self,alias:str):
        '''微服务地址'''
        endpoint = await AsynClient(host=self.host, port=self.port, db=self.db, password=self.password).load(alias)
        if isinstance(endpoint, bytes):
            endpoint = endpoint.decode('utf-8')
        return endpoint
        
    async def Store(self,alias,location):
        '存储示例'
        success = await AsynClient(host=self.host, port=self.port, db=self.db, password=self.password).store(alias, value=location)
        if success:
            print("RPCSuper存储成功")
