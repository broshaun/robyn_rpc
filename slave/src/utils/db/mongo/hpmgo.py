from .mgops import Mongo
from bson import ObjectId,errors
from pymongoarrow.api import find_arrow_all
from pymongoarrow.schema import Schema
import polars as pl

def convert_to_objectid(object_id:str):
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
        if not isinstance(object_id, ObjectId):
            object_id = convert_to_objectid(object_id)
            if not object_id:
                return 0
        return self.col.delete_one({"_id": object_id}).deleted_count
    
    def delete_many(self, **filter):
        return self.col.delete_many(filter).deleted_count
    
    def drop(self):
        self.col.drop()

    def update_one(self, object_id, document:dict={}):
        if not isinstance(object_id,ObjectId):
            object_id = convert_to_objectid(object_id)
            if not object_id:
                return 0
        if 'push' in document:
            result = self.col.update_one(filter={'_id':object_id},update={'$push':document.get('push')})
        elif 'pull' in document:
            result = self.col.update_one(filter={'_id':object_id},update={'$pull':document.get('pull')})
        elif 'unset' in document:
            result = self.col.update_one(filter={'_id':object_id},update={'$unset':document.get('unset')})
        elif 'set' in document:
            result = self.col.update_one(filter={'_id':object_id},update={'$set':document.get('set')})
        else:
            result = self.col.update_one(filter={'_id':object_id},update=document)
        return result.modified_count
    

    def count(self,**filter)->int:
        return self.col.count_documents(filter)

    def find(self,size=10,offset=1,**filter):
        with self.col.find(filter=filter).skip(int(offset)-1).limit(int(size)) as cursor:
            for doc in cursor:
                yield doc
                
    def find_id(self,object_id):
        if not isinstance(object_id,ObjectId):
            object_id = convert_to_objectid(object_id)
            if not object_id:
                return {}
        return self.col.find_one(filter={'_id':object_id})

    def find_one(self,**filter):
        return self.col.find_one(filter)
    
    def find_for_total_detail(self,size=10,offset=1,**filter):
        data = {}
        data['total'] = self.col.count_documents(filter)
        cursor = self.col.find(filter).skip(int(offset)-1).limit(int(size))
        result = []
        for document in cursor:
            result.append(document)
        else:
            data['detail'] = result
        return data
    

    def polars_get_database(self,schema:Schema=None, skip=0, limit=100, **filter: dict):
        table = find_arrow_all(self.col, query=filter, schema=schema, skip=skip, limit=limit)
        return pl.from_arrow(table)
        






        







   
            


        
    
        
        
        
