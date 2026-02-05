import aiozmq.rpc
from utils.middle import Rsp
# from bson import ObjectId


# translation_table = {
#     0: (ObjectId,
#         lambda obj: obj.binary,
#         lambda binary: ObjectId(binary)
#     ),
# }

class RPClient():
    '''RPC客户端, 用于与RPC服务端通信\n
    rpcserver: RPC地址
    '''
    def __init__(self,rpcserver):
        if not rpcserver:
            Rsp.rpc(msg=f'未设定RPCServer地址:[{rpcserver}]')
        self.rpcserver = rpcserver

    async def run(self, path:str,method:str,headers:dict,kwargs:dict):
        """调用RPC服务端的echo方法
            path: RPC服务的路由
            method: 路由方法 get | post | put ...
            headers: 传递头文件
            kwargs: 传递访问参数
        """ 
        client = await aiozmq.rpc.connect_rpc(
            connect=self.rpcserver,
            # translation_table=translation_table
        )
        async with client:
            result = await client.call.echo(path,method,headers,kwargs)
            Rsp.from_raw_json(result)