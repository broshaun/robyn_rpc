from .mgops import MgoDB
from .hpmgo import CRUD
from .fsmgo import Files


class DBOpen(MgoDB):
    def open(self,collection_name):
        return CRUD(self,collection_name=collection_name)

    

class FSOpen(MgoDB):
    def open(self,collection_name):
        return Files(self,collection_name)
    







# 以下为示例代码
class MgoFS:
    # HOST = "mongo.service"
    HOST = "localhost"
    PORT = 27017
    DBUSER = 'root'
    DBPWD = 'aak123456'
    def __new__(cls,database):
        return FSOpen(host=cls.HOST,port=cls.PORT,user=cls.DBUSER,password=cls.DBPWD,database=database)
# 上传文件
async def upf(self,file_content):
    hpmgo = MgoFS('files').open('test')
    await hpmgo.put_file(file_content)

# 下载文件
async def down(self):
    from bson import ObjectId
    hpmgo = MgoFS('files').open('test')
    file_content = await hpmgo.get_file(ObjectId("693be928c5058d0f9fc0d6c2"))
    with open("downloaded_img.py", "wb") as f:
        f.write(file_content) 
            