from utils.middle import Rsp,CompatRouter


class TestV(CompatRouter):
    async def get(self,**kwargs):
        Rsp.ok('Robyn is OK !!!')

  
