from utils.middle import Rsp
from app.model.slave import MGSuper



class RolesS():
    """角色管理"""
    def __init__(self):
        self.obj = MGSuper("roles")

    async def create(self,role,permission):
        cnt = await self.obj.hpmgo.count({"role":role})
        if cnt > 0:
            Rsp.repeat("角色已存在")
        lastid = await self.obj.hpmgo.insert(role=role,permission=permission)
        Rsp.ok(lastid,msg='添加角色成功')
    
    async def delete(self,id):
        rowcount = await self.obj.hpmgo.delete_id(id)
        Rsp.ok(rowcount)

    async def modify(self,id,**kwargs):
        if 'role'in kwargs:
            cnt = await self.obj.hpmgo.count({"role":kwargs.get('role')})
            if cnt > 0:
                Rsp.repeat("角色已存在")
        rowcount = await self.obj.hpmgo.update_one(id,document={'set':kwargs})
        Rsp.ok(rowcount)

    async def find(self,id):
        data = await self.obj.hpmgo.find_id(id)
        Rsp.ok(data)

    async def browse(self,**kwargs):
        data = await self.obj.hpmgo.find_for_total_detail(**kwargs)
        Rsp.ok(data)
            
        
        



