from utils.middle import Rsp
from app.model.slave import MGSuper



class RegisterS():
    """子用户管理"""
    def __init__(self):
        self.obj = MGSuper("user")

    def create(self,email,pass_word,role=""):
        cnt = self.obj.hpmgo.count(email=email)
        if cnt > 0:
            Rsp.repeat("邮箱已注册")
        lastid = self.obj.hpmgo.insert_one(document=dict(email=email,pass_word=pass_word,role=role))
        Rsp.ok(lastid,msg='注册成功。')
    
    def delete(self,id):
        rowcount = self.obj.hpmgo.delete_id(id)
        Rsp.ok(rowcount)

    def modify(self,id,**kwargs):
        if 'phone' in kwargs:
            cnt = self.obj.hpmgo.count(phone=kwargs.get('phone'))
            if cnt > 0:
                Rsp.repeat("电话已注册")
        if 'email'in kwargs:
            cnt = self.obj.hpmgo.count(email=kwargs.get('email'))
            if cnt >0:
                Rsp.repeat("邮箱已注册")

        rowcount = self.obj.hpmgo.update_one_set(id,kwargs)
        Rsp.ok(rowcount)

    def find(self,id):
        da = self.obj.hpmgo.find_id(id)
        Rsp.ok(da)

    def browse(self,skip=0,limit=10,**filter):
        "查看子用户"
        # filter['creator'] = self.obj.uid
        data = self.obj.hpmgo.find_for_total_detail(filter=filter,skip=skip,limit=limit)
        Rsp.ok(data)
            
        
        



