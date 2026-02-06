from utils.middle import Rsp,JWT
from app.model.slave import MGSuper



class LoginS():
    """用户登陆"""
    def __init__(self):
        self.obj = MGSuper('user')
        self.obj2 = MGSuper('roles')

    def sign_in(self,email,pass_word):
        '''用户登陆'''
        df = self.obj.hpmgo.polars_get_database()
        return df
        # cursor = self.obj.hpmgo.find(email=email)
        # for document in cursor:
        #     uid = document.get('uid',0)
        #     oid = document.get('_id')
        #     if pass_word == document.get('pass_word'):
        #         self.obj.session.store(alias=f'super:{uid}', value=str(oid) ,ex=100000)
        #         data = {}
        #         data['login_token'] = JWT.jwt_login(uid,sub='super',eff=100000)
        #         data['login_expired'] = 100000
        #         data['refresh_token'] = JWT.jwt_refresh(uid, eff=1000000)
        #         data['user'] = {'sub': 'super', 'uid': uid}
        #         data['user'].update(self.obj2.hpmgo.find_one(role=document.get('role')))
        #         # 1/0
        #         Rsp.ok('data')
        # else:
        #     Rsp.login_fail()

    def sign_out(self):
        '''用户登出；清除缓存'''
        Rsp.ok(data=self.obj.session.delete(self.obj.alias),msg="注销成功")

    def sign_new(self,refresh_token):
        '''刷新验证；获取新的Token'''
        data = dict()
        payload = JWT.jwt_decode(refresh_token)
        if payload['sub'] != "refresh":
            Rsp.invalid_token()
        data['login_token'] = JWT.jwt_login(uid=payload["uid"],sub="super",eff=100000)
        data['login_expired'] = 100000
        Rsp.ok(data)
    
    async def sign_info(self):
        '登陆信息获取'
        data = dict()
        object_id = self.obj.session.load(self.obj.alias)
        data = await self.obj.hpmgo.find_id(object_id)
        Rsp.ok(data)

    async def sign_password(self,pass_word):
        '修改登录密码'
        object_id = self.obj.session.load(self.obj.alias)
        modified = await self.obj.hpmgo.update_one(object_id,document={'set':{'pass_word':pass_word}})
        Rsp.ok(modified,msg="密码修改成功")
