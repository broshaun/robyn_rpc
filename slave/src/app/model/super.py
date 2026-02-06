from utils.middle import JWT
import config


class MGSuper():

    def __init__(self,collection_name):
        usr = JWT.get_user()
        self.uid = usr.get('uid',0)
        self.sub = usr.get('sub','...')
        self.alias = f'{self.sub}:{self.uid}'
        self.session = config.Session()
        self._hpmgo = config.MongoDB('super').open(collection_name)
        self._hpmgo.uid = self.uid

    @property
    def hpmgo(self):
        return self._hpmgo
    
    async def delete(self, id, *ids):
        ids_to_delete = (*id,*ids) if isinstance(id, (tuple,list)) else (id, *ids)
        rowcount = 0
        for i in ids_to_delete:
            rowcount += await self.hpmgo.delete_id(i)
        return rowcount
        
    async def update(self, id, *ids, **kwargs):
        ids_to_update =  (*id,*ids) if isinstance(id, (tuple,list)) else (id, *ids)
        lastid = []
        for i in ids_to_update:
            lastid.append(await self.hpmgo.update_one(i, **kwargs))
        return lastid
        
