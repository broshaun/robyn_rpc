from utils.middle import Rsp,RqsH


class TestV(RqsH):
    async def get(self,**kwargs):
        Rsp.ok('Wecome RobynRPC')

  
