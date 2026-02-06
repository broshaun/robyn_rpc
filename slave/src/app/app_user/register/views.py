from  utils.middle import JWT,RqsH
from .server import RegisterS





class RegisterV(RqsH):

    @JWT.jwt_sign_auth
    async def post(self,**argument):
        """用户注册"""
        css = RegisterS()
        await css.create(**argument)

    @JWT.jwt_sign_auth
    async def delete(self,**argument):
        """用户删除"""
        css = RegisterS()
        await css.delete(**argument)
    
    @JWT.jwt_sign_auth
    async def put(self,**argument):
        """用户修改"""
        css = RegisterS()
        await css.modify(**argument)

    @JWT.jwt_sign_auth
    async def get(self,**argument):
        """注册用户查看"""
        css = RegisterS()
        await css.browse(**argument)

    @JWT.jwt_sign_auth
    async def options(self,**argument):
        """用户信息"""
        css = RegisterS()
        await css.find(**argument)


