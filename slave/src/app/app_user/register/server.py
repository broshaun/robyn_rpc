from utils.middle import Rsp
from app.model.super import MGSuper



class RegisterS():
    """子用户管理"""
    def __init__(self):
        self.obj = MGSuper("user")

    async def create(self,email,pass_word,role=""):
        cnt = await self.obj.hpmgo.count(email=email)
        if cnt > 0:
            Rsp.repeat("邮箱已注册")
        uid = await self.obj.hpmgo.count()
        lastid = await self.obj.hpmgo.insert_one(document=dict(email=email,pass_word=pass_word,uid=(uid+1),role=role))
        Rsp.ok(lastid,msg='注册成功。')
    
    async def delete(self,id):
        rowcount = await self.obj.delete(id)
        Rsp.ok(rowcount)

    async def modify(self,id,**kwargs):
        if 'phone' in kwargs:
            cnt = await self.obj.hpmgo.count(phone=kwargs.get('phone'))
            if cnt > 0:
                Rsp.repeat("电话已注册")
        if 'email'in kwargs:
            cnt = await self.obj.hpmgo.count(email=kwargs.get('email'))
            if cnt >0:
                Rsp.repeat("邮箱已注册")

        rowcount = await self.obj.hpmgo.update_one(id,document={'set':kwargs})
        Rsp.ok(rowcount)

    async def find(self,id):
        data = await self.obj.hpmgo.find_id(id)
        Rsp.ok(data)

    async def browse(self,**kwargs):
        "查看子用户"
        kwargs['creator'] = self.obj.uid
        data = await self.obj.hpmgo.find_for_total_detail(**kwargs)
        Rsp.ok(data)
            
        
        



