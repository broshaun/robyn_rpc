from utils.middle import CompatRouter,Rsp
from utils.rpc import RPClient
from config import RPC


class RPCProxyView(CompatRouter):
    '''
    RPC 代理兼容方案
    职责：接收 HTTP 请求，通过 X-HTTP-Method 识别意图，并透明转发至远端 RPC 服务
    RPC 穿透网关视图
    实现逻辑：/rpc/:rpc_server/*sub_path -> 目标 RPC Server
    '''
    async def post(self,method,**kwargs):
        rpc_server = self.request.path_params["rpc_server"]
        path = self.request.path_params["sub_path"]
        headers = {'Authorization':self.request.headers.get('Authorization')}
        rpclient = RPClient(await RPC.HOST(alias=rpc_server))
        await rpclient.run(path,method,headers,kwargs)

    async def get(self,**kwargs):
        rpc_server = self.request.path_params["rpc_server"]
        path = self.request.path_params["sub_path"]
        headers = {'Authorization':self.request.headers.get('Authorization')}
        rpclient = RPClient(await RPC.HOST(alias=rpc_server))
        await rpclient.run(path,'get',headers,kwargs)

