from utils.middle import Rsp
from app.model.slave import MGSuper



class RolesS():
    """角色管理"""
    def __init__(self):
        self.obj = MGSuper("roles")

    def create(self,role,permission):
        cnt = self.obj.hpmgo.count(**{"role":role})
        if cnt > 0:
            Rsp.repeat("角色已存在")
        lastid = self.obj.hpmgo.insert_one(document=dict(role=role,permission=permission))
        Rsp.ok(lastid,msg='添加角色成功')
    
    def delete(self,id):
        rowcount = self.obj.hpmgo.delete_id(id)
        Rsp.ok(rowcount)

    def modify(self,id,**kwargs):
        if 'role'in kwargs:
            cnt = self.obj.hpmgo.count(**{"role":kwargs.get('role')})
            if cnt > 0:
                Rsp.repeat("角色已存在")
        rowcount = self.obj.hpmgo.update_one_set(id,document=kwargs)
        Rsp.ok(rowcount)

    def find(self,id):
        data = self.obj.hpmgo.find_id(id)
        Rsp.ok(data)

    def browse(self,skip=0,limit=10,**kwargs):
        data = self.obj.hpmgo.find_for_total_detail(filter=kwargs,skip=skip,limit=limit)
        Rsp.ok(data)
            
        
        



