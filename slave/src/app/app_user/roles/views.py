from  utils.middle import JWT,RqsH
from .server import RolesS


class RolesV(RqsH):

    @JWT.jwt_sign_auth
    async def put(self,**argument):
        """创建角色"""
        css = RolesS()
        await css.create(**argument)

    @JWT.jwt_sign_auth
    async def delete(self,**argument):
        """角色删除"""
        css = RolesS()
        await css.delete(**argument)
    
    @JWT.jwt_sign_auth
    async def patch(self,**argument):
        """角色修改"""
        css = RolesS()
        await css.modify(**argument)

    @JWT.jwt_sign_auth
    async def post(self,**argument):
        """角色列表"""
        css = RolesS()
        await css.browse(**argument)

    @JWT.jwt_sign_auth
    async def get(self,**argument):
        """角色信息"""
        css = RolesS()
        await css.find(**argument)


