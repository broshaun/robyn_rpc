from utils.middle import Rsp,CompatRouter


class TestV(CompatRouter):
    async def get(self,**kwargs):
        Rsp.ok('Robyn is OK !!!')


class PingV(CompatRouter):
    async def get(self,**kwargs):
        Rsp.ok('Pong !!!')

    async def post(self,**kwargs):
        Rsp.ok('Pong !!!')

    async def delete(self,**kwargs):
        Rsp.ok('Pong !!!')

    async def options(self,**kwargs):
        Rsp.ok('Pong !!!')

    async def put(self,**kwargs):
        Rsp.ok('Pong !!!')
    
    async def patch(self,**kwargs):
        Rsp.ok('Pong !!!')

  
