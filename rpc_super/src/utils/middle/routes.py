import asyncio
from aiozmq import rpc
from typing import Dict, Callable, Awaitable
from .answer import Rsp


class Routes(rpc.AttrHandler):
    '路由基础类'
    
    def __init__(self):
        super().__init__()  # 初始化父类AttrHandler
        self.routes: Dict[str, Callable] = {} # 存储路由映射关系
        self.routes_set() # 注册路由

    def routes_set(self):
        pass
    
    @rpc.method
    @Rsp.response
    async def echo(self,path:str,method:str,headers:dict,kwargs:dict):
        '''说明：
        执行 fn_method 方法。
        fn_method 的方法也可以是异步的，当返回结果是为执行的 <coroutine object> 则使用 result = await result 执行。
        返回 method 的结果
        '''
        views = self.routes.get(path)
        if views is None:
            Rsp.not_found(data=path)
        obj = views(headers)
        fn_method = method.lower()
        if not hasattr(obj, fn_method):
            Rsp.no_method(msg=f'{fn_method}方法不存在')
        result = getattr(obj, fn_method)(**kwargs) # 执行obj对象的fn_method方法
        if isinstance(result, Awaitable):
            return await result
            
    @rpc.method
    async def test(self):
        await asyncio.sleep(0.1)
        return f'Wecome RPCOfficial !!!'








