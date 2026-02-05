from utils.middle import RqsH
from utils.rpc import RPClient
from config import RPC


class RPCView(RqsH):
    async def post(self,**kwargs):
        rpc_server = self.request.path_params["rpc_server"]
        path = self.request.path_params["sub_path"]
        method = self.request.method.lower()
        headers = {'Authorization':self.request.headers.get('Authorization')}
        rpclient = RPClient(await RPC.RPCServer(alias=rpc_server))
        await rpclient.run(path,method,headers,kwargs)

    async def delete(self,**kwargs):
        rpc_server = self.request.path_params["rpc_server"]
        path = self.request.path_params["sub_path"]
        method = self.request.method.lower()
        headers = {'Authorization':self.request.headers.get('Authorization')}
        rpclient = RPClient(await RPC.RPCServer(alias=rpc_server))
        await rpclient.run(path,method,headers,kwargs)

    async def options(self,**kwargs):
        rpc_server = self.request.path_params["rpc_server"]
        path = self.request.path_params["sub_path"]
        method = self.request.method.lower()
        headers = {'Authorization':self.request.headers.get('Authorization')}
        rpclient = RPClient(await RPC.RPCServer(alias=rpc_server))
        await rpclient.run(path,method,headers,kwargs)

    async def get(self,**kwargs):
        rpc_server = self.request.path_params["rpc_server"]
        path = self.request.path_params["sub_path"]
        method = self.request.method.lower()
        headers = {'Authorization':self.request.headers.get('Authorization')}
        rpclient = RPClient(await RPC.RPCServer(alias=rpc_server))
        await rpclient.run(path,method,headers,kwargs)

    async def put(self,**kwargs):
        rpc_server = self.request.path_params["rpc_server"]
        path = self.request.path_params["sub_path"]
        method = self.request.method.lower()
        headers = {'Authorization':self.request.headers.get('Authorization')}
        rpclient = RPClient(await RPC.RPCServer(alias=rpc_server))
        await rpclient.run(path,method,headers,kwargs)
    
    async def patch(self,**kwargs):
        rpc_server = self.request.path_params["rpc_server"]
        path = self.request.path_params["sub_path"]
        method = self.request.method.lower()
        headers = {'Authorization':self.request.headers.get('Authorization')}
        rpclient = RPClient(await RPC.RPCServer(alias=rpc_server))
        await rpclient.run(path,method,headers,kwargs)
