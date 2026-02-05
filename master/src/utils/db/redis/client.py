import redis
from typing import Optional, Dict, ClassVar


class RedisClient:
    __POOL_MAP: ClassVar[Dict[int, redis.ConnectionPool]] = {}
    def __init__(self, host: str, port: int, db: int, password: Optional[str] = None):
        if db not in RedisClient.__POOL_MAP:
            RedisClient.__POOL_MAP[db] = redis.ConnectionPool(host=host,port=port,db=db,password=password,decode_responses=True)
        self.client = redis.Redis.from_pool(connection_pool=RedisClient.__POOL_MAP[db])

    def store(self, alias:str, value, *args, **kwargs) -> bool:
        '''存储数据'''
        return self.client.set(name=alias, value=value, *args, **kwargs)

    def load(self, alias:str):
        '''加载数据'''
        return self.client.get(name=alias)
    
    def delete(self, *alias:str) -> int:
        '''删除别名对于缓存'''
        return self.client.delete(*alias)

    def exists(self,*alias:str) -> int:
        '''返回存在的名称数'''
        return self.client.exists(*alias)
    