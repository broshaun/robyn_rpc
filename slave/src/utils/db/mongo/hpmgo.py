from .mgops import Mongo
from bson import ObjectId,errors
from pymongoarrow.api import aggregate_arrow_all
import polars as pl

def convert_to_objectid(object_id):
    if isinstance(object_id, ObjectId):
        return object_id
    try:
        return ObjectId(object_id)
    except errors.InvalidId:
        return None


class CRUD(object):
    def __init__(self,mgo:Mongo,collection_name):
        self.uid = 0
        self.col = mgo.col(collection_name)
    
    def insert_one(self, document):
        document["creator"] = self.uid
        return self.col.insert_one(document).inserted_id
    
    def insert_many(self, documents):
        return self.col.insert_many(documents).inserted_ids
    
    def delete_id(self, object_id):
        object_id = convert_to_objectid(object_id)
        if not object_id:
            return 0
        return self.col.delete_one({"_id": object_id}).deleted_count
    
    def delete_many(self, **filter):
        return self.col.delete_many(filter).deleted_count
    
    def drop(self):
        self.col.drop()

    def update_one_push(self,object_id, document:dict={}):
        object_id = convert_to_objectid(object_id)
        if not object_id:
            return 0
        return self.col.update_one(filter={'_id':object_id},update={'$push':document}).modified_count
    
    def update_one_pull(self,object_id, document:dict={}):
        object_id = convert_to_objectid(object_id)
        if not object_id:
            return 0
        return self.col.update_one(filter={'_id':object_id},update={'$pull':document}).modified_count
    
    def update_one_set(self,object_id, document:dict={}):
        object_id = convert_to_objectid(object_id)
        if not object_id:
            return 0
        return self.col.update_one(filter={'_id':object_id},update={'$set':document}).modified_count
    
    def update_one_unset(self,object_id, document:dict={}):
        object_id = convert_to_objectid(object_id)
        if not object_id:
            return 0
        return self.col.update_one(filter={'_id':object_id},update={'$unset':document}).modified_count
    
    def replace_one(self,object_id, document:dict={}):
        object_id = convert_to_objectid(object_id)
        if not object_id:
            return 0
        return self.col.update_one(filter={'_id':object_id},update=document).modified_count

    def count(self,**filter)->int:
        return self.col.count_documents(filter)

    def find(self, filter:dict, skip=0, limit=10,**kwargs)->pl.DataFrame:
        pipeline= [
            {"$match": filter},
            {"$set": {"id": {"$toString": "$_id"}}},
            {"$unset": "_id"},
            {"$skip": int(skip)},
            {"$limit": int(limit)},
        ]
        table = aggregate_arrow_all(self.col, pipeline=pipeline, **kwargs)
        return pl.from_arrow(table)

    def find_id(self, object_id, **kwargs)->pl.DataFrame:
        object_id = convert_to_objectid(object_id)
        if not object_id:
            return dict()
        
        for ss in self.find(filter={'_id':object_id}, **kwargs).iter_rows(named=True):
            return ss
        else:
            return dict()
        
    def find_one(self, filter, **kwargs):
        for ss in self.find(filter, **kwargs).iter_rows(named=True):
            return ss
        else:
            return dict()

    def find_for_total_detail(self, filter:dict, skip=0, limit=10, **kwargs):
        data = {}
        data['total'] = self.col.count_documents(filter)
        data['detail'] = self.find(filter, skip, limit, **kwargs)
        return data
    
        






        







   
            


        
    
        
        
        
