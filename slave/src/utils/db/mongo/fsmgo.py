from .mgops import MgoDB



class Files(object):
    def __init__(self,mgo:MgoDB,collection_name):
        self.uid = 0
        self.fs = mgo.fs(collection_name)

    async def find_files(self,filename):
        files = await self.fs.find({"filename": filename})
        return files
    
    async def delete_file(self,file_id):
        return await self.fs.delete(file_id)
    
    async def get_file(self,file_id):
        file = await self.fs.get(file_id)
        file_data = await file.read()
        return file_data
    
    async def put_file(self,data):
        file_id = await self.fs.put(data)
        print('file_id',file_id)
        return file_id
    



            