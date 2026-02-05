from robyn import SubRouter,Request
from utils.middle import Rsp
import config
import os
import hashlib
from .server import VideosS


router = SubRouter(__name__, prefix="/video")

@router.post('upload')
@Rsp.response
def post(request:Request):
    video = VideosS()
    files = request.files
    if not request.files:
        Rsp.no_content('No file uploaded')

    for key in files:
        file_content = files[key]
        if not video.is_valid_mp4_header(file_content):
            Rsp.no_method(msg='只支持mp4格式上传')

        original_md5 = hashlib.md5(file_content).hexdigest()
        file_name = f"{original_md5}.mp4"
        existing_file = video.check_existing_file(file_name)
        if not existing_file:
            file_path = os.path.join(config.VIDEO, file_name)
            with open(file_path, "wb") as f:
                f.write(file_content)
    else:
        Rsp.ok(file_name,msg="上传成功")

@router.delete('md5')
@Rsp.response
def delete(request:Request):
    kwargs = request.json()
    file_name = kwargs.get('file_name')
    file_path = os.path.join(config.VIDEO, file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)
        Rsp.ok(data=file_name, msg="删除成功")

@router.get('list')
@Rsp.response
def get(request:Request):
    video_list = []
    if os.path.exists(config.VIDEO):
        video_list =  os.listdir(config.VIDEO)
    Rsp.ok(data=video_list, msg='Video file list')
