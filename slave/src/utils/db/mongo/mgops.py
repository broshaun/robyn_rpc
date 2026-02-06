from pymongo import MongoClient


class Mongo:
    def __init__(self, host, port=27017, user=None, password=None,database='admin'):
        """初始化MongoDB连接"""
        if user and password:
            self._client = MongoClient(f"mongodb://{user}:{password}@{host}:{port}/?authSource=admin")
        else:
            self._client = MongoClient(f"mongodb://{host}:27017/")
        self._db = self._client[database]
        
    @property
    def ping(self)->dict:
        return self._client['admin'].command("ping")

    def col(self,collection):
        return self._db[collection]
    
    

