from robyn import Request,Robyn,SubRouter
from orjson import loads
from utils.middle import Rsp
import inspect


class Router:
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
    def __init__(self,app:Robyn,prefix:str):
        self.app = app
        self.router = SubRouter(__name__,prefix)
    
    def include_views(self,views:dict[str, type]):
        for path in views:
            views[path](self.router,path)
        else:
            self.app.include_router(self.router)