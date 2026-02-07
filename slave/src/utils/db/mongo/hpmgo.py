from .mgops import Mongo
from bson import ObjectId,errors
import polars as pl

def convert_to_objectid(*ids):
    result = []
    for value in ids:
        if isinstance(value, ObjectId):
            result.append(value)
        else:
            try:
                result.append(ObjectId(value))
            except (errors.InvalidId, TypeError):
                continue
    return result


class CRUD(object):
    def __init__(self,mgo:Mongo, collection_name):
        self.uid = 0
        self.mgo = mgo
        self.collection_name = collection_name

    def drop(self):
        self.mgo.db[self.collection_name].drop()

    @property
    def collection(self):
        return self.mgo.db[self.collection_name]

    def insert_one(self, document):
        document["creator"] = self.uid
        return self.collection.insert_one(document).inserted_id
    
    def insert_many(self, documents):
        return self.collection.insert_many(documents).inserted_ids
    
    def delete_id(self, id):
        objs = convert_to_objectid(id)
        if objs:
            return self.collection.delete_one({"_id": objs[0]}).deleted_count
        return 0
    
    def delete_many(self, **filter):
        return self.collection.delete_many(filter).deleted_count

    def update_one_push(self, id, document:dict={}):
        objs = convert_to_objectid(id)
        if objs:
            return self.collection.update_one(filter={'_id':objs[0]},update={'$push':document}).modified_count
        return 0
    
    def update_one_pull(self, id, document:dict={}):
        objs = convert_to_objectid(id)
        if objs:
            return self.collection.update_one(filter={'_id':objs[0]},update={'$pull':document}).modified_count
        return 
    
    def update_one_set(self,id, document:dict={}):
        objs = convert_to_objectid(id)
        if objs:
            return self.collection.update_one(filter={'_id':objs[0]},update={'$set':document}).modified_count
        return 0
    
    def update_one_unset(self,id, document:dict={}):
        objs = convert_to_objectid(id)
        if objs:
            return self.collection.update_one(filter={'_id':objs[0]},update={'$unset':document}).modified_count
        return 0
    
    def replace_one(self,id, document:dict={}):
        objs = convert_to_objectid(id)
        if objs:
            return self.collection.update_one(filter={'_id':objs[0]},update=document).modified_count
        return 0

    def count(self,**filter)->int:
        return self.collection.count_documents(filter)

    def find(self, filter:dict, skip=0, limit=10,**kwargs)->pl.DataFrame:
        return self.mgo.aggregate_to_polars(self.collection,filter=filter,skip=skip,limit=limit,**kwargs)
    
    def find_id(self, id, **kwargs)->dict:
        objs = convert_to_objectid(id)
        if objs:
            for ss in self.mgo.aggregate_to_polars(self.collection,filter={'_id':objs[0]},**kwargs).iter_rows(named=True):
                return ss
        return dict()
        
    def find_ids(self, ids:list, **kwargs)->pl.DataFrame:
        objs = convert_to_objectid(*ids)
        return self.mgo.aggregate_to_polars(self.collection,filter={"_id": {"$in": objs}},**kwargs)

    def find_one(self, filter, **kwargs):
        for ss in self.mgo.aggregate_to_polars(self.collection,filter=filter,**kwargs).iter_rows(named=True):
            return ss
        else:
            return dict()

    def find_for_total_detail(self, filter:dict, skip=0, limit=10, **kwargs):
        data = {}
        data['total'] = self.collection.count_documents(filter)
        data['detail'] = self.find(filter, skip, limit, **kwargs)
        return data
    
        






        







   
            


        
    
        
        
        
