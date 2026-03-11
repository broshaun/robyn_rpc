from robyn import Request,Robyn,SubRouter
from orjson import loads
from utils.middle import Rsp
import inspect



class CompatRouter:
    """
    国内环境兼容版路由器 (POST 语义补偿模式)
    职责：通过 X-HTTP-Method 头部实现 POST 隧道，转发至对应的 CRUD 方法。
    """
    def __init__(self,router:SubRouter,sub_path:str):

        self.request:Request = None
        @router.post(sub_path)
        @Rsp.response
        async def _(request: Request):
            method = request.headers.get('X-HTTP-Method').lower()
            if hasattr(self,method):
                result = getattr(self,method)(**self.get_kwargs(request))
                if inspect.isawaitable(result):
                    result = await result
                return result

        @router.get(sub_path)
        @Rsp.response
        async def _(request: Request):
            if hasattr(self,'get'):
                result = getattr(self,'get')(**self.get_kwargs(request))
                if inspect.isawaitable(result):
                    result = await result
                return result


    def get_kwargs(self,request:Request):
        '''获取请求参数'''
        self.request = request
        kwargs = {}

        for i,v in request.query_params.to_dict().items():
            kwargs[i] = v[0]
        
        content_type = str(request.headers.get("content-type")).lower()
        if content_type.startswith('application/json') and request.body:
            kwargs = loads(request.body)
        return kwargs
    




class Router:
    '''通用路由器'''
    def __init__(self,router:SubRouter,sub_path:str):
        self.request:Request = None
  
        if hasattr(self,'get'):
            @router.get(sub_path)
            @Rsp.response
            async def _(request: Request):
                result = getattr(self,'get')(**self.get_kwargs(request))
                if inspect.isawaitable(result):
                    result = await result
                return result
   
        if hasattr(self,'post'):
            @router.post(sub_path)
            @Rsp.response
            async def _(request: Request):
                result = getattr(self,'post')(**self.get_kwargs(request))
                if inspect.isawaitable(result):
                    result = await result
                return result
            
        if hasattr(self,'put'):
            @router.put(sub_path)
            @Rsp.response
            async def _(request: Request):
                result = getattr(self,'put')(**self.get_kwargs(request))
                if inspect.isawaitable(result):
                    result = await result
                return result
            
        if hasattr(self,'patch'):
            @router.patch(sub_path)
            @Rsp.response
            async def _(request: Request):
                result = getattr(self,'patch')(**self.get_kwargs(request))
                if inspect.isawaitable(result):
                    result = await result
                return result
            
        if hasattr(self,'delete'):
            @router.delete(sub_path)
            @Rsp.response
            async def _(request: Request):
                result = getattr(self,'delete')(**self.get_kwargs(request))
                if inspect.isawaitable(result):
                    result = await result
                return result
        
        if hasattr(self,'options'):
            @router.options(sub_path)
            @Rsp.response
            async def _(request: Request):
                result = getattr(self,'options')(**self.get_kwargs(request))
                if inspect.isawaitable(result):
                    result = await result
                return result


    def get_kwargs(self,request:Request):
        self.request = request
        self.token = request.headers.get('Authorization')
        kwargs = {}
        for i,v in request.query_params.to_dict().items():
            kwargs[i] = v[0]
        content_type = str(request.headers.get("content-type")).lower()
        if content_type.startswith('application/json'):
            kwargs = loads(request.body)
        return kwargs
    

class BlueRouter:
    def __init__(self,app:Robyn,prefix=""):
        self.app = app
        self.router = SubRouter(__name__,prefix)
    
    def include_views(self,views:dict[str, type]):
        for path in views:
            views[path](self.router,path)
        else:
            self.app.include_router(self.router)