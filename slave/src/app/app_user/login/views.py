from utils.middle import JWT,Rsp,RqsH
from .server import LoginS

 
class LoginV(RqsH):

    async def post(self,**kwargs):
        '用户登陆'
        css = LoginS()
        await css.sign_in(**kwargs)
        
    @JWT.jwt_sign_auth
    def delete(self,**kwargs):
        '登陆注销'
        css = LoginS()
        css.sign_out(**kwargs)
    
    @JWT.jwt_sign_auth
    def options(self,**kwargs):
        '刷新验证'
        css = LoginS()
        css.sign_new(**kwargs)

    @JWT.jwt_sign_auth
    async def get(self,**kwargs):
        '登录信息'
        css = LoginS()
        await css.sign_info(**kwargs)

    @JWT.jwt_sign_auth
    async def put(self,**kwargs):
        '修改登录密码'
        css = LoginS()
        await css.sign_password(**kwargs)
        


