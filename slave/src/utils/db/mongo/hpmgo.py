from .mgops import MgoDB
from bson import ObjectId,errors
from copy import deepcopy


def convert_to_objectid(object_id:str):
    try:
        return ObjectId(object_id)
    except errors.InvalidId:
        return ObjectId()


class CRUD(object):
    def __init__(self,mgo:MgoDB,collection_name):
        self.uid = 0
        self.col = mgo.col(collection_name)

        
    @property
    async def count(self)->int:
        return await self.col.count_documents(filter={})
    
    async def count(self,**filter)->int:
        # filter:dict = deepcopy(filter)
        return await self.col.count_documents(filter)

    async def insert_one(self, document):
        document['creator'] = self.uid
        result = await self.col.insert_one(document)
        return result.inserted_id
    
    async def insert_many(self, documents):
        result = await self.col.insert_many(documents)
        return result.inserted_ids
    
    async def delete_id(self, object_id):
        if not isinstance(object_id,ObjectId):
            object_id = convert_to_objectid(object_id)
        result = await self.col.delete_one({'_id':object_id})
        return result.deleted_count
    
    async def delete_many(self, **filter):
        # filter:dict = deepcopy(filter)
        return await self.col.delete_many(filter)
    

    async def drop(self):
        await self.col.drop()

    async def update_one(self, object_id,document:dict={}):
        '''
        更新数据
        
        :param object_id: 指定修改的object_id.

        :document set 更新指定字段

        :document unset 删除指定字段

        :document push 向数组字段追加元素

        :document pull 从数组删除指定元素

        : document 没有指定操作符,覆盖当前数据
        '''
        if not isinstance(object_id,ObjectId):
            object_id = convert_to_objectid(object_id)

        if 'push' in document:
            result = await self.col.update_one(filter={'_id':object_id},update={'$push':document.get('push')})
        elif 'pull' in document:
            result = await self.col.update_one(filter={'_id':object_id},update={'$pull':document.get('pull')})
        elif 'unset' in document:
            result = await self.col.update_one(filter={'_id':object_id},update={'$unset':document.get('unset')})
        elif 'set' in document:
            result = await self.col.update_one(filter={'_id':object_id},update={'$set':document.get('set')})
        else:
            result = await self.col.update_one(filter={'_id':object_id},update=document)
        return result.modified_count

    async def find(self,size=10,offset=1,**filter):
        filter:dict = deepcopy(filter)
        async with self.col.find(filter=filter).skip(int(offset)-1).limit(int(size)) as cursor:
            async for doc in cursor:
                yield doc
                
    async def find_id(self,object_id):
        if not isinstance(object_id,ObjectId):
            object_id = convert_to_objectid(object_id)
            return await self.col.find_one(filter={'_id':object_id})

    async def find_one(self,**filter):
        return await self.col.find_one(filter=filter)
    
    async def find_for_total_detail(self,size=10,offset=1,**filter):
        data = {}
        data['total'] = await self.col.count_documents(filter=filter)
        cursor = self.col.find(filter).skip(int(offset)-1).limit(int(size))
        result = []
        async for document in cursor:
            result.append(document)
        else:
            data['detail'] = result
        return data






        







   
            


        
    
        
        
        
