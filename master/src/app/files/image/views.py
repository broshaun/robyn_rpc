from utils.middle import Rsp,RqsH
import config
import os
import hashlib
from .server import ImgasS


class ImgesV(RqsH):
    def get(self,**kwargs):
        data = []
        if os.path.exists(config.IMGS):
            data = os.listdir(config.IMGS)
        Rsp.ok(data)

    def put(self,**kwargs):
        imgs = ImgasS()
        files = self.request.files
        if not files:
            Rsp.no_content('No file uploaded')
        for file_name in files:
            file_content = files[file_name]
            original_md5 = hashlib.md5(file_content).hexdigest()
            new_file_name = f"{original_md5}.jpg"
            if not imgs.check_existing_file(new_file_name):
                file_path = os.path.join(config.IMGS, new_file_name)
                with open(file_path, "wb") as f:
                    compressed_content = imgs.convert_to_jpg(file_content)
                    f.write(compressed_content)
        else:
            Rsp.ok(data=new_file_name,msg="上传成功")
        Rsp.keynull()

    def delete(self,**kwargs):
        file_name = kwargs.get('file_name')
        file_path = os.path.join(config.IMGS, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
        Rsp.ok(data=file_name,msg="删除成功")




