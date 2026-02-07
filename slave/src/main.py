from utils.middle import Routes
from app import app_user
from config import WebIP,DEBUG
import asyncio
from aiozmq import rpc
from bson import ObjectId

translation_table = {
    0: (ObjectId,
        lambda obj: obj.binary,
        lambda binary: ObjectId(binary)
    ),
}

class Views(Routes):
    def routes_set(self):
        self.routes[r'login/'] = app_user.LoginV
        self.routes[r'register/'] = app_user.RegisterV
        self.routes[r'roles/'] = app_user.RolesV

async def start_server():
    """启动RPC服务端"""
    server = await rpc.serve_rpc(
        Views(), 
        bind=f"tcp://{WebIP.HOST}:{WebIP.PORT}",
        # translation_table=translation_table
    )
    print(f"RPC服务端启动, 监听 {WebIP.HOST}:{WebIP.PORT} ...")
    await server.wait_closed()  # 保持服务运行（等待关闭信号）


if __name__ == "__main__":
    if DEBUG:
        print('当前为调试模式 ...')
    else:
        print('当前为线上模式 ...')
    asyncio.run(start_server())
