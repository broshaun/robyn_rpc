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