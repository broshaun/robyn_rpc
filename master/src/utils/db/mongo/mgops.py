from pymongo import AsyncMongoClient
from gridfs import AsyncGridFS
# import asyncio


class MgoDB:
    def __init__(self, host, port=27017, user=None, password=None,database='admin'):
        """初始化MongoDB连接"""
        if user is not None and password is not None:
            self._client = AsyncMongoClient(f"mongodb://{user}:{password}@{host}:{port}/?authSource=admin")
        else:
            self._client = AsyncMongoClient(f"mongodb://{host}:27017/")
        self._db = self._client[database]
        
    @property
    async def ping(self)->dict:
        return await self._client['admin'].command("ping")

    def fs(self,collection='fs'):
        return AsyncGridFS(self._db, collection)

    def col(self,collection):
        return self._db[collection]
    
    # def __del__(self):
    #     asyncio.create_task(self._client.close())
