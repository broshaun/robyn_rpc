from pymongo import MongoClient
from pymongoarrow.api import aggregate_arrow_all
from pymongoarrow.schema import Schema
import polars as pl


class Mongo:
    def __init__(self, host, port=27017, user=None, password=None, database=None, **kwargs):
        """初始化MongoDB连接"""
        if user and password:
            self._client = MongoClient(f"mongodb://{user}:{password}@{host}:{port}/?authSource=admin", **kwargs)
        else:
            self._client = MongoClient(f"mongodb://{host}:27017/", **kwargs)
        self._db = self._client[database]

    @property
    def ping(self)->dict:
        return self._client['admin'].command("ping")
    
    @property
    def db(self):
        if self._db is None:
            raise RuntimeError("Database not set")
        return self._db

    def aggregate_to_polars(self, collection, filter:dict, *, skip=None, limit=None, schema:Schema=None, allow_invalid=False, **kwargs)->pl.DataFrame:
        pipeline= [
            {"$match": filter},
            {"$set": {"id": {"$toString": "$_id"}}},{"$unset": "_id"}
        ]
        if skip:
            pipeline.append({"$skip": int(skip)})
        if limit:
            pipeline.append({"$limit": int(limit)})
        return pl.from_arrow(aggregate_arrow_all(collection, pipeline, schema=schema, allow_invalid=allow_invalid, **kwargs))
    


