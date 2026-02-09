import redis.asyncio as redis
from typing import Optional, Dict, ClassVar


class AsynClient:
    __POOL_MAP: ClassVar[Dict[int, redis.ConnectionPool]] = {}
    def __init__(self, host: str, port: int, db: int, password: Optional[str] = None):
        if db not in AsynClient.__POOL_MAP:
            AsynClient.__POOL_MAP[db] = redis.ConnectionPool(host=host,port=port,db=db,password=password,decode_responses=True)
        self.client = redis.Redis.from_pool(AsynClient.__POOL_MAP[db])

    async def store(self, alias: str, value, *args, **kwargs) -> bool:
        return await self.client.set(alias, value, *args, **kwargs)

    async def load(self, alias: str):
        return await self.client.get(alias)

    async def delete(self, *alias: str) -> int:
        return await self.client.delete(*alias)

    async def exists(self, *alias: str) -> int:
        return await self.client.exists(*alias)
    




class RPC:
    HOST = "192.168.64.1"
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
        success = await AsynClient(host=cls.HOST,port=cls.PORT,db=cls.DB,password=cls.DBPWD).store(alias='super',value='tcp://127.0.0.1:4242')
        if success:
            print("RPCSuper存储成功")


import asyncio

a = RPC()


asyncio.run( a.RPCServer(alias='slave'))