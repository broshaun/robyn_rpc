from robyn import SubRouter,Request
from utils.middle import Rsp
import config
import os
import hashlib
from .server import PDFsS


router = SubRouter(__name__, prefix="/pdf")

@router.post('upload')
@Rsp.response
def post(request:Request):
    pdf = PDFsS()
    files = request.files
    if not request.files:
        Rsp.no_content('No file uploaded')

    for key in files:
        file_content = files[key]
        original_md5 = hashlib.md5(file_content).hexdigest()
        file_name = f"{original_md5}.pdf"
        existing_file = pdf.check_existing_file(file_name)
        if not existing_file:
            file_path = os.path.join(config.PDF, file_name)
            with open(file_path, "wb") as f:
                f.write(file_content)
    else:
        Rsp.ok(file_name,msg="上传成功")

@router.delete('md5')
@Rsp.response
def delete(request:Request):
    kwargs = request.json()
    file_name = kwargs.get('file_name')
    file_path = os.path.join(config.PDF, file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)
    Rsp.ok(data=file_name,msg="删除成功")

@router.get('list')
@Rsp.response
def get(request:Request):
    all_entries = []
    if os.path.exists(config.PDF):
        all_entries = os.listdir(config.PDF)
    Rsp.ok(data=all_entries,msg='文件列表')
  






    


    